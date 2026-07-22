# 🎉 GitHub Emoji Reference

GitHub รองรับการใช้ emoji ผ่าน colon-syntax เช่น `:tada:` → 🎉 ได้ทั้งใน commit message, issue, PR comment และไฟล์ markdown

ในการ refactor README ให้เลือก emoji ตาม **ความหมายของ section** ไม่ใช่ตามความชอบ — เพราะ emoji ที่สม่ำเสมอทำให้ผู้อ่านสแกนโครงสร้างได้เร็วและทุก repo ดูเป็น pattern เดียวกัน ไฟล์นี้มี 2 ตารางคนละจุดประสงค์:

- **Section Headers** — emoji หน้าหัวข้อ `### H3` ใน README (ใช้บ่อยที่สุด)
- **Commit Message** — emoji แนะนำเฉพาะเมื่อ README มี section อธิบาย commit convention

ถ้าเจอ section ที่ไม่ตรงกับ mapping หลักเลย ให้เลือก emoji ที่สื่อความหมายของ section นั้นตรงที่สุดด้วยเหตุผล ไม่ใช่หยิบจากลิสต์ตายตัว

## 🎖️ Badges มาตรฐาน (วางใต้ intro paragraph)

Badge มี 2 แบบ: **dynamic** (ดึงข้อมูลจริงจาก endpoint ของ shields.io — อัปเดตอัตโนมัติ) และ **static** (พิมพ์ label/message/color เอง ไม่ผูกกับข้อมูลจริง) — เลือก dynamic ก่อนเสมอถ้ามี endpoint รองรับ

### Dynamic (แนะนำ — ใช้เมื่อมีข้อมูลจริงให้ดึง)

| Badge | URL Pattern | ใช้เมื่อ |
| --- | --- | --- |
| Release version | `https://img.shields.io/github/v/release/{owner}/{repo}` | มี GitHub release/tag |
| npm version | `https://img.shields.io/npm/v/{package}` | เป็น npm package |
| Build / CI status | `https://img.shields.io/github/actions/workflow/status/{owner}/{repo}/{workflow}.yml` | มี GitHub Actions |
| License | `https://img.shields.io/github/license/{owner}/{repo}` | มีไฟล์ LICENSE |
| Code coverage | `https://img.shields.io/codecov/c/github/{owner}/{repo}` | ใช้ Codecov |
| Downloads | `https://img.shields.io/npm/dm/{package}` | เป็น npm package |
| Stars | `https://img.shields.io/github/stars/{owner}/{repo}` | ต้องการโชว์ popularity จริง |
| Last commit | `https://img.shields.io/github/last-commit/{owner}/{repo}` | โชว์ว่า repo ยัง active |
| Open issues | `https://img.shields.io/github/issues/{owner}/{repo}` | โชว์สถานะ maintenance |

### Static (ใช้เฉพาะเมื่อไม่มี endpoint จริงรองรับ)

```markdown
![python](https://img.shields.io/badge/python-3.11-blue)
![status](https://img.shields.io/badge/status-active-brightgreen)
```

> **ห้าม** ใช้ static badge แทน dynamic เมื่อมี endpoint จริงรองรับอยู่แล้ว (เช่น version, license, build status) และ **ห้ามสร้าง badge ที่ไม่มี metric ใดวัดได้จริงรองรับเลย** (เช่น `rating-★★★★★` ที่ไม่มี service ไหนให้ query คะแนน repo ได้จริง) เพราะจะกลายเป็น vanity badge ที่ทำให้ README ดูไม่น่าเชื่อถือ

---

## 🏷️ Section Headers (สำหรับ H3 ในไฟล์ README)

ใช้ mapping นี้เพื่อเลือก emoji ให้ตรงกับหน้าที่ของ section เสมอ:

ลำดับด้านล่างตรงกับลำดับ section จริงใน `references/structure.md`:

| Emoji | Code | Section |
| --- | --- | --- |
| 🎉 Party Popper | `:tada:` | Title (H1) / Initial Commit |
| 💎 Gem | `:gem:` | Repository / About |
| ✨ Sparkles | `:sparkles:` | Features |
| 🔥 Fire | `:fire:` | Performance / Benchmarks |
| 🧊 Ice | `:ice:` | Tech Stack / Folder Structure |
| 🧩 Puzzle Piece | `:jigsaw:` | Integrations / Plugins / Extensions |
| ✅ Check Mark Button | `:white_check_mark:` | Requirements / Prerequisites |
| 🚀 Rocket | `:rocket:` | Setup / Installation |
| ⚙️ Gear | `:gear:` | Configuration / Environment |
| 🔑 Key | `:key:` | API Key / Credentials / Secrets |
| 🐳 Docker | `:whale:` | Deployment |
| 🏆 Trophy | `:trophy:` | Run / Usage |
| 👉🏼 Backhand Index Pointing Right | `:point_right:` | Try it out / Demo |
| 📸 Camera with Flash | `:camera_with_flash:` | Screenshots |
| 📝 Memo | `:memo:` | Document / API Reference |
| 📅 Calendar | `:calendar:` | Schedule / Cron |
| 🧪 Test Tube | `:test_tube:` | Testing |
| ⚠️ Warning | `:warning:` | Fix Error / Troubleshooting |
| 🦄 Unicorn | `:unicorn:` | Roadmap / Future Plans |
| 🙏 Pray | `:pray:` | Contributors / Credits / Thanks |
| ⚡ High Voltage | `:zap:` | New Updates / Changelog |
| 🔔 Bell | `:bell:` | Notifications / Webhooks / Alerts |
| 🛡️ Shield | `:shield:` | Security / Security Policy |
| 📜 Scroll | `:scroll:` | License |
| ✉️ Envelope | `:envelope:` | Contact / Author |
| 🍺 Beer Mug | `:beer:` | Donate / Support / Sponsor |

---

## 💬 Commit Message (สำหรับแนะนำเมื่อ README มี section เกี่ยวกับ convention)

| Emoji | Code | Type |
| --- | --- | --- |
| ✨ Sparkles | `:sparkles:` | feat |
| 🐛 Bug | `:bug:` | fix |
| 📚 Books | `:book:` | docs |
| 🎨 Art | `:art:` | style |
| ♻️ Recycling Symbol | `:recycle:` | refactor |
| ⚡ High Voltage | `:zap:` | perf |
| 🧪 Test Tube | `:test_tube:` | test |
| 📦 Package | `:package:` | build |
| 👷 Construction Worker | `:construction_worker:` | ci |
| 🔧 Wrench | `:wrench:` | chore |

