---
title: Speed Up Address Book Access with Key Bindings
description: Bind alias functions and create macros for common address book workflows in NeoMutt
keywords: alias, key bindings, bind, macro, create-alias, query, address book, shortcuts, workflow
---

# Speed Up Address Book Access with Key Bindings

## Prerequisites

1. A working alias setup (see [Using the Address Book](../tutorials/address-book)).

## Bind the Alias Menu to a Key

The [`<alias-dialog>`](fn-alias-dialog) function opens the full alias list.
By default it may not have a binding in the index.

1. Bind it to a convenient key:

```neomuttrc
bind index,pager a alias-dialog
```

2. Press {kbd}`a` in the index to open the alias menu directly.

Expected result: the alias menu opens and you can select a contact to compose a message to.

## Create a Macro to Save and Reload Aliases

The default [`<create-alias>`](fn-create-alias) ({kbd}`a`) appends to [`$alias_file`](cfg-alias-file) but doesn't reload it.

1. Create a macro that saves and reloads in one step:

```neomuttrc
macro index,pager A "<create-alias><enter-command>source $alias_file<Enter>" "Save alias and reload"
```

2. Open a message and press {kbd}`A`.

Expected result: the alias is saved and immediately available without a manual [`:source`](cmd-source).

## Bind a Key for External Queries

If you use [`$query_command`](cfg-query-command) (abook, khard, LDAP):

1. Bind a key for quick queries from the index:

```neomuttrc
bind index,pager Q <query>
```

2. Press {kbd}`Q`, enter a search term, and select a result.

Expected result: the query menu opens and you can compose a message to the selected address.

## Create a Macro to Open a Specific Alias File

If you split aliases into multiple files, you can create a macro to edit one quickly:

```neomuttrc
macro index,pager \ea "<shell-escape>$EDITOR ~/.config/neomutt/aliases-work<Enter><enter-command>source ~/.config/neomutt/aliases-work<Enter>" "Edit and reload work aliases"
```

Expected result: pressing {kbd}`Alt-a` opens your editor on the work alias file, and reloads it when you return.

See [Customise Key Bindings](key-bindings) for the full [`:bind`](cmd-bind) and [`:macro`](cmd-macro) syntax and [Macros](macros) for more macro examples.
