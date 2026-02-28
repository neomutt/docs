---
title: How to Use Quasi-Delete
description: Mark emails that should be hidden from the index but not deleted using the quasi-delete feature
keywords: quasi-delete, hide, notmuch, index, sync-mailbox
---

# How to Use Quasi-Delete

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

*Mark emails that should be hidden, but not deleted*

## Introduction

The "quasi-delete" function marks an email that should be hidden from the index, but NOT
deleted. The email will disappear from the index when {ref}`<sync-mailbox> <index-map>` is
called.

On its own, this feature isn't very useful. It forms a useful part of the notmuch plugin.

## Functions

| Menus | Default Key | Function | Description |
|-------|-------------|----------|-------------|
| index,pager | (none) | `<quasi-delete>` | delete from NeoMutt, don't touch on disk |

## neomuttrc

```
# Example NeoMutt config file for the quasi-delete feature.

# The 'quasi-delete' function marks an email that should be hidden
# from the index, but NOT deleted.
bind index,pager Q quasi-delete

# vim: syntax=neomuttrc
```

## See Also

- {ref}`notmuch feature <notmuch>`

## Known Bugs

None

## Credits

Karel Zak, Richard Russon
