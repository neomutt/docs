---
title: MH Options
description: NeoMutt configuration variables for MH-format mailbox handling.
keywords: neomutt, mh, mh_purge, mh_seq_flagged, mh_seq_replied, mh_seq_unseen, configuration
---

# MH Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

--------------------------------------------------------------------------------

(mh-purge)=
## `$mh_purge`

- **Type:** [Boolean](types.md#bool)
- **Default:**
    ```neomuttrc
    set mh_purge = no
    ```

When _unset_, NeoMutt will mimic mh's behavior and rename deleted messages to _,<old file name>_ in mh folders instead of really deleting them.
This leaves the message on disk but makes programs reading the folder ignore it.
If the variable is _set_, the message files will simply be deleted.

This option is similar to $$maildir_trash for Maildir folders.

--------------------------------------------------------------------------------

(mh-seq-flagged)=
## `$mh_seq_flagged`

- **Type:** [String](types.md#string)
- **Default:**
    ```neomuttrc
    set mh_seq_flagged = "flagged"
    ```

The name of the MH sequence used for flagged messages.

--------------------------------------------------------------------------------

(mh-seq-replied)=
## `$mh_seq_replied`

- **Type:** [String](types.md#string)
- **Default:**
    ```neomuttrc
    set mh_seq_replied = "replied"
    ```

The name of the MH sequence used to tag replied messages.

--------------------------------------------------------------------------------

(mh-seq-unseen)=
## `$mh_seq_unseen`

- **Type:** [String](types.md#string)
- **Default:**
    ```neomuttrc
    set mh_seq_unseen = "unseen"
    ```

The name of the MH sequence used for unseen messages.

