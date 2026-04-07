---
title: Attach Options
description: Configuration variables for attachment handling, saving, forwarding, bouncing, and MIME multipart options.
keywords: attachment, mime, attach_save_dir, attach_split, bounce, mime_forward, count_alternatives, digest_collapse, message_format, save attachments, forwarding
---

(ref-cfg-attach)=
# Attach Options

(cfg-attach-save-dir)=
## `$attach_save_dir`

:Description: Default directory where attachments are saved
:Type: [Path (String)](type-path)
:Default:
    ```neomuttrc
    set attach_save_dir = "./"
    ```

The directory where attachments are saved.

--------------------------------------------------------------------------------

(cfg-attach-save-without-prompting)=
## `$attach_save_without_prompting`

:Description: If true, then don't prompt to save
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set attach_save_without_prompting = no
    ```

This variable, when set to true, will cause attachments to be saved to the [`$attach_save_dir`](cfg-attach-save-dir) location without prompting the user for the filename.

--------------------------------------------------------------------------------

(cfg-attach-sep)=
## `$attach_sep`

:Description: Separator to add between saved/printed/piped attachments
:Type: [String](type-string)
:Default:
    ```neomuttrc
    set attach_sep = "\n"
    ```

The separator to add between attachments when operating (saving, printing, piping, etc) on a list of tagged attachments.

--------------------------------------------------------------------------------

(cfg-attach-split)=
## `$attach_split`

:Description: Save/print/pipe tagged messages individually
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set attach_split = yes
    ```

If this variable is _unset_, when operating (saving, printing, piping, etc) on a list of tagged attachments, NeoMutt will concatenate the attachments and will operate on them as a single attachment.
The [`$attach_sep`](cfg-attach-sep) separator is added after each attachment.
When _set_, NeoMutt will operate on the attachments one by one.

--------------------------------------------------------------------------------

(cfg-bounce)=
## `$bounce`

:Description: Confirm before bouncing a message
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set bounce = ask-yes
    ```

Controls whether you will be asked to confirm bouncing messages.
If set to _yes_ you don't get asked if you want to bounce a message.
Setting this variable to _no_ is not generally useful, and thus not recommended, because you are unable to bounce messages.

--------------------------------------------------------------------------------

(cfg-count-alternatives)=
## `$count_alternatives`

:Description: Recurse inside `multipart/alternatives` while counting attachments
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set count_alternatives = no
    ```

When _set_, NeoMutt will recurse inside multipart/alternatives while performing attachment searching and counting.

Traditionally, multipart/alternative parts have simply represented different encodings of the main content of the email.
Unfortunately, some mail clients have started to place email attachments inside one of alternatives.
Setting this will allow NeoMutt to find and count matching attachments hidden there, and include them in the index via `%X` or through `~X` pattern matching.

:::{seealso}
{ref}`cmd-attachments`
:::

--------------------------------------------------------------------------------

(cfg-digest-collapse)=
## `$digest_collapse`

:Description: Hide the subparts of a multipart/digest
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set digest_collapse = yes
    ```

If this option is _set_, NeoMutt's received-attachments menu will not show the subparts of individual messages in a multipart/digest.
To see these subparts, press {kbd}`v` on that menu.

--------------------------------------------------------------------------------

(cfg-message-format)=
## `$message_format`

:Description: Format string for listing attached messages
:Type: [Expando](type-expando)
:Notes: [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set message_format = "%s"
    ```
:Alternative:
    ```neomuttrc
    set message_format = "%{subject}"
    ```

Specify the format of attached messages displayed in the [`Attach Dialog`](tour-attach).

:::{seealso}
- [`$index_format`](cfg-index-format) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-mime-forward)=
## `$mime_forward`

:Description: Forward a message as a `message/RFC822` MIME part
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set mime_forward = no
    ```

When _set_, the message you are forwarding will be attached as a separate `message/rfc822` MIME part instead of included in the main body of the message.
This is useful for forwarding MIME messages so the receiver can properly view the message as it was delivered to you.
If you like to switch between MIME and not MIME from mail to mail, set this variable to "ask-no" or "ask-yes".

:::{seealso}
[`$forward_decode`](cfg-forward-decode), [`$mime_forward_decode`](cfg-mime-forward-decode)
:::

--------------------------------------------------------------------------------

(cfg-mime-forward-rest)=
## `$mime_forward_rest`

:Description: Forward all attachments, even if they can't be decoded
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set mime_forward_rest = yes
    ```

When forwarding multiple attachments of a MIME message from the attachment menu, attachments which can't be decoded in a reasonable manner will be attached to the newly composed message if this option is _set_.

