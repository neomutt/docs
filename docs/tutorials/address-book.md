---
title: Using the Address Book
description: Create an alias file, add your first contact, and use the address book to send an email in NeoMutt
keywords: neomutt, address book, alias, contacts, alias_file, source, compose, tutorial
diataxis_type: tutorial
---

# Using the Address Book

This tutorial walks you through creating a simple address book, adding a contact, and using it to send an email.
By the end you will have a working alias file that NeoMutt loads automatically.

If you haven't configured NeoMutt yet, start with [Writing Your First Configuration](first-config).

## Choose Where to Store Aliases

1. Add these lines to your `neomuttrc`:

```neomuttrc
set alias_file = "~/.config/neomutt/aliases"
source ~/.config/neomutt/aliases
```

`alias_file` tells NeoMutt where to save new aliases created interactively.
The `source` line loads existing aliases when NeoMutt starts.

2. Create the file so NeoMutt can source it without error:

```sh
touch ~/.config/neomutt/aliases
```

## Add Your First Contact

1. Open `~/.config/neomutt/aliases` in your editor and add a line:

```neomuttrc
alias alice Alice Example <alice@example.com>
```

The format is: `alias` *shortname* *Real Name* `<email@address>`.

2. Save the file.

## Load the Alias File

1. Start NeoMutt (or, if already running, reload with `:source ~/.config/neomutt/aliases`).

Expected result: NeoMutt loads without errors.

## Open the Address Book

1. At any address prompt (e.g. after pressing {kbd}`m` to compose), press {kbd}`<Tab>` with an empty field.

Expected result: the alias menu appears showing your `alice` entry.

2. Select the alias and press {kbd}`<Enter>`.

Expected result: NeoMutt inserts `Alice Example <alice@example.com>` into the address field.

## Send a Message Using an Alias

1. Press {kbd}`m` to compose a new message.
2. At the `To:` prompt, type `alice` and press {kbd}`<Tab>`.

Expected result: NeoMutt expands the alias to the full address.

3. Enter a subject, write a message, and send.

Expected result: the message is addressed to `alice@example.com`.

## Save a Contact from a Received Message

1. Open a message in the index or pager.
2. Press {kbd}`a` (the default binding for `<create-alias>`).
3. NeoMutt prompts you to confirm or edit the alias name.

Expected result: a new `alias` line is appended to [`$alias_file`](cfg-alias-file).

4. Reload the file so the new alias is available immediately:

```
:source ~/.config/neomutt/aliases
```

## Add More Contacts

1. Open your alias file and add more entries:

```neomuttrc
alias bob    Bob Builder <bob@example.com>
alias team   alice, bob
```

The last line creates a group alias that expands to multiple addresses.

2. Reload with `:source` or restart NeoMutt.

Expected result: typing `team` at an address prompt expands to both Alice and Bob.

## Next Steps

- "I want to customise the alias display." See [Customise Alias Display](../howto/alias-display).
- "I want to split contacts into multiple files." See [Use Multiple Alias Files](../howto/alias-multiple-files).
- "I want to search my contacts faster." See [Find a Contact Quickly](../howto/alias-search).
- "I want to use an external address book." See [Set Up Address Book Integration](../howto/address-book) and [External Address Queries](../howto/address-query).
