# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## 邮件

- **当前使用:** QQ邮箱 804314819@qq.com
- **SMTP:** smtp.qq.com:465
- **IMAP:** imap.qq.com:993
- **授权码:** ibxdfrsmjhzybgac
- **macOS发邮件:** 需加 `SSL_CERT_FILE=/Users/yimozhang/Library/Python/3.13/lib/python/site-packages/certifi/cacert.pem`

### 你的邮箱（发件人/收件人）
- **QQ:** 804314819@qq.com
- **Gmail:** yimocool@gmail.com
- **默认规则:** 说"给我发邮件"时，同时发送到这两个邮箱

## SSH

### 成都阿里云服务器
- **地址:** `ssh root@47.108.50.206`
- **私钥:** 本机 SSH 私钥（`~/.ssh/id_rsa` 或对应私钥）

### FrePPLe
- **地址:** http://47.108.50.206:8000/data/
- **账号密码:**
  | 用户名 | 密码 |
  |--------|------|
  | admin | `admin123` |
  | test2 | `test2123` |
  | frepple01~05 | `frepple123` |

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
