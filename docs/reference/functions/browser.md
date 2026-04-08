---
title: Browser Functions
description: Key bindings and functions for browsing files, directories, and IMAP/NNTP mailboxes in NeoMutt
keywords: neomutt, functions, browser, menu, bindings, keys, files, directories, imap, nntp, mailbox, subscribe, change-dir, create-mailbox, toggle-mailboxes, file browser
---

(menu-browser)=
# Browser Functions

Browse files on disk or mailboxes on a server.
You can navigate directories, sort listings, subscribe to mailboxes, and select a mailbox to open.

| Function                | Default Keys   | Description                                                |
|-------------------------|----------------|------------------------------------------------------------|
| `<catchup>`             |                | Mark all articles in newsgroup as read                     |
| `<change-dir>`          | {kbd}`c`       | Change directories                                         |
| `<check-new>`           |                | Check mailboxes for new mail                               |
| `<create-mailbox>`      | {kbd}`C`       | Create a new mailbox (IMAP only)                           |
| `<delete-mailbox>`      | {kbd}`d`       | Delete the current mailbox (IMAP only)                     |
| `<descend-directory>`   |                | Descend into a directory                                   |
| `<display-filename>`    | {kbd}`@`       | Display the currently selected file's name                 |
| `<enter-mask>`          | {kbd}`m`       | Enter a file mask                                          |
| `<exit>`                | {kbd}`q`       | Exit this menu                                             |
| `<goto-folder>`         | {kbd}`=`       | Swap the current folder position with $folder if it exists |
| `<goto-parent>`         | {kbd}`p`       | Go to parent directory                                     |
| `<mailbox-list>`        | {kbd}`.`       | List mailboxes with new mail                               |
| `<reload-active>`       |                | Load list of all newsgroups from NNTP server               |
| `<rename-mailbox>`      | {kbd}`r`       | Rename the current mailbox (IMAP only)                     |
| `<select-new>`          | {kbd}`N`       | Select a new file in this directory                        |
| `<sort>`                | {kbd}`o`       | Sort messages                                              |
| `<sort-reverse>`        | {kbd}`O`       | Sort messages in reverse order                             |
| `<subscribe>`           | {kbd}`s`       | Subscribe to current mbox (IMAP/NNTP only)                 |
| `<subscribe-pattern>`   |                | Subscribe to newsgroups matching a pattern                 |
| `<toggle-mailboxes>`    | {kbd}`<Tab>`   | Toggle whether to browse mailboxes or all files            |
| `<toggle-subscribed>`   | {kbd}`T`       | Toggle view all/subscribed mailboxes (IMAP only)           |
| `<uncatchup>`           |                | Mark all articles in newsgroup as unread                   |
| `<unsubscribe>`         | {kbd}`u`       | Unsubscribe from current mbox (IMAP/NNTP only)             |
| `<unsubscribe-pattern>` |                | Unsubscribe from newsgroups matching a pattern             |
| `<view-file>`           | {kbd}`<Space>` | View file                                                  |

