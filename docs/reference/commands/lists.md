---
title: Mailing Lists
description: XXX
keywords: XXX
---

# Mailing Lists

Commands for managing mailing list addresses and subscriptions.

(cmd-lists)=
## `lists`

Mark email addresses as belonging to mailing lists.

- `lists <regex>` — add a mailing list pattern
- `lists -group <name> <regex>` — add a list to a named group

```neomuttrc
lists neomutt-devel@neomutt.org
lists ".*@lists\\.example\\.com"
lists -group work-lists dev-team@company.com
```

(cmd-unlists)=
## `unlists`

Remove addresses from the mailing lists list.

- `unlists *` — remove all
- `unlists <regex>` — remove a specific pattern

```neomuttrc
unlists *
unlists neomutt-devel@neomutt.org
```

(cmd-subscribe)=
## `subscribe`

Mark a mailing list as one the user is subscribed to.  The address must also
be known via `lists`.

- `subscribe <regex>` — subscribe to a list
- `subscribe -group <name> <regex>` — subscribe and add to a group

```neomuttrc
subscribe neomutt-devel@neomutt.org
subscribe -group oss neomutt-users@neomutt.org
```

(cmd-unsubscribe)=
## `unsubscribe`

Remove an address from the subscribed list.

- `unsubscribe *` — unsubscribe from all
- `unsubscribe <regex>` — unsubscribe from a specific list

```neomuttrc
unsubscribe *
unsubscribe neomutt-devel@neomutt.org
```

