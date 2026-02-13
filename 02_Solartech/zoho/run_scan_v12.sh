#!/bin/bash
# WF-ZOHO-DEPLOY v1.2 Enhanced Scan — run from Mac
# Scans: blueprints, workflow_rules, assignment_rules, scoring_rules, wizards, webhooks, field_updates for ALL 11 modules

OUTPUT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_FILE="$OUTPUT_DIR/scan_v12_results.json"

echo "Running WF-ZOHO-DEPLOY v1.2 enhanced scan..."
echo "This will take ~60-120 seconds (72+ API calls to Zoho)..."

curl -s -X POST "https://n8n-production-f0e6.up.railway.app/webhook/zoho-deploy" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: dpk-zoho-4a7c2e9f1b5d8h30" \
  -d '{"action":"scan","description":"v1.2 enhanced scan - full enforcement coverage"}' \
  -o "$OUTPUT_FILE"

if [ $? -eq 0 ] && [ -s "$OUTPUT_FILE" ]; then
  SIZE=$(wc -c < "$OUTPUT_FILE" | tr -d ' ')
  echo "Scan complete! Results saved to: $OUTPUT_FILE ($SIZE bytes)"
  # Quick summary
  python3 -c "
import json
with open('$OUTPUT_FILE') as f:
    d = json.load(f)
print(f\"Status: {d.get('status','?')}\")
if d.get('response_data',{}).get('summary'):
    s = d['response_data']['summary']
    print(f\"Modules: {s.get('modules_scanned','?')}, API calls: {s.get('api_calls','?')}, Version: {s.get('scan_version','?')}\")
" 2>/dev/null
else
  echo "ERROR: Scan failed. Check network connectivity."
fi
