---
title: Use Multiple Alias Files
description: Split contacts into separate alias files for work, personal, and other groups, and load them with source
keywords: alias, multiple files, source, alias_file, split, work, personal, groups, address book, organisation
---

# Use Multiple Alias Files

## Prerequisites

1. A working alias setup (see [Using the Address Book](../tutorials/address-book)).

## Split Contacts into Separate Files

1. Create one file per group:

```sh
touch ~/.config/neomutt/aliases-personal
touch ~/.config/neomutt/aliases-work
```

2. Move the relevant aliases into each file:

`~/.config/neomutt/aliases-personal`:

```neomuttrc
alias alice Alice Example <alice@example.com>   # tags:friends
alias bob   Bob Builder <bob@example.com>
```

`~/.config/neomutt/aliases-work`:

```neomuttrc
alias carol Carol Davis <carol@company.com>     # tags:work
alias dave  Dave Evans <dave@company.com>        # tags:work
```

## Load All Alias Files

1. Source each file in your `neomuttrc`:

```neomuttrc
source ~/.config/neomutt/aliases-personal
source ~/.config/neomutt/aliases-work
```

Expected result: all aliases from both files are available at address prompts.

## Set alias_file for Interactive Saves

[`$alias_file`](cfg-alias-file) can point to only one file.
New aliases created with [`<create-alias>`](fn-create-alias) (pressing {kbd}`a` on a message) are saved there.

1. Choose the file you want new aliases saved to:

```neomuttrc
set alias_file = "~/.config/neomutt/aliases-personal"
```

Expected result: pressing {kbd}`a` on a message appends the alias to the personal file.

## Reload After Changes

After editing any alias file, reload it:

```
:source ~/.config/neomutt/aliases-work
```

Or reload all files at once by re-sourcing your main config:

```
:source ~/.config/neomutt/neomuttrc
```

Expected result: changes take effect without restarting NeoMutt.

See [Manage Aliases](aliases) for the full alias syntax and [Using the Address Book](../tutorials/address-book) for the setup tutorial.
