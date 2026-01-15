---
description: Sync changes to GitHub repository
---

This workflow automates the process of pushing your latest changes to GitHub.
It ensures that 'Expenses_tracker.html' is always copied to 'index.html' so the mobile app stays updated.

// turbo
1. Sync all changes to GitHub:
```bash
cp Expenses_tracker.html index.html && cp sw.js deploy/sw.js && cp index.html deploy/index.html && git add . && git commit -m "Auto-sync: $(date)" && git push origin main
```
