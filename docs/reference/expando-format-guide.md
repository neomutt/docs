---
title: Formatting Expandos
description: Guide to controlling column width, alignment, truncation, zero-padding, and fill padding in NeoMutt format strings
keywords: neomutt, expando, format string, width, padding, justification, alignment, truncation, zero-padding, lowercase, hard-fill, soft-fill, index_format, status_format
---

# Formatting Expandos

NeoMutt uses **expandos** — short codes starting with `%` — to build the format strings that control how the message list, status bar, sidebar, and other parts of the interface look.
Each expando is replaced at runtime with a real value: a sender's name, a subject line, a date, a message count, and so on.

This guide explains how to format those expandos: how to set column widths,
align text, truncate long values, and use padding to fill the screen.

---

## What Is an Expando?

An expando is a placeholder.
You write it in a format string, and NeoMutt replaces it with the appropriate value.

For example, in the index (message list), `%s` means "the subject" and `%n` means "the author's name".
So this format string:

```neomuttrc
set index_format = "%n — %s"
```

might display as:

```
Alice — Lunch on Friday?
```

### Short Names and Long Names

Every expando has a **short name** — one or two characters after `%`.
Most also have a **long name** enclosed in braces.
The two forms are interchangeable:

| Short Name | Long Name             | Meaning          |
|------------|-----------------------|------------------|
| `%s`       | `%{subject}`          | Subject          |
| `%n`       | `%{name}`             | Author's name    |
| `%a`       | `%{from}`             | From address     |
| `%C`       | `%{number}`           | Message number   |
| `%c`       | `%{size}`             | Message size     |
| `%d`       | `%{date-format}`      | Date             |
| `%Z`       | `%{combined-flags}`   | Flag characters  |
| `%l`       | `%{lines}`            | Line count       |
| `%X`       | `%{attachment-count}` | Attachment count |

These two lines produce identical results:

```neomuttrc
set index_format = "%C %n %s"
set index_format = "%{number} %{name} %{subject}"
```

Long names are easier to read in complex format strings.
Short names are quicker to type.
Use whichever you prefer — or mix them freely.

### Literal Percent Sign

To display an actual `%` character, use `%%`:

```neomuttrc
set status_format = "100%% complete"
```

---

## Column Width

By default, an expando takes up exactly as much space as its value needs.
A short subject uses fewer columns than a long one.
This makes columns ragged and hard to scan:

```
  1 Alice — Hi
  2 Bob — Re: Planning the team offsite for next quarter
  3 Carol — Meeting
```

To fix this, you set a **minimum width** and a **maximum width** to force
every value into the same number of columns.

### Minimum Width

Put a number between `%` and the expando letter.
NeoMutt pads the value with spaces if it's shorter than the minimum:

```neomuttrc
# Give the subject at least 30 columns
set index_format = "%30s"

# Give the name at least 15 columns
set index_format = "%15n"
```

With a long name:

```neomuttrc
set index_format = "%30{subject}"
set index_format = "%15{name}"
```

### Maximum Width (Truncation)

Put a dot and a number to set a maximum.
NeoMutt truncates the value if it's longer:

```neomuttrc
# Truncate the subject to at most 40 columns
set index_format = "%.40s"

# Truncate the name to at most 20 columns
set index_format = "%.20{name}"
```

### Both Together

Combine minimum and maximum to create a fixed-width column.
This is the most common pattern — it makes every row line up neatly:

```neomuttrc
# Name in exactly 20 columns (pad if short, truncate if long)
set index_format = "%20.20n"

# Subject in exactly 40 columns
set index_format = "%40.40{subject}"
```

An `index_format` with fixed columns:

```neomuttrc
set index_format = "%4C %Z %10.10d %20.20n %s"
#                   ^^^  ^  ^^^^^^^  ^^^^^^^  ^
#                   |    |  |        |        subject (no limit)
#                   |    |  |        name: exactly 20 columns
#                   |    |  date: exactly 10 columns
#                   |    flags (no width — always short)
#                   message number: at least 4 digits
```

Result:

```
   1 N+ 2025-03-20 Alice                Lunch on Friday?
   2  + 2025-03-19 Bob                  Re: Planning the team offsite
  42 N  2025-03-18 Carol                Meeting tomorrow
 100    2025-03-17 Dave                  Budget review
```

---

## Justification (Alignment)

By default, values are **right-justified** — padded on the left side.
You can change this with a flag immediately after `%`:

| Flag     | Alignment | Padding goes… |
|----------|-----------|---------------|
| *(none)* | Right     | on the left   |
| `-`      | Left      | on the right  |
| `=`      | Centre    | on both sides |

### Right-Justified (Default)

```neomuttrc
# Right-justify the name in 20 columns
set index_format = "%20n"
```

```
               Alice
                 Bob
               Carol
```

Right justification is natural for numbers — digits line up on the right:

```neomuttrc
# Right-justify the message number in 5 columns
set index_format = "%5C"
```

```
    1
   42
  100
```

### Left-Justified

A `-` flag left-justifies the value — padding goes on the right.
This is the natural choice for names, addresses, and subjects:

```neomuttrc
# Left-justify the name in 20 columns
set index_format = "%-20n"
```

```
Alice
Bob
Carol
```

With a long name:

```neomuttrc
set index_format = "%-20{name}"
```

### Centre-Justified

An `=` flag centres the value:

```neomuttrc
# Centre the subject in 40 columns
set index_format = "%=40s"
```

```
          Lunch on Friday?
    Re: Planning the team offsite
            Meeting tomorrow
```

### Combining Justification with Width

Justification works with both minimum and maximum widths:

```neomuttrc
# Left-justified name, exactly 20 columns
set index_format = "%-20.20n"

# Right-justified message number, at least 4 digits
set index_format = "%4C"

# Centre-justified subject in 50 columns, truncated if needed
set index_format = "%=50.50s"
```

A practical `index_format`:

```neomuttrc
set index_format = "%4C %Z %-12.12d %-20.20n %s"
```

```
   1 N+ Mar 20       Alice                Lunch on Friday?
   2  + Mar 19       Bob                  Re: Planning the team offsite
  42 N  Mar 18       Carol                Meeting tomorrow
```

---

## Zero-Padding

For numeric expandos, you can pad with `0` instead of spaces by placing a
`0` after the `%` (or after the justification flag):

```neomuttrc
# Pad message number with zeros: 00001, 00042, 00100
set index_format = "%05C"

# With a long name
set index_format = "%05{number}"
```

```
00001
00042
00100
```

:::{admonition} Zero-padding and left justification
:class: note

Zero-padding is ignored when combined with left-justification (`-`).
A left-justified number is padded with spaces on the right, never with zeros.
:::

---

## Lowercase Modifier

A trailing `_` (underscore) before the expando letter forces the output
to lowercase:

```neomuttrc
# Subject in lowercase
set index_format = "%_s"
```

```
re: lunch on friday?
re: planning the team offsite
meeting tomorrow
```

This can be combined with other formatting:

```neomuttrc
# Left-justified, 30 columns, lowercase
set index_format = "%-30_s"

# With a long name
set index_format = "%-30_{subject}"
```

---

## The Full Format Specifier

Putting it all together, the complete syntax between `%` and the expando
name is:

```
%[justification][zero][min_width][.max_width][lowercase]EXPANDO
```

| Component     | Values                   | Default   | |---------------|--------------------------|-----------| | Justification | `-` (left), `=` (centre) | Right     | | Zero-padding  | `0`                      | Spaces    | | Minimum width | A number (e.g.
`20`)     | 0 (none)  | | Maximum width | `.` then a number        | Unlimited | | Lowercase     | `_`                      | Off       | | Expando       | Letter or `{long-name}`  | —         |

### More Combined Examples

```
# Right-justify, min 5 columns
%5C              %5{number}

# Left-justify, exactly 20 columns
%-20.20n         %-20.20{name}

# Truncate to 40 columns (no minimum)
%.40s            %.40{subject}

# Centre in 30 columns
%=30s            %=30{subject}

# Zero-padded number, 4 digits
%04C             %04{number}

# Left-justified, max 15, lowercase
%-15_a           %-15_{from}
```

---

## Padding

Padding expandos are special.
Instead of inserting a value, they fill space — they push content apart, draw separator lines, or ensure the right side of the screen is used.

Every format string is rendered within a fixed width (usually your terminal width).
A padding expando divides the format string into a **left side** and a **right side**, then fills the gap between them with a character.

### The Three Padding Types

| Expando | Long Name           | Name      | Left side | Right side  |
|---------|---------------------|-----------|-----------|-------------|
| `%\|X`  | `%{padding-eol:X}`  | EOL fill  | Kept      | *(nothing)* |
| `%>X`   | `%{padding-hard:X}` | Hard fill | Kept      | Truncated   |
| `%*X`   | `%{padding-soft:X}` | Soft fill | Truncated | Kept        |

The character `X` after the padding symbol is the **fill character**.
If you omit it (or use a space), the gap is filled with spaces.

### End-of-Line Padding (`%|X`)

Renders the left side, then fills from there to the end of the screen with the fill character.
Nothing appears after the padding.

```
[--- left content ---][XXXXXXXXXXXXXXXXXX]
```

Use this to draw a line across the rest of the screen:

```neomuttrc
# Fill the rest of the line with dashes
set status_format = "Folder: %f  Msgs: %m %|-"
```

```
Folder: inbox  Msgs: 42 ----------------------------
```

```neomuttrc
# Fill with equals signs
set compose_format = "Compose: %l bytes %|="
```

```
Compose: 1234 bytes =============================
```

### Hard-Fill Padding (`%>X`)

The left side is "hard" — it is always shown in full.
The right side gets whatever space remains.
If the screen is too narrow for both, the **right side is truncated**.

```
[--- left (kept) ---][XXXXX][--- right (truncated if needed) ---]
```

This is the most common padding type.
Use it when the left side is more important:

```neomuttrc # Left: flags, date, name.
Right: subject.
# The subject is truncated if the screen is narrow.
set index_format = "%4C %Z %d %-20.20n %> %s" ```

On a wide screen:

```
   1 N+ Mar 20 Alice                 Lunch on Friday?
```

On a narrow screen (the subject gets cut):

```
   1 N+ Mar 20 Alice                 Lun…
```

With a visible fill character:

```neomuttrc
# Use dots as filler between name and subject
set index_format = "%-20.20n %>.%s"
```

```
Alice                ......Lunch on Friday?
Bob                  ..Re: Planning the team offsite
```

### Soft-Fill Padding (`%*X`)

The opposite of hard fill.
The right side is "hard" — always shown in full.
The left side gets whatever space remains.
If the screen is too narrow for both, the **left side is truncated**.

```
[--- left (truncated if needed) ---][XXXXX][--- right (kept) ---]
```

Use this when the right side is more important:

```neomuttrc
# Right side (percentage) is always visible
set status_format = "%f — %m messages %* (%P)"
```

On a wide screen:

```
inbox — 42 messages                           (strstr100%)
```

On a narrow screen (the folder path gets cut):

```
…ail/inbox — 42 messages (100%)
```

### Choosing the Right Padding

| You want…                             | Use           |
|---------------------------------------|---------------|
| Fill to end of line, nothing after    | `%\|X` (EOL)  |
| Left side kept, right side expendable | `%>X`  (Hard) |
| Right side kept, left side expendable | `%*X`  (Soft) |

### Padding Rules

- Only **one** padding expando per format string.
  If you use more than one, only the first takes effect.
- Padding expandos **cannot** have format specifiers (no widths or justification).
- Padding expandos **cannot** be used inside conditions.

---

## Putting It All Together

Here are complete, realistic format strings that combine everything from
this guide.

### Message List (`$index_format`)

A clean, aligned message list with fixed-width columns and a flexible
subject:

```neomuttrc
set index_format = "%4C %Z %<[y?%[%b %d]&%[%Y-%m]> %-20.20n %> %s"
```

```
   1 N+ Mar 20 Alice                 Lunch on Friday?
   2  + Mar 19 Bob                   Re: Planning the team offsite
  42 N  2024-11 Carol                 Old thread
```

Using long names for readability:

```neomuttrc
set index_format = "%4{number} %{combined-flags} %{date-format} %-20.20{name} %> %{subject}"
```

### Status Bar (`$status_format`)

NeoMutt's default status format uses conditionals and padding:

```neomuttrc
set status_format = "-%r-NeoMutt: %D [Msgs:%m%<n? New:%n>%<d? Del:%d>%<t? Tag:%t>]-%>-(%P)---"
```

```
--NeoMutt: inbox [Msgs:42 New:3 Del:1]--------------------(strstr100%)---
```

A simpler alternative:

```neomuttrc
set status_format = " %f — %m msgs %<n?(%n new) >%>  %P "
```

```
 inbox — 42 msgs (3 new)                               100%
```

### Sidebar (`$sidebar_format`)

The default sidebar format uses soft-fill to keep the count visible:

```neomuttrc
set sidebar_format = "%D%*  %n"
```

```
inbox              3
sent
drafts             1
work/project       12
```

### Pager (`$pager_format`)

```neomuttrc
set pager_format = "-%Z- %C/%m: %-20.20n   %s%*  -- (%P)"
```

```
-N+- 1/42: Alice                  Lunch on Friday?  -- (100%)
```

### Attachment List (`$attach_format`)

```neomuttrc
set attach_format = "%u%D%I %t%4n %T%d %> [%.7m/%.10M, %.6e%<C?, %C>, %s]"
```

### Alias List (`$alias_format`)

```neomuttrc
set alias_format = "%3i %f%t %-15a %-56A | %C%> %Y"
```

---

## Quick Reference Card

### Format Specifier

```
%[-|=][0][min][.max][_]X        short name
%[-|=][0][min][.max][_]{name}   long name
%%                               literal %
```

### Justification

| Flag | Alignment | Example | Result (width 10) |
|------|-----------|---------|-------------------|
| —    | Right     | `%10s`  | `···· Hello`      |
| `-`  | Left      | `%-10s` | `Hello ····`      |
| `=`  | Centre    | `%=10s` | `·· Hello ··`     |

*(dots represent spaces)*

### Width and Truncation

| Spec      | Meaning                   | Example        |
|-----------|---------------------------|----------------|
| `%20n`    | At least 20 columns       | Pad if short   |
| `%.30n`   | At most 30 columns        | Cut if long    |
| `%20.30n` | Between 20 and 30 columns | Pad or cut     |
| `%20.20n` | Exactly 20 columns        | Always 20 wide |

### Padding

| Expando | Effect                               |
|---------|--------------------------------------|
| `%>X`   | Hard fill — left kept, right trimmed |
| `%*X`   | Soft fill — right kept, left trimmed |
| `%\|X`  | EOL fill — fill to end of line       |

Where `X` is the fill character (space if omitted).

---

## See Also

- [Conditional Expandos](expando-conditional-guide.md) — how to show different text based on message properties
- Expando Syntax Reference — technical reference
- [NeoMutt Manual](https://neomutt.org/guide/) — full documentation
