# E2E Credential Store Reference

This reference defines how QA skills store local E2E credentials. It is for
test-only accounts and SSH access used during QA validation.

## Local File

All local E2E credentials are stored in:

```text
.qa/e2e/accounts.local.json
```

The file must stay local and must be ignored by git. Do not create or commit
real credentials in repository documents, eval fixtures, reports, or scripts.

## Schema

```json
{
  "schema_version": "1.0",
  "updated_at": "YYYY-MM-DDTHH:mm:ssZ",
  "platform_accounts": [
    {
      "id": "platform.default.admin",
      "platform": "default",
      "role": "admin",
      "base_url": "",
      "username": "",
      "password": "",
      "totp_secret": "",
      "notes": ""
    }
  ],
  "ssh_accounts": [
    {
      "id": "ssh.default.deploy",
      "host": "",
      "port": 22,
      "role": "deploy",
      "username": "",
      "password": "",
      "private_key_path": "",
      "passphrase": "",
      "notes": ""
    }
  ]
}
```

## Credential IDs

- Platform account: `platform.<platform-slug>.<role-slug>`
- SSH account: `ssh.<host-slug>.<role-slug>`

Use stable lowercase slugs. If the user does not provide a slug, infer the
smallest clear slug from the platform, host, or role.

## Upsert Rules

When the user provides platform account, password, SSH account, SSH password,
SSH key path, or passphrase details:

1. Create `.qa/e2e/` if needed.
2. Read `.qa/e2e/accounts.local.json` if it exists.
3. Upsert by `id`; do not overwrite unrelated accounts.
4. Update `updated_at`.
5. Write the file with UTF-8 JSON.
6. Run `chmod 600 .qa/e2e/accounts.local.json` when the local environment
   supports it.
7. Ensure `.gitignore` contains `.qa/e2e/accounts.local.json`.

## Documentation Rules

Committed QA documents may only reference credential IDs:

```markdown
- 平台账号引用：`platform.default.admin`
- SSH 账号引用：`ssh.default.deploy`
```

Do not write plaintext usernames, passwords, tokens, cookies, sessions, TOTP
secrets, SSH passwords, SSH private key contents, or SSH passphrases into:

- `docs/qa/e2e/**`
- `agents/**/test/**`
- `cases/`
- `scripts/`
- `results/`
- `_reports/`
- eval fixture files
- conversation summaries intended for commit

If a required credential is absent or the requested `credential_ref` cannot be
resolved, mark the affected E2E task as `blocked` and ask for the missing
account reference or local credential details.
