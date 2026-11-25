# Exercise 38: review an expiring security exception

[Risk guide](../../study-guides/risk-management.md) · [Baseline guide](../../study-guides/secure-baselines.md) · [Records](exceptions.csv)

Offline fictional exercise. Partial SY0-701 5.2 and 1.3. Ready to try.

## Policy

Review at 17:00 UTC on November 25, 2026. A deviation may remain only when it has an owner, approval, and an unexpired end time. Expired or pending records do not authorize a deviation. Required follow-up is to restore the baseline through the approved process or obtain a newly authorized decision before continuing.

This policy belongs to the exercise. It does not describe every organization's exception process.

Identify which records currently authorize a deviation and what needs follow-up.

<details>
<summary>Worked review</summary>

EX1 has an owner, approval, and a future expiry. It currently meets the stated conditions but expires in one hour. Plan the required baseline restoration or authorized decision before that deadline.

EX2 expired the previous day. Its approved status does not make the old approval permanent.

EX3 is pending and has no owner. A future expiry alone does not authorize it.

</details>

## Explain the risk

An exception documents a decision; it does not remove the underlying exposure. State which additional access the temporary setting permits and who is responsible for the next decision.

If a team adds monitoring as a compensating measure, explain what it observes and what it does not block. Do not assume monitoring makes the temporary access equivalent to the baseline.

At 18:05, reevaluate EX1. Under the supplied policy, it is expired unless a new decision has actually been authorized.

Keep the record ID, failed condition, next action, and evidence needed to close the review. [Questions](../../practice-tests/layers-and-exceptions-21.md) · [Cards](../../anki/layers-and-exceptions.txt).
