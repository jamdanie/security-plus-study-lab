# Practice set 2: risk, vulnerabilities, and response

Nine original single-answer questions. This set covers only three introductory sections, not the full exam. Choose answers before opening the key. Score one point each; results are review prompts, not an exam-readiness prediction.

## Question 1

A control lowers estimated risk, but some exposure remains. What is the remaining risk called?

A. Residual risk
B. Risk avoidance
C. A guaranteed loss
D. A false positive

## Question 2

An authorized owner documents retaining a risk and sets a review date. Which response is this?

A. Eradication
B. Risk acceptance
C. Risk avoidance
D. File restoration

## Question 3

Asset value is $40,000, exposure factor is 10%, and ARO is 0.25. What is ALE?

A. $40,000
B. $4,000
C. $1,000 per year
D. $10,000 per year

## Question 4

Which fact most directly supports urgency beyond a severity score?

A. The asset has a short name
B. The report has many pages
C. The scanner theme is red
D. Exploitation is known and the affected production service is exposed

## Question 5

A scan reports a weakness that investigation confirms is absent. What is this?

A. False positive
B. False negative
C. Confirmed exploitation
D. Risk transfer

## Question 6

A patch installs successfully. What best supports closing the finding?

A. Delete the original report
B. Verify the weakness is addressed and required service functions still work
C. Assume all related systems are fixed
D. Disable future scanning

## Question 7

An authorized team isolates an affected workstation to limit spread. Which purpose is this?

A. Risk transfer
B. Backup scheduling
C. Containment
D. Final recovery validation

## Question 8

Which statement about evidence is accurate?

A. A hash replaces chain of custody
B. Rebuilding first always preserves all evidence
C. Only filenames matter
D. Hashes and documented evidence handling serve different purposes

## Question 9

A restored service works, but the exploited access path remains open. What follows?

A. Recovery should include validating the cause and required fixes
B. The incident must be closed
C. Backups prove data was never stolen
D. Lessons learned are unnecessary

## Answer key

<details>
<summary>Open after answering</summary>

### 1: A

Residual risk remains after controls. Avoidance stops the risk-generating activity; an estimate is not a guaranteed loss; a false positive is an incorrect finding.

[Review this section](../study-guides/risk-management.md).

### 2: B

Acceptance is an informed decision to retain risk. Eradication removes incident causes, avoidance stops an activity, and restoration recovers data.

[Review this section](../study-guides/risk-management.md).

### 3: C

SLE is $40,000 × 0.10 = $4,000. ALE is $4,000 × 0.25 = $1,000 per year. ARO means annualized rate of occurrence; SLE means single loss expectancy; ALE means annualized loss expectancy. The other values do not complete both operations correctly.

[Review this section](../study-guides/risk-management.md).

### 4: D

D adds exploitation, applicability, and exposure context. Naming, report length, and display colors do not establish risk.

[Review this section](../study-guides/vulnerability-management.md).

### 5: A

A false positive reports an absent problem. A false negative misses a present problem. A scan error does not establish exploitation or transfer risk.

[Review this section](../study-guides/vulnerability-management.md).

### 6: B

Verification checks remediation and operational impact. Installation alone does not establish either; deleting evidence, assuming broader coverage, or stopping checks does not validate the result.

[Review this section](../study-guides/vulnerability-management.md).

### 7: C

Containment limits harm or spread. Isolation alone does not transfer risk, schedule backups, or establish restored safe operations.

[Review this section](../study-guides/incident-response.md).

### 8: D

Hashes support checking collected bytes for changes. Chain of custody records handling and transfers. A is incomplete, B can destroy evidence, and C ignores content and handling.

[Review this section](../study-guides/incident-response.md).

### 9: A

Operational restoration alone does not address recurrence. B closes prematurely, C confuses recovery with confidentiality, and D removes an opportunity to correct response gaps.

[Review this section](../study-guides/incident-response.md).

</details>

Questions 1–3 cover risk, 4–6 vulnerability management, and 7–9 incident response. Review both wrong answers and guesses. Explain one new scenario in your own words after reading the linked guide.
