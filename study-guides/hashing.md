# Hashing: checking whether a file changed

A cryptographic hash function takes input and produces a fixed-length value called a hash or message digest. SHA-256 means Secure Hash Algorithm with a 256-bit output.

If you hash the same bytes with the same algorithm, you get the same result. Changing the contents should produce a different result. Renaming a file without changing its bytes does not change its content hash.

Hashing is useful for checking integrity. Encryption protects confidentiality and can be reversed with the appropriate key. Hashing is not encryption and has no decryption key.

A matching hash is only as useful as the reference you trust. If someone replaces a download and the published hash, comparing the two will not establish that the download is safe. Hash collisions are possible because different inputs can produce the same output; secure algorithms make finding useful collisions computationally difficult.

Try the [Windows hashing exercise](../labs/01-file-hashing/README.md), then review the [original Anki cards](../anki/README.md).

## Predict before you calculate

Treat the file's bytes as the input. A rename changes its path, not necessarily its contents. An editor can change line endings or encoding even when the visible wording looks identical.

### Try it without the answer

Two files look identical in an editor but have different hashes under the same algorithm. What can you conclude?

<details>
<summary>Explanation</summary>

Their bytes differ. The mismatch alone does not identify malware, the author, or the reason for the difference. Investigate encoding, line endings, or other changes.

</details>


## Sources

- [Microsoft: Get-FileHash](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-5.1)
- [Project references](../resources/README.md)
