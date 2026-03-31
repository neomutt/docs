---
title: Attach Options
description: Configuration variables for attachment handling, saving, forwarding, bouncing, and MIME multipart options.
keywords: attachment, mime, attach_save_dir, attach_split, bounce, mime_forward, count_alternatives, digest_collapse, message_format, save attachments, forwarding
---

(cfg-attach)=
# Attach Options

(attach-save-dir)=
## `$attach_save_dir`

:Type: [Path (String)](path)
:Default:
    ```neomuttrc
    set attach_save_dir = "./"
    ```

The directory where attachments are saved.

--------------------------------------------------------------------------------

(attach-save-without-prompting)=
## `$attach_save_without_prompting`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set attach_save_without_prompting = no
    ```

This variable, when set to true, will cause attachments to be saved to the 'attach_save_dir' location without prompting the user for the filename.

--------------------------------------------------------------------------------

(attach-sep)=
## `$attach_sep`

:Type: [String](string)
:Default:
    ```neomuttrc
    set attach_sep = "\n"
    ```

The separator to add between attachments when operating (saving, printing, piping, etc) on a list of tagged attachments.

--------------------------------------------------------------------------------

(attach-split)=
## `$attach_split`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set attach_split = yes
    ```

If this variable is _unset_, when operating (saving, printing, piping, etc) on a list of tagged attachments, NeoMutt will concatenate the attachments and will operate on them as a single attachment.
The [$attach_sep](attach-sep) separator is added after each attachment.
When _set_, NeoMutt will operate on the attachments one by one.

--------------------------------------------------------------------------------

(bounce)=
## `$bounce`

:Type: [Quad-Option](quad)
:Default:
    ```neomuttrc
    set bounce = ask-yes
    ```

Controls whether you will be asked to confirm bouncing messages.
If set to _yes_ you don't get asked if you want to bounce a message.
Setting this variable to _no_ is not generally useful, and thus not recommended, because you are unable to bounce messages.

--------------------------------------------------------------------------------

(count-alternatives)=
## `$count_alternatives`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set count_alternatives = no
    ```

When _set_, NeoMutt will recurse inside multipart/alternatives while performing attachment searching and counting (see [`attachments`](cmd-attachments)).

Traditionally, multipart/alternative parts have simply represented different encodings of the main content of the email.
Unfortunately, some mail clients have started to place email attachments inside one of alternatives.
Setting this will allow NeoMutt to find and count matching attachments hidden there, and include them in the index via %X or through ~X pattern matching.

--------------------------------------------------------------------------------

(digest-collapse)=
## `$digest_collapse`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set digest_collapse = yes
    ```

If this option is _set_, NeoMutt's received-attachments menu will not show the subparts of individual messages in a multipart/digest.
To see these subparts, press "v" on that menu.

--------------------------------------------------------------------------------

(message-format)=
## `$message_format`

:Type: [Expando](expando)
:Default:
    ```neomuttrc
    set message_format = "%s"
    ```
:Alternative:
    ```neomuttrc
    set message_format = "%{subject}"
    ```

This is the string displayed in the "attachment" menu for attachments of type `message/rfc822`.  
For a full listing of defined `printf(3)`-like sequences see the section on [$index_format](index-format).

--------------------------------------------------------------------------------

(mime-forward)=
## `$mime_forward`

:Type: [Quad-Option](quad)
:Default:
    ```neomuttrc
    set mime_forward = no
    ```

When _set_, the message you are forwarding will be attached as a separate `message/rfc822` MIME part instead of included in the main body of the message.
This is useful for forwarding MIME messages so the receiver can properly view the message as it was delivered to you.
If you like to switch between MIME and not MIME from mail to mail, set this variable to "ask-no" or "ask-yes".

Also see [$forward_decode](forward-decode) and [$mime_forward_decode](mime-forward-decode).

--------------------------------------------------------------------------------

(mime-forward-rest)=
## `$mime_forward_rest`

:Type: [Quad-Option](quad)
:Default:
    ```neomuttrc
    set mime_forward_rest = yes
    ```

When forwarding multiple attachments of a MIME message from the attachment menu, attachments which can't be decoded in a reasonable manner will be attached to the newly composed message if this option is _set_.

