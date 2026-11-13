# Incident response: limit harm and keep useful evidence

An alert is a signal to assess. An incident determination requires context and the organization's criteria. A suspicious login alone does not establish the full scope of a compromise.

## Know the purpose of each action

| Action | Purpose | Example |
|---|---|---|
| Preparation | Make response possible before an incident | Assign authority, contacts, logging, and playbooks |
| Detection and analysis | Establish what happened and assess scope | Correlate an alert with identity and host evidence |
| Containment | Limit continuing harm or spread | Isolate an affected endpoint through an approved process |
| Eradication | Remove the cause or foothold | Remove persistence and address the exploited weakness |
| Recovery | Restore validated operations | Restore service, test it, and monitor for recurrence |
| Lessons learned | Improve future prevention and response | Assign and verify a fix for a response gap |

These are useful study distinctions, not a claim that every framework uses the same linear phases. Response may loop as evidence changes. NIST SP 800-61 Revision 3 integrates incident response with the Cybersecurity Framework (CSF) 2.0 rather than simply repeating older phase diagrams.

## Preserve evidence while responding

Record times, actions, systems, decision makers, and evidence handling. Use the approved response process. Isolation can reduce spread, but turning off or rebuilding a system can destroy volatile or disk evidence. Balance urgent harm reduction and preservation with the authorized response team.

Chain of custody documents evidence handling and transfers. Hashes support checking whether collected bytes changed; they do not replace the handling record or prove how evidence was collected.

## Do not confuse containment with recovery

Disconnecting an affected workstation can contain communication without removing malware. Restoring a file can improve availability without closing the original access path. Validate the cause, required fixes, and service operation before declaring recovery complete.

Try the [sign-in evidence exercise](../labs/05-sign-in-log-review/README.md) and [practice set 2](../practice-tests/foundations-02.md).

## Source

[NIST SP 800-61 Revision 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
