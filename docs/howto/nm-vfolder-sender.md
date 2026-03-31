---
title: Show Mail from a Specific Person
description: Create a Notmuch virtual mailbox that filters messages by sender address or domain
keywords: notmuch, virtual mailbox, sender, from, filter, domain, virtual-mailboxes, vfolder
---

# Show Mail from a Specific Person

## Prerequisites

1. Notmuch integration working in NeoMutt (see [Setting Up Notmuch](../tutorials/notmuch-setup)).

## Filter by Sender Address

1. Add a virtual mailbox for a specific sender:

```neomuttrc
virtual-mailboxes "Alice" "notmuch://?query=from:alice@example.com"
```

2. Open the mailbox.

Expected result: only messages from `alice@example.com` are shown.

## Filter by Domain

1. Use a domain-level query to match anyone at a company:

```neomuttrc
virtual-mailboxes "ACME Corp" "notmuch://?query=from:@acme.com"
```

Expected result: messages from any address at `acme.com` are shown.

## Combine with Other Conditions

1. Show only unread messages from a sender:

```neomuttrc
virtual-mailboxes "Alice Unread" "notmuch://?query=from:alice@example.com and tag:unread"
```

Expected result: the mailbox shows only unread messages from Alice.

See [Combine Multiple Conditions](nm-vfolder-combine) for more complex queries.
