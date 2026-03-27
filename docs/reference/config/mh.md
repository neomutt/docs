---
title: MH Options
description: Configuration variables for MH mailbox format, including message deletion, and sequence names for flags.
keywords: neomutt, mh, mh_purge, mh_seq_flagged, mh_seq_replied, mh_seq_unseen, mailbox format, mail storage, message sequences
---

# MH Options

(mh-purge)=
## `$mh_purge`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set mh_purge = no
    ```

When _unset_, NeoMutt will mimic mh's behavior and rename deleted messages to _,<old file name>_ in mh folders instead of really deleting them.
This leaves the message on disk but makes programs reading the folder ignore it.
If the variable is _set_, the message files will simply be deleted.

This option is similar to [$maildir_trash](maildir-trash) for Maildir folders.

--------------------------------------------------------------------------------

(mh-seq-flagged)=
## `$mh_seq_flagged`

:Type: [String](string)
:Default:
    ```neomuttrc
    set mh_seq_flagged = "flagged"
    ```

The name of the MH sequence used for flagged messages.

--------------------------------------------------------------------------------

(mh-seq-replied)=
## `$mh_seq_replied`

:Type: [String](string)
:Default:
    ```neomuttrc
    set mh_seq_replied = "replied"
    ```

The name of the MH sequence used to tag replied messages.

--------------------------------------------------------------------------------

(mh-seq-unseen)=
## `$mh_seq_unseen`

:Type: [String](string)
:Default:
    ```neomuttrc
    set mh_seq_unseen = "unseen"
    ```

The name of the MH sequence used for unseen messages.

