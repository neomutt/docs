---
title: Create a Virtual Mailbox for Unread Mail
description: Show only unread inbox messages in a Notmuch virtual mailbox in NeoMutt
keywords: notmuch, virtual mailbox, unread, tag:inbox, tag:unread, virtual-mailboxes, vfolder
---

# Create a Virtual Mailbox for Unread Mail

## Prerequisites

1. Notmuch integration working in NeoMutt (see [Setting Up Notmuch](../tutorials/notmuch-setup)).

## Add the Virtual Mailbox

1. Add this line to your `neomuttrc`:

```neomuttrc
virtual-mailboxes "Unread" "notmuch://?query=tag:inbox and tag:unread"
```

2. Restart NeoMutt or reload with `:source`.

## Verify

1. Open the **Unread** mailbox from the sidebar or browser.

Expected result: only unread inbox messages are visible.
Messages you have already read do not appear.

When you read a message and Notmuch removes the `unread` tag, the message disappears from this view the next time the mailbox is refreshed.

See [Getting Started with Notmuch Virtual Mailboxes](../tutorials/notmuch-virtual-mailboxes) for the full tutorial.
