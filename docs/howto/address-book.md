---
title: Set Up Address Book Integration
description: XXX
keywords: XXX
---

# Set Up Address Book Integration

## Prerequisites

1. Confirm NeoMutt is working and you can open a mailbox.
2. Decide which address source you want to use: aliases, abook, khard, LDAP, or a custom query script.

## Using NeoMutt's Built-In Alias System

1. Add aliases to a config file that is sourced:

```neomuttrc
alias alan   Alan Jones <alan@example.com>      # tags:friends
alias briony Briony Williams <bw@example.com>   # tags:friends
```

2. (Optional) Store aliases in a separate file and source it:

```neomuttrc
source ~/.mail_aliases
set alias_file=~/.mail_aliases
```

3. At an address prompt, press Tab to expand an alias or list matches.

Expected result: aliases expand at `To:` and `Cc:` prompts, and the alias menu appears if there are multiple matches.

## Integrating with abook

1. Install and configure abook (see its documentation).
2. Configure NeoMutt to query abook:

```neomuttrc
set query_command = "abook --mutt-query %s"
```

3. In the index menu, press `Q` to query addresses.

Expected result: the query menu lists contacts returned by abook.

References: abook man page and project docs.

## Integrating with khard (CardDAV)

1. Install and configure khard and its address book backend (see khard docs).
2. Configure NeoMutt to query khard:

```neomuttrc
set query_command = "khard email --parsable %s"
```

3. Press `Q` in the index menu or `^T` at an address prompt to query.

Expected result: the query menu lists khard results and address completion works.

References: khard scripting docs.

## Using `query_command` for External Lookups

1. Create or install a query wrapper script.
2. Point NeoMutt at it:

```neomuttrc
set query_command = "mutt_ldap_query.pl %s"
```

3. Use `Q` in the index menu to run a query.

Expected result: a query menu with matching results and selectable addresses.

See [How to Use External Address Queries](address-query).

## Using LDAP for Address Lookups

1. Install or configure an LDAP query wrapper script (for example `mutt_ldap_query.pl`).
2. Set `query_command` to that script.
3. Use `Q` to search and select results.

Expected result: LDAP results appear in the query menu and can be inserted into address fields.

## Auto-Saving Addresses from Received Mail

1. Decide where you want to store new contacts.
2. Add a macro to pipe a message to your address tool:

```neomuttrc
macro index,pager A "<pipe-message>abook --add-email-quiet<Enter>" "Save sender to abook"
```

3. Open a message and press `A`.

Expected result: the sender is added to your address book.

Adjust the command to match your tool (abook, khard, or a custom script).

## Configuring Tab Completion for Addresses

1. Use aliases or an external query source.
2. At any address prompt, press Tab to expand or list matches.
3. Use `^T` to query external address sources if configured.

Expected result: you can complete addresses quickly without leaving the prompt.
