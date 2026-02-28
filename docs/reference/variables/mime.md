---
title: MIME Variables
description: NeoMutt configuration variables for MIME message forwarding and type queries.
keywords: neomutt, mime, mime_forward, mime_forward_decode, mime_forward_rest, mime_type_query_command, mime_type_query_first, configuration
---

# MIME Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

## `$mime_forward`

- **Type:** quadoption
- **Default:** `no`

When *set*, the message you are forwarding will be attached as a separate `message/rfc822` MIME part instead of included in the main body of the message. This is useful for forwarding MIME messages so the receiver can properly view the message as it was delivered to you. If you like to switch between MIME and not MIME from mail to mail, set this variable to "ask-no" or "ask-yes".

Also see `$forward_decode` and [`$mime_forward_decode`](#mime_forward_decode).

## `$mime_forward_decode`

- **Type:** boolean
- **Default:** `no`

Controls the decoding of complex MIME messages into `text/plain` when forwarding a message while [`$mime_forward`](#mime_forward) is *set*. Otherwise `$forward_decode` is used instead.

## `$mime_forward_rest`

- **Type:** quadoption
- **Default:** `yes`

When forwarding multiple attachments of a MIME message from the attachment menu, attachments which can't be decoded in a reasonable manner will be attached to the newly composed message if this option is *set*.

## `$mime_type_query_command`

- **Type:** command
- **Default:** (empty)

This specifies a command to run, to determine the mime type of a new attachment when composing a message. Unless [`$mime_type_query_first`](#mime_type_query_first) is set, this will only be run if the attachment's extension is not found in the mime.types file.

The string may contain a "%s", which will be substituted with the attachment filename. NeoMutt will add quotes around the string substituted for "%s" automatically according to shell quoting rules, so you should avoid adding your own. If no "%s" is found in the string, NeoMutt will append the attachment filename to the end of the string.

The command should output a single line containing the attachment's mime type.

Suggested values are "xdg-mime query filetype" or "file -bi".

## `$mime_type_query_first`

- **Type:** boolean
- **Default:** `no`

When *set*, the [`$mime_type_query_command`](#mime_type_query_command) will be run before the mime.types lookup.
