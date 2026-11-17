# Wireless practice set 9

Four original single-answer questions, partially aligned to SY0-701 4.1 and 3.2. This is a focused introduction, not a complete wireless assessment or a full mock exam.

## Question 1

In a typical 802.1X wireless exchange, which component acts as the authenticator?

A. The user's password vault
B. The access point controlling access
C. The application's data owner
D. The certificate expiration date

## Question 2

An access point sends authentication requests to a RADIUS server. What is the access point in that exchange?

A. Always the end user's supplicant
B. The certificate authority by definition
C. A RADIUS client
D. The organization's risk owner

## Question 3

A guest authenticates and reaches the internet, but a rule denies access to an internal payroll server as intended. Which explanation fits?

A. Authentication succeeded; authorization restricts the requested path
B. Wireless authentication must have failed
C. A shared password must be exposed
D. The server certificate must be expired

## Question 4

A familiar SSID appears on an unknown access point. What can be concluded from the name alone?

A. It is definitely the authorized access point
B. All traffic is decrypted
C. The user has administrator rights
D. Ownership is not established and should be verified

## Explained answers

<details>
<summary>Open after answering</summary>

### 1: B

The access point controls admission. The supplicant runs on the connecting device; the authentication server evaluates the configured authentication. The other choices do not perform the stated role.

### 2: C

RADIUS means Remote Authentication Dial-In User Service. Its client can be an access point. A confuses roles; B assumes certificate issuance; D concerns business accountability.

### 3: A

The observed connection and intended policy support A. The denial alone establishes none of B, C, or D.

### 4: D

SSID means Service Set Identifier. Its name alone does not prove access-point ownership, decryption, or elevated permissions.

</details>

Review the [guide](../study-guides/wireless-access.md) and [exercise](../labs/14-wireless-access/README.md). Explain each authentication role without relying on the answer letters.
