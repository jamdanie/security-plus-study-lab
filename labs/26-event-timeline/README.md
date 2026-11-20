# Exercise 26: build a timeline without inventing a cause

[Contents](../../study/contents.md) · [Incident response](../../study-guides/incident-response.md)

Offline exercise with [fictional events](events.csv). Partial SY0-701 4.9. All timestamps use UTC, all clocks are assumed accurate, and rows are complete only for this supplied sample. Ready to try.

## Investigate the sample

Order the events. Identify:
- The approved change and matching network records.
- The failed and passed application checks.
- The interval between those two checks.
- A cause you suspect but cannot prove from these rows.

Do not call an account owner an attacker based solely on these events.

<details>
<summary>Worked interpretation</summary>

E2 approves CHG-LAB-42. E3 records a move using that identifier. E4 records a failed application check. E5 records restoration of the previous link. E6 records a passed check.

Four minutes separate the failed check at 14:05 and passed check at 14:09. This is an interval between observations, not a proven exact outage duration. The failure could have started before the failed probe or ended before the passed probe.

The ordering is consistent with a problem after the change and improvement after rollback, but does not prove the technical root cause. Check configuration, application details, monitoring coverage, and relevant change records.

</details>

## Why timestamps matter

When using real sources, compare time zones and clock accuracy before correlating events. Keep event identity, source, action, and outcome clear. Record missing evidence rather than filling it with a plausible story.

Supporting reading: [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html), particularly event attributes and verification. This sample and its findings are original.

Save an evidence table with fact, interpretation, and next check. [Review questions](../../practice-tests/data-center-decisions-17.md).
