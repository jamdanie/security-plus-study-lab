# Exercise 43: assess the evidence behind a claim

[Dataset](evidence.csv) · [Control guide](../../study-guides/security-controls.md)

Offline fictional exercise. Partial SY0-701 5.5. Ready to try.

## Assessment question

The requirement is that logging is enabled on every lab host during the current review. Read the supplied records. Which items establish the requirement, describe intended practice, or contradict the claim?

Write a finding with the requirement, evidence, gap, and next verification. Do not expand a sample from one host into a statement about every host.

<details>
<summary>Worked review</summary>

E1 states what should happen; it is not proof of implementation. E2 is limited to host-a in the previous month. It does not establish current fleet-wide operation.

E3 is current evidence of a mismatch on host-b. E4 records the administrator's statement, which conflicts with E3 and needs clarification.

A defensible finding is: the current configuration export for host-b shows logging disabled, contrary to the requirement. Review the relevant configuration and history, resolve the discrepancy, and validate corrected behavior under the approved process. Broader coverage remains unestablished.

</details>

## Choose complementary methods

Examine relevant policies and configuration records, interview the responsible staff to clarify the discrepancy, and test authorized sample behavior against the assessment objective. Record scope, date, and limitations for each.

[NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) describes examine, interview, and test methods. This is an original small evidence exercise, not a complete audit procedure.

For a game connection, inspect only the evidence the product actually provides. A screenshot of one setting does not prove every system is configured the same way.

[Questions](../../practice-tests/evidence-and-automation-24.md).
