---
title: Index Menu
description: Default Keys bindings and functions for the NeoMutt Index Menu.
keywords: neomutt, functions, index, menu, bindings, keys, mail
---

(menu-index)=
# Index Menu

The main screen showing the list of emails in a mailbox.
You can read, reply, forward, delete, tag, sort, search, and manage messages.

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

| Function                        | Default Keys                                      | Description                                                             | Inherited From                      |
|---------------------------------|---------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------|
| `<alias-dialog>`                |                                                   | Open the aliases dialog                                                 |                                     |
| `<autocrypt-acct-menu>`         | `A`                                               | Manage autocrypt accounts                                               |                                     |
| `<bounce-message>`              | `b`                                               | Remail a message to another user                                        |                                     |
| `<break-thread>`                | `#`                                               | Break the thread in two                                                 |                                     |
| `<catchup>`                     |                                                   | Mark all articles in newsgroup as read                                  |                                     |
| `<change-folder-readonly>`      | `Esc c`                                           | Open a different folder in read only mode                               |                                     |
| `<change-folder>`               | `c`                                               | Open a different folder                                                 |                                     |
| `<change-newsgroup-readonly>`   | `Esc i`                                           | Open a different newsgroup in read only mode                            |                                     |
| `<change-newsgroup>`            | `i`                                               | Open a different newsgroup                                              |                                     |
| `<change-vfolder>`              |                                                   | Open a different virtual folder                                         |                                     |
| `<check-traditional-pgp>`       | `Esc P`                                           | Check for classic PGP                                                   |                                     |
| `<clear-flag>`                  | `W`                                               | Clear a status flag from a message                                      |                                     |
| `<close-all-threads>`           |                                                   | Collapse all threads                                                    |                                     |
| `<close-thread>`                |                                                   | Collapse current thread                                                 |                                     |
| `<collapse-all>`                | `Esc V`                                           | Collapse/Uncollapse all threads                                         |                                     |
| `<collapse-thread>`             | `Esc v`                                           | Collapse/Uncollapse current thread                                      |                                     |
| `<compose-to-sender>`           |                                                   | Compose new message to the current message sender                       |                                     |
| `<copy-message>`                | `C`                                               | Copy a message to a file/mailbox                                        |                                     |
| `<create-alias>`                | `a`                                               | Create an alias from a message sender                                   |                                     |
| `<decode-copy>`                 | `Esc C`                                           | Make decoded (text/plain) copy                                          |                                     |
| `<decode-save>`                 | `Esc s`                                           | Make decoded copy (text/plain) and delete                               |                                     |
| `<decrypt-copy>`                |                                                   | Make decrypted copy                                                     |                                     |
| `<decrypt-save>`                |                                                   | Make decrypted copy and delete                                          |                                     |
| `<delete-message>`              | `d`                                               | Delete the current entry                                                |                                     |
| `<delete-pattern>`              | `D`                                               | Delete non-hidden messages matching a pattern                           |                                     |
| `<delete-subthread>`            | `Esc d`                                           | Delete all messages in subthread                                        |                                     |
| `<delete-thread>`               | `^D`                                              | Delete all messages in thread                                           |                                     |
| `<display-address>`             | `@`                                               | Display full address of sender                                          |                                     |
| `<display-message>`             | `<Enter>`, `<KeypadEnter>`, `<Return>`, `<Space>` | Display a message                                                       |                                     |
| `<display-toggle-weed>`         | `h`                                               | Display message and toggle header weeding                               |                                     |
| `<edit-label>`                  | `Y`                                               | Add, change, or delete a message's label                                |                                     |
| `<edit-or-view-raw-message>`    | `e`                                               | Edit the raw message if the mailbox is not read-only, otherwise view it |                                     |
| `<edit-raw-message>`            |                                                   | Edit the raw message (edit and edit-raw-message are synonyms)           |                                     |
| `<edit-type>`                   | `^E`                                              | Edit attachment content type                                            |                                     |
| `<edit>`                        |                                                   | Edit the raw message (edit and edit-raw-message are synonyms)           |                                     |
| `<entire-thread>`               |                                                   | Read entire thread of the current message                               |                                     |
| `<exit>`                        | `x`                                               | Exit this menu                                                          |                                     |
| `<extract-keys>`                | `^K`                                              | Extract supported public keys                                           |                                     |
| `<fetch-mail>`                  | `G`                                               | Retrieve mail from POP server                                           |                                     |
| `<flag-message>`                | `F`                                               | Toggle a message's 'important' flag                                     |                                     |
| `<followup-message>`            |                                                   | Followup to newsgroup                                                   |                                     |
| `<forget-passphrase>`           | `^F`                                              | Wipe passphrases from memory                                            |                                     |
| `<forward-message>`             | `f`                                               | Forward a message with comments                                         |                                     |
| `<forward-to-group>`            |                                                   | Forward to newsgroup                                                    |                                     |
| `<get-children>`                |                                                   | Get all children of the current message                                 |                                     |
| `<get-message>`                 |                                                   | Get message with Message-Id                                             |                                     |
| `<get-parent>`                  |                                                   | Get parent of the current message                                       |                                     |
| `<group-chat-reply>`            |                                                   | Reply to all recipients preserving To/Cc                                |                                     |
| `<group-reply>`                 | `g`                                               | Reply to all recipients                                                 |                                     |
| `<imap-fetch-mail>`             |                                                   | Force retrieval of mail from IMAP server                                |                                     |
| `<imap-logout-all>`             |                                                   | Logout from all IMAP servers                                            |                                     |
| `<limit-current-thread>`        |                                                   | Limit view to current thread                                            |                                     |
| `<limit>`                       | `l`                                               | Show only messages matching a pattern                                   |                                     |
| `<link-threads>`                | `&`                                               | Link tagged message to the current one                                  |                                     |
| `<list-reply>`                  | `L`                                               | Reply to specified mailing list                                         |                                     |
| `<list-subscribe>`              |                                                   | Subscribe to a mailing list                                             |                                     |
| `<list-unsubscribe>`            |                                                   | Unsubscribe from a mailing list                                         |                                     |
| `<mail-key>`                    | `Esc k`                                           | Mail a PGP public key                                                   |                                     |
| `<mail>`                        | `m`                                               | Compose a new mail message                                              |                                     |
| `<mailbox-list>`                | `.`                                               | List mailboxes with new mail                                            |                                     |
| `<mark-message>`                | `~`                                               | Create a hotkey macro for the current message                           |                                     |
| `<modify-labels-then-hide>`     |                                                   | Modify (notmuch/imap) tags and then hide message                        |                                     |
| `<modify-labels>`               |                                                   | Modify (notmuch/imap) tags                                              |                                     |
| `<modify-tags-then-hide>`       |                                                   | Modify (notmuch/imap) tags and then hide message                        |                                     |
| `<modify-tags>`                 |                                                   | Modify (notmuch/imap) tags                                              |                                     |
| `<next-entry>`                  | `J`                                               | Move to the next entry                                                  | [{bdg-info}`generic`](menu-generic) |
| `<next-new-then-unread>`        | `<Tab>`                                           | Jump to the next new or unread message                                  |                                     |
| `<next-new>`                    |                                                   | Jump to the next new message                                            |                                     |
| `<next-subthread>`              | `Esc n`                                           | Jump to the next subthread                                              |                                     |
| `<next-thread>`                 | `^N`                                              | Jump to the next thread                                                 |                                     |
| `<next-undeleted>`              | `<Down>`, `j`                                     | Move to the next undeleted message                                      |                                     |
| `<next-unread-mailbox>`         |                                                   | Open next mailbox with new mail                                         |                                     |
| `<next-unread>`                 |                                                   | Jump to the next unread message                                         |                                     |
| `<open-all-threads>`            |                                                   | Uncollapse all threads                                                  |                                     |
| `<open-thread>`                 |                                                   | Uncollapse current thread                                               |                                     |
| `<parent-message>`              | `P`                                               | Jump to parent message in thread                                        |                                     |
| `<pipe-entry>`                  |                                                   | Pipe message/attachment to a shell command                              |                                     |
| `<pipe-message>`                | `\|`                                              | Pipe message/attachment to a shell command                              |                                     |
| `<post-message>`                |                                                   | Post message to newsgroup                                               |                                     |
| `<previous-entry>`              | `K`                                               | Move to the previous entry                                              | [{bdg-info}`generic`](menu-generic) |
| `<previous-new-then-unread>`    | `Esc <Tab>`                                       | Jump to the previous new or unread message                              |                                     |
| `<previous-new>`                |                                                   | Jump to the previous new message                                        |                                     |
| `<previous-subthread>`          | `Esc p`                                           | Jump to previous subthread                                              |                                     |
| `<previous-thread>`             | `^P`                                              | Jump to previous thread                                                 |                                     |
| `<previous-undeleted>`          | `<Up>`, `k`                                       | Move to the previous undeleted message                                  |                                     |
| `<previous-unread>`             |                                                   | Jump to the previous unread message                                     |                                     |
| `<print-message>`               | `p`                                               | Print the current entry                                                 |                                     |
| `<purge-message>`               |                                                   | Delete the current entry, bypassing the trash folder                    |                                     |
| `<purge-thread>`                |                                                   | Delete the current thread, bypassing the trash folder                   |                                     |
| `<quasi-delete>`                |                                                   | Delete from NeoMutt, don't touch on disk                                |                                     |
| `<query>`                       | `Q`                                               | Query external program for addresses                                    |                                     |
| `<quit>`                        | `q`                                               | Save changes to mailbox and quit                                        |                                     |
| `<read-subthread>`              | `Esc r`                                           | Mark the current subthread as read                                      |                                     |
| `<read-thread>`                 | `^R`                                              | Mark the current thread as read                                         |                                     |
| `<recall-message>`              | `R`                                               | Recall a postponed message                                              |                                     |
| `<reconstruct-thread>`          |                                                   | Reconstruct thread containing current message                           |                                     |
| `<reply>`                       | `r`                                               | Reply to a message                                                      |                                     |
| `<resend-message>`              | `Esc e`                                           | Use the current message as a template for a new one                     |                                     |
| `<root-message>`                |                                                   | Jump to root message in thread                                          |                                     |
| `<save-message>`                | `s`                                               | Save message/attachment to a mailbox/file                               |                                     |
| `<set-flag>`                    | `w`                                               | Set a status flag on a message                                          |                                     |
| `<show-limit>`                  | `Esc l`                                           | Show currently active limit pattern                                     |                                     |
| `<show-log-messages>`           | `M`                                               | Show log (and debug) messages                                           | [{bdg-info}`generic`](menu-generic) |
| `<sort-mailbox>`                | `o`                                               | Sort messages                                                           |                                     |
| `<sort-reverse>`                | `O`                                               | Sort messages in reverse order                                          |                                     |
| `<sync-mailbox>`                | `$`                                               | Save changes to mailbox                                                 |                                     |
| `<tag-pattern>`                 | `T`                                               | Tag non-hidden messages matching a pattern                              |                                     |
| `<tag-subthread>`               |                                                   | Tag the current subthread                                               |                                     |
| `<tag-thread>`                  | `Esc t`                                           | Tag the current thread                                                  |                                     |
| `<toggle-new>`                  | `N`                                               | Toggle a message's 'new' flag                                           |                                     |
| `<toggle-read>`                 |                                                   | Toggle view of read messages                                            |                                     |
| `<toggle-write>`                | `%`                                               | Toggle whether the mailbox will be rewritten                            |                                     |
| `<undelete-message>`            | `u`                                               | Undelete the current entry                                              |                                     |
| `<undelete-pattern>`            | `U`                                               | Undelete non-hidden messages matching a pattern                         |                                     |
| `<undelete-subthread>`          | `Esc u`                                           | Undelete all messages in subthread                                      |                                     |
| `<undelete-thread>`             | `^U`                                              | Undelete all messages in thread                                         |                                     |
| `<untag-pattern>`               | `^T`                                              | Untag non-hidden messages matching a pattern                            |                                     |
| `<vfolder-from-query-readonly>` |                                                   | Generate a read-only virtual folder from query                          |                                     |
| `<vfolder-from-query>`          |                                                   | Generate virtual folder from query                                      |                                     |
| `<vfolder-window-backward>`     |                                                   | Shifts virtual folder time window backwards                             |                                     |
| `<vfolder-window-forward>`      |                                                   | Shifts virtual folder time window forwards                              |                                     |
| `<vfolder-window-reset>`        |                                                   | Resets virtual folder time window to the present                        |                                     |
| `<view-attachments>`            | `v`                                               | Show MIME attachments                                                   |                                     |
| `<view-raw-message>`            |                                                   | Show the raw message                                                    |                                     |

