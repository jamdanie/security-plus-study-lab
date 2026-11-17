# Attack patterns: describe what changed

Start with the observed behavior. A scenario can involve several attacks, but the question may ask about only one step.

## Distinguish the mechanisms

| Pattern | Main distinction | Evidence to look for |
|---|---|---|
| Privilege escalation | Obtaining higher-level permissions | An unauthorized account or process gains administrative capability |
| ARP cache poisoning | Corrupting local address mappings | A gateway's network address is associated with an attacker's hardware address |
| DNS cache poisoning | Corrupting cached name-resolution information | A trusted name is resolved using a forged cached entry |
| On-path attack | Attacker is positioned in a communication path | Traffic passes through an unauthorized intermediary |
| Credential replay | Reusing captured authentication material | Previously obtained credentials or exchanges are reused |

ARP means Address Resolution Protocol. DNS means Domain Name System. IP means Internet Protocol. MAC means Media Access Control in the networking address context.

Poisoning describes corruption of information a system relies on. Privilege escalation describes a gain in permissions. Poisoning can help an attacker perform a later action, but gaining privilege alone is not evidence that a cache was poisoned.

## Worked example

A workstation's local cache maps the default gateway's IP address to an unauthorized device's MAC address. Traffic is redirected through that device.

The changed local IP-to-MAC association supports investigating ARP cache poisoning. The intermediary position is consistent with an on-path attack. No evidence yet establishes that the workstation's user became an administrator.

Now change the evidence: the cache is unchanged, but exploitation of a local service lets an ordinary account run administrative commands. Privilege escalation fits that observed permission change.

## Do not classify by impact alone

A wrong destination could result from a hosts-file change, a bad configuration, a forged DNS response, or another cause. You need evidence about the mechanism before naming a specific poisoning attack.

Similarly, failed sign-ins do not prove which passwords were attempted. State uncertainty when the records are incomplete.

## Ready to move on?

Explain why ARP poisoning and an on-path position can describe different aspects of one incident. Then state what evidence would support a privilege-escalation finding.

Try the [evidence exercise](../labs/13-attack-evidence/README.md) and [practice questions](../practice-tests/attack-patterns-08.md).

Objective connection: partial SY0-701 2.4. This does not cover every malicious indicator in that objective.

## Check the mechanism before the label

An unexpected destination is an observation. A corrupted cache entry is evidence about a mechanism. Higher administrative capability is evidence about permissions. Keep those claims separate in your answer.

### Try it without the answer

A browser reaches the wrong server, but the local address cache is unchanged. Does that prove privilege escalation?

<details>
<summary>Explanation</summary>

No. Neither an unexpected destination nor an unchanged cache establishes a gain in permissions. Gather evidence about resolution, configuration, and account activity.

</details>


## Sources

- [MITRE ATT&CK: Privilege Escalation](https://attack.mitre.org/tactics/TA0004/).
- [MITRE ATT&CK: Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/).
- [MITRE ATT&CK: ARP Cache Poisoning](https://attack.mitre.org/techniques/T1557/002/).

Examples are fictional and original. No attack commands or live targets are involved.
