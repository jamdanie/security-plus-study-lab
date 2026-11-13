# Security+ study lab

I'm building this project while studying for CompTIA Security+. It brings together study notes, Anki cards, walkthroughs, and exercises so I can practice what I'm learning and make it easier for someone else to get started.

The goal is to connect an explanation to something you can actually try. Each topic can include a guide, an exercise, review cards, and notes about what happened when I worked through it. Completed work and exercises that are ready to try will be labeled separately.

## Start here

The first topic is file hashing:

1. Read [Hashing: checking whether a file changed](study-guides/hashing.md).
2. Try the [Windows PowerShell walkthrough](labs/01-file-hashing/README.md).
3. Review the [original Anki cards](anki/README.md).
4. Record your results and explain what the comparisons tell you.

The walkthrough is ready to try. I haven't recorded my results yet.

## More to try

- [Identity and access guide](study-guides/identity-and-access.md): authentication, authorization, roles, and least privilege.
- [Access-review exercise](labs/02-access-review/README.md): review a fictional group's permissions and explain your decisions.
- [Python hash-checker exercise](labs/03-python-hash-checker/README.md): calculate a file hash, compare a reference, and inspect exit codes.
- [Script tests](tests/test_hash_file.py): seven automated checks covering known hashes and failure cases.

These exercises are ready to try. Personal completion notes have not been recorded. The Python tool's seven automated tests passed during development; that is separate from completing the exercises.

- [Network segmentation guide](study-guides/network-segmentation.md): VLAN boundaries, access control lists, and default deny.
- [Firewall rule-review exercise](labs/04-firewall-rule-review/README.md): identify a broad permit that defeats a guest-access restriction, repair it, and retest four requests.

- [Sign-in log review](labs/05-sign-in-log-review/README.md): investigate fictional login events, distinguish authentication from authorization, and separate evidence from assumptions.

- [Cryptography choices](study-guides/cryptography-choices.md) and [scenario exercise](labs/06-choose-cryptographic-controls/README.md): distinguish hashing, encryption, and digital signatures.
- [Using existing Anki decks](anki/using-your-existing-decks.md): export, review, and identify material suitable for public sharing.

- [Secure baselines guide](study-guides/secure-baselines.md) and [configuration-drift exercise](labs/07-configuration-drift/README.md): compare settings, review exceptions, and explain corrections.
- [Security+ deck review](anki/deck-review.md): inventory and cleanup priorities for the existing personal study collection. Cisco material is outside this review's scope.

- [Backup and recovery guide](study-guides/backup-and-recovery.md) and [recovery-objectives exercise](labs/08-recovery-objectives/README.md): distinguish recovery point from recovery time and evaluate failed backups.

## What's in the repository

| Folder | Purpose |
|---|---|
| [study-guides](study-guides/hashing.md) | Explanations connected to practical examples |
| [labs](labs/01-file-hashing/README.md) | Steps, expected results, and troubleshooting |
| [anki](anki/README.md) | Original cards and import instructions |
| [scripts](scripts/README.md) | A Python hash checker and command documentation |
| [resources](resources/README.md) | Textbook credit and supporting documentation |

## What comes next

- Run the first exercise and document the results.
- Confirm the target exam version and map topics to its objectives.
- Add more topics as I study them.
- Add automated checks and an exercise using an application programming interface (API) when there is a useful reason for each.

This is a work in progress, not a complete exam guide. The website, automated GitHub workflow, and connected services haven't been built yet. Script tests can be run locally.

## Textbook and sources

I'm using Mark Ciampa's *CompTIA Security+ Guide to Network Security Fundamentals*, eighth edition, published by Cengage, as a starting point. Supporting documentation is linked in the guides and [references](resources/README.md).

The textbook PDF and copied textbook review questions aren't included. Public practice questions are original supporting material. This project is independent and isn't affiliated with or endorsed by CompTIA or Cengage.

## Corrections and contributions

If an explanation is wrong or a step doesn't work, open an issue with the page, command, and what happened. Remove personal information from screenshots and error messages before posting. Contributions should use original material or material you have permission to share.
