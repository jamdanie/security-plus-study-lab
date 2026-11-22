# Exercise 30: respond to an availability incident

[Contents](../../study/contents.md) · [Incident response guide](../../study-guides/incident-response.md)

Original discussion-based exercise. Partial SY0-701 4.8. Ready to try. It does not run a live outage.

## Roles and opening condition

Work alone by writing each role's decision, or ask willing study partners to take the service owner, technical responder, and communications roles. The owner sets business priorities; the responder investigates and coordinates technical actions; communications tracks approved updates.

A fictional public service becomes unavailable. You have no confirmed cause.

## Reveal one update at a time

1. Monitoring shows the internet connection is saturated. Internal application health checks still pass.
2. The network provider reports abnormal inbound traffic and offers its agreed mitigation process.
3. After provider mitigation, external checks pass, but some users still report errors.
4. A post-incident review finds that the escalation contact list was outdated.

At each update, record what is known, the next action, the responsible role, and what would verify progress.

<details>
<summary>Example reasoning</summary>

1. Investigate network evidence and engage the appropriate response path. Passing internal checks does not establish external availability or prove the cause.
2. Coordinate the provider process under the response plan. Record the change and its effect.
3. Validate required functions from relevant locations and investigate remaining reports. Do not declare full recovery solely from one passed check.
4. Assign an owner to correct and test the escalation information. Record the follow-up action.

These are example decisions, not a universal response script.

</details>

## Debrief

Identify one missing piece of evidence and one process improvement. A tabletop can reveal decision and coordination gaps; it does not measure actual failover or restore performance.

For an optional game session, pause at a supported failure and discuss roles before continuing. Do not claim the game implements provider mitigation.

[Free exercise resources](../../resources/tabletop-learning.md) · [Review questions](../../practice-tests/availability-and-access-18.md)
