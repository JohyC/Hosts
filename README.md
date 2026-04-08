# 🌐 Hosts

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub Repo stars](https://img.shields.io/github/stars/JohyC/Hosts?style=flat)
![GitHub last commit](https://img.shields.io/github/last-commit/JohyC/Hosts)
![Auto Update](https://img.shields.io/badge/Auto_Update-GitHub%20Actions-brightgreen)

> Keep your `hosts` file updated automatically — for GitHub, Epic Games, Steam, and Microsoft.

## 📋 Table of Contents

- [What This Does](#what-this-does)
- [Features](#features)
- [Quick Start](#quick-start)
- [Auto-Update with SwitchHosts](#auto-update-with-switchhosts)
- [Manual Setup](#manual-setup)
- [Hosts Sources](#hosts-sources)
- [Script Usage](#script-usage)
- [Contributing](#contributing)

---

## What This Does

This repository maintains **up-to-date hosts file entries** for services that may be slow or inaccessible in certain regions — primarily GitHub, Epic Games, Steam, and Microsoft. A **GitHub Actions workflow** automatically syncs changes daily.

---

## Features

| Feature | Description |
|---------|-------------|
| 🔄 **Auto-Sync** | GitHub Actions updates hosts daily |
| 📦 **Multi-Service** | Covers GitHub, Epic, Steam, and Microsoft |
| 🤖 **GitOps** | Syncs to Gitee and custom Gitea servers |
| 🖥️ **Cross-Platform** | Works on macOS, Linux, and Windows |
| ⚡ **SwitchHosts!** | Native app integration for automatic updates |

---

## Quick Start

### 1. Get the Latest Hosts

Download `hosts.txt` directly:

```bash
# GitHub hosts
https://raw.githubusercontent.com/JohyC/Hosts/main/hosts.txt

# Gitee mirror (faster in China)
https://gitee.com/yuchi-shentang/GithubHosts/raw/branch/main/hosts.txt
```

### 2. Apply to Your System

**macOS / Linux:**

```bash
# Append hosts to system file
cat hosts.txt | sudo tee -a /etc/hosts

# Flush DNS cache
sudo killall -HUP mDNSResponder   # macOS
sudo systemctl restart systemd-resolved  # Linux
```

**Windows:**

```powershell
# Append to hosts file
type hosts.txt >> C:\Windows\System32\drivers\etc\hosts

# Flush DNS
ipconfig /flushdns
```

---

## Auto-Update with SwitchHosts

The easiest way — **automatic daily updates**:

### Setup SwitchHosts

1. Download [SwitchHosts](https://swh.app/zh/)
2. Click the **+** button to add a new rule
3. Configure:

| Field | Value |
|-------|-------|
| **Title** | `Johy/Hosts` (or any name) |
| **Type** | `Remote` |
| **URL** | `https://www.foul.trade:3000/Johy/Hosts/raw/branch/main/hosts.txt` |
| **Auto-Refresh** | `24 hours` |

> 💡 The Gitea mirror (`foul.trade:3000`) is recommended — more stable than the raw GitHub URL.

---

## Manual Setup

### macOS

1. Open **Finder**
2. Press `Shift + Cmd + G` → type `/etc/hosts` → press Enter
3. Copy `hosts.txt` content to the clipboard
4. Paste at the end of the system hosts file
5. Run: `sudo killall -HUP mDNSResponder`

### Windows

1. Open Notepad as **Administrator**
2. Open `C:\Windows\System32\drivers\etc\hosts`
3. Paste the contents of `hosts.txt` at the end
4. Save and run: `ipconfig /flushdns`

---

## Hosts Sources

| Service | Source URL |
|---------|------------|
| **GitHub** | `GithubHosts.txt` |
| **Epic Games** | `EpicHosts.txt` |
| **Steam** | `SteamDomains.txt` |
| **Microsoft** | `MicrosoftHosts.txt` |
| **Combined** | `hosts.txt` |

### Mirrors

| Mirror | URL |
|--------|-----|
| GitHub (raw) | `https://github.com/JohyC/Hosts/blob/main/hosts.txt` |
| Gitee | `https://gitee.com/yuchi-shentang/GithubHosts/blob/main/hosts.txt` |
| Gitea | `https://www.foul.trade:3000/Johy/Hosts/raw/branch/main/hosts.txt` |

---

## Script Usage

The `workingDir/ph.py` script lets you **manage hosts dynamically**:

```bash
cd workingDir
pip install -r requirements  # requires: rich

# Append domains to default list
python ph.py -a example.com another.com

# Use completely custom domain list
python ph.py -d example.com newdomain.com

# Read domains from a file
python ph.py -f my_domains.txt

# Custom output filename
python ph.py -a example.com -o my_hosts.txt
```

All commands generate `hosts.txt` in the current directory.

---

## Contributing

- ✅ Issues and PRs welcome
- ✅ GitHub Actions auto-syncs contributions
- ✅ Submit domains to block or unblock via Issues

---

*README optimized with [Gingiris README Generator](https://gingiris.github.io/github-readme-generator/)*
