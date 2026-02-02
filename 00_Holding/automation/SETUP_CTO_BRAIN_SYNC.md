# cto-brain Auto-Sync Setup

Mirrors the bizos auto-sync pattern for cto-brain.

## Quick Setup (5 steps)

### 1. Clone cto-brain to iCloud (one-time)
```bash
cd ~/iCloud  # or wherever your iCloud Drive folder is
git clone https://github.com/YOUR_USERNAME/cto-brain.git
```

### 2. Copy sync script
```bash
cp ~/iCloud/BizOS/00_Holding/automation/sync_cto_brain.sh ~/Automation/
chmod +x ~/Automation/sync_cto_brain.sh
```

### 3. Update paths in both files
Edit `sync_cto_brain.sh` and `com.user.sync-cto-brain.plist`:
- Replace `YOUR_USERNAME` with your actual Mac username
- Adjust `iCloud` path if different (e.g., `Library/Mobile Documents/com~apple~CloudDocs`)

### 4. Install launchd watcher
```bash
# Edit plist first to replace YOUR_USERNAME
cp ~/iCloud/BizOS/00_Holding/automation/com.user.sync-cto-brain.plist ~/Library/LaunchAgents/

# Load the watcher
launchctl load ~/Library/LaunchAgents/com.user.sync-cto-brain.plist
```

### 5. Test it
```bash
# Make a change in cto-brain
cd ~/iCloud/cto-brain
touch test.txt

# Wait 30 seconds, then check log
cat ~/Automation/logs/cto_brain_sync.log
```

## How It Works

```
File change in ~/iCloud/cto-brain/
        │
        ▼
launchd detects change (WatchPaths)
        │
        ▼
Runs sync_cto_brain.sh
        │
        ▼
git add -A → git commit → git push
```

## Troubleshooting

**Watcher not running?**
```bash
launchctl list | grep cto-brain
# Should show the job. If not, reload:
launchctl unload ~/Library/LaunchAgents/com.user.sync-cto-brain.plist
launchctl load ~/Library/LaunchAgents/com.user.sync-cto-brain.plist
```

**Permission errors?**
```bash
chmod +x ~/Automation/sync_cto_brain.sh
```

**Check logs:**
```bash
tail -20 ~/Automation/logs/cto_brain_sync.log
```
