# 通用爬虫（揭榜挂帅）

一个面向公开互联网信息采集场景的可扩展数据采集平台骨架。

项目目标不是做“一个站点一个脚本”的临时爬虫，而是搭建一套可持续扩展的采集框架：

- 支持普通网页、JSON 接口等公开数据源；
- 支持按站点或业务快速增加新的采集器；
- 统一任务调度、去重、清洗、存储、导出与日志；
- 预留浏览器采集、智能体/API 接入、分布式执行等扩展能力；
- 尽量把复杂技术封装在底层，对使用者提供简单配置与任务接口。

> 合规说明：本项目只用于合法、授权或公开数据采集，不包含绕过登录、验证码、访问控制、付费墙或其他安全限制的能力设计。

## 1. 当前阶段

当前仓库是“第一阶段最小可运行版本（MVP）”骨架，已经具备：

- HTTP 页面采集；
- JSON 接口采集；
- 采集器插件注册机制；
- 简单任务执行入口；
- 文本摘要与基础清洗；
- 基于 URL + 内容指纹的去重；
- JSONL 结果导出；
- 日志记录；
- FastAPI 查询/提交任务接口；
- 为 Playwright、数据库、消息队列和智能体接口预留扩展点。

## 2. 推荐技术路线

| 模块 | 首期方案 | 后续可扩展 |
|---|---|---|
| HTTP 采集 | httpx | aiohttp / 代理池（合规场景） |
| 页面解析 | BeautifulSoup / lxml | trafilatura / readability |
| 动态网页 | 预留接口 | Playwright |
| 服务接口 | FastAPI | 鉴权、任务管理后台 |
| 任务调度 | 轻量任务服务 | APScheduler / Celery |
| 数据存储 | JSONL | SQLite / PostgreSQL / Elasticsearch |
| 去重 | URL + SHA256 指纹 | SimHash / 向量近似去重 |
| 配置 | YAML / 环境变量 | 配置中心 |
| 日志 | logging | Prometheus / Grafana / OpenTelemetry |

## 3. 目录结构

```text
general-crawler-bounty/
├─ app/
│  ├─ api/             # FastAPI 接口
│  ├─ collectors/      # 采集器插件
│  ├─ core/            # 配置、日志、注册机制
│  ├─ models/          # 数据模型
│  ├─ services/        # 任务、清洗、去重、导出
│  ├─ storage/         # 存储适配器
│  └─ utils/           # 通用工具
├─ config/             # 示例配置
├─ data/input/         # 输入数据
├─ data/output/        # 输出结果
├─ docs/               # 技术方案与阶段计划
├─ logs/               # 运行日志
├─ scripts/            # CLI 脚本
├─ tests/              # 测试
├─ .env.example
├─ .gitignore
├─ pyproject.toml
└─ README.md
```

## 4. 快速启动

### 4.1 创建环境

```bash
python -m venv .venv
```

Windows：

```bash
.venv\Scripts\activate
```

macOS / Linux：

```bash
source .venv/bin/activate
```

安装依赖：

```bash
pip install -e .
```

### 4.2 启动 API

```bash
uvicorn app.api.main:app --reload
```

打开：

```text
http://127.0.0.1:8000/docs
```

### 4.3 命令行采集

```bash
python scripts/run_task.py --url https://example.com --collector html
```

JSON 接口示例：

```bash
python scripts/run_task.py --url https://httpbin.org/json --collector json
```

采集结果默认写入：

```text
data/output/results.jsonl
```

## 5. 后续开发顺序

第一优先级：把核心任务链路跑稳。

1. 补充站点级采集器模板；
2. 引入 SQLite/PostgreSQL 保存任务状态；
3. 增加 Playwright 动态网页采集器；
4. 增加定时任务与批量 URL 任务；
5. 增加统一字段映射、正文提取与质量检测；
6. 增加管理后台；
7. 根据实际业务增加智能体/API 适配器。

详细内容见：

- `docs/technical-plan.md`
- `docs/milestones.md`
- `docs/development-plan.md`
- `docs/codex-first-tasks.md`

## 6. 给 Codex 的一句话任务说明

> 在现有骨架上，优先完善“任务创建 → 采集器执行 → 清洗去重 → 结果存储 → 状态查询”的完整闭环。每新增功能都要配测试，避免先做复杂前端或过度设计。
