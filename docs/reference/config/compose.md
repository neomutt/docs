---
title: "Compose Options"
description: "Reference for NeoMutt compose mode configuration variables."
keywords: "compose, editing, variables, neomutt"
---

# Compose Options

(compose-confirm-detach-first)=
## `$compose_confirm_detach_first`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set compose_confirm_detach_first = yes
    ```

When _set_, NeoMutt will prompt for confirmation when trying to use `<detach-file>` on the first entry in the compose menu.
This is to help prevent irreversible loss of the typed message by accidentally hitting 'D' in the menu.

Note: NeoMutt only prompts for the first entry.
It doesn't keep track of which message is the typed message if the entries are reordered, or if the first entry was already deleted.

--------------------------------------------------------------------------------

(compose-format)=
## `$compose_format`

- **Type:** [Expando](expando)
- **Notes:** {ref}`Localised String <general>`
- **Default:**
    ```neomuttrc
    set compose_format = "-- NeoMutt: Compose  [Approx. msg size: %l   Atts: %a]%>-"
    ```

Controls the format of the status line displayed in the "compose" menu.
This string is similar to [$status_format](status-format), but has its own set of `printf(3)`-like sequences:

| Short  | Long Name           | Description                                                              |
|--------|---------------------|--------------------------------------------------------------------------|
| `%a`   | `%{attach-count}`   | Total number of attachments                                              |
| `%h`   | `%{hostname}`       | Local hostname                                                           |
| `%l`   | `%{attach-size}`    | Approximate size (in bytes) of the current message (see **Size Format**) |
| `%v`   | `%{version}`        | NeoMutt version string                                                   |
| `%*X`  | `%{padding-soft:X}` | Soft-fill with character `X` as pad                                      |
| `%>X`  | `%{padding-hard:X}` | Right justify the rest of the string and pad with character `X`          |
| `%\|X` | `%{padding-eol:X}`  | Pad to the end of the line with character `X`                            |

See the text describing the [$status_format](status-format) option for more information on how to set [$compose_format](compose-format).

--------------------------------------------------------------------------------

(compose-preview-above-attachments)=
## `$compose_preview_above_attachments`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set compose_preview_above_attachments = no
    ```

Show the message preview above the attachments list.
By default it is shown below it.

--------------------------------------------------------------------------------

(compose-preview-min-rows)=
## `$compose_preview_min_rows`

- **Type:** [Number](number)
- **Notes:** {ref}`Not Negative <general>`
- **Default:**
    ```neomuttrc
    set compose_preview_min_rows = 5
    ```

This variable specifies the minimum number of rows that have to be available for the message preview window to shown.

--------------------------------------------------------------------------------

(compose-show-preview)=
## `$compose_show_preview`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set compose_show_preview = yes
    ```

When _set_, NeoMutt will display a preview of message in the compose view.

--------------------------------------------------------------------------------

(compose-show-user-headers)=
## `$compose_show_user_headers`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set compose_show_user_headers = yes
    ```

When _set_, NeoMutt will display user-defined headers (set via $my-header or from editing with edit-headers).

--------------------------------------------------------------------------------

(copy)=
## `$copy`

- **Type:** [Quad-Option](quad)
- **Default:**
    ```neomuttrc
    set copy = yes
    ```

This variable controls whether or not copies of your outgoing messages will be saved for later references.
Also see [$record](record), [$save_name](save-name), [$force_name](force-name) and "$fcc-hook".

--------------------------------------------------------------------------------

(edit-headers)=
## `$edit_headers`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set edit_headers = no
    ```

This option allows you to edit the header of your outgoing messages along with the body of your message.

Although the compose menu may have localized header labels, the labels passed to your editor will be standard [RFC2822](https://www.rfc-editor.org/rfc/rfc2822.html) headers, (e.g. To:, Cc:, Subject:).
Headers added in your editor must also be [RFC2822](https://www.rfc-editor.org/rfc/rfc2822.html) headers, or one of the pseudo headers listed in "$edit-header".
NeoMutt will not understand localized header labels, just as it would not when parsing an actual email.

**Note** that changes made to the References: and Date: headers are ignored for interoperability reasons.

--------------------------------------------------------------------------------

(ispell)=
## `$ispell`

- **Type:** [Command (String)](string)
- **Default:**
    ```neomuttrc
    set ispell = "ispell"
    ```

How to invoke ispell (GNU's spell-checking software).

--------------------------------------------------------------------------------

(postpone)=
## `$postpone`

- **Type:** [Quad-Option](quad)
- **Default:**
    ```neomuttrc
    set postpone = ask-yes
    ```

Controls whether or not messages are saved in the [$postponed](postponed) mailbox when you elect not to send immediately.
If set to _ask-yes_ or _ask-no_, you will be prompted with "Save (postpone) draft message?" when quitting from the "compose" screen.

Also see the [$recall](recall) variable.

