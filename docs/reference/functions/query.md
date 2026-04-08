---
title: Query Functions
description: Key bindings and functions for searching an external address book and selecting contacts in NeoMutt
keywords: neomutt, functions, query, menu, bindings, keys, address book, external query, contacts, create-alias, query-append, search results, address lookup
---

(menu-query)=
# Query Functions

Display results from an external address-book query.
You can search for contacts, create aliases from the results, and compose messages to selected addresses.

| Function          | Default Keys   | Description                                  | Inherited From                      |
|-------------------|----------------|----------------------------------------------|-------------------------------------|
| `<create-alias>`  | {kbd}`a`       | Create an alias from a message sender        |                                     |
| `<exit>`          | {kbd}`q`       | Exit this menu                               |                                     |
| `<limit>`         | {kbd}`l`       | Show only messages matching a pattern        |                                     |
| `<mail>`          | {kbd}`m`       | Compose a new mail message                   |                                     |
| `<query-append>`  | {kbd}`A`       | Append new query results to current results  |                                     |
| `<query>`         | {kbd}`Q`       | Query external program for addresses         |                                     |
| `<sort>`          | {kbd}`o`       | Sort messages                                |                                     |
| `<sort-reverse>`  | {kbd}`O`       | Sort messages in reverse order               |                                     |
| `<tag-entry>`     | {kbd}`<Space>` | Tag the current entry                        | [{bdg-info}`generic`](menu-generic) |
| `<tag-pattern>`   | {kbd}`T`       | Tag non-hidden messages matching a pattern   |                                     |
| `<untag-pattern>` | {kbd}`Ctrl-T`  | Untag non-hidden messages matching a pattern |                                     |

