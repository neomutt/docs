---
title: Browser Menu
description: Key bindings and functions for browsing files, directories, and IMAP/NNTP mailboxes in NeoMutt
keywords: neomutt, functions, browser, menu, bindings, keys, files, directories, imap, nntp, mailbox, subscribe, change-dir, create-mailbox, toggle-mailboxes, file browser
---

(menu-browser)=
# Browser Menu

Browse files on disk or mailboxes on a server.
You can navigate directories, sort listings, subscribe to mailboxes, and select a mailbox to open.

| Function                | Default Keys | Description                                                |
|-------------------------|--------------|------------------------------------------------------------|
| `<catchup>`             |              | Mark all articles in newsgroup as read                     |
| `<change-dir>`          | `c`          | Change directories                                         |
| `<check-new>`           |              | Check mailboxes for new mail                               |
| `<create-mailbox>`      | `C`          | Create a new mailbox (IMAP only)                           |
| `<delete-mailbox>`      | `d`          | Delete the current mailbox (IMAP only)                     |
| `<descend-directory>`   |              | Descend into a directory                                   |
| `<display-filename>`    | `@`          | Display the currently selected file's name                 |
| `<enter-mask>`          | `m`          | Enter a file mask                                          |
| `<exit>`                | `q`          | Exit this menu                                             |
| `<goto-folder>`         | `=`          | Swap the current folder position with $folder if it exists |
| `<goto-parent>`         | `p`          | Go to parent directory                                     |
| `<mailbox-list>`        | `.`          | List mailboxes with new mail                               |
| `<reload-active>`       |              | Load list of all newsgroups from NNTP server               |
| `<rename-mailbox>`      | `r`          | Rename the current mailbox (IMAP only)                     |
| `<select-new>`          | `N`          | Select a new file in this directory                        |
| `<sort>`                | `o`          | Sort messages                                              |
| `<sort-reverse>`        | `O`          | Sort messages in reverse order                             |
| `<subscribe>`           | `s`          | Subscribe to current mbox (IMAP/NNTP only)                 |
| `<subscribe-pattern>`   |              | Subscribe to newsgroups matching a pattern                 |
| `<toggle-mailboxes>`    | `<Tab>`      | Toggle whether to browse mailboxes or all files            |
| `<toggle-subscribed>`   | `T`          | Toggle view all/subscribed mailboxes (IMAP only)           |
| `<uncatchup>`           |              | Mark all articles in newsgroup as unread                   |
| `<unsubscribe>`         | `u`          | Unsubscribe from current mbox (IMAP/NNTP only)             |
| `<unsubscribe-pattern>` |              | Unsubscribe from newsgroups matching a pattern             |
| `<view-file>`           | `<Space>`    | View file                                                  |

