---
title: Spam & Scoring
description: XXX
keywords: XXX
---

# Spam & Scoring

Commands for spam detection rules and message scoring.

## `spam`

Define a rule to detect and label spam based on a header regex.

- `spam <regex> <format>` — match a header and produce a spam label

```neomuttrc
spam "X-Spam-Score: ([0-9.]+).*"   "Spam: %1"
spam "X-Spam-Status: Yes"          "Spam"
spam "X-Bogosity: Spam"            "Bogus"
```

## `nospam`

Remove a spam detection rule.

- `nospam *` — remove all spam rules
- `nospam <regex>` — remove a specific rule

```neomuttrc
nospam *
nospam "X-Bogosity: Spam"
```

## `score`

Assign a score to messages matching a pattern.  Scores are cumulative.

- `score <pattern> <value>` — add a score value to matching messages

```neomuttrc
score "~f boss@company.com"   10
score "~s urgent"              5
score "~t neomutt-devel@"      3
score "~f spammer@"          -50
```

## `unscore`

Remove scoring rules.

- `unscore *` — remove all scoring rules
- `unscore <pattern>` — remove a specific rule

```neomuttrc
unscore *
unscore "~f spammer@"
```

