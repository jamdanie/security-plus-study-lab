# Secure baselines: know what the settings should be

A baseline configuration is an approved, documented reference for a system. A security-focused baseline records settings that support the system's security requirements.

Without a reference, "this setting changed" tells you less than "this setting changed from the approved configuration."

## Distinguish the terms

| Term | Meaning in this guide |
|---|---|
| Baseline | The reviewed configuration used as the reference |
| Hardening | Reducing unnecessary exposure through configuration and other protective measures |
| Configuration drift | Observed settings moving away from the reference |
| Change control | Reviewing, approving, testing, and documenting changes |
| Exception | A documented, approved departure with a reason and review conditions |

Drift is a finding to investigate. It does not automatically prove an attack. A technician, software update, emergency repair, or attacker could cause a change. Check evidence before deciding why it happened.

## What a useful baseline records

Specify the device role, software version, setting, approved value, and how to verify it. Record the baseline version and approval information so later comparisons use the right reference.

A shared workstation and an application server may need different settings. A checklist that ignores the device's role can interrupt required services.

## Respond to a difference

Confirm the observation, compare it with the correct baseline version, and check approved changes and exceptions. Assess impact before restoring settings. Test the correction and record the result.

Do not edit the reference merely to make a failed comparison pass. If the reference needs to change, use the review process.

Try the [configuration-drift exercise](../labs/07-configuration-drift/README.md).

## Sources

- [NIST: Baseline configuration](https://csrc.nist.gov/glossary/term/baseline_configuration).
- [NIST: Common secure configuration](https://csrc.nist.gov/glossary/term/common_secure_configuration).
- [NIST: Configuration settings](https://csrc.nist.gov/glossary/term/configuration_settings).

These notes are original supporting material. The exercise values are fictional, not a universal hardening standard.
