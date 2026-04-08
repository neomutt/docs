---
title: Add or Update a Contact
description: Add new aliases, update existing entries, and reload the alias file in NeoMutt
keywords: alias, add contact, update contact, alias_file, source, reload, create-alias, address book
---

# Add or Update a Contact

## Prerequisites

1. An alias file configured via [`$alias_file`](cfg-alias-file) and loaded with `source`.
2. If you haven't set this up, complete [Using the Address Book](../tutorials/address-book) first.

## Add a New Contact Manually

1. Open your alias file ([`$alias_file`](cfg-alias-file)) in your editor.
2. Add an `alias` line:

```neomuttrc
alias carol Carol Davis <carol@example.com>    # tags:work
```

3. Save the file.
4. Reload it in NeoMutt:

```
:source ~/.config/neomutt/aliases
```

Expected result: the new alias is available at address prompts.

## Add a Contact from a Received Message

1. Open a message in the index or pager.
2. Press {kbd}`a` ([`<create-alias>`](fn-create-alias)).
3. Confirm or edit the alias name when prompted.

Expected result: NeoMutt appends the alias to [`$alias_file`](cfg-alias-file).

4. Reload the file so the alias takes effect immediately:

```
:source ~/.config/neomutt/aliases
```

## Update an Existing Contact

1. Open your alias file.
2. Find and edit the alias line.
3. Save and reload with `:source`.

Expected result: the alias expands to the updated address.

## Remove a Contact

1. Delete the alias line from your alias file.
2. Save and reload.

Alternatively, remove it at runtime without editing the file:

```neomuttrc
unalias carol
```

Expected result: the alias is no longer available.

See [Manage Aliases](aliases) for the full alias syntax and [Using the Address Book](../tutorials/address-book) for the setup tutorial.
