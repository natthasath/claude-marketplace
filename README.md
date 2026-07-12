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
claude plugin install projects
claude plugin install language
```

## Plugins

| Plugin | Skills | วัตถุประสงค์ |
|---|---|---|
| `capacities` | 1 | จัดการ PKM บน Capacities |
| `masterplan` | 5 | วางแผนและวิเคราะห์โปรเจกต์ซอฟต์แวร์ |
| `refactor` | 3 | ปรับปรุงโค้ด Docker และ Shell Script |
| `roleplay` | 4 | จำลองบทบาทเพื่อฝึกและวิเคราะห์ |
| `social` | 2 | สร้างโพสต์โซเชียลมีเดีย |
| `productive` | 6 | เพิ่มประสิทธิภาพการทำงาน Short Summary, Meetings Summary, PDF Downloader, Workplace Communication และ IT Work Scorecard |
| `devops` | 1 | จัดการ Session Context และ DevOps Workflow |
| `projects` | 15 | Setup และจัดการ development project — scaffold ครบ workflow ตั้งแต่ init จนถึง ship |
| `language` | 2 | เครื่องมือด้านภาษา — ล่ามแปลภาษาแบบต่อเนื่อง และ English Mentor |

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
| `mood-tag` | วิเคราะห์อารมณ์จาก Daily Notes และแนะนำ Mood Tag ตาม Yale Mood Meter Framework |

### การติดตั้ง

```bash
claude plugin install capacities
```

### การเรียกใช้ Skill

```
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

Plugin สำหรับ **เพิ่มประสิทธิภาพการทำงาน** — Short Summary, Meetings Summary, PDF Downloader, Workplace Communication Coach และ IT Work Scorecard

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `tldr` | สรุปข้อมูลบริการหรือเทคโนโลยีแบบกระชับ พร้อม Key Features และ Real-world Example |
| `comeet` | สรุปการประชุมเป็นโครงสร้างมาตรฐาน: Objective, Key Topics, Discussions, Decisions, Action Items และ Next Step |
| `perspective` | ให้มุมมองและข้อคิดจากหัวข้ออบรม เขียนในเสียงของ Senior Engineer — เจ็บแต่จริง ไม่ใช่สไตล์ HR |
| `ebook` | ค้นหาและดาวน์โหลดไฟล์ PDF จากแหล่งที่น่าเชื่อถือและถูกกฎหมาย รองรับทั้งค้นหาจากชื่อและดาวน์โหลดจาก URL |
| `laura-whaley` | Workplace communication coach สไตล์ Corporate Laura — แปลงสถานการณ์ในที่ทำงานเป็น script มืออาชีพ พร้อมใช้ได้ทันที |
| `scorecard` | ประเมินระดับความยากง่ายของงาน IT ทุกสายงาน (Infrastructure, Network, Database, Developer, Security, Cloud, DevOps) พร้อม scorecard 6 มิติ |

### การติดตั้ง

```bash
claude plugin install productive
```

### การเรียกใช้ Skill

```
/tldr
/comeet
/perspective <หัวข้ออบรม>
/ebook <ชื่อหนังสือหรือ URL>
/laura-whaley <สถานการณ์ในที่ทำงาน>
/scorecard <งาน IT ที่ต้องการประเมิน>
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


---

## projects

Plugin สำหรับ **Setup และจัดการ Development Project** — scaffold โครงสร้าง `.claude/` และ `context/` พร้อม skills ครบ workflow ตั้งแต่ init จนถึง ship

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `setup` | Scaffold project structure ใหม่ทั้งหมด: CLAUDE.md, .claude/rules/, .claude/config/, context/ |
| `checkpoint` | สร้าง git safety commit ก่อนให้ Claude ทำงาน ป้องกัน code หาย |
| `add-phase` | เพิ่ม development phase ใหม่พร้อม plan file, backlog, และ archive section |
| `add-task` | เพิ่ม task ใหม่เข้า backlog พร้อม Acceptance Criteria |
| `start-task` | เริ่ม task — ย้ายเข้า sprint และแนะนำ git branch |
| `implement` | Implement task ตาม Acceptance Criteria พร้อมรัน typecheck/lint/test |
| `ship` | ตรวจสอบ pre-merge checklist ก่อน merge branch |
| `done-task` | Mark task ว่าเสร็จแล้ว ย้ายเข้า archive |
| `done-phase` | Mark phase ว่าเสร็จแล้ว เลื่อนไป phase ถัดไป |
| `debug` | วิเคราะห์และแก้ bug ด้วย root cause analysis รองรับ --hotfix |
| `status` | แสดงภาพรวมสถานะโปรเจค — phase, sprint, git status |
| `today` | สรุปงานที่ทำวันนี้ — commits, tasks ที่เสร็จ, และสิ่งที่ค้างอยู่ |
| `list-task` | แสดง backlog ทั้งหมด แยก In Progress / Backlog (High/Med/Low) / Feature Requests |
| `list-phase` | แสดง phases ทั้งหมดพร้อม status — ใส่เลข phase เพื่อดู detail |
| `set-stack` | ตั้งค่า tech stack และ commands — presets: react-vite, python, go, laravel, node-express |

### การติดตั้ง

```bash
claude plugin install projects
```

### การเรียกใช้ Skill

```
/setup "My Project Name" optional description
/checkpoint <task-or-description>
/add-phase "Phase 1: Foundation" 2026-09-01
/add-task <description>
/start-task <TSK-1-001>
/implement <TSK-1-001>
/ship <TSK-1-001>
/done-task <TSK-1-001>
/done-phase
/debug <bug description>
/debug <bug> --hotfix
/status
/today
/list-task
/list-phase
/list-phase 1
/set-stack react-vite
/set-stack python
```

### Workflow มาตรฐาน

```
# 1. เริ่มต้น project ใหม่
/setup "My API Project" REST API for e-commerce platform

# 2. วางแผน phases
/add-phase "Phase 1: Foundation" 2026-08-15

# 3. เพิ่ม tasks
/add-task "Setup JWT authentication middleware"

# 4. เริ่มทำงาน
/start-task TSK-1-001
/checkpoint TSK-1-001
  ... Claude ทำงาน ...
/implement TSK-1-001
/ship TSK-1-001
/done-task TSK-1-001

# 5. ดูสถานะ
/status
/today
/list-task
/list-phase
```

### ไฟล์ที่ /setup สร้าง

```
<project>/
├── CLAUDE.md
├── .claude/
│   ├── config/
│   │   ├── current-phase.md
│   │   ├── task-format.md
│   │   └── tech-stack.md
│   └── rules/
│       ├── git-conventions.md
│       ├── coding-standards.md
│       ├── error-handling.md
│       ├── testing-rules.md
│       ├── security-rules.md
│       └── performance-rules.md
└── context/
    ├── plans/PLAN.md
    ├── tasks/
    │   ├── backlog/
    │   │   └── feature_requests.md
    │   ├── in_progress/current_sprint.md
    │   └── completed/archive.md
    ├── memory/
    └── docs/
```

### เปรียบเทียบ `/kickoff` (masterplan) vs `/setup` (projects)

| ด้าน | `/kickoff` | `/setup` |
|---|---|---|
| Input | Idea ในหัว ยังไม่มีโค้ด | Project name + description |
| Output | masterplan.md blueprint | .claude/ + context/ structure พร้อมใช้งาน |
| Stage | ก่อนเริ่ม code | หลังตัดสินใจเรื่อง stack แล้ว |

> ใช้ร่วมกัน: `/kickoff` แล้ว `/setup` แล้วเริ่ม implement ได้เลย

---

## language

Plugin สำหรับ **เครื่องมือด้านภาษา** — ล่ามแปลภาษาแบบต่อเนื่อง ไม่มีคำอธิบายพ่วง

### Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `translate` | ล่ามแปลภาษาแบบต่อเนื่องระหว่าง 2 ภาษา ตรวจจับภาษาอัตโนมัติ แปลอย่างเดียวไม่มีคำอธิบาย |
| `mentor-english` | ครู English ส่วนตัว รองรับ 5 โหมด: แปล, ตรวจแกรมมา, คิดประโยคตอบกลับ, ปรับ tone, คลังคำศัพท์ |

### การติดตั้ง

```bash
claude plugin install language
```

### การเรียกใช้ Skill

```
/language:translate
/language:translate ไทย ↔ ญี่ปุ่น
/language:mentor-english --translation
/language:mentor-english --grammar
/language:mentor-english --reply
/language:mentor-english --tone
/language:mentor-english --vocab
```

### เปรียบเทียบ `translate` vs `mentor-english`

| ด้าน | `/language:translate` | `/language:mentor-english` |
|---|---|---|
| เป้าหมาย | แปลอย่างเดียว รวดเร็ว | สอนและอธิบายภาษา |
| Output | คำแปลเท่านั้น | คำแปล + word choice + ทางเลือก |
| ใช้เมื่อ | ต้องการล่ามระหว่างสนทนา | ต้องการเรียนรู้ภาษา |
