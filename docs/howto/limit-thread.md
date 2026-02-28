---
title: How to Limit to Current Thread
description: Use the limit-current-thread function to focus on a single email thread in NeoMutt
keywords: limit, thread, limit-current-thread, focus, filter, index
---

# How to Limit to Current Thread

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

## Introduction

This feature adds a new way of using the {ref}`Limit Command <tuning-search>`. The `<limit-current-thread>` function restricts the view to just the current thread. Setting the limit (the `l` key) to "all" will restore the full email list.

## Functions

Limit-current-thread adds the following function to NeoMutt. By default, it is not bound to a key.

| Menus | Function | Description |
|-------|----------|-------------|
| index | `<limit-current-thread>` | Limit view to current thread |

## neomuttrc

```
# Example NeoMutt config file for the limit-current-thread feature.

# Limit view to current thread
bind index <esc>L limit-current-thread

# vim: syntax=neomuttrc
```

## Known Bugs

None

## Credits

David Sterba, Richard Russon
