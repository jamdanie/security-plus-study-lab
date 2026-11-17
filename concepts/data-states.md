# Data states: protect the copy that is exposed

A document can move through several states during one task.

| State | Fictional example | Relevant question |
|---|---|---|
| At rest | Saved on a laptop | Who can read the stored copy? |
| In transit | Sent to a server | Is the connection appropriately protected? |
| In use | Opened and processed by an application | Who can access the active data and process? |

Disk encryption can protect a powered-off device's stored data without preventing an authorized session from reading it. Transport encryption protects a connection without controlling a recipient's later sharing decisions.

Worked example: an employee securely downloads a report, then puts it in a publicly shared folder. The protected transfer does not resolve the new access exposure.

Start with the data, its state, and the access requirement. Classification should guide handling, but a label alone does not enforce it.

Check yourself: name two different controls for two different exposure points in the report's journey. Avoid assuming one encryption setting protects every copy everywhere.

## Exam connection and review

Partial SY0-701 3.3 alignment. This short page does not complete the objective. [Review questions](../practice-tests/concept-review-10.md) · [Study index](../study/README.md).

## Source

[Primary documentation](https://csrc.nist.gov/glossary/term/data_loss_prevention). Examples are original and fictional.
