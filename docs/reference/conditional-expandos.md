---
title: Conditional Expandos
description: XXX
---

# Conditional Expandos — Step by Step

Conditional expandos let a format string display different text depending
on whether an expando has a value.  This tutorial builds up from simple
cases to practical real-world configurations.

---

## Step 1 — The Simplest Conditional

A conditional tests an expando and shows text only when it is "true."

An expando is **true** when:
- A numeric expando is non-zero (e.g. attachment count > 0)
- A string expando is non-empty (e.g. subject is set)

An expando is **false** when:
- A numeric expando is zero
- A string expando is empty

### Syntax

```
%<X?true-text>
```

- `%<` opens the conditional
- `X` is the expando to test
- `?` separates the condition from the true-text
- `>` closes the conditional

### Example

Show "Flagged" only if the message is flagged (`%F` is non-zero):

```neomuttrc
set index_format = "%C %<F?Flagged> %s"
```

| Message state | Result |
|---------------|--------|
| Flagged | `42 Flagged Meeting notes` |
| Not flagged | `42  Meeting notes` |

---

## Step 2 — Adding an Else Clause

The `&` separator adds a false-text branch.

### Syntax

```
%<X?true-text&false-text>
```

### Example

Show "Flagged" or "Normal":

```neomuttrc
set index_format = "%C %<F?Flagged&Normal> %s"
```

| Message state | Result |
|---------------|--------|
| Flagged | `42 Flagged Meeting notes` |
| Not flagged | `42 Normal Meeting notes` |

---

## Step 3 — Using Expandos Inside Branches

The true-text and false-text can contain any expandos, not just literal text.

### Example

If there are attachments, show the count; otherwise show nothing:

```neomuttrc
set index_format = "%C %s %<X?[%X att]>"
```

| Attachments | Result |
|-------------|--------|
| 3 | `42 Meeting notes [3 att]` |
| 0 | `42 Meeting notes ` |

Show the count or a dash:

```neomuttrc
set index_format = "%C %s %<X?%X&->"
```

| Attachments | Result |
|-------------|--------|
| 3 | `42 Meeting notes 3` |
| 0 | `42 Meeting notes -` |

---

## Step 4 — Formatting the Conditional Output

A format specifier before the `<` applies to the **entire output** of the
conditional (whichever branch is taken), not to the condition itself.

### Syntax

```
%[format]<X?true-text&false-text>
```

### Example

Left-justify the result in 10 columns:

```neomuttrc
set index_format = "%C %-10<F?Flagged&Normal> %s"
```

| Message state | Result (padded to 10) |
|---------------|-----------------------|
| Flagged | `42 Flagged    Meeting notes` |
| Not flagged | `42 Normal     Meeting notes` |

---

## Step 5 — Old Style Syntax

NeoMutt also supports the original Mutt conditional syntax using `?` delimiters:

```
%?X?true-text&false-text?
```

This is equivalent to the new style `%<X?true-text&false-text>`.

### Comparison

| New style | Old style |
|-----------|-----------|
| `%<F?Flagged>` | `%?F?Flagged?` |
| `%<F?Flagged&Normal>` | `%?F?Flagged&Normal?` |
| `%<X?%X att&no att>` | `%?X?%X att&no att?` |

Both styles work identically.  The new style (`< >`) is recommended for
readability.

---

## Step 6 — Conditional Dates

Date expandos support time-based conditions.  Instead of testing whether a
value exists, they test whether a date falls within a time period.

### Syntax

```
%<[Np?true-text&false-text>
```

- `N` is a number (optional; if omitted, means "this" period)
- `p` is a period character:

| Period | Meaning |
|--------|---------|
| `y` | Year |
| `m` | Month |
| `w` | Week |
| `d` | Day |
| `H` | Hour |
| `M` | Minute |

### How It Works

- `%<[1d?...>` — true if the message date is within the last 1 day
- `%<[2w?...>` — true if the message date is within the last 2 weeks
- `%<[d?...>` — true if the message date is "today" (this day)
- `%<[m?...>` — true if the message date is "this month"
- `%<[y?...>` — true if the message date is "this year"

### Example

Show time for today's messages, date for older ones:

```neomuttrc
set index_format = "%C %<[1d?%[%H:%M]&%[%b %d]> %-20.20n %s"
```

| Message date | Result |
|--------------|--------|
| Today, 14:30 | `42 14:30 Alice Jones Meeting notes` |
| March 15 | `42 Mar 15 Alice Jones Meeting notes` |

A three-level date display:

```neomuttrc
set index_format = "%C %<[1d?%[%H:%M]&%<[1y?%[%b %d]&%[%Y-%m]>> %-20.20n %s"
```

| Message date | Result |
|--------------|--------|
| Today | `42 14:30 ...` |
| This year | `42 Mar 15 ...` |
| Older | `42 2023-06 ...` |

---

## Step 7 — Nesting Conditionals

Conditionals can be nested inside each other's branches.

### Example

Two-level nesting: if flagged, show the flag; then if new, add a marker:

```neomuttrc
set index_format = "%C %<F?%<N?F+N&F>&%<N?N& >> %s"
```

| State | Result |
|-------|--------|
| Flagged + New | `42 F+N Meeting notes` |
| Flagged only | `42 F Meeting notes` |
| New only | `42 N Meeting notes` |
| Neither | `42   Meeting notes` |

---

## Step 8 — Practical Configurations

### A Complete `$index_format`

```neomuttrc
set index_format = "%4C %Z %<[1d?%[%H:%M]&%<[1y?%[%b %d]&%[%Y-%m]>> %-20.20n %<M?(%M)&   > %s %> %<X?[%X]>"
#                   |    |  |                                         |          |           |       |
#                   |    |  |                                         |          |           |       attachment count (if any)
#                   |    |  |                                         |          |           padding
#                   |    |  |                                         |          thread count (if collapsed)
#                   |    |  |                                         author name
#                   |    |  smart date (time/date/year-month)
#                   |    combined flags
#                   message number
```

### A Status Bar with Conditionals

```neomuttrc
set status_format = "%f [Msgs:%m%<n? New:%n>%<d? Del:%d>%<F? Flag:%F>] %> (%P)"
```

This shows New/Del/Flag counts only when non-zero:

| State | Result |
|-------|--------|
| 5 new, 2 flagged | `INBOX [Msgs:42 New:5 Flag:2] (50%)` |
| No new, no flags | `INBOX [Msgs:42] (50%)` |

---

## Quick Reference

### Syntax

| Style | True only | True + False |
|-------|-----------|--------------|
| New | `%<X?true>` | `%<X?true&false>` |
| Old | `%?X?true?` | `%?X?true&false?` |
| Date | `%<[Np?true>` | `%<[Np?true&false>` |
| Formatted | `%-10<X?true&false>` | |

### Truthiness

| Type | True | False |
|------|------|-------|
| Number | Non-zero | Zero |
| String | Non-empty | Empty |
| Date condition | Within period | Outside period |

### Date Period Characters

| Char | Period |
|------|--------|
| `y` | Year |
| `m` | Month |
| `w` | Week |
| `d` | Day |
| `H` | Hour |
| `M` | Minute |

