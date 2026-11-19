# Exercise 22: reconcile a rack inventory

[Asset guide](../../study-guides/asset-lifecycle.md) · [Game connections](../../resources/steam-data-center-games.md)

Offline fictional exercise. Open [rack-records.csv](rack-records.csv) in a spreadsheet or text editor. All identifiers are invented. Ready to try. Partial SY0-701 4.2.

## The situation

A team moved equipment during maintenance. The CSV combines recorded locations and a new physical observation. In this exercise, each physical device should have its own unique serial number. The supplier is not part of the investigation.

Find:
- A location mismatch.
- An unresolved owner.
- A duplicate identity value.
- A disposition status that still needs evidence before closure.

For each, state what the record shows and the next verification. Don't silently fix the dataset by guessing.

<details>
<summary>Worked review</summary>

| Record | Issue | Next check |
|---|---|---|
| 2 | Recorded U12 differs from observed U14 | Confirm the device identity and authorized move, then update the approved record |
| 3 | Owner is blank | Confirm the responsible team through the ownership process |
| 1 and 4 | Both use LAB-S100 | Inspect labels and reconcile source records; don't assume which row is wrong |
| 5 | Pending disposal | Confirm applicable retention decisions, approved handling, and disposition evidence before marking complete |

A duplicate value is a data-quality concern; the table alone does not prove theft or a compromised device.

</details>

## Optional game connection

If your game tracks equipment locations, sketch a small inventory from what you can actually observe. If it does not show serials, label your identifiers as learner-assigned asset tags. Don't present invented labels as game-provided evidence.

Keep your reconciliation decisions, then try [Operations missions 16](../../practice-tests/operations-missions-16.md).
