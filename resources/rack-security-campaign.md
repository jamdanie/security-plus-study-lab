# Mini campaign: prepare a fictional rack for service

[Contents](../study/contents.md) · [Game choices](steam-data-center-games.md)

Use this sequence as a visual study session. The rack, policies, and findings are fictional. It works on paper; no paid game is required.

## Choose a mission

| Mission | Activity | Evidence to keep |
|---|---|---|
| Know the equipment | [Rack reconciliation](../labs/22-rack-inventory/README.md) | Identity, owner, and location questions |
| Limit access | [Temporary grants](../labs/31-temporary-access/README.md) | Scope, approval, expiry |
| Prepare the configuration | [Server hardening](../labs/34-server-hardening/README.md) | Requirement, observed value, proposed check |
| Validate maintenance | [Patch review](../labs/35-patch-validation/README.md) | Installed versus running version and follow-up |
| Observe the service | [Alert tradeoffs](../labs/36-alert-tradeoffs/README.md) | Detected, missed, and benign-alert counts |
| Check recovery | [Recovery validation](../labs/27-recovery-validation/README.md) | Data point and validated service time |

Complete one mission per session or work through them in order. These are related study tasks, not one integrated software simulation.

## Use a game if it helps

Build or inspect a small layout in a simulator you already own. Draw the equipment and dependencies it actually models. For permissions, patch versions, or alert rules the game does not implement, use the supplied offline evidence.

Label a proposed test as proposed. Record actual gameplay separately from hypothetical policy decisions.

## Review the result

Try [Rack readiness 20](../practice-tests/rack-readiness-20.md), then [three cards](../anki/rack-readiness.txt). Explain the control requirement and why the closest alternative fails.

A successful campaign means you have completed and reviewed these learning tasks. It does not certify a real rack as secure or establish full Security+ readiness.
