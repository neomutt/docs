---
title: Score Variables
description: NeoMutt configuration variables for message scoring and automatic actions based on score thresholds.
keywords: neomutt, score, score_threshold_delete, score_threshold_flag, score_threshold_read, configuration
---

# Score Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

## `$score`

- **Type:** boolean
- **Default:** `yes`

When this variable is *unset*, scoring is turned off. This can be useful to selectively disable scoring for certain folders when the `$score_threshold_delete` variable and related are used.

## `$score_threshold_delete`

- **Type:** number
- **Default:** `-1`

Messages which have been assigned a score equal to or lower than the value of this variable are automatically marked for deletion by NeoMutt. Since NeoMutt scores are always greater than or equal to zero, the default setting of this variable will never mark a message for deletion.

## `$score_threshold_flag`

- **Type:** number
- **Default:** `9999`

Messages which have been assigned a score greater than or equal to this variable's value are automatically marked "flagged".

## `$score_threshold_read`

- **Type:** number
- **Default:** `-1`

Messages which have been assigned a score equal to or lower than the value of this variable are automatically marked as read by NeoMutt. Since NeoMutt scores are always greater than or equal to zero, the default setting of this variable will never mark a message read.
