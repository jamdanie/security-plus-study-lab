# Risk management: explain the decision

A threat is a potential cause of harm. A vulnerability is a weakness that could be exploited. Risk considers the likelihood and consequences of a harmful event in context.

For example, an unsupported booking server is a weakness; an attacker exploiting it is a threat scenario. The risk depends on exposure, data, service importance, and existing protections.

## Choose a response

| Response | Fictional example |
|---|---|
| Mitigate | Restrict access and replace unsupported software |
| Avoid | Stop offering the activity that creates the risk |
| Transfer or share | Arrange contractual or insurance coverage for defined consequences |
| Accept | An authorized owner documents a decision to retain the risk |

Insurance does not remove a technical weakness or transfer every responsibility. Acceptance should identify an accountable owner and review conditions. Doing nothing accidentally is not the same as informed acceptance.

Residual risk remains after controls. Controls can reduce exposure without eliminating every possible loss.

## Quantitative practice

A simplified annual loss model uses:

- Single loss expectancy (SLE) = asset value × exposure factor.
- Annualized loss expectancy (ALE) = SLE × annualized rate of occurrence (ARO).

Exposure factor is the estimated fraction lost in one event. ARO is the estimated frequency per year.

For fictional values of $20,000, an exposure factor of 25%, and an ARO of 0.2, SLE is $5,000 and ALE is $1,000 per year. An ARO of 0.2 means an estimated average rate of one event per five years, not a prediction of its date.

These estimates support comparison; they do not capture every dependency or guarantee the actual loss. State assumptions and uncertainty.

## Practice

A control costs $600 annually and is estimated to reduce ALE from $1,000 to $300. Its estimated annual loss reduction is $700, or $100 above its annual cost in this simplified model. Business, safety, and contractual requirements can still matter beyond that comparison.

Try [practice set 2](../practice-tests/foundations-02.md).

## Source

[NIST: Risk response](https://csrc.nist.gov/glossary/term/risk_response). Numerical examples are fictional teaching calculations.
