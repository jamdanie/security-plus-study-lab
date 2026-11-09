# Scripts

[hash_file.py](hash_file.py) calculates a SHA-256 (Secure Hash Algorithm with a 256-bit output) file hash and optionally compares it with a reference.

Use Python 3.9 or newer. No third-party packages are required.

```text
py scripts/hash_file.py path-to-your-file
py scripts/hash_file.py path-to-your-file --expected YOUR_REFERENCE_HASH
```

Replace the example path and reference with your own values, or follow the [complete walkthrough](../labs/03-python-hash-checker/README.md) for runnable commands.

The script reads the file without modifying it. It returns 0 for a successful calculation or matching reference, 1 for a mismatch, and 2 for a usage or read error. A match does not establish that your reference is trustworthy.

Run the checks from the repository root:

```text
py -m unittest discover -s tests -v
```

The original [PowerShell exercise](../labs/01-file-hashing/README.md) is also available. Connected services and application programming interface (API) exercises are planned; none are connected yet.
