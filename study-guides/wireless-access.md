# Wireless access: connecting is not the same as being authorized

Start with the requirement: who needs access, how will their identity be checked, and what may they reach after connecting?

SSID means Service Set Identifier: the network name presented to users. A familiar name does not prove that an access point belongs to the organization. An evil twin imitates a legitimate wireless network to attract connections.

## Enterprise authentication roles

In a typical 802.1X deployment:

| Role | Function |
|---|---|
| Supplicant | The connecting device's authentication software |
| Authenticator | The access point or switch controlling network access |
| Authentication server | Evaluates authentication through the configured method and policy |

RADIUS means Remote Authentication Dial-In User Service. An access point can be a RADIUS client when it communicates with the authentication server. The word client here refers to the access point's role in that exchange, not necessarily the user's laptop.

EAP means Extensible Authentication Protocol, a framework supporting authentication methods. EAP-TLS uses Transport Layer Security and certificates. Certificate-based designs need trustworthy server validation, protected private keys, and managed certificate lifecycle processes. Do not train users to ignore certificate warnings.

## Worked decision

A business needs individually revocable employee wireless access. A shared password is being passed between staff.

A correctly designed enterprise authentication system can support individual identities. Changing only the SSID does not address individual revocation. Choosing a strong wireless encryption setting also does not by itself establish that access is individually managed.

After authentication, enforce the appropriate network policy. A guest can connect successfully while being denied access to an internal application. That denial may be the intended authorization boundary rather than a wireless failure.

## Ready to move on?

Name the three authentication roles and explain why a RADIUS client can be an access point. Then distinguish a failure to authenticate from a blocked application connection.

Try the [wireless decision exercise](../labs/14-wireless-access/README.md) and [practice questions](../practice-tests/wireless-09.md).

Objective connection: partial SY0-701 4.1 and 3.2. This introduction does not cover every wireless protocol or deployment requirement.

## Separate admission from application access

Successful wireless authentication can coexist with a denied application request. Verify the intended access policy before treating isolation as a wireless outage. A familiar network name alone does not prove the access point is authorized.

### Try it without the answer

A guest reaches approved internet services but payroll is denied as required. Must the wireless password be wrong?

<details>
<summary>Explanation</summary>

No. The stated results fit successful admission followed by an enforced authorization boundary.

</details>


## Sources

- [Microsoft: Plan NPS as a RADIUS server](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-plan-server).
- [Microsoft: Configure RADIUS clients](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-radius-clients-configure).
- [Microsoft: Troubleshoot 802.1X authentication](https://learn.microsoft.com/en-us/troubleshoot/windows-client/networking/802-1x-authentication-issues-troubleshooting).

NPS means Network Policy Server. Examples are original and fictional; no live wireless changes are required.
