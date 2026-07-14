---
name: done-phase
description: Mark phase ปัจจุบันว่าเสร็จแล้วและเปลี่ยนไป phase ถัดไป ตรวจสอบ tasks ค้าง, อัปเดต PLAN.md และเลื่อน current-phase config ใช้ skill นี้เมื่อต้องการปิด phase เช่น "phase นี้เสร็จแล้ว", "เปลี่ยน phase ถัดไป"
tools:
  - Read
  - Edit
  - Bash
---

!`cat .claude/config/current-phase.md 2>/dev/null && echo "---" && cat context/plans/PLAN.md 2>/dev/null`

Mark phase ปัจจุบันว่าเสร็จแล้ว และเริ่ม phase ถัดไป

**Input:** $ARGUMENTS (ถ้าไม่มี ใช้ phase จาก config ด้านบน)

---

## ขั้นที่ 1 — ตรวจสอบ phase ที่จะ done

อ่าน `phase:` จาก config ด้านบน (หรือใช้ $ARGUMENTS ถ้ามี)
- ถ้า phase นั้น status ไม่ใช่ 🔄 In Progress ใน PLAN.md — แจ้ง "Phase <N> ยังไม่ได้เริ่มทำงาน" แล้วหยุด

## ขั้นที่ 2 — ตรวจสอบ tasks ค้างใน sprint

อ่าน `context/tasks/in_progress/current_sprint.md`
- ถ้ายังมี entries ที่มี `**Status:** 🔄 In Progress` อยู่ใน current_sprint.md — แจ้งรายการและถามว่า "ยังมี tasks ค้างอยู่ ต้องการดำเนินการต่อไหม? (y/n)"
- ถ้า n — หยุด
- ถ้า y — ดำเนินการต่อ

## ขั้นที่ 3 — อัปเดต PLAN.md

แก้ไข `context/plans/PLAN.md`:
1. เปลี่ยน row ของ phase ปัจจุบัน: `🔲 Not Started` หรือ `🔄 In Progress` → `✅ Done`
2. ถ้ามี phase ถัดไป (N+1) อยู่ใน PLAN.md: เปลี่ยน `🔲 Not Started` → `🔄 In Progress`

## ขั้นที่ 4 — อัปเดต phase plan file

ก่อนแก้ไข: หา slug จริงของ phase ด้วย Bash glob
```bash
ls context/plans/phase_<N>_*.md 2>/dev/null | head -1
```
ใช้ชื่อไฟล์ที่ได้จาก glob (เช่น `context/plans/phase_1_foundation.md`) ในขั้นตอนถัดไป

แก้ไข `context/plans/phase_<N>_<slug>.md` (ชื่อไฟล์จาก glob ด้านบน):
- เปลี่ยน `**Status:** 🔄 In Progress` → `**Status:** ✅ Done`
- เพิ่มบรรทัด `**Completed:** YYYY-MM-DD` (วันนี้)

## ขั้นที่ 5 — อัปเดต current-phase config

เขียน `.claude/config/current-phase.md` ให้ `phase:` เป็นเลข phase ถัดไป (N+1)
- ถ้าไม่มี phase ถัดไปใน PLAN.md — ให้ `phase:` คงค่าเดิมและแจ้ง "นี่คือ phase สุดท้าย 🎉"

## ขั้นที่ 6 — สรุปผล

```
✅ Phase <N> — <ชื่อ> เสร็จสมบูรณ์

ไฟล์ที่อัปเดต:
  ✅ context/plans/PLAN.md
  ✅ context/plans/phase_<N>_<slug>.md
  ✅ .claude/config/current-phase.md  (→ phase <N+1>)
```

แล้วปิดท้ายด้วย:

```
─────────────────────────────────────────────────
ถัดไป → /status              (ดูภาพรวมโปรเจค)
         /add-task <desc>     (เพิ่ม tasks ใน phase ถัดไป)
─────────────────────────────────────────────────
```
