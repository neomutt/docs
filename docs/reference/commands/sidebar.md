---
title: Sidebar
description: XXX
keywords: XXX
---

# Sidebar

Commands for pinning/unpinning mailboxes in the sidebar.

## `sidebar-pin`

Pin a mailbox so it is always visible in the sidebar, even if it has no new
mail.

- `sidebar-pin <mailbox> [<mailbox> ...]` — pin one or more mailboxes

```neomuttrc
sidebar-pin =INBOX
sidebar-pin =INBOX =Sent =Drafts
```

## `sidebar-unpin`

Unpin a mailbox from the sidebar.

- `sidebar-unpin *` — unpin all
- `sidebar-unpin <mailbox>` — unpin a specific mailbox

```neomuttrc
sidebar-unpin *
sidebar-unpin =Drafts
```

