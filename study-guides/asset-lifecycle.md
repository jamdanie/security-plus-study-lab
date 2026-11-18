# Asset management: know what you have before deciding what to do

An asset record connects a device or service to its purpose, accountable owner, location, and handling requirements. A hostname alone may not uniquely identify a physical device.

## Follow the lifecycle

| Stage | Question to answer | Useful evidence |
|---|---|---|
| Acquire | Is it approved and suitable for the intended work? | Procurement approval and requirements |
| Assign | Who is accountable and who uses it? | Asset identifier, owner, assignment record |
| Operate | What version and configuration are present? | Inventory and monitoring records |
| Transfer | Who receives custody and what data remains? | Transfer approval and updated assignment |
| Retire | Can the data and media leave control safely? | Retention decision, sanitization evidence, final disposition |

Inventory supports vulnerability work: a finding matters differently when you know the affected version, exposure, and business role. An unowned asset can leave patch and disposal decisions without a responsible person.

## Worked decision

A business wants to donate a laptop. Its inventory names a former employee, and its storage may contain customer records.

First reconcile the device identifier and accountable owner. Check retention and any hold requirements before authorizing data removal. Select an approved sanitization approach for the actual media and intended destination, verify the outcome, and document disposition.

Deleting a visible folder does not establish sanitization. Encryption also does not automatically establish that cryptographic erase is suitable: key coverage, key copies, implementation, and policy conditions need review.

## Sanitization terms

Clear, purge, and destroy are sanitization methods with different assurance and reuse implications. Choose according to media, data sensitivity, intended reuse, and applicable requirements. Do not apply a magnetic-media technique to flash storage by assuming all drives work alike.

A tool reporting success and an organization accepting the outcome are related but distinct checks. Keep evidence of the method, device identity, result, review, and destination. This page provides no destructive commands.

## Ready to move on?

Explain why an asset can be physically located but still lack an accountable owner. Then explain why a donation decision needs both data-handling approval and evidence of sanitization.

[Exercise](../labs/15-asset-disposition/README.md) · [Practice questions](../practice-tests/assets-13.md) · [Contents](../study/contents.md)

Partial SY0-701 4.2 alignment. This is not a complete media-sanitization procedure.

## Sources

- [NIST: IT asset management](https://csrc.nist.gov/news/2018/nist-releases-special-publication-1800-5).
- [NIST SP 800-88 Revision 2](https://csrc.nist.gov/pubs/sp/800/88/r2/final).
- [NIST sanitization FAQ](https://csrc.nist.gov/files/pubs/sp/800/88/r2/final/docs/sp800-88r2-faq.pdf).

Original fictional examples; use approved service- and media-specific procedures for real work.
