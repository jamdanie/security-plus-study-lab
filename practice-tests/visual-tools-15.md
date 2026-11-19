# Visual tools 15

Four original questions. Partial SY0-701 1.4 and 4.9. This targeted set is not a weighted mock exam.

[Mission directory](../resources/hands-on-missions.md) · [Contents](../study/contents.md)

Choose one answer per question before opening the key.

## 1. A message becomes aGVsbG8= after Base64 encoding. What protection does that alone provide?

- A. Confidentiality with a secret key.
- B. A changed representation that can be decoded without a secret.
- C. Proof of sender identity.
- D. Proof the receiver is authorized.

## 2. A Wireshark display filter hides packets. What happened to the original capture?

- A. The hidden packets were deleted.
- B. The network blocked those packets.
- C. The packets remain; the view changed.
- D. The traffic was encrypted.

## 3. No ARP packets appear in one saved capture. Which statement is supported?

- A. ARP never occurred anywhere.
- B. The network is secure.
- C. Every host uses static ARP entries.
- D. This file has no displayed packets matching the filter.

## 4. A digest matches a reference from an unverified source. What remains unresolved?

- A. Whether the reference is trustworthy.
- B. Whether a display filter is enabled.
- C. Whether Base64 has a key.
- D. Whether the filename has capitals.

<details>
<summary>Answers and explanations</summary>

1. **B.** Base64 changes representation. A assumes encryption, C assumes authentication, and D assumes authorization that encoding does not supply.

2. **C.** Display filtering changes visibility. A confuses viewing with deletion, B with traffic enforcement, and D with encryption.

3. **D.** D stays within the evidence. A generalizes beyond the capture, while B and C require evidence not provided.

4. **A.** A matters to the integrity claim. B is unrelated. C assumes a secret key for Base64. D does not establish the reference's provenance.

</details>

Review correct guesses as well as errors. State the missed requirement, explain the nearest alternative, and retry with one changed condition. Supporting documentation is linked in the mission exercises.
