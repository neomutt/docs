---
title: Fix Missing or Outdated Aliases
description: Diagnose and fix common alias problems — missing aliases, syntax errors, and stale entries in NeoMutt
keywords: alias, troubleshooting, missing, syntax error, source, alias_file, reload, debug, address book
---

# Fix Missing or Outdated Aliases

## Prerequisites

1. An alias file configured via [`$alias_file`](cfg-alias-file) (see [Using the Address Book](../../tutorials/address-book)).

## Alias Does Not Expand

1. Confirm the alias file is sourced in your `neomuttrc`:

```neomuttrc
source ~/.config/neomutt/aliases
```

2. Confirm the file path matches [`$alias_file`](cfg-alias-file):

```
:set alias_file?
```

3. Reload the file:

```
:source ~/.config/neomutt/aliases
```

Expected result: after reloading, the alias expands at address prompts.

## Check for Syntax Errors

1. Look for common problems in the alias file:

- Missing angle brackets around the email address.
- Commas missing between multiple addresses in a group alias.
- Unmatched quotes in comments.

Correct format:

```neomuttrc
alias alice Alice Example <alice@example.com>
alias team  alice, bob
```

2. Start NeoMutt and watch for error messages on the command line at the bottom of the screen.

Expected result: NeoMutt reports the file and line number of any syntax error.

## Alias Saved but Not Available

When [`<create-alias>`](fn-create-alias) appends to [`$alias_file`](cfg-alias-file), NeoMutt does not re-source the file automatically.

1. Reload after saving:

```
:source ~/.config/neomutt/aliases
```

Or use a macro that saves and reloads in one step (see [Speed Up Address Book Access](alias-keybindings)).

Expected result: the newly saved alias is immediately usable.

## Alias Points to an Old Address

1. Open the alias file and update the entry.
2. Save and reload with `:source`.

Expected result: the alias expands to the corrected address.

## Duplicate Alias Names

Alias names are matched case-insensitively.
If two entries share the same name, the last one defined wins.

1. Search the alias file for duplicates:

```sh
grep -i "^alias alice" ~/.config/neomutt/aliases
```

2. Remove or rename the duplicate.

Expected result: only one alias with that name remains.

See [Manage Aliases](aliases) for the full alias syntax.
