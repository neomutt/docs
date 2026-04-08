---
title: Getting Started with Notmuch Virtual Mailboxes
description: View mail in NeoMutt using Notmuch queries as virtual mailboxes — from your first query to multiple query-backed views
keywords: neomutt, notmuch, virtual mailbox, virtual-mailboxes, query, tag, vfolder, tutorial
diataxis_type: tutorial
---

# Getting Started with Notmuch Virtual Mailboxes

In this tutorial you will turn Notmuch search queries into virtual mailboxes inside NeoMutt.
You'll verify your Notmuch database, write a query, add it as a virtual mailbox, and open it.
By the end you'll have multiple query-backed views of your mail.

This tutorial assumes your mail is already indexed by Notmuch.
If not, complete [Setting Up Notmuch for Email Search](notmuch-setup) first.

## Check Your Notmuch Setup

1. Run a quick search from the command line:

```sh
notmuch search tag:inbox
```

Expected result: a list of message threads.

If the output is empty:

1. Run `notmuch new` to index any new mail.
2. Confirm that the database path in your Notmuch config matches your Maildir location:

```sh
notmuch config get database.path
```

## Create Your First Query

A Notmuch query selects messages by tags, sender, date, or full-text content.

1. Try a simple query that combines two tags:

```sh
notmuch search tag:inbox and tag:unread
```

- `tag:inbox` — messages in the inbox.
- `tag:unread` — messages you haven't read.
- `and` — both conditions must match.

Expected result: only unread inbox messages are listed.

## Add a Virtual Mailbox in NeoMutt

1. Add these lines to your `neomuttrc`:

```neomuttrc
set virtual_spool_file = yes
virtual-mailboxes "Unread" "notmuch://?query=tag:inbox and tag:unread"
```

- `"Unread"` is the label NeoMutt shows in the sidebar and mailbox browser.
- `notmuch://?query=...` tells NeoMutt to populate the mailbox from the query result.

## Open the Virtual Mailbox

1. Start NeoMutt.
2. Navigate to the mailbox list — use the sidebar, or press {kbd}`c` then {kbd}`?` to open the browser.
3. Select **Unread**.

Expected result: the index shows only messages that match `tag:inbox and tag:unread`.
Messages from different physical folders appear together in one unified view.

## Add Another Virtual Mailbox

1. Append a second entry to your config:

```neomuttrc
virtual-mailboxes "Flagged" "notmuch://?query=tag:flagged"
```

2. Restart NeoMutt or reload the config with `:source`.

Expected result: both **Unread** and **Flagged** appear in your mailbox list, each showing a different slice of your mail.

## What Just Happened

Notmuch stores your mail in a Maildir and maintains a database of tags alongside it.
Each query selects a subset of messages based on those tags (or sender, date, body text, etc.).
NeoMutt presents each query result as if it were a regular mailbox — you read, reply, and tag messages the same way you would in any other folder.

The key difference is that virtual mailboxes are dynamic: their contents change as messages are tagged or new mail arrives and is indexed.

## Next Steps

- "I want to build more queries." See [Create a Virtual Mailbox for Unread Mail](../howto/nm-vfolder-unread) and [Combine Multiple Conditions](../howto/nm-vfolder-combine).
- "I want to organise my mailbox list." See [Organise Multiple Virtual Mailboxes](../howto/nm-vfolder-organise).
- "I want to tag messages as a workflow." See [Organising Email with Tags](tags-workflow) and [Use Tags as a Workflow](../howto/nm-vfolder-tag-workflow).
- "I want to understand Notmuch query syntax." See [Notmuch](../howto/notmuch).
