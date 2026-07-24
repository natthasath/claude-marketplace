# 🎉 generator

Plugin for **generating ASCII art** — text banners, image-to-ASCII conversion, cowsay speech bubbles, and rainbow coloring, all self-contained with no external CLI tools to install.

### ⭐ Skills

| Skill | วัตถุประสงค์ |
|---|---|
| `generator-ascii` | แปลงข้อความหรือรูปภาพเป็น ASCII art — Text Banner (สไตล์ figlet/toilet), Image to ASCII (สไตล์ jp2a/chafa/img2txt), Cowsay และ Rainbow Coloring (สไตล์ lolcat) ทำงานผ่าน script ที่ bundle มากับ skill เอง ไม่ต้องติดตั้ง CLI tool ภายนอกเลย |

### 🚀 Usage

```
/generator-ascii <ข้อความ หรือ path ของไฟล์รูปภาพ>
```

### 🛠️ โหมดที่รองรับ

| โหมด | สไตล์ต้นแบบ | Input |
|---|---|---|
| Text Banner | figlet / toilet | ข้อความ (A-Z, 0-9, เครื่องหมายพื้นฐาน) |
| Image to ASCII | jp2a / chafa / img2txt | ไฟล์รูปภาพ (JPG, PNG, GIF, BMP, WebP ฯลฯ) |
| Cowsay | cowsay | ข้อความให้ตัวการ์ตูนพูด |
| Rainbow | lolcat | ต่อ pipe จากโหมดอื่นเพื่อเติมสีรุ้งไล่เฉด |

ทุกโหมดรันผ่าน `uv run` (แนะนำ) หรือ `python3`/`python`/`py -3` ตรงๆ — โหมด Image to
ASCII เท่านั้นที่ต้องใช้ Pillow ซึ่ง `uv run` จะติดตั้งให้อัตโนมัติผ่าน inline script
metadata โดยไม่ต้อง `pip install` เอง
