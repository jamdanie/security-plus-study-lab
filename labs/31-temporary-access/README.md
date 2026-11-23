# Exercise 31: review temporary administrative grants

[Guide](../../study-guides/privilege-decisions.md) · [Dataset](grants.csv) · [Contents](../../study/contents.md)

Offline fictional exercise. Partial SY0-701 4.6. Ready to try.

## Policy and review time

The approved task is restarting lab-web between 17:00 and 18:00 UTC on November 23, 2026. Grants must be limited to that service, must not outlast the window, and require approval from someone other than the recipient.

Review the records at **17:30 UTC**. Treat expiry times as enforced. All accounts are otherwise authenticated. An expiry at 18:00 means the grant is active before 18:00.

For each grant, identify scope, approval, and time issues separately.

<details>
<summary>Worked review</summary>

G1 meets the stated conditions at 17:30.

G2 is too broad and has no expiry. Its independent approver does not resolve either issue.

G3 has the right scope and expiry, but the recipient approved their own grant. It fails the independent-approval condition.

G4 is expired at the review time. Do not extend it by assumption; follow the approval process if access is still needed.

</details>

## Change the condition

Review G1 at 18:05. Its scope has not changed, but it is no longer active. Explain why “it was approved earlier” is insufficient.

For optional simulator practice, identify whether your tool actually supports scoped, expiring roles. If it does not, use this dataset rather than claiming a game implements them.

Keep a four-row review and one proposed correction per failed condition. [Questions](../../practice-tests/permissions-and-data-19.md).
