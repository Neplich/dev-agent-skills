# 数据库证据

- `migrations/2026071901_add_message_files.sql` 新增 nullable JSONB 字段 `message_files`。
- 迁移先加 nullable 列，再由后台任务回填；不锁表改成 NOT NULL。
- 回滚只删除新列，会丢失已写入附件元数据，执行前必须备份。
