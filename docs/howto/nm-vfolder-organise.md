---
title: Organise Multiple Virtual Mailboxes
description: Name, group, and order Notmuch virtual mailboxes to keep the sidebar and browser manageable
keywords: notmuch, virtual mailbox, organise, sidebar, named-mailboxes, virtual-mailboxes, order, naming, prefix, group
---

# Organise Multiple Virtual Mailboxes

## Prerequisites

1. Two or more Notmuch virtual mailboxes already configured (see [Getting Started with Notmuch Virtual Mailboxes](../tutorials/notmuch-virtual-mailboxes)).

## Use Clear, Consistent Names

1. Choose short, descriptive labels:

```neomuttrc
virtual-mailboxes "Inbox"   "notmuch://?query=tag:inbox"
virtual-mailboxes "Unread"  "notmuch://?query=tag:inbox and tag:unread"
virtual-mailboxes "Flagged" "notmuch://?query=tag:flagged"
virtual-mailboxes "Sent"    "notmuch://?query=tag:sent"
```

Expected result: the sidebar and browser show a readable list.

## Group by Prefix

1. Prefix related mailboxes to create visual groups:

```neomuttrc
virtual-mailboxes "Work/Inbox"   "notmuch://?query=tag:work and tag:inbox"
virtual-mailboxes "Work/Unread"  "notmuch://?query=tag:work and tag:unread"
virtual-mailboxes "Work/Flagged" "notmuch://?query=tag:work and tag:flagged"
virtual-mailboxes "Personal/Inbox"  "notmuch://?query=tag:personal and tag:inbox"
virtual-mailboxes "Personal/Unread" "notmuch://?query=tag:personal and tag:unread"
```

Expected result: the sidebar shows mailboxes grouped under `Work/` and `Personal/`.

If the sidebar is configured with `$sidebar_short_path` and `$sidebar_delim_chars`, it can shorten these paths into an indented tree.

## Control the Order

Virtual mailboxes appear in the sidebar and browser in the order they are declared in your config.

1. Put the most-used mailboxes first:

```neomuttrc
virtual-mailboxes "Inbox"   "notmuch://?query=tag:inbox"
virtual-mailboxes "Unread"  "notmuch://?query=tag:inbox and tag:unread"
virtual-mailboxes "Flagged" "notmuch://?query=tag:flagged"
virtual-mailboxes "Archive" "notmuch://?query=tag:archive"
```

Expected result: the mailboxes you check most often are at the top.

## Hide Low-Traffic Mailboxes

1. Use `$sidebar_new_mail_only` to show only mailboxes with new or flagged mail:

```neomuttrc
set sidebar_new_mail_only
```

2. Pin important mailboxes so they always appear:

```neomuttrc
sidebar-pin "Inbox" "Flagged"
```

Expected result: quiet mailboxes are hidden until they receive new mail.

## Move Mailbox Definitions to a Separate File

1. Create `~/.config/neomutt/virtual-mailboxes`:

```neomuttrc
virtual-mailboxes "Inbox"   "notmuch://?query=tag:inbox"
virtual-mailboxes "Unread"  "notmuch://?query=tag:inbox and tag:unread"
virtual-mailboxes "Flagged" "notmuch://?query=tag:flagged"
```

2. Source it from your main config:

```neomuttrc
source ~/.config/neomutt/virtual-mailboxes
```

Expected result: your main config stays short and mailbox definitions are easy to edit separately.

See [Sidebar](sidebar) for display options and [Sidebar Workflows](sidebar-workflows) for navigation tips.
