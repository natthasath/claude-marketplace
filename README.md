# natthasath-marketplace

รวม Claude Plugins และ Skills สำหรับใช้งานกับ Claude Code

## การติดตั้ง Marketplace

```bash
claude marketplace add natthasath/natthasath-marketplace
```

## การติดตั้ง Plugin

```bash
claude plugin install plugin-capacities
claude plugin install plugin-project-masterplan
claude plugin install plugin-refactor
claude plugin install plugin-roleplay
claude plugin install plugin-social-post
claude plugin install plugin-productive
claude plugin install plugin-devops
```

## Plugins

| Plugin | Skills | วัตถุประสงค์ |
|---|---|---|
| `plugin-capacities` | 2 | จัดการ PKM บน Capacities |
| `plugin-project-masterplan` | 5 | วางแผนและวิเคราะห์โปรเจกต์ซอฟต์แวร์ |
| `plugin-refactor` | 3 | ปรับปรุงโค้ด Docker และ Shell Script |
| `plugin-roleplay` | 3 | จำลองบทบาทเพื่อฝึกและวิเคราะห์ |
| `plugin-social-post` | 2 | สร้างโพสต์โซเชียลมีเดีย |
| `plugin-productive` | 3 | เพิ่มประสิทธิภาพการทำงาน English Mentor, Short Summary และ Meetings Summary |
| `plugin-devops` | 1 | จัดการ Session Context และ DevOps Workflow |

---

## Folder Structure

โครงสร้าง Folder มาตรฐานของ Plugin และ Skill ในรูปแบบ `skill-creator` standard:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json               # Plugin metadata (name, version, description, keywords)
└── skills/
    └── skill-name/
        ├── SKILL.md              # (required) Frontmatter + instructions
        ├── agents/               # Instructions for specialized subagents
        │   ├── analyzer.md
        │   ├── comparator.md
        │   └── grader.md
        ├── assets/               # Files used in output (templates, icons, HTML)
        │   └── eval_review.html
        ├── eval-viewer/          # Evaluation viewer scripts
        │   ├── generate_review.py
        │   └── viewer.html
        ├── references/           # Docs loaded into context as needed
        │   └── schemas.md
        └── scripts/              # Executable Python scripts for automation
            ├── aggregate_benchmark.py
            ├── improve_description.py
            ├── package_skill.py
            ├── run_eval.py
            ├── run_loop.py
            └── utils.py
```

### Progressive Disclosure

Skills ใช้ระบบโหลด 3 ระดับ:

| ระดับ | เนื้อหา | เมื่อโหลด |
|---|---|---|
| 1 | `name` + `description` (frontmatter) | ทุกครั้งใน context (~100 words) |
| 2 | SKILL.md body | เมื่อ skill ถูก trigger |
| 3 | Bundled resources (scripts/references/assets) | เมื่อ skill เรียกใช้งาน |

---

## plugin-capacities

Plugin สำหรับ **Capacities PKM** — ออกแบบ Space, Object Types, Tags, Collections และ Workflow

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `skill-capacities-specialist` | ออกแบบและปรับปรุงระบบ Capacities ครอบคลุม Object Type, Properties, Tags, Collections, Relations |
| `skill-mood-tags` | วิเคราะห์อารมณ์จาก Daily Notes และแนะนำ Mood Tag ตาม Yale Mood Meter Framework |

### การติดตั้ง

```bash
claude plugin install plugin-capacities
```

### การเรียกใช้ Skill

```
/skill-capacities-specialist
/skill-mood-tags
```

### Yale Mood Meter Zones

| โซน | Valence | Arousal | ตัวอย่าง |
|---|---|---|---|
| 🟡 Yellow | บวก | สูง | `#mood-joyful`, `#mood-excited` |
| 🔴 Red | ลบ | สูง | `#mood-stressed`, `#mood-frustrated` |
| 🟢 Green | บวก | ต่ำ | `#mood-calm`, `#mood-reflective` |
| 🔵 Blue | ลบ | ต่ำ | `#mood-sad`, `#mood-unsettled` |

---

## plugin-project-masterplan

Plugin สำหรับ **วางแผนและวิเคราะห์โปรเจกต์** — ครอบคลุมตั้งแต่ Requirement จนถึง Architecture และ Database Design

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `skill-project-masterplan` | ช่วยนักพัฒนาวางแผนไอเดียแอปผ่านการสนทนา และสร้าง `masterplan.md` |
| `skill-requirement-collector-masterplan` | เก็บรวบรวม Business และ Technical Requirements จาก Stakeholders อย่างเป็นระบบ |
| `skill-system-requirement-masterplan` | แปลง Business Needs เป็น Functional และ Technical System Requirements |
| `skill-architecture-collector-masterplan` | เก็บข้อมูล IT Infrastructure, Application Architecture เพื่อวาง Enterprise Architecture |
| `skill-database-design-masterplan` | ออกแบบ Database Schema สำหรับ PostgreSQL และ Laravel พร้อม Migration-ready guidance |

### การติดตั้ง

```bash
claude plugin install plugin-project-masterplan
```

### การเรียกใช้ Skill

```
/skill-project-masterplan
/skill-requirement-collector-masterplan
/skill-system-requirement-masterplan
/skill-architecture-collector-masterplan
/skill-database-design-masterplan
```

---

## plugin-refactor

Plugin สำหรับ **ปรับปรุงคุณภาพโค้ด** — เน้น Docker และ Shell Script ให้เป็น Production-ready

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `skill-docker-compose-refactor` | Refactor `docker-compose.yml` และ `.env` ให้เป็น Best Practice |
| `skill-dockerfile-refactor` | สร้างและ Refactor `Dockerfile` ให้มี Security, Performance และ Layer Caching ที่ดี |
| `skill-shell-script-refactor` | สร้างและ Refactor Shell Script ให้มี Error Handling, Logging และโครงสร้างมาตรฐาน |

### การติดตั้ง

```bash
claude plugin install plugin-refactor
```

### การเรียกใช้ Skill

```
/skill-docker-compose-refactor
/skill-dockerfile-refactor
/skill-shell-script-refactor
```

---

## plugin-roleplay

Plugin สำหรับ **จำลองบทบาท** — ฝึกทักษะการสัมภาษณ์ การสอบสวน และการตัดสินใจเชิงยุทธศาสตร์

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `skill-job-interview` | จำลองนักสัมภาษณ์งานที่ใช้คำถาม Behavioral และ Psychological Probing |
| `skill-investigator-officer` | จำลองเจ้าหน้าที่สืบสวนที่ใช้ Reid Technique และ PEACE Model |
| `skill-presidential-strategic-assistant` | จำลองผู้ช่วยประธานาธิบดีสำหรับวิเคราะห์นโยบายและวางแผนยุทธศาสตร์ |

### การติดตั้ง

```bash
claude plugin install plugin-roleplay
```

### การเรียกใช้ Skill

```
/skill-job-interview
/skill-investigator-officer
/skill-presidential-strategic-assistant
```

---

## plugin-social-post

Plugin สำหรับ **สร้างโพสต์โซเชียลมีเดีย** — เน้น Thought Leadership และ Personal Branding

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `skill-facebook-post` | เขียนโพสต์ Facebook ภาษาไทยแนว Thought Leadership จริงจังปนกวนเล็กน้อย |
| `skill-linkedin-post` | เขียนโพสต์ LinkedIn ภาษาอังกฤษสายไอทีและเทคโนโลยี เพื่อ Personal Branding |

### การติดตั้ง

```bash
claude plugin install plugin-social-post
```

### การเรียกใช้ Skill

```
/skill-facebook-post
/skill-linkedin-post
```

---

## plugin-productive

Plugin สำหรับ **เพิ่มประสิทธิภาพการทำงาน** — English Mentor หลายโหมด, Short Summary สำหรับบริการ/เทคโนโลยี และ Meetings Summary

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `skill-english-mentor` | ครู English ส่วนตัว รองรับ 6 โหมด: แปล, ตรวจแกรมมา, คิดประโยคตอบกลับ, จำลองสถานการณ์, ปรับ tone, คลังคำศัพท์ |
| `skill-short-summary` | สรุปข้อมูลบริการหรือเทคโนโลยีแบบกระชับ พร้อม Key Features และ Real-world Example |
| `skill-meetings-summary` | สรุปการประชุมเป็นโครงสร้างมาตรฐาน: Objective, Key Topics, Discussions, Decisions, Action Items และ Next Step |

### การติดตั้ง

```bash
claude plugin install plugin-productive
```

### การเรียกใช้ Skill

```
/skill-english-mentor --translation
/skill-english-mentor --grammar
/skill-english-mentor --reply
/skill-english-mentor --roleplay
/skill-english-mentor --tone
/skill-english-mentor --vocab
/skill-short-summary
/skill-meetings-summary
```

---

## plugin-devops

Plugin สำหรับ **DevOps Workflow** — จัดการ Session Context และเพิ่มประสิทธิภาพการทำงานกับ Claude Code

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `skill-session-name` | ตั้งชื่อ session ปัจจุบัน บันทึกลง memory และแสดง context สำหรับอ้างอิงในการสนทนา |

### การติดตั้ง

```bash
claude plugin install plugin-devops
```

### การเรียกใช้ Skill

```
/skill-session-name <ชื่อ session>
```
