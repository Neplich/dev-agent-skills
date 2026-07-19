# Formal documentation audit

- Audit phase: pre-tag
- base_ref: `v1.1.0` (`1111111`)
- target_ref: `release-head` (`2222222`)
- target_release_version: `v1.2.0` (maintainer-confirmed)
- Changed files: `M src/catalog/routes.txt`
- Complete affected set: `docs/site/api/catalog-items.md`, `docs/site/api/catalog-status.md`
- Hash algorithm: SHA-256 over exact file bytes
- Audited target_ref commit: `2222222`
- Post-stamp HEAD: `3333333`

## Per-document evidence

- `docs/site/api/catalog-items.md`: pre-stamp `v1.1.0`; post-stamp `v1.2.0`; SHA-256 `4699c95098a22aab06d014d404f452ec0965ef79dc7025255e822e464107a53c`; verified.
- `docs/site/api/catalog-status.md`: pre-stamp `unverified`; post-stamp `v1.2.0`; SHA-256 `995e20a2e7d492592fb455bcc220c9c80ea6afbdee4b28d231e980ca1ce28a7e`; verified.

## Release-version surfaces

- #116 handoff: ready for `v1.2.0`
- `docs/site/release-notes/v1.2.0.md`: SHA-256 `f159690c0f8a816db8efbc2fdb2146ed73f2b04f43fdda4d79e2bd13bd746a77`
- `docs/site/release-notes/index.md`: SHA-256 `88fc254cad95a0a023f125419e5fc3eed7649cda6c99be890019b55d6f1cb248`
- `docs/site/.meta/releases.json`: SHA-256 `0a9cc1bda146381fd73264801d7510cedfbb9ff42f766e3b5b9cf9e0be7388ca`
- `package.json`: SHA-256 `f37f1a40a628982c7ad3297df8a0b3ae5035ac8c46dab0440c9d32b6d3dfa71e`

## Successful unified stamp record

- Stamped pages: `docs/site/api/catalog-items.md`, `docs/site/api/catalog-status.md`
- Stamp read-back: complete; both pages read back as `v1.2.0`
- Atomic record read-back: complete
- Ready result time: `2026-07-19T10:00:00+08:00`

## Conclusion

- Blocking items: none at pre-tag time
- Phase result: `ready_for_tag`
- Meaning: ready for tag creation, not published.
- Review commands: `git diff --name-status v1.1.0 release-head`; host docs checks; release-surface version checks.
