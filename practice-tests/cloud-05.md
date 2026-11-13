# Cloud practice set 5

Four original single-answer questions, aligned partially to SY0-701 3.1. This focused set is not a full mock exam. Select an answer and explain the responsibility boundary before opening the key.

## Question 1

A service agreement assigns guest operating-system patches to the customer. The provider maintains the physical host. Who should coordinate a missing guest patch?

A. The provider's facilities team because the system is hosted
B. The customer workload owner through the approved change process
C. Neither party until the physical host fails
D. Only the software users through password changes

## Question 2

A managed document application encrypts storage, but a tenant setting permits public links to sensitive files. Which action most directly addresses the exposure?

A. Increase the encryption key length only
B. Move the application to another region without changing sharing
C. Restrict sharing to approved recipients and verify effective access
D. Assume provider encryption prevents unauthorized readers

## Question 3

A provider-managed platform takes responsibility for operating-system updates. What should the customer conclude?

A. All application and data-access responsibilities have disappeared
B. The customer must still review the settings and code it controls
C. No contract review is necessary
D. Public sharing is safe because patching is managed

## Question 4

Which evidence best helps determine responsibility for a cloud security task?

A. The marketing phrase 'fully managed' alone
B. A different provider's unrelated service table
C. The applicable service agreement and responsibility matrix, checked against the configured service
D. The number of users in the account

## Answers

<details>
<summary>Open after answering</summary>

### 1: B

The scenario explicitly assigns that layer to the customer. A confuses guest and host responsibilities; C defers a known duty; D changes credentials rather than patching.

### 2: C

C addresses who can read the documents through the application. A does not remove broad authorization; B leaves the permission issue; D assumes encryption overrides allowed access.

### 3: B

The management boundary changes for the stated layer. A overextends that change; C ignores service-specific terms; D confuses patching with authorization.

### 4: C

C establishes the applicable boundary. A is too broad, B may describe different duties, and D does not assign layer ownership.

</details>

Review the [cloud guide](../study-guides/cloud-responsibility.md) and [exercise](../labs/10-cloud-responsibility/README.md). Check correct guesses as well as errors. Four questions cannot establish complete domain mastery.
