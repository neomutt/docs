---
title: Show Recent Mail
description: Create a Notmuch virtual mailbox that shows only messages from the last N days, weeks, or months
keywords: notmuch, virtual mailbox, recent, date, time, date range, virtual-mailboxes, vfolder
---

# Show Recent Mail

## Prerequisites

1. Notmuch integration working in NeoMutt (see [Setting Up Notmuch](../../tutorials/notmuch-setup)).

## Show the Last 7 Days

1. Add a virtual mailbox with a date range:

```neomuttrc
virtual-mailboxes "Recent" "notmuch://?query=date:7d..now"
```

2. Open the mailbox.

Expected result: only messages from the last 7 days are shown.

## Adjust the Range

Use Notmuch date syntax to widen or narrow the window:

| Query             | Period         |
|-------------------|----------------|
| `date:1d..now`    | Last 24 hours  |
| `date:7d..now`    | Last 7 days    |
| `date:1m..now`    | Last month     |
| `date:3m..now`    | Last 3 months  |
| `date:1y..now`    | Last year      |

## Combine with Tags

1. Show only recent unread messages:

```neomuttrc
virtual-mailboxes "Recent Unread" "notmuch://?query=date:7d..now and tag:unread"
```

Expected result: the mailbox shows unread messages from the last week.

For rolling time windows managed by NeoMutt, see [Notmuch Advanced Queries](../notmuch-advanced) and the `nm_query_window_*` variables.
