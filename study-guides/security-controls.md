# Security controls: how it works versus what it does

Ask two questions: "How is the protection implemented?" and "What purpose does it serve?" Those are different classifications.

## Implementation categories

| Category | Study meaning | Fictional example |
|---|---|---|
| Technical | Enforced through system mechanisms | Software denies access without the required permission |
| Managerial | Direction and oversight | Management approves an access-review policy |
| Operational | People carry out a security process | Staff follow a verification checklist during account recovery |
| Physical | Protects physical access or assets | A locked equipment cage |

A control can involve several mechanisms. Classify the component described in the question rather than every part of a whole program.

## Purposes

| Type | What it is intended to do | Example in the stated role |
|---|---|---|
| Preventive | Stop an unwanted action | A rule blocks an unapproved connection |
| Detective | Identify activity or a condition | An alert reports an attempted connection |
| Corrective | Address a problem after it occurs | A recovery process restores a damaged configuration |
| Deterrent | Discourage an action | A warning notice discourages unauthorized entry |
| Directive | State required behavior | A policy requires approval before granting access |
| Compensating | Provide an approved alternative with comparable protection | An assessed alternative addresses a requirement the normal control cannot meet |

A compensating control is not merely any extra protection or any temporary workaround. It must be evaluated against the intended protection and applicable approval requirements.

## Worked decision

A monitoring system reports repeated failed logins. The component described is technical because software performs it, and detective because its stated function is to identify activity.

Now add an automated rule that blocks the next attempt. That blocking component has a preventive function. Do not assume "monitoring product" means every action it performs has the same purpose.

A visible camera may discourage entry and record evidence. If the question asks about reviewing its recordings, focus on the detective use. If it asks about discouraging entry, focus on deterrence. Some prompts need more context; the device name alone may not settle the purpose.

## Ready to move on?

Classify an access-denial rule by both implementation and purpose. Then explain why an alert does not necessarily block an action.

Try the [control-selection exercise](../labs/12-control-selection/README.md) and [practice questions](../practice-tests/controls-07.md).

Objective connection: partial SY0-701 1.1 coverage. [Exam map](../study/exam-alignment.md).

## Classify the component described

Ask separately how a control is implemented and what function is emphasized. An application may both alert and block, but those are distinct actions. Do not let the product name answer both questions.

### Try it without the answer

Software alerts an analyst but leaves the connection open. Which purpose is directly shown?

<details>
<summary>Explanation</summary>

Detection. The software implementation is technical, but the described alert does not itself prevent the connection.

</details>


## Sources

- [NIST: Technical controls](https://csrc.nist.gov/glossary/term/Technical_Controls).
- [NIST: Compensating controls](https://csrc.nist.gov/glossary/term/compensating_controls).
- [CompTIA SY0-701 objectives](https://assets.ctfassets.net/82ripq7fjls2/6TYWUym0Nudqa8nGEnegjG/0f9b974d3b1837fe85ab8e6553f4d623/CompTIA-Security-Plus-SY0-701-Exam-Objectives.pdf), objective 1.1.

Classifications here follow the stated function of each original example.
