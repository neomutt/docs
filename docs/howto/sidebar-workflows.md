---
title: How to Organize Mailboxes with the Sidebar
description: Build a mailbox navigation workflow using the NeoMutt sidebar
keywords: sidebar, mailboxes, named-mailboxes, sidebar_format, sidebar-pin
---

# How to Organize Mailboxes with the Sidebar

## Prerequisites

1. Sidebar enabled (`set sidebar_visible`).
2. Mailboxes defined with the `mailboxes` command.

## Give Mailboxes Friendly Names

1. Define named mailboxes for clarity:

```neomuttrc
named-mailboxes "Work INBOX" "imaps://imap.work.example/INBOX"
named-mailboxes "Personal INBOX" "imaps://imap.personal.example/INBOX"
```

Expected result: the sidebar shows descriptive names instead of raw paths.

## Pin Important Mailboxes

1. Always show key folders:

```neomuttrc
sidebar-pin "Work INBOX" "Personal INBOX"
```

Expected result: pinned mailboxes remain visible even when filters are enabled.

## Keep the Sidebar Focused

1. Hide empty folders:

```neomuttrc
set sidebar_non_empty_mailbox_only = yes
```

2. Or show only mailboxes with new or flagged mail:

```neomuttrc
set sidebar_new_mail_only = yes
```

Expected result: the sidebar stays compact and actionable.

## Customize the Sidebar Format

1. Show counts in the sidebar:

```neomuttrc
set sidebar_format = "%D%* %<N?%N/>%S"
```

Expected result: you can see new and total message counts at a glance.

See [How to Use the Sidebar](sidebar) for full options.
