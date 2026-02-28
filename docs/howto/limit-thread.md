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

This feature adds a new way of using the **Limit Command**. The `<limit-current-thread>` function restricts the view to just the current thread. Setting the limit (the `l` key) to "all" will restore the full email list.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Limited view of a single thread

**Description:** The NeoMutt index after invoking `<limit-current-thread>`, showing only the messages belonging to one thread (with tree-style indentation) while all other messages are hidden. The status bar should indicate that a limit is active.

**Highlights:** How the index shows only the focused thread with its reply structure, the "limited" indicator in the status bar, and the reduced message count compared to the full mailbox.
:::

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
