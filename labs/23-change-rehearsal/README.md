# Exercise 23: rehearse a change and a rollback

[Baselines](../../study-guides/secure-baselines.md) · [Learning missions](../../resources/hands-on-missions.md)

Offline fictional exercise; optional simulator use. Ready to try. Partial SY0-701 1.3.

## Change request

A fictional team wants to move a service connection from Switch A to Switch B during an approved window. Required checks are:
- Confirm the service is reachable before the move.
- Confirm the same required functions after the move.
- Return to the previous connection if the service fails its checks.

The proposal says: “Move the cable. If the link light turns green, close the ticket.”

## Your review

Explain what is missing. Write the order of checks, what would trigger rollback, and how you would verify the restored baseline.

<details>
<summary>Worked answer</summary>

Record the existing connection and baseline service checks before changing it. Confirm approval, affected users, dependencies, and responsibilities. Move the connection only within the authorized scope.

A link light is a physical/link indication; it does not establish that required application functions work. Run the agreed functional checks. If the required service fails and the rollback criterion is met, restore the known connection and verify service again.

Record the result and any unresolved issue. Don't close the ticket solely from the link indicator.

</details>

## Try it visually

Use a copy of a simulator project you control. Before changing a supported connection, predict the result and save the baseline. Perform and document the supported checks. A simulator may not model the real application's functions, so state that limit.

No live network change is part of this task. For a no-install activity, annotate the [resilience drawing](../19-visual-resilience/README.md).

[Review questions](../../practice-tests/operations-missions-16.md) · [Learning notes](../../study/hands-on-notes.md)
