#!/bin/bash
# sync_cto_brain.sh
# Auto-sync cto-brain folder to GitHub (mirrors bizos pattern)
# Place in ~/Automation/ and make executable: chmod +x sync_cto_brain.sh

CTO_BRAIN_PATH="$HOME/Library/Mobile Documents/com~apple~CloudDocs/cto-brain"
LOG_FILE="$HOME/Automation/logs/cto_brain_sync.log"

# Create log directory if needed
mkdir -p "$(dirname "$LOG_FILE")"

# Log timestamp
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Sync triggered" >> "$LOG_FILE"

cd "$CTO_BRAIN_PATH" || {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: Cannot cd to $CTO_BRAIN_PATH" >> "$LOG_FILE"
    exit 1
}

# Check for changes
if [[ -n $(git status --porcelain) ]]; then
    # Stage all changes
    git add -A

    # Commit with timestamp
    git commit -m "Auto-sync: $(date '+%Y-%m-%d %H:%M')" >> "$LOG_FILE" 2>&1

    # Push to remote
    git push >> "$LOG_FILE" 2>&1

    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Changes committed and pushed" >> "$LOG_FILE"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] No changes detected" >> "$LOG_FILE"
fi
