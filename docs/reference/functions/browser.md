---
title: Browser Menu
description: Default Keys bindings and functions for the NeoMutt Browser Menu.
keywords: neomutt, functions, browser, menu, bindings, keys, files
---

(menu-browser)=
# Browser Menu

Browse files on disk or mailboxes on a server.
You can navigate directories, sort listings, subscribe to mailboxes, and select a mailbox to open.

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

| Function                | Default Keys | Description                                                |
|-------------------------|--------------|------------------------------------------------------------|
| `<catchup>`             |              | mark all articles in newsgroup as read                     |
| `<change-dir>`          | `c`          | change directories                                         |
| `<check-new>`           |              | check mailboxes for new mail                               |
| `<create-mailbox>`      | `C`          | create a new mailbox (IMAP only)                           |
| `<delete-mailbox>`      | `d`          | delete the current mailbox (IMAP only)                     |
| `<descend-directory>`   |              | descend into a directory                                   |
| `<display-filename>`    | `@`          | display the currently selected file's name                 |
| `<enter-mask>`          | `m`          | enter a file mask                                          |
| `<exit>`                | `q`          | exit this menu                                             |
| `<goto-folder>`         | `=`          | swap the current folder position with $folder if it exists |
| `<goto-parent>`         | `p`          | go to parent directory                                     |
| `<mailbox-list>`        | `.`          | list mailboxes with new mail                               |
| `<reload-active>`       |              | load list of all newsgroups from NNTP server               |
| `<rename-mailbox>`      | `r`          | rename the current mailbox (IMAP only)                     |
| `<select-new>`          | `N`          | select a new file in this directory                        |
| `<sort>`                | `o`          | sort messages                                              |
| `<sort-reverse>`        | `O`          | sort messages in reverse order                             |
| `<subscribe>`           | `s`          | subscribe to current mbox (IMAP/NNTP only)                 |
| `<subscribe-pattern>`   |              | subscribe to newsgroups matching a pattern                 |
| `<toggle-mailboxes>`    | `<Tab>`      | toggle whether to browse mailboxes or all files            |
| `<toggle-subscribed>`   | `T`          | toggle view all/subscribed mailboxes (IMAP only)           |
| `<uncatchup>`           |              | mark all articles in newsgroup as unread                   |
| `<unsubscribe>`         | `u`          | unsubscribe from current mbox (IMAP/NNTP only)             |
| `<unsubscribe-pattern>` |              | unsubscribe from newsgroups matching a pattern             |
| `<view-file>`           | `<Space>`    | view file                                                  |

