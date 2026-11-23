# Exercise 32: review backup exposure

[Recovery guide](../../study-guides/backup-and-recovery.md) · [Contents](../../study/contents.md)

Offline fictional exercise. Partial SY0-701 3.4. Ready to try.

## The stated incident

An attacker controls a production account that can delete any backup it can reach. Compare these arrangements using only the assumptions given.

| Copy | Production account can reach and delete it? | Restore evidence |
|---|---|---|
| A: connected share | Yes | Previous test passed |
| B: disconnected copy | No during disconnection | No restore test recorded |
| C: second connected share | Yes | Job completed, no restore test |

Which copies are exposed to deletion through this account? Which have demonstrated restoration in the supplied record? Does any row alone establish complete incident recovery?

<details>
<summary>Worked answer</summary>

A and C are exposed under the stated account permissions. B is outside that account's reach while disconnected, but its recoverability is untested in the supplied record.

A has evidence of a previous restore test; that does not remove its current deletion exposure. A completed job for C is not the same as a restore test.

No row establishes complete incident recovery. You still need usable data, required dependencies, a safe recovery process, and validation against service requirements.

</details>

## Keep the requirements separate

Copy count, access isolation, encryption, retention, and recoverability answer different questions. A second copy reachable by the same compromised account can share its exposure.

CISA recommends offline encrypted backups and regular testing. [Supporting CISA fact sheet](https://www.cisa.gov/sites/default/files/publications/CISA_Fact_Sheet-Protecting_Sensitive_and_Personal_Information_from_Ransomware-Caused_Data_Breaches-508C.pdf). The table is fictional, not a product guarantee.

Sketch the three copies and the account's allowed paths. Cross out the paths to B while it is disconnected. No ransomware or destructive command is part of this exercise.

[Review questions](../../practice-tests/permissions-and-data-19.md).
