# Commit Message Emoji Convention

ทุก skill ใน plugin `projects` ที่สร้าง git commit (`checkpoint`, `debug`, `setup`) ใช้ emoji นำหน้า commit message ตาม convention นี้ — รูปแบบ: `<emoji> <type>(<scope>): <คำอธิบาย>`

อ้างอิงจาก [gitmoji](https://gitmoji.dev/) official ผสมกับ Conventional Commits — แบ่งเป็น 2 กลุ่ม: **Core Types** (10 ประเภทหลักที่ใช้บ่อยสุด) และ **Extended** (สถานการณ์เฉพาะเจาะจงที่ core ไม่ครอบคลุม)

## Core Types

| Emoji | Code | Type | ใช้เมื่อ |
| --- | --- | --- | --- |
| ✨ | `:sparkles:` | feat | เพิ่มฟีเจอร์ใหม่ |
| 🐛 | `:bug:` | fix | แก้ bug |
| 📝 | `:memo:` | docs | แก้เอกสาร/comment |
| 💄 | `:lipstick:` | style | ปรับ UI หรือ code formatting (ไม่กระทบ logic) |
| ♻️ | `:recycle:` | refactor | จัดโครงสร้างโค้ดใหม่ (ไม่เปลี่ยน behavior) |
| ⚡ | `:zap:` | perf | ปรับปรุงประสิทธิภาพ |
| ✅ | `:white_check_mark:` | test | เพิ่ม/แก้ automated test |
| 📦 | `:package:` | build | แก้ build system หรือ external dependency |
| 👷 | `:construction_worker:` | ci | แก้ CI pipeline/config |
| 🔧 | `:wrench:` | chore | งานดูแลทั่วไปที่ไม่เข้าประเภทไหนข้างต้น |

## Extended

สำหรับสถานการณ์เฉพาะที่ core types ไม่ครอบคลุมพอ — ใช้แทน core type ตัวใดตัวหนึ่งเมื่อสื่อความหมายได้ตรงกว่า:

| Emoji | Code | ใช้เมื่อ |
| --- | --- | --- |
| 🎉 | `:tada:` | Initial commit ของ repo |
| 🚑️ | `:ambulance:` | Critical hotfix (production emergency) |
| 🎨 | `:art:` | ปรับโครงสร้าง/organize ไฟล์โค้ด (คนละอย่างกับ 💄 style) |
| 🚚 | `:truck:` | ย้ายหรือเปลี่ยนชื่อไฟล์/โฟลเดอร์ |
| 🔥 | `:fire:` | ลบโค้ดหรือไฟล์ทิ้ง |
| ➕ | `:heavy_plus_sign:` | เพิ่ม dependency |
| ➖ | `:heavy_minus_sign:` | ลบ dependency |
| ⬆️ | `:arrow_up:` | อัปเกรด dependency |
| ⬇️ | `:arrow_down:` | ดาวน์เกรด dependency |
| 💚 | `:green_heart:` | แก้ CI ที่ fail |
| 🚀 | `:rocket:` | Deploy |
| 🔒 | `:lock:` | แก้ปัญหาด้าน security |
| 🔐 | `:closed_lock_with_key:` | เพิ่ม/แก้ secrets, credentials |
| 🌐 | `:globe_with_meridians:` | Internationalization / localization |
| ♿ | `:wheelchair:` | Accessibility |
| 💥 | `:boom:` | Breaking changes |
| 🧪 | `:test_tube:` | โค้ด experiment/spike (ไม่ใช่ automated test — ดู ✅ ด้านบน) |

**หมายเหตุการรวม convention:** ไฟล์นี้ย้ายมาจาก `refactor-readme` และขยายด้วย gitmoji official — 3 จุดที่ต่างจาก convention เดิม (ตามที่ผู้ใช้เลือกให้ gitmoji ทับความหมายเดิม): docs เปลี่ยนจาก 📚 → 📝, style เปลี่ยนจาก 🎨 → 💄 (แล้ว 🎨 ไปเป็น "Improve structure" แทน), และ 🧪 เปลี่ยนจาก test → Experiments (เพิ่ม ✅ เป็น emoji ใหม่สำหรับ test แทน เพราะ gitmoji ไม่มี dedicated emoji สำหรับ test ในลิสต์ที่ให้มา — ถ้าไม่ต้องการ ✅ แจ้งได้)
