# หลักการออกแบบตัวชี้วัด

## SMART Framework

ตัวชี้วัดที่ดีต้องผ่านหลักทั้ง 5 ข้อนี้:

| หลัก | ความหมาย | ตัวอย่างที่ดี | ตัวอย่างที่ไม่ดี |
|------|----------|--------------|----------------|
| **Specific** | ระบุชัดว่าวัดอะไร ไม่กว้างเกินไป | อัตราการตอบสนอง Ticket ภายใน 4 ชม. | "บริการลูกค้าดีขึ้น" |
| **Measurable** | มีหน่วยวัดและวิธีวัดที่ทำได้จริง | %, จำนวนครั้ง, ชั่วโมง, บาท | "มีคุณภาพสูง" |
| **Achievable** | ท้าทายแต่ไม่เกินเอื้อม | ≥85% จากเดิม 70% | 100% ทุกกรณีไม่มี context |
| **Relevant** | ตรงกับวัตถุประสงค์ของกิจกรรม | วัด defect rate สำหรับงาน QA | วัด attendance สำหรับงาน QA |
| **Time-bound** | กำหนดช่วงเวลาและความถี่ชัดเจน | รายเดือน, รายไตรมาส | "เมื่อเสร็จแล้ว" |

---

## แนวทางตาม Domain

### ระดับองค์กร
- พิจารณา OKR (Objective + Key Results) ควบคู่ — Objective คือทิศทาง, Key Results คือตัวชี้วัด
- เน้น outcome (ผลลัพธ์) มากกว่า output (ผลผลิต)

### IT / Tech Project
- รวม SLA (availability, response time, error rate) ตามความเหมาะสม
- เพิ่ม MTTR (Mean Time to Recover) และ MTBF (Mean Time Between Failures) สำหรับ infrastructure
- ระบุ monitoring tool ที่จะใช้วัด (เช่น Grafana, Datadog, Jira)

### HR / People Development
- รวม engagement score, retention rate, time-to-complete
- วัด behavior change ไม่ใช่แค่จำนวนการอบรม (เช่น "นำไปประยุกต์ใช้ภายใน 30 วัน")
- Pre/Post assessment score เหมาะสำหรับงาน training

### Operations / Process
- ใช้ cycle time, throughput, defect rate
- เน้น process efficiency ไม่ใช่แค่ effort

---

## Pitfall ที่พบบ่อย

- **วัดง่ายแต่ไม่ตรงจุด** — เช่น วัดจำนวนชั่วโมงอบรมแทนที่จะวัดว่าเอาไปใช้ได้จริงไหม
- **KPI มากเกินไป** — 3-5 ตัวต่อกิจกรรมคือขีดจำกัดที่บริหารได้จริง
- **เป้าหมาย 100% โดยไม่มี baseline** — ทำให้ทีมไม่กล้ารายงานตามจริง
- **ไม่ระบุ data source** — ตัวชี้วัดที่ไม่รู้ว่าดึงข้อมูลจากไหน มักถูกข้ามเมื่อถึงเวลาวัดจริง
