# 可直接粘贴给 Codex 的启动提示词

你现在负责维护“通用爬虫（揭榜挂帅）”项目。

请先阅读 README.md、docs/technical-plan.md、docs/development-plan.md 和 docs/codex-first-tasks.md。

当前目标不是重构整个项目，而是把第一阶段 MVP 做成稳定、可扩展、可测试的采集平台。

优先执行 docs/codex-first-tasks.md 中的 P0 任务：

1. 使用 SQLite 持久化任务状态；
2. 增加任务列表和筛选接口；
3. 为 HTTP 请求增加合理重试、响应大小限制和域名级并发限制；
4. 为 HTML、JSON 采集器和任务服务补充测试；
5. 保持现有 Collector Registry 插件机制；
6. 不加入验证码绕过、登录绕过、访问控制规避等功能。

每完成一个阶段：

- 运行测试；
- 更新 README；
- 简要说明改动文件、设计理由、测试结果和下一步建议。

如果现有代码有明显结构问题，可以小范围调整，但不要过度设计。
