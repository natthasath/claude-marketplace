# Linux Install Commands

ใช้ Bash tool เป็นหลัก ตรวจสอบ distro/package manager ก่อน:

```bash
command -v apt || command -v dnf || command -v pacman
```

**หมายเหตุสำคัญ:** หลาย tool ในลิสต์นี้ไม่มีอยู่ใน apt repo ของ Ubuntu/Debian รุ่นเก่า หรือมีชื่อ binary ต่างจากชื่อ package (เช่น `fd-find` ติดตั้งแล้วได้ binary ชื่อ `fdfind`, `bat` บาง distro ได้ binary ชื่อ `batcat`) — ถ้า apt ไม่มี package ให้ fallback ไปใช้ `cargo install <tool>` (ต้องมี Rust toolchain) หรือ `npm install -g <tool>` ตามแต่ละ tool แนะนำไว้ด้านล่าง

## กลุ่ม A

| Tool | apt (Debian/Ubuntu) | fallback |
|---|---|---|
| `gh` | ต้อง add GitHub CLI apt repo ก่อน (ดู cli.github.com/manual) หรือ `sudo snap install gh` | — |
| `jq` | `sudo apt install jq` | — |
| `ast-grep` | ไม่มีใน apt | `npm install -g @ast-grep/cli` หรือ `cargo install ast-grep --locked` |
| `uv` | ไม่มีใน apt | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| `yq` | ไม่มีใน apt (เวอร์ชันเก่าคนละตัว) | `sudo snap install yq` |
| `git-delta` | ไม่มีใน apt รุ่นเก่า | ดาวน์โหลด `.deb` จาก GitHub release หรือ `cargo install git-delta` |
| `shellcheck` | `sudo apt install shellcheck` | — |
| `just` | มีใน apt รุ่นใหม่ | `cargo install just` |
| `bun` | ไม่มีใน apt | `curl -fsSL https://bun.sh/install \| bash` |
| `tldr` | ไม่มีใน apt | `pip install tldr` หรือ `cargo install tlrc` |
| `duckdb` | ไม่มีใน apt | ดาวน์โหลด binary จาก duckdb.org/install |
| `sd` | ไม่มีใน apt | `cargo install sd` |
| `xh` | ไม่มีใน apt | `cargo install xh` |
| `dust` | ไม่มีใน apt | `cargo install du-dust` |
| `procs` | ไม่มีใน apt | `cargo install procs` |
| `tokei` | มีใน apt รุ่นใหม่ | `cargo install tokei` |
| `difftastic` | ไม่มีใน apt | `cargo install difftastic` |
| `pup` | ไม่มีใน apt | `go install github.com/ericchiang/pup@latest` |
| `hyperfine` | มีใน apt รุ่นใหม่ | `cargo install hyperfine` |

## กลุ่ม B

```bash
sudo apt install ripgrep fd-find bat   # fd-find ให้ binary ชื่อ fdfind, bat ให้ binary ชื่อ batcat บางเวอร์ชัน
cargo install eza   # eza ไม่มีใน apt repo หลัก
```

## กลุ่ม C (ถามแยกก่อนติดตั้ง)

```bash
sudo apt install fzf
cargo install watchexec-cli
# lazygit ไม่มีใน apt — ดาวน์โหลด binary จาก GitHub release ของ jesseduffield/lazygit
```

## Config ที่ต้องเซ็ตเพิ่ม

**`git-delta`** — ต้องตั้งเป็น git pager ถึงจะทำงาน:
```bash
git config --global core.pager delta
git config --global interactive.diffFilter "delta --color-only"
git config --global delta.navigate true
```

**`fzf`** (กลุ่ม C — ติดตั้งไว้ใช้เองในเทอร์มินัล) — apt version มักไม่รวม shell keybinding script ต้อง source เพิ่มใน `.bashrc`/`.zshrc`:
```bash
[ -f /usr/share/doc/fzf/examples/key-bindings.bash ] && source /usr/share/doc/fzf/examples/key-bindings.bash
```
ถามผู้ใช้ก่อนแก้ shell rc file เสมอ เพราะเป็นการแก้ startup script ของผู้ใช้

**ชื่อ binary ต่าง distro** — ถ้า `fd`/`bat` เรียกไม่เจอหลังติดตั้งบน Debian/Ubuntu ให้ลอง `fdfind`/`batcat` แทน หรือสร้าง symlink ให้ผู้ใช้ยืนยันก่อน
