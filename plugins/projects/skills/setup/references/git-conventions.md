---
description: Git workflow และ commit conventions
---

# Git Conventions

## ⚠️ Claude Code ไม่ทำ Git อัตโนมัติ

Claude Code **ไม่** สร้าง branch, commit, หรือ push เองโดยอัตโนมัติ
ทำได้ก็ต่อเมื่อคุณสั่งเท่านั้น

**วิธีป้องกัน code หาย:** ทำ checkpoint commit ก่อนให้ Claude ทำงานทุกครั้ง

---

## Workflow กับ Claude Code

```bash
# ขั้นที่ 1: สร้าง branch ใหม่
git checkout main && git pull
git checkout -b feature/ชื่อ-feature

# ขั้นที่ 2: checkpoint commit (ก่อนให้ Claude ทำงาน)
/checkpoint <ชื่องาน>

# ขั้นที่ 3: บอก Claude ให้ทำงาน

# ขั้นที่ 4: ตรวจสอบ
/ship [task-id]

# ขั้นที่ 5ก: โอเค → commit + merge
git add src/ tests/
git commit -m "✨ feat(scope): add feature name"

# ขั้นที่ 5ข: พัง → ย้อนกลับ
git checkout .          # ทิ้งการแก้ไขทุกไฟล์
git clean -fd           # ลบไฟล์ใหม่ที่ Claude สร้าง
# ถ้ามี checkpoint: git reset --hard HEAD
```

## วิธีย้อนกลับแบบต่างๆ

| สถานการณ์ | คำสั่ง |
|---|---|
| ยังไม่ได้ commit, อยากทิ้งการแก้ไข | `git checkout .` |
| มี checkpoint commit, อยากกลับไปจุดนั้น | `git reset --hard HEAD` |
| Commit ไปแล้ว, อยาก undo ล่าสุด | `git revert HEAD` |
| อยากดูว่า Claude เปลี่ยนอะไร | `git diff` |
| Compare กับ main | `git diff main...HEAD` |

## Branch Naming

```
feature/<short-description>    # feature ใหม่
fix/<issue-or-description>     # แก้ bug
refactor/<what-changed>        # refactor (ไม่เปลี่ยน behavior)
docs/<what-docs>               # เอกสารอย่างเดียว
chore/<task>                   # tooling, dependencies, CI
```

## Commit Message Format

```
<emoji> <type>(<scope>): <imperative summary>

[Optional body — อธิบาย WHY ไม่ใช่ WHAT]
```

**Types:**

| Emoji | Type | Emoji | Type |
|---|---|---|---|
| ✨ | feat | ✅ | test |
| 🐛 | fix | 📦 | build |
| 📝 | docs | 👷 | ci |
| 💄 | style | 🔧 | chore |
| ♻️ | refactor | ⚡ | perf |

**Scope:** กำหนดเองตามโปรเจค เช่น `api` | `ui` | `auth` | `db` | `config`
**Summary:** max 72 chars, imperative mood, ไม่มีจุดท้าย

```
✨ feat(api): add JWT authentication middleware
🐛 fix(ui): resolve button focus trap on modal close
♻️ refactor(db): extract query builder to separate module
✅ test(auth): add token expiry edge cases
```

> Emoji เพิ่มเติม (hotfix, breaking change, dependency, security ฯลฯ) ดูได้ที่ `plugins/projects/references/commit-emoji.md` ของ marketplace ที่ติดตั้ง skill ชุดนี้

## Protected Branches

- `main` — production-ready, ห้าม push โดยตรง
- Force push ห้ามเด็ดขาดบน `main`
- ทุก PR ต้อง pass: lint, typecheck, tests
