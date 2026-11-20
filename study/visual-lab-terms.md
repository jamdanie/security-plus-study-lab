# What a visual result actually tells you

[Contents](contents.md) · [Missions](../resources/hands-on-missions.md)

Use this reference when a simulation looks successful but you are unsure what it demonstrates.

| Observation | Supported conclusion | Still needs evidence |
|---|---|---|
| Two drawn paths reach one server | There are two paths in the drawing | Whether the server, power, or routing remains a shared failure |
| A link indicator is ready | The tool reports that link state | Required application functions and authorization |
| TCP 443 appears | The observed flow uses that destination port | Whether policy permits the destination and content is trustworthy |
| A restore job finishes | The job reports completion | Required service validation and recovery objectives |
| A failed check is followed by a passed check | The observations have that order and interval | Exact outage boundaries and root cause |
| A device has an inventory row | A record exists | Identity, location, ownership, and disposition accuracy |

## Work through one distinction

A fictional restore finishes at 11:15, but required application checks pass at 12:10. If the requirement measures validated service, use 12:10 as the endpoint. Choosing the earlier timestamp answers a different question.

Similarly, a game may show traffic moving through two switches. Draw the downstream service dependencies before saying the whole service tolerates a device failure.

## Use precise verbs

Write “the sample records a passed check” when that is your evidence. Write “I verified service restoration” only after actually performing the required checks. Record uncertainty as a next verification, not an invented result.

Try the [recovery validation](../labs/27-recovery-validation/README.md), [timeline review](../labs/26-event-timeline/README.md), or [service dependency](../labs/24-service-dependencies/README.md) exercise. Their original fictional conditions define what each answer establishes.
