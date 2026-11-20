# Exercise 27: test the recovery claim

[Recovery guide](../../study-guides/backup-and-recovery.md) · [Contents](../../study/contents.md)

Offline fictional exercise. Partial SY0-701 3.4. Ready to try.

## The requirement and observations

An outage begins at 10:00. The agreed recovery time objective (RTO) is two hours from outage start to validated required service. The recovery point objective (RPO) allows at most 30 minutes of lost data.

The newest usable recovery point is 09:20. The restore job finishes at 11:15. Required application checks pass at 12:10.

Decide whether each objective is met. Then explain whether the restore job's finish time is enough to close the incident.

<details>
<summary>Worked calculations</summary>

RPO is missed: the usable point is 40 minutes before the outage, exceeding 30 minutes by 10.

RTO is missed under the stated measurement: validated required service returns two hours and 10 minutes after the outage, exceeding the two-hour target by 10 minutes.

The restore job's finish time is not the required service-validation time. Finishing a data restore does not establish that the application's required functions pass.

</details>

## Change one condition

Suppose the usable data point were 09:45, with all other observations unchanged. Explain which objective changes.

<details>
<summary>Changed answer</summary>

RPO is met with a 15-minute recovery-point gap. RTO is still missed. A newer usable backup does not change the given validation time.

</details>

## What to keep

Record the two calculations separately and name the measurement boundary. In a game or simulator, label a game timer as a game observation; do not claim it establishes a real restore test.

Supporting reading: [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Values and questions are original.

[Review questions](../../practice-tests/data-center-decisions-17.md) · [Cards](../../anki/data-center-decisions.txt)
