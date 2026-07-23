# macOS Install Commands

ใช้ Bash tool เป็นหลัก ตรวจสอบว่ามี Homebrew ก่อน:

```bash
command -v brew
```

ถ้ายังไม่มี brew และผู้ใช้ต้องการ ติดตั้งด้วย `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` — เกือบทุก tool ในลิสต์นี้มีอยู่ใน Homebrew โดยตรง

## กลุ่ม A

```bash
brew install gh jq ast-grep uv yq git-delta shellcheck just bun duckdb sd xh dust procs tokei difftastic pup hyperfine
brew install tlrc   # tldr client
```

## กลุ่ม B

```bash
brew install ripgrep fd bat eza
```

## กลุ่ม C (ถามแยกก่อนติดตั้ง)

```bash
brew install lazygit fzf watchexec
```

## Config ที่ต้องเซ็ตเพิ่ม

**`git-delta`** — ต้องตั้งเป็น git pager ถึงจะทำงาน:
```bash
git config --global core.pager delta
git config --global interactive.diffFilter "delta --color-only"
git config --global delta.navigate true
```

**`fzf`** (กลุ่ม C — ติดตั้งไว้ใช้เองในเทอร์มินัล) — ต้อง run install script เพื่อเซ็ต shell keybinding:
```bash
$(brew --prefix)/opt/fzf/install
```
ถามผู้ใช้ก่อนแก้ shell rc file (`.zshrc`/`.bashrc`) เสมอ เพราะเป็นการแก้ startup script ของผู้ใช้
