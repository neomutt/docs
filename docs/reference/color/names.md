---
title: Colour Names and Attributes
description: Reference for NeoMutt colour names, modifiers, attributes, ANSI escape sequences, and colorable objects
keywords: neomutt, color, colour, attributes, theme, terminal, names, modifiers, bright, default, palette, 256-color, rgb, ansi, escape sequences
---

(ref-color-names)=
# Colour Names and Attributes

## Colour Specification

Objects in NeoMutt must be given *both* a foreground and background colour (it is not possible to specify one or the other). Note that `default` can be used as a transparent colour (see below).

Colours can be specified in three ways:

| Method          | Example               | Description                                                                                                                                |
|-----------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Name            | `green`, `blue`       | Use the colour's name                                                                                                                      |
| Palette number  | `color12`, `color207` | Use the colour's number in the [256 Xterm colour palette](https://web.archive.org/web/20190712111427/https://jonasjacek.github.io/colors/) |
| Hexadecimal RGB | `#00FFFF`, `#12af84`  | Use `#RRGGBB` notation (requires `$color_directcolor` to be set)                                                                           |

## Regex-Matched and Pattern-Matched Objects

Some colour objects require a regex or NeoMutt pattern as an additional argument (see [Command Syntax](#command-syntax) below).
These objects colour only the parts of the display that match the given expression.

| Object            | Match type | Applies to                       |
|-------------------|------------|----------------------------------|
| `body`            | regex      | Email body text                  |
| `header`          | regex      | Email header lines               |
| `index`           | pattern    | Entire index line                |
| `index_author`    | pattern    | Author fields (`%A %a %F %L %n`) |
| `index_collapsed` | pattern    | Collapsed thread count (`%M`)    |
| `index_date`      | pattern    | Date field                       |
| `index_flags`     | pattern    | Flags (`%S %Z`)                  |
| `index_label`     | pattern    | Label (`%y %Y`)                  |
| `index_number`    | pattern    | Message number (`%C`)            |
| `index_size`      | pattern    | Size (`%c %cr %l`)               |
| `index_subject`   | pattern    | Subject (`%s`)                   |
| `index_tag`       | pattern    | Tag name (`%G`)                  |
| `index_tags`      | pattern    | Transformed tags (`%g %J`)       |
| `status`          | regex      | Status bar text                  |

## Colour Names

The following named colours are available for *foreground* and *background*:

| Colour    |
|-----------|
| `white`   |
| `black`   |
| `green`   |
| `magenta` |
| `blue`    |
| `cyan`    |
| `yellow`  |
| `red`     |
| `default` |

## Colour Modifiers

Named colours may be prefixed by a modifier:

| Modifier            | Effect                             | Example     |
|---------------------|------------------------------------|-------------|
| `bright` or `light` | Make the colour boldfaced or light | `brightred` |
| `alert`             | Make a blinking/alert colour       | `alertred`  |

The precise behavior depends on the terminal and its configuration.
The boldfaced/light difference and such background colours may be available only for terminals configured with at least 16 colours.

## The `default` Colour

If your terminal supports it, the special keyword `default` can be used as a transparent colour.
In this case `default` can be used to only set the foreground or background colour individually:

```neomuttrc
# Make error messages white text on a red background
color error default red
color error white   default
```

## Attributes

In addition to colours, objects may have their attributes set:

| Attribute   |
|-------------|
| `none`      |
| `bold`      |
| `italic`    |
| `reverse`   |
| `standout`  |
| `underline` |

## Simple Colour Objects

These are general NeoMutt objects that can be coloured:

| Object       | Description                                                    |
|--------------|----------------------------------------------------------------|
| `attachment` | Colour for attachment headers                                  |
| `bold`       | Highlighting bold patterns in the body of messages             |
| `error`      | Error messages printed by NeoMutt                              |
| `hdrdefault` | Default colour of the message header in the pager              |
| `indicator`  | Arrow or bar used to indicate the current item in a menu       |
| `markers`    | The `+` markers at the beginning of wrapped lines in the pager |
| `message`    | Informational messages                                         |
| `normal`     | Default colour for all text                                    |
| `options`    | The key letters in multi-choice questions                      |
| `progress`   | Visual progress bar                                            |
| `prompt`     | A question                                                     |
| `search`     | Highlighting of words in the pager                             |
| `signature`  | Email's signature lines (.sig)                                 |
| `tilde`      | The `~` used to pad blank lines in the pager                   |
| `tree`       | Thread tree drawn in the message index and attachment menu     |
| `underline`  | Highlighting underlined patterns in the body of messages       |
| `warning`    | Warning messages                                               |

## Sidebar Colour Objects

| Object               | Description                                                      |
|----------------------|------------------------------------------------------------------|
| `sidebar_background` | The entire sidebar panel                                         |
| `sidebar_divider`    | The dividing line between the Sidebar and the Index/Pager panels |
| `sidebar_flagged`    | Mailboxes containing flagged mail                                |
| `sidebar_highlight`  | Cursor to select a mailbox                                       |
| `sidebar_indicator`  | The mailbox open in the Index panel                              |
| `sidebar_new`        | Mailboxes containing new mail                                    |
| `sidebar_ordinary`   | Mailboxes that have no new/flagged mails, etc                    |
| `sidebar_spool_file` | Mailbox that receives incoming mail                              |
| `sidebar_unread`     | Mailboxes containing unread mail                                 |

## Compose Colour Objects

| Object                     | Description                          |
|----------------------------|--------------------------------------|
| `compose_header`           | Header labels, e.g. `From:`          |
| `compose_security_encrypt` | Mail will be encrypted               |
| `compose_security_sign`    | Mail will be signed                  |
| `compose_security_both`    | Mail will be encrypted and signed    |
| `compose_security_none`    | Mail will not be encrypted or signed |

## Quoted Email Colours

The quoted email colours don't use a pattern. The first colour, `quoted`, provides a default colour for all quoted text.
Each different level of quoting can be given a different colour using `quoted1` through `quoted9`.

| Object    | Description                                           |
|-----------|-------------------------------------------------------|
| `quoted`  | Text matching `$quote_regex` in the body of a message |
| `quoted1` | 1 level deeper quoted text, e.g. `> > text`           |
| `quoted2` | 2 level deeper quoted text, e.g. `> > > text`         |
| ...       | ...                                                   |
| `quoted9` | 9 level deeper quoted text                            |

(command-syntax)=
## Command Syntax

```neomuttrc
color object [attribute ...] foreground background
color {header | body} [attribute ...] foreground background regex
color index [attribute ...] foreground background [pattern]
color status [attribute ...] foreground background [regex [num]]

uncolor object
uncolor {index | header | body} {* | pattern [...]}
uncolor status {* | regex [...]}
```

## ANSI Escape Sequences

NeoMutt's pager recognises ANSI escape sequences embedded in message text and renders them as colour and attribute changes.
Sequences use the format `ESC[Ps;Ps;...m` (e.g., `\e[1;32m` for bold green, `\e[0m` to reset).

### Set Attributes

| Code | Effect                                    |
|------|-------------------------------------------|
| `0`  | Normal (reset all attributes and colours) |
| `1`  | Bold                                      |
| `3`  | Italic                                    |
| `4`  | Underline                                 |
| `5`  | Blink                                     |
| `7`  | Reverse video                             |

### Clear Attributes

| Code | Effect              |
|------|---------------------|
| `22` | Clear bold          |
| `23` | Clear italic        |
| `24` | Clear underline     |
| `25` | Clear blink         |
| `27` | Clear reverse video |

### Foreground Colours

| Code         | Effect                                                                           |
|--------------|----------------------------------------------------------------------------------|
| `30`–`37`    | Basic foreground colours (black, red, green, yellow, blue, magenta, cyan, white) |
| `38;5;n`     | 256-colour palette foreground (`n` = 0–255)                                      |
| `38;2;R;G;B` | True colour (24-bit RGB) foreground                                              |
| `39`         | Default foreground colour                                                        |

### Background Colours

| Code         | Effect                                              |
|--------------|-----------------------------------------------------|
| `40`–`47`    | Basic background colours (same order as foreground) |
| `48;5;n`     | 256-colour palette background (`n` = 0–255)         |
| `48;2;R;G;B` | True colour (24-bit RGB) background                 |
| `49`         | Default background colour                           |
