# Exercise 34: check a server before release

[Baseline guide](../../study-guides/secure-baselines.md) · [Settings](settings.csv) · [Campaign](../../resources/rack-security-campaign.md)

Offline fictional exercise. Partial SY0-701 4.1. Ready to try.

## Release policy

The CSV gives the approved requirements for one fictional lab server. Every requirement must match before release; no exceptions are approved. Compare each required and observed value.

Write the mismatch, proposed correction, and verification. Do not connect to or change a real server.

<details>
<summary>Worked review</summary>

| Setting | Result | Verification after an approved correction |
|---|---|---|
| Shared factory password | Mismatch | Confirm the shared factory credential no longer authenticates and the approved replacement method works |
| Remote administration source | Mismatch | Test permitted management access and blocked access from another zone |
| Unused demo service | Mismatch | Confirm the service is disabled and no longer reachable as applicable |
| Security logging | Matches | Generate an authorized test event and confirm the expected record |
| Approved time source | Mismatch | Confirm the configured source and check clock agreement |

A matching setting is configuration evidence. A functional check adds evidence that the intended behavior works. Do not record these proposed checks as completed tests.

</details>

## Connect the controls

Changing a credential does not restrict every network path. Restricting a path does not remove an unused service. Logging observes events but does not replace access enforcement.

CISA's [default-password alert](https://www.cisa.gov/sites/default/files/2023-12/SbD-Alert-How-Software-Manufacturers-Can-Protect-Customers-by-Eliminating-Default-Passwords-508c_0.pdf) explains why shared defaults create exposure. The CSV is an original policy example, not a universal baseline.

If a simulator supports a setting, test it in a copy of your project. Otherwise keep the activity as an offline review. [Questions](../../practice-tests/rack-readiness-20.md).
