# Exercise 8: does this recovery meet the objectives?

Status: ready to try. No learner completion results have been recorded.

This is an offline exercise using a fictional booking service. No real systems or files are changed.

## Requirements and timeline

The service has a recovery point objective (RPO) of one hour and a recovery time objective (RTO) of four hours. For this exercise, measure both from the outage at 14:00, with no earlier hidden corruption.

All times are on the same fictional day in Coordinated Universal Time (UTC).

| Time | Event |
|---|---|
| 12:30 | Data point captured in the latest usable backup |
| 13:30 | Scheduled backup fails |
| 14:00 | Outage begins |
| 17:00 | Required service is restored and validated using the 12:30 data point |

Assume no transaction logs or other recovery copies are available.

## Decide before opening the answer

1. How old is the recovered data relative to the outage?
2. Does that meet the RPO?
3. How long did service recovery take?
4. Does that meet the RTO?
5. Does an hourly backup schedule prove the RPO was achieved?

<details>
<summary>Suggested answer</summary>

The recovered data point is 90 minutes before the outage. That exceeds the one-hour RPO by 30 minutes.

Service recovery took three hours, meeting the four-hour RTO under the exercise's stated measurement.

The hourly schedule did not establish the recovery result because the 13:30 job failed. The actual usable recovery point matters.

</details>

## Change the scenario

A second recovery option contains data captured at 13:30, but service recovery and validation finish at 19:00. Assume the copy is usable and all other conditions are unchanged.

<details>
<summary>Compare the second option</summary>

The recovered data is 30 minutes old at the outage, so the one-hour RPO is met. Recovery takes five hours, so the four-hour RTO is missed by one hour.

Meeting one objective does not establish that the other is met.

</details>

## Record a recommendation

Describe one improvement to investigate, what evidence would show it works, and any dependencies you would test. For example, failed-job alerts could help staff detect the missing backup sooner, but an alert by itself does not create a usable copy.

[Read the backup and recovery guide](../../study-guides/backup-and-recovery.md).
