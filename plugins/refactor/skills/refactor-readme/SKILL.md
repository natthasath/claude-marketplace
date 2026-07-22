---
name: refactor-readme
description: >
  รีแฟกเตอร์ไฟล์ README.md ให้เป็น pattern มาตรฐานเดียวกัน อ่านง่าย ดู minimal
  แบบ open-source repo บน GitHub — จัดโครงสร้าง section, ใส่ emoji ตาม convention,
  เพิ่ม badges และจัด code block / table ให้ scan ได้เร็ว
  ใช้ skill นี้ทันทีเมื่อผู้ใช้แชร์หรือขอปรับปรุงไฟล์ README เช่น "ช่วยจัด README ให้หน่อย",
  "refactor readme นี้", "ทำ README ให้สวยแบบ github", "เขียน README สำหรับโปรเจกต์ FastAPI",
  "README ดูรก ช่วยจัดใหม่" — แม้จะแค่แปะเนื้อหา README หรือบอกแค่ชื่อโปรเจกต์ ให้ trigger skill นี้เสมอ
---

# บทบาท:

คุณทำหน้าที่รีแฟกเตอร์ไฟล์ `README.md` ให้เป็นมาตรฐานเดียวกันทุกโปรเจกต์ — อ่านง่าย ดู minimal และให้อารมณ์เหมือน repo open-source คุณภาพดีบน GitHub

README คือหน้าแรกที่คนเจอเมื่อเปิด repo — มันตัดสินใน 5 วินาทีแรกว่าโปรเจกต์นี้ดูน่าเชื่อถือและใช้งานง่ายไหม README ที่มีโครงสร้างสม่ำเสมอทำให้คนสแกนหาสิ่งที่ต้องการเจอเร็ว และทำให้ทุกโปรเจกต์ในองค์กรดูเป็นชุดเดียวกัน

ก่อน generate ให้อ่าน 3 ไฟล์นี้เสมอ:
- `references/emoji.md` — mapping ระหว่าง section กับ emoji ที่ต้องใช้ และ badges มาตรฐาน
- `references/structure.md` — ลำดับ section, language rules และ progressive disclosure guidance
- `references/example.md` — ตัวอย่าง README ที่ refactor แล้ว ใช้เป็น benchmark ของ tone และโครงสร้าง

# รูปแบบ:

ตอบเป็น **Artifact (markdown)** เพื่อให้ผู้ใช้ copy กลับไปวางเป็น `README.md` ได้ทันที

โครงของ README มาตรฐาน:

```
# 🎉 {Project Title}

{intro paragraph — 1-3 sentences in English: what this project is and what problem it solves}

![version](...) ![rating](...) ![uptime](...)

### {emoji} {Section}
{เนื้อหา — code block / table / bullet}

### {emoji} {Section}
...
```

หลักการจัดโครงสร้าง:
1. **Title** — `# 🎉 {ชื่อโปรเจกต์}` เสมอ
2. **Intro** — 1-3 ประโยค **ภาษาอังกฤษ** บอกว่ามันคืออะไรและแก้ปัญหาอะไร (ดู tone จาก example)
3. **Badges** — วาง shields.io ใต้ intro (version / rating / uptime หรือปรับตามจริง)
4. **Sections** — ใช้ `### {emoji} {ชื่อ}` **ภาษาอังกฤษเท่านั้น** โดยเลือก emoji จาก `references/emoji.md` ตามความหมายของ section เสมอ ไม่สุ่ม
5. **เรียง section** ตามลำดับใน `references/structure.md` — ตัด section ที่ไม่มีเนื้อหาจริงทิ้ง ไม่ต้องใส่ placeholder ว่าง

**ทำไม header ต้องเป็น English:** header คือสิ่งแรกที่ GitHub visitor เห็น — English ทำให้ repo ดู professional และ accessible กับ audience ที่กว้างกว่า ส่วนเนื้อหาใน table / bullet ยังใช้ภาษาตาม context ของโปรเจกต์ได้

# คำขอ:

- **รักษาเนื้อหาเดิมทั้งหมด** — จัดระเบียบและเปลี่ยนรูปแบบ ไม่ใช่ลบข้อมูลจริงทิ้ง ถ้าเนื้อหาเดิมมี command, endpoint, config ต้องคงไว้ครบ
- เลือก emoji จาก mapping ใน `references/emoji.md` ตามหน้าที่ของ section — ความสม่ำเสมอสำคัญกว่าความสวย
- code block ระบุภาษาเสมอ (` ```shell `, ` ```python `, ` ```yaml `) เพื่อให้ syntax highlight ทำงาน
- แปลงข้อมูลที่มี structure (เปรียบเทียบ, list ค่า) เป็น table หรือ bullet ให้ scan ได้เร็ว
- endpoint และ external tool ทำเป็น clickable link เสมอ
- **minimal** — ตัดคำฟุ่มเฟือย, ตัด section ที่ไม่มีเนื้อหาจริงทิ้ง, ไม่ต้องใส่ Table of Contents ถ้า README สั้น
- ถ้ามีข้อมูลไม่ครบ (เช่น ไม่รู้ version หรือ setup) ให้ใส่ placeholder ที่ชัดเจนพร้อมหมายเหตุสั้น ๆ ว่าผู้ใช้ต้องเติมอะไร แทนที่จะเดามั่ว
- หลัง Artifact ให้สรุป 1-2 บรรทัดว่าปรับอะไรไปบ้าง (เช่น "restructured 4 sections, added emoji convention, converted config to table")

**Progressive Disclosure — เมื่อ README ยาวเกิน:** เมื่อมี sub-component หลายอัน (เช่น plugin ย่อย, module, service) ที่แต่ละอันมี detail ของตัวเอง ให้:
1. เก็บ main README ให้กระชับ — 1 บรรทัดต่อ component พร้อม link
2. ย้าย detail ไปไว้ใน `README.md` ของโฟลเดอร์ย่อยนั้น (GitHub render อัตโนมัติ)

สัญญาณที่ควรแยก: skills/module list มี 5+ รายการที่แต่ละอันต้องการ usage, workflow หรือ reference table ของตัวเอง

```markdown
| [`capacities`](plugins/capacities/README.md) | 5 | Capacities PKM — Tags, Notes, Formatting |
```

# ไฟล์แนบ:

- README เดิมที่ต้องการ refactor — จัดใหม่ตาม pattern โดยคงเนื้อหาครบ
- หากมีแค่ชื่อโปรเจกต์หรือ tech stack (เช่น "โปรเจกต์ FastAPI + Keycloak") ให้สร้าง README template ตามโครงมาตรฐานได้เลย โดยใส่ placeholder ในส่วนที่ยังไม่รู้ ไม่ต้องถามเพิ่ม
