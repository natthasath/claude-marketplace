# Skill Framework Guide

คู่มือเลือก Framework สำหรับสร้าง Skill — แต่ละ framework เหมาะกับ skill ประเภทต่างกัน
เลือกให้ตรงกับลักษณะงานก่อนเขียน SKILL.md เพื่อให้โครงสร้างชัด และ Claude trigger ได้แม่น

---

## Framework ยอดนิยม

### 1. RTF — Role, Task, Format

โครงสร้างพื้นฐานที่สุด เหมาะกับ skill ที่ output ชัดเจนและไม่มี step ซับซ้อน

```
# บทบาท (Role)
อธิบายว่า Claude เป็นใคร และทำไมถึงทำหน้าที่นี้

# คำขอ / งาน (Task)
สิ่งที่ต้องทำ และ constraints สำคัญ

# รูปแบบ (Format)
โครงสร้าง output ที่ต้องการ
```

**เหมาะกับ:**
- Conversational skill (roleplay, mentor)
- Single-turn creative output (โพสต์โซเชียล, สรุป)
- Simple analysis (mood-tag, tldr)

**ตัวอย่าง skill ในโปรเจกต์นี้:** `translate`, `mentor-english`, `tldr`, `post-facebook`, `post-linkedin`, `comeet`, `perspective`, `roleplay-*`

---

### 2. RISEN — Role, Instructions, Steps, End Goal, Narrowing

เหมาะกับ workflow skill ที่มีลำดับขั้นตอนชัดเจน และ trigger condition สำคัญ

```
---
description: Use when [specific condition / problem symptom]
---

# Role
บทบาทและเหตุผล

# Instructions
กฎและข้อจำกัดหลัก

# Steps
ขั้นตอนที่ต้องทำตามลำดับ — ห้ามข้าม

# End Goal
ผลลัพธ์สุดท้ายที่ถูกต้องเป็นอย่างไร

# Narrowing (อยู่ใน description frontmatter)
เงื่อนไขที่ trigger skill นี้ vs. ไม่ trigger
```

**เหมาะกับ:**
- Workflow ที่มี ORDER สำคัญ (ข้ามขั้นแล้วเสียหาย)
- Discipline-enforcing skill (ต้องห้ามพฤติกรรมบางอย่าง)
- Multi-step process ที่มี checkpoint

**ตัวอย่าง skill ในโปรเจกต์นี้:** `kickoff`, `gather`, `analyze`, `architect`, `implement`, `debug`, `ship`, `refactor-*`

---

### 3. CO-STAR — Context, Objective, Style, Tone, Audience, Response

เหมาะกับ skill ที่ output ต้องการ style และ tone ที่แม่นยำ เช่น content writing

```
# Context
บริบทและที่มาของงาน

# Objective
เป้าหมายที่ต้องการบรรลุ

# Style
รูปแบบการเขียน / น้ำเสียง

# Tone
ระดับความเป็นทางการ, อารมณ์ของ output

# Audience
กลุ่มเป้าหมายของ output

# Response
โครงสร้าง output ที่ต้องการ
```

**เหมาะกับ:**
- Content creation ที่ต้องการ brand voice ชัดเจน
- Skill ที่ audience แตกต่างกันทำให้ output เปลี่ยน
- Creative writing, copywriting

**ตัวอย่าง skill ในโปรเจกต์นี้:** `post-facebook`, `post-linkedin` (ควรพิจารณา upgrade)

---

### 4. RACE — Role, Action, Context, Execute

เน้น action-oriented — เหมาะกับ skill ที่ทำงานแบบ one-shot และต้องการ output ทันที

```
# Role
Claude เป็นใคร

# Action
สิ่งที่ต้องทำ (กริยา + object ชัดเจน)

# Context
ข้อมูลพื้นหลังที่จำเป็น

# Execute
วิธี execute และ format ของ output
```

**เหมาะกับ:**
- Tool-use skill (เรียก API, อ่านไฟล์, ค้นหาข้อมูล)
- Transformation skill (input → output ตรงๆ)
- Utility skill ที่ไม่ต้องสนทนา

**ตัวอย่าง skill ในโปรเจกต์นี้:** `ebook`, `session-name`, `checkpoint`, `set-stack`

---

### 5. CRAFT — Context, Role, Action, Format, Target

ใกล้เคียง RACE แต่เน้น Target (ผู้รับ output) และ Format แยกชัด

```
# Context
สถานการณ์และข้อมูลพื้นหลัง

# Role
บทบาทของ Claude

# Action
สิ่งที่ต้องทำ

# Format
โครงสร้างและรูปแบบ output

# Target
ผู้รับ output คือใคร / จะนำไปใช้ทำอะไร
```

**เหมาะกับ:**
- Skill ที่ output ถูกนำไปใช้ต่อ (เช่น เอกสาร, template)
- Skill ที่ audience กำหนด format ของ output

**ตัวอย่าง skill ในโปรเจกต์นี้:** `setup`, `add-phase`, `writing-plans` style

---

### 6. APE — Action, Purpose, Expectation

Framework สั้นที่สุด เหมาะกับ skill ง่ายๆ ที่ไม่ต้องการบริบทมาก

```
# Action
ทำอะไร

# Purpose
ทำเพื่ออะไร

# Expectation
output ที่ถูกต้องเป็นอย่างไร
```

**เหมาะกับ:**
- Simple utility skill
- Skill ที่ใช้ภายในเป็น sub-step ของ skill ใหญ่

**ตัวอย่าง skill ในโปรเจกต์นี้:** `status`, `today`, `list-task`, `list-phase`, `done-task`, `done-phase`

---

### 7. TAG — Task, Action, Goal

Ultra-minimal — เหมาะกับ helper skill หรือ skill ที่ context ชัดเจนมาก

```
Task: อธิบายงานสั้นๆ
Action: ขั้นตอนเดียวที่ต้องทำ
Goal: ผลลัพธ์ที่ต้องการ
```

**เหมาะกับ:**
- Sub-skill ที่ถูกเรียกจาก skill อื่น
- Skill ที่มี input/output ชัดเจนมาก ไม่มี edge case

---

### 8. CARE — Context, Action, Result, Example

เน้น Example — เหมาะกับ skill ที่ต้องการตัวอย่างเพื่อให้ Claude เข้าใจ pattern

```
# Context
บริบทของงาน

# Action
สิ่งที่ต้องทำ

# Result
output ที่ต้องการ

# Example
ตัวอย่าง input → output จริง
```

**เหมาะกับ:**
- Skill ที่มี pattern เฉพาะที่อธิบายด้วยคำยาก แต่เห็นตัวอย่างแล้วเข้าใจทันที
- Format transformation skill (เช่น แปลง log format, rewrite prose style)

**ตัวอย่าง skill ในโปรเจกต์นี้:** `mood-tag`

---

## ตาราง Decision

| ลักษณะ Skill | Framework ที่แนะนำ |
|---|---|
| Conversational / ตอบโต้ต่อเนื่อง | RTF |
| Workflow มีขั้นตอนเรียงลำดับ | RISEN |
| Creative / Content writing | CO-STAR |
| Tool-use / One-shot transformation | RACE |
| Output ถูกนำไปใช้ต่อ | CRAFT |
| Simple utility / State change | APE |
| Sub-skill / Helper | TAG |
| Pattern-based / ต้องการตัวอย่าง | CARE |

---

## แผนที่ Skill ในโปรเจกต์นี้

### RTF (คงไว้)
`translate` · `mentor-english` · `tldr` · `comeet` · `perspective`
`post-facebook` · `post-linkedin` · `roleplay-interview` · `roleplay-investigator`
`roleplay-president` · `roleplay-english` · `mood-tag` · `laura-whaley`

### RISEN (ควรปรับ)
`kickoff` · `gather` · `analyze` · `architect` · `database`
`implement` · `debug` · `ship` · `setup`
`refactor-compose` · `refactor-dockerfile` · `refactor-shell`
`start-task`

### RACE (ควรปรับ)
`ebook` · `session-name` · `checkpoint` · `set-stack`

### APE (ควรปรับ)
`status` · `today` · `list-task` · `list-phase`
`add-task` · `add-phase` · `done-task` · `done-phase`

### CARE (ควรปรับ)
`mood-tag`

---

## หลักการเลือก Framework

1. **ถามก่อนว่า skill นี้บังคับ order ไหม?** → ใช่ = RISEN, ไม่ใช่ = ดูข้อถัดไป
2. **output ต้องการ tone/style เฉพาะไหม?** → ใช่ = CO-STAR หรือ RTF
3. **มีตัวอย่างที่อธิบายได้ดีกว่าคำอธิบาย?** → CARE
4. **เป็น tool-use หรือ one-shot?** → RACE หรือ APE
5. **ง่ายมาก ไม่มี edge case?** → APE หรือ TAG

---

## Tips สำหรับ description Frontmatter

ไม่ว่าจะใช้ framework ไหน description ควรทำหน้าที่เป็น **trigger condition เท่านั้น**

```yaml
# ดี — บอก "เมื่อไหร่" และ "ปัญหาอะไร"
description: Use when the user needs to translate messages continuously
  between two languages without explanations or commentary.

# ไม่ดี — บอก "ทำอะไร" แทน "เมื่อไหร่"
description: Translates text between languages using auto-detection
  and returns only the translation result in Artifact format.
```

description ที่ดีทำให้ Claude decide invoke ได้แม่น — instructions อยู่ใน body เท่านั้น
