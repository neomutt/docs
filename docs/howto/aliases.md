---
title: How to Manage Aliases
description: Create and use email address aliases in NeoMutt
keywords: alias, unalias, address book, contacts, alias_file
---

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

# How to Manage Aliases

## Syntax

```neomuttrc
alias [-group name ...] key address [, address ...] [# [comments] [tags:...]]
unalias {* | key ...}
```

## Defining Aliases

It's usually very cumbersome to remember or type out the address of someone you are communicating with. NeoMutt allows you to create "aliases" which map a short string to a full address.

:::{note}
If you want to create an alias for more than one address, you **must** separate the addresses with a comma (`,`).
:::

The optional `-group` argument to `alias` causes the aliased address(es) to be added to the named *group*.

To add aliases:

```neomuttrc
# Some aliases, with comments and tags
alias alan   Alan Jones <alan@example.com>      # Al tags:friends
alias briony Briony Williams <bw@example.com>   # tags:friends
alias jim    James Smith <js@example.com>       # Pointy-haired boss

# An alias that references two other aliases
alias friends alan, briony
```

Aliases can be given tags (labels) which can be used for searching or limiting. Tags consist of comma-separated strings after a comment of `tags:`. In the Address Book, you can search for a tag with `~Y friends` or limit the view to friends.

## Removing Aliases

To remove an alias or aliases (`*` means all aliases):

```neomuttrc
unalias muttdude
unalias *
```

:::{note}
The alias *key* is matched case insensitively when creating (checking for duplicates), removing, or expanding aliases.
:::

## Alias File Configuration

Unlike other mailers, NeoMutt doesn't require aliases to be defined in a special file. The `alias` command can appear anywhere in a configuration file, as long as this file is `source`d. Consequently, you can have multiple alias files, or you can have all aliases defined in your `.neomuttrc`.

On the other hand, the `<create-alias>` function can use only one file, the one pointed to by the `$alias_file` variable (which is `~/.neomuttrc` by default). This file is not special either, in the sense that NeoMutt will happily append aliases to any file, but in order for the new aliases to take effect you need to explicitly `source` this file too.

### Configuring external alias files

```neomuttrc
source /usr/local/share/NeoMutt.aliases
source ~/.mail_aliases
set alias_file=~/.mail_aliases
```

## Using Aliases

To use aliases, you merely use the alias at any place in NeoMutt where NeoMutt prompts for addresses, such as the *To:* or *Cc:* prompt. You can also enter aliases in your editor at the appropriate headers if you have the `$edit_headers` variable set.

In addition, at the various address prompts, you can use the tab character to expand a partial alias to the full alias. If there are multiple matches, NeoMutt will bring up a menu with the matching aliases. In order to be presented with the full list of aliases, you must hit tab without a partial alias, such as at the beginning of the prompt or after a comma denoting multiple addresses.

In the alias menu, you can select as many aliases as you want with the `tag-entry` key (default: &lt;Space&gt; or t), and use the *exit* key (default: q) to return to the address prompt.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Alias selection menu

**Description:** The NeoMutt alias menu displayed after pressing Tab at an address prompt, showing a list of defined aliases with their short names, full email addresses, and comment fields. Several aliases should be tagged (marked with `*`) to illustrate multi-selection.

**Highlights:** How aliases are listed for selection, the tag marker (`*`) on selected entries, and the alias key / address / comment columns.
:::
