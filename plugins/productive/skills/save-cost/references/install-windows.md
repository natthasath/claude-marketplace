# Windows Install Commands

ใช้ PowerShell tool เป็นหลัก ตรวจสอบ package manager ที่มีก่อนเสมอ:

```powershell
Get-Command winget -ErrorAction SilentlyContinue
Get-Command scoop -ErrorAction SilentlyContinue
```

**winget มากับ Windows 10/11 อยู่แล้ว** ใช้เป็นตัวเลือกแรก ถ้า package ใดไม่มีใน winget หรือ command ล้มเหลว ให้ลอง scoop เป็นตัวสำรอง (ถ้ายังไม่มี scoop และผู้ใช้ต้องการ ติดตั้งด้วย `irm get.scoop.sh | iex`)

**หมายเหตุสำคัญ:** package ID ของ winget อาจเปลี่ยนหรือคลาดเคลื่อนได้ตามเวลา — ถ้ารันคำสั่งด้านล่างแล้ว error ว่าไม่พบ package ให้ลอง `winget search <ชื่อ tool>` เพื่อหา ID ที่ถูกต้องก่อนแจ้งผู้ใช้ว่าติดตั้งไม่สำเร็จ

## กลุ่ม A

| Tool | winget | scoop (สำรอง) |
|---|---|---|
| `gh` | `winget install GitHub.cli` | `scoop install gh` |
| `jq` | `winget install jqlang.jq` | `scoop install jq` |
| `ast-grep` | `winget install ast-grep.ast-grep` | `scoop install ast-grep` หรือ `npm install -g @ast-grep/cli` |
| `uv` | `winget install astral-sh.uv` | `powershell -c "irm https://astral.sh/uv/install.ps1 \| iex"` |
| `yq` | `winget install MikeFarah.yq` | `scoop install yq` |
| `git-delta` | `winget install dandavison.delta` | `scoop install delta` |
| `shellcheck` | `winget install koalaman.shellcheck` | `scoop install shellcheck` |
| `just` | `winget install casey.just` | `scoop install just` |
| `bun` | `winget install Oven-sh.Bun` | `powershell -c "irm bun.sh/install.ps1 \| iex"` |
| `tldr` | `winget install tldr-pages.tlrc` | `npm install -g tldr` |
| `duckdb` | `winget install DuckDB.cli` | `scoop install duckdb` |
| `sd` | `winget install chmln.sd` | `scoop install sd` |
| `xh` | `winget install ducaale.xh` | `scoop install xh` |
| `dust` | `winget install bootandy.dust` | `scoop install dust` |
| `procs` | `winget install dalance.procs` | `scoop install procs` |
| `tokei` | `winget install XAMPPRocky.tokei` | `scoop install tokei` |
| `difftastic` | `winget install Wilfred.difftastic` | `scoop install difftastic` |
| `pup` | — | `scoop install pup` |
| `hyperfine` | `winget install sharkdp.hyperfine` | `scoop install hyperfine` |

## กลุ่ม B

| Tool | winget | scoop (สำรอง) |
|---|---|---|
| `ripgrep` | `winget install BurntSushi.ripgrep.MSVC` | `scoop install ripgrep` |
| `fd` | `winget install sharkdp.fd` | `scoop install fd` |
| `bat` | `winget install sharkdp.bat` | `scoop install bat` |
| `eza` | `winget install eza-community.eza` | `scoop install eza` |

## กลุ่ม C (ถามแยกก่อนติดตั้ง)

| Tool | winget | scoop (สำรอง) |
|---|---|---|
| `lazygit` | `winget install JesseDuffield.lazygit` | `scoop install lazygit` |
| `fzf` | `winget install junegunn.fzf` | `scoop install fzf` |
| `watchexec` | `winget install watchexec.watchexec` | `scoop install watchexec` |

## Config ที่ต้องเซ็ตเพิ่ม

**`git-delta`** — ต้องตั้งเป็น git pager ถึงจะทำงาน:
```powershell
git config --global core.pager delta
git config --global interactive.diffFilter "delta --color-only"
git config --global delta.navigate true
```

**`fzf`** (กลุ่ม C — ติดตั้งไว้ใช้เองในเทอร์มินัล) — ต้อง init ใน PowerShell profile ถ้าต้องการ keybinding (Ctrl+R ค้นหา history):
```powershell
# เพิ่มใน $PROFILE
Import-Module PSFzf
```
ต้องติดตั้ง `PSFzf` module เพิ่มด้วย `Install-Module PSFzf -Scope CurrentUser` — ถามผู้ใช้ก่อนแก้ `$PROFILE` เสมอ เพราะเป็นการแก้ shell startup script ของผู้ใช้
