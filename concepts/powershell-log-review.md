# PowerShell: read a small log sample before drawing a conclusion

This optional Windows exercise reads existing local events. It does not enable logging or change system settings. Use a device you are authorized to inspect.

Open PowerShell and request five recent Application events:

```powershell
Get-WinEvent -LogName Application -MaxEvents 5 |
    Select-Object TimeCreated, Id, ProviderName, LevelDisplayName
```

Get-WinEvent retrieves events. -LogName selects the log, -MaxEvents limits the sample, and Select-Object displays chosen properties. An event ID needs provider and log context; the number alone is not a universal diagnosis.

Write down what the sample establishes and what remains unknown. Five records are not a complete timeline. This query does not by itself identify malicious PowerShell execution.

If access is denied or the log has no entries, preserve the message for troubleshooting. Do not change permissions or logging policy just to make the example return output. Log details may contain private information; do not upload real logs publicly.

Check yourself: explain why an empty result is different from evidence that nothing happened. The command is documented, but this repository has not recorded a learner's Windows execution result.

## Exam connection and review

Partial SY0-701 4.9 alignment. This short page does not complete the objective. [Review questions](../practice-tests/concept-review-10.md) · [Study index](../study/README.md).

## Source

[Primary documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-5.1). Examples are original and fictional.
