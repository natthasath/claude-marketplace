# Naming Convention Examples

เอกสารนี้แสดงตัวอย่าง naming convention แต่ละแบบ พร้อม use case ที่เหมาะสม

---

## 1. kebab-case
ตัวพิมพ์เล็กทั้งหมด คั่นด้วยขีด `-`

```
my-project-folder/
react-web-app/
config-backup-2024/
setup-notes.md
api-client.ts
user-profile.json
```

**เหมาะกับ:** Folder ชื่อ project, URL slug, npm package, CSS class, ไฟล์ Markdown/HTML

---

## 2. snake_case
ตัวพิมพ์เล็กทั้งหมด คั่นด้วยขีดล่าง `_`

```
my_project_folder/
user_profile/
backup_2024_07/
config_file.py
api_client.go
database_schema.sql
```

**เหมาะกับ:** Python files, database column names, ชื่อ variable ใน Python/Ruby

---

## 3. PascalCase (UpperCamelCase)
ขึ้นต้นทุก word ด้วยตัวพิมพ์ใหญ่

```
MyProject/
UserProfile/
ConfigManager/
ApiClient.cs
DatabaseSchema.java
UserController.ts
```

**เหมาะกับ:** Class names, Component names (React), C# files, Java files

---

## 4. camelCase (lowerCamelCase)
ขึ้นต้น word แรกด้วยตัวพิมพ์เล็ก word ถัดไปตัวพิมพ์ใหญ่

```
myProject/
userProfile/
configManager/
apiClient.js
getUserData.ts
handleSubmit.js
```

**เหมาะกับ:** JavaScript/TypeScript variable, function names, JSON keys

---

## 5. SCREAMING_SNAKE_CASE
ตัวพิมพ์ใหญ่ทั้งหมด คั่นด้วยขีดล่าง `_`

```
MAX_RETRY_COUNT
API_BASE_URL
DATABASE_HOST
DEFAULT_TIMEOUT_MS
```

**เหมาะกับ:** Constants, Environment variables, Config keys

---

## 6. dot.notation
คั่นด้วยจุด `.`

```
config.production.json
app.settings.json
api.v2.config.js
database.migration.sql
```

**เหมาะกับ:** Config files ที่มี environment (dev/staging/prod), versioned files

---

## 7. Date-prefix Format
นำหน้าด้วยวันที่ เรียง chronologically ได้

```
2024-07-18_meeting-notes.md
2024-07-18_backup-config.zip
20240718_report.pdf
2024-07_monthly-summary.md
```

**เหมาะกับ:** Log files, Meeting notes, Backup files, รายงาน

---

## 8. Version-suffix Format
ต่อท้ายด้วย version number

```
project-v1.0/
config-v2.1.json
backup-final-v3/
design-mockup-v1.2.fig
```

**เหมาะกับ:** Versioned backups, Design files, Release packages

---

## 9. Mixed Pattern (ตัวอย่างการใช้ร่วมกัน)

```
projects/
├── web-apps/                    ← kebab-case (folder)
│   └── my-react-app/           ← kebab-case (project folder)
│       ├── src/
│       │   ├── components/
│       │   │   └── UserProfile.tsx    ← PascalCase (React component)
│       │   ├── hooks/
│       │   │   └── useAuthToken.ts    ← camelCase (hook)
│       │   └── utils/
│       │       └── api-client.ts      ← kebab-case (util file)
│       └── config/
│           ├── app.dev.json           ← dot.notation (env config)
│           └── app.prod.json
├── scripts/
│   └── backup_config.sh         ← snake_case (shell script)
└── docs/
    └── 2024-07-18_setup-guide.md ← date-prefix (doc file)
```

---

## Quick Reference

| Style | ตัวอย่าง | ใช้กับ |
|-------|---------|--------|
| kebab-case | `my-project` | Folders, URLs, npm, Markdown |
| snake_case | `my_project` | Python, SQL, shell vars |
| PascalCase | `MyProject` | Classes, React components |
| camelCase | `myProject` | JS/TS vars, JSON keys |
| SCREAMING_SNAKE | `MY_PROJECT` | Constants, ENV vars |
| dot.notation | `my.project` | Config files |
| date-prefix | `2024-07-18_name` | Logs, notes, backups |
| version-suffix | `name-v1.0` | Releases, versioned files |
