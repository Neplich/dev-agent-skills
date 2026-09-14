# GitHub 发布内容

标题清晰说明版本。正文按本次变化选择重点更新、其他改进、升级说明和变更明细，采用宿主术语和风格。

- 重点更新说明用户能完成的新任务或行为变化。
- 其他改进归纳有实际影响的接口、配置、性能、文档和可靠性变化。
- 升级说明给出适用条件、兼容性、迁移、资产和可执行操作。
- 变更明细使用 PR、commit、contributor 与 compare 链接支持追溯。

每个声明与目标版本证据一致，正文保留实际交付事实和读者需要的动作。相关 PR 可归并成主题，贡献者信息来自实际提交或 PR。

## 本仓库安装信息

生成 dev-agent-skills 发布说明时，从目标版本 manifest 获取插件名称与数量，从目标版本安装文件核对平台能力。

Claude Code 的更新命令取得 marketplace 当前版本；固定版本安装使用目标版本已经支持的安装路径。相应平台支持时可采用：

```text
/plugin marketplace update dev-agent-skills
/plugin update {plugin-name}@dev-agent-skills
/reload-plugins
```

```text
Fetch and follow instructions from https://raw.githubusercontent.com/Neplich/dev-agent-skills/refs/tags/v{VERSION}/.codex/INSTALL.md, setting TARGET_TAG=v{VERSION}
```

```text
/plugins install https://github.com/Neplich/dev-agent-skills/releases/tag/v{VERSION}
```

按目标版本实际支持的平台给出命令，历史版本说明核对该版本对应文件。安装和升级结果用可验证事实表述。
