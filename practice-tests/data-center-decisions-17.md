# Data center decisions 17

Six original questions. Partial SY0-701 connections: 3.4 (1, 4, 5), 4.5 (2), and 4.9 (3, 6). These are author-selected links, not official question classifications or a weighted mock exam.

[Mission directory](../resources/hands-on-missions.md) · [Contents](../study/contents.md)

## 1. Two web servers depend on one database for every successful request. The database stops. What follows under these assumptions?

- A. Both web servers can still complete requests.
- B. Another web server always fixes it.
- C. The shared dependency prevents either from completing requests.
- D. The backup automatically becomes a live service.

## 2. Guest access to payroll is forbidden. A guest requests payroll over TCP 443. What follows?

- A. Deny under the stated policy.
- B. Allow because 443 means authorized.
- C. Allow because the cable is connected.
- D. Allow because every encrypted request is safe.

## 3. A failed probe is at 14:05 and the next supplied passed probe is at 14:09. What is established?

- A. The exact outage lasted four minutes.
- B. An attacker caused a four-minute outage.
- C. The system was healthy at every other moment.
- D. Four minutes separate the two observations.

## 4. An outage starts at 10:00. RPO is 30 minutes; the newest usable point is 09:20. What is the result?

- A. RPO is met because restoration is fast.
- B. RPO is missed by 10 minutes.
- C. RTO must also be missed.
- D. The backup schedule alone proves success.

## 5. RTO is two hours from 10:00 to validated service. Restore finishes 11:15; required checks pass 12:10. Which result fits?

- A. RTO is met at 11:15.
- B. RPO must be two hours.
- C. RTO is missed by 10 minutes.
- D. A completed restore proves every function works.

## 6. A change precedes a failed check and rollback precedes a passed check. What is the best conclusion?

- A. The order supports investigation of the change, but root cause needs more evidence.
- B. The account is certainly malicious.
- C. The logs prove the cable was defective.
- D. No further verification is useful.

<details>
<summary>Answers and explanations</summary>

1. **C.** C follows the dependency. A ignores it. B adds more users of the same failed dependency. D assumes restoration or failover that was not provided.

2. **A.** A applies the destination restriction. B confuses port with permission. C establishes no authorization. D assumes both encryption and safety from insufficient evidence.

3. **D.** D is the measured interval. A assumes exact start and end boundaries. B invents intent and cause. C generalizes beyond the sample.

4. **B.** B compares a 40-minute gap with the 30-minute target. A confuses recovery time with data point. C needs restoration timing. D ignores actual usability.

5. **C.** C uses the defined boundary. A stops measurement early. B confuses objectives. D assumes untested functions.

6. **A.** A separates correlation from cause. B and C assert unsupported explanations. D abandons needed verification.

</details>

For errors and correct guesses, return to the related mission. Explain the dependency, policy constraint, evidence limit, or calculation before repeating the question. The [new missions](../resources/hands-on-missions.md#next-missions) link the supporting material.
