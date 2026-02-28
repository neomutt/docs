---
title: Pipe Variables
description: NeoMutt configuration variables for piping messages to external commands.
keywords: neomutt, pipe, pipe_decode, pipe_decode_weed, pipe_sep, pipe_split, configuration
---

# Pipe Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

(pipe-decode)=
## `$pipe_decode`

- **Type:** boolean
- **Default:** `no`

Used in connection with the `<pipe-message>` function. When *unset*, NeoMutt will pipe the messages without any preprocessing. When *set*, NeoMutt will attempt to decode the messages first.

Also see [`$pipe_decode_weed`](#pipe-decode-weed), which controls whether headers will be weeded when this is *set*.

(pipe-decode-weed)=
## `$pipe_decode_weed`

- **Type:** boolean
- **Default:** `yes`

For `<pipe-message>`, when [`$pipe_decode`](#pipe-decode) is set, this further controls whether NeoMutt will weed headers.

(pipe-sep)=
## `$pipe_sep`

- **Type:** string
- **Default:** `"\n"`

The separator to add between messages when piping a list of tagged messages to an external Unix command.

(pipe-split)=
## `$pipe_split`

- **Type:** boolean
- **Default:** `no`

Used in connection with the `<pipe-message>` function following `<tag-prefix>`. If this variable is *unset*, when piping a list of tagged messages NeoMutt will concatenate the messages and will pipe them all concatenated. When *set*, NeoMutt will pipe the messages one by one. In both cases the messages are piped in the current sorted order, and the [`$pipe_sep`](#pipe-sep) separator is added after each message.
