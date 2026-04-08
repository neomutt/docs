---
title: Find a Contact Quickly
description: Search and filter the alias menu by name, email, or tag to find contacts fast in NeoMutt
keywords: alias, search, find contact, alias menu, tab completion, filter, limit, tags, address book
---

# Find a Contact Quickly

## Prerequisites

1. One or more aliases defined and loaded (see [Using the Address Book](../tutorials/address-book)).

## Search the Alias Menu

1. Open the alias menu by pressing {kbd}`<Tab>` at an address prompt (with an empty field) or by using the `<alias>` function if bound.
2. Press {kbd}`/` to search.
3. Type part of a name or email address.

Expected result: the cursor jumps to the first matching alias.

4. Press {kbd}`n` to jump to the next match.

## Filter by Tag

If your aliases use tags (e.g. `# tags:work,friends`):

1. Open the alias menu.
2. Press {kbd}`l` to limit the view.
3. Enter a tag pattern:

```
~Y work
```

Expected result: only aliases tagged `work` are shown.

4. Press {kbd}`l` again and enter `~A` to clear the limit and show all aliases.

## Use Tab Completion at Address Prompts

1. At a `To:` or `Cc:` prompt, type the first few characters of an alias name.
2. Press {kbd}`<Tab>`.

If there is a single match, NeoMutt expands it in place.
If there are multiple matches, the alias menu opens showing only the matches.

Expected result: you reach the right contact without browsing the full list.

## Query an External Address Book

If you have `$query_command` configured (abook, khard, LDAP):

1. At an address prompt, press {kbd}`^T` (`<complete-query>`).
2. Type part of a name or address.

Expected result: results from the external source appear and you can select one.

See [External Address Queries](how-address-query) for setup details.

See [Manage Aliases](aliases) for the full alias syntax and [Alias Options](../reference/config/alias) for `$alias_format` and `$alias_sort`.
