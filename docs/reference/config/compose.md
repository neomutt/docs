---
title: "Compose Options"
description: "Reference for NeoMutt compose mode configuration variables."
keywords: "compose, editing, variables, neomutt"
---

# Compose Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::


compose.md
	  { "compose_confirm_detach_first", DT_BOOL, true, 0, NULL,
	  { "compose_format", DT_EXPANDO|D_L10N_STRING, IP N_("-- NeoMutt: Compose  [Approx. msg size: %l   Atts: %a]%>-"), IP &ComposeFormatDef, NULL,
	  { "compose_show_preview", DT_BOOL, true, 0, NULL,
	  { "compose_show_user_headers", DT_BOOL, true, 0, NULL,
	  { "compose_preview_min_rows", DT_NUMBER|D_INTEGER_NOT_NEGATIVE, 5, 0, NULL,
	  { "compose_preview_above_attachments", DT_BOOL, false, 0, NULL,
	  { "copy", DT_QUAD, MUTT_YES, 0, NULL,
	  { "edit_headers", DT_BOOL, false, 0, NULL,
	  { "ispell", DT_STRING|D_STRING_COMMAND, IP ISPELL, 0, NULL,
	  { "postpone", DT_QUAD, MUTT_ASKYES, 0, NULL,
	  { "edit_hdrs", DT_SYNONYM, IP "edit_headers", IP "2021-03-21" },

----------------------------------------------------------------------------------------------------------

(compose-confirm-detach-first)=
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

----------------------------------------------------------------------------------------------------------

(compose-format)=
## `$compose_format`

- **Type:** string
- **Default:** "`-- NeoMutt: Compose  [Approx. msg size: %l   Atts: %a]%>-`"

Controls the format of the status line displayed in the "compose"
menu.  This string is similar to [`$status_format`](#status-format), but has its own
set of `printf(3)`-like sequences:

| Short  | Long Name           | Description                                                              |
|--------|---------------------|--------------------------------------------------------------------------|
| `%a`   | `%{attach-count}`   | Total number of attachments                                              |
| `%h`   | `%{hostname}`       | Local hostname                                                           |
| `%l`   | `%{attach-size}`    | Approximate size (in bytes) of the current message (see **Size Format**) |
| `%v`   | `%{version}`        | NeoMutt version string                                                   |
| `%*X`  | `%{padding-soft:X}` | Soft-fill with character `X` as pad                                      |
| `%>X`  | `%{padding-hard:X}` | Right justify the rest of the string and pad with character `X`          |
| `%\|X` | `%{padding-eol:X}`  | Pad to the end of the line with character `X`                            |

See the text describing the [`$status_format`](#status-format) option for more
information on how to set [`$compose_format`](#compose-format).

----------------------------------------------------------------------------------------------------------

(compose-show-preview)=
## `$compose_show_preview`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will display a preview of message in the compose
view.

----------------------------------------------------------------------------------------------------------

(compose-show-user-headers)=
## `$compose_show_user_headers`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will display user-defined headers (set via `my_header`
or from editing with edit-headers).

----------------------------------------------------------------------------------------------------------

(compose-preview-min-rows)=
## `$compose_preview_min_rows`

- **Type:** number
- **Default:** 5

This variable specifies the minimum number of rows that have to be
available for the message preview window to shown.

----------------------------------------------------------------------------------------------------------

(compose-preview-above-attachments)=
## `$compose_preview_above_attachments`

- **Type:** boolean
- **Default:** no

Show the message preview above the attachments list.
By default it is shown below it.

----------------------------------------------------------------------------------------------------------

(copy)=
## `$copy`

- **Type:** quadoption
- **Default:** yes

This variable controls whether or not copies of your outgoing messages
will be saved for later references.  Also see [$record](#record),
[$save_name](#save-name), [$force_name](#force-name) and "`fcc-hook`".

----------------------------------------------------------------------------------------------------------

(edit-headers)=
## `$edit_headers`

- **Type:** boolean
- **Default:** no

This option allows you to edit the header of your outgoing messages
along with the body of your message.

Although the compose menu may have localized header labels, the
labels passed to your editor will be standard [RFC2822](https://www.rfc-editor.org/rfc/rfc2822.html) headers,
(e.g. To:, Cc:, Subject:).  Headers added in your editor must
also be [RFC2822](https://www.rfc-editor.org/rfc/rfc2822.html) headers, or one of the pseudo headers listed in
"`edit-header`".  NeoMutt will not understand localized header
labels, just as it would not when parsing an actual email.

**Note** that changes made to the References: and Date: headers are
ignored for interoperability reasons.

----------------------------------------------------------------------------------------------------------

(ispell)=
## `$ispell`

- **Type:** command
- **Default:** "`ispell`"

How to invoke ispell (GNU's spell-checking software).

----------------------------------------------------------------------------------------------------------

(postpone)=
## `$postpone`

- **Type:** quadoption
- **Default:** ask-yes

Controls whether or not messages are saved in the [$postponed](#postponed)
mailbox when you elect not to send immediately. If set to
*ask-yes* or *ask-no*, you will be prompted with "Save
(postpone) draft message?" when quitting from the "compose"
screen.

Also see the [$recall](#recall) variable.

