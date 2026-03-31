---
title: Mbox Options
description: Configuration variable for mbox and mmdf mailbox new-mail detection using file size instead of access time.
keywords: neomutt, mbox, mmdf, check_mbox_size, new mail detection, file size, mailbox format, mail storage
---

(cfg-mbox)=
# Mbox Options

(check-mbox-size)=
## `$check_mbox_size`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set check_mbox_size = no
    ```

When this variable is _set_, NeoMutt will use file size attribute instead of access time when checking for new mail in mbox and mmdf folders.

This variable is _unset_ by default and should only be enabled when new mail detection for these folder types is unreliable or doesn't work.

Note that enabling this variable should happen before any [`mailboxes`](cmd-mailboxes) directives occur in configuration files regarding mbox or mmdf folders because NeoMutt needs to determine the initial new mail status of such a mailbox by performing a fast mailbox scan when it is defined.
Afterwards the new mail status is tracked by file size changes.

