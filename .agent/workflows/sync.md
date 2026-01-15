---
description: Sync changes to GitHub repository
---

This workflow automates the process of pushing your latest changes to GitHub so you don't have to use the website manually.

// turbo
1. Sync all changes to GitHub:
```bash
git add . && git commit -m "Auto-sync from Antigravity: $(date)" && git push origin main
```
