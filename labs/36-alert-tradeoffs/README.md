# Exercise 36: compare two alert rules

[Log exercise](../05-sign-in-log-review/README.md) · [Campaign](../../resources/rack-security-campaign.md)

Offline fictional exercise. Partial SY0-701 4.4. Ready to try.

## Labeled test set

This exercise supplies reliable labels for 100 test events: 10 are malicious and 90 are benign. A rule either alerts on an event or does not. These labels are known for the exercise; real investigations may not have that certainty.

| Rule | Malicious events alerted | Benign events alerted |
|---|---|---|
| A | 9 | 30 |
| B | 6 | 3 |

Calculate total alerts, missed malicious events, and alerts that were benign. Does the rule with fewer alerts necessarily detect more attacks?

<details>
<summary>Worked calculations</summary>

Rule A generates 39 alerts: 9 true positives and 30 false positives. It misses 1 malicious event, a false negative. It does not alert on 60 benign events, true negatives.

Rule B generates 9 alerts: 6 true positives and 3 false positives. It misses 4 malicious events and does not alert on 87 benign events.

B reduces false alerts in this set but misses more malicious events. A catches more malicious events but creates more review work. The exercise does not specify an organizational cost or required detection target that would make one universally best.

</details>

## Choose evidence before tuning

If you change a threshold, retest against the required detection cases and benign activity. Track what changed. Do not claim that lower alert volume alone proves improved security.

The same logic applies to a game's score: find out what is measured before treating the number as proof of a security outcome.

Keep the calculations and a short tradeoff explanation. [Questions](../../practice-tests/rack-readiness-20.md) · [Cards](../../anki/rack-readiness.txt).
