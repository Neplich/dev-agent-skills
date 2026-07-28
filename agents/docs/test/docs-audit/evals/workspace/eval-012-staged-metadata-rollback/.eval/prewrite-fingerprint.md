# Host transaction fingerprints

## Before attempt

- branch SHA: `2222222`
- porcelain_v2_sha256: `sha256:1111111111111111111111111111111111111111111111111111111111111111`
- staged_raw_sha256: `sha256:2222222222222222222222222222222222222222222222222222222222222222`
- unstaged_raw_sha256: `sha256:3333333333333333333333333333333333333333333333333333333333333333`
- authorized page identity: `100644 blob sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`
- candidate record preimage: absent
- discovery handoff preimage: absent
- unrelated user path: `notes/local.txt`, `100644 blob sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb`

## After failed cleanup

- branch SHA: `2222222`
- porcelain_v2_sha256: `sha256:1111111111111111111111111111111111111111111111111111111111111111`
- staged_raw_sha256: `sha256:9999999999999999999999999999999999999999999999999999999999999999`
- unstaged_raw_sha256: `sha256:3333333333333333333333333333333333333333333333333333333333333333`
- authorized page identity: `100644 blob sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`
- candidate record path: absent
- discovery handoff path: absent
- unrelated user path: `notes/local.txt`, `100644 blob sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb`
