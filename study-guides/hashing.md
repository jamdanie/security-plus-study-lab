# Hashing: checking whether a file changed

A cryptographic hash function takes input and produces a fixed-length value called a hash or message digest. SHA-256 means Secure Hash Algorithm with a 256-bit output.

If you hash the same bytes with the same algorithm, you get the same result. Changing the contents should produce a different result. Renaming a file without changing its bytes does not change its content hash.

Hashing is useful for checking integrity. Encryption protects confidentiality and can be reversed with the appropriate key. Hashing is not encryption and has no decryption key.

A matching hash is only as useful as the reference you trust. If someone replaces a download and the published hash, comparing the two will not establish that the download is safe. Hash collisions are possible because different inputs can produce the same output; secure algorithms make finding useful collisions computationally difficult.

Try the [Windows hashing exercise](../labs/01-file-hashing/README.md), then review the [original Anki cards](../anki/README.md).

## Sources

- [Microsoft: Get-FileHash](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-5.1)
- [Project references](../resources/README.md)
