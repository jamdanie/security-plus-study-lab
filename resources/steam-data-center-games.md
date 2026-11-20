# Steam data center games: choose the right title

[Learning resources](visual-and-gamified-learning.md) · [Resilience exercise](../labs/19-visual-resilience/README.md)

Several Steam listings use similar names. Match the title, developer, and app number before buying. These are paid games, not required study tools. Prices vary by region and sale.

## Two distinct listings

| Listing | Developer | Store description, checked November 18, 2026 |
|---|---|---|
| [Data Center, app 4170200](https://store.steampowered.com/app/4170200/Data_Center/) | Waseku | Racks, servers, switches, manual Ethernet connections, visible traffic, capacity, and device failures |
| [Data Center Simulator Game, app 1917160](https://store.steampowered.com/app/1917160/Data_Center_Simulator_Game/) | DC Uplink | Early Access; the developer describes first-person server assembly, power/cabling, and ticket-based work |

These descriptions come from the store pages. This project has not playtested either game. Review current gameplay footage, recent reviews, update history, and system requirements before spending money. Early Access plans describe intended development, not guaranteed features.

## Turn a session into study

These are suggested reflection tasks, not claims that every game implements every feature.

| If you can observe this | Ask this | Read next |
|---|---|---|
| A cable connects two devices | Which service depends on this connection? | [Segmentation](../study-guides/network-segmentation.md) |
| A switch or server fails | Does another usable path or service instance remain? | [Backup and recovery](../study-guides/backup-and-recovery.md) |
| A replacement device is installed | What inventory and ownership records would change? | [Asset lifecycle](../study-guides/asset-lifecycle.md) |
| A layout changes | What would you test before and after a real change? | [Secure baselines](../study-guides/secure-baselines.md) |

The availability and dependency questions can support partial SY0-701 3.4 study. Asset tracking can support partial 4.2. These are author-selected connections; completing a game does not complete those objectives.

## Pair gameplay with an offline mission

After placing or moving equipment, try the [rack inventory exercise](../labs/22-rack-inventory/README.md). It supplies fictional records so you can practice even if your game has no inventory export. After changing a supported connection, use the [change rehearsal](../labs/23-change-rehearsal/README.md) to explain baseline checks and rollback.

These are companion study activities, not claims of additional game features. [Operations questions](../practice-tests/operations-missions-16.md) and [cards](../anki/operations-missions.txt) check the distinctions afterward.

## Go beyond the cable path

Use the [service dependency drawing](../labs/24-service-dependencies/README.md) to distinguish alternate network paths from shared application dependencies. Then try [guest policy review](../labs/25-guest-policy/README.md) and [recovery validation](../labs/27-recovery-validation/README.md). These companion exercises supply their own conditions; they do not claim the game implements firewall policy or database recovery.

[Visual lab comparisons](../study/visual-lab-terms.md) helps keep a game observation separate from a real-world security conclusion. [New review questions](../practice-tests/data-center-decisions-17.md) check the distinction.

## Avoid the wrong takeaway

Two cables do not automatically prove redundancy. They may still depend on one switch, power source, or service. A game animation also does not prove that a connection is encrypted or that permissions are correct.

The Waseku listing describes a visual experience without complex command lines. Do not buy it expecting a general Linux terminal. Use [Bandit](https://overthewire.org/wargames/bandit/) for a command-line challenge or [Packet Tracer](../labs/18-packet-tracer-visual/README.md) for a guided network observation.

Keep a [short learning note](../study/hands-on-notes.md) showing what you actually tested and what the simulation could not establish.
