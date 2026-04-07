---
title: Mailboxes
description: Commands for defining monitored mailboxes, adding labels, and controlling polling and notification for new mail.
keywords: mailboxes, unmailboxes, named-mailboxes, new mail, polling, notifications, labels, mailbox monitoring, folder management, mail folders
---

(ref-cmd-mailbox)=
# Mailboxes

Commands for defining and managing monitored mailboxes.

(cmd-mailboxes)=
## `:mailboxes`

Define mailboxes that NeoMutt should watch for new mail.

- `mailboxes <mailbox>` — add a single mailbox
- `mailboxes <mailbox1> <mailbox2>` — add multiple mailboxes
- `mailboxes -label <label> <mailbox>` — add with a display label
- `mailboxes -poll <mailbox>` — add and poll for new mail
- `mailboxes -notify <mailbox>` — add and enable desktop notifications

```neomuttrc
mailboxes ~/Mail/INBOX
mailboxes ~/Mail/INBOX ~/Mail/Sent ~/Mail/Drafts
mailboxes imaps://user@mail.example.com/INBOX
mailboxes -label "Work" ~/Mail/work
mailboxes -poll ~/Mail/INBOX
```

(cmd-named-mailboxes)=
## `:named-mailboxes`

Define labelled mailboxes — a label is required for each mailbox.

- `named-mailboxes <label> <mailbox>` — add with a label

```neomuttrc
named-mailboxes "Inbox" +INBOX
named-mailboxes "Sent" +Sent "Drafts" +Drafts
named-mailboxes -poll "Work" imaps://user@work.example.com/INBOX
```

(cmd-unmailboxes)=
## `:unmailboxes`

Remove mailboxes from the watch list.

- `unmailboxes *` — remove all mailboxes
- `unmailboxes <mailbox>` — remove a specific mailbox

```neomuttrc
unmailboxes *
unmailboxes ~/Mail/old-list
```

