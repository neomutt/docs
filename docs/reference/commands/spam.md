---
title: Spam & Scoring
description: Commands for defining spam detection rules based on header patterns and assigning cumulative scores to messages.
keywords: spam, nospam, score, unscore, spam detection, spam filtering, message scoring, header matching, spam label, bogofilter, scoring rules
---

(ref-cmd-spam)=
# Spam & Scoring

Commands for spam detection rules and message scoring.

(cmd-spam)=
## `spam`

Define a rule to detect and label spam based on a header regex.

- `spam <regex> <format>` — match a header and produce a spam label

```neomuttrc
spam "X-Spam-Score: ([0-9.]+).*"   "Spam: %1"
spam "X-Spam-Status: Yes"          "Spam"
spam "X-Bogosity: Spam"            "Bogus"
```

(cmd-nospam)=
## `nospam`

Remove a spam detection rule.

- `nospam *` — remove all spam rules
- `nospam <regex>` — remove a specific rule

```neomuttrc
nospam *
nospam "X-Bogosity: Spam"
```

(cmd-score)=
## `score`

Assign a score to messages matching a pattern.  Scores are cumulative.

- `score <pattern> <value>` — add a score value to matching messages

```neomuttrc
score "~f boss@company.com"   10
score "~s urgent"              5
score "~t neomutt-devel@"      3
score "~f spammer@"          -50
```

(cmd-unscore)=
## `unscore`

Remove scoring rules.

- `unscore *` — remove all scoring rules
- `unscore <pattern>` — remove a specific rule

```neomuttrc
unscore *
unscore "~f spammer@"
```

