---
title: Customise Colours
description: Configure colours, attributes, and themes for the index, status bar, sidebar, compose menu, and attachment headers
keywords: color, colour, theme, index-color, status-color, attach_headers, mono, directcolor, truecolor, 256 color, foreground, background, quoted, sidebar, compose, uncolor, bold, underline, reverse
---

# Customise Colours

(using-color-and-mono-video-attributes)=
## Using Color and Mono Video Attributes

Usage:

```neomuttrc
color <object> [<attribute> ...] <foreground> <background>
color <pattern-object> [<attribute> ...] <foreground> <background> <pattern>
color <regex-object> [<attribute> ...] <foreground> <background> <regex>
color status [<attribute> ...] <foreground> <background> [<regex> [<num>]]
uncolor <object>
uncolor <pattern-object> { <pattern> | * }
uncolor <regex-object> { <regex> | * }
uncolor status { <regex> | * }
```

If your terminal supports color, you can spice up NeoMutt by creating your own color scheme.

:::{note}
The config option [`$color_directcolor`](cfg-color-directcolor) must be set to its final value *before* using any [`:color`](cmd-color) command.
:::

The types of objects that can be colored fall into two categories: [Simple Colors](#simple-colors) such as the highlight in the index, and [Color Lists](#color-lists) such as the status bar.
These lists can create complex coloring rules.

### Color Style

Objects in NeoMutt can be given colors and attributes to make things easier to find and use.

:::{note}
Objects must be given *both* a foreground and background color (it is not possible to specify one or the other).
Note that `default` can be used as transparent color (see below).
:::

Colors can be specified in up to three ways, using their name such as `green`, `blue`; by their number in the palette, such as `color12`, `color207` (the palette consists of the [256 Xterm colors](https://web.archive.org/web/20190712111427/https://jonasjacek.github.io/colors/)); or by using hexadecimal RGB codes `#RRGGBB`, where `RR`, `GG`, `BB` are the red, green, and blue components given as a hexadecimal number between 00 and FF (=255), e.g. `#00FFFF` (bright cyan) or `#12af84` (greenish).
The last syntax is only accepted if [`$color_directcolor`](cfg-color-directcolor) is set.

Named colours may also be prefixed by a *modifier*. `bright` or `light` will make the color boldfaced or light (e.g., `brightred`). `alert` to make a blinking/alert color (e.g., `alertred`).

The precise behavior depends on the terminal and its configuration.
In particular, the boldfaced/light difference and such background colors may be available only for terminals configured with at least 16 colors, as specified by the `$TERM` environment variable.

*foreground* and *background* can be one of the following:

- white
- black
- green
- magenta
- blue
- cyan
- yellow
- red
- default

In addition to the colors, objects may have their *attributes* set:

- none
- bold
- italic
- reverse
- standout
- underline

If your terminal supports it, the special keyword *default* can be used as a transparent color.
In this case *default* can be used to only set the foreground or background color.
The following sets the foreground and background color individually: the first command leaves the foreground untouched while the second one leaves the background untouched:

```neomuttrc
# Make error messages white text on a red background
color error default red
color error white   default
```

On startup NeoMutt tries to detect whether the terminal it is running in supports directcolor (aka TrueColor aka 24-bit color).
If the terminal does, NeoMutt enables the config option [`$color_directcolor`](cfg-color-directcolor) otherwise it disables it.
Furthermore, NeoMutt allows to use the RGB colors syntax with the [`:color`](cmd-color) command to colour elements with 24-bit colors.

For the detection to work the *TERM* environment variable must be set up properly to advertise the terminals directcolor capability.
*TERM*-values which do that usually end in `-direct`, e.g. `xterm-direct`.

If NeoMutt does not detect directcolor color support, but you are sure your terminal supports it, you may try to explicitly set the *TERM* environment variable by starting NeoMutt from the terminal as follows:

```neomuttrc
TERM=xterm-direct neomutt
```

If that still does not help, you can additionally force NeoMutt to use directcolors by setting [`$color_directcolor`](cfg-color-directcolor).
Setting this variable manually is strongly discouraged since it usually leads to wrong colors.

(simple-colors)=
### Simple Colors

Most of NeoMutt's colorable objects follow simple rules.
They don't use a pattern and any new configuration will overwrite the old colours.

Simple colors can be undone by setting the foreground and background to `default`, or by using the [`:uncolor`](cmd-uncolor) command.

These are general NeoMutt objects:

| Colour Name | Description                                                    |
|-------------|----------------------------------------------------------------|
| attachment  | Colour for attachment headers                                  |
| bold        | Highlighting bold patterns in the body of messages             |
| error       | Error messages printed by NeoMutt                              |
| hdrdefault  | Default colour of the message header in the pager              |
| indicator   | Arrow or bar used to indicate the current item in a menu       |
| markers     | The "+" markers at the beginning of wrapped lines in the pager |
| message     | Informational messages                                         |
| normal      | Default colour for all text                                    |
| options     | The key letters in multi-choice questions                      |
| progress    | Visual progress bar                                            |
| prompt      | A question                                                     |
| search      | Highlighting of words in the pager                             |
| signature   | Email's signature lines (.sig)                                 |
| tilde       | The "\~" used to pad blank lines in the pager                  |
| tree        | Thread tree drawn in the message index and attachment menu     |
| underline   | Highlighting underlined patterns in the body of messages       |
| warning     | Warning messages                                               |

```neomuttrc
# Make error messages white text on a red background
color error white red
# Make questions bold, underlined, with light blue text (with default background)
color prompt bold underline cyan default
```

```neomuttrc
uncolor error
uncolor prompt
```

These are sidebar objects.
See [Sidebar](sidebar.md) for more details.

| Colour Name        | Description                                                      |
|--------------------|------------------------------------------------------------------|
| sidebar_background | The entire sidebar panel                                         |
| sidebar_divider    | The dividing line between the Sidebar and the Index/Pager panels |
| sidebar_flagged    | Mailboxes containing flagged mail                                |
| sidebar_highlight  | Cursor to select a mailbox                                       |
| sidebar_indicator  | The mailbox open in the Index panel                              |
| sidebar_new        | Mailboxes containing new mail                                    |
| sidebar_ordinary   | Mailboxes that have no new/flagged mails, etc                    |
| sidebar_spool_file | Mailbox that receives incoming mail                              |
| sidebar_unread     | Mailboxes containing unread mail                                 |

```neomuttrc
color sidebar_divider brightblack default
```

```neomuttrc
uncolor sidebar_divider
```

These are compose objects.

| Colour Name              | Description                          |
|--------------------------|--------------------------------------|
| compose_header           | Header labels, e.g. From:            |
| compose_security_encrypt | Mail will be encrypted               |
| compose_security_sign    | Mail will be signed                  |
| compose_security_both    | Mail will be encrypted and signed    |
| compose_security_none    | Mail will not be encrypted or signed |

```neomuttrc
color compose_header bold white default
```

```neomuttrc
uncolor compose_header
```

The quoted objects refer to quoted lines in an email reply.
They are defined using the [`$reply_regex`](cfg-reply-regex) config option.

The quoted email colours don't use a pattern.
The first colour, `quoted` provides a default colour for all quoted text.
Also, each different level of quoting can be given a different colour using, `quoted1`, `quoted2`, `quoted3` up to `quoted9`.

| Colour Name | Description                                           |
|-------------|-------------------------------------------------------|
| quoted      | Text matching [`$quote_regex`](cfg-quote-regex) in the body of a message |
| quoted1     | 1 level deeper quoted text, e.g. `> > text`           |
| quoted2     | 2 level deeper quoted text, e.g. `> > > text`         |
| ...         | ...                                                   |
| quoted9     | 9 level deeper quoted text                            |

```neomuttrc
color quoted brightblue default
color quoted1 brightgreen default
color quoted2 yellow default
```

```neomuttrc
uncolor quoted
uncolor quoted1
uncolor quoted2
```

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Quoted text with per-level colours

**Description:** NeoMutt pager showing a deeply-quoted email reply with three or more levels of quoting — level 1 (`>`) in bright blue, level 2 (`>>`) in bright green, level 3 (`>>>`) in yellow, each visually distinct.
The unquoted reply text appears in the default colour.

**Highlights:** The colour gradient across quote levels — how distinct colours make it easy to follow the conversation depth and quickly identify the newest reply text.
:::

(color-lists)=
### Color Lists

Some objects in NeoMutt support *lists* of color rules.
Each rule has a pattern and a color.
Each is checked in turn and any matching rules are applied cumulatively (overlaid).

When applying the colours, each pattern will be tested against the field to be colored.
All of the matching patterns will have their colors applied in the order they are configured.

The color lists work in slightly different ways to each other.

`attach_headers`, `body` and `header` match a *regular expression* (regex) in the header/body of an email.

`index` objects match a *pattern* in the email index (see Patterns).
Note that IMAP server-side searches (=b, =B, =h) are not supported for color index patterns.

When [`$header_color_partial`](cfg-header-color-partial) is unset (the default), a `header` matched by *regex* will have color applied to the entire header.
When set, color is applied only to the exact text matched by *regex*.

For the `status` list, the *regular expression* is optional.
Without one, the command will set the default style for the status bar.
With a regex (and an optional number), it's possible to style parts of the status bar.
See: [Status-Color feature](#status-color-feature) for more detail.

Color lists can be undone by using the [`:uncolor`](cmd-uncolor) command and the pattern or `*` to match.

| Colour Name     | Match   | Description                                          |
|-----------------|---------|------------------------------------------------------|
| attach_headers  | regex   | Attachment headers                                   |
| body            | regex   | Email body                                           |
| header          | regex   | Email headers                                        |
| index           | pattern | Default highlighting of the entire index line        |
| index_author    | pattern | Author in the index: `%A`, `%a`, `%F`, `%L`, `%n`    |
| index_collapsed | pattern | Number of messages in a collapsed thread: `%M`       |
| index_date      | pattern | Date field: `%d`, `%D`, `%{fmt}`, `%[fmt]`, `%(fmt)` |
| index_flags     | pattern | Flags in the index: `%S`, `%Z`                       |
| index_label     | pattern | Message label: `%y`, `%Y`                            |
| index_number    | pattern | Message number: `%C`                                 |
| index_size      | pattern | Message size: `%c`, `%cr`, `%l`                      |
| index_subject   | pattern | Subject in the index: `%s`                           |
| index_tag       | pattern | Tags in the index: `%G`                              |
| index_tags      | pattern | Transformed message tags: `%g`, `%J`                 |
| status          | regex   | Status bar                                           |

```neomuttrc
# Highlight emails from work (entire line)
color index          cyan default "~f @work.com"
# Extra highlighting for the boss (just the author column)
color index_author   cyan red     "~f boss@work.com"
```

```neomuttrc
uncolor index          "~f @work.com"
# Clear all index_author colors
uncolor index_author   *
```

```neomuttrc
# Add some highlights to the body of an email
color body    bold red    default "(urgent|important)"
color body         yellow default "(warning|notice)"
# Make the label header red
color header       cyan   default "X-Label"
```

```neomuttrc
uncolor body    "(urgent|important)"
# Clear all body colors
uncolor body    *
uncolor header  "X-Label"
```

```neomuttrc
# Set the default color for the entire status line
color status blue white
# Highlight New, Deleted, or Flagged emails
color status brightred white '(New|Del|Flag):[0-9]+'
# Highlight the contents of the []s but not the [] themselves
color status red default '\[([^]]+)\]' 1
```

```neomuttrc
uncolor status '(New|Del|Flag):[0-9]+'
uncolor status *
```

### Mono Color

If your terminal does not support color, it is still possible change the video attributes through the use of the "mono" command.
Usage:

```neomuttrc
mono <object> <attribute>
mono { header | body } <attribute> <regex>
mono <index-object> <attribute> <pattern>
unmono { <index-object> | header | body } { * | <pattern> ... }
```

For *object* and *attribute*, see the [`:color`](cmd-color) command.

(index-color-feature)=
## Index Color Feature

The "index-color" feature allows you to specify colors for individual parts of the email index. e.g. Subject, Author, Flags.

First choose which part of the index you'd like to color.
Then, if needed, pick a pattern to match.

Note: The pattern does not have to refer to the object you wish to color. e.g.

```neomuttrc
color index_author red default "~sneomutt"
```

The author appears red when the subject (\~s) contains "neomutt".

### Index Colors

All the colors default to `default`, i.e. unset.

The index objects can be themed using the [`:color`](cmd-color) command and an optional pattern.
A missing pattern is equivalent to a match-all `.*` pattern.

```neomuttrc
color index-object foreground background [pattern]
```

| Object            | Highlights                                   |
|-------------------|----------------------------------------------|
| `index`           | Entire index line                            |
| `index_author`    | Author name, %A %a %F %L %n                  |
| `index_collapsed` | Number of messages in a collapsed thread, %M |
| `index_date`      | Date field                                   |
| `index_flags`     | Message flags, %S %Z                         |
| `index_label`     | Message label, %y %Y                         |
| `index_number`    | Message number, %C                           |
| `index_size`      | Message size, %c %cr %l                      |
| `index_subject`   | Subject, %s                                  |
| `index_tag`       | Message tags, `%G`                           |
| `index_tags`      | Transformed message tags, `%g` `%J`          |

### Index Color neomuttrc

```neomuttrc
# Example NeoMutt config file for the index-color feature.

# Entire index line
color index white black '.*'
# Author name, %A %a %F %L %n
# Give the author column a dark grey background
color index_author default color234 '.*'
# Highlight a particular from (~f)
color index_author brightyellow color234 '~fRay Charles'
# Message flags, %S %Z
# Highlight the flags for flagged (~F) emails
color index_flags default red '~F'
# Subject, %s
# Look for a particular subject (~s)
color index_subject brightcyan default '~s\(closes #[0-9]+\)'
# Number of messages in a collapsed thread, %M
color index_collapsed default brightblue
# Date field
color index_date green default
# Message label, %y %Y
color index_label default brightgreen
# Message number, %C
color index_number red default
# Message size, %c %cr %l
color index_size cyan default

# vim: filetype=neomuttrc
```

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Index with per-column colours

**Description:** NeoMutt index view with the index-color configuration applied — message numbers in red, dates in green, author names on a dark grey background (with one author "Ray Charles" highlighted in bright yellow), subject lines showing a bright cyan highlight for subjects matching a pattern, flags in red for flagged messages, and sizes in cyan.

**Highlights:** How different index columns (number, date, author, flags, subject, size) each have their own colour, making the dense index easier to scan — and how pattern-matched colours draw attention to specific messages.
:::

### Index Color See Also

- Regular Expressions
- Patterns
- [`$index_format`](cfg-index-format)
- [Color command](#using-color-and-mono-video-attributes)
- [Status-Color feature](#status-color-feature)

### Index Color Credits

Christian Aichinger, Christoph "Myon" Berg, Elimar Riesebieter, Eric Davis, Vladimir Marek, Richard Russon

(status-color-feature)=
## Status Color Feature

The "status-color" feature allows you to theme different parts of the status bar (also when it's used by the index).

Unlike normal color commands, `color status` can now take up to 2 extra parameters (regex, num).

### Status Color Commands

```neomuttrc
color status <foreground> <background> [<regex> [<num>]]
```

With zero parameters, NeoMutt will set the default color for the entire status bar.

With one parameter, NeoMutt will only color the parts matching the regex.

With two parameters, NeoMutt will only color the num'th sub-match of the regex.

### Status Colors

| Name   | Default Color | Description |
|--------|---------------|-------------|
| status | `reverse`     | Status bar  |

### Status Color neomuttrc

```neomuttrc
# Example NeoMutt config file for the status-color feature.

# The 'status-color' feature allows you to theme different parts of
# the status bar (also when it's used by the index).

# For the examples below, set some defaults
set status_format='-%r-NeoMutt: %f [Msgs:%<M?%M/>%m%<n? New:%n>%<o? Old:%o>%<d? Del:%d>\
%<F? Flag:%F>%<t? Tag:%t>%<p? Post:%p>%<b? Inc:%b>%<l? %l>]---(%s/%S)-%>-(%P)---'
set index_format='%4C %Z %{%b %d} %-15.15L (%<l?%4l&%4c>) %s'
set use_threads=yes
set sort=last-date-received
set sort_aux=date
# 'status color' can take up to 2 extra parameters
# color status foreground background [ regex [ num ]]
# 0 extra parameters
# Set the default color for the entire status line
color status blue white
# 1 extra parameter
# Set the color for a matching pattern
# color status foreground background regex
# Highlight New, Deleted, or Flagged emails
color status brightred white '(New|Del|Flag):[0-9]+'
# Highlight mailbox ordering if it's different from the default
# First, highlight anything (*/*)
color status brightred default '\([^)]+/[^)]+\)'
# Then override the color for one specific case
color status default default '\(threads/last-date-received\)'
# 2 extra parameters
# Set the color for the nth submatch of a pattern
# color status foreground background regex num
# Highlight the contents of the []s but not the [] themselves
color status red default '\[([^]]+)\]' 1
# The '1' refers to the first regex submatch, which is the inner
# part in ()s
# Highlight the mailbox
color status brightwhite default 'NeoMutt: ([^ ]+)' 1
# Search for 'NeoMutt: ' but only highlight what comes after it

# vim: filetype=neomuttrc
```

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Status bar with coloured sections

**Description:** NeoMutt status bar showing the status-color feature in action — the overall bar is blue on white, "New:", "Del:", and "Flag:" counters are highlighted in bright red, the mailbox name after "NeoMutt:" is bright white, and the sort order in parentheses is coloured differently when it differs from the default.

**Highlights:** How regex-based and submatch-based status colouring highlights specific parts of the status line — counters, mailbox name, and sort order each get distinct colours within the same bar.
:::

### Status Color See Also

- Compile-Time Features
- Regular Expressions
- Patterns
- [Index-Color feature](#index-color-feature)
- [Color command](#using-color-and-mono-video-attributes)

### Status Color Credits

David Sterba, Thomas Glanzmann, Kirill A.
Shutemov, Richard Russon

## Attach Headers Color Feature

The attach headers color feature allows specifying regexes to color attachment headers just like the mail body would.
The headers are the parts colored by the `attachment` color.
Coloring them is useful to highlight the results of GPGME's signature checks or simply the mimetype or size of the attachment.
Only the part matched by the regex is colored.

### Attach Headers Color Usage

The `attach_headers` color should be used just like the `body` color.

```neomuttrc
color attach_headers foreground background pattern
```

### Attach Headers Color neomuttrc

```neomuttrc
# Example NeoMutt config file for the attach-headers-color feature.

# Color if the attachment is autoviewed
color   attach_headers     brightgreen     default    "Autoview"
# Color only the brackets around the headers
color   attach_headers     brightyellow    default    "^\\[--"
color   attach_headers     brightyellow    default    "--]$"
# Color the mime type and the size
color   attach_headers     green           default    "Type: [a-z]+/[a-z0-9\-]+"
color   attach_headers     green           default    "Size: [0-9\.]+[KM]"
# Color GPGME signature checks
color   attach_headers     brightgreen     default    "Good signature from.*"
color   attach_headers     brightred       default    "Bad signature from.*"
color   attach_headers     brightred       default    "BAD signature from.*"
color   attach_headers     brightred       default    "Note: This key has expired!"
color   attach_headers     brightmagenta   default    "Problem signature from.*"
color   attach_headers     brightmagenta   default    "WARNING: This key is not certified with a trusted signature!"
color   attach_headers     brightmagenta   default    "         There is no indication that the signature belongs to the owner."
color   attach_headers     brightmagenta   default    "can't handle these multiple signatures"
color   attach_headers     brightmagenta   default    "signature verification suppressed"
color   attach_headers     brightmagenta   default    "invalid node with packet of type"

# vim: filetype=neomuttrc
```

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Coloured attachment headers

**Description:** NeoMutt pager or attachment view showing attachment headers
with the attach-headers-color rules applied — "Autoview" text in bright green,
bracket delimiters `[--` and `--]` in bright yellow, MIME type (e.g. "Type:
text/html") and size in green, and a GPGME "Good signature from..." line in
bright green (or "Bad signature" in bright red).

**Highlights:** How attachment header colouring brings attention to key metadata — MIME type, size, autoview status, and especially GPGME signature verification results (good/bad/problem) at a glance.
:::

### Attach Headers Color See Also

- [Color command](#using-color-and-mono-video-attributes)
- Regular Expressions

