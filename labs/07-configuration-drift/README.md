# Exercise 7: review configuration drift

Status: ready to try. No personal completion results have been recorded.

This is an offline exercise about a fictional shared workstation. Do not apply these example values to your computer as a hardening standard.

## Approved reference

Baseline version 1 applies to this workstation. Its fictional requirements and observations are:

| Setting | Approved value | Observed value |
|---|---|---|
| Automatic screen lock | 5 minutes | 20 minutes |
| Host firewall | Enabled | Enabled |
| Guest account | Disabled | Enabled |
| Security event logging | Enabled | Disabled |
| Remote support service | Disabled | Enabled |

The change register contains one approved exception: remote support may remain enabled during a maintenance window ending at 18:00 UTC on the fictional exercise day. The review takes place at 16:00 UTC that day. The exception requires access restricted to the support network and logging enabled.

UTC means Coordinated Universal Time. The table does not establish whether the service's access restriction is configured.

## Your decisions

1. Identify every value that differs from baseline version 1.
2. Identify which difference has an approved exception.
3. Does the exception make the workstation fully compliant with its conditions?
4. What would you verify before changing the remote support setting?
5. What evidence would help explain the other differences?

<details>
<summary>Suggested answer</summary>

Screen lock, guest account, logging, and remote support differ from the reference. The host firewall matches.

Remote support has a time-limited exception, but compliance with its conditions is not established. Logging is disabled, contrary to the exception, and the support-network restriction has not been verified.

Confirm that the approval applies to this workstation and review time. Verify the network restriction and investigate the disabled logging. Coordinate changes with the responsible owner so required maintenance is not interrupted without a plan.

For the other differences, review approved changes, management records, and available system logs. Do not conclude that an attacker caused them from this table alone.

</details>

## Explain a correction

Choose one difference and describe the expected value, why the difference matters, who should authorize the correction, and how you would verify the result. If logging was disabled, restoring it does not reconstruct events that were never recorded.

[Read the baseline guide](../../study-guides/secure-baselines.md) and connect this exercise to the [log-review exercise](../05-sign-in-log-review/README.md).
