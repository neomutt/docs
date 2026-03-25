---
title: Use Notmuch Advanced Queries
description: Build complex Notmuch queries, create virtual mailboxes on the fly, and use windowed time-based searches in NeoMutt.
keywords: notmuch, query, virtual mailbox, nm_query_window_enable, nm_query_window_duration, nm_query_window_timebase, vfolder-from-query, boolean operators, full-text search, windowed queries, named-mailboxes
---

# Use Notmuch Advanced Queries

## Prerequisites

1. Notmuch integration working in NeoMutt.
2. A notmuch database already indexed.

## Build Complex Queries

1. Use boolean operators in a query:

```neomuttrc
named-mailboxes "Important" "notmuch://?query=tag:inbox and tag:flagged"
```

2. Open the mailbox.

Expected result: only messages matching the combined query are shown.

## Create a Virtual Mailbox from a Query

1. Bind the `vfolder-from-query` function:

```neomuttrc
bind index,pager \eX vfolder-from-query
```

2. Press `Esc X` and enter a query such as:

```
tag:inbox and from:boss@example.com
```

Expected result: NeoMutt opens a virtual mailbox using your query.

## Use Windowed Queries

Windowed queries limit results to a moving time window.

1. Enable windowed queries:

```neomuttrc
set nm_query_window_enable = yes
set nm_query_window_duration = 2
set nm_query_window_timebase = "week"
```

2. Ensure important items are always included:

```neomuttrc
set nm_query_window_or_terms = "tag:unread and tag:flagged"
```

Expected result: queries use a rolling two-week window but keep unread/flagged messages visible.

See [How to Use Notmuch](notmuch) for full configuration details.
