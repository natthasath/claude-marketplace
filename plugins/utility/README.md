# 🎉 utility

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

```shell
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
