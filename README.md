# 🎉 natthasath-marketplace

Claude Code plugin marketplace ที่รวม **11 plugins** และ **51 skills** ครอบคลุมงาน PKM, การวางแผนโปรเจกต์, DevOps, การเขียน content, ภาษา, การออกแบบ และ productivity — ติดตั้งผ่านคำสั่งเดียว แล้วเรียกใช้ผ่าน slash command ได้ทันที

![plugins](https://img.shields.io/badge/plugins-11-blue)
![skills](https://img.shields.io/badge/skills-51-brightgreen)
![Claude Code](https://img.shields.io/badge/Claude_Code-marketplace-8A63D2)

### 🚀 Install

```shell
# 1. เพิ่ม marketplace
/plugin marketplace add natthasath/claude-marketplace

# 2. ติดตั้ง plugin ที่ต้องการ
/plugin install capacities@natthasath-marketplace
/plugin install masterplan@natthasath-marketplace
/plugin install refactor@natthasath-marketplace
/plugin install roleplay@natthasath-marketplace
/plugin install social@natthasath-marketplace
/plugin install productive@natthasath-marketplace
/plugin install devops@natthasath-marketplace
/plugin install projects@natthasath-marketplace
/plugin install language@natthasath-marketplace
/plugin install guide@natthasath-marketplace
/plugin install utility@natthasath-marketplace
```

### ⭐ Plugins

| Plugin | Skills | วัตถุประสงค์ |
|---|---|---|
| `capacities` | 5 | จัดการ PKM บน Capacities — Tags, Knowledge Notes และ Text Formatting |
| `masterplan` | 5 | วางแผนและวิเคราะห์โปรเจกต์ซอฟต์แวร์ |
| `refactor` | 4 | ปรับปรุงโค้ด Docker, Shell Script และ README |
| `roleplay` | 4 | จำลองบทบาทเพื่อฝึกและวิเคราะห์ |
| `social` | 2 | สร้างโพสต์โซเชียลมีเดีย |
| `productive` | 8 | เพิ่มประสิทธิภาพการทำงาน Short Summary, Meetings Summary, PDF Downloader, Workplace Communication, IT Work Scorecard, KPI Designer และ Activity Report |
| `devops` | 1 | จัดการ Session Context และ DevOps Workflow |
| `projects` | 15 | Setup และจัดการ development project — scaffold ครบ workflow ตั้งแต่ init จนถึง ship |
| `language` | 2 | เครื่องมือด้านภาษา — ล่ามแปลภาษาแบบต่อเนื่อง และ English Mentor |
| `guide` | 3 | แนะนำ Design Style, Font Pairing, Web Design และ Note-taking Pattern |
| `utility` | 2 | จัดการ OS Setup และ Config Snapshot — รองรับ Windows 11, macOS, Linux Ubuntu |

### ⚓ Folder Structure

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

Skills ใช้ระบบโหลด 3 ระดับ (Progressive Disclosure):

| ระดับ | เนื้อหา | เมื่อโหลด |
|---|---|---|
| 1 | `name` + `description` (frontmatter) | ทุกครั้งใน context (~100 words) |
| 2 | SKILL.md body | เมื่อ skill ถูก trigger |
| 3 | Bundled resources (scripts/references/assets) | เมื่อ skill เรียกใช้งาน |

---

## 📦 capacities

Plugin สำหรับ **Capacities PKM** — ออกแบบ Space, Object Types, Tags, Collections, Knowledge Notes และ Text Formatting

### ⭐ Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `mood-tag` | วิเคราะห์อารมณ์จาก Daily Notes และแนะนำ Mood Tag ตาม Yale Mood Meter Framework |
| `movies-tag` | วิเคราะห์ genre/theme ของหนัง และแนะนำ Genre Tags สำหรับ Capacities |
| `glossary` | อธิบายความหมายตัวย่อหรือศัพท์เทคนิค (Abbreviations / Acronyms) แบบ 1 paragraph |
| `knowledge` | สร้าง Knowledge Note พร้อม frontmatter และ sections ที่เป็นระบบ |
| `highlight` | แปลงข้อความธรรมดาให้อ่านง่ายขึ้นด้วย bold, italic, code, highlight, underline |

### 💎 Yale Mood Meter Zones

| โซน | Valence | Arousal | ตัวอย่าง |
|---|---|---|---|
| 🟡 Yellow | บวก | สูง | `#mood-joyful`, `#mood-excited` |
| 🔴 Red | ลบ | สูง | `#mood-stressed`, `#mood-frustrated` |
| 🟢 Green | บวก | ต่ำ | `#mood-calm`, `#mood-reflective` |
| 🔵 Blue | ลบ | ต่ำ | `#mood-sad`, `#mood-unsettled` |

### 💎 Highlight Formatting Guide

| Formatting | Markdown | ใช้เมื่อ |
|---|---|---|
| **ตัวหนา** | `**text**` | คำสำคัญ, แนวคิดหลัก, ชื่อที่ต้องจำ |
| *ตัวเอียง* | `*text*` | ชื่อสื่อ, คำต่างชาติ, นิยามครั้งแรก |
| `code` | `` `text` `` | command, path, ค่า technical |
| ==highlight== | `==text==` | คำเตือน, deadline, ห้ามพลาด (🟡 เหลือง) |
| <u>underline</u> | `<u>text</u>` | คำที่กำลัง define, proper noun พิเศษ |

---

## 📦 masterplan

Plugin สำหรับ **วางแผนและวิเคราะห์โปรเจกต์** — ครอบคลุมตั้งแต่ Requirement จนถึง Architecture และ Database Design

### ⭐ Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `kickoff` | ช่วยนักพัฒนาวางแผนไอเดียแอปผ่านการสนทนา และสร้าง `masterplan.md` |
| `gather` | เก็บรวบรวม Business และ Technical Requirements จาก Stakeholders อย่างเป็นระบบ |
| `analyze` | แปลง Business Needs เป็น Functional และ Technical System Requirements |
| `architect` | เลือกและกำหนด IT Architecture ที่จะใช้ ครอบคลุม Infrastructure, Application และ Integration Strategy |
| `database` | ออกแบบ Database Schema สำหรับ PostgreSQL และ Laravel พร้อม Migration-ready guidance |

### 💎 /kickoff vs /init

| ด้าน | `/kickoff` | `/init` (Claude Code built-in) |
|---|---|---|
| **Input** | Idea ในหัว ยังไม่มีโค้ด | Codebase ที่มีอยู่แล้ว |
| **Output** | `masterplan.md` (blueprint สำหรับ developer) | `CLAUDE.md` (ให้ Claude เข้าใจ repo) |
| **Stage** | ก่อนเริ่ม code เลย | หลัง project มีอยู่แล้ว |
| **วัตถุประสงค์** | วางแผน project ใหม่จากศูนย์ | Document codebase ที่มี |

> `/kickoff` คือสิ่งที่ทำ **ก่อน** `/init` — เปลี่ยน idea ให้เป็นแผน แล้วค่อย init repo

---

## 📦 refactor

Plugin สำหรับ **ปรับปรุงคุณภาพโค้ดและเอกสาร** — เน้น Docker, Shell Script และ README ให้เป็น Production-ready

### ⭐ Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `refactor-compose` | Refactor `docker-compose.yml` และ `.env` ให้เป็น Best Practice |
| `refactor-dockerfile` | สร้างและ Refactor `Dockerfile` ให้มี Security, Performance และ Layer Caching ที่ดี |
| `refactor-shell` | สร้างและ Refactor Shell Script ให้มี Error Handling, Logging และโครงสร้างมาตรฐาน |
| `refactor-readme` | Refactor `README.md` ให้เป็น pattern มาตรฐาน อ่านง่าย ดู minimal แบบ open-source repo พร้อม emoji convention |

### 💎 README Section Emoji Convention

| Emoji | Section | Emoji | Section |
|---|---|---|---|
| 🎉 | Title | 🚀 | Setup |
| ⭐ | Features | 🏆 | Run |
| ✅ | Requirements | 👉🏼 | Try it out |
| 🔑 | Configuration | 🔨 | Fix Error |
| ⚡ | New Updates | 💎 | Document |

---

## 📦 roleplay

Plugin สำหรับ **จำลองบทบาท** — ฝึกทักษะการสัมภาษณ์ การสอบสวน การตัดสินใจเชิงยุทธศาสตร์ และการสนทนาภาษาอังกฤษ

### ⭐ Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `roleplay-interview` | จำลองนักสัมภาษณ์งานที่ใช้คำถาม Behavioral และ Psychological Probing |
| `roleplay-investigator` | จำลองเจ้าหน้าที่สืบสวนที่ใช้ Reid Technique และ PEACE Model |
| `roleplay-president` | จำลองผู้ช่วยประธานาธิบดีสำหรับวิเคราะห์นโยบายและวางแผนยุทธศาสตร์ |
| `roleplay-english` | ฝึกสนทนาภาษาอังกฤษผ่าน scenario จริง: Interview, Meeting, Customer, Small Talk, Email, Negotiation |

---

## 📦 social

Plugin สำหรับ **สร้างโพสต์โซเชียลมีเดีย** — เน้น Thought Leadership และ Personal Branding

### ⭐ Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `post-facebook` | เขียนโพสต์ Facebook ภาษาไทยแนว Thought Leadership จริงจังปนกวนเล็กน้อย |
| `post-linkedin` | เขียนโพสต์ LinkedIn ภาษาอังกฤษสายไอทีและเทคโนโลยี เพื่อ Personal Branding |

---

## 📦 productive

Plugin สำหรับ **เพิ่มประสิทธิภาพการทำงาน** — Short Summary, Meetings Summary, PDF Downloader, Workplace Communication Coach, IT Work Scorecard, KPI Designer และ Activity Report

### ⭐ Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `tldr` | สรุปข้อมูลบริการหรือเทคโนโลยีแบบกระชับ พร้อม Key Features และ Real-world Example |
| `comeet` | สรุปการประชุมเป็นโครงสร้างมาตรฐาน: Objective, Key Topics, Discussions, Decisions, Action Items และ Next Step |
| `perspective` | ให้มุมมองและข้อคิดจากหัวข้ออบรม เขียนในเสียงของ Senior Engineer — เจ็บแต่จริง ไม่ใช่สไตล์ HR |
| `ebook` | ค้นหาและดาวน์โหลดไฟล์ PDF จากแหล่งที่น่าเชื่อถือและถูกกฎหมาย รองรับทั้งค้นหาจากชื่อและดาวน์โหลดจาก URL |
| `laura-whaley` | Workplace communication coach สไตล์ Corporate Laura — แปลงสถานการณ์ในที่ทำงานเป็น script มืออาชีพ พร้อมใช้ได้ทันที |
| `scorecard` | ประเมินระดับความยากง่ายของงาน IT ทุกสายงาน (Infrastructure, Network, Database, Developer, Security, Cloud, DevOps) พร้อม scorecard 6 มิติ |
| `kpi` | ออกแบบ KPI และตัวชี้วัดสำหรับ Action Plan — รับกิจกรรมแล้วแนะนำตัวชี้วัด เกณฑ์ความสำเร็จ เป้าหมาย และวิธีวัดผล |
| `activity-report` | สรุปความคืบหน้ากิจกรรมในแผนการปฏิบัติงานประจำปีของสำนัก — ถามข้อมูลครบ 5W (แผน / ทำ / ได้ / ติด / ต่อ) แล้วสรุปเป็น 1 paragraph ภาษาทางการ |

### 🏆 Usage

```
/tldr
/comeet
/perspective <หัวข้ออบรม>
/ebook <ชื่อหนังสือหรือ URL>
/laura-whaley <สถานการณ์ในที่ทำงาน>
/scorecard <งาน IT ที่ต้องการประเมิน>
/kpi <กิจกรรมหรือโปรเจกต์ที่ต้องการวางตัวชี้วัด>
/activity-report <ชื่อกิจกรรม>
```

---

## 📦 devops

Plugin สำหรับ **DevOps Workflow** — จัดการ Session Context และเพิ่มประสิทธิภาพการทำงานกับ Claude Code

### ⭐ Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `session-name` | ตั้งชื่อ session ปัจจุบัน บันทึกลง memory และแสดง context สำหรับอ้างอิงในการสนทนา |

---

## 📦 projects

Plugin สำหรับ **Setup และจัดการ Development Project** — scaffold โครงสร้าง `.claude/` และ `context/` พร้อม skills ครบ workflow ตั้งแต่ init จนถึง ship

### ⭐ Skills

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

### 🔁 Workflow

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

### 💎 Files created by /setup

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

### 💎 /kickoff vs /setup

| ด้าน | `/kickoff` | `/setup` |
|---|---|---|
| Input | Idea ในหัว ยังไม่มีโค้ด | Project name + description |
| Output | masterplan.md blueprint | .claude/ + context/ structure พร้อมใช้งาน |
| Stage | ก่อนเริ่ม code | หลังตัดสินใจเรื่อง stack แล้ว |

> ใช้ร่วมกัน: `/kickoff` แล้ว `/setup` แล้วเริ่ม implement ได้เลย

---

## 📦 language

Plugin สำหรับ **เครื่องมือด้านภาษา** — ล่ามแปลภาษาแบบต่อเนื่อง ไม่มีคำอธิบายพ่วง

### ⭐ Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `translate` | ล่ามแปลภาษาแบบต่อเนื่องระหว่าง 2 ภาษา ตรวจจับภาษาอัตโนมัติ แปลอย่างเดียวไม่มีคำอธิบาย |
| `mentor-english` | ครู English ส่วนตัว รองรับ 5 โหมด: แปล, ตรวจแกรมมา, คิดประโยคตอบกลับ, ปรับ tone, คลังคำศัพท์ |

### 🏆 Usage

```
/language:translate
/language:translate ไทย ↔ ญี่ปุ่น
/language:mentor-english --translation
/language:mentor-english --grammar
/language:mentor-english --reply
/language:mentor-english --tone
/language:mentor-english --vocab
```

### 💎 translate vs mentor-english

| ด้าน | `/language:translate` | `/language:mentor-english` |
|---|---|---|
| เป้าหมาย | แปลอย่างเดียว รวดเร็ว | สอนและอธิบายภาษา |
| Output | คำแปลเท่านั้น | คำแปล + word choice + ทางเลือก |
| ใช้เมื่อ | ต้องการล่ามระหว่างสนทนา | ต้องการเรียนรู้ภาษา |

---

## 📦 guide

Plugin สำหรับ **ให้คำแนะนำและจับคู่ตัวเลือกที่เหมาะสม** — Design Style, Font Pairing, Web Design และ Note-taking Pattern

### ⭐ Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `creative-book` | แนะนำ Design Style + Font Pairing (ไทย/อังกฤษ) สำหรับ presentation, report, สื่อสิ่งพิมพ์ — 42 สไตล์ |
| `creative-web` | แนะนำ Design Style สำหรับเว็บไซต์ พร้อม Font, Color Palette (hex) และเว็บอ้างอิงจริง — 20 สไตล์ |
| `note-taking` | แนะนำ Pattern การจดโน้ตที่เหมาะกับงาน เช่น Cornell, Zettelkasten, PARA, Outline |

### 🏆 Usage

```
/guide:creative-book
/guide:creative-web
/guide:note-taking
```

### 💎 creative-book vs creative-web

| ด้าน | `/guide:creative-book` | `/guide:creative-web` |
|---|---|---|
| เป้าหมาย | งานสิ่งพิมพ์/นำเสนอ (slide, report) | เว็บไซต์ (landing page, web UI) |
| Output | Design Style + Font Pairing | Design Style + Font + Color Palette (hex) + เว็บอ้างอิง |
| ใช้เมื่อ | ทำ slide/report/pitch deck | ออกแบบเว็บให้เห็นภาพจากเว็บจริง |

### 💎 Web Design Styles

| Style | เหมาะกับ | เว็บอ้างอิง |
|---|---|---|
| Minimal | Portfolio, Startup, Blog | [Apple](https://apple.com) |
| Modern SaaS | SaaS, AI, Dashboard | [Stripe](https://stripe.com) |
| Glassmorphism | AI, Creative, Portfolio | [Linear](https://linear.app) |
| Dark Modern | Dashboard, AI | [Vercel](https://vercel.com) |
| Luxury | Jewelry, Hotel | [Rolex](https://www.rolex.com) |
| E-commerce | Shopping | [Nike](https://www.nike.com) |

---

## 📦 utility

Plugin สำหรับ **จัดการ OS Setup และ Config Snapshot** — บันทึกโครงสร้างระบบส่วนตัว และ export การตั้งค่าโปรแกรม รองรับ Windows 11, macOS (Mac Mini M4) และ Linux Ubuntu Desktop 24.04

### ⭐ Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `os-design` | สัมภาษณ์ผู้ใช้และสร้าง `os-profile.md` — บันทึก drive layout, paths, naming convention, software และ shared conventions ครบทุก OS |
| `snapshot-config` | Export และ snapshot การตั้งค่าโปรแกรม พร้อมแนะนำการตั้งค่าที่เหมาะสมตาม OS และ workflow ของผู้ใช้ |

### 🏆 Usage

```
/utility:os-design
/utility:snapshot-config <ชื่อโปรแกรม>
```

### 🔁 Workflow

```
# ครั้งแรก: skill จะถามตั้งค่า path ก่อนอัตโนมัติ
# (os-profile.md บันทึกที่ไหน, snapshots บันทึกที่ไหน)

# 1. บันทึกโครงสร้าง OS ครั้งแรก (หรืออัปเดตเมื่อ setup เปลี่ยน)
/utility:os-design

# 2. Snapshot config โปรแกรมที่ต้องการ
/utility:snapshot-config VSCode
/utility:snapshot-config Git
/utility:snapshot-config Windows Terminal
```

### 💎 Files created

```
~/.config/claude-utility/
└── settings.json                  ← Path config (สร้างครั้งแรกอัตโนมัติ)

<os_profile_path>/                 ← default: plugins/utility/references/os-profile.md
└── os-profile.md                  ← โครงสร้าง OS ส่วนตัว (สร้างโดย os-design)

<snapshots_base_path>/             ← default: plugins/utility/snapshots/
└── <program-name>/
    └── <YYYY-MM-DD>/
        ├── snapshot.md            ← สรุป config + คำแนะนำ
        ├── settings.json          ← config จริง (ถ้าเข้าถึงได้)
        ├── extensions.txt         ← รายการ extensions (ถ้ามี)
        └── restore-guide.md       ← วิธี restore บนเครื่องใหม่
```
