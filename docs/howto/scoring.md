---
title: How to Use Scoring
description: Assign scores to messages using pattern matching for sorting and filtering
keywords: score, unscore, scoring, patterns, message scoring
---

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

# How to Use Scoring

## Syntax

```
score pattern value
unscore {* | pattern ...}
```

## Adding Score Rules

The `score` command adds *value* to a message's score if *pattern* matches it. *pattern* is a string in the format described in the patterns section (note: for efficiency reasons, patterns which scan information not available in the index, such as `~b`, `~B`, `~h`, `~M`, or `~X` may not be used). *value* is a positive or negative integer. A message's final score is the sum total of all matching `score` entries. However, you may optionally prefix *value* with an equal sign (`=`) to cause evaluation to stop at a particular entry if there is a match. Negative final scores are rounded up to 0.

## Removing Score Rules

The `unscore` command removes score entries from the list. You **must** specify the same pattern specified in the `score` command for it to be removed. The pattern `*` is a special token which means to clear the list of all score entries.

## Scoring and Threading

Scoring occurs as the messages are read in, before the mailbox is sorted. Because of this, patterns which depend on threading, such as *~=*, *~$*, and *~()*, will not work by default. A workaround is to push the scoring command in a folder hook. This will cause the mailbox to be rescored after it is opened and input starts being processed:

```
folder-hook . 'push "<enter-command>score ~= 10<enter>"'
```
