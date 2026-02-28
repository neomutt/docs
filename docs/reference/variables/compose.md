---
title: "Compose Variables"
description: "Reference for NeoMutt compose mode configuration variables."
keywords: "compose, editing, variables, neomutt"
---

# Compose Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

## `$compose_confirm_detach_first`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will prompt for confirmation when trying to use
`<detach-file>` on the first entry in the compose menu. This is to help
prevent irreversible loss of the typed message by accidentally hitting 'D' in
the menu.

Note: NeoMutt only prompts for the first entry.  It doesn't keep track of
which message is the typed message if the entries are reordered, or if the
first entry was already deleted.

## `$compose_format`

- **Type:** string
- **Default:** "`-- NeoMutt: Compose  [Approx. msg size: %l   Atts: %a]%>-`"

Controls the format of the status line displayed in the "compose"
menu.  This string is similar to [`$status_format`](../index.md#status_format), but has its own
set of `printf(3)`-like sequences:

*Short* *Long Name*       *Description*

`%a`    `%{attach-count}` Total number of attachments

`%h`    `%{hostname}`     Local hostname

`%l`    `%{attach-size}`  Approximate size (in bytes) of the current message (see [`formatstrings-size`](../index.md#formatstrings_size))

`%v`    `%{version}`      NeoMutt version string

`%*X`   `%{padding-soft}` Soft-fill with character `X` as pad

`%>X`   `%{padding-hard}` Right justify the rest of the string and pad with character `X`

`%|X`   `%{padding-eol}`  Pad to the end of the line with character `X`

See the text describing the [`$status_format`](../index.md#status_format) option for more
information on how to set [`$compose_format`](../index.md#compose_format).

## `$compose_preview_above_attachments`

- **Type:** boolean
- **Default:** no

Show the message preview above the attachments list.
By default it is shown below it.

## `$compose_preview_min_rows`

- **Type:** number
- **Default:** 5

This variable specifies the minimum number of rows that have to be
available for the message preview window to shown.

## `$compose_show_preview`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will display a preview of message in the compose
view.

## `$compose_show_user_headers`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will display user-defined headers (set via [`my-header`](../index.md#my_header)
or from editing with edit-headers).
