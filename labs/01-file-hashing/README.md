# Exercise 1: see a file change through its hash

Status: ready to try. No learner results have been recorded.

## What you need

Windows PowerShell. Administrator access and extra software are not needed. Run the blocks in the same PowerShell window. The exercise makes a separate temporary folder for each run.

## 1. Create your practice file

Open PowerShell and paste:

```powershell
$labFolder = Join-Path ([System.IO.Path]::GetTempPath()) ('security-plus-hashing-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $labFolder | Out-Null
$samplePath = Join-Path $labFolder 'practice.txt'
Set-Content -LiteralPath $samplePath -Value 'Security study lab' -Encoding UTF8
$before = (Get-FileHash -LiteralPath $samplePath -Algorithm SHA256).Hash
$before
```

The result is the file's SHA-256 hash: 64 hexadecimal characters representing 256 bits. Keep this window open.

## 2. Hash it again

```powershell
$repeat = (Get-FileHash -LiteralPath $samplePath -Algorithm SHA256).Hash
$before -eq $repeat
```

Expected result: True. The file's bytes have not changed.

## 3. Change the contents

```powershell
Add-Content -LiteralPath $samplePath -Value 'I changed the contents.' -Encoding UTF8
$after = (Get-FileHash -LiteralPath $samplePath -Algorithm SHA256).Hash
$after
$before -eq $after
```

Expected comparison: False. You changed the contents, so the hash should differ.

## 4. Rename it without editing it

```powershell
$renamedPath = Join-Path $labFolder 'renamed-practice.txt'
Move-Item -LiteralPath $samplePath -Destination $renamedPath
$renamedHash = (Get-FileHash -LiteralPath $renamedPath -Algorithm SHA256).Hash
$after -eq $renamedHash
$labFolder
```

Expected comparison: True. Get-FileHash hashes the contents, not the filename.

## Record what you observed

After running the exercise, write down which comparisons returned True or False, why the rename behaved differently from the content edit, and anything you had to troubleshoot. Explain whether a matching hash alone proves a file is safe.

Your exact hash values may differ from another person's because encoding and line endings affect the bytes. Compare your own before and after values.

## Troubleshooting and cleanup

If a variable is missing, start again at step 1 in the same PowerShell window. Use PowerShell, not Command Prompt. If a command fails, keep its error message so we can work through it.

The final command prints your temporary folder location. After reviewing your results, you can delete that specific practice folder through File Explorer.

## Related material

- [Hashing guide](../../study-guides/hashing.md)
- [Anki cards and import steps](../../anki/README.md)
- [Microsoft command documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-5.1)
