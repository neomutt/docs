---
title: Jump Quickly to a Virtual Mailbox
description: Bind keys and macros to switch between Notmuch virtual mailboxes instantly in NeoMutt
keywords: notmuch, virtual mailbox, jump, navigate, macro, change-vfolder, change-folder, key binding, sidebar, vfolder
---

# Jump Quickly to a Virtual Mailbox

## Prerequisites

1. Notmuch virtual mailboxes configured in NeoMutt (see [Getting Started with Notmuch Virtual Mailboxes](../tutorials/notmuch-virtual-mailboxes)).

## Jump with a Macro

1. Create macros that jump directly to specific virtual mailboxes:

```neomuttrc
macro index gi "<change-folder>notmuch://?query=tag:inbox<Enter>"            "Jump to Inbox"
macro index gu "<change-folder>notmuch://?query=tag:inbox and tag:unread<Enter>" "Jump to Unread"
macro index gf "<change-folder>notmuch://?query=tag:flagged<Enter>"          "Jump to Flagged"
```

2. Press {kbd}`gi`, {kbd}`gu`, or {kbd}`gf` in the index.

Expected result: NeoMutt opens the matching virtual mailbox immediately.

## Use change-vfolder to Cycle

1. Bind the `<change-vfolder>` function:

```neomuttrc
bind index,pager X change-vfolder
```

2. Press {kbd}`X` and type the label of a virtual mailbox (e.g. `Inbox`), or press {kbd}`Enter` to jump to the next virtual folder with unread messages.

Expected result: NeoMutt switches to the named virtual mailbox.

## Run an Ad-Hoc Query

1. Bind `<vfolder-from-query>`:

```neomuttrc
bind index,pager \eX vfolder-from-query
```

2. Press {kbd}`Esc X`, type a Notmuch query, and press {kbd}`Enter`.

Expected result: NeoMutt opens a temporary virtual mailbox for that query.

## Navigate with the Sidebar

If the sidebar is enabled, virtual mailboxes appear alongside regular mailboxes.

1. Use sidebar navigation keys to move between them:

```neomuttrc
bind index,pager \CP sidebar-prev
bind index,pager \CN sidebar-next
bind index,pager \CO sidebar-open
```

2. Press {kbd}`Ctrl-N` / {kbd}`Ctrl-P` to highlight, then {kbd}`Ctrl-O` to open.

Expected result: you can switch between virtual mailboxes without typing queries.

See [Sidebar Workflows](sidebar-workflows) for more navigation tips.
