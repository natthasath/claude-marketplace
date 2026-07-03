# claude-marketplace

รวม Claude Plugins และ Skills สำหรับใช้งานกับ Claude Code

## Plugins

| Plugin | Skills | วัตถุประสงค์ |
|---|---|---|
| `plugin-capacities` | 2 | จัดการ PKM บน Capacities |
| `plugin-project-masterplan` | 5 | วางแผนและวิเคราะห์โปรเจกต์ซอฟต์แวร์ |
| `plugin-refactor` | 3 | ปรับปรุงโค้ด Docker และ Shell Script |
| `plugin-roleplay` | 3 | จำลองบทบาทเพื่อฝึกและวิเคราะห์ |
| `plugin-social-post` | 2 | สร้างโพสต์โซเชียลมีเดีย |

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
claude plugin install natthasath/plugin-capacities
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
claude plugin install natthasath/plugin-project-masterplan
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
claude plugin install natthasath/plugin-refactor
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
claude plugin install natthasath/plugin-roleplay
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
claude plugin install natthasath/plugin-social-post
```
