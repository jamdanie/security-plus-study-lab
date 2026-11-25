# Layers and exceptions 21

Six original questions. Partial SY0-701 2.5 (1–2) and 5.2/1.3 (3–5); question 6 checks interpretation of learning evidence. This targeted set is not a weighted mock exam.

[Layered controls](../labs/37-layered-controls/README.md) · [Exception review](../labs/38-exception-review/README.md) · [Mission selector](../resources/mission-selector.md)

## 1. Staff-zone traffic is permitted, but records require a records-reader role. An account in that zone lacks the role. What follows?

- A. Network access automatically grants records.
- B. The application denies the record under its rule.
- C. Logging assigns the role.
- D. The zone must be malicious.

## 2. Application authorization is removed while the permitted staff path and logging remain. What do the stated remaining controls establish?

- A. They necessarily enforce the missing application role.
- B. Logging blocks every unauthorized request.
- C. They do not replace the removed role check.
- D. The network rule has disappeared.

## 3. An exception expired yesterday but its status still reads approved. Policy requires unexpired approval. Is it currently valid?

- A. No; the expiry condition fails.
- B. Yes; the status always overrides time.
- C. Yes; it never needs an owner.
- D. Only if the filename changes.

## 4. A pending exception has a future expiry but no owner. What is established?

- A. The future expiry authorizes it.
- B. The risk is eliminated.
- C. It is equivalent to the baseline.
- D. It fails the approval and ownership requirements.

## 5. A valid exception expires in one hour. What is an appropriate next step?

- A. Ignore the end time.
- B. Plan approved baseline restoration or obtain a new authorized decision before continuing.
- C. Silently change the old expiry.
- D. Claim monitoring removes every risk.

## 6. A game does not model application roles. How should a learner complete the layered-control task?

- A. Treat visible packets as proof of authorization.
- B. Invent a role test result.
- C. Use the supplied offline rules and label the exercise accurately.
- D. Assume the game implements every real control.

<details>
<summary>Answers and explanations</summary>

1. **B.** B applies the application condition. A confuses network reachability with authorization. C invents a logging function. D assigns intent without evidence.

2. **C.** C identifies the missing control. A and B assume functionality not stated. D contradicts the conditions.

3. **A.** A applies all policy conditions. B ignores expiry. C discards another stated condition. D is unrelated.

4. **D.** D follows the stated policy. A treats one condition as sufficient. B and C confuse a record with elimination of exposure.

5. **B.** B follows the supplied process. A and C bypass it. D overstates monitoring.

6. **C.** C preserves the evidence boundary. A, B, and D claim functionality or results not established.

</details>

Review guesses as well as errors. Explain the deciding condition and then change one condition in the scenario. [Contents](../study/contents.md).
