---
title: IMAP
description: XXX
keywords: XXX
---

# IMAP

Commands for managing IMAP mailbox subscriptions on the server.

(cmd-subscribe-to)=
## `subscribe-to`

Subscribe to an IMAP folder on the server.

- `subscribe-to <imap-uri>`

```neomuttrc
subscribe-to imaps://user@mail.example.com/INBOX
subscribe-to imaps://user@mail.example.com/Lists/neomutt-devel
```

(cmd-unsubscribe-from)=
## `unsubscribe-from`

Unsubscribe from an IMAP folder on the server.

- `unsubscribe-from <imap-uri>`

```neomuttrc
unsubscribe-from imaps://user@mail.example.com/Lists/old-list
```

