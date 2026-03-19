---
title: Maildir Options
description: NeoMutt configuration variables for Maildir-format mailbox handling.
keywords: neomutt, maildir, maildir_check_cur, maildir_field_delimiter, maildir_header_cache_verify, maildir_trash, configuration
---

# Maildir Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::


maildir.md
	  { "check_new", DT_BOOL, true, 0, NULL,
	  { "maildir_check_cur", DT_BOOL, false, 0, NULL,
	  { "maildir_field_delimiter", DT_STRING|D_NOT_EMPTY|D_ON_STARTUP, IP ":", 0, maildir_field_delimiter_validator,
	  { "maildir_trash", DT_BOOL, false, 0, NULL,
	  { "maildir_header_cache_verify", DT_BOOL, true, 0, NULL,

----------------------------------------------------------------------------------------------------------

(check-new)=
## `$check_new`

- **Type:** boolean
- **Default:** yes

**Note:** this option only affects *maildir* and *MH* style
mailboxes.

When *set*, NeoMutt will check for new mail delivered while the
mailbox is open.  Especially with MH mailboxes, this operation can
take quite some time since it involves scanning the directory and
checking each file to see if it has already been looked at.  If
this variable is *unset*, no check for new mail is performed
while the mailbox is open.

----------------------------------------------------------------------------------------------------------

(maildir-check-cur)=
## `$maildir_check_cur`

- **Type:** boolean
- **Default:** `no`

If *set*, NeoMutt will poll both the new and cur directories of a maildir folder for new messages. This might be useful if other programs interacting with the folder (e.g. dovecot) are moving new messages to the cur directory. Note that setting this option may slow down polling for new messages in large folders, since NeoMutt has to scan all cur messages.

----------------------------------------------------------------------------------------------------------

(maildir-field-delimiter)=
## `$maildir_field_delimiter`

- **Type:** string
- **Default:** `":"`

Use the value as maildir field delimiter. This is a single-character used to accommodate maildir mailboxes on platforms where `:` is not allowed in a filename. The recommended alternative on such platforms is `;`. NeoMutt supports all non-alphanumeric values except for `-`, `.`, `\`, `/`.

**Note:** this only applies to maildir-style mailboxes. Setting it will have no effect on other mailbox types.

----------------------------------------------------------------------------------------------------------

(maildir-trash)=
## `$maildir_trash`

- **Type:** boolean
- **Default:** `no`

If *set*, messages marked as deleted will be saved with the maildir trashed flag instead of unlinked. **Note:** this only applies to maildir-style mailboxes. Setting it will have no effect on other mailbox types.

----------------------------------------------------------------------------------------------------------

(maildir-header-cache-verify)=
## `$maildir_header_cache_verify`

- **Type:** boolean
- **Default:** `yes`

Check for Maildir unaware programs other than NeoMutt having modified maildir files when the header cache is in use. This incurs one `stat(2)` per message every time the folder is opened (which can be very slow for NFS folders).

