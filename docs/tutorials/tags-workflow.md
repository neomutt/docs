---
title: Organising Email with Tags
description: Step-by-step guide to using tags and virtual mailboxes for email organisation in NeoMutt
keywords: [neomutt, tags, notmuch, virtual mailboxes, workflow, tutorial]
---

# Organising Email with Tags

This tutorial uses Notmuch tags to build a simple, repeatable workflow.
If Notmuch is not set up yet, start with [How to Use Notmuch](../howto/notmuch).

## What Are Tags?

Tags are labels attached to messages. One message can have many tags, and tags can drive virtual mailboxes.

## Set Up Notmuch for Tagging

1. Install and initialize notmuch.
2. Configure NeoMutt with a notmuch URL:

```neomuttrc
set nm_default_url = "notmuch:///path/to/your/maildir"
```

3. Add a virtual mailbox for your inbox tag:

```neomuttrc
named-mailboxes "Inbox" "notmuch://?query=tag:inbox"
```

Expected result: you can open the Inbox virtual mailbox from NeoMutt.

## Add and Remove Tags

1. Bind a key for tagging if you do not already have one:

```neomuttrc
bind index,pager \eT modify-tags
```

2. Open a message and press `Esc T`.
3. Add or remove tags as prompted.

Expected result: the message tags change in the notmuch database.

## Search by Tags

1. Use a notmuch query to open a tagged view:

```neomuttrc
named-mailboxes "Action" "notmuch://?query=tag:action"
```

2. Open the mailbox.

Expected result: you see only messages with the `action` tag.

## Create Virtual Mailboxes from Tags

1. Add more tag-based mailboxes:

```neomuttrc
named-mailboxes "Waiting" "notmuch://?query=tag:waiting"
named-mailboxes "Reference" "notmuch://?query=tag:reference"
```

2. Open each mailbox and confirm the filters.

Expected result: virtual mailboxes map directly to tag queries.

## Build a Tag-Based Workflow

1. Triage your inbox and tag items as `action`, `waiting`, or `reference`.
2. Remove the `inbox` tag from items once they are triaged.

Expected result: the Inbox mailbox becomes a short list of untriaged items.

## Display Tags in the Index

1. Update your index format to show tags:

```neomuttrc
set index_format = "%4C %Z %{%b %d} %-15.15F %g %s"
```

Expected result: tags appear next to messages in the index.

See [How to Use Notmuch](../howto/notmuch) for full configuration details.

## Next Steps

- "I want to search by tag quickly." Continue with [Searching and Filtering Email](searching-email).
- "I want to tune my index view." See [Format Strings](../howto/format-strings) and [Index Format](../reference/options).
