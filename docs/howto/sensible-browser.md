---
title: How to Use the Sensible Browser
description: Configure NeoMutt's mailbox browser to behave predictably with fixed or variable sort orders.
keywords: sensible browser, browser_sort, mailbox browser, file browser
---

# How to Use the Sensible Browser

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

The "sensible browser" is a set of small changes to NeoMutt's mailbox browser which make the browser behave in a more predictable way.

The behavior is divided into two use cases: Fixed Order; Variable Order.

### A Fixed Order of Mailboxes

This is for users who like their mailboxes in a fixed order, e.g. alphabetical, or unsorted (in the order of the config file).

```bash
# Fixed order
set browser_sort = "alpha"
set browser_sort = "unsorted"
```

When you first start the browser, e.g. `c?` your current mailbox will be highlighted.

When you navigate to a parent mailbox ("..") your old mailbox will be highlighted.

".." will always be listed at the top, however the rest of the list is sorted.

### A Variable Order of Mailboxes

This is for users who like their mailboxes sorted by a characteristic that changes, e.g. count of new mail, or the size of mailbox.

```bash
# Variable order
set browser_sort = "reverse-count"
set browser_sort = "reverse-size"
```

When you first start the browser, e.g. `c?` the highlight will be on the first mailbox, e.g. the one with the most new mail.

When you navigate to a parent mailbox ("..") your old mailbox will be highlighted.

".." will always be listed at the top, however the rest of the list is sorted.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Mailbox browser with fixed vs variable sort

**Description:** Two NeoMutt file browser views: (1) with `browser_sort=alpha` showing mailboxes in alphabetical order with the current mailbox highlighted, and (2) with `browser_sort=reverse-count` showing mailboxes sorted by message count (highest first) with the highlight on the top entry. Both views show ".." at the top.

**Highlights:** The difference in highlight position — in fixed-order mode the current mailbox is highlighted wherever it falls alphabetically, while in variable-order mode the highlight starts at the top (the mailbox with the most mail). The ".." entry always stays at the top regardless of sort.
:::

## See Also

- `$folder_format`

## Known Bugs

None

## Credits

Pierre-Elliott Bécue, Haakon Riiser, Richard Russon
