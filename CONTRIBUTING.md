提交规范与分支说明

这份文档用于约束当前仓库的日常开发习惯，目标是让提交记录更清晰、分支更容易维护。

## 分支说明

- `main`
  - 默认主分支
  - 只保留相对稳定、可运行的内容
  - 适合阶段性整理后再合并

- `feat/<name>`
  - 新功能分支
  - 例：`feat/course-search`

- `fix/<name>`
  - Bug 修复分支
  - 例：`fix/login-rate-limit`

- `docs/<name>`
  - 文档调整分支
  - 例：`docs/readme-cleanup`

- `chore/<name>`
  - 工程化、配置、依赖、目录清理
  - 例：`chore/docker-cleanup`

如果只是个人本地小步练习，也可以直接提交到 `main`。  
但只要改动开始变多，建议切到功能分支再合并回来。

## 提交规范

推荐使用下面这套前缀：

- `feat:` 新功能
- `fix:` 修复问题
- `docs:` 文档改动
- `refactor:` 重构
- `style:` 仅格式或注释调整
- `test:` 测试相关
- `chore:` 配置、清理、依赖调整
- `build:` 构建与部署相关
- `perf:` 性能优化

## 提交示例

```text
feat: 新增课程关键词搜索
fix: 修复管理员概览缓存失效问题
docs: 重写 README 和开发说明
chore: 清理多余文件并整理 docker 配置
refactor: 拆分账号模块校验逻辑
```

## 提交建议

- 一次提交只做一类事情
- 先改代码，再补文档
- 配置变更时同步更新：
  - `backend/env.example`
  - `README.md`
  - `DEPLOY_DOCKER.md`
- 不要把临时产物提交进仓库

## 不应提交的内容

下面这些默认不应该进 Git：

- `backend/.env`
- `frontend/node_modules`
- `frontend/dist`
- 本地缓存目录，如 `__pycache__`
- 临时测试脚本、临时截图、临时导出文件

## 推荐工作流

### 本地小步开发

```powershell
git status
git add .
git commit -m "feat: 这里写本次改动"
```

### 新功能分支

```powershell
git checkout -b feat/your-feature
git add .
git commit -m "feat: 完成某个功能"
git push -u origin feat/your-feature
```

### 合并前自查

- 项目能启动
- 关键页面能打开
- 关键接口能调用
- 文档没有明显过期
- 没有把本地私密配置提交进仓库
