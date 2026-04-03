---
title: Color / UI Appearance
description: Commands for setting foreground and background colors, attributes, and mono-mode styles on UI elements and message patterns.
keywords: color, uncolor, mono, unmono, theme, appearance, foreground, background, attributes, bold, underline, index color, body color, header color, ui styling
---

(ref-cmd-color)=
# Color / UI Appearance

Commands for defining and removing colors and mono-mode attributes.

(cmd-color)=
## `color`

Define colors for a UI element.

- `color <object> <fg> <bg>` — set foreground/background on a UI object
- `color <object> <attribute> <fg> <bg>` — add bold, underline, etc.
- `color body <fg> <bg> <regex>` — colorize text in the message body matching a pattern
- `color index <fg> <bg> <pattern>` — colorize index lines matching a pattern
- `color header <fg> <bg> <regex>` — colorize message headers matching a pattern

```neomuttrc
color normal     default  default
color status     black    cyan
color indicator  brightwhite default bold
color tree       red      default
color attachment  white    default
color signature   brightred default reverse
color body       brightblue  default "(https?|ftp)://[^ ]+"
color body       brightyellow default "[a-z0-9._-]+@[a-z0-9._-]+"
color index      brightgreen default "~N"
color index      red         default "~F"
color header     cyan        default "^(From|Subject):"
```

(cmd-uncolor)=
## `uncolor`

Remove a color definition.

- `uncolor <object> *` — remove all color rules for an object
- `uncolor <object> <pattern>` — remove a specific color rule

```neomuttrc
uncolor index *
uncolor body "(https?|ftp)://[^ ]+"
```

(cmd-mono)=
## `mono`

**Deprecated** — use `color` instead.

(cmd-unmono)=
## `unmono`

**Deprecated** — use `uncolor` instead.

