---
title: Conditional Expandos
description: Guide to conditional logic in NeoMutt format strings including if-else branches, date conditions, nesting, and practical examples
keywords: neomutt, expando, conditional, format string, if-else, date, boolean, nesting, index_format, status_format, sidebar_format, branching
---

# Conditional Expandos

Conditional expandos let you show different text depending on the properties
of a message, mailbox, or other context.  For example, you can display "New"
next to unread messages, show a count only when it's non-zero, or format
dates differently depending on how old the message is.

This guide starts with the basics and builds step by step toward
real-world format strings.

---

## The Basic Idea

A conditional expando asks a yes-or-no question about a value:

- **Is there a value?**  (Is the string non-empty?  Is the number non-zero?)
- **Yes →** show this text
- **No →** show that text (or nothing)

It looks like this:

```
%<X?yes-text&no-text>
```

Where `X` is any expando.

---

## Step 1: A Simple Condition

Let's start with the simplest case.  The expando `%n` is the count of new
messages.  Suppose you want to show the word "NEW" only when there are
new messages.

```neomuttrc
set status_format = "%f %<n?NEW>"
```

How it works:

| Part  | Meaning                                   |
|-------|-------------------------------------------|
| `%<`  | Start a conditional                       |
| `n`   | Test the `%n` expando (new message count) |
| `?`   | Separator: "if true, then…"               |
| `NEW` | Text to show when the condition is true   |
| `>`   | End of the conditional                    |

If there are new messages (`%n` is non-zero), NeoMutt shows `NEW`.
If there are no new messages (`%n` is zero), it shows nothing.

```
inbox NEW         ← 3 new messages
inbox             ← 0 new messages
```

---

## Step 2: True and False Branches

Add an `&` to provide alternative text for when the condition is false:

```neomuttrc
set status_format = "%<n?New mail!&No new mail>"
```

| Part          | Meaning              |
|---------------|----------------------|
| `%<n?`        | If `%n` is non-zero… |
| `New mail!`   | …show this           |
| `&`           | Otherwise…           |
| `No new mail` | …show this           |
| `>`           | End                  |

```
inbox New mail!       ← has new messages
inbox No new mail     ← no new messages
```

---

## Step 3: Using Expandos Inside Branches

The true and false branches aren't limited to plain text.  You can put
expandos inside them:

```neomuttrc
set status_format = "%f %<n?%n new messages&No new mail>"
```

Now `%n` inside the true branch is replaced with the actual count:

```
inbox 3 new messages  ← 3 new messages
inbox No new mail     ← 0 new messages
```

You can format the embedded expandos with widths and justification just
like normal:

```neomuttrc
set status_format = "%f %<n?%4n new>"
```

```
inbox    3 new        ← right-justified in 4 columns
```

---

## Step 4: Conditions on String Expandos

Conditions work on string expandos too.  A string is "true" when it's
non-empty, and "false" when it's empty.

The expando `%g` shows a message's tags.  Not every message has tags:

```neomuttrc
set index_format = "%s %<g?[%g]>"
```

```
Lunch on Friday? [important]     ← tagged message
Budget review                    ← no tags
```

The expando `%M` shows the number of hidden messages in a collapsed thread:

```neomuttrc
set index_format = "%<M?(%M hidden) >%s"
```

```
(5 hidden) Re: Team discussion   ← collapsed thread
Lunch on Friday?                  ← single message
```

---

## Step 5: Putting Conditions Side by Side

You can use multiple conditionals in the same format string.  Each one is
independent:

```neomuttrc
set status_format = "%f [Msgs:%m%<n? New:%n>%<d? Del:%d>%<t? Tag:%t>]"
```

This shows `New:`, `Del:`, and `Tag:` sections only when they're non-zero:

```
inbox [Msgs:42 New:3 Del:1]           ← 3 new, 1 deleted, 0 tagged
inbox [Msgs:42 New:3 Del:1 Tag:2]     ← 3 new, 1 deleted, 2 tagged
inbox [Msgs:42]                        ← nothing special
```

Each conditional decides independently whether to show its section.

---

## Step 6: Formatting the Whole Condition

You can apply a format specifier (width, justification) to the **entire
conditional**, not just to expandos inside it.  Put the format between `%`
and the `<`:

```neomuttrc
# The result of the conditional is right-justified in 20 columns
set status_format = "%20<n?%n new&No new>"
```

```
               3 new     ← right-justified in 20 columns
              No new     ← right-justified in 20 columns
```

```neomuttrc
# Left-justified in 15 columns, truncated if needed
set status_format = "%-15.15<n?%n new messages&none>"
```

The format specifier applies to the *output* of whichever branch is chosen.

---

## Step 7: Nesting Conditionals

A conditional branch can contain another conditional.  This lets you build
multi-level logic:

```neomuttrc
set status_format = "%<n?%<d?%n new, %d deleted&%n new>&No activity>"
```

Reading from the outside in:

1. **Outer condition:** Is `%n` (new count) non-zero?
   - **Yes →** check the inner condition
   - **No →** show "No activity"
2. **Inner condition:** Is `%d` (deleted count) non-zero?
   - **Yes →** show "3 new, 1 deleted"
   - **No →** show "3 new"

```
3 new, 1 deleted      ← new messages AND deleted messages
3 new                  ← new messages but nothing deleted
No activity            ← no new messages
```

:::{admonition} Keep nesting shallow
:class: tip

Deeply nested conditionals are hard to read.  One level of nesting is
common.  Two levels should be rare.  If you need more, consider simplifying
your format string.
:::

---

## Step 8: Date-Based Conditions

Date conditions are a special, powerful feature.  Instead of testing whether
a value is non-zero, they test whether a message's date falls within a time
period.

### Syntax

```
%<[PERIOD?true-text&false-text>
%<[COUNTPERIOD?true-text&false-text>
```

The condition is `[` followed by an optional count and a period letter:

| Letter | Period | Example | Meaning     |
|--------|--------|---------|-------------|
| `y`    | Year   | `[y`    | This year   |
| `m`    | Month  | `[m`    | This month  |
| `w`    | Week   | `[w`    | This week   |
| `d`    | Day    | `[d`    | Today       |
| `H`    | Hour   | `[H`    | This hour   |
| `M`    | Minute | `[M`    | This minute |

### "This" vs "Last N"

- **No count** (`[d`): means "this current period" — today, this week, this
  month, etc.  The cutoff is the *start* of the period (e.g. midnight for
  `[d`, Monday for `[w`, January 1st for `[y`).

- **With a count** (`[3d`): means "within the last N periods" — the last
  3 days, the last 2 weeks, etc.  The cutoff is exactly N periods ago from
  right now.

### Example: Show "Today" or the Date

```neomuttrc
set index_format = "%4C %Z %<[d?Today&%d> %-20.20n %s"
```

```
   1 N+ Today   Alice                Lunch on Friday?
   2  + Mar 19  Bob                  Re: Planning the team offsite
```

Messages from today show "Today".  Older messages show the date.

### Example: Short Date for Recent, Full Date for Old

```neomuttrc
set index_format = "%4C %Z %<[y?%[%b %d]&%[%Y-%m-%d]> %-20.20n %s"
```

Messages from this year show `Mar 20`.  Older messages show `2024-03-20`.

```
   1 N+ Mar 20  Alice                Lunch on Friday?
   2  + Mar 19  Bob                  Re: Planning the team offsite
  42 N  2024-11-05 Carol             Old thread
```

### Example: "Just now" for Messages from the Last Hour

```neomuttrc
set index_format = "%4C %<[1H?*new* &      >%<[d?%[%H:%M]&%[%b %d]> %-20.20n %s"
```

```
   1 *new*  14:30 Alice                Lunch on Friday?
   2        09:15 Bob                  Morning update
  42        Mar 19 Carol               Yesterday's thread
```

### Date Period Reference

| Condition | Meaning                    | Cutoff point           |
|-----------|----------------------------|------------------------|
| `[d`      | Today                      | Midnight today         |
| `[w`      | This week                  | Monday 00:00           |
| `[m`      | This month                 | 1st of the month 00:00 |
| `[y`      | This year                  | January 1st 00:00      |
| `[1d`     | Within the last 24 hours   | Exactly 24 hours ago   |
| `[3d`     | Within the last 3 days     | Exactly 72 hours ago   |
| `[2w`     | Within the last 2 weeks    | Exactly 14 days ago    |
| `[6m`     | Within the last 6 months   | Exactly 6 months ago   |
| `[1y`     | Within the last year       | Exactly 1 year ago     |
| `[30M`    | Within the last 30 minutes | Exactly 30 minutes ago |

---

## Step 9: Combining Conditions with Padding

Conditionals and padding work together naturally.  Padding fills the space
between fixed content and flexible content:

```neomuttrc
set status_format = "%f [%m msgs%<n? (%n new)>] %> %P"
```

The conditional `%<n?...>` only shows the new count when relevant, and the
hard-fill `%>` pushes the percentage to the right:

```
inbox [42 msgs (3 new)]                              100%
inbox [42 msgs]                                      100%
```

---

## Real-World Configurations

Here are complete, practical format strings that combine everything from
this guide.

### A Clean Status Bar

```neomuttrc
set status_format = " %f — %m msgs%<n? (%n new)>%<d? [%d deleted]>%<t? {%t tagged}> %> %P "
```

```
 inbox — 42 msgs (3 new) [1 deleted]                          100%
 sent — 128 msgs                                               50%
```

Breakdown:
- `%f` — folder name
- `%m` — total messages (always shown)
- `%<n? (%n new)>` — show new count only when non-zero
- `%<d? [%d deleted]>` — show deleted count only when non-zero
- `%<t? {%t tagged}>` — show tagged count only when non-zero
- `%>` — hard-fill with spaces
- `%P` — percentage position

### A Smart Index Format

```neomuttrc
set index_format = "%4C %Z %<[d? %[%H:%M]&%<[y?%[%b %d]&%[%Y-%m]>> %-20.20n %<M?(%3M) >%<g?[%g] >%s"
```

Breakdown:
- `%4C` — message number, 4 digits
- `%Z` — combined flags (new, replied, encrypted, etc.)
- Date with nested conditions:
  - Today → show time: `14:30`
  - This year → show month and day: `Mar 20`
  - Older → show year and month: `2024-11`
- `%-20.20n` — author name, left-justified, exactly 20 columns
- `%<M?(%3M) >` — show hidden thread count only when collapsed
- `%<g?[%g] >` — show tags only when present
- `%s` — subject (takes remaining space)

Result:

```
   1 N+  14:30 Alice                (  5) [urgent] Re: Team discussion
   2  + Mar 19 Bob                  Budget review
  42 N  2024-11 Carol                [archive] Old thread
 100    Mar 18 Dave                  Meeting tomorrow
```

### A Sidebar with Conditional Counts

```neomuttrc
set sidebar_format = "%D%*  %<n?%n>"
```

Mailboxes with new mail show the count.  Others show nothing:

```
inbox              3
sent
drafts             1
work/project
spam
```

### Terminal Title with Context

```neomuttrc
set ts_status_format = "NeoMutt: %f %<m?— %m messages>%<n? [%n NEW]>"
```

```
NeoMutt: inbox — 42 messages [3 NEW]       ← has messages
NeoMutt: drafts                              ← empty folder
```

### Icon That Changes with Mail Status

```neomuttrc
set ts_icon_format = "M%<n?AIL&ail>"
```

```
MAIL       ← new messages (uppercase)
Mail       ← no new messages (mixed case)
```

### Attachment List with Conditional Charset

```neomuttrc
set attach_format = "%u%D%I %t%4n %T%d %> [%.7m/%.10M, %.6e%<C?, %C>, %s]"
```

The `%<C?, %C>` part shows the charset only when present:

```
    1 [text/plain, utf-8, 1.2K]
    2 [application/pdf, 245K]          ← no charset (binary file)
```

### Mailbox Browser with Conditional New Count

```neomuttrc
set mailbox_folder_format = "%2C %<n?%6n&      > %6m %i"
```

Shows the new-message count when non-zero, or blank spaces to keep
alignment:

```
 1      3     42 inbox
 2             128 sent
 3      1      5 drafts
```

The `%<n?%6n&      >` conditional ensures the column is always 6 characters
wide — either a right-justified number or 6 spaces.

---

## Old-Style Syntax

NeoMutt also accepts an older syntax using `?` as both the opening and
closing delimiter:

```
%?X?true-text&false-text?
```

This is functionally identical to the new style:

```
%<X?true-text&false-text>
```

| New style            | Old style            |
|----------------------|----------------------|
| `%<n?%n new>`        | `%?n?%n new?`        |
| `%<n?%n new&No new>` | `%?n?%n new&No new?` |
| `%<[d?Today&%d>`     | `%?[d?Today&%d?`     |

The new style (`%<…>`) is recommended because it's easier to read — the
angle brackets clearly show where the conditional starts and ends.

---

## Condition Logic Summary

| Expando type | Condition is TRUE when…        | Condition is FALSE when…   |
|--------------|--------------------------------|----------------------------|
| Number       | Value is non-zero              | Value is zero              |
| String       | String is non-empty            | String is empty            |
| Date         | Date is within the time period | Date is outside the period |

---

## Quick Reference

```
CONDITIONAL SYNTAX
──────────────────
  %<X?true>                    Show text if X is true
  %<X?true&false>              Show text if true, other text if false

  %<[d?true&false>             Date: today
  %<[3d?true&false>            Date: within last 3 days
  %<[m?true&false>             Date: this month

DATE PERIODS
────────────
  y = year    m = month    w = week
  d = day     H = hour     M = minute

  No count = "this" period (today, this week, this month)
  With count = "last N" periods (last 3 days, last 2 weeks)

CONDITION TRUTH TABLE
─────────────────────
  Number:  non-zero = true,  zero = false
  String:  non-empty = true, empty = false
  Date:    within period = true, outside = false

NESTING
───────
  %<X?%<Y?both&only-X>&neither>
  └── outer condition on X
       └── inner condition on Y

OLD STYLE (deprecated)
──────────────────────
  %?X?true?            equivalent to  %<X?true>
  %?X?true&false?      equivalent to  %<X?true&false>
```

---

## See Also

- [Formatting Expandos](expando-format-guide.md) — how to control width,
  alignment, and padding
- Expando Syntax Reference — technical reference
- [NeoMutt Manual](https://neomutt.org/guide/) — full documentation
