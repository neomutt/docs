---
title: Combine Multiple Query Conditions
description: Build precise Notmuch virtual mailboxes using AND, OR, NOT, and parentheses in queries
keywords: notmuch, virtual mailbox, query, boolean, and, or, not, combine, filter, virtual-mailboxes, vfolder
---

# Combine Multiple Query Conditions

## Prerequisites

1. Notmuch integration working in NeoMutt (see [Setting Up Notmuch](../../tutorials/notmuch-setup)).

## AND — Match All Conditions

1. Use `and` to require multiple criteria:

```neomuttrc
virtual-mailboxes "Work Unread" "notmuch://?query=tag:work and tag:unread"
```

Expected result: only messages that are both tagged `work` and tagged `unread` are shown.

## OR — Match Any Condition

1. Use `or` to accept either criterion:

```neomuttrc
virtual-mailboxes "Team" "notmuch://?query=from:alice@example.com or from:bob@example.com"
```

Expected result: messages from Alice or Bob are shown.

## NOT — Exclude Messages

1. Use `not` to remove unwanted messages:

```neomuttrc
virtual-mailboxes "Inbox Clean" "notmuch://?query=tag:inbox and not tag:spam"
```

Expected result: inbox messages appear, but spam-tagged messages are excluded.

## Parentheses — Group Conditions

1. Use parentheses to control evaluation order:

```neomuttrc
virtual-mailboxes "Priority" \
  "notmuch://?query=tag:inbox and (tag:flagged or tag:unread)"
```

Expected result: inbox messages that are either flagged or unread are shown.

## Test Queries on the Command Line

Before adding a query to your config, test it with `notmuch search`:

```sh
notmuch search 'tag:inbox and (tag:flagged or tag:unread)'
```

Expected result: you see the matching messages, confirming the query is correct before using it in NeoMutt.

See [Notmuch](../notmuch) for the full URL syntax and [Notmuch Advanced Queries](../notmuch-advanced) for windowed queries.
