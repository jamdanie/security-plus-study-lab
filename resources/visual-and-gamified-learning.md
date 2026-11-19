# Visual and gamified learning

[Contents](../study/contents.md) · [Steam games](steam-data-center-games.md) · [Record what you learned](../study/hands-on-notes.md)

If a page of definitions isn't clicking, choose one concept and watch it happen. Start with a free option. Paid games are optional, and none of these resources is a complete Security+ course.

## Pick the experience you want

| Resource | Cost and access | What to try | Connection to this guide |
|---|---|---|---|
| [Cisco Packet Tracer](https://learningnetwork.cisco.com/s/article/packet-tracer-and-alternative-lab-solutions) | Free software through Cisco Networking Academy; account and installation required | Build a small network and step through packet events | [Guided first observation](../labs/18-packet-tracer-visual/README.md); then [segmentation](../study-guides/network-segmentation.md) |
| [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) | Public beginner wargame; SSH client and internet connection required | Start at Level 0; use the level's command hints | Read files, navigate directories, and explain which evidence a command returned |
| [CMU CyLab Security Academy, formerly picoCTF](https://picoctf.org/) | Free platform; follow the official page to current login and account requirements | Choose one introductory challenge and explain its mechanism | [Web attack distinctions](../concepts/web-attack-distinctions.md) or [cryptography choices](../study-guides/cryptography-choices.md), depending on the challenge |
| [PortSwigger Web Security Academy](https://portswigger.net/web-security/) | Free interactive labs; account and tool requirements vary by lab | Read one beginner topic, then attempt its provided lab | [Web attack distinctions](../concepts/web-attack-distinctions.md) |
| [Data Center on Steam](https://store.steampowered.com/app/4170200/Data_Center/) | Paid game; check current price and system requirements | Observe cable paths and service dependencies | [Resilience exercise](../labs/19-visual-resilience/README.md) |

Cost and access descriptions were checked November 18, 2026. Recheck provider pages before downloading or buying.

## More ways to see the result

[Hands-on missions](hands-on-missions.md) connects four new activities to questions and cards.

| Tool or format | Activity | What it helps distinguish |
|---|---|---|
| [CyberChef](https://gchq.github.io/CyberChef/) | [Supplied practice text](../labs/20-cyberchef-basics/README.md) | Encoding, digest comparison, and confidentiality |
| [Wireshark](https://www.wireshark.org/) | [Saved sample capture](../labs/21-wireshark-display/README.md) | Filtering a view versus blocking traffic |
| Spreadsheet or text editor | [Fictional rack records](../labs/22-rack-inventory/README.md) | Inventory evidence versus assumptions |
| Paper or a simulator you control | [Change rehearsal](../labs/23-change-rehearsal/README.md) | Link indication versus service validation |

CyberChef and Wireshark documentation was checked November 19, 2026; links are provided in the exercises. These activities do not require a paid game.

## A short session

Choose a question first: “What fails if this switch stops working?” Predict the outcome. Make one change in the simulator or complete one challenge. Record the observed result, explain it, then return to the related guide.

If you need a hint, record which part helped. Complete the explanation in your own words before opening another challenge.

## What these activities do and don't establish

A capture-the-flag challenge rewards finding a solution or flag. Security+ also asks you to choose an appropriate control under stated constraints. After a challenge, explain the weakness, affected asset, matching defense, and how you would check the defense.

Packet Tracer models networking behavior; it is not a full Linux environment. Bandit practices real shell interaction but is less visual. A data center game can make dependencies easier to see without proving that its traffic, commands, or failure behavior match production equipment.

The exam connections here are this project's partial study suggestions, not provider claims of CompTIA alignment. Use only the training environments supplied by the provider.

## No download option

Try the [offline resilience exercise](../labs/19-visual-resilience/README.md). It includes a topology, a changed condition, and a worked answer.
