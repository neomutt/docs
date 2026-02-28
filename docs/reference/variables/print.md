---
title: Print Variables
description: NeoMutt configuration variables for message printing behavior.
keywords: neomutt, print, print_command, print_decode, print_decode_weed, print_split, configuration
---

# Print Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

## `$print`

- **Type:** quadoption
- **Default:** `ask-no`

Controls whether or not NeoMutt really prints messages. This is set to "ask-no" by default, because some people accidentally hit "p" often.

## `$print_command`

- **Type:** command
- **Default:** `"lpr"`

This specifies the command pipe that should be used to print messages.

## `$print_decode`

- **Type:** boolean
- **Default:** `yes`

Used in connection with the `<print-message>` function. If this option is *set*, the message is decoded before it is passed to the external command specified by [`$print_command`](#print_command). If this option is *unset*, no processing will be applied to the message when printing it. The latter setting may be useful if you are using some advanced printer filter which is able to properly format e-mail messages for printing.

Also see [`$print_decode_weed`](#print_decode_weed), which controls whether headers will be weeded when this is *set*.

## `$print_decode_weed`

- **Type:** boolean
- **Default:** `yes`

For `<print-message>`, when [`$print_decode`](#print_decode) is set, this further controls whether NeoMutt will weed headers.

## `$print_split`

- **Type:** boolean
- **Default:** `no`

Used in connection with the `<print-message>` function. If this option is *set*, the command specified by [`$print_command`](#print_command) is executed once for each message which is to be printed. If this option is *unset*, the command specified by [`$print_command`](#print_command) is executed only once, and all the messages are concatenated, with a form feed as the message separator.

Those who use the `enscript(1)` program's mail-printing mode will most likely want to *set* this option.
