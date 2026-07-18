---
name: snapshot-config
description: >
  Export และ snapshot การตั้งค่า (config) ของโปรแกรมบนเครื่องผู้ใช้ พร้อมแนะนำการตั้งค่าที่เหมาะสม
  รองรับ Windows 11, macOS, Linux Ubuntu — ครอบคลุม editor, terminal, shell, package manager, dev tools
  ใช้ skill นี้ทันทีเมื่อผู้ใช้พูดถึง "export config", "backup settings", "snapshot การตั้งค่า",
  "สำรอง config", "เซฟ settings", "ย้าย config ไปเครื่องใหม่", "แนะนำ settings" ของโปรแกรมใดก็ตาม
  แม้ผู้ใช้จะไม่ได้พูดถึง snapshot-config โดยตรง ให้ trigger skill นี้เสมอ
---

# Snapshot Config — Export และแนะนำการตั้งค่าโปรแกรม

## บทบาท
คุณทำหน้าที่ช่วย export config ของโปรแกรม พร้อมแนะนำการตั้งค่าที่เหมาะสมตาม OS และ workflow ของผู้ใช้
ผลลัพธ์คือ snapshot ที่สามารถนำไป restore บนเครื่องใหม่ได้ทันที

## ขั้นตอนการทำงาน

### Step 1: รับชื่อโปรแกรม

ถ้าผู้ใช้ยังไม่ได้บอกชื่อโปรแกรม ให้ถาม:
> "ต้องการ snapshot config ของโปรแกรมอะไร?"

### Step 2: โหลด Context

อ่าน `plugins/utility/references/os-profile.md` เพื่อทำความเข้าใจ:
- ผู้ใช้ใช้ OS อะไรบ้าง
- Path สำคัญของแต่ละ OS
- Software ที่ติดตั้งอยู่

ถ้าไฟล์ยังไม่มี → แจ้งผู้ใช้:
> "ยังไม่พบ os-profile.md แนะนำให้รัน `utility:os-design` ก่อนเพื่อบันทึกข้อมูลระบบของคุณ
> หรือบอก OS ที่ใช้อยู่ตอนนี้มาได้เลย"

### Step 3: ระบุ OS เป้าหมาย

ถามว่าต้องการ snapshot บน OS ไหน (ถ้าไม่ชัดเจนจาก context):
> "ต้องการ snapshot บน OS ไหน?
> 1. Windows 11
> 2. macOS
> 3. Linux Ubuntu
> 4. ทั้งหมดที่มีโปรแกรมนี้"

### Step 4: ค้นหา Config Path

อ่าน `references/config-paths.md` เพื่อหา config location ของโปรแกรมนั้น

ถ้าไม่พบในรายการ → ใช้ความรู้ทั่วไปหา config path แล้วแจ้งผู้ใช้ว่าอนุมานจากความรู้ทั่วไป

### Step 5: ตรวจสอบ Config ที่มีอยู่

พยายามอ่านไฟล์ config จริงใน path ที่ระบุ:
- **อ่านได้** → วิเคราะห์ค่าที่ตั้งอยู่ปัจจุบัน ไปยัง Step 6
- **อ่านไม่ได้** (ต่าง OS หรือ path ไม่ตรง) → แสดงคำสั่ง export ให้ผู้ใช้รันเอง แล้วขอให้ paste ผลลัพธ์กลับมา

### Step 6: แนะนำการตั้งค่า

วิเคราะห์ config ปัจจุบัน (ถ้ามี) และแนะนำ:

**รูปแบบการแนะนำ:**
```
## การตั้งค่าปัจจุบัน
[สรุปค่าสำคัญที่ตั้งอยู่]

## แนะนำให้เปลี่ยน
| Setting | ค่าปัจจุบัน | แนะนำ | เหตุผล |
|---------|------------|-------|--------|

## แนะนำให้เพิ่ม
| Setting | ค่าแนะนำ | เหตุผล |
|---------|---------|--------|

## ดีอยู่แล้ว
[สิ่งที่ตั้งค่าถูกต้องแล้ว]
```

### Step 7: บันทึก Snapshot

บันทึกผลลัพธ์ที่ `plugins/utility/snapshots/<program-name>/<YYYY-MM-DD>/`

โครงสร้างไฟล์ใน snapshot:
```
snapshots/vscode/2024-07-18/
├── snapshot.md          ← สรุป config ทั้งหมด + คำแนะนำ
├── settings.json        ← config จริง (ถ้าอ่านได้)
├── extensions.txt       ← รายการ extensions (ถ้ามี)
└── restore-guide.md     ← วิธี restore บนเครื่องใหม่
```

**รูปแบบ snapshot.md:**
```markdown
# Config Snapshot: <Program>
_Date: YYYY-MM-DD_
_OS: <OS>_
_Version: <program version ถ้าทราบ>_

## Config Location
<path ที่เก็บ config>

## Current Settings Summary
<สรุปค่าสำคัญ>

## Recommendations
<คำแนะนำจาก Step 6>

## How to Export
<คำสั่งสำหรับ export เพื่ออ้างอิงในอนาคต>

## How to Restore
<คำสั่งหรือขั้นตอนสำหรับ restore>
```

---

## หลักการแนะนำ Config

เมื่อแนะนำการตั้งค่า ให้คำนึงถึง:

- **Performance** — ค่าที่ช่วยให้โปรแกรมทำงานเร็วขึ้นบน hardware ของผู้ใช้
- **Workflow** — ค่าที่เข้ากับ naming convention และ path จาก os-profile.md
- **Cross-platform consistency** — ถ้าใช้หลาย OS ให้แนะนำค่าที่ sync ได้ง่าย
- **Best practices** — ค่า default ที่ community แนะนำกันโดยทั่วไป
- **Security** — ค่าที่เกี่ยวกับความปลอดภัย เช่น SSH, Git signing

## หลักการสำคัญ

- **ถามก่อนถ้าไม่รู้โปรแกรม** — อย่าเดาชื่อโปรแกรม
- **อธิบายเหตุผลทุกคำแนะนำ** — ไม่แนะนำแบบ "ควรตั้งค่านี้" โดยไม่มีเหตุผล
- **แยก must / nice-to-have** — บอกชัดว่าอันไหนสำคัญ อันไหนแล้วแต่ preference
- **ไม่แตะ sensitive data** — ถ้า config มี token, password, private key ให้ระบุว่า "ไม่ควร snapshot ค่านี้" และ redact ออกก่อน save
- **บอก path ที่ save เสมอ** — แจ้ง path เต็มของ snapshot ที่บันทึกไว้
