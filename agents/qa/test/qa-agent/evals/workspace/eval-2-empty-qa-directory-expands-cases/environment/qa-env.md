# QA Environment

- Target route: `/settings/profile`
- Browser validation: use the active Codex Chrome plugin / browser connector
  against `QA_BASE_URL`; if `QA_BASE_URL` is missing, mark browser checks
  blocked.
- Auth: use credential ref `platform.profile-settings.qa_user`; do not write
  account, password, token, cookie, or session values into TC, script, or result
  files.
- Feature flag: `profile_settings_refresh=true`
