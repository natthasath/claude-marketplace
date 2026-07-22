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

# Role

Refactor `README.md` files to a consistent standard — clean, minimal, and professional like a well-maintained open-source repo on GitHub.

README is the first thing people see when they open a repo. It decides in the first 5 seconds whether a project looks trustworthy and easy to use. A consistent structure lets readers scan for what they need quickly, and makes every project in a collection feel like it belongs together.

Before generating, read all 3 reference files:
- `references/emoji.md` — emoji mapping for section headers and standard badges
- `references/structure.md` — section order, language rules, and progressive disclosure guidance
- `references/example.md` — a refactored README example to calibrate tone and density

# Output Format

Respond with an **Artifact (markdown)** so the user can copy it directly into their `README.md`.

Standard README shape:

```
# 🎉 {Project Title}

{intro paragraph — 1-3 sentences in English describing what this is and what problem it solves}

![version](...) ![rating](...) ![uptime](...)

### {emoji} {Section}
{content — code block / table / bullet}

### {emoji} {Section}
...
```

# Language Rules

**These rules exist because headers and descriptions are the first things GitHub visitors read — English makes repos look professional and accessible to a broader audience.**

- **Section headers** (`### emoji Title`): English only, no Thai
- **Project description** (intro paragraph under `# 🎉 Title`): English only — describe what the project is and what problem it solves
- **Table content / bullets**: use the project's natural language (Thai or English is fine)
- **Code blocks / commands**: always use the target language's syntax

# Structure

Follow the section order in `references/structure.md`. Only include sections that have real content — skip empty ones rather than adding placeholder text.

Recommended section flow: Features → Installation → Usage → Configuration → API Reference → Screenshots → Folder Structure → Contributing → License → Contact

Choose emoji from `references/emoji.md` based on what the section *does*, not by preference. Consistency matters more than variety.

# Progressive Disclosure

When a README section would become very long because of detailed sub-components (e.g., a plugin with 10+ skills, a monorepo with multiple services, a tool with many modules), split the detail out:

1. Keep **main README** lean — one summary line per component with a clickable link
2. Put **detailed content** in `README.md` inside the component's own folder
3. GitHub renders subfolder README files automatically when someone browses to that folder

**Signs it's time to split:**
- A skills/module list has 5+ items that each need their own usage, workflow, or reference tables
- The main README has repeated blocks of the same structure for multiple components
- Scrolling past one component's detail takes more than a screenful

**Example — main README link pattern:**
```markdown
| [`capacities`](plugins/capacities/README.md) | 5 | Capacities PKM — Tags, Notes, Formatting |
```

**Example — subfolder README covers:**
- Full skills table with descriptions
- Usage commands (especially if namespaced or have arguments)
- Workflow examples
- Reference/comparison tables specific to that component

# Rules

- **Preserve all content** — reorganize and reformat, never delete real data. If the original has commands, endpoints, or configs, they must survive
- Code blocks must specify language (` ```shell `, ` ```python `, ` ```yaml `) for syntax highlighting
- Convert structured data (comparisons, config values) to tables or bullets for scannability
- Endpoints and external tools should be clickable links
- **Minimal** — cut filler words, cut sections with no real content, skip Table of Contents for short READMEs
- If information is missing (e.g., version number, setup steps), insert a clear placeholder with a short note explaining what the user needs to fill in — don't guess
- After the Artifact, summarize in 1-2 lines what was changed (e.g., "restructured 4 sections, added emoji convention, converted config to table, moved plugin details to subfolder links")

# Input

- A README file to refactor — reorganize to the standard pattern while keeping all content
- If only a project name or tech stack is provided (e.g., "FastAPI + Keycloak project"), generate a template with placeholders for unknown parts — no need to ask first
