# E2E Credential Storage

Prefer the project's existing secret mechanism for test accounts. A local JSON
store can use `.qa/e2e/accounts.local.json`, protected by `.gitignore` and file
mode `600` where supported.

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

When authorized to save supplied credentials, update the matching stable ID,
preserve other accounts, refresh the timestamp, and verify local protection.
Keep passwords, tokens, cookies, session values, TOTP seeds, and key material in
that protected mechanism. Committed evidence contains credential IDs and
sanitized observations.

When a required account is unavailable, request the missing access through a
suitable secure channel and continue checks that use available access.
