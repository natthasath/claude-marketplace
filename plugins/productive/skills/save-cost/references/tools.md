# Token-Saving CLI Tools Reference

รายการ CLI tools ที่ช่วยลดการใช้ token ระหว่าง Claude ทำงาน แบ่งเป็น 3 กลุ่มตามความปลอดภัยในการให้ Claude เรียกใช้เอง — **อ่านหัวข้อ "กลุ่มเครื่องมือ" ก่อนเสมอ** ก่อนจะเสนอ checklist ให้ผู้ใช้เลือก

## กลุ่มเครื่องมือ (สำคัญมาก — อ่านก่อน)

- **กลุ่ม A — Claude เรียกใช้ตรงได้ปลอดภัย**: เป็นคำสั่งที่รันแล้วจบ (non-interactive) ให้ผลลัพธ์แล้ว return ทันที เหมาะให้ Claude เรียกผ่าน Bash เองระหว่างทำงาน
- **กลุ่ม B — ติดตั้งได้ แต่ประโยชน์หลักคือสำหรับคน ไม่ใช่ Claude**: ไม่มีความเสี่ยงจะค้าง แต่ Claude มักมี built-in tool (Read/Glob/Grep) ที่ทำงานคล้ายกันอยู่แล้ว หรือประโยชน์หลัก (สี, interactive) มีไว้เพื่อให้คนอ่านสบายตา
- **กลุ่ม C — ห้าม Claude เรียกโดยตรงเด็ดขาด**: เป็นโปรแกรมแบบ full-screen (TUI) หรือ long-running process ที่รอ input จากคนหรือไม่จบเอง ถ้า Claude สั่งผ่าน Bash ตรงๆ จะทำให้ session ค้าง ติดตั้งได้สำหรับให้ผู้ใช้ (คน) เปิดใช้เองในเทอร์มินัลแยกเท่านั้น

เวลาเขียน guidance ลง CLAUDE.md ให้ระบุกลุ่มนี้กำกับไว้ด้วยเสมอ เพื่อไม่ให้ Claude ในอนาคตพยายามเรียกเครื่องมือกลุ่ม C ตรงๆ

---

## กลุ่ม A — Claude เรียกใช้ตรงได้ (ประหยัด token จริง ไม่มี built-in tool ทดแทน)

| Tool | ใช้แทน | ลด Token เพราะอะไร | Priority |
|---|---|---|---|
| `gh` | Web Search / Browser | ดึงเฉพาะ JSON จาก GitHub API ไม่ต้องอ่าน HTML | ⭐⭐⭐⭐⭐ |
| `jq` | เขียน Python เพื่อ parse JSON | กรอง JSON เฉพาะ field ที่ต้องการก่อนเข้า context | ⭐⭐⭐⭐⭐ |
| `ast-grep` | grep ปกติสำหรับหาโค้ด | ค้นหาตามโครงสร้าง AST แม่นยำ ไม่ต้องอ่านทั้งไฟล์เพื่อกรองเอง | ⭐⭐⭐⭐⭐ |
| `uv` | pip | ติดตั้ง/resolve package เร็วกว่า log สั้นกว่ามาก | ⭐⭐⭐⭐⭐ |
| `yq` | เขียน Python เพื่อ parse YAML | กรอง YAML (GitHub Actions, K8s manifest) ก่อนเข้า context | ⭐⭐⭐⭐ |
| `git-delta` | `git diff` เปล่า | จัดรูปแบบ diff ให้อ่านง่าย ส่งเฉพาะส่วนเปลี่ยนแปลงที่ชัดเจน (ต้อง config เพิ่ม) | ⭐⭐⭐⭐ |
| `shellcheck` | ให้ Claude debug เอง | เจอ error ใน shell script ทันที ไม่ต้องรันแล้วอ่าน error log ยาวๆ หลายรอบ | ⭐⭐⭐⭐ |
| `just` | อธิบาย workflow หลายขั้นตอนซ้ำๆ | รวม workflow เป็นคำสั่งเดียว ไม่ต้องพิมพ์คำสั่งยาวซ้ำทุกครั้ง | ⭐⭐⭐⭐ |
| `bun` | node + npm | รันและติดตั้ง package เร็วกว่า log สั้นกว่า | ⭐⭐⭐⭐ |
| `tldr` | `man <cmd>` | ตัวอย่างการใช้คำสั่งแบบสั้น กระชับ แทน man page ที่ยาวมาก | ⭐⭐⭐⭐ |
| `duckdb` | เปิดไฟล์ CSV/JSON/Parquet เต็มไฟล์ | query ด้วย SQL ได้ผลลัพธ์เฉพาะที่ต้องการ ไม่ต้อง dump ทั้งไฟล์เข้า context | ⭐⭐⭐⭐ |
| `sd` | `sed` | syntax ง่ายกว่า ลด error/retry รอบที่ Claude ต้องแก้ regex | ⭐⭐⭐ |
| `xh` | `curl` (เพื่อดู response ยาวๆ) | จัดรูปแบบ HTTP response ให้อ่านง่าย กรอง header/body ได้ | ⭐⭐⭐ |
| `dust` | `du` | สรุปการใช้ disk แบบย่อ ไม่ต้อง parse output ยาว | ⭐⭐ |
| `procs` | `ps` | รายการ process อ่านง่ายกว่า คอลัมน์ชัดเจน | ⭐⭐ |
| `tokei` | ไล่อ่านทุกไฟล์เพื่อสรุปภาพรวม repo | สรุปจำนวนบรรทัด/ภาษาทั้ง repo ในคำสั่งเดียว ไม่ต้องเปิดไฟล์ทีละไฟล์ | ⭐⭐⭐ |
| `difftastic` | diff บรรทัดต่อบรรทัด | diff แบบ structural/AST-aware อ่านง่ายกว่าสำหรับโค้ดที่ reformat | ⭐⭐⭐ |
| `pup` | โหลดหน้า HTML เต็มหน้ามาอ่าน | query ด้วย CSS selector คล้าย jq สำหรับ HTML | ⭐⭐⭐ |
| `hyperfine` | ให้ Claude รันเวลาเองแล้ววิเคราะห์ | benchmark พร้อมสรุปสถิติในตัว ไม่ต้องรันหลายรอบเอง | ⭐⭐ |

## กลุ่ม B — ติดตั้งได้ แต่ประโยชน์หลักเป็นของคน ไม่ใช่ Claude

| Tool | ใช้แทน | หมายเหตุ | Priority |
|---|---|---|---|
| `ripgrep (rg)` | `grep` | Claude Code เรียกผ่าน built-in Grep tool อยู่แล้วโดย harness เอง ติดตั้งไว้เผื่อผู้ใช้เรียกเองในเทอร์มินัล | ⭐⭐⭐ |
| `fd` | `find` | เช่นเดียวกับ `rg` — Claude Code ใช้ built-in Glob tool อยู่แล้ว | ⭐⭐⭐ |
| `bat` | `cat` | มีประโยชน์ก็ต่อเมื่อ**คน**เป็นคนอ่าน (syntax highlight); ถ้า Claude อ่าน output เอง ต้องสั่ง `--plain --color=never` ไม่งั้น ANSI code จะเพิ่ม token แทนที่จะลด | ⭐⭐ |
| `eza` | `ls` | มุมมอง tree สั้นๆ สำหรับคนดูสบายตา ครอบคลุมการทำงานของ `tree` ไปด้วย (ไม่ต้องติดตั้ง `tree` แยก) | ⭐⭐ |

## กลุ่ม C — ห้าม Claude เรียกตรง (interactive / long-running)

| Tool | ใช้แทน | เหตุผลที่ต้องระวัง | Priority |
|---|---|---|---|
| `lazygit` | `git` หลายคำสั่ง | เป็น full-screen TUI รอ keypress — ถ้า Claude สั่งผ่าน Bash จะค้างทันที มีไว้ให้ผู้ใช้เปิดเองในเทอร์มินัลแยกเท่านั้น | ⭐⭐⭐ |
| `fzf` | เลือกไฟล์แบบ manual | เป็น interactive picker รอ input; Claude เรียกได้เฉพาะโหมด non-interactive (`fzf --filter "keyword"`) เท่านั้น ห้ามเรียกแบบเปล่าๆ | ⭐⭐⭐ |
| `watchexec` | เขียน loop script เอง | เป็น long-running process ไม่จบเอง ถ้า Claude รันตรงจะบล็อก session ค้างรอ | ⭐⭐ |

---

**สรุป:** เสนอ checklist ให้ผู้ใช้เลือกจากกลุ่ม A และ B เป็นหลัก (แจ้ง priorityกำกับ) ส่วนกลุ่ม C ให้ถามแยกต่างหากว่าต้องการติดตั้งไว้ใช้เองไหม (ไม่รวมใน guidance ที่บอก Claude ให้เรียกใช้)
