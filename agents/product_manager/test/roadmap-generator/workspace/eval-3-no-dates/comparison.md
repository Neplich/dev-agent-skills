# Eval Result: roadmap-no-dates

## Evaluation Target

- Skill: `roadmap-generator`
- Test case: Go roadmap when milestones have no due dates
- Test set: roadmap generator eval workspace
- Entry: workspace `eval-3-no-dates`
- Latest result: PASS

## With Skill

- Correctly treats open milestones without due dates as unscheduled instead of inventing dates.
- Lists progress counts and milestone links while staying explicit about missing schedule data.

## Baseline

- Earlier output grouped all open milestones under unscheduled but did not provide enough semantic classification.
- Iteration 2 improved classification into patch releases, next release, far future, tool ecosystem, sub-projects, and unplanned/backlog.

## Failures

- None recorded.

## Next Steps

- Keep this eval for no-date handling and semantic milestone grouping.
- Runtime roadmap outputs should not be committed.
