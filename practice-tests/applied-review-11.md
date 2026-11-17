# Applied review 11: explain the decision

Four original offline tasks. These practice interpretation and verification, but do not reproduce CompTIA performance-based question interfaces or scoring. No learner results are recorded.

## 1. Fix the boundary

A first-match policy permits Any source to an application on Transmission Control Protocol (TCP) port 443, then denies the guest network, then denies everything else. The requirement permits only staff access.

Name the smallest rule change that directly enforces staff-only access. List one allowed and two denied tests.

<details>
<summary>Worked answer</summary>

Narrow the first permit's source to staff. Test staff-to-application TCP 443 as allowed, guest-to-application TCP 443 as denied, and another nonstaff source to the same service as denied. Testing only guests can miss access from other unapproved sources.

Moving the guest deny first blocks guests but leaves other nonstaff sources allowed by the broad permit.

</details>

[Review firewall rules](../study-guides/network-segmentation.md). Partial 4.5 alignment.

## 2. Explain both recovery measurements

An outage occurs at 11:00. The newest usable data point is 10:40. The required service is validated at 14:30. The recovery point objective is 30 minutes; the recovery time objective is three hours. Measure recovery duration from the outage.

<details>
<summary>Worked answer</summary>

Data age is 20 minutes, within the 30-minute recovery point objective (RPO). Recovery takes three hours 30 minutes, exceeding the recovery time objective (RTO) by 30 minutes.

Meeting the RPO does not offset missing the RTO. Ask which dependencies delayed restoration before proposing a fix.

</details>

[Review recovery](../study-guides/backup-and-recovery.md). Partial 5.2 alignment.

## 3. Revise the analyst's conclusion

An analyst writes: "Four accounts failed from the same source label, and one later succeeded, so all four accounts are compromised."

Rewrite the finding to separate observation from inference and identify a useful evidence request.

<details>
<summary>Worked answer</summary>

The source label appears in failed logins for four accounts and a later success for one account. Investigate that session and correlate identity-provider records, factor results, and subsequent actions before deciding whether compromise occurred.

The failed attempts do not establish control of every account or which passwords were tested.

</details>

[Review the logs exercise](../labs/05-sign-in-log-review/README.md). Partial 4.9 alignment.

## 4. Repair the help-desk advice

A user receives an unexpected certificate hostname warning on enterprise wireless. Help-desk advice says: "Accept it because the network name looks correct."

Explain the missing trust check and a better next step.

<details>
<summary>Worked answer</summary>

The Service Set Identifier (SSID), or network name, does not establish the authentication server's identity. Check the expected server identity, certificate configuration, and trusted client profile through the approved support process. Do not routinely bypass the warning.

A misconfiguration is possible; the warning does not by itself prove an evil twin.

</details>

[Review wireless access](../study-guides/wireless-access.md) and [certificate trust](../concepts/certificate-trust.md). Partial 4.1 and 1.4 alignment.

## Review method

For each task, check whether you named the requirement, used only supplied evidence, and included a verification step. A remembered answer letter cannot replace that explanation.
