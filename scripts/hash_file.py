"""Compute or verify a SHA-256 file hash. No external packages required."""
import argparse
import hashlib
import re
import sys
from pathlib import Path


def hash_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--expected", help="Trusted SHA-256 hash (64 hexadecimal characters)")
    args = parser.parse_args(argv)
    if args.expected is not None and not re.fullmatch(r"[0-9a-fA-F]{64}", args.expected):
        parser.error("--expected must contain exactly 64 hexadecimal characters")
    try:
        actual = hash_file(args.file)
    except OSError as error:
        print(f"Cannot read file: {error}", file=sys.stderr)
        return 2
    print(f"SHA-256: {actual}")
    if args.expected is None:
        return 0
    if actual == args.expected.lower():
        print("MATCH: the content hash matches the supplied reference.")
        return 0
    print("MISMATCH: the content hash differs from the supplied reference.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
