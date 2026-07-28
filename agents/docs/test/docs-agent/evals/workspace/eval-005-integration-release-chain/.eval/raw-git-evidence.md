# Synthetic Git evidence inputs

在 runner 复制出的隔离 workspace 中执行：

```sh
sh .eval/setup-git-fixture.sh
```

脚本只初始化本地 synthetic Git repository，并提供发布内容、进入检查时的 tag
快照、当前 tag、release-evidence 预期位置和当前分支位置。对象索引写入
`.eval/runtime-git-evidence.md`。

所有发布资格结论必须由执行者依据适用 skill 契约和实际对象读取作出。setup
不生成 audit record、handoff success、`ready_for_tag` 或
`release_verified`，也不执行 schema、自检、CAS 或成功判定。

隔离 fixture 之外的 tag、远端和 GitHub Release 均不在授权范围内。
