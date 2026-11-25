# Exercise 37: trace the layers protecting a record

[Control guide](../../study-guides/security-controls.md) · [Contents](../../study/contents.md)

Offline fictional exercise. Partial SY0-701 2.5. Ready to try.

## Conditions

A fictional records service has three controls:
- A network rule permits requests only from the staff zone.
- The application permits records only to the records-reader role.
- Audit logging records permitted and denied requests.

Assume these controls work exactly as stated. A staff-zone account without records-reader requests a record.

Draw the request path. Which control permits the network path? Which denies the record? Does logging itself deny access?

<details>
<summary>Worked answer</summary>

The network rule permits the staff-zone path. The application denies the record because the account lacks the required role. Logging records the decision; it is not the denying control in this scenario.

The controls address different parts of the request. Passing the network check does not satisfy application authorization.

</details>

## Change one condition

The application authorization check is disabled by mistake. The network and logging controls remain unchanged. Can the same account now obtain the record under the exercise's assumptions?

<details>
<summary>Changed answer</summary>

Yes: the staff-zone path remains permitted and the stated application restriction is gone. Logging may preserve evidence, but does not replace the removed authorization check. The remaining controls do not automatically meet the original access requirement.

</details>

Now move the request source outside the staff zone. The network rule blocks that path under the stated conditions. Explain why the effect of losing one control depends on which threat path you consider.

[NIST defense-in-depth glossary](https://csrc.nist.gov/glossary/term/defense_in_depth) describes a strategy using multiple layers. The conditions and conclusions here are original examples; a count of controls alone does not prove sufficient protection.

[Review questions](../../practice-tests/layers-and-exceptions-21.md) · [Cards](../../anki/layers-and-exceptions.txt).
