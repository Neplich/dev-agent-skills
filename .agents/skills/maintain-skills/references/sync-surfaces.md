# Skill Sync Surfaces

Select the surfaces affected by the actual change:

| Surface | Contents |
| --- | --- |
| Registration | Marketplace Skill paths, plugin sources and manifests, Kimi directories, lockfile paths and hashes |
| Discovery | Marketplace and plugin descriptions, Skill name and description |
| Capability directories | Role navigation Skill and bilingual role READMEs |
| Public documentation | Root READMEs, architecture and installation guides |
| Shared references | Source files, generated plugin copies and applicable host assets |
| Verification | Behavior, installation, metadata and link tests |

`skills-lock.json` records a SHA-256 hash over tracked paths and content within each Skill directory. A reference, script or asset change updates that Skill's hash together with the implementation.

Shared reference copies are generated from `agents/product_manager/skills/idea-to-spec/_internal/_shared/`. Host-site assets are copied during bootstrap; when their behavior changes, document the actual update action for existing hosts.
