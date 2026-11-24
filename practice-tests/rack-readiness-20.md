# Rack readiness 20

Six original questions. Partial SY0-701 4.1 (1–2), 4.3 (3), and 4.4 (4–5). Question 6 checks learning-evidence interpretation. This is not a weighted mock exam.

[Campaign](../resources/rack-security-campaign.md) · [Contents](../study/contents.md)

## 1. A fictional release policy forbids shared factory credentials. The observed setting leaves one enabled. What follows?

- A. The requirement is met because logging is on.
- B. Correct it through the approved process and verify authentication behavior.
- C. Publish the credential in the ticket.
- D. Ignore it because the server is new.

## 2. An approved baseline restricts administration to the management zone, but observed access is any-zone. Which verification addresses the correction?

- A. Rename the server.
- B. Check only the asset tag.
- C. Test allowed management access and denied access from another zone.
- D. Count the rack cables.

## 3. A package reports 2.4, but the running service is 2.3 and vendor instructions require restart. Is installation success enough to close the finding?

- A. No; verify the approved restart, running version, targeted validation, and required functions.
- B. Yes; the installer is the only relevant evidence.
- C. Yes; older running versions are always harmless.
- D. No; every patch must break the application.

## 4. A test has 10 malicious events. A rule alerts on 9 malicious and 30 benign events. How many malicious events were missed?

- A. 30.
- B. 39.
- C. 9.
- D. 1.

## 5. Another rule alerts on 6 malicious and 3 benign events in the same test. What is established compared with the first rule?

- A. It detects every attack.
- B. It has fewer benign alerts but misses more malicious events.
- C. It is universally the best rule.
- D. It eliminates the need for review.

## 6. A game does not model patch versions. How should a learner use the patch mission?

- A. Claim the game verified the running version.
- B. Invent a successful scan.
- C. Use the supplied offline evidence and label the result accordingly.
- D. Treat the game score as a vulnerability report.

<details>
<summary>Answers and explanations</summary>

1. **B.** B addresses the mismatch and checks the result. A substitutes another control. C exposes a credential. D provides no justification.

2. **C.** C tests the intended access boundary. A, B, and D do not verify that boundary.

3. **A.** A follows the unresolved evidence. B ignores effective state. C invents safety. D invents inevitable failure.

4. **D.** D is 10 minus 9. A counts benign alerts, B all alerts, and C detected malicious events.

5. **B.** B describes the supplied tradeoff. A contradicts the labels. C requires a decision criterion not supplied. D assumes automation replaces investigation.

6. **C.** C preserves what was actually practiced. A, B, and D claim evidence the game does not supply.

</details>

Review guesses along with errors. Return to the campaign activity, explain the requirement, and try a changed condition. Sources are linked in the activities.
