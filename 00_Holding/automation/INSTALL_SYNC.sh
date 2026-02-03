#!/bin/bash
# One-command installer for cto-brain sync
# Run: bash ~/Library/Mobile\ Documents/com~apple~CloudDocs/BizOS/00_Holding/automation/INSTALL_SYNC.sh

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "📦 Installing cto-brain sync..."

# Create directories
mkdir -p ~/Automation/logs

# Copy sync script
cp "$SCRIPT_DIR/sync_cto_brain.sh" ~/Automation/
chmod +x ~/Automation/sync_cto_brain.sh
echo "✅ Sync script installed"

# Copy and load launchd plist
cp "$SCRIPT_DIR/com.user.sync-cto-brain.plist" ~/Library/LaunchAgents/

# Unload if already loaded (ignore errors)
launchctl unload ~/Library/LaunchAgents/com.user.sync-cto-brain.plist 2>/dev/null || true

# Load the watcher
launchctl load ~/Library/LaunchAgents/com.user.sync-cto-brain.plist
echo "✅ File watcher installed and running"

# Verify
if launchctl list | grep -q "cto-brain"; then
    echo "✅ Sync automation active!"
    echo ""
    echo "📍 Files installed:"
    echo "   ~/Automation/sync_cto_brain.sh"
    echo "   ~/Library/LaunchAgents/com.user.sync-cto-brain.plist"
    echo ""
    echo "📋 Logs at: ~/Automation/logs/cto_brain_sync.log"
else
    echo "❌ Something went wrong. Check launchctl output."
fi
