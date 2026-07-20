# Host docs checks

- command: `npm ci --ignore-scripts`
- cwd: `docs/site`
- result: passed
- command: `npm run test:docs`
- cwd: `docs/site`
- result: passed
- source: runtime immutable target ref `refs/heads/fixture-target` (resolve exact commit after `.eval/setup-git-fixture.sh`; commands are rerun from that detached target workspace)
