---
date: 2026-06-19
tags:
  - home
aliases:
  - Dashboard
---

# 🧠 Worldwidebro Holdings's Executive Vault

> Claude automatically saves everything important from every conversation.

---

## ⚡ Quick Navigation

[[Boards/OKRs\|📋 OKRs]]

[[Daily/\|📁 Daily]] · [[People/\|📁 People]] · [[Meetings/\|📁 Meetings]] · [[Decisions/\|📁 Decisions]] · [[OKRs/\|📁 OKRs]] · [[Projects/\|📁 Projects]] · [[Knowledge/\|📁 Knowledge]] · [[Reviews/\|📁 Reviews]]

---

## 📅 Recent Daily Notes

```dataview
TABLE WITHOUT ID file.link AS "Day", mood AS "Mood", energy AS "Energy"
FROM "Daily"
SORT date DESC
LIMIT 7
```

---

## 📊 Vault Stats

```dataviewjs
const all = dv.pages("");
dv.paragraph(`📝 **${all.length}** total notes`);
```
