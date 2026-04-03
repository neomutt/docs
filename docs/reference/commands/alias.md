---
title: Aliases & Address Groups
description: Commands for creating email aliases, defining alternate addresses, and organizing contacts into named address groups.
keywords: alias, unalias, alternates, unalternates, group, ungroup, address book, contacts, email aliases, address groups, shortcuts, neomutt configuration
---

(ref-cmd-alias)=
# Aliases & Address Groups

Commands for defining email address aliases, alternate addresses, and address groups.

(cmd-alias)=
## `alias`

Create a short name for one or more email addresses.

- `alias <key> <address>` — simple alias
- `alias <key> <addr1>, <addr2>` — alias to multiple addresses
- `alias -group <name> <key> <address>` — add alias to a group

```neomuttrc
alias jd jane@example.com
alias jd Jane Doe <jane@example.com>
alias team alice@co.com, bob@co.com, carol@co.com
alias -group work boss Boss Person <boss@company.com>
```

(cmd-unalias)=
## `unalias`

Remove an alias.

- `unalias *` — remove all aliases
- `unalias <key>` — remove a specific alias

```neomuttrc
unalias *
unalias jd
```

(cmd-alternates)=
## `alternates`

Define alternate email addresses that belong to the user.  NeoMutt uses
these to tell "sent" mail from "received".

- `alternates <regex>` — add an alternate address pattern

```neomuttrc
alternates jane@example.com
alternates "jane@(work|home)\\.example\\.com"
alternates -group work "jane\\.doe@company\\.com"
```

(cmd-unalternates)=
## `unalternates`

Remove patterns from the alternates list.

- `unalternates *` — remove all
- `unalternates <regex>` — remove a specific pattern

```neomuttrc
unalternates *
unalternates jane@example.com
```

(cmd-group)=
## `group`

Add addresses to a named address group.  Groups can be used in hook patterns.

- `group -group <name> -addr <address>` — add a single address
- `group -group <name> -rx <regex>` — add addresses matching a pattern

```neomuttrc
group -group friends -addr alice@example.com
group -group friends -addr alice@example.com -addr bob@example.com
group -group coworkers -rx "@company\\.com$"
```

(cmd-ungroup)=
## `ungroup`

Remove addresses from a group.

- `ungroup -group <name> *` — remove all addresses from the group
- `ungroup -group <name> -addr <address>` — remove a specific address

```neomuttrc
ungroup -group friends *
ungroup -group friends -addr alice@example.com
```

