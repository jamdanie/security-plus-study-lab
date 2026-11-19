# Exercise 21: inspect a saved packet capture

[Learning missions](../../resources/hands-on-missions.md) · [Log interpretation](../05-sign-in-log-review/README.md)

Requires Wireshark and an official sample capture. No live capture is needed. Ready to try; no local execution is claimed. Partial SY0-701 4.9: interpreting packet-capture evidence.

## Choose and open evidence

1. Install Wireshark from [the official site](https://www.wireshark.org/).
2. Open the [official sample capture directory](https://wiki.wireshark.org/SampleCaptures). Choose a small ordinary TCP sample from its TCP section. Record its filename and source URL. Avoid malware samples for this introductory task.
3. Open the downloaded capture in Wireshark with File > Open. Do not start a live interface capture.
4. Record the total packet count and select one TCP packet. Expand its protocol details.

## Change the view

Enter `tcp` in the display-filter bar and apply it. Compare displayed and total counts. Then apply `arp`, note the result, and clear the filter.

A sample containing only TCP might show the same count under `tcp`. It may contain no ARP packets. Record what your chosen file contains instead of inventing missing traffic.

| Observation | What it supports |
|---|---|
| A packet matches tcp | Wireshark decoded TCP in that captured packet |
| No packets match arp | No matching ARP packets are displayed from this file |
| Clearing the filter restores the list | The display filter changed the view |

## Check the limit

<details>
<summary>Worked interpretation</summary>

A display filter hides nonmatching packets in the view; it does not remove them from the original capture. It also does not block network traffic.

No displayed ARP packets does not prove that ARP never occurred anywhere on the network. Capture location, time range, and capture filtering can limit the evidence.

A packet's presence does not establish malicious intent. Describe fields and timing before assigning an attack label.

</details>

Save a [learning note](../../study/hands-on-notes.md) with a filename, filter, observation, and limit. Do not republish the sample capture here; use the provider link.

[Wireshark display-filter documentation](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkDisplayFilterSection.html) · [Review questions](../../practice-tests/visual-tools-15.md)
