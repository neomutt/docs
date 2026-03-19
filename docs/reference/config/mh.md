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


mh.md
	  { "mh_purge", DT_BOOL, false, 0, NULL,
	  { "mh_seq_flagged", DT_STRING, IP "flagged", 0, NULL,
	  { "mh_seq_replied", DT_STRING, IP "replied", 0, NULL,
	  { "mh_seq_unseen", DT_STRING, IP "unseen", 0, NULL,

----------------------------------------------------------------------------------------------------------

(mh-purge)=
## `$mh_purge`

- **Type:** boolean
- **Default:** `no`

When *unset*, NeoMutt will mimic mh's behavior and rename deleted messages to `,<old file name>` in mh folders instead of really deleting them. This leaves the message on disk but makes programs reading the folder ignore it. If the variable is *set*, the message files will simply be deleted.

This option is similar to [`$maildir_trash`](#maildir-trash) for Maildir folders.

----------------------------------------------------------------------------------------------------------

(mh-seq-flagged)=
## `$mh_seq_flagged`

- **Type:** string
- **Default:** `"flagged"`

The name of the MH sequence used for flagged messages.

----------------------------------------------------------------------------------------------------------

(mh-seq-replied)=
## `$mh_seq_replied`

- **Type:** string
- **Default:** `"replied"`

The name of the MH sequence used to tag replied messages.

----------------------------------------------------------------------------------------------------------

(mh-seq-unseen)=
## `$mh_seq_unseen`

- **Type:** string
- **Default:** `"unseen"`

The name of the MH sequence used for unseen messages.

