# Exercise 39: choose a recovery sequence

[Dataset](services.csv) · [Recovery guide](../../study-guides/backup-and-recovery.md)

Offline fictional exercise. Partial SY0-701 5.2 and 3.4. Ready to try.

## Conditions

All three services are down at minute zero. One team can restore only one service at a time. Restore durations are fixed for this exercise and include successful validation. Orders and reports cannot begin restoration until identity is restored. The business owner gives orders priority over reports.

Build a schedule that restores the highest-priority business service as early as possible. Calculate when each service becomes available.

<details>
<summary>Worked schedule</summary>

| Task | Start | Validated finish |
|---|---|---|
| Identity | 0 | 20 |
| Orders | 20 | 50 |
| Reports | 50 | 65 |

Identity is a prerequisite even though it is not listed as the first business service. Restoring reports before orders would delay orders to minute 65. A shorter individual restore does not automatically make it the right first business task.

</details>

## Change the resources

Suppose two teams can work independently, with all other assumptions unchanged. Identity must still finish first. After minute 20, orders and reports can proceed in parallel. Reports finishes at 35 and orders at 50.

More staff does not remove the dependency. These arithmetic results use stipulated durations; they are not measured recovery performance.

NIST's [business impact analysis guidance](https://csrc.nist.gov/pubs/ir/8286/d/upd1/final) connects business impact with prioritization. This simplified schedule is original practice, not a complete business impact analysis.

Draw the dependency before planning the order. If a game supports timed repairs, keep its actual timing separate from the supplied exercise durations.

[Review questions](../../practice-tests/recovery-and-handoff-22.md).
