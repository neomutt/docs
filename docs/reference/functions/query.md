---
title: Query Functions
description: Key bindings and functions for searching an external address book and selecting contacts in NeoMutt
keywords: neomutt, functions, query, menu, bindings, keys, address book, external query, contacts, create-alias, query-append, search results, address lookup
---

(ref-fn-query)=
# Query Functions

Display results from an external address-book query.
You can search for contacts, create aliases from the results, and compose messages to selected addresses.

| Function          | Default Keys | Description                                  | Inherited From                        |
|-------------------|--------------|----------------------------------------------|---------------------------------------|
| `<create-alias>`  | `a`          | Create an alias from a message sender        |                                       |
| `<exit>`          | `q`          | Exit this menu                               |                                       |
| `<limit>`         | `l`          | Show only messages matching a pattern        |                                       |
| `<mail>`          | `m`          | Compose a new mail message                   |                                       |
| `<query-append>`  | `A`          | Append new query results to current results  |                                       |
| `<query>`         | `Q`          | Query external program for addresses         |                                       |
| `<sort>`          | `o`          | Sort messages                                |                                       |
| `<sort-reverse>`  | `O`          | Sort messages in reverse order               |                                       |
| `<tag-entry>`     | `<Space>`    | Tag the current entry                        | [{bdg-info}`generic`](ref-fn-generic) |
| `<tag-pattern>`   | `T`          | Tag non-hidden messages matching a pattern   |                                       |
| `<untag-pattern>` | `^T`         | Untag non-hidden messages matching a pattern |                                       |

