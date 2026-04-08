---
title: Customise Alias Display
description: Adjust alias_format to control which columns and layout the alias menu shows in NeoMutt
keywords: alias, alias_format, alias_sort, display, layout, columns, format string, address book, alias menu
---

# Customise Alias Display

## Prerequisites

1. One or more aliases defined and loaded (see [Using the Address Book](../tutorials/address-book)).

## Change the Alias Menu Layout

1. Set [`$alias_format`](cfg-alias-format) in your `neomuttrc`:

```neomuttrc
set alias_format = "%3i %f%t %-15a %-56A | %C%> %Y"
```

2. Open the alias menu to see the effect.

Expected result: aliases are displayed with the number, flags, alias name, full address, comment, and tags.

## Available Format Sequences

| Sequence | Description                            |
|----------|----------------------------------------|
| `%i`     | Index number                           |
| `%a`     | Alias short name                       |
| `%A`     | Full address (name and email)          |
| `%E`     | Email address only                     |
| `%N`     | Real name only                         |
| `%C`     | Comment text                           |
| `%Y`     | User-defined tags                      |
| `%f`     | Flags (`d` if marked for deletion)     |
| `%t`     | Tagged indicator                       |

See [Alias Options](../reference/config/alias) for the complete list and long-name alternatives.

## Show Only Name and Email

```neomuttrc
set alias_format = "%3i %-20N %E"
```

Expected result: a compact view with just the real name and email address.

## Change the Sort Order

1. Set [`$alias_sort`](cfg-alias-sort):

```neomuttrc
set alias_sort = "name"
```

| Value      | Sorts by              |
|------------|-----------------------|
| `alias`    | Alias short name      |
| `email`    | Email address         |
| `name`     | Real name             |
| `unsorted` | Order in config file  |

Prefix with `reverse-` to invert the order.

Expected result: the alias menu is sorted by real name.

See [Alias Options](../reference/config/alias) for full reference and [Format Strings](format-strings) for general formatting guidance.
