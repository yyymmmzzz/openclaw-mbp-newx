# MEMORY.md - Long-Term Memory

## Projects

### FrePPLe
- **路径:** `/Users/yimozhang/Desktop/trae_projects/frepple`
- **语言:** Python
- **类型:** 供应链/生产计划优化工具
- **插件:** excel, csv, json, xml, html, odflog, xsdgraph, epsogis, doorld 等
- **构成:** 主应用(frepple/) + 架构(arch/) + 工具(utils/) + 贡献代码(contrib/) + 文档(docs/) + 测试(tests/)
- **版本控制:** Git

## Infrastructure

### 成都阿里云服务器 (47.108.50.206)
- **地址:** `ssh root@47.108.50.206`
- **私钥:** 本机 SSH 私钥（`~/.ssh/id_rsa`）
- **位置:** 成都
- **用途:** FrePPLe 测试/部署服务器

#### FrePPLe 部署进度（截至 2026-04-01 20:05）
- ✅ 源码同步到 `/opt/frepple/`
- ✅ Docker 镜像 `frepple:dev` (1.87GB) build 完成
- ✅ PostgreSQL 配置好（31个数据库 frepple0~30）
- ✅ Django 数据库迁移完成
- ✅ FrePPLe 容器运行中（端口 8000）
- ✅ HTTP 访问正常（302 重定向到登录页）
- ❌ systemd 开机自启服务未创建
- ❌ Nginx 反向代理未配置
- ❌ 系统 Python 仍是 3.8，容器内是 3.12

#### 服务器磁盘状态
- 总计: 20GB，已用 15GB，可用 4.4GB (77%)
- 已清理: WordPress、crush-ai 网站、Docker 孤立卷、journal 日志、旧内核

### 博望AIGC平台 MixVideo
- **连接:** mixvideo.bowong.cc
- **账号:** momoking
- **密码:** Pp123456
- **邮箱:** 315098779@qq.com

---

_最后更新: 2026-04-01 20:05_
