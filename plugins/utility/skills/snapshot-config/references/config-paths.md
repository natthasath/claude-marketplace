# Config Paths Reference

Config file locations สำหรับโปรแกรมยอดนิยมแต่ละ OS
ใช้เป็น lookup table เมื่อต้องการ export หรือ snapshot config

---

## Editor & IDE

### Visual Studio Code
| OS | Config Path |
|----|------------|
| Windows | `%APPDATA%\Code\User\settings.json` |
| Windows | `%APPDATA%\Code\User\keybindings.json` |
| Windows | `%APPDATA%\Code\User\snippets\` |
| macOS | `~/Library/Application Support/Code/User/settings.json` |
| macOS | `~/Library/Application Support/Code/User/keybindings.json` |
| Linux | `~/.config/Code/User/settings.json` |
| Linux | `~/.config/Code/User/keybindings.json` |

**Export extensions:**
```bash
# Export
code --list-extensions > extensions.txt
# Restore
cat extensions.txt | xargs -L 1 code --install-extension
```

### Cursor
| OS | Config Path |
|----|------------|
| Windows | `%APPDATA%\Cursor\User\settings.json` |
| macOS | `~/Library/Application Support/Cursor/User/settings.json` |
| Linux | `~/.config/Cursor/User/settings.json` |

### Neovim
| OS | Config Path |
|----|------------|
| Windows | `%LOCALAPPDATA%\nvim\` |
| macOS/Linux | `~/.config/nvim/` |

---

## Terminal & Shell

### Windows Terminal
| OS | Config Path |
|----|------------|
| Windows | `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json` |
| Windows (preview) | `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe\LocalState\settings.json` |

### iTerm2 (macOS)
| OS | Config Path |
|----|------------|
| macOS | `~/Library/Preferences/com.googlecode.iterm2.plist` |

**Export:** iTerm2 → Preferences → General → Preferences → Save to folder

### Warp
| OS | Config Path |
|----|------------|
| macOS | `~/.warp/` |
| Linux | `~/.warp/` |

### Zsh
| OS | Config Path |
|----|------------|
| macOS/Linux | `~/.zshrc` |
| macOS/Linux | `~/.zprofile` |
| macOS/Linux | `~/.zshenv` |

### Bash
| OS | Config Path |
|----|------------|
| Linux | `~/.bashrc` |
| macOS/Linux | `~/.bash_profile` |
| Windows (Git Bash) | `~/.bashrc` |

### Fish
| OS | Config Path |
|----|------------|
| macOS/Linux | `~/.config/fish/config.fish` |
| macOS/Linux | `~/.config/fish/functions/` |

### Oh My Zsh
| OS | Config Path |
|----|------------|
| macOS/Linux | `~/.zshrc` (theme + plugins section) |
| macOS/Linux | `~/.oh-my-zsh/custom/` |

### PowerShell
| OS | Config Path |
|----|------------|
| Windows | `$PROFILE` → `Documents\PowerShell\Microsoft.PowerShell_profile.ps1` |
| macOS/Linux | `~/.config/powershell/Microsoft.PowerShell_profile.ps1` |

---

## Version Control

### Git
| Config | Path |
|--------|------|
| Global config | `~/.gitconfig` |
| Global gitignore | `~/.gitignore_global` |
| SSH keys | `~/.ssh/` |

**Export:**
```bash
git config --global --list
```

---

## Package Managers

### npm / Node.js
| Config | Path |
|--------|------|
| npmrc | `~/.npmrc` |
| nvmrc (default version) | `~/.nvmrc` |
| nvm config | `~/.nvm/` |

**Export installed global packages:**
```bash
npm list -g --depth=0
```

### pip / Python
| OS | Config Path |
|----|------------|
| Windows | `%APPDATA%\pip\pip.ini` |
| macOS/Linux | `~/.pip/pip.conf` |
| macOS/Linux | `~/.config/pip/pip.conf` |

**Export packages:**
```bash
pip freeze > requirements.txt
```

### Homebrew (macOS/Linux)
**Export:**
```bash
brew bundle dump --file=Brewfile
# Restore
brew bundle install --file=Brewfile
```

### Winget (Windows)
**Export:**
```bash
winget export -o winget-packages.json
# Restore
winget import -i winget-packages.json
```

### Chocolatey (Windows)
**Export:**
```bash
choco export packages.config
# Restore
choco install packages.config
```

---

## Container & Virtualization

### Docker
| OS | Config Path |
|----|------------|
| Windows | `%APPDATA%\Docker\settings.json` |
| macOS | `~/Library/Group Containers/group.com.docker/settings.json` |
| Linux | `~/.docker/config.json` |
| Linux (daemon) | `/etc/docker/daemon.json` |

---

## Database Tools

### DBeaver
| OS | Config Path |
|----|------------|
| Windows | `%APPDATA%\DBeaverData\workspace6\` |
| macOS | `~/Library/DBeaverData/workspace6/` |
| Linux | `~/.local/share/DBeaverData/workspace6/` |

### TablePlus
| OS | Config Path |
|----|------------|
| macOS | `~/Library/Application Support/com.tinyapp.TablePlus/` |
| Windows | `%APPDATA%\TablePlus\` |

---

## Communication & Productivity

### Obsidian
| Config | Path |
|--------|------|
| Vault config | `<vault>/.obsidian/` |
| App config | `<vault>/.obsidian/app.json` |
| Plugins | `<vault>/.obsidian/plugins/` |
| Themes | `<vault>/.obsidian/themes/` |

### Slack
| OS | Config Path |
|----|------------|
| Windows | `%APPDATA%\Slack\storage\` |
| macOS | `~/Library/Application Support/Slack/` |

---

## System & Security

### SSH
| Config | Path |
|--------|------|
| Config file | `~/.ssh/config` |
| Known hosts | `~/.ssh/known_hosts` |

### 1Password / Bitwarden
ไม่ควร export โดยตรง — ใช้ built-in export feature ของ app เท่านั้น

---

## Quick Command Summary

```bash
# VSCode extensions list
code --list-extensions

# Git global config
git config --global --list

# npm global packages
npm list -g --depth=0

# pip packages
pip freeze

# Homebrew bundle (macOS)
brew bundle dump

# Winget export (Windows)
winget export -o packages.json

# Installed apt packages (Ubuntu)
dpkg --get-selections > packages.txt
```
