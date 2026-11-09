# Exercise 3: verify a hash with a Python tool

Status: ready to try. Automated script tests are separate from learner completion.

## Requirements

Python 3.9 or newer. No third-party packages, API keys, or administrator access are needed. Download the repository ZIP from GitHub's Code menu and extract it. Open a terminal in the extracted repository folder.

The commands below use Windows' Python launcher, py. If your installation uses python or python3, use that command instead.

## Calculate a known hash

Create a three-byte file and hash it:

```powershell
py -c "from pathlib import Path; Path('hash-practice.txt').write_bytes(b'abc')"
py scripts/hash_file.py hash-practice.txt
```

Expected SHA-256 (Secure Hash Algorithm with a 256-bit output):

```text
ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
```

This exact value is possible because the command writes specific bytes without adding a newline. If hash-practice.txt already exists, this command replaces it; use a new extracted practice folder.

## Compare with a reference

```powershell
py scripts/hash_file.py hash-practice.txt --expected ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
$LASTEXITCODE
```

Expected: MATCH and exit code 0.

Now change the file and repeat the same comparison:

```powershell
py -c "from pathlib import Path; Path('hash-practice.txt').write_bytes(b'abd')"
py scripts/hash_file.py hash-practice.txt --expected ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
$LASTEXITCODE
```

Expected: MISMATCH and exit code 1. Exit code 2 indicates a usage or file-read error. A calculation without --expected returns 0 if successful; that does not mean a reference was checked.

## Inspect the code

Open [hash_file.py](../../scripts/hash_file.py). Find where it reads bytes, updates the digest, and compares the result. Reading in chunks avoids loading the entire file into memory.

The script does not download files or establish whether a reference is trustworthy. It compares the file with the reference you supply.

## Run the automated checks

```powershell
py -m unittest discover -s tests -v
```

The checks cover known hashes, content changes, renames, uppercase references, a mismatch, missing files, and malformed references.

## Record your observations

Explain why changing one byte affected the comparison and how an exit code could help another script decide what to do next. Delete hash-practice.txt after finishing if you no longer need it.

## Sources

- [Python hashlib documentation](https://docs.python.org/3/library/hashlib.html)
- [Hashing guide](../../study-guides/hashing.md)
