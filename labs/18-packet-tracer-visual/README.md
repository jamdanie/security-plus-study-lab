# Exercise 18: watch a packet cross a small network

[Resource choices](../../resources/visual-and-gamified-learning.md) · [Contents](../../study/contents.md)

Requires Cisco Packet Tracer, a Cisco account, and a local installation. Cisco provides the simulator free through Networking Academy. This original activity is ready to try; no completed run is claimed.

Purpose: observe a baseline before later studying access controls. This supports the network understanding used in partial SY0-701 3.2 and 4.5 study; it does not demonstrate an ACL or firewall.

## Build the baseline

1. Add two PCs and one switch, such as a 2960.
2. Connect PC-A FastEthernet0 to switch FastEthernet0/1 and PC-B FastEthernet0 to FastEthernet0/2 using copper straight-through cables.
3. On each PC, open Desktop, then IP Configuration. Give PC-A address `192.168.50.10` and PC-B `192.168.50.20`, both with mask `255.255.255.0`. Leave the gateway blank for this same-subnet exercise.
4. Wait for the links to become ready. From PC-A's Command Prompt, run `ping 192.168.50.20`. Repeat if the first attempt times out during address resolution or startup.

Save a baseline copy of your project.

## Observe before changing anything

Switch to Simulation mode. Filter for ARP and ICMP if those controls are available in your version. Generate another ping, then advance events with Capture/Forward. Open an event's protocol details.

ARP resolves a local IPv4 address to a link-layer address. ICMP carries the echo request/reply used here. An existing ARP cache entry can mean you see ICMP without a new ARP exchange. Don't interpret a missing ARP event alone as failure.

Record the source, destination, path, and protocol you actually see. Menu placement and event detail can vary by version.

## Change one condition

Disconnect only PC-B's cable. Predict the effect, then repeat the ping. Reconnect it, wait for readiness, and repeat. Save the changed project separately if you want to preserve the baseline.

<details>
<summary>Expected interpretation</summary>

With correct addressing and ready links, the baseline should permit communication through the switch. Removing PC-B's only link removes that path; restoring it should restore communication after the link is ready.

A failed ping alone does not prove a firewall blocked traffic. Here, the deliberate physical disconnect supplies the explanation. In another network, you would need more evidence.

The initial local exchange does not require a router because both PCs are in the same subnet. Successful communication does not prove encryption, authorization, or secure segmentation.

</details>

## Keep evidence

Save your project and a short [learning note](../../study/hands-on-notes.md): prediction, observed events, changed condition, result, and limit. Then use the [firewall rule exercise](../04-firewall-rule-review/README.md) to reason about permitted traffic.

## Official help

[Cisco access information](https://learningnetwork.cisco.com/s/article/packet-tracer-and-alternative-lab-solutions) · [First Packet Tracer lab and simulation explanation](https://tutorials.ptnetacad.net/help/default/myFirstPTLab.htm) · [Simulation mode](https://tutorials.ptnetacad.net/help/default/mode_simulation.htm)
