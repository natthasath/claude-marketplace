---
name: status
description: แสดงภาพรวมสถานะโปรเจค — phase, sprint, git status ในครั้งเดียว
tools:
  - Read
  - Bash
---

แสดงภาพรวมสถานะโปรเจคทั้งหมด

อ่านไฟล์เหล่านี้แล้วสรุป:
1. `.claude/config/current-phase.md` → phase number ปัจจุบัน (N)
2. `context/plans/PLAN.md` → ชื่อ phase และ % เสร็จ
3. `context/tasks/in_progress/current_sprint.md` → งานที่กำลังทำ
4. `context/tasks/backlog/phase_<N>_*.md` → top 3 tasks รอทำ (ใช้ N จากข้อ 1)
5. รัน `git status --short` → มี uncommitted changes ไหม
6. รัน `git log --oneline -5` → commits ล่าสุด

แสดงผลในรูปแบบนี้:
─────────────────────────────
📍 Phase ปัจจุบัน: [ชื่อ] ([X/Y tasks เสร็จ])
🔄 กำลังทำ: [ชื่อ tasks]
📋 รอทำต่อ: [top 3 tasks จาก backlog]
🌿 Branch: [ชื่อ branch]
📝 Uncommitted: [มี/ไม่มี + จำนวนไฟล์]
🕐 Commit ล่าสุด: [message + เวลา]
─────────────────────────────
แนะนำ next action: [หนึ่งประโยค]

```
─────────────────────────────────────
ถัดไป → /list-task   (ดู tasks ทั้งหมด)
─────────────────────────────────────
```
