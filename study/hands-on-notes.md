# Turn a hands-on session into something useful

[Visual resources](../resources/visual-and-gamified-learning.md) · [Contents](contents.md)

A useful note lets you explain the result after the game or lab is closed. Record what you actually did. Keep plans separate from completed work.

## What to record

| Item | What belongs there |
|---|---|
| Question | The concept or requirement you wanted to test |
| Environment | Product, version if known, and relevant setup |
| Prediction | What you expected before the change |
| Action | The specific change or command |
| Observation | What the tool actually displayed |
| Explanation | Why the result follows from the setup |
| Limit | What this activity did not establish |
| Next check | A different condition worth testing |

A screenshot helps when its caption says what to inspect. Remove account details, tokens, passwords, and unrelated personal information before sharing. Follow platform rules about publishing challenge solutions.

## Worked example: fictional, not a completed project result

Question: Would two switches keep a service available after any single device failure?

Setup: The [offline resilience drawing](../labs/19-visual-resilience/README.md) has two switches but one service server.

Prediction: Either switch can fail without removing every drawn path. A server failure still removes the service.

Action: Trace the paths after crossing out one component at a time.

Observation: Removing the server leaves neither path with a working service endpoint.

Explanation: Redundant network paths and redundant service instances solve different dependencies.

Limit: This drawing does not test routing, power independence, data replication, or failover timing.

Next check: Add a second service instance and identify the configuration and testing needed to use it.

## For your portfolio

Write a short explanation of a decision and support it with your own evidence. A description such as “identified a shared server dependency in an offline topology” is defensible when that is what you did. Claim live failover testing only after actually performing it.

For an error, record what you changed after discovering it and how you checked the correction. That makes the note useful to another learner.

## Bring it back to Security+

Link the related guide and explain the distinction in one sentence without answer choices. Then attempt a changed scenario. The [domain routes](domain-routes.md) help you return to reading and review; the [exam map](exam-alignment.md) labels coverage as partial.
