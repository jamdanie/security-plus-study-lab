# Exercise 14: diagnose the right access layer

Status: ready to try. Fictional offline exercise.

A business uses enterprise wireless authentication and separates guests from internal systems. Employees have individually managed access.

| Case | Evidence |
|---|---|
| A | The device receives a server-certificate trust warning before authentication completes |
| B | A guest authenticates and reaches approved internet resources, but an internal server connection is denied by policy |
| C | A former employee's individual access must be revoked |
| D | An unknown access point broadcasts the same network name as the business |

For each case, choose the next verification and explain what the evidence does not prove.

<details>
<summary>Suggested analysis</summary>

A: Check trusted server identity, certificate validity, and client configuration through the approved process. Do not bypass the warning as a default fix. The warning alone does not prove an attacker.

B: Check the stated policy. The denial matches guest isolation in this scenario; it does not establish failed wireless authentication.

C: Revoke the individual's assigned access and check active sessions and certificate or account lifecycle requirements as applicable. Changing the network's display name does not revoke an identity.

D: Investigate the access point's authorization and identity. The matching name alone does not establish ownership or prove a successful evil-twin compromise.

</details>

Explain the difference between authenticating a connection and authorizing an application request. [Guide and sources](../../study-guides/wireless-access.md).
