# Applied review 4: choose between plausible controls

Six original, single-answer questions. Read the requirement and constraints before choosing. These are not copied or reconstructed exam questions. Objective mappings are author-assigned and partial. This targeted set is not weighted like the complete exam.

## Question 1

A public software update must be readable by anyone, but readers need to verify its publisher and signed contents. Which option best meets that requirement?

A. Encrypt the update with a shared password
B. Publish a digital signature and provide a trusted way to obtain the publisher's verification key
C. Publish an unsigned hash on the same untrusted mirror
D. Store the update on two mirrors

## Question 2

A recipient verifies a signature with a key attached to an unsolicited message. What additional check is needed before attributing the document to the expected sender?

A. Whether the document is compressed
B. Whether the filename matches the sender's name
C. Whether the key is reliably bound to that sender
D. Whether a second identical copy arrives

## Question 3

An employee moves to scheduling. The old billing group still grants export access. Which action best corrects the permission problem while keeping required scheduling access?

A. Reset the password and retain all groups
B. Remove only the displayed billing job title
C. Disable the employee's entire account indefinitely
D. Remove unnecessary billing grants and verify effective scheduling permissions

## Question 4

A receptionist signs in successfully and receives access denied when opening payroll. Which explanation is supported?

A. Authentication succeeded but authorization did not permit that action
B. Authentication failed because payroll denied access
C. The account must be compromised
D. A password reset will necessarily grant payroll access

## Question 5

Only staff should initiate TCP 443 connections to a server. In a first-match rule set, rule 1 permits any source to that service and rule 2 denies guests to the server. Which single change most directly enforces the requirement, with a final deny already present?

A. Move the guest deny above rule 1 while keeping the broad permit
B. Narrow rule 1's source to staff
C. Add another guest deny below rule 2
D. Replace the final deny with a permit

## Question 6

Two VLANs already exist and routing permits broad communication. Staff need one server service; guests need no server access. What best addresses the stated gap?

A. Renumber both VLANs
B. Require a longer wireless password without changing routed policy
C. Enforce a narrow staff-to-service allow rule and deny unapproved paths
D. Add a second physical link with the same unrestricted policy

## Explanations

<details>
<summary>Open after answering</summary>

### 1: B · objective 1.4

The requested properties are origin verification and integrity, not secrecy. A restricts reading without establishing the signer. C lacks an independent trust basis. D improves distribution but does not authenticate the publisher.

[Review the worked example](../study-guides/cryptography-choices.md).

### 2: C · objective 1.4

A valid signature establishes a relationship to a key. Trustworthy identity binding is still needed. Compression, filenames, and repeated delivery do not establish key ownership.

[Review the worked example](../study-guides/cryptography-choices.md).

### 3: D · objective 4.6

D addresses actual authorization. A changes a credential, B changes a label, and C prevents the approved work. Check inherited and direct grants.

[Review the worked example](../study-guides/identity-and-access.md).

### 4: A · objective 1.2

A separates the identity check from the permission decision. B confuses the checks, C infers compromise without evidence, and D does not follow from a credential change.

[Review the worked example](../study-guides/identity-and-access.md).

### 5: B · objective 4.5

Narrowing the permit enforces staff-only access. A blocks guests but allows other nonstaff sources. C is shadowed for the same request. D opens unrelated traffic. TCP means Transmission Control Protocol.

[Review the worked example](../study-guides/network-segmentation.md).

### 6: C · objective 2.5

C enforces the requested communication boundary. A changes identifiers, B may protect wireless access but leaves this routed gap, and D adds connectivity without restricting it. VLAN means virtual local area network.

[Review the worked example](../study-guides/network-segmentation.md).

</details>

Record the requirement you missed, not only the answer letter. Revisit a wrong answer or correct guess, close the explanation, and explain a changed scenario. Retaking identical questions can reward answer memory; use the exercises to check transfer.
