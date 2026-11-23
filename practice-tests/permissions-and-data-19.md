# Permissions and data 19

Six original questions. Partial SY0-701 4.6 (1–3), 3.4 (4–5), and 3.3 (6). This targeted set is not a weighted mock exam.

[Privilege guide](../study-guides/privilege-decisions.md) · [Session challenges](../resources/game-session-challenges.md) · [Contents](../study/contents.md)

## 1. A technician only needs to restart lab-web. Which grant best matches least privilege?

- A. Permanent administrator on all systems.
- B. Restart permission for lab-web within the approved window.
- C. All permissions because MFA passed.
- D. A shared administrator password.

## 2. Policy forbids self-approval. A scoped temporary grant is approved by its recipient. Which condition fails?

- A. Expiry must always be permanent.
- B. The service name is too short.
- C. Independent approval.
- D. The grant has no permissions.

## 3. A grant expires at 18:00 and expiry is enforced. At 18:05, what follows?

- A. It is no longer active.
- B. It remains active because it once had approval.
- C. It becomes a broader grant.
- D. MFA automatically renews it.

## 4. A compromised production account can delete two connected backup copies. What does having two copies alone establish?

- A. Both are immune.
- B. Recovery is proven.
- C. Encryption must be absent.
- D. There are two copies, but both share the stated deletion exposure.

## 5. A disconnected copy has no restore test recorded. What is the defensible conclusion?

- A. It is guaranteed recoverable.
- B. It avoids the stated account's access while disconnected, but restore evidence is missing.
- C. It has already restored every application.
- D. It must be corrupted.

## 6. Policy prohibits Restricted data in public repositories. Renaming a Restricted export notes.txt permits what?

- A. Public upload automatically.
- B. Classification removal.
- C. No change to its handling requirement.
- D. Any recipient to approve it.

<details>
<summary>Answers and explanations</summary>

1. **B.** B matches the task and time. A exceeds scope and duration. C confuses authentication with authorization. D shares a credential without establishing the needed scope or accountability.

2. **C.** C directly violates the stated rule. A invents a requirement. B is irrelevant. D contradicts the granted action.

3. **A.** A follows the time condition. B ignores expiry. C and D assume mechanisms not supplied.

4. **D.** D follows the scenario. A ignores reachability. B requires restore evidence. C cannot be inferred from permissions.

5. **B.** B separates exposure and recoverability. A and C claim untested success. D invents failure.

6. **C.** C follows the contents and policy. A and B assume renaming changes classification. D invents approval authority.

</details>

For each error or correct guess, state the requirement you missed. Try changing scope, review time, reachability, or destination and explain the new decision. Supporting reading is linked in the activities.
