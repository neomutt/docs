---
title: Color Command
description: Syntax reference for the NeoMutt color command covering simple, regex, and pattern color objects
keywords: neomutt, color, colour, command, syntax, theme, regex, pattern, uncolor, attributes, foreground, background, index, status, sidebar
---

(ref-color-syntax)=
# Color Command — Syntax Reference

## Overview

The `color` command defines colors for NeoMutt's user interface.  There are
three kinds of color object, each with different syntax:

| Kind        | Syntax                                            | Matching | Rules    |
|-------------|---------------------------------------------------|----------|----------|
| **Simple**  | `color <object> [<attr> ...] <fg> <bg>`           | none     | single   |
| **Regex**   | `color <object> [<attr> ...] <fg> <bg> <regex>`   | regex    | multiple |
| **Pattern** | `color <object> [<attr> ...] <fg> <bg> <pattern>` | pattern  | multiple |

- **Simple** objects have a single color.  Setting a new color replaces the old one.
- **Regex** and **Pattern** objects are cumulative.
  Each `color` command adds a rule to a list.  All matching rules are applied in order.

---

## General Syntax

```neomuttrc
color <object> [<attribute> ...] <foreground> <background> [<regex-or-pattern>]
```

### Color Names

NeoMutt supports several ways to specify a color:

| Format      | Example     | Description                                      |
|-------------|-------------|--------------------------------------------------|
| Named color | `red`       | One of 8 basic terminal colors                   |
| `bright`    | `brightred` | Bright/bold variant of a named color             |
| `light`     | `lightred`  | Light variant (same as bright on most terms)     |
| `alert`     | `alertred`  | Alert variant (same as bright on most terms)     |
| `default`   | `default`   | Terminal's default foreground or background      |
| Palette     | `color123`  | 256-color palette (color0 .. color255)           |
| RGB hex     | `#FF5F00`   | 24-bit true color (requires `color_directcolor`) |

The eight named colors are: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`.

### Attributes

Zero or more attributes may be placed before the foreground color:

| Attribute   | Effect                         |
|-------------|--------------------------------|
| `bold`      | Bold text                      |
| `underline` | Underlined text                |
| `italic`    | Italic text                    |
| `reverse`   | Swap foreground and background |
| `standout`  | Terminal's standout mode       |
| `none`      | Clear all attributes           |

Multiple attributes may be combined:

```neomuttrc
color indicator bold underline white blue
```

---

## Simple Color Objects

Simple objects have **a single color**.
Each `color` command replaces any previous color for that object.

### General UI

| Object      | Description                                    |
|-------------|------------------------------------------------|
| `normal`    | Plain text, the default color for all text     |
| `error`     | Error messages on the message line             |
| `warning`   | Warning messages on the message line           |
| `message`   | Informational messages on the message line     |
| `indicator` | The selected/highlighted line in any menu      |
| `prompt`    | Question/prompt text on the message line       |
| `options`   | Option letters in a prompt (e.g. `[y/n]?`)     |
| `search`    | Matching text when searching in the pager      |
| `markers`   | The `+` markers for wrapped lines in the pager |
| `progress`  | The progress bar                               |
| `bold`      | Bold text in the pager                         |
| `italic`    | Italic text in the pager                       |
| `underline` | Underlined text in the pager                   |

```neomuttrc
color normal            default      default
color error             red          default
color warning           yellow       default
color message           cyan         default
color indicator reverse white        black
color prompt            yellow       default
color options           brightcyan   default
color search            black        yellow
color markers           brightblue   default
color progress          white        blue
color bold              brightwhite  default
color italic            brightyellow default
color underline         brightgreen  default
```

### Pager & Message Display

| Object       | Description                             |
|--------------|-----------------------------------------|
| `hdrdefault` | Default color for message headers       |
| `signature`  | Signature lines at the end of a message |
| `tilde`      | `~` lines after the end of message body |
| `attachment` | MIME attachment info lines in the pager |
| `tree`       | Thread-tree drawing characters          |

```neomuttrc
color attachment magenta     default
color hdrdefault cyan        default
color signature  brightblack default
color tilde      brightblack default
color tree       red         default
```

### Compose Screen

| Object                     | Description                                   |
|----------------------------|-----------------------------------------------|
| `compose_header`           | Header labels (`From:`, `To:`, etc.)          |
| `compose_security_none`    | Security indicator: no encryption/signing     |
| `compose_security_sign`    | Security indicator: message will be signed    |
| `compose_security_encrypt` | Security indicator: message will be encrypted |
| `compose_security_both`    | Security indicator: signed and encrypted      |

```neomuttrc
color compose_header            brightblue  default
color compose_security_none     red         default
color compose_security_sign     yellow      default
color compose_security_encrypt  green       default
color compose_security_both     brightgreen default
```

### Sidebar

| Object               | Description                                                  |
|----------------------|--------------------------------------------------------------|
| `sidebar_background` | Background color for the entire sidebar                      |
| `sidebar_divider`    | Divider line between sidebar and index/pager                 |
| `sidebar_highlight`  | The currently highlighted mailbox                            |
| `sidebar_indicator`  | The currently open mailbox                                   |
| `sidebar_new`        | Mailboxes with new mail                                      |
| `sidebar_unread`     | Mailboxes with unread mail                                   |
| `sidebar_flagged`    | Mailboxes with flagged messages                              |
| `sidebar_ordinary`   | Mailboxes with no new/flagged messages                       |
| `sidebar_spool_file` | The primary incoming mailbox [`$spool_file`](cfg-spool-file) |

```neomuttrc
color sidebar_background  default       default
color sidebar_divider     brightblack   default
color sidebar_highlight   reverse       default default
color sidebar_indicator   brightcyan    default
color sidebar_new         brightgreen   default
color sidebar_unread      brightblue    default
color sidebar_flagged     red           default
color sidebar_ordinary    default       default
color sidebar_spool_file  brightmagenta default
```

### Quoted Text

Quoted text levels 0-9, for nested email replies.
`quoted0` (or the deprecated alias `quoted`) is the outermost level.

| Object    | Description                      |
|-----------|----------------------------------|
| `quoted0` | Quoted text, level 0 (outermost) |
| `quoted1` | Quoted text, level 1             |
| `quoted2` | Quoted text, level 2             |
| ...       | ...                              |
| `quoted9` | Quoted text, level 9 (deepest)   |

```neomuttrc
color quoted0  blue      default
color quoted1  cyan      default
color quoted2  green     default
color quoted3  yellow    default
color quoted4  red       default
```

### Help Page Stripes

| Object        | Description                          |
|---------------|--------------------------------------|
| `stripe_even` | Even-numbered lines on the help page |
| `stripe_odd`  | Odd-numbered lines on the help page  |

```neomuttrc
color stripe_even  default    color234
color stripe_odd   default    default
```

---

## Regex Color Objects

Regex objects are **cumulative** — each `color` command adds a rule to a list.
Multiple rules can match the same text; all matching rules apply in order, with later rules overriding earlier ones for overlapping regions.

The regex is a POSIX Extended Regular Expression and is matched against the text being displayed.
Case-sensitive matching is used when the regex contains uppercase letters; otherwise matching is case-insensitive.

### `body`

Colorise text in the message body matching a regex.

```neomuttrc
color body [<attr> ...] <fg> <bg> <regex>
```

The regex is matched against each line of the message body.

```neomuttrc
# URLs
color body  brightblue   default  "(https?|ftp)://[^ >\"]*"

# Email addresses
color body  brightyellow default  "[a-z0-9._-]+@[a-z0-9._-]+"

# Bold text (*word*)
color body  bold         default  default  "\\*[a-z]+\\*"

# Underline text (_word_)
color body  underline    default  default  "_[a-z]+_"

# IPv4 addresses
color body  cyan         default  "[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}"
```

### `header`

Colorise message headers matching a regex.
The regex is matched against the entire header line (name and value).

```neomuttrc
color header [<attr> ...] <fg> <bg> <regex>
```

```neomuttrc
color header  brightcyan   default  "^From:"
color header  brightcyan   default  "^Subject:"
color header  cyan         default  "^To:"
color header  cyan         default  "^Cc:"
color header  brightblack  default  "^Date:"
color header  yellow       default  "^X-Mailer:"
```

### `attach_headers`

Colorise MIME attachment header lines in the pager, matching a regex.

```neomuttrc
color attach_headers [<attr> ...] <fg> <bg> <regex>
```

```neomuttrc
color attach_headers  brightmagenta  default  "image/"
color attach_headers  green          default  "application/pgp-signature"
```

---

## Pattern Color Objects

Pattern objects are **cumulative** — each `color` command adds a rule to a list.
Multiple rules can match the same message; all matching rules apply in order.

The pattern uses NeoMutt's search pattern language (the same syntax used by `limit`, `tag-pattern`, `score`, hooks, etc.).
Common pattern operators:

| Pattern     | Matches                                 |
|-------------|-----------------------------------------|
| `~A`        | All messages                            |
| `~N`        | New (unread, recent) messages           |
| `~O`        | Old (unread, not recent) messages       |
| `~U`        | Unread messages                         |
| `~R`        | Read messages                           |
| `~F`        | Flagged messages                        |
| `~D`        | Deleted messages                        |
| `~T`        | Tagged messages                         |
| `~f <addr>` | Messages from `<addr>`                  |
| `~t <addr>` | Messages to `<addr>`                    |
| `~s <expr>` | Messages with subject matching `<expr>` |
| `~d <date>` | Messages dated within a range           |

### `index`

Colorise the entire index line for messages matching a pattern.

```neomuttrc
color index [<attr> ...] <fg> <bg> <pattern>
```

```neomuttrc
color index  brightgreen  default  "~N"
color index  red          default  "~F"
color index  brightblack  default  "~D"
color index  yellow       default  "~T"
color index  cyan         default  "~U"
color index  magenta      default  "~f boss@company\\.com"
color index  brightred    default  "~s urgent"
```

### `index_*` Sub-fields

Colorise individual fields within the index line.
These all use the same pattern syntax as `index`.

| Object            | Field colored                            |
|-------------------|------------------------------------------|
| `index_author`    | Author/sender name                       |
| `index_collapsed` | Number of messages in a collapsed thread |
| `index_date`      | Date field                               |
| `index_flags`     | Message flags field                      |
| `index_label`     | X-Label field (`%y`)                     |
| `index_number`    | Index number                             |
| `index_size`      | Message size                             |
| `index_subject`   | Subject field                            |
| `index_tag`       | Individual tag (`%G`)                    |
| `index_tags`      | Tags field (`%g`, `%J`)                  |

```neomuttrc
# Highlight the author of new messages
color index_author  brightblue   default  "~N"

# Highlight the subject of flagged messages
color index_subject brightred    default  "~F"

# Highlight the date of messages from today
color index_date    brightgreen  default  "~d<1d"

# Dim the size of read messages
color index_size    brightblack  default  "~R"

# Highlight flags on deleted messages
color index_flags   red          default  "~D"
```

---

## Status Bar Colors

The `status` object is a special case.
Used without a regex, it is a **simple** (single) color.
Used with a regex, it is **cumulative** and supports submatch highlighting.

### Simple status color

```neomuttrc
color status [<attr> ...] <fg> <bg>
```

```neomuttrc
color status  black  cyan
color status  bold white blue
```

### Status bar with regex

Colorise parts of the status bar matching a regex.

```neomuttrc
color status [<attr> ...] <fg> <bg> <regex>
```

```neomuttrc
# Highlight the mailbox name in the status bar
color status  brightwhite  blue  "INBOX"

# Highlight unread count
color status  brightyellow blue  "Msgs:[0-9]+"
```

### Status bar with submatch

Colorise only the Nth parenthesized submatch of a regex.

```neomuttrc
color status [<attr> ...] <fg> <bg> <regex> <num>
```

```neomuttrc
# Colorise just the number inside "Msgs:NNN"
color status  brightred  blue  "Msgs:([0-9]+)" 1
```

---

## Removing Colors

### `uncolor`

Remove color rules.

```neomuttrc
uncolor <object> { * | <pattern> ... }
```

- `uncolor <object> *` — remove all rules for that object
- `uncolor <object> <pattern>` — remove a specific rule by its regex/pattern string

Simple objects are reset to the default color.  Regex/pattern objects have
matching rules removed from their list.

```neomuttrc
# Remove all body colors
uncolor body *

# Remove a specific index color rule
uncolor index "~D"

# Remove a specific header color rule
uncolor header "^X-Mailer:"
```

---

## Quick Reference

### Simple (single color, last-one-wins)

```
attachment             compose_header            hdrdefault
bold                   compose_security_both     indicator
error                  compose_security_encrypt  markers
italic                 compose_security_none     message
normal                 compose_security_sign     options
progress               search                    signature
prompt                 stripe_even               tilde
tree                   stripe_odd                underline
warning                                          quoted0..quoted9
sidebar_background     sidebar_highlight         sidebar_ordinary
sidebar_divider        sidebar_indicator         sidebar_spool_file
sidebar_flagged        sidebar_new               sidebar_unread
```

### Regex (cumulative, POSIX regex)

```
attach_headers         body                   header
```

### Pattern (cumulative, NeoMutt search pattern)

```
index                  index_date             index_number
index_author           index_flags            index_size
index_collapsed        index_label            index_subject
                       index_tag              index_tags
```

### Special (both modes)

```
status                 (no regex = simple, with regex = cumulative)
```
