---
title: Pattern Syntax
description: XXX
keywords: XXX
---

# Pattern Syntax

NeoMutt uses patterns to select messages and aliases. This document covers both
pattern systems: **message patterns** (used throughout NeoMutt for filtering,
coloring, scoring, and hooks) and **alias patterns** (used in the alias dialog).

## Message Patterns

Message patterns are the primary pattern system in NeoMutt. They are used by
many commands and configuration directives:

- `limit` — filter the index view
- `tag-pattern` / `untag-pattern` — tag or untag messages
- `score` — assign scores to messages
- `color index` — colorize messages in the index
- `folder-hook`, `message-hook`, `reply-hook`, `send-hook`, `send2-hook` — hooks
- `push` and macro commands that reference patterns

### General Syntax

A pattern is composed of one or more **pattern terms**, optionally connected by
logical operators. Each term consists of a **prefix character**, a **pattern
letter**, and (for some patterns) an **argument**.

```sh
~X [ARGUMENT]
│ │
│ └── pattern letter (e.g., f for From, s for Subject)
└──── prefix character (~, =, or %)
```

### Pattern Prefixes

Patterns use three prefix characters to control matching behavior:

| Prefix | Name | Argument Type | Description |
|--------|------|---------------|-------------|
| `~` | Standard | REGEX | Matches using a POSIX regular expression |
| `=` | IMAP server-side | STRING | Matches using substring comparison (IMAP only) |
| `%` | Address group | GROUP | Matches against a named address group |

Examples:

```neomuttrc
# Standard regex match: From contains "alice"
color index green default "~f alice"

# IMAP server-side match: body contains "project update"
color index cyan default "=b project update"

# Address group match: From is a member of the "work" group
color index yellow default "%f work"
```

### Logical Operators and Grouping

Multiple pattern terms can be combined using logical operators:

| Operator | Meaning | Example |
|----------|---------|---------|
| *(implicit)* | AND | `~N ~F` — new **and** flagged |
| `\|` | OR | `~N \| ~F` — new **or** flagged |
| `!` | NOT | `!~D` — not deleted |
| `()` | Grouping | `!(~N \| ~F)` — neither new nor flagged |
| `^` | All addresses | `^~t user@example.com` — ALL To: addresses match |
| `@` | Alias mode | Marks the pattern for alias matching |

Operator precedence (highest to lowest): `!`, implicit AND, `|`. Use
parentheses to override precedence.

```neomuttrc
# Tag messages that are new and flagged
tag-pattern "~N ~F"

# Color messages that are either new or flagged
color index brightred default "~N | ~F"

# Score messages that are not deleted and not read
score "!~D !~R" +5

# Limit to messages where ALL To: recipients are at example.com
limit "^~t @example\\.com$"

# Complex grouping: unread messages from Alice or Bob
color index cyan default "(~f alice | ~f bob) ~U"
```

### Flag Patterns (No Argument)

These patterns match on message flags and properties. They take no argument.

| Pattern | Description |
|---------|-------------|
| `~A` | All messages |
| `~D` | Deleted messages |
| `~E` | Expired messages |
| `~F` | Flagged (important/starred) messages |
| `~g` | Cryptographically signed messages |
| `~G` | Cryptographically encrypted messages |
| `~k` | Messages containing a PGP key |
| `~l` | Messages addressed to a known mailing list |
| `~N` | New messages |
| `~O` | Old messages (seen in previous session, but not read) |
| `~p` | Messages addressed to you |
| `~P` | Messages from you |
| `~Q` | Messages which have been replied to |
| `~R` | Read messages |
| `~S` | Superseded messages |
| `~T` | Tagged messages |
| `~u` | Messages addressed to a subscribed mailing list |
| `~U` | Unread messages (combines `~N` and `~O`) |
| `~v` | Messages part of a collapsed thread |
| `~V` | Cryptographically verified messages |
| `~#` | Broken threads (missing parent) |
| `~$` | Unreferenced messages (not referenced by other messages) |
| `~=` | Duplicated messages (same Message-Id) |

Examples:

```neomuttrc
# Color flagged messages bright yellow
color index brightyellow default "~F"

# Limit view to unread messages only
# (type 'l' in the index, then enter:)
# ~U

# Score new messages from mailing lists
score "~N ~l" +10

# Tag all deleted messages
tag-pattern "~D"

# Color encrypted messages
color index brightmagenta default "~G"

# Find duplicate messages
limit "~="
```

### Address and Header Patterns (Regex Argument)

These patterns take a regular expression argument for `~` prefix, a plain
string for `=` prefix, or an address group name for `%` prefix.

| Pattern | `=` variant | `%` variant | Matches against |
|---------|-------------|-------------|-----------------|
| `~b REGEX` | `=b STRING` | | Message body |
| `~B REGEX` | `=B STRING` | | Entire message (headers + body) |
| `~c REGEX` | | `%c GROUP` | Cc: header |
| `~C REGEX` | | `%C GROUP` | To:, Cc:, or Bcc: (any recipient) |
| `~e REGEX` | | `%e GROUP` | Sender: header |
| `~f REGEX` | | `%f GROUP` | From: header |
| `~h REGEX` | `=h STRING` | | All headers (raw) |
| `~H REGEX` | | | Spam header (X-Spam-Status, etc.) |
| `~i REGEX` | | | Message-Id header |
| `~K REGEX` | | | Bcc: header |
| `~L REGEX` | | `%L GROUP` | From:, Sender:, To:, or Cc: (any address) |
| `~M REGEX` | | | Content-Type header (MIME type) |
| `~s REGEX` | | | Subject: header |
| `~t REGEX` | | | To: header |
| `~w REGEX` | | | Newsgroups header (NNTP only) |
| `~x REGEX` | | | References: or In-Reply-To: header |
| `~y REGEX` | | | X-Label: header |
| `~Y REGEX` | | | Message tags |

> **Note:** `~w` is only available when NeoMutt is compiled with NNTP support.

Examples:

```neomuttrc
# Color messages from anyone at example.com
color index green default "~f @example\\.com"

# Limit to messages with "budget" in the subject
# (type 'l' in the index, then enter:)
# ~s budget

# Score messages where you are in Cc
score "~c your@email\\.com" +3

# Color messages addressed to any recipient matching a pattern
color index blue default "~C @dev\\.example\\.org"

# Find messages with PDF attachments
limit "~M application/pdf"

# Color messages referencing a specific Message-Id
color index cyan default "~x 20240315\\.abc123@mail\\.example\\.com"

# Match messages tagged with "important"
color index brightyellow default "~Y important"

# Body search for a specific phrase
limit "~b quarterly report"

# Color messages from members of the "colleagues" address group
color index green default "%f colleagues"

# Use with hooks: auto-flag messages from your boss
message-hook "~f boss@company\\.com" "set scoring=yes"
```

### Date Patterns

Date patterns filter messages by when they were sent or received.

| Pattern | Description |
|---------|-------------|
| `~d DATERANGE` | Date the message was sent (Date: header) |
| `~r DATERANGE` | Date the message was received |

#### Relative Date Offsets

Relative offsets compare the message date to the current time:

| Syntax | Meaning |
|--------|---------|
| `<3d` | Less than 3 days ago |
| `>3d` | More than 3 days ago |
| `=3d` | Exactly 3 days ago |

#### Offset Units

| Unit | Meaning |
|------|---------|
| `y` | Years |
| `m` | Months |
| `w` | Weeks |
| `d` | Days |
| `H` | Hours |
| `M` | Minutes |
| `S` | Seconds |

#### Absolute Dates

Absolute dates can be specified in `DD/MM/YYYY` format (month and year are
optional and default to the current month/year) or ISO 8601 `YYYYMMDD` format:

| Example | Meaning |
|---------|---------|
| `10` | 10th of the current month |
| `10/12` | 10th of December, current year |
| `10/12/2024` | 10th of December, 2024 |
| `20241210` | 10th of December, 2024 (ISO 8601) |

#### Date Ranges

Two dates separated by `-` define an inclusive range:

| Example | Meaning |
|---------|---------|
| `1/1/2024-31/12/2024` | January 1 to December 31, 2024 |
| `20240101-20241231` | Same range in ISO 8601 format |
| `1/6/2024-` | June 1, 2024 until now |

#### Mixed Date-Offset Ranges

A date and an offset can be combined:

| Example | Meaning |
|---------|---------|
| `-3d+2d` | From 3 days ago to 2 days from now |
| `1/6/2024-3d` | June 1, 2024 minus 3 days (May 29) |
| `1/6/2024+2w` | June 1, 2024 plus 2 weeks (June 15) |
| `*2w` | 2 weeks in both directions from today |

Examples:

```neomuttrc
# Color messages received in the last 24 hours
color index brightgreen default "~r <1d"

# Limit to messages sent in the past week
# (type 'l' in the index, then enter:)
# ~d <1w

# Score messages older than 6 months
score "~d >6m" -5

# Color messages from a specific date range
color index cyan default "~d 1/1/2025-31/3/2025"

# Find messages received more than a year ago
limit "~r >1y"

# Messages sent in the last 2 hours
limit "~d <2H"

# Messages within a 1-month window centered on today
limit "~d *1m"
```

### Range Patterns

Range patterns match on numeric properties of messages.

| Pattern | Description |
|---------|-------------|
| `~m RANGE` | Message number in the mailbox |
| `~n RANGE` | Message score |
| `~X RANGE` | Number of MIME attachments |
| `~z RANGE` | Message size (in bytes) |

#### Range Syntax

| Syntax | Meaning |
|--------|---------|
| `100` | Exactly 100 |
| `10-100` | Between 10 and 100, inclusive |
| `-100` | Up to 100 (0 to 100) |
| `100-` | 100 or more |
| `<100` | Less than 100 (exclusive) |
| `>100` | Greater than 100 (exclusive) |

#### Size Suffixes (for `~z` only)

| Suffix | Meaning |
|--------|---------|
| `K` | Kilobytes (×1024) |
| `M` | Megabytes (×1048576) |

Examples:

```neomuttrc
# Color large messages (over 1 megabyte)
color index brightred default "~z >1M"

# Limit to messages with attachments
# (type 'l' in the index, then enter:)
# ~X >0

# Score messages with high scores even higher
score "~n >50" +10

# Color small messages (under 10 kilobytes)
color index white default "~z <10K"

# Limit to messages 50 through 100
limit "~m 50-100"

# Find messages with exactly 3 attachments
limit "~X 3"

# Messages between 100K and 500K
color index yellow default "~z 100K-500K"
```

### Thread Patterns

Thread patterns match messages based on their position in a thread hierarchy.

| Pattern | Description |
|---------|-------------|
| `~(PATTERN)` | Messages in threads containing a message that matches PATTERN |
| `~<(PATTERN)` | Messages whose immediate parent matches PATTERN |
| `~>(PATTERN)` | Messages having a direct child that matches PATTERN |

Examples:

```neomuttrc
# Color all messages in threads that contain a flagged message
color index yellow default "~(~F)"

# Limit to threads containing messages from your boss
limit "~(~f boss@company.com)"

# Find messages whose parent was from Alice
limit "~<(~f alice@example.com)"

# Find messages that have a reply from Bob
limit "~>(~f bob@example.com)"

# Color entire threads that contain unread messages
color index brightcyan default "~(~U)"

# Combine with other patterns: threads with flagged messages, but only show unread
limit "~(~F) ~U"
```

### IMAP Server-Side Patterns

When connected to an IMAP server, the `=` prefix performs server-side string
matching. This is faster than downloading messages for local regex matching,
but only supports substring comparison (not regular expressions).

| Pattern | Description |
|---------|-------------|
| `=b STRING` | Body contains STRING |
| `=B STRING` | Headers or body contain STRING |
| `=h STRING` | Headers contain STRING |
| `=/ STRING` | Gmail custom server-side search (Gmail only) |

The `=/ STRING` pattern is specific to Gmail's IMAP implementation and passes
the string directly to Gmail's search engine, supporting Gmail's search
operators.

Examples:

```neomuttrc
# IMAP server-side body search (faster than ~b for IMAP)
limit "=b project deadline"

# Gmail-specific search using Gmail operators
limit "=/ has:attachment larger:5M"

# Server-side header search
limit "=h X-Mailer: Thunderbird"
```

### Regex Case Sensitivity

NeoMutt uses **smart case matching** for regular expressions:

- If the regex contains **only lowercase** characters, matching is
  **case-insensitive**
- If the regex contains **any uppercase** character, matching is
  **case-sensitive**

```sh
# Case-insensitive: matches "alice", "Alice", "ALICE"
~f alice

# Case-sensitive: matches only "Alice" (not "alice" or "ALICE")
~f Alice

# Case-insensitive: all lowercase, matches "urgent", "Urgent", "URGENT"
~s urgent

# Case-sensitive: uppercase letter present, matches only "URGENT"
~s URGENT
```

### Simple Search Shortcuts

When a search string does **not** start with `~`, `=`, or `%`, it is treated
as a "simple search." NeoMutt expands it using the `$simple_search` variable.

The default value of `$simple_search` is `~f %s | ~s %s`, where `%s` is
replaced with the search string. This means a plain search term like `alice`
becomes `~f alice | ~s alice`, searching both the From: and Subject: fields.

```neomuttrc
# Set a custom simple search to also search the body
set simple_search = "~f %s | ~s %s | ~b %s"
```

#### Special Simple Search Keywords

Certain keywords are recognized and expanded to flag patterns:

| Keyword | Expands to | Meaning |
|---------|------------|---------|
| `all` | `~A` | All messages |
| `.` | `~A` | All messages |
| `^` | `~A` | All messages |
| `del` | `~D` | Deleted messages |
| `flag` | `~F` | Flagged messages |
| `new` | `~N` | New messages |
| `old` | `~O` | Old messages |
| `repl` | `~Q` | Replied-to messages |
| `read` | `~R` | Read messages |
| `tag` | `~T` | Tagged messages |
| `unread` | `~U` | Unread messages |

These keywords work in the `limit` command. For example, typing `l` then
entering `new` is equivalent to entering `~N`.

---

## Alias Patterns

Alias patterns are a **separate** pattern system used exclusively in the alias
dialog. When you open the alias dialog and use `limit`, `tag-pattern`, or
`untag-pattern`, patterns are interpreted as alias patterns, not message
patterns.

### Supported Operators

Only four pattern operators are supported in alias mode:

| Pattern | Matches against |
|---------|-----------------|
| `~f REGEX` | Alias **name** (the short identifier/key) |
| `~t REGEX` | Alias **address list** (email addresses) |
| `~c REGEX` | Alias **comment** (descriptive text) |
| `~Y REGEX` | Alias **tags** |

> **Important:** Although alias patterns reuse the same `~f`, `~t`, and `~c`
> syntax as message patterns, they match against completely different fields.
> In message patterns, `~f` matches the From: header; in alias patterns, `~f`
> matches the alias name.

Examples:

```sh
# In the alias dialog, limit to aliases whose name contains "work"
~f work

# Find aliases with addresses at example.com
~t @example\.com

# Find aliases with "team lead" in the comment
~c team lead

# Find aliases tagged as "project-alpha"
~Y project-alpha

# Combine: aliases named "dev" with addresses at example.org
~f dev ~t @example\.org

# Either work aliases or personal aliases
~f work | ~f personal

# Aliases NOT tagged as "archived"
!~Y archived
```

### Alias Simple Search

When a plain string is entered in the alias dialog (without a `~`, `=`, or `%`
prefix), it is expanded using the built-in alias simple search:

```
~f %s | ~t %s | ~c %s
```

This searches the alias name, addresses, and comment simultaneously. For
example, entering `john` in the alias dialog limit prompt is equivalent to:

```
~f john | ~t john | ~c john
```

### Differences from Message Patterns

| Feature | Message Patterns | Alias Patterns |
|---------|-----------------|----------------|
| `~f` | Matches From: header | Matches alias name |
| `~t` | Matches To: header | Matches alias addresses |
| `~c` | Matches Cc: header | Matches alias comment |
| `~Y` | Matches message tags | Matches alias tags |
| Flag patterns (`~N`, `~F`, etc.) | Supported | **Not supported** |
| Date patterns (`~d`, `~r`) | Supported | **Not supported** |
| Range patterns (`~m`, `~z`, etc.) | Supported | **Not supported** |
| Thread patterns (`~()`, `~<()`, `~>()`) | Supported | **Not supported** |
| Body/header search (`~b`, `~h`, etc.) | Supported | **Not supported** |
| IMAP patterns (`=b`, `=h`, etc.) | Supported | **Not supported** |
| Group patterns (`%f`, `%c`, etc.) | Supported | **Not supported** |
| Logical operators (`!`, `\|`, `()`) | Supported | Supported |
| Simple search | Configurable via `$simple_search` | Fixed: `~f %s \| ~t %s \| ~c %s` |

> **Note:** Unsupported operators in alias mode will silently fail to match any
> alias. No error is reported.

---

## Quick Reference

### Pattern Prefixes

| Prefix | Type | Argument |
|--------|------|----------|
| `~` | Standard | Regular expression |
| `=` | IMAP server-side | Substring |
| `%` | Address group | Group name |

### All Message Pattern Operators

| Pattern | Argument | Description |
|---------|----------|-------------|
| `~A` | — | All messages |
| `~b` | REGEX | Body matches |
| `~B` | REGEX | Entire message matches |
| `~c` | REGEX | Cc: matches |
| `~C` | REGEX | To:, Cc:, or Bcc: matches |
| `~d` | DATE | Sent date |
| `~D` | — | Deleted |
| `~e` | REGEX | Sender: matches |
| `~E` | — | Expired |
| `~f` | REGEX | From: matches |
| `~F` | — | Flagged |
| `~g` | — | Cryptographically signed |
| `~G` | — | Cryptographically encrypted |
| `~h` | REGEX | Headers match |
| `~H` | REGEX | Spam header matches |
| `~i` | REGEX | Message-Id matches |
| `~I` | QUERY | External search query |
| `~k` | — | Contains PGP key |
| `~K` | REGEX | Bcc: matches |
| `~l` | — | To known mailing list |
| `~L` | REGEX | Any address field matches |
| `~m` | RANGE | Message number |
| `~M` | REGEX | Content-Type matches |
| `~n` | RANGE | Score |
| `~N` | — | New |
| `~O` | — | Old |
| `~p` | — | Addressed to you |
| `~P` | — | From you |
| `~Q` | — | Replied to |
| `~r` | DATE | Received date |
| `~R` | — | Read |
| `~s` | REGEX | Subject: matches |
| `~S` | — | Superseded |
| `~t` | REGEX | To: matches |
| `~T` | — | Tagged |
| `~u` | — | To subscribed mailing list |
| `~U` | — | Unread |
| `~v` | — | Collapsed thread |
| `~V` | — | Cryptographically verified |
| `~w` | REGEX | Newsgroups match |
| `~x` | REGEX | References: or In-Reply-To: matches |
| `~X` | RANGE | Number of attachments |
| `~y` | REGEX | X-Label: matches |
| `~Y` | REGEX | Tags match |
| `~z` | RANGE | Message size |
| `~#` | — | Broken thread |
| `~$` | — | Unreferenced message |
| `~=` | — | Duplicate (same Message-Id) |
| `~()` | PATTERN | Thread contains match |
| `~<()` | PATTERN | Parent matches |
| `~>()` | PATTERN | Child matches |

### Logical Operators

| Operator | Meaning |
|----------|---------|
| *(space)* | AND |
| `\|` | OR |
| `!` | NOT |
| `()` | Grouping |
| `^` | All addresses must match |

### Date Range Quick Reference

| Syntax | Example | Meaning |
|--------|---------|---------|
| `<Nd` | `<7d` | Within the last 7 days |
| `>Nd` | `>30d` | More than 30 days ago |
| `=Nd` | `=1d` | Exactly 1 day ago |
| `DD/MM/YYYY` | `15/6/2025` | Specific date |
| `YYYYMMDD` | `20250615` | Specific date (ISO 8601) |
| `DATE-DATE` | `1/1/2025-31/3/2025` | Date range |
| `*Nw` | `*2w` | ±2 weeks from today |

### Number Range Quick Reference

| Syntax | Example | Meaning |
|--------|---------|---------|
| `N` | `5` | Exactly 5 |
| `N-M` | `10-50` | Between 10 and 50 |
| `-N` | `-100` | Up to 100 |
| `N-` | `100-` | 100 or more |
| `<N` | `<10` | Less than 10 |
| `>N` | `>100` | Greater than 100 |
| `NK` / `NM` | `100K` / `5M` | Kilobytes / Megabytes (size only) |

### Alias Pattern Operators

| Pattern | Matches |
|---------|---------|
| `~f REGEX` | Alias name |
| `~t REGEX` | Alias addresses |
| `~c REGEX` | Alias comment |
| `~Y REGEX` | Alias tags |
