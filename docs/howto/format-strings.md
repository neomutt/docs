---
title: Format Strings
description: Customise index, status bar, and other displays using format strings, conditionals, filters, padding, and dynamic hooks
keywords: format strings, index_format, status_format, expandos, conditionals, nested-if, cond-date, initials, index-format-hook, padding, filters, width, justification, centering, strftime, size_show_bytes, pager_format
---

# Format Strings

## Basic Usage

Format strings are a general concept you'll find in several locations through the NeoMutt configuration, especially in the `$index_format`, `$pager_format`, `$status_format`, and other related variables.

The most basic format string element is a percent symbol followed by another character.
For example, `%s` represents a message's Subject: header in the `$index_format` variable.
The "expandos" available are documented with each format variable, but there are general modifiers available with all formatting expandos, too.

### Width and Justification Modifiers

Some of the modifiers are borrowed right out of C.
These are the `[-]m.n` modifiers, as in `%-12.12s`.
These modifiers allow you to specify the minimum and maximum size of the resulting string, as well as its justification.
If the `-` sign follows the percent, the string will be left-justified instead of right-justified.
If there's a number immediately following that, it's the minimum amount of space the formatted string will occupy — if it's naturally smaller than that, it will be padded out with spaces.
If a decimal point and another number follow, that's the maximum space allowable — the string will not be permitted to exceed that width, no matter its natural size.
Each of these three elements is optional, so that all these are legal format strings: `%-12s`, `%4c`, `%.15F` and `%-12.15L`.

### Centering

NeoMutt adds some other modifiers to format strings.
If you use an equals symbol (`=`) as a numeric prefix (like the minus above), it will force the string to be centered within its minimum space range.
For example, `%=14y` will reserve 14 characters for the %y expansion — that's the set of message keywords (formerly X-Label).
If the expansion results in a string less than 14 characters, it will be centered in a 14-character space.

### Case and Character Modifiers

There are two very little-known modifiers that affect the way that an expando is replaced.
If there is an underline (`_`) character between any format modifiers and the expando letter, it will expand in all lower case.
And if you use a colon (`:`), it will replace all decimal points with underlines.

## Conditionals

Depending on the format string variable, some of its sequences can be used to optionally print a string if their value is nonzero.
To optionally print a string based upon one of the above sequences, the following construct is used:

```
%<sequence_char?optional_string>
```

where *sequence_char* is an expando, and *optional_string* is the string you would like printed if *sequence_char* is nonzero. *optional_string* may contain other sequences as well as normal text, but you may not nest optional strings.

Here is an example illustrating how to optionally print the number of new messages (`%n`) in a mailbox in `$status_format`:

```
%<n?%n new messages>
```

You can also switch between two strings using the following construct:

```
%<sequence_char?if_string&else_string>
```

If the value of *sequence_char* is non-zero, *if_string* will be expanded, otherwise *else_string* will be expanded.

The conditional sequences can also be nested by using the `%<` and `>` operators.
The `%?` notation can still be used but requires quoting.
For example:

```
%<x?true&false>
%<x?%<y?%<z?xyz&xy>&x>&none>
```

## Filters

Any format string ending in a vertical bar (`|`) will be expanded and piped through the first word in the string, using spaces as separator. 
The string returned will be used for display.
If the returned string ends in %, it will be passed through the formatter a second time.
This allows the filter to generate a replacement format string including % expandos.

All % expandos in a format string are expanded before the script is called so that:

```neomuttrc
set status_format="script.sh '%r %f (%L)'|"
```

will make NeoMutt expand `%r`, `%f` and `%L` before calling the script.
The example also shows that arguments can be quoted: the script will receive the expanded string between the single quotes as the only argument.

A practical example is the `mutt_xtitle` script installed in the `samples` subdirectory of the NeoMutt documentation: it can be used as filter for `$status_format` to set the current terminal's title, if supported.

## Padding

In most format strings, NeoMutt supports different types of padding using special %-expandos:

### `%|X` — Fill to End of Line

When this occurs, NeoMutt will fill the rest of the line with the character `X`.
For example, filling the rest of the line with dashes:

```neomuttrc
set status_format = "%v on %h: %B: %<n?%n&no> new messages %|-"
```

### `%>X` — Right-Justify with Fill

This puts as many characters `X` in between two items so that the rest of the line will be right-justified.
For example, to put the version string and hostname on the right and fill the gap with spaces (note the space after `%>`):

```neomuttrc
set status_format = "%B: %<n?%n&no> new messages %> (%v on %h)"
```

### `%*X` — Soft-Fill (Priority Right-Justify)

Normal right-justification will print everything to the left of the `%>`, displaying padding and whatever lies to the right only if there's room.
By contrast, "soft-fill" gives priority to the right-hand side, guaranteeing space to display it and showing padding only if there's still room.
If necessary, soft-fill will eat text leftwards to make room for rightward text.
For example (note two spaces after `%*`):

```neomuttrc
set index_format="%4C %Z %{%b %d} %-15.15L (%<l?%4l&%4c>)%*  %s"
```

(how-bytes-size)=
## Bytes Size Display

Various format strings contain expandos that display the size of messages in bytes.
This includes `%s` in `$attach_format`, `%l` in `$compose_format`, `%s` in `$folder_format`, `%c` and `%cr` in `$index_format`, and `%l` and `%L` in `$status_format`.
There are four configuration variables that can be used to customise how the numbers are displayed:

- `$size_show_bytes` — display the number of bytes when the size is < 1 kilobyte. When unset, kilobytes will be displayed instead.
- `$size_show_mb` — display the number of megabytes when the size is >= 1 megabyte. When unset, kilobytes will be displayed instead.
- `$size_show_fractions` — display numbers with a single decimal place for values from 0 to 10 kilobytes, and 1 to 10 megabytes.
- `$size_units_on_left` — display the unit ("K" or "M") to the left of the number, instead of the right if unset.

These variables also affect size display in a few other places, such as progress indicators and attachment delimiters in the pager.

---

## Conditional Dates

This feature allows the format of dates in the index to vary based on how recent the message is.
This is especially useful in combination with the nested-if feature.

For example, using `%<[y?%<[d?%[%H:%M]&%[%m/%d]>&%[%y.%m]>` for the date in the `$index_format` will produce a display like:

```
   1   + 14.12 Grace Hall      (   13) Gulliver's Travels
   2   + 10/02 Callum Harrison (   48) Huckleberry Finn
   3     12:17 Rhys Lee        (   42) The Lord Of The Rings
```

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Conditional date formatting in the index

**Description:** The NeoMutt index view showing messages with different date
formats depending on age: today's messages showing time only (e.g. `12:17`),
this month's messages showing day (e.g. `10/02`), and older messages showing
year-month (e.g. `14.12`).

**Highlights:** How the same date column automatically adapts its format based on message age, saving space while keeping recent dates precise.
:::

### Potential Formatting Scheme

| Email Sent        | Format  | Example |
|-------------------|---------|---------|
| Today             | `%H:%M` | 13:23   |
| This Month        | `%a %d` | Thu 17  |
| This Year         | `%b %d` | Dec 10  |
| Older than 1 Year | `%m/%y` | 06/14   |

For an explanation of the date formatting strings, see [`strftime(3)`](exp-strftime).

NeoMutt's conditional format strings have the form (whitespace introduced for clarity):

```
%< TEST ? TRUE & FALSE >
```

The date tests are of the form:

```
%<[nX? TRUE & FALSE >
```

- "n" is an optional count (defaults to 1 if missing)
- "X" is the time period

#### Date Formatting Codes

| Letter | Time Period |
|--------|-------------|
| y      | Years       |
| m      | Months      |
| w      | Weeks       |
| d      | Days        |
| H      | Hours       |
| M      | Minutes     |

#### Example Date Tests

| Test   | Meaning              |
|--------|----------------------|
| `%[y`  | This year            |
| `%[1y` | This year            |
| `%[6m` | In the last 6 months |
| `%[w`  | This week            |
| `%[d`  | Today                |
| `%[4H` | In the last 4 hours  |

### Example 1 — One-Condition Test

| Test   | Date Range | Format String | Example    |
|--------|------------|---------------|------------|
| `%[1m` | This month | `%[%b %d]`    | Dec 10     |
|        | Older      | `%[%Y-%m-%d]` | 2015-04-23 |

The `$index_format` string would contain:

```
%<[1m?%[%b %d]&%[%Y-%m-%d]>
```

Reparsed for clarity:

```
%<[1m?        &           >

      %[%b %d] %[%Y-%m-%d]
```

### Example 2 — Three-Condition Test

| Test  | Date Range | Format String | Example |
|-------|------------|---------------|---------|
| `%[d` | Today      | `%[%H:%M ]`   | 12:34   |
| `%[m` | This month | `%[%a %d]`    | Thu 12  |
| `%[y` | This year  | `%[%b %d]`    | Dec 10  |
|       | Older      | `%[%m/%y ]`   | 06/15   |

The `$index_format` string would contain:

```
%<[y?%<[m?%<[d?%[%H:%M ]&%[%a %d]>&%[%b %d]>&%[%m/%y ]>
```

Reparsed for clarity:

```
%<[y?                                       &%[%m/%y ]>  Older
     %<[m?                        &%[%b %d]>             This year
          %<[d?         &%[%a %d]>                       This month
               %[%H:%M ]                                 Today
```

Another view:

```
%<[y? %<[m? %<[d? AAA & BBB > & CCC > & DDD >
```

AAA = `%[%H:%M ]` BBB = `%[%a %d]` CCC = `%[%b %d]` DDD = `%[%m/%y ]`

### Example neomuttrc for Conditional Dates

```neomuttrc
# Example NeoMutt config file for the cond-date feature.

#
# The default index_format is:
#       '%4C %Z %{%b %d} %-15.15L (%<l?%4l&%4c>) %s'
#
# We replace the date field '%{%b %d}', giving:
set index_format='%4C %Z %<[y?%<[m?%<[d?%[%H:%M ]&%[%a %d]>&%[%b %d]>&%[%m/%y ]> %-15.15L (%<l?%4l&%4c>) %s'
# Test  Date Range  Format String  Example
# --------------------------------------------
# %[d   Today       %[%H:%M ]      12:34
# %[m   This month  %[%a %d]       Thu 12
# %[y   This year   %[%b %d]       Dec 10
#  —    Older       %[%m/%y ]      06/15
```

### Known Bugs

Date parsing doesn't quite do what you expect.
"1w" doesn't mean "in the last 7 days", but "*this* week".
This doesn't match the normal NeoMutt behavior: for example `~d>1w` means emails dated in the last 7 days.

---

## Nested If

The nested-if feature allows complex nested conditions in format strings.

NeoMutt's format strings can contain embedded if-then-else conditions.
They are of the form:

```
%?VAR?TRUE&FALSE?
```

If the variable "VAR" has a value greater than zero, print the "TRUE" string, otherwise print the "FALSE" string.

e.g. `%?S?Size: %S&Empty?`

Which can be read as:

```
if (%S > 0) { print "Size: %S" } else { print "Empty" }
```

These conditions are useful, but in NeoMutt they cannot be nested within one another.
This feature uses the notation `%<VAR?TRUE&FALSE>` and allows them to be nested.

A simple nested condition might be (some whitespace has been introduced for clarity):

```
%<x? %<y? XY & X > & %<y? Y & NONE > >  Conditions
     %<y? XY & X >                      x>0
          XY                            x>0,y>0
               X                        x>0,y=0
```

```
%<x? %<y? XY & X > & %<y? Y & NONE > >  Conditions
                     %<y? Y & NONE >    x=0
                          Y             x=0,y>0
                              NONE      x=0,y=0
```

Equivalent to:

```
if (x > 0) {
  if (y > 0) {
    print 'XY'
  } else {
    print 'X'
  }
} else {
  if (y > 0) {
    print 'Y'
  } else {
    print 'NONE'
  }
}
```

### Examples

```neomuttrc
set index_format='%4C %Z %{%b %d} %-25.25n %s%> %<M?%M Msgs &%<l?%l Lines&%c Bytes>>'
```

If a thread is folded display the number of messages (%M), else if we know how many lines in the message display lines in message (%l), else display the size of the message in bytes (%c).

```neomuttrc
set index_format='%4C %Z %{%b %d} %-25.25n %<M?[%M] %s&%s%* %<l?%l&%c>>'
```

If a thread is folded display the number of messages (%M) and the subject (%s), else if we know how many lines are in the message display subject (%s) and the lines in message (%l), else display the subject (%s) and the size of the message in bytes (%c).

:::{note}
If you wish to use angle brackets `< >` in a nested condition, then it's necessary to escape them, e.g.

```neomuttrc
set index_format='%<M?\<%M\>&%s>'
```
:::

### Example neomuttrc for Nested-If

```neomuttrc
# Example NeoMutt config file for the nested-if feature.

# This feature uses the format: '%<VAR?TRUE&FALSE>' for conditional
# format strings that can be nested.

# Example 1
# if a thread is folded
#       display the number of messages (%M)
# else if we know how many lines in the message
#       display lines in message (%l)
# else display the size of the message in bytes (%c)
set index_format='%4C %Z %{%b %d} %-25.25n %s%> %<M?%M Msgs &%<l?%l Lines&%c Bytes>>'

# Example 2
# if a thread is folded
#       display the number of messages (%M)
#       display the subject (%s)
# else if we know how many lines in the message
#       display lines in message (%l)
# else
#       display the size of the message in bytes (%c)
set index_format='%4C %Z %{%b %d} %-25.25n %<M?[%M] %s&%s%* %<l?%l&%c>>'
```

---

## Initials Expando

The "initials" feature adds an expando (`%I`) for an author's initials.

The index panel displays a list of emails.
Its layout is controlled by the `$index_format` variable.
Using this expando saves space in the index panel.
This can be useful if you are regularly working with a small set of people.

This feature has no config of its own.
It adds an expando which can be used in the `$index_format` variable.

### Example neomuttrc for Initials

```neomuttrc
# The default 'index_format' is:
set index_format='%4C %Z %{%b %d} %-15.15L (%<l?%4l&%4c>) %s'
# Where %L represents the author/recipient
# This might look like:
#       1   + Nov 17 David Bowie   Changesbowie    ( 689)
#       2   ! Nov 17 Stevie Nicks  Rumours         ( 555)
#       3   + Nov 16 Jimi Hendrix  Voodoo Child    ( 263)
#       4   + Nov 16 Debbie Harry  Parallel Lines  ( 540)
# Using the %I expando:
set index_format='%4C %Z %{%b %d} %I (%<l?%4l&%4c>) %s'
# This might look like:
#       1   + Nov 17 DB Changesbowie    ( 689)
#       2   ! Nov 17 SN Rumours         ( 555)
#       3   + Nov 16 JH Voodoo Child    ( 263)
#       4   + Nov 16 DH Parallel Lines  ( 540)
```

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Index with initials vs full names

**Description:** Two side-by-side or before/after views of the NeoMutt index: one using `%L` (full author name like "David Bowie") and one using `%I` (initials like "DB"), showing how the initials expando saves horizontal space.

**Highlights:** The space savings from using initials, and how the rest of the index columns shift to accommodate more subject text.
:::

---

## index-format-hook — Dynamically Changing $index_format Using Patterns

### Syntax

```neomuttrc
index-format-hook name [!]pattern format-string
```

This command is used to inject format strings dynamically into `$index_format` based on pattern matching against the current message.

If the pattern is a plain string, or a regex, it will be expanded to a pattern using `$default_hook`.

The `$index_format` expando `%@name@` specifies a placeholder for the injection.
Index-format-hooks with the same *name* are matched using *pattern* against the current message.
Matching is done in the order specified in the .muttrc, with the first match being used.
The hook's *format-string* is then substituted and evaluated.

Because the first match is used, best practice is to put a catch-all `~A` pattern as the last hook.

### Example: Dynamic Date Formatting

```neomuttrc
set index_format="%4C %-6@date@ %-15.15F %Z (%4c) %s"

index-format-hook  date  "~d<1d"    "%[%H:%M]"
index-format-hook  date  "~d<1m"    "%[%a %d]"
index-format-hook  date  "~d<1y"    "%[%b %d]"
index-format-hook  date  "~A"       "%[%m/%y]"
```

### Example: Prepending to the Subject

Note that without a catch-all `~A` pattern, no match results in the expando being replaced with an empty string.

```neomuttrc
set index_format="%4C %@subj_flags@%s"

index-format-hook  subj_flags  "~f boss@example.com"    "** BOSS ** "
index-format-hook  subj_flags  "~f spouse@example.com"  ":-) "
```
