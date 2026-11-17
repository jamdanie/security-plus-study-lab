# Requirement review 12

Six original single-answer questions. Identify the requested outcome before choosing. This set reviews existing material and is not a full weighted mock exam or a readiness predictor.

## Question 1

A public file needs verification of its signer, but must remain readable by anyone. Which requirement should guide the choice?

A. Conceal the entire file
B. Verify signed contents using a trusted key
C. Disable every reader's account
D. Reduce the file size

## Question 2

A user signs in successfully but an application denies an export. What should be evaluated for that denied action?

A. Only whether the password is long
B. Only the network display name
C. The resource's effective authorization rules
D. Only the file's hash

## Question 3

The latest usable data is too old, although service restoration is fast enough. Which objective was missed?

A. Recovery point objective
B. Recovery time objective
C. A certificate's validity period
D. The firewall's first-match order

## Question 4

An organization already requires approved access removal, but technicians need a consistent ordered checklist. Which document would most directly fill the gap?

A. Another broad policy stating the same obligation
B. An optional recommendation with no required workflow
C. A risk score by itself
D. A procedure describing actions and verification

## Question 5

A patch job reports success. The owner needs evidence that the finding is resolved. Which next step meets that need?

A. Close the finding based only on the job status
B. Perform suitable remediation checks and verify service functions
C. Remove the original report
D. Assume every related asset was patched

## Question 6

A monitoring component reports an attempt, but leaves the connection open. Which function is actually described?

A. Preventive blocking
B. Eradication of the cause
C. Detection of activity
D. Automatic recovery

## Explained answers

<details>
<summary>Open after answering</summary>

### 1: B

The stated need is signature verification, not secrecy. A conflicts with public readability; C removes intended access; D does not authenticate a signer.

[Review the relevant guide](../study-guides/cryptography-choices.md).

### 2: C

The denied resource action concerns permissions. A addresses one credential property; B is unrelated to application grants; D checks content rather than permission.

[Review the relevant guide](../study-guides/identity-and-access.md).

### 3: A

The recovery point objective concerns the usable data point. The recovery time objective concerns duration, which the prompt says is acceptable. C and D do not describe recovery objectives.

[Review the relevant guide](../study-guides/backup-and-recovery.md).

### 4: D

The missing item is an operational sequence. A repeats direction, B does not establish the required steps, and C estimates risk without supplying the workflow.

[Review the relevant guide](../study-guides/security-governance.md).

### 5: B

B checks both remediation and required operation. A treats installation status as full validation; C removes evidence; D extends the result to untested assets.

[Review the relevant guide](../study-guides/vulnerability-management.md).

### 6: C

The component detects activity. A assumes blocking, B assumes removal, and D assumes restoration; none of those actions is stated.

[Review the relevant guide](../study-guides/security-controls.md).

</details>

Record errors and correct guesses. For each, write the requested outcome and why the closest alternative fails. Use the [comparison reference](../study/quick-comparisons.md) and [review plan](../study/review-plan.md) for another pass.

[All tests](README.md) · [Contents](../study/contents.md)
