# MEMORY.md - Long-Term Memory

## Projects

### FrePPLe
- **路径:** `/Users/yimozhang/Desktop/trae_projects/frepple`
- **语言:** Python
- **类型:** 供应链/生产计划优化工具
- **插件:** excel, csv, json, xml, html, odflog, xsdgraph, epsogis, doorld 等
- **构成:** 主应用(frepple/) + 架构(arch/) + 工具(utils/) + 贡献代码(contrib/) + 文档(docs/) + 测试(tests/)
- **版本控制:** Git

### 上饶光学（拍频 + 鑫望）
- **位置:** 上饶
- **车间:** 拍频（主，目前资料以这家为主）、鑫望
- **资料路径:** `/Users/yimozhang/Desktop/金乌牧云/上饶光学/`
- **业务:** 光学冷加工（精密光学元件切割、抛光、镀膜等）
- **设备:** 粗抛机9台、精抛机6台、切割机2台、铣磨机1台（瓶颈）、单轴机2台
- **核心人员:** 余德付、平浩东、王佳俊、郭晓阳、郭永建、黄子明、吴正涛等
- **AI排产系统:** 有规划文档（`上饶拍频工厂：AI排产管理系统.docx`），目标是解决多订单并行排程、人员设备调度问题

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

### 邮件
- **发送/读取邮箱:** 804314819@qq.com
- **授权码:** ibxdfrsmjhzybgac
- **SMTP/IMAP:** smtp.qq.com:465 / imap.qq.com:993

---

_最后更新: 2026-04-01 20:05_
