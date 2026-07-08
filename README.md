# natthasath-marketplace

รวม Claude Plugins และ Skills สำหรับใช้งานกับ Claude Code

## การติดตั้ง Marketplace

```bash
claude marketplace add natthasath/natthasath-marketplace
```

## การติดตั้ง Plugin

```bash
claude plugin install capacities
claude plugin install masterplan
claude plugin install refactor
claude plugin install roleplay
claude plugin install social
claude plugin install productive
claude plugin install devops
```

## Plugins

| Plugin | Skills | วัตถุประสงค์ |
|---|---|---|
| `capacities` | 2 | จัดการ PKM บน Capacities |
| `masterplan` | 5 | วางแผนและวิเคราะห์โปรเจกต์ซอฟต์แวร์ |
| `refactor` | 3 | ปรับปรุงโค้ด Docker และ Shell Script |
| `roleplay` | 4 | จำลองบทบาทเพื่อฝึกและวิเคราะห์ |
| `social` | 2 | สร้างโพสต์โซเชียลมีเดีย |
| `productive` | 3 | เพิ่มประสิทธิภาพการทำงาน English Mentor, Short Summary และ Meetings Summary |
| `devops` | 1 | จัดการ Session Context และ DevOps Workflow |

---

## Folder Structure

โครงสร้าง Folder มาตรฐานของ Plugin และ Skill ในรูปแบบ `skill-creator` standard:

```
<name>/                           # e.g. refactor, social, masterplan
├── .claude-plugin/
│   └── plugin.json               # Plugin metadata (name, version, description, keywords)
└── skills/
    └── <skill-name>/
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

## capacities

Plugin สำหรับ **Capacities PKM** — ออกแบบ Space, Object Types, Tags, Collections และ Workflow

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `capacities` | ออกแบบและปรับปรุงระบบ Capacities ครอบคลุม Object Type, Properties, Tags, Collections, Relations |
| `mood-tag` | วิเคราะห์อารมณ์จาก Daily Notes และแนะนำ Mood Tag ตาม Yale Mood Meter Framework |

### การติดตั้ง

```bash
claude plugin install capacities
```

### การเรียกใช้ Skill

```
/capacities
/mood-tag
```

### Yale Mood Meter Zones

| โซน | Valence | Arousal | ตัวอย่าง |
|---|---|---|---|
| 🟡 Yellow | บวก | สูง | `#mood-joyful`, `#mood-excited` |
| 🔴 Red | ลบ | สูง | `#mood-stressed`, `#mood-frustrated` |
| 🟢 Green | บวก | ต่ำ | `#mood-calm`, `#mood-reflective` |
| 🔵 Blue | ลบ | ต่ำ | `#mood-sad`, `#mood-unsettled` |

---

## masterplan

Plugin สำหรับ **วางแผนและวิเคราะห์โปรเจกต์** — ครอบคลุมตั้งแต่ Requirement จนถึง Architecture และ Database Design

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `kickoff` | ช่วยนักพัฒนาวางแผนไอเดียแอปผ่านการสนทนา และสร้าง `masterplan.md` |
| `gather` | เก็บรวบรวม Business และ Technical Requirements จาก Stakeholders อย่างเป็นระบบ |
| `analyze` | แปลง Business Needs เป็น Functional และ Technical System Requirements |
| `architect` | เลือกและกำหนด IT Architecture ที่จะใช้ ครอบคลุม Infrastructure, Application และ Integration Strategy |
| `database` | ออกแบบ Database Schema สำหรับ PostgreSQL และ Laravel พร้อม Migration-ready guidance |

### การติดตั้ง

```bash
claude plugin install masterplan
```

### การเรียกใช้ Skill

```
/kickoff
/gather
/analyze
/architect
/database
```

### `/kickoff` vs `/init`

| ด้าน | `/kickoff` | `/init` (Claude Code built-in) |
|---|---|---|
| **Input** | Idea ในหัว ยังไม่มีโค้ด | Codebase ที่มีอยู่แล้ว |
| **Output** | `masterplan.md` (blueprint สำหรับ developer) | `CLAUDE.md` (ให้ Claude เข้าใจ repo) |
| **Stage** | ก่อนเริ่ม code เลย | หลัง project มีอยู่แล้ว |
| **วัตถุประสงค์** | วางแผน project ใหม่จากศูนย์ | Document codebase ที่มี |

> `/kickoff` คือสิ่งที่ทำ **ก่อน** `/init` — เปลี่ยน idea ให้เป็นแผน แล้วค่อย init repo

---

## refactor

Plugin สำหรับ **ปรับปรุงคุณภาพโค้ด** — เน้น Docker และ Shell Script ให้เป็น Production-ready

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `refactor-compose` | Refactor `docker-compose.yml` และ `.env` ให้เป็น Best Practice |
| `refactor-dockerfile` | สร้างและ Refactor `Dockerfile` ให้มี Security, Performance และ Layer Caching ที่ดี |
| `refactor-shell` | สร้างและ Refactor Shell Script ให้มี Error Handling, Logging และโครงสร้างมาตรฐาน |

### การติดตั้ง

```bash
claude plugin install refactor
```

### การเรียกใช้ Skill

```
/refactor-compose
/refactor-dockerfile
/refactor-shell
```

---

## roleplay

Plugin สำหรับ **จำลองบทบาท** — ฝึกทักษะการสัมภาษณ์ การสอบสวน การตัดสินใจเชิงยุทธศาสตร์ และการสนทนาภาษาอังกฤษ

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `roleplay-interview` | จำลองนักสัมภาษณ์งานที่ใช้คำถาม Behavioral และ Psychological Probing |
| `roleplay-investigator` | จำลองเจ้าหน้าที่สืบสวนที่ใช้ Reid Technique และ PEACE Model |
| `roleplay-president` | จำลองผู้ช่วยประธานาธิบดีสำหรับวิเคราะห์นโยบายและวางแผนยุทธศาสตร์ |
| `roleplay-english` | ฝึกสนทนาภาษาอังกฤษผ่าน scenario จริง: Interview, Meeting, Customer, Small Talk, Email, Negotiation |

### การติดตั้ง

```bash
claude plugin install roleplay
```

### การเรียกใช้ Skill

```
/roleplay-interview
/roleplay-investigator
/roleplay-president
/roleplay-english
```

---

## social

Plugin สำหรับ **สร้างโพสต์โซเชียลมีเดีย** — เน้น Thought Leadership และ Personal Branding

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `post-facebook` | เขียนโพสต์ Facebook ภาษาไทยแนว Thought Leadership จริงจังปนกวนเล็กน้อย |
| `post-linkedin` | เขียนโพสต์ LinkedIn ภาษาอังกฤษสายไอทีและเทคโนโลยี เพื่อ Personal Branding |

### การติดตั้ง

```bash
claude plugin install social
```

### การเรียกใช้ Skill

```
/post-facebook
/post-linkedin
```

---

## productive

Plugin สำหรับ **เพิ่มประสิทธิภาพการทำงาน** — English Mentor หลายโหมด, Short Summary สำหรับบริการ/เทคโนโลยี และ Meetings Summary

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `mentor-english` | ครู English ส่วนตัว รองรับ 5 โหมด: แปล, ตรวจแกรมมา, คิดประโยคตอบกลับ, ปรับ tone, คลังคำศัพท์ |
| `summarize` | สรุปข้อมูลบริการหรือเทคโนโลยีแบบกระชับ พร้อม Key Features และ Real-world Example |
| `summarize-meeting` | สรุปการประชุมเป็นโครงสร้างมาตรฐาน: Objective, Key Topics, Discussions, Decisions, Action Items และ Next Step |

### การติดตั้ง

```bash
claude plugin install productive
```

### การเรียกใช้ Skill

```
/mentor-english --translation
/mentor-english --grammar
/mentor-english --reply
/mentor-english --tone
/mentor-english --vocab
/summarize
/summarize-meeting
```

---

## devops

Plugin สำหรับ **DevOps Workflow** — จัดการ Session Context และเพิ่มประสิทธิภาพการทำงานกับ Claude Code

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `session-name` | ตั้งชื่อ session ปัจจุบัน บันทึกลง memory และแสดง context สำหรับอ้างอิงในการสนทนา |

### การติดตั้ง

```bash
claude plugin install devops
```

### การเรียกใช้ Skill

```
/session-name <ชื่อ session>
```
