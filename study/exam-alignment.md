# SY0-701: exam weights and guide connections

Mapping reference: CompTIA Security+ SY0-701 objectives, version 5.0. Confirm that SY0-701 matches your registration before using this plan. This does not establish availability or retirement dates.

[Official objectives PDF](https://assets.ctfassets.net/82ripq7fjls2/6TYWUym0Nudqa8nGEnegjG/0f9b974d3b1837fe85ab8e6553f4d623/CompTIA-Security-Plus-SY0-701-Exam-Objectives.pdf). The percentages below are CompTIA's domain weights. Connections, coverage judgments, time allocations, and practice tasks below are this project's study design, not CompTIA endorsements.

## Domain weights

| Domain | Examination weight | Example allocation across 10 study hours |
|---|---|---|
| 1. General Security Concepts | 12% | 72 minutes |
| 2. Threats, Vulnerabilities, and Mitigations | 22% | 132 minutes |
| 3. Security Architecture | 18% | 108 minutes |
| 4. Security Operations | 28% | 168 minutes |
| 5. Security Program Management and Oversight | 20% | 120 minutes |

These are starting allocations, not a rule to stop reviewing a weak topic. Domain percentages do not specify the weight of an individual objective, the number of questions about it, or the points for a particular question. Do not multiply a practice percentage into an official scaled score.

## What the current material prepares you to do

Every row is partial coverage. Reading a linked page does not complete its entire objective.

| Official objective IDs | Material | Observable practice skill |
|---|---|---|
| 1.2, 1.4 | [Cryptography](../study-guides/cryptography-choices.md) | Select a mechanism for a stated need and explain why a plausible alternative fails |
| 1.2, 4.6 | [Identity and access](../study-guides/identity-and-access.md) | Remove grants that no longer match a person's work |
| 1.3, 4.1 | [Baselines](../study-guides/secure-baselines.md) | Check a changed setting against an approval and an exception |
| 2.2, 5.6 | [Phishing](../study-guides/phishing.md) | Pick an independent verification and reporting path |
| 2.5, 3.2, 4.5 | [Segmentation](../study-guides/network-segmentation.md) | Trace a new connection through rules and correct the first bad match |
| 3.4, 5.2 | [Recovery](../study-guides/backup-and-recovery.md) | Compare a usable data point and service restoration time with stated requirements |
| 4.3 | [Vulnerabilities](../study-guides/vulnerability-management.md) | Prioritize a validated finding using exposure and exploitation context |
| 4.4, 4.9 | [Logs](../labs/05-sign-in-log-review/README.md) | Separate recorded facts from an explanation that needs more evidence |
| 4.8 | [Response](../study-guides/incident-response.md) | Distinguish limiting spread from removing a foothold or restoring service |
| 5.2 | [Risk](../study-guides/risk-management.md) | Calculate a stated loss estimate and explain a risk decision |

## Newly connected sections

These are additional author-assigned partial connections. The official source above defines the objectives; these links identify where our examples practice a subset.

| Objective IDs | Read | Demonstrate |
|---|---|---|
| 1.1 | [Control selection](../study-guides/security-controls.md) | Separate implementation category from purpose |
| 1.4 | [Certificate trust](../concepts/certificate-trust.md) | Explain why one valid certificate property is insufficient |
| 2.3, 2.4 | [Web attacks](../concepts/web-attack-distinctions.md) | Identify the interpreter and matching defense |
| 3.1 | [Cloud responsibility](../study-guides/cloud-responsibility.md) | Apply the stated service agreement |
| 3.3 | [Data states](../concepts/data-states.md) | Locate the exposed copy and required control |
| 4.1 | [Wireless](../study-guides/wireless-access.md), [mobile](../concepts/mobile-deployment.md) | Separate access, ownership, and management scope |
| 4.6 | [MFA](../concepts/multifactor-authentication.md), [SSO](../concepts/single-sign-on.md) | Distinguish factor categories and application permissions |
| 5.1 | [Governance](../study-guides/security-governance.md) | Choose the document that meets the request |

MFA means multifactor authentication; SSO means single sign-on. [Clickable contents](contents.md) · [All practice sets](../practice-tests/README.md).

## How to read a scenario

First identify the requested outcome: identify, compare, apply, analyze, or choose a next action. Then identify constraints such as access scope, time, existing approval, and business need. Explain why the selected answer meets those constraints.

A question about "same file contents" can need a digest comparison. A question about "which key signed this" needs a signature and a trustworthy identity binding. A question about "who can read this" needs authorization. Similar wording about security does not make these interchangeable.

This approach is a study method. We do not know the wording of your actual exam.

## Question-level connections

| Existing set | Questions | Primary objective IDs for this project's items |
|---|---|---|
| [Mixed 1](../practice-tests/mixed-01.md) | 1–2 | 1.4 |
| Mixed 1 | 3–4 | 4.6 |
| Mixed 1 | 5–6 | 4.5, 2.5 |
| Mixed 1 | 7–8 | 4.9 |
| Mixed 1 | 9–10 | 4.1 |
| Mixed 1 | 11–12 | 5.2 |
| Mixed 1 | 13–14 | 5.6 |
| [Foundations 2](../practice-tests/foundations-02.md) | 1–3 | 5.2 |
| Foundations 2 | 4–6 | 4.3 |
| Foundations 2 | 7–9 | 4.8 |

These are author-assigned alignments to particular skills, not official question classifications. Neither existing set follows the official domain proportions.

## Coverage gaps and next priorities

The repository is strongest in introductory operations exercises, but it is not complete even in Domain 4.

| Domain | Examples of work still needed |
|---|---|
| 1 | Deeper certificate lifecycle, physical controls, trust architecture |
| 2 | Actor comparisons, application weaknesses, malware and network indicators |
| 3 | Deeper deployment constraints, classification decisions, availability designs |
| 4 | Detailed wireless/mobile configuration, inventory/disposal, tools, automation |
| 5 | Supplier review, compliance, audits, and governance lifecycle |

Choose the largest gaps that also match your weak areas. Review the full linked objectives document rather than treating this table as the whole syllabus.

## Plan practice by weight without inventing exam statistics

For a future 50-item practice set, exact domain-proportional counts would be 6, 11, 9, 14, and 10. That is a proposed authoring plan, not an already available mock exam and not a claim about your live exam's question distribution.

For now, use the [mapped scenario drill](../practice-tests/mapped-scenarios-03.md) to practice identifying the requirement and explaining the decision.
