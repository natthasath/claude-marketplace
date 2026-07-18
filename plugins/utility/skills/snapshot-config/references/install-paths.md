# Install Paths Reference

Best-practice installation paths สำหรับโปรแกรมยอดนิยมแต่ละ OS
ใช้เป็น reference เมื่อวิเคราะห์ "แนะนำ Installation Path" ใน Step 6

## หลักการตรวจสอบ

| สัญญาณอันตราย | ทำไม |
|--------------|------|
| อยู่ที่ root drive (`C:\flutter`, `C:\go`) | ต้องการ admin ในการ update, ระเกะระกะ |
| Path มีช่องว่าง (`C:\Program Files\flutter`) | Flutter, Go, Rust build อาจพัง |
| อยู่ใน `C:\Program Files` หรือ `C:\Windows` | ต้องการ admin ทุกครั้ง |
| `/usr/local/bin` บน Linux (user install) | ควรใช้ `~/.local/bin` หรือ package manager แทน |

---

## Dev SDK & Runtimes

### Flutter
| OS | แนะนำ | หลีกเลี่ยง | เหตุผล |
|----|-------|-----------|--------|
| Windows | `C:\dev\flutter` หรือ `D:\dev\flutter` | `C:\flutter`, `C:\Program Files\flutter` | ไม่ต้องการ admin, ไม่มีช่องว่างใน path |
| macOS | `~/development/flutter` หรือ `/opt/flutter` | `/usr/local/flutter` | user-owned, ไม่ต้อง sudo |
| Ubuntu | `~/development/flutter` หรือ `/opt/flutter` | `/usr/flutter`, `/usr/local/flutter` | user-owned, snap/apt ไม่รองรับ stable channel |

### Node.js / nvm
| OS | แนะนำ | หลีกเลี่ยง | เหตุผล |
|----|-------|-----------|--------|
| Windows | ติดตั้งผ่าน [nvm-windows](https://github.com/coreybutler/nvm-windows): `C:\Users\<user>\AppData\Roaming\nvm` | ติดตั้ง Node.js ตรงๆ ไว้ที่ `C:\Program Files\nodejs` | nvm จัดการหลาย version ได้, ไม่ต้อง admin |
| macOS | ติดตั้งผ่าน `nvm` หรือ `mise`: `~/.nvm` / `~/.local/share/mise` | `/usr/local/bin/node` (Homebrew แนะนำได้) | สลับ version ได้ง่าย |
| Ubuntu | ติดตั้งผ่าน `nvm`: `~/.nvm` | `apt install nodejs` (version เก่ามาก) | nvm ได้ version ล่าสุด |

### Python / pyenv
| OS | แนะนำ | หลีกเลี่ยง | เหตุผล |
|----|-------|-----------|--------|
| Windows | ติดตั้งผ่าน [pyenv-win](https://github.com/pyenv-win/pyenv-win): `%USERPROFILE%\.pyenv` | `C:\Python312\`, `C:\Program Files\Python` | สลับ version ได้, ไม่ต้อง admin |
| macOS | `pyenv`: `~/.pyenv` | system Python (`/usr/bin/python3`) | ไม่รบกวน system Python |
| Ubuntu | `pyenv`: `~/.pyenv` หรือ `deadsnakes` PPA | `python3` จาก apt สำหรับ dev | แยก system กับ dev environment |

### Go
| OS | แนะนำ | หลีกเลี่ยง | เหตุผล |
|----|-------|-----------|--------|
| Windows | `C:\go` หรือ `C:\dev\go` | `C:\Program Files\Go` | Go tools ทำงานได้ดีกับ path สั้นๆ ไม่มีช่องว่าง |
| macOS | `/usr/local/go` (official installer) หรือ `brew install go` | — | official installer default |
| Ubuntu | `/usr/local/go` (official tarball) | `apt install golang` (version เก่า) | official เป็น version ล่าสุด |

### Rust
| OS | แนะนำ | หลีกเลี่ยง | เหตุผล |
|----|-------|-----------|--------|
| Windows | ติดตั้งผ่าน `rustup`: `%USERPROFILE%\.cargo` | — | rustup เป็น official way |
| macOS/Ubuntu | `rustup`: `~/.cargo` | apt/brew (version เก่า) | rustup เป็น official way |

### Java / JDK
| OS | แนะนำ | หลีกเลี่ยง | เหตุผล |
|----|-------|-----------|--------|
| Windows | ติดตั้งผ่าน `winget` หรือ SDKMAN!: `C:\Program Files\Eclipse Adoptium\` หรือ Android Studio bundled JDK | Oracle JDK บน `C:\java` | Microsoft/Eclipse build ฟรี, ไม่มี license issue |
| macOS | `brew install openjdk` → `/opt/homebrew/opt/openjdk` | Oracle JDK | SDKMAN! ถ้าต้องการหลาย version |
| Ubuntu | `apt install openjdk-21-jdk` → `/usr/lib/jvm/java-21-openjdk-amd64` | Oracle JDK | apt managed, auto update |

### Android SDK
| OS | แนะนำ | หลีกเลี่ยง | เหตุผล |
|----|-------|-----------|--------|
| Windows | `%LOCALAPPDATA%\Android\sdk` (Android Studio default) | `C:\android-sdk` | Android Studio จัดการให้อัตโนมัติ |
| macOS | `~/Library/Android/sdk` (Android Studio default) | `/usr/local/android-sdk` | user-owned |
| Ubuntu | `~/Android/Sdk` (Android Studio default) | `/opt/android-sdk` | user-owned |

### .NET SDK
| OS | แนะนำ | หลีกเลี่ยง | เหตุผล |
|----|-------|-----------|--------|
| Windows | ติดตั้งผ่าน `winget install Microsoft.DotNet.SDK.8`: `C:\Program Files\dotnet` | — | official installer จัดการ PATH ให้ |
| macOS | `brew install dotnet` | — | Homebrew จัดการ update |
| Ubuntu | Microsoft apt repo → `/usr/share/dotnet` | snap (มี limitation) | official repo |

### Ruby / rbenv
| OS | แนะนำ | หลีกเลี่ยง | เหตุผล |
|----|-------|-----------|--------|
| Windows | [RubyInstaller](https://rubyinstaller.org): `C:\Ruby33-x64` | — | official Windows installer |
| macOS | `rbenv`: `~/.rbenv` | system Ruby (`/usr/bin/ruby`) | ไม่รบกวน system |
| Ubuntu | `rbenv` หรือ `rvm`: `~/.rbenv` | `apt install ruby` (version เก่า) | version manager |

---

## Editor & IDE

### VS Code
| OS | แนะนำ | หลีกเลี่ยง | เหตุผล |
|----|-------|-----------|--------|
| Windows | `%LOCALAPPDATA%\Programs\Microsoft VS Code` (user install) | System install ใน `C:\Program Files` | User install ไม่ต้อง admin ในการ update |
| macOS | `/Applications/Visual Studio Code.app` | — | standard macOS app location |
| Ubuntu | `snap install code` หรือ `.deb` package: `/usr/share/code` | manual extraction | auto update |

### JetBrains IDEs
| OS | แนะนำ | หลีกเลี่ยง | เหตุผล |
|----|-------|-----------|--------|
| Windows | JetBrains Toolbox: `%LOCALAPPDATA%\JetBrains\Toolbox\apps\` | manual install ใน `C:\Program Files` | Toolbox จัดการ update ทุก IDE ให้ |
| macOS | JetBrains Toolbox: `~/Applications/` | `/Applications/` (system) | User-owned, Toolbox update |
| Ubuntu | JetBrains Toolbox: `~/.local/share/JetBrains/Toolbox/apps/` | snap (มี limitation กับ filesystem) | Toolbox |

---

## Terminal & Prompt

### Oh My Posh
| OS | แนะนำ | หลีกเลี่ยง | เหตุผล |
|----|-------|-----------|--------|
| Windows | ติดตั้งผ่าน `winget install JanDeDobbeleer.OhMyPosh`: `%LOCALAPPDATA%\Programs\oh-my-posh\` | manual copy ไว้ที่ `C:\tools\` | winget จัดการ update อัตโนมัติ |
| macOS | `brew install jandedobbeleer/oh-my-posh/oh-my-posh` | manual | Homebrew update |
| Ubuntu | `curl ... | bash` → `/usr/local/bin/oh-my-posh` | snap | official installer |

**Theme files:** เก็บ custom theme ที่ `~/.config/oh-my-posh/` เสมอ — ไม่ใช้ built-in themes folder เพราะอาจถูก overwrite ตอน upgrade

### Starship
| OS | แนะนำ | แนะนำ config | เหตุผล |
|----|-------|------------|--------|
| Windows | `winget install Starship.Starship` | `~/.config/starship.toml` | — |
| macOS | `brew install starship` | `~/.config/starship.toml` | — |
| Ubuntu | official install script → `/usr/local/bin/starship` | `~/.config/starship.toml` | — |

---

## Package Manager (ตัว manager เอง)

### Homebrew (macOS/Linux)
| OS | Path |
|----|------|
| macOS (Apple Silicon) | `/opt/homebrew/` |
| macOS (Intel) | `/usr/local/` |
| Linux | `/home/linuxbrew/.linuxbrew/` |

### Scoop (Windows)
| Location | Path |
|----------|------|
| Scoop itself | `%USERPROFILE%\scoop\` |
| Apps | `%USERPROFILE%\scoop\apps\` |
| Global apps | `C:\ProgramData\scoop\` |

**Scoop ดีกว่า Chocolatey สำหรับ dev tools** — ติดตั้ง user-level ไม่ต้อง admin

### Chocolatey (Windows)
| Location | Path |
|----------|------|
| Chocolatey itself | `C:\ProgramData\chocolatey\` |
| Tools | `C:\tools\` |

---

## Design & Media Tools

### CapCut
| OS | Default Install | แนะนำ Config/Project |
|----|----------------|---------------------|
| Windows | `%LOCALAPPDATA%\CapCut\` | Drafts/Materials บน D: หรือ E: แยกจาก C: |
| macOS | `/Applications/CapCut.app` | — |

**Config:** `%LOCALAPPDATA%\CapCut\User Data\Config\` — ไม่ควรย้าย install location

### Figma
| OS | Path |
|----|------|
| Windows | `%LOCALAPPDATA%\Figma\` (auto-updated) |
| macOS | `/Applications/Figma.app` |

---

## Container & Cloud

### Docker Desktop
| OS | แนะนำ | หมายเหตุ |
|----|-------|---------|
| Windows | `C:\Program Files\Docker\Docker` (default) | WSL2 backend data อยู่ที่ `%LOCALAPPDATA%\Docker\wsl\` |
| macOS | `/Applications/Docker.app` | — |
| Ubuntu | Docker Engine (ไม่ใช่ Desktop): `/usr/bin/docker` ผ่าน apt repo | Desktop บน Linux มี limitation |

---

## Quick Reference: Windows Path Tiers

```
C:\dev\<tool>          ← แนะนำสำหรับ SDK ที่ต้องการ fast path (Flutter, Go)
C:\tools\<tool>        ← สำหรับ standalone tools ที่ไม่มี installer
%LOCALAPPDATA%\<tool>  ← สำหรับ GUI apps และ tools ที่มี installer (user-level)
%USERPROFILE%\.<tool>  ← สำหรับ tools ที่ใช้ dotfile convention (rust, nvm)
C:\Program Files\      ← สำหรับ system-wide tools เท่านั้น (admin required)
```

## Quick Reference: macOS Path Tiers

```
/opt/homebrew/         ← Homebrew (Apple Silicon)
/usr/local/            ← Homebrew (Intel) หรือ manual installs
~/Applications/        ← User-level GUI apps (JetBrains Toolbox)
/Applications/         ← System GUI apps (VS Code, Docker)
~/.local/bin/          ← User-level CLI tools
~/.<tool>/             ← Version managers (nvm, pyenv, rbenv)
```

## Quick Reference: Ubuntu Path Tiers

```
/usr/bin/              ← apt-managed system packages
/usr/local/bin/        ← manual installs system-wide (ต้องการ sudo)
~/.local/bin/          ← user-level CLI tools (แนะนำ)
~/.<tool>/             ← Version managers (nvm, pyenv, rbenv)
/opt/<tool>/           ← large SDKs ที่ติดตั้ง system-wide (Flutter, Android Studio)
~/development/         ← user-owned SDKs (Flutter, Go)
```
