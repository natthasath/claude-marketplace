# README Structure Reference

ลำดับ section มาตรฐานสำหรับ README.md ทุกประเภทโปรเจกต์ ใช้ลำดับนี้เป็น default — ตัด section ที่ไม่มีเนื้อหาจริงออก ไม่ต้องใส่ placeholder ว่าง

## Section Order

| # | Section | Emoji | Required | เมื่อใส่ |
|---|---|---|---|---|
| 1 | Project Name | 🎉 | ✅ | เสมอ (H1 title) |
| 2 | Description | — | ✅ | เสมอ (intro paragraph ใต้ title) |
| 3 | Features | ⭐ | เมื่อมี | มีฟีเจอร์เด่นที่ต้องการ highlight |
| 4 | Installation | 🚀 | ✅ | เสมอ (ถ้าไม่มีขั้นตอนให้ใส่คำสั่งเดียว) |
| 5 | Usage | 🏆 | ✅ | ตัวอย่างการใช้งาน + code snippet |
| 6 | Configuration | 🔑 | เมื่อมี | มี `.env`, `config.json` หรือ env vars |
| 7 | API Reference | 💎 | เมื่อมี | มี endpoint หรือ public function หลัก |
| 8 | Screenshots | 📸 | เมื่อมี | มี UI หรือ CLI output ที่ช่วยให้เห็นภาพ |
| 9 | Folder Structure | ⚓ | เมื่อมี | โปรเจกต์ซับซ้อนหรือมีหลาย module |
| 10 | Contributing | 👉🏼 | เมื่อมี | repo เปิดรับ contribution |
| 11 | License | ✅ | เมื่อมี | ระบุประเภท License เช่น MIT |
| 12 | Contact / Author | 💘 | เมื่อมี | ช่องทางติดต่อหรือชื่อผู้พัฒนา |

## Progressive Disclosure — เมื่อ section ยาวเกินไป

เมื่อ README มีเนื้อหาที่ละเอียดมากในระดับ sub-component (เช่น plugin ย่อย, module, หรือ service แต่ละตัว) ให้แยกออกเป็น `README.md` ในโฟลเดอร์ย่อยนั้น แล้ว link กลับมาจาก main README

**สัญญาณที่ควรแยก:**
- Skills table หรือ component list มีมากกว่า 5 รายการที่แต่ละอันต้องการ detail ของตัวเอง
- มี Workflow, comparison table หรือ reference ที่เฉพาะกับ sub-component นั้น
- Main README มีเนื้อหาซ้ำซ้อนในหลาย section สำหรับ component เดียวกัน

**วิธีทำ:**
```
# แทนที่จะขยาย main README ให้ยาว:
main README → สรุป 1 บรรทัดต่อ component + link

# ตัวอย่าง main README:
| [`capacities`](plugins/capacities/README.md) | 5 | Capacities PKM — Tags, Notes, Formatting |

# ตัวอย่าง sub-folder README:
plugins/capacities/README.md → Skills table + Usage + reference tables ทั้งหมด
```

## Language Rules

- **Section headers**: English เท่านั้น — ไม่ใช้ภาษาไทยเป็นหัวข้อ
- **Project description** (intro paragraph ใต้ title): English เท่านั้น — อธิบายว่าโปรเจกต์คืออะไร แก้ปัญหาอะไร
- **เนื้อหาใน table / bullet**: ใช้ภาษาตาม context ของโปรเจกต์ได้ (Thai หรือ English)
- **Code block / command**: English / syntax ของภาษานั้นๆ เสมอ

เหตุผล: header และ description เป็นสิ่งแรกที่คนอ่าน GitHub เจอ — English ทำให้ repo ดู professional และ accessible กับ audience ที่กว้างกว่า
