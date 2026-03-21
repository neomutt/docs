---
title: Query Menu
description: Default Keys bindings and functions for the NeoMutt Query Menu.
keywords: neomutt, functions, query, menu, bindings, keys, search
---

(menu-query)=
# Query Menu

Display results from an external address-book query.
You can search for contacts, create aliases from the results, and compose messages to selected addresses.

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

| Function          | Default Keys | Description                                  | Inherited From                      |
|-------------------|--------------|----------------------------------------------|-------------------------------------|
| `<create-alias>`  | `a`          | Create an alias from a message sender        |                                     |
| `<exit>`          | `q`          | Exit this menu                               |                                     |
| `<limit>`         | `l`          | Show only messages matching a pattern        |                                     |
| `<mail>`          | `m`          | Compose a new mail message                   |                                     |
| `<query-append>`  | `A`          | Append new query results to current results  |                                     |
| `<query>`         | `Q`          | Query external program for addresses         |                                     |
| `<sort>`          | `o`          | Sort messages                                |                                     |
| `<sort-reverse>`  | `O`          | Sort messages in reverse order               |                                     |
| `<tag-entry>`     | `<Space>`    | Tag the current entry                        | [{bdg-info}`generic`](menu-generic) |
| `<tag-pattern>`   | `T`          | Tag non-hidden messages matching a pattern   |                                     |
| `<untag-pattern>` | `^T`         | Untag non-hidden messages matching a pattern |                                     |

