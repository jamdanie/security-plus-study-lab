# Exercise 35: verify what the patch changed

[Vulnerability guide](../../study-guides/vulnerability-management.md) · [Campaign](../../resources/rack-security-campaign.md)

Offline fictional exercise. Partial SY0-701 4.3. Ready to try. Product versions below are invented and do not name real vulnerabilities.

## Supplied evidence

The fictional vendor says LabService 2.4 fixes finding LAB-001. A maintenance record says the installer completed successfully.

After the maintenance:
- The package inventory reports 2.4.
- The running service still reports 2.3.
- The vendor instructions say a service restart is required.
- The targeted validation has not run.
- Required application checks have not run.

Should the finding be closed? What should the responder verify next?

<details>
<summary>Worked answer</summary>

Do not close the finding from installer success alone. The running service evidence indicates the old version is still active.

Follow the approved change procedure and vendor instructions for the required restart. Verify the running version afterward, perform appropriate targeted vulnerability validation, and check required application functions. Record the results and any remaining risk.

Do not assume the restart or later checks succeed. Those are next actions, not observations already supplied.

</details>

## Change one condition

Suppose the running service reports 2.4 but the targeted validation still reports LAB-001. Investigate applicability, test reliability, and remaining exposure rather than overwriting the result to match the ticket.

Supporting reading: [NIST SP 800-40 Rev. 4, Guide to Enterprise Patch Management Planning](https://csrc.nist.gov/pubs/sp/800/40/r4/final). NIST treats enterprise patch management as preventive maintenance. This exercise supplies its own fictional conditions.

[Questions](../../practice-tests/rack-readiness-20.md) · [Learning notes](../../study/hands-on-notes.md)
