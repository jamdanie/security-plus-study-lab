# Backup and recovery: saving data is only part of the job

A backup is useful when it can restore the required information and support getting the service working again. A successful backup job does not establish that a full recovery will succeed.

## Two objectives to keep separate

| Objective | Question it helps answer | Example requirement |
|---|---|---|
| Recovery point objective (RPO) | How far back can the recovered data be? | Recover data to within one hour before the outage |
| Recovery time objective (RTO) | How long can recovery take? | Restore the required service within four hours |

RPO concerns the recovery point. RTO concerns recovery duration. The examples are fictional business requirements, not universal targets.

Actual data age and actual recovery time are measurements to compare with the objectives. Scheduling hourly backups alone does not prove an RPO is met: jobs can fail, copies can be incomplete, or the latest usable copy can be older.

## Copies and access paths

File synchronization may copy deletions or unwanted changes to another location. Version history and independent backups can help, depending on retention and protection.

Offline backups are disconnected from the active environment. Immutable storage restricts changes or deletion under its retention controls. These are different properties. Verify how access, retention, and administrative privileges work in the chosen system.

Protect backup confidentiality and make sure recovery staff can obtain required keys through an approved process. An encrypted copy is not recoverable if the required key is unavailable.

## Test the recovery

A useful test checks that selected data can be restored and the required application functions work. Record the recovery point, elapsed time, missing dependencies, and results. Test in an appropriate isolated environment, without replacing production data.

Recovery may require identities, configuration, application software, licenses, and keys in addition to files. Restoring data also does not undo information theft that happened before an outage.

Try the [recovery-planning exercise](../labs/08-recovery-objectives/README.md).

## Sources

- [NIST: Recovery point objective](https://csrc.nist.gov/glossary/term/recovery_point_objective).
- [NIST: Recovery time objective](https://csrc.nist.gov/glossary/term/recovery_time_objective).
- [CISA: StopRansomware Guide](https://www.cisa.gov/sites/default/files/2025-03/StopRansomware-Guide%20508.pdf), backup protection and recovery testing guidance.

Original supporting material. Exam-objective mapping has not been confirmed.
