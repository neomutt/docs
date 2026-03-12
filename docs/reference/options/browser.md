---
title: Browser Options
description: NeoMutt configuration variables for the file browser display and sorting.
keywords: neomutt, browser, browser_abbreviate_mailboxes, browser_sort, browser_sort_dirs_first, configuration
---

# Browser Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

(browser-abbreviate-mailboxes)=
## `$browser_abbreviate_mailboxes`

- **Type:** boolean
- **Default:** `yes`

When this variable is *set*, NeoMutt will abbreviate mailbox names in the browser mailbox list, using '~' and '=' shortcuts.

The default `"alpha"` setting of [`$browser_sort`](#browser-sort) uses locale-based sorting (using `strcoll(3)`), which ignores some punctuation. This can lead to some situations where the order doesn't make intuitive sense. In those cases, it may be desirable to *unset* this variable.

(browser-sort)=
## `$browser_sort`

- **Type:** sort order
- **Default:** `alpha`

Specifies how to sort entries in the file browser.

| Value      | Sort by               |
|------------|-----------------------|
| `alpha`    | Name                  |
| `count`    | Total message count   |
| `date`     | Date                  |
| `desc`     | Description           |
| `size`     | Count of new messages |
| `new`      | Size                  |
| `unsorted` | Unsorted              |

| Deprecated Value | Use this instead |
|------------------|------------------|
| `unread`         | `new`            |

Prefixing the value with `reverse-` sorts the entries in reverse order, e.g. `set browser_sort = "reverse-date"`

(browser-sort-dirs-first)=
## `$browser_sort_dirs_first`

- **Type:** boolean
- **Default:** `no`

If this variable is *set*, the browser will group directories before files.
