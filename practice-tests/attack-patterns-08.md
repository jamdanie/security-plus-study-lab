# Attack patterns practice set 8

Four original single-answer questions. Partial SY0-701 2.4 alignment. Choose based on the stated mechanism and evidence. This is focused practice, not a complete exam simulation.

## Question 1

An ordinary account exploits a local service and gains administrative execution. No cache manipulation is observed. Which behavior is directly supported?

A. DNS cache poisoning
B. Privilege escalation
C. ARP cache poisoning
D. Credential replay

## Question 2

A local cache associates the gateway's IP address with an unauthorized device's MAC address. Which mechanism best matches?

A. ARP cache poisoning
B. Password spraying
C. Privilege escalation
D. File hashing

## Question 3

A familiar website reaches an unexpected destination. No resolver or host evidence is available. What is the strongest supported conclusion?

A. DNS poisoning is proven
B. Every user has administrator rights
C. The destination is unexpected; its cause needs investigation
D. Encryption is necessarily broken

## Question 4

ARP cache poisoning places an unauthorized device in the traffic path. Which additional claim requires separate evidence?

A. Local address mappings were manipulated
B. The device is positioned as an intermediary
C. The event warrants investigation
D. Properly validated encrypted application content was decrypted

## Explained answers

<details>
<summary>Open after answering</summary>

### 1: B

The evidence establishes higher permissions. A and C require specific cache manipulation; D requires reuse of captured authentication material. DNS means Domain Name System; ARP means Address Resolution Protocol.

### 2: A

ARP cache poisoning targets local IP-to-MAC mappings. B concerns password attempts across accounts, C concerns higher permissions, and D calculates a digest. IP means Internet Protocol; MAC means Media Access Control.

### 3: C

The observation does not establish a mechanism. A asserts a specific cause; B adds unrelated permission claims; D infers cryptographic failure without evidence.

### 4: D

An intermediary position does not itself establish decryption. The other choices follow the stated scenario. Encryption validation and key compromise would need separate analysis.

</details>

Review the [guide](../study-guides/attack-patterns.md) and [evidence exercise](../labs/13-attack-evidence/README.md). For each wrong answer or guess, identify which missing evidence would be needed to support the alternative.
