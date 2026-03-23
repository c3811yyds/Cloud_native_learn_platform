云原生学习平台

一个用于学习和演练前后端分离、MySQL/Redis、Docker Compose 与基础工程化实践的项目。

## 项目简介

- 后端：Flask + SQLAlchemy + JWT
- 前端：Vue 3 + Vite
- 数据库：MySQL 8.0
- 缓存/限流：Redis
- 部署：Docker Compose + Nginx + Gunicorn

当前项目包含 3 类角色：

- 学生：选课、学习、留言、记笔记、查看进度
- 教师：建课、上传课件、查看学生进度、回复评价
- 管理员：账号管理、邀请码管理、全站概览

## 核心功能

- 用户注册、登录、JWT 鉴权
- 邮箱验证码注册 / 找回密码 / 已登录改密
- 课程列表、课程详情、选课与退课
- 视频 / 音频 / 图片 / PDF 预览与文件下载
- 学习进度记录与统计
- 留言、评价、点赞、教师回复
- 全局侧边栏笔记
- AI 助教对话
- 管理员后台与教师邀请码
- Redis 缓存、限流与验证码冷却

## 目录结构

```text
e:\all_
├─ backend/               Flask 后端
├─ frontend/              Vue 前端
├─ db-backups/            数据库初始化与快照
├─ third_party/           第三方词库等项目内依赖
├─ docker-compose.yml     Docker 编排
├─ DEPLOY_DOCKER.md       Docker 部署说明
├─ CONTRIBUTING.md        提交规范与分支说明
└─ VERSION                当前项目版本号
```

## 本地开发

### 1. 准备数据库

先在本机 MySQL 中创建数据库：

```sql
CREATE DATABASE cloud_native_learning_platform
DEFAULT CHARACTER SET utf8mb4;
```

然后导入初始化数据：

```sql
USE cloud_native_learning_platform;
SOURCE /你的路径/db-backups/database_seed.sql;
```

### 2. 启动 Redis

本项目当前默认使用独立的 Docker Redis 容器，宿主机端口映射为 `6380`：

```powershell
cd E:\all_
docker compose up -d redis
```

### 3. 启动后端

```powershell
cd E:\all_\backend
copy env.example .env
E:\all_\.venv\Scripts\python.exe app.py
```

最少需要确认这些配置：

- `SECRET_KEY`
- `JWT_SECRET_KEY`
- `DATABASE_URL=mysql+pymysql://root:mysql@127.0.0.1:3306/cloud_native_learning_platform?charset=utf8mb4`
- `REDIS_URL=redis://127.0.0.1:6380/0`
- `SILICON_API_KEY`
- `MAIL_SERVER / MAIL_PORT / MAIL_USERNAME / MAIL_PASSWORD`

### 4. 启动前端

```powershell
cd E:\all_\frontend
npm install
npm run dev
```

浏览器访问：

```text
http://localhost:5173
```

## Docker 启动

如果你想整套一起启动：

```powershell
cd E:\all_
docker compose up -d --build
```

当前这套项目的关键容器名：

- `cnlp-frontend`
- `cnlp-backend`
- `cnlp-mysql`
- `cnlp-redis`

## 常用文档

- Docker 部署说明：[DEPLOY_DOCKER.md](./DEPLOY_DOCKER.md)
- 提交规范 / 分支说明：[CONTRIBUTING.md](./CONTRIBUTING.md)

## 当前约定

- 本地数据库名：`cloud_native_learning_platform`
- 本地 Redis 地址：`redis://127.0.0.1:6380/0`
- Docker 内部 Redis 地址：`redis://redis:6379/0`
- Docker Redis 容器名：`cnlp-redis`
- 当前版本号见根目录 [VERSION](./VERSION)

## 适合拿来练什么

- Flask 路由与蓝图拆分
- JWT 登录鉴权
- Vue 组件通信与路由
- MySQL 表设计与联表查询
- Redis 缓存与限流
- Docker Compose 编排
- 学习如何维护一个完整的前后端项目

CI test update.
