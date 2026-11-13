# Security+ study lab

I'm building this project while studying for CompTIA Security+. It brings together explanations, Anki cards, walkthroughs, and exercises so I can practice what I'm learning and help others work through the same topics.

## Where do you want to start?

| Goal | Start here |
|---|---|
| Work on a weak section | [Study by topic](study/README.md) |
| Find what needs review | [Mixed practice test 1: 14 questions](practice-tests/mixed-01.md) |
| Check answers and choose a section | [Explained answers and review links](practice-tests/mixed-01-answers.md) |
| Review with flashcards | [Anki sets and import instructions](anki/README.md) |
| Use existing class cards as a study source | [Security+ deck review](anki/deck-review.md) |

## Study sections

- [Cryptography](study-guides/cryptography-choices.md)
- [Identity and access](study-guides/identity-and-access.md)
- [Network segmentation and firewall rules](study-guides/network-segmentation.md)
- [Security monitoring and sign-in logs](labs/05-sign-in-log-review/README.md)
- [Secure baselines and configuration drift](study-guides/secure-baselines.md)
- [Backup and recovery](study-guides/backup-and-recovery.md)
- [Phishing and message verification](study-guides/phishing.md)

Each section connects explanation to practice. Start with the [topic index](study/README.md) for the exercise and card links.

## Hands-on tools

The [PowerShell file-hashing walkthrough](labs/01-file-hashing/README.md) and [Python hash-checker exercise](labs/03-python-hash-checker/README.md) let you compare file contents with a reference. The [Python tool](scripts/hash_file.py) includes [seven automated tests](tests/test_hash_file.py), which passed during development.

## Project status

Exercises are ready to try; personal completion results have not been recorded. Public practice questions are original. The short test covers this repository's available topics, not the full certification blueprint, and its score does not predict exam readiness.

The target exam version and objective mapping have not been confirmed. Dedicated coverage of governance, risk, vulnerability management, wireless security, cloud security, and broader incident response remains to be built. The website, automated GitHub workflow, and connected services are not implemented.

## Textbook and sources

I'm using Mark Ciampa's *CompTIA Security+ Guide to Network Security Fundamentals*, eighth edition, published by Cengage, as a starting point. Supporting documentation is linked in the guides and [references](resources/README.md).

The textbook PDF and copied textbook review questions aren't included. Public practice questions are original supporting material. This project is independent and isn't affiliated with or endorsed by CompTIA or Cengage.

## Corrections and contributions

If an explanation is wrong or a step doesn't work, open an issue with the page, command, and what happened. Remove personal information from screenshots and error messages before posting. Contributions should use original material or material you have permission to share.
