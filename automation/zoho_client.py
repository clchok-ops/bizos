"""
Zoho CRM API Client for BizOS Kaizen Architecture
==================================================
Handles authentication, token refresh, and API calls with retry logic.

Follows GLOBAL_STANDARDS.md:
- G-API-001: Retry with exponential backoff
- G-ERR-001: Try/catch with meaningful logging
- G-ERR-002: Fail loudly, not silently

Usage:
    from zoho_client import ZohoClient

    client = ZohoClient()
    deals = client.get_deals(criteria="Stage:equals:Qualification")
"""

import os
import time
import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, Any, List

import requests
from dotenv import load_dotenv

# Configure logging (G-ERR-002: Fail loudly)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ZohoAPIError(Exception):
    """Custom exception for Zoho API errors"""
    def __init__(self, message: str, status_code: int = None, response: dict = None):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)


class ZohoClient:
    """
    Zoho CRM API client with automatic token refresh and retry logic.
    """

    # API endpoints
    TOKEN_URL = "https://accounts.zoho.com/oauth/v2/token"
    API_BASE = "https://www.zohoapis.com/crm/v2"  # v2 works without explicit fields

    # Retry configuration (G-API-001)
    MAX_RETRIES = 3
    INITIAL_BACKOFF = 1  # seconds
    MAX_BACKOFF = 30  # seconds

    def __init__(self, env_path: str = None):
        """
        Initialize the Zoho client.

        Args:
            env_path: Path to .env file. Defaults to ~/.bizos/.env
        """
        # Load environment variables
        if env_path:
            load_dotenv(env_path)
        else:
            # Default locations to check
            default_paths = [
                Path.home() / ".bizos" / ".env",
                Path(__file__).parent / ".env",
            ]
            for path in default_paths:
                if path.exists():
                    load_dotenv(path)
                    break

        # Load credentials
        self.client_id = os.getenv("ZOHO_CLIENT_ID")
        self.client_secret = os.getenv("ZOHO_CLIENT_SECRET")
        self.refresh_token = os.getenv("ZOHO_REFRESH_TOKEN")

        # Validate credentials (G-ERR-002: Fail loudly if missing)
        if not all([self.client_id, self.client_secret, self.refresh_token]):
            missing = []
            if not self.client_id: missing.append("ZOHO_CLIENT_ID")
            if not self.client_secret: missing.append("ZOHO_CLIENT_SECRET")
            if not self.refresh_token: missing.append("ZOHO_REFRESH_TOKEN")
            raise ValueError(f"Missing required credentials: {', '.join(missing)}")

        # Token management
        self._access_token = None
        self._token_expiry = None

        logger.info("ZohoClient initialized")

    def _get_access_token(self) -> str:
        """
        Get a valid access token, refreshing if necessary.

        Returns:
            Valid access token string
        """
        # Check if current token is still valid (with 5 min buffer)
        if self._access_token and self._token_expiry:
            if datetime.now() < self._token_expiry - timedelta(minutes=5):
                return self._access_token

        # Refresh the token
        logger.info("Refreshing access token...")

        try:
            response = requests.post(
                self.TOKEN_URL,
                data={
                    "grant_type": "refresh_token",
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "refresh_token": self.refresh_token,
                },
                timeout=30
            )
            response.raise_for_status()

            data = response.json()

            if "error" in data:
                raise ZohoAPIError(
                    f"Token refresh failed: {data.get('error')}",
                    response=data
                )

            self._access_token = data["access_token"]
            expires_in = data.get("expires_in", 3600)
            self._token_expiry = datetime.now() + timedelta(seconds=expires_in)

            logger.info(f"Token refreshed, expires in {expires_in}s")
            return self._access_token

        except requests.RequestException as e:
            # G-ERR-002: Fail loudly
            logger.error(f"Token refresh request failed: {e}")
            raise ZohoAPIError(f"Token refresh request failed: {e}")

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Dict = None,
        json_data: Dict = None,
        retry_count: int = 0
    ) -> Dict[str, Any]:
        """
        Make an API request with retry logic (G-API-001).

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint (e.g., "/Deals")
            params: Query parameters
            json_data: JSON body data
            retry_count: Current retry attempt

        Returns:
            API response as dictionary
        """
        url = f"{self.API_BASE}{endpoint}"
        headers = {
            "Authorization": f"Zoho-oauthtoken {self._get_access_token()}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json_data,
                timeout=60
            )

            # Log response for debugging (G-API-003)
            logger.debug(f"{method} {endpoint} -> {response.status_code}")

            # Handle rate limiting (G-API-001: retry with backoff)
            if response.status_code == 429:
                if retry_count < self.MAX_RETRIES:
                    backoff = min(
                        self.INITIAL_BACKOFF * (2 ** retry_count),
                        self.MAX_BACKOFF
                    )
                    logger.warning(f"Rate limited, retrying in {backoff}s...")
                    time.sleep(backoff)
                    return self._request(method, endpoint, params, json_data, retry_count + 1)
                else:
                    raise ZohoAPIError("Rate limit exceeded after max retries", 429)

            # Handle token expiry
            if response.status_code == 401:
                logger.warning("Token expired, refreshing...")
                self._access_token = None  # Force refresh
                if retry_count < 1:
                    return self._request(method, endpoint, params, json_data, retry_count + 1)
                else:
                    raise ZohoAPIError("Authentication failed after token refresh", 401)

            # Handle server errors with retry
            if response.status_code >= 500:
                if retry_count < self.MAX_RETRIES:
                    backoff = min(
                        self.INITIAL_BACKOFF * (2 ** retry_count),
                        self.MAX_BACKOFF
                    )
                    logger.warning(f"Server error {response.status_code}, retrying in {backoff}s...")
                    time.sleep(backoff)
                    return self._request(method, endpoint, params, json_data, retry_count + 1)
                else:
                    raise ZohoAPIError(
                        f"Server error after max retries",
                        response.status_code,
                        response.json() if response.text else None
                    )

            # Handle client errors
            if response.status_code >= 400:
                error_data = response.json() if response.text else {}
                raise ZohoAPIError(
                    f"API error: {error_data.get('message', response.status_code)}",
                    response.status_code,
                    error_data
                )

            return response.json() if response.text else {}

        except requests.RequestException as e:
            # G-ERR-001: Meaningful error logging
            logger.error(f"Request failed: {method} {endpoint} - {e}")

            # Retry on connection errors (G-API-001)
            if retry_count < self.MAX_RETRIES:
                backoff = min(
                    self.INITIAL_BACKOFF * (2 ** retry_count),
                    self.MAX_BACKOFF
                )
                logger.warning(f"Connection error, retrying in {backoff}s...")
                time.sleep(backoff)
                return self._request(method, endpoint, params, json_data, retry_count + 1)
            else:
                raise ZohoAPIError(f"Request failed after max retries: {e}")

    # ==================== CRM Module Methods ====================

    def get_deals(
        self,
        criteria: str = None,
        fields: List[str] = None,
        page: int = 1,
        per_page: int = 200
    ) -> Dict[str, Any]:
        """
        Get deals from CRM.

        Args:
            criteria: COQL criteria string (e.g., "Stage:equals:Qualification")
            fields: List of fields to return
            page: Page number
            per_page: Records per page (max 200)

        Returns:
            API response with deals data
        """
        params = {
            "page": page,
            "per_page": per_page,
        }

        if fields:
            params["fields"] = ",".join(fields)

        if criteria:
            params["criteria"] = f"({criteria})"

        return self._request("GET", "/Deals", params=params)

    def search_deals(self, criteria: str, fields: List[str] = None) -> Dict[str, Any]:
        """
        Search deals using COQL criteria.

        Args:
            criteria: COQL criteria (e.g., "((Stage:equals:Qualification)and(Amount:greater_than:50000))")
            fields: List of fields to return

        Returns:
            API response with matching deals
        """
        params = {"criteria": criteria}
        if fields:
            params["fields"] = ",".join(fields)

        return self._request("GET", "/Deals/search", params=params)

    def get_deal(self, deal_id: str) -> Dict[str, Any]:
        """Get a single deal by ID."""
        return self._request("GET", f"/Deals/{deal_id}")

    def update_deal(self, deal_id: str, data: Dict) -> Dict[str, Any]:
        """Update a deal."""
        return self._request("PUT", f"/Deals/{deal_id}", json_data={"data": [data]})

    def get_contacts(
        self,
        criteria: str = None,
        fields: List[str] = None,
        page: int = 1,
        per_page: int = 200
    ) -> Dict[str, Any]:
        """Get contacts from CRM."""
        params = {"page": page, "per_page": per_page}
        if fields:
            params["fields"] = ",".join(fields)
        if criteria:
            params["criteria"] = f"({criteria})"
        return self._request("GET", "/Contacts", params=params)

    def get_users(self) -> Dict[str, Any]:
        """Get all CRM users."""
        return self._request("GET", "/users")

    def get_modules(self) -> Dict[str, Any]:
        """Get all available modules."""
        return self._request("GET", "/settings/modules")

    def get_fields(self, module: str) -> Dict[str, Any]:
        """Get fields for a module."""
        return self._request("GET", f"/settings/fields?module={module}")

    # ==================== Task Methods (for Alerts) ====================

    def create_task(
        self,
        subject: str,
        due_date: str = None,
        priority: str = "Normal",
        owner_id: str = None,
        related_to: Dict = None,
        description: str = None
    ) -> Dict[str, Any]:
        """
        Create a task (for Kaizen alerts).

        Args:
            subject: Task subject
            due_date: Due date (YYYY-MM-DD)
            priority: "High", "Normal", "Low"
            owner_id: Assign to user ID
            related_to: {"module": "Deals", "id": "123"}
            description: Task description

        Returns:
            Created task data
        """
        task_data = {
            "Subject": subject,
            "Priority": priority,
        }

        if due_date:
            task_data["Due_Date"] = due_date
        if owner_id:
            task_data["Owner"] = {"id": owner_id}
        if related_to:
            task_data["What_Id"] = {"id": related_to["id"]}
            task_data["$se_module"] = related_to["module"]
        if description:
            task_data["Description"] = description

        return self._request("POST", "/Tasks", json_data={"data": [task_data]})

    # ==================== Utility Methods ====================

    def test_connection(self) -> bool:
        """
        Test the API connection.

        Returns:
            True if connection successful
        """
        try:
            result = self.get_deals(per_page=1)
            deals = result.get("data", [])
            logger.info(f"Connection successful! Can access Deals module.")
            return True
        except Exception as e:
            logger.error(f"Connection test failed: {e}")
            return False

    def coql_query(self, query: str) -> Dict[str, Any]:
        """
        Execute a COQL (CRM Object Query Language) query.

        Args:
            query: COQL query string

        Returns:
            Query results

        Example:
            client.coql_query("SELECT Deal_Name, Amount, Stage FROM Deals WHERE Amount > 50000")
        """
        return self._request("POST", "/coql", json_data={"select_query": query})


# Quick test when run directly
if __name__ == "__main__":
    print("Testing Zoho client...")
    try:
        client = ZohoClient()
        if client.test_connection():
            print("SUCCESS: Zoho API connection working!")
        else:
            print("FAILED: Could not connect to Zoho API")
    except Exception as e:
        print(f"ERROR: {e}")
