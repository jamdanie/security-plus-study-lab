# Exercise 13: name the mechanism without inventing evidence

Status: ready to try. Fictional offline exercise.

Review each case separately. Identify the supported mechanism and one conclusion the evidence does not establish.

| Case | Evidence |
|---|---|
| A | A gateway IP-to-MAC cache entry changes to an unauthorized device's MAC address |
| B | An ordinary account exploits a local service and gains administrator-level execution |
| C | A website opens at an unexpected destination, but no cache, resolver, or host evidence has been collected |

IP means Internet Protocol. MAC means Media Access Control.

<details>
<summary>Suggested analysis</summary>

A supports investigating Address Resolution Protocol (ARP) cache poisoning. The entry alone does not establish administrative execution or that encrypted application content was readable.

B supports privilege escalation. It does not establish that any name-resolution or address cache was corrupted.

C identifies an unexpected destination but does not settle the cause. Check relevant host, resolver, and network evidence before concluding that Domain Name System (DNS) cache poisoning occurred.

</details>

## Change the scenario

Case A also includes evidence that traffic traversed the unauthorized device. Explain how poisoning describes a mechanism while an on-path position describes the resulting placement. Do not assume this automatically bypasses properly validated encryption.

Write one additional evidence request for each case. Keep your observations separate from your hypotheses.

[Guide and sources](../../study-guides/attack-patterns.md).
