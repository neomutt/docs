---
title: Expando Syntax
description: Technical reference for NeoMutt expando format string syntax including short and long names, format specifiers, and padding
keywords: neomutt, expando, format string, syntax, short name, long name, format specifier, width, truncation, padding, justification, index_format, status_format
---

# Expando Syntax — Format Strings

NeoMutt uses printf()-style format strings called **expandos** to control
the display of the index, status bar, sidebar, compose screen, and other
UI elements.  Each expando is a `%` followed by a letter (or long name)
that is replaced at runtime with a value from the current message,
mailbox, or context.

---

## Basic Syntax

```
%X          short name  (one or two characters)
%{long-name}  long name (lowercase, digits, hyphens, in braces)
%%          literal percent sign
```

The short name `%s` and long name `%{subject}` are interchangeable — they
refer to the same expando.

---

## Short Names vs Long Names

Every expando has a short name.  Most also have a descriptive long name.

| Short | Long | Meaning |
|-------|------|---------|
| `%a` | `%{from}` | From address |
| `%A` | `%{reply-to}` | Reply-To address |
| `%b` | `%{mailbox-name}` | Mailbox name |
| `%c` | `%{size}` | Message size |
| `%C` | `%{number}` | Message number |
| `%d` | `%{date-format}` | Date (strftime via `$date_format`) |
| `%e` | `%{thread-number}` | Thread number |
| `%E` | `%{thread-count}` | Thread count |
| `%f` | `%{from-full}` | From (full address) |
| `%F` | `%{sender}` | Smart sender (uses Reply-To or From) |
| `%g` | `%{tags}` | Tags |
| `%i` | `%{message-id}` | Message-Id |
| `%l` | `%{lines}` | Line count |
| `%n` | `%{name}` | Author's real name |
| `%s` | `%{subject}` | Subject |
| `%S` | `%{flag-chars}` | Message flag characters |
| `%t` | `%{to}` | To address |
| `%X` | `%{attachment-count}` | Attachment count |
| `%Z` | `%{combined-flags}` | Combined flag characters |
| `%cr` | `%{body-characters}` | Body character count (two-char short name) |
| `%zc` | `%{crypto-flags}` | Crypto flags |
| `%zs` | `%{status-flags}` | Status flags |
| `%zt` | `%{message-flags}` | Message flags |

Long names use only lowercase letters, digits, and hyphens, enclosed in
braces: `%{long-name}`.

---

## Format Specifiers

A format specifier goes between `%` and the expando name:

```
%[justification][0][min_cols][.max_cols][_]X
```

### Justification

| Flag | Justification | Padding position |
|------|---------------|------------------|
| *(none)* | Right | Left side padded |
| `-` | Left | Right side padded |
| `=` | Center | Both sides padded |

### Minimum Width (`min_cols`)

If the value is shorter than `min_cols`, it is padded (with spaces by
default) to fill the minimum width.

```neomuttrc
# Right-justify subject in 30 columns (pad on the left)
set index_format = "%30s"

# Left-justify subject in 30 columns (pad on the right)
set index_format = "%-30s"

# Center subject in 30 columns
set index_format = "%=30s"
```

### Maximum Width / Truncation (`.max_cols`)

If the value is longer than `max_cols`, it is truncated.

```neomuttrc
# Truncate subject to at most 40 columns
set index_format = "%.40s"

# Left-justify in exactly 30 columns (min=30, max=30)
set index_format = "%-30.30s"
```

### Zero Padding (`0`)

A `0` after the justification flag uses `0` instead of spaces for padding.
This is mainly useful for numeric expandos.  Ignored with left-justification.

```neomuttrc
# Zero-pad message number to 5 digits: "00042"
set index_format = "%05C"
```

### Lowercase Modifier (`_`)

A trailing `_` before the letter forces the output to lowercase.

```neomuttrc
# Show subject in lowercase
set index_format = "%_s"
```

### Combined Examples

```neomuttrc
# Right-justified subject, min 20 cols
set index_format = "%20s"

# Left-justified subject, exactly 30 cols
set index_format = "%-30.30s"

# Truncate from address to 15 cols, no minimum
set index_format = "%.15a"

# Center name in 20 columns
set index_format = "%=20n"

# Long name with formatting: left-justify, 30 cols
set index_format = "%-30{subject}"
```

---

## Padding

Padding expandos control how a format string fills the full width of the
screen.  They split the format string into a **left side** and a
**right side**, with padding filling the gap between them.

### Three Padding Types

| Expando | Long Name | Type | Description |
|---------|-----------|------|-------------|
| `%\|X` | `%{padding-eol:X}` | End-of-line | Fill from left content to the end of the line |
| `%>X` | `%{padding-hard:X}` | Hard fill | Left side preserved; right side truncated if needed |
| `%*X` | `%{padding-soft:X}` | Soft fill | Right side preserved; left side truncated if needed |

The character `X` after the padding symbol is the **fill character**.
If omitted, a space is used.

> **Note:** Padding expandos cannot have format specifiers (no widths or
> justification) and cannot be used as conditions.

### End-of-Line Padding (`%|X`)

Renders the left side, then fills the remaining screen width with the
pad character.  Nothing appears after the padding.

```
[---- left content ----][XXXXXXXXXXXXXXXX]
```

```neomuttrc
# Fill the rest of the line with dashes after the subject
set status_format = "Subject: %s %|-"
```

### Hard-Fill Padding (`%>X`)

The left side is "hard" — it is rendered first and preserved.  The right
side gets whatever space remains.  If the screen is too narrow, the
right side is truncated.

```
[---- left (preserved) ----][XXX][---- right (truncated) ----]
```

```neomuttrc
# Left: flags + name.  Right: subject.  Gap filled with spaces.
set index_format = "%Z %d %-20.20n %> %s"
```

### Soft-Fill Padding (`%*X`)

The right side is "hard" — it is rendered first and preserved.  The left
side gets whatever space remains.  If the screen is too narrow, the
left side is truncated.

```
[---- left (truncated) ----][XXX][---- right (preserved) ----]
```

```neomuttrc
# Right side (percentage) is preserved; left side truncated if needed
set status_format = "%f %m msgs %* %P"
```

---

## Real-World Examples

### `$index_format`

```neomuttrc
# A practical index format
set index_format = "%4C %Z %d %-20.20n %s"
#                   ^    ^  ^  ^          ^
#                   |    |  |  |          subject (no limit)
#                   |    |  |  name, left-justified, 20 cols
#                   |    |  date
#                   |    combined flags
#                   message number, 4 digits

# With padding to push the subject to the right
set index_format = "%4C %Z %d %-20.20n %> %s"

# Using long names
set index_format = "%4{number} %{combined-flags} %{date-format} %-20.20{name} %> %{subject}"
```

### `$status_format`

```neomuttrc
# Show folder, message counts, and percentage
set status_format = "%f: %m msgs, %n new %> %P"

# With soft-fill to preserve the percentage on the right
set status_format = "Folder=%f [Msgs:%m New:%n] %* (%P)"
```

---

## Quick Reference

### Format Specifier Syntax

```
%[- | =][0][min_cols][.max_cols][_]X
%[- | =][0][min_cols][.max_cols][_]{long-name}
```

| Component | Values | Default | Description |
|-----------|--------|---------|-------------|
| Justification | `-`, `=`, *(none)* | Right | Left, Center, Right |
| Leader | `0` | Space | Pad character |
| `min_cols` | Number | 0 | Minimum column width |
| `.max_cols` | `.Number` | Unlimited | Maximum column width |
| `_` | `_` | Off | Force lowercase |

### Padding

| Expando | Name | Left side | Right side |
|---------|------|-----------|------------|
| `%\|X` | EOL fill | Kept | *(none)* |
| `%>X` | Hard fill | Kept | Truncated |
| `%*X` | Soft fill | Truncated | Kept |

