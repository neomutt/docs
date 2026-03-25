---
title: How to Use Quasi-Delete
description: Mark emails that should be hidden from the index but not deleted using the quasi-delete feature
keywords: quasi-delete, hide, notmuch, index, sync-mailbox
---

# How to Use Quasi-Delete

*Mark emails that should be hidden, but not deleted*

## Introduction

The "quasi-delete" function marks an email that should be hidden from the index, but NOT deleted.
The email will disappear from the index when **\<sync-mailbox\>** is called.

On its own, this feature isn't very useful.
It forms a useful part of the notmuch plugin.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Quasi-deleted messages in the index

**Description:** The NeoMutt index showing one or more messages that have been quasi-deleted, displaying them with a distinct visual indicator (dimmed or with a special flag) compared to normal and fully deleted messages, before `<sync-mailbox>` hides them.

**Highlights:** How quasi-deleted messages look different from regular deleted messages (marked `D`), that they remain visible until sync, and the flag column indicator distinguishing their state.
:::

## Functions

| Menus       | Default Key | Function         | Description                              |
|-------------|-------------|------------------|------------------------------------------|
| index,pager | (none)      | `<quasi-delete>` | Delete from NeoMutt, don't touch on disk |

## neomuttrc

```neomuttrc
# Example NeoMutt config file for the quasi-delete feature.

# The 'quasi-delete' function marks an email that should be hidden
# from the index, but NOT deleted.
bind index,pager Q quasi-delete

# vim: filetype=neomuttrc
```

## See Also

- [notmuch feature](notmuch.md)

## Known Bugs

None

## Credits

Karel Zak, Richard Russon
