# Host docs checks

- command: `npm ci --ignore-scripts`
- cwd: `docs/site`
- result: passed
- command: `npm run test:docs`
- cwd: `docs/site`
- result: passed
- source: release manager read-only checkout of `refs/heads/release-candidate` at `5dc0861b549124be38709d4ae35ff21c52af55c7`, captured with `release-evidence/git-reference-snapshot.md`
