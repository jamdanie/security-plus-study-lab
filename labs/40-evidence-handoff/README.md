# Exercise 40: write a useful incident handoff

[Timeline exercise](../26-event-timeline/README.md) · [Contents](../../study/contents.md)

Offline fictional exercise. Partial SY0-701 4.8 and 4.9. Ready to try.

## Supplied records

All times are UTC and clocks are assumed accurate.

| Time | Record |
|---|---|
| 10:00 | External service check failed |
| 10:02 | Internal application check passed |
| 10:04 | Network team opened provider case LAB-7 |
| 10:08 | External service check passed |
| 10:10 | Two users still reported errors |

A draft handoff says: “The attacker broke the router for exactly eight minutes. Everything is fixed.”

Replace it with facts, unresolved questions, and the next action. Use only the supplied evidence.

<details>
<summary>Example handoff</summary>

The external check failed at 10:00 and passed at 10:08. The internal application check passed at 10:02. Provider case LAB-7 was opened at 10:04. Two users still reported errors at 10:10.

The cause and exact outage boundaries remain unconfirmed. The next responder should review the provider case, investigate the remaining reports, and validate required functions from affected locations.

</details>

## Why it helps

The draft invents an attacker, a failed router, exact outage boundaries, and complete recovery. The records support none of those conclusions. Internal and external checks observe different conditions.

A useful handoff preserves source, time, status, and the unresolved decision. It gives the next person enough detail to continue investigating.

## Optional visual session

Pause a simulator after a supported failure. Record only observations it supplies. Ask a study partner to continue from your note without extra explanation. If a needed timestamp or cause is unavailable, say so.

Keep game observations separate from this fictional table. [Review questions](../../practice-tests/recovery-and-handoff-22.md) · [Learning notes](../../study/hands-on-notes.md).
