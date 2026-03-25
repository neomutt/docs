---
title: Maildir Options
description: "Configuration variables for Maildir mailbox format, including new mail checks, field delimiters, caching, and trash handling."
keywords: neomutt, maildir, maildir_check_cur, maildir_field_delimiter, maildir_header_cache_verify, maildir_trash, check_new, mail storage, mailbox format
---

# Maildir Options

(check-new)=
## `$check_new`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set check_new = yes
    ```

**Note:** this option only affects _maildir_ and _MH_ style mailboxes.

When _set_, NeoMutt will check for new mail delivered while the mailbox is open.
Especially with MH mailboxes, this operation can take quite some time since it involves scanning the directory and checking each file to see if it has already been looked at.
If this variable is _unset_, no check for new mail is performed while the mailbox is open.

--------------------------------------------------------------------------------

(maildir-check-cur)=
## `$maildir_check_cur`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set maildir_check_cur = no
    ```

If _set_, NeoMutt will poll both the new and cur directories of a maildir folder for new messages.
This might be useful if other programs interacting with the folder (e.g. dovecot) are moving new messages to the cur directory.
Note that setting this option may slow down polling for new messages in large folders, since NeoMutt has to scan all cur messages.

--------------------------------------------------------------------------------

(maildir-field-delimiter)=
## `$maildir_field_delimiter`

- **Type:** [String](string)
- **Notes:** {ref}`Not Empty <general>`, {ref}`On Startup <general>`
- **Default:**
    ```neomuttrc
    set maildir_field_delimiter = ":"
    ```

Use the value as maildir field delimiter.
This is a single-character used to accommodate maildir mailboxes on platforms where `:` is not allowed in a filename.
The recommended alternative on such platforms is `;`.
NeoMutt supports all non-alphanumeric values except for `-`, `.`, `\`, `/`.
**Note:** this only applies to maildir-style mailboxes.
Setting it will have no effect on other mailbox types.

**Note:** this only applies to maildir-style mailboxes. Setting it will have no effect on other mailbox types.

--------------------------------------------------------------------------------

(maildir-header-cache-verify)=
## `$maildir_header_cache_verify`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set maildir_header_cache_verify = yes
    ```

Check for Maildir unaware programs other than NeoMutt having modified maildir files when the header cache is in use.
This incurs one `stat(2)` per message every time the folder is opened (which can be very slow for NFS folders).

--------------------------------------------------------------------------------

(maildir-trash)=
## `$maildir_trash`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set maildir_trash = no
    ```

If _set_, messages marked as deleted will be saved with the maildir trashed flag instead of unlinked.
**Note:** this only applies to maildir-style mailboxes.
Setting it will have no effect on other mailbox types.

