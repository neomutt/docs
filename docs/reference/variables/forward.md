---
title: "Forwarding Variables"
description: "Reference for NeoMutt message forwarding configuration variables."
keywords: "forward, forwarding, variables, neomutt"
---

# Forwarding Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

## `$forward_attachments`

- **Type:** quadoption
- **Default:** ask-yes

When forwarding inline (i.e. [`$mime_forward`](../index.md#mime_forward) *unset* or
answered with "no" and [`$forward_decode`](../index.md#forward_decode) *set*), attachments
which cannot be decoded in a reasonable manner will be attached
to the newly composed message if this quadoption is *set* or
answered with "yes".

## `$forward_attribution_intro`

- **Type:** string
- **Default:** "`----- Forwarded message from %f -----`"

This is the string that will precede a message which has been forwarded
in the main body of a message (when [`$mime_forward`](../index.md#mime_forward) is unset).
For a full listing of defined `printf(3)`-like sequences see
the section on [`$index_format`](../index.md#index_format).  See also [`$attribution_locale`](../index.md#attribution_locale).

## `$forward_attribution_trailer`

- **Type:** string
- **Default:** "`----- End forwarded message -----`"

This is the string that will follow a message which has been forwarded
in the main body of a message (when [`$mime_forward`](../index.md#mime_forward) is unset).
For a full listing of defined `printf(3)`-like sequences see
the section on [`$index_format`](../index.md#index_format).  See also [`$attribution_locale`](../index.md#attribution_locale).

## `$forward_decode`

- **Type:** boolean
- **Default:** yes

Controls the decoding of complex MIME messages into `text/plain` when
forwarding a message.  The message header is also RFC2047 decoded.
This variable is only used, if [`$mime_forward`](../index.md#mime_forward) is *unset*,
otherwise [`$mime_forward_decode`](../index.md#mime_forward_decode) is used instead.

## `$forward_decrypt`

- **Type:** boolean
- **Default:** yes

Controls the handling of encrypted messages when forwarding a message.
When *set*, the outer layer of encryption is stripped off.  This
variable is only used if [`$mime_forward`](../index.md#mime_forward) is *set* and
[`$mime_forward_decode`](../index.md#mime_forward_decode) is *unset*.

## `$forward_edit`

- **Type:** quadoption
- **Default:** yes

This quadoption controls whether or not the user is automatically
placed in the editor when forwarding messages.  For those who always want
to forward with no modification, use a setting of "no".

## `$forward_format`

- **Type:** string
- **Default:** "`[%a: %s]`"

This variable controls the default subject when forwarding a message.
It uses the same format sequences as the [`$index_format`](../index.md#index_format) variable.

## `$forward_quote`

- **Type:** boolean
- **Default:** no

When *set*, forwarded messages included in the main body of the
message (when [`$mime_forward`](../index.md#mime_forward) is *unset*) will be quoted using
[`$indent_string`](../index.md#indent_string).

## `$forward_references`

- **Type:** boolean
- **Default:** no

When *set*, forwarded messages set the "In-Reply-To:" and
"References:" headers in the same way as normal replies would. Hence the
forwarded message becomes part of the original thread instead of starting
a new one.
