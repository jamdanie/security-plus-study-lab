# Concept review 10: eight close distinctions

Eight original single-answer questions covering the new concept pages. Partial SY0-701 coverage only. This is targeted practice, not a weighted full mock exam. Choose an answer and explain the requirement before opening the key.

## Question 1

A sign-in uses a password and a PIN. Which conclusion is supported?

A. Two prompts guarantee MFA
B. Both prompts use knowledge factors
C. A biometric factor is present
D. A possession factor is necessarily present

## Question 2

Two accounts use the same password but different salts. What is the purpose of that salt difference?

A. Prevent every online guess
B. Keep the salt permanently secret
C. Reduce identical stored results and reuse of precomputed tables
D. Recover the password through decryption

## Question 3

A user signs in through a trusted identity provider but cannot open payroll. What should be checked next for the stated permission issue?

A. The application's authorization rules
B. Whether every user shares a password
C. Whether the page is compressed
D. The number of identity-provider logos

## Question 4

A server certificate is within its validity dates but names a different hostname. What is the best conclusion?

A. Dates resolve all validation requirements
B. The application must be malicious
C. The client should always ignore the mismatch
D. The hostname mismatch needs investigation; valid dates alone do not resolve it

## Question 5

A report travels over a protected connection and is then placed in a publicly shared folder. Which exposure needs attention?

A. Only the old connection's cipher length
B. The destination's sharing permissions
C. Only the sender's filename
D. No exposure exists after encrypted transfer

## Question 6

A search parameter changes the structure of an unsafe database query. Which development correction most directly addresses that mechanism?

A. Only browser output encoding
B. Changing the network name
C. Parameterized queries separating data from query structure
D. Increasing the password length

## Question 7

A query shows five recent Application events. What can this sample establish?

A. A limited view of records in that selected log
B. That the entire device is uncompromised
C. That no older events exist
D. That all PowerShell commands were captured

## Question 8

A departing employee used a personally owned phone with managed work data. What should be checked before removing data?

A. Assume full wipe is always required
B. Assume personal ownership prevents every work-data action
C. Delete the organization's policy
D. Approved authority, enrollment capabilities, and work-data removal options

## Answer key

<details>
<summary>Open after answering</summary>

### 1: B

A PIN is a personal identification number. Password and PIN are knowledge factors; prompt count alone does not establish multifactor authentication (MFA). A, C, and D claim a factor distinction not stated.

[Review](../concepts/multifactor-authentication.md).

### 2: C

Unique salts distinguish derivations and limit precomputation reuse. A overclaims prevention, B misstates the salt's role, and D confuses hashing with reversible encryption.

[Review](../concepts/password-storage.md).

### 3: A

Trusted identity information does not grant every resource permission. B does not establish appropriate access; C and D are unrelated to the permission decision.

[Review](../concepts/single-sign-on.md).

### 4: D

Trust validation has multiple checks. A omits identity matching, B infers malicious intent without evidence, and C bypasses a relevant validation failure.

[Review](../concepts/certificate-trust.md).

### 5: B

The recipient's sharing configuration affects access to the stored copy. A and C do not restrict readers; D assumes transport protection controls later handling.

[Review](../concepts/data-states.md).

### 6: C

Parameterization addresses SQL (Structured Query Language) query construction. A is relevant to browser output contexts; B and D do not correct this query boundary.

[Review](../concepts/web-attack-distinctions.md).

### 7: A

The scope is limited by selected log and sample size. B, C, and D exceed that scope. A successful read does not establish comprehensive logging.

[Review](../concepts/powershell-log-review.md).

### 8: D

D checks scope and supported action. A assumes authority and impact, B ignores possible managed containers, and C removes the governing reference.

[Review](../concepts/mobile-deployment.md).

</details>

Score one point per item. Also mark correct guesses. A topic has only one item here, so this result cannot establish mastery. Review the concept, then explain a different example without the answer key.
