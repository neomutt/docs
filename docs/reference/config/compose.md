---
title: Compose Options
description: Configuration variables for the compose menu, message preview, header editing, spell checking, and draft handling.
keywords: compose, compose_format, edit_headers, compose_show_preview, copy, postpone, ispell, spell check, draft, outgoing messages, compose menu
---

(ref-cfg-compose)=
# Compose Options

(cfg-compose-confirm-detach-first)=
## `$compose_confirm_detach_first`

:Description: Prevent the accidental deletion of the composed message
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set compose_confirm_detach_first = yes
    ```

When _set_, NeoMutt will prompt for confirmation when trying to use [`<detach-file>`](ref-fn-compose) on the first entry in the compose menu.
This is to help prevent irreversible loss of the typed message by accidentally hitting 'D' in the menu.

:::{note}
NeoMutt only prompts for the first entry.
It doesn't keep track of which message is the typed message if the entries are reordered, or if the first entry was already deleted.
:::

--------------------------------------------------------------------------------

(cfg-compose-format)=
## `$compose_format`

:Description: Format string for the [Compose Dialog](tour-compose)'s status bar
:Type: [Expando](type-expando)
:Notes: [Localised String](type-general), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set compose_format = "-- NeoMutt: Compose  [Approx. msg size: %l   Atts: %a]%>-"
    ```
:Alternative:
    ```neomuttrc
    set compose_format = "-- NeoMutt: Compose  [Approx. msg size: %{attach-size}   Atts: %{attach-count}]%{padding-hard:-}"
    ```

Specify the format of the data displayed in the [`Compose Dialog`](tour-compose)'s status bar.

**Format Sequences**

| Short  | Long Name           | Description                                                                    |
|--------|---------------------|--------------------------------------------------------------------------------|
| `%a`   | `%{attach-count}`   | Total number of attachments                                                    |
| `%h`   | `%{hostname}`       | Local hostname                                                                 |
| `%l`   | `%{attach-size}`    | Approximate size (in bytes) of the current message (see {ref}`how-bytes-size`) |
| `%v`   | `%{version}`        | NeoMutt version string                                                         |
| `%*X`  | `%{padding-soft:X}` | Soft-fill with character `X` as pad                                            |
| `%>X`  | `%{padding-hard:X}` | Right justify the rest of the string and pad with character `X`                |
| `%\|X` | `%{padding-eol:X}`  | Pad to the end of the line with character `X`                                  |

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-compose-preview-above-attachments)=
## `$compose_preview_above_attachments`

:Description: Show the message preview above the attachments list. By default it is shown below it.
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set compose_preview_above_attachments = no
    ```

Show the message preview above the attachments list.
By default it is shown below it.

--------------------------------------------------------------------------------

(cfg-compose-preview-min-rows)=
## `$compose_preview_min_rows`

:Description: Hide the preview if it has fewer than this number of rows
:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set compose_preview_min_rows = 5
    ```

This variable specifies the minimum number of rows that have to be available for the message preview window to shown.

--------------------------------------------------------------------------------

(cfg-compose-show-preview)=
## `$compose_show_preview`

:Description: Display a preview of the message body in the [Compose Dialog](tour-compose)
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set compose_show_preview = yes
    ```

When _set_, NeoMutt will display a preview of message in the compose view.

--------------------------------------------------------------------------------

(cfg-compose-show-user-headers)=
## `$compose_show_user_headers`

:Description: Controls whether or not custom headers are shown in the compose envelope
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set compose_show_user_headers = yes
    ```

When _set_, NeoMutt will display user-defined headers (set via [`:my-header`](cmd-my-header) or from editing with edit-headers).

--------------------------------------------------------------------------------

(cfg-copy)=
## `$copy`

:Description: Save outgoing emails to [`$record`](cfg-record)
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set copy = yes
    ```

This variable controls whether or not copies of your outgoing messages will be saved for later references.

:::{seealso}
[`$record`](cfg-record), [`$save_name`](cfg-save-name), [`$force_name`](cfg-force-name) and [`:fcc-hook`](cmd-fcc-hook)
:::

--------------------------------------------------------------------------------

(cfg-edit-headers)=
## `$edit_headers`

:Description: Let the user edit the email headers whilst editing an email
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set edit_headers = no
    ```

This option allows you to edit the header of your outgoing messages along with the body of your message.

Although the compose menu may have localized header labels, the labels passed to your editor will be standard [RFC2822](https://www.rfc-editor.org/rfc/rfc2822.html) headers, (e.g. `To:`, `Cc:`, `Subject:`).
Headers added in your editor must also be [RFC2822](https://www.rfc-editor.org/rfc/rfc2822.html) headers, or one of the pseudo headers listed in "$edit-header".
NeoMutt will not understand localized header labels, just as it would not when parsing an actual email.

:::{note}
Changes made to the References: and Date: headers are ignored for interoperability reasons.
:::

--------------------------------------------------------------------------------

(cfg-ispell)=
## `$ispell`

:Description: External command to perform spell-checking
:Type: [Command (String)](type-string)
:Default:
    ```neomuttrc
    set ispell = "ispell"
    ```

How to invoke `ispell` (GNU's spell-checking software).

--------------------------------------------------------------------------------

(cfg-postpone)=
## `$postpone`

:Description: Save messages to the [`$postponed`](cfg-postponed) folder
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set postpone = ask-yes
    ```

Controls whether or not messages are saved in the [`$postponed`](cfg-postponed) mailbox when you elect not to send immediately.
If set to `ask-yes` or `ask-no`, you will be prompted with "Save (postpone) draft message?" when quitting from the [Compose Dialog](tour-compose).

:::{seealso}
[`$recall`](cfg-recall)
:::

