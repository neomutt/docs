---
title: Pager Functions
description: Key bindings and functions for the NeoMutt pager — scrolling, searching, replying, and navigating within an email message
keywords: neomutt, functions, pager, menu, bindings, keys, reading email, message viewer, scroll, search, reply, forward, skip-quoted, toggle-quoted, next-page, previous-page
---

(ref-fn-pager)=
# Pager Functions

The email reading view that displays a message's contents.
You can scroll, search within the text, and perform many of the same actions as the index.

| Function                        | Default Keys                           | Description                                                             | Inherited From                        |
|---------------------------------|----------------------------------------|-------------------------------------------------------------------------|---------------------------------------|
| `<bottom>`                      | `<End>`                                | Jump to the bottom of the message                                       |                                       |
| `<bounce-message>`              | `b`                                    | Remail a message to another user                                        | [{bdg-success}`index`](ref-fn-index)  |
| `<break-thread>`                | `#`                                    | Break the thread in two                                                 | [{bdg-success}`index`](ref-fn-index)  |
| `<change-folder>`               | `c`                                    | Open a different folder                                                 | [{bdg-success}`index`](ref-fn-index)  |
| `<change-folder-readonly>`      | `Esc c`                                | Open a different folder in read only mode                               | [{bdg-success}`index`](ref-fn-index)  |
| `<change-newsgroup>`            |                                        | Open a different newsgroup                                              | [{bdg-success}`index`](ref-fn-index)  |
| `<change-newsgroup-readonly>`   |                                        | Open a different newsgroup in read only mode                            | [{bdg-success}`index`](ref-fn-index)  |
| `<change-vfolder>`              |                                        | Open a different virtual folder                                         | [{bdg-success}`index`](ref-fn-index)  |
| `<check-stats>`                 |                                        | Calculate message statistics for all mailboxes                          | [{bdg-info}`generic`](ref-fn-generic) |
| `<check-traditional-pgp>`       | `Esc P`                                | Check for classic PGP                                                   | [{bdg-success}`index`](ref-fn-index)  |
| `<clear-flag>`                  | `W`                                    | Clear a status flag from a message                                      | [{bdg-success}`index`](ref-fn-index)  |
| `<compose-to-sender>`           |                                        | Compose new message to the current message sender                       | [{bdg-success}`index`](ref-fn-index)  |
| `<copy-message>`                | `C`                                    | Copy a message to a file/mailbox                                        | [{bdg-success}`index`](ref-fn-index)  |
| `<create-alias>`                | `a`                                    | Create an alias from a message sender                                   | [{bdg-success}`index`](ref-fn-index)  |
| `<decode-copy>`                 | `Esc C`                                | Make decoded (text/plain) copy                                          | [{bdg-success}`index`](ref-fn-index)  |
| `<decode-save>`                 | `Esc s`                                | Make decoded copy (text/plain) and delete                               | [{bdg-success}`index`](ref-fn-index)  |
| `<decrypt-copy>`                |                                        | Make decrypted copy                                                     | [{bdg-success}`index`](ref-fn-index)  |
| `<decrypt-save>`                |                                        | Make decrypted copy and delete                                          | [{bdg-success}`index`](ref-fn-index)  |
| `<delete-message>`              | `d`                                    | Delete the current entry                                                | [{bdg-success}`index`](ref-fn-index)  |
| `<delete-subthread>`            | `Esc d`                                | Delete all messages in subthread                                        | [{bdg-success}`index`](ref-fn-index)  |
| `<delete-thread>`               | `^D`                                   | Delete all messages in thread                                           | [{bdg-success}`index`](ref-fn-index)  |
| `<display-address>`             | `@`                                    | Display full address of sender                                          | [{bdg-success}`index`](ref-fn-index)  |
| `<display-toggle-weed>`         | `h`                                    | Display message and toggle header weeding                               | [{bdg-success}`index`](ref-fn-index)  |
| `<edit>`                        |                                        | Edit the raw message (edit and edit-raw-message are synonyms)           | [{bdg-success}`index`](ref-fn-index)  |
| `<edit-label>`                  | `Y`                                    | Add, change, or delete a message's label                                | [{bdg-success}`index`](ref-fn-index)  |
| `<edit-or-view-raw-message>`    | `e`                                    | Edit the raw message if the mailbox is not read-only, otherwise view it | [{bdg-success}`index`](ref-fn-index)  |
| `<edit-raw-message>`            |                                        | Edit the raw message (edit and edit-raw-message are synonyms)           | [{bdg-success}`index`](ref-fn-index)  |
| `<edit-type>`                   | `^E`                                   | Edit attachment content type                                            | [{bdg-success}`index`](ref-fn-index)  |
| `<enter-command>`               | `:`                                    | Enter a neomuttrc command                                               | [{bdg-info}`generic`](ref-fn-generic) |
| `<entire-thread>`               |                                        | Read entire thread of the current message                               | [{bdg-success}`index`](ref-fn-index)  |
| `<exit>`                        | `q`, `x`                               | Exit this menu                                                          |                                       |
| `<extract-keys>`                | `^K`                                   | Extract supported public keys                                           | [{bdg-success}`index`](ref-fn-index)  |
| `<flag-message>`                | `F`                                    | Toggle a message's 'important' flag                                     | [{bdg-success}`index`](ref-fn-index)  |
| `<followup-message>`            |                                        | Followup to newsgroup                                                   | [{bdg-success}`index`](ref-fn-index)  |
| `<forget-passphrase>`           | `^F`                                   | Wipe passphrases from memory                                            | [{bdg-success}`index`](ref-fn-index)  |
| `<forward-message>`             | `f`                                    | Forward a message with comments                                         | [{bdg-success}`index`](ref-fn-index)  |
| `<forward-to-group>`            |                                        | Forward to newsgroup                                                    | [{bdg-success}`index`](ref-fn-index)  |
| `<group-chat-reply>`            |                                        | Reply to all recipients preserving `To:`/`Cc:`                          | [{bdg-success}`index`](ref-fn-index)  |
| `<group-reply>`                 | `g`                                    | Reply to all recipients                                                 | [{bdg-success}`index`](ref-fn-index)  |
| `<half-down>`                   |                                        | Scroll down 1/2 page                                                    |                                       |
| `<half-up>`                     |                                        | Scroll up 1/2 page                                                      |                                       |
| `<help>`                        | `?`                                    | Show help screen                                                        |                                       |
| `<imap-fetch-mail>`             |                                        | Force retrieval of mail from IMAP server                                | [{bdg-success}`index`](ref-fn-index)  |
| `<imap-logout-all>`             |                                        | Logout from all IMAP servers                                            | [{bdg-success}`index`](ref-fn-index)  |
| `<jump>`                        | `1`,`2`,`3`,`4`,`5`,`6`,`7`,`8`,`9`    | Jump to an index number                                                 | [{bdg-info}`generic`](ref-fn-generic) |
| `<link-threads>`                | `&`                                    | Link tagged message to the current one                                  | [{bdg-success}`index`](ref-fn-index)  |
| `<list-reply>`                  | `L`                                    | Reply to specified mailing list                                         | [{bdg-success}`index`](ref-fn-index)  |
| `<list-subscribe>`              |                                        | Subscribe to a mailing list                                             | [{bdg-success}`index`](ref-fn-index)  |
| `<list-unsubscribe>`            |                                        | Unsubscribe from a mailing list                                         | [{bdg-success}`index`](ref-fn-index)  |
| `<mail>`                        | `m`                                    | Compose a new mail message                                              | [{bdg-success}`index`](ref-fn-index)  |
| `<mail-key>`                    | `Esc k`                                | Mail a PGP public key                                                   | [{bdg-success}`index`](ref-fn-index)  |
| `<mailbox-list>`                | `.`                                    | List mailboxes with new mail                                            | [{bdg-success}`index`](ref-fn-index)  |
| `<mark-as-new>`                 | `N`                                    | Toggle a message's 'new' flag                                           | [{bdg-success}`index`](ref-fn-index)  |
| `<modify-labels>`               |                                        | Modify (notmuch/imap) tags                                              | [{bdg-success}`index`](ref-fn-index)  |
| `<modify-labels-then-hide>`     |                                        | Modify (notmuch/imap) tags and then hide message                        | [{bdg-success}`index`](ref-fn-index)  |
| `<modify-tags>`                 |                                        | Modify (notmuch/imap) tags                                              | [{bdg-success}`index`](ref-fn-index)  |
| `<modify-tags-then-hide>`       |                                        | Modify (notmuch/imap) tags and then hide message                        | [{bdg-success}`index`](ref-fn-index)  |
| `<next-entry>`                  | `J`                                    | Move to the next entry                                                  | [{bdg-info}`generic`](ref-fn-generic) |
| `<next-line>`                   | `<Enter>`, `<Return>`, `<KeypadEnter>` | Scroll down one line                                                    |                                       |
| `<next-new>`                    |                                        | Jump to the next new message                                            | [{bdg-success}`index`](ref-fn-index)  |
| `<next-new-then-unread>`        | `<Tab>`                                | Jump to the next new or unread message                                  | [{bdg-success}`index`](ref-fn-index)  |
| `<next-page>`                   | `<PageDown>` , `<Space>`               | Move to the next page                                                   |                                       |
| `<next-subthread>`              | `Esc n`                                | Jump to the next subthread                                              | [{bdg-success}`index`](ref-fn-index)  |
| `<next-thread>`                 | `^N`                                   | Jump to the next thread                                                 | [{bdg-success}`index`](ref-fn-index)  |
| `<next-undeleted>`              | `<Down>`, `<Right>`, `j`               | Move to the next undeleted message                                      | [{bdg-success}`index`](ref-fn-index)  |
| `<next-unread>`                 |                                        | Jump to the next unread message                                         | [{bdg-success}`index`](ref-fn-index)  |
| `<next-unread-mailbox>`         |                                        | Open next mailbox with new mail                                         | [{bdg-success}`index`](ref-fn-index)  |
| `<parent-message>`              | `P`                                    | Jump to parent message in thread                                        | [{bdg-success}`index`](ref-fn-index)  |
| `<pipe-entry>`                  |                                        | Pipe message/attachment to a shell command                              | [{bdg-success}`index`](ref-fn-index)  |
| `<pipe-message>`                | `\|`                                   | Pipe message/attachment to a shell command                              | [{bdg-success}`index`](ref-fn-index)  |
| `<post-message>`                |                                        | Post message to newsgroup                                               | [{bdg-success}`index`](ref-fn-index)  |
| `<previous-entry>`              | `K`                                    | Move to the previous entry                                              | [{bdg-info}`generic`](ref-fn-generic) |
| `<previous-line>`               | `<BackSpace>`                          | Scroll up one line                                                      |                                       |
| `<previous-new>`                |                                        | Jump to the previous new message                                        | [{bdg-success}`index`](ref-fn-index)  |
| `<previous-new-then-unread>`    |                                        | Jump to the previous new or unread message                              | [{bdg-success}`index`](ref-fn-index)  |
| `<previous-page>`               | `<PageUp>`, `-`                        | Move to the previous page                                               |                                       |
| `<previous-subthread>`          | `Esc p`                                | Jump to previous subthread                                              | [{bdg-success}`index`](ref-fn-index)  |
| `<previous-thread>`             | `^P`                                   | Jump to previous thread                                                 | [{bdg-success}`index`](ref-fn-index)  |
| `<previous-undeleted>`          | `<Up>`, `<Left>`, `k`                  | Move to the previous undeleted message                                  | [{bdg-success}`index`](ref-fn-index)  |
| `<previous-unread>`             |                                        | Jump to the previous unread message                                     | [{bdg-success}`index`](ref-fn-index)  |
| `<print-entry>`                 |                                        | Print the current entry                                                 | [{bdg-success}`index`](ref-fn-index)  |
| `<print-message>`               | `p`                                    | Print the current entry                                                 | [{bdg-success}`index`](ref-fn-index)  |
| `<purge-message>`               |                                        | Delete the current entry, bypassing the trash folder                    | [{bdg-success}`index`](ref-fn-index)  |
| `<purge-thread>`                |                                        | Delete the current thread, bypassing the trash folder                   | [{bdg-success}`index`](ref-fn-index)  |
| `<quasi-delete>`                |                                        | Delete from NeoMutt, don't touch on disk                                | [{bdg-success}`index`](ref-fn-index)  |
| `<quit>`                        | `Q`                                    | Save changes to mailbox and quit                                        | [{bdg-success}`index`](ref-fn-index)  |
| `<read-subthread>`              | `Esc r`                                | Mark the current subthread as read                                      | [{bdg-success}`index`](ref-fn-index)  |
| `<read-thread>`                 | `^R`                                   | Mark the current thread as read                                         | [{bdg-success}`index`](ref-fn-index)  |
| `<recall-message>`              | `R`                                    | Recall a postponed message                                              | [{bdg-success}`index`](ref-fn-index)  |
| `<reconstruct-thread>`          |                                        | Reconstruct thread containing current message                           | [{bdg-success}`index`](ref-fn-index)  |
| `<redraw-screen>`               | `^L`                                   | Clear and redraw the screen                                             | [{bdg-info}`generic`](ref-fn-generic) |
| `<reply>`                       | `r`                                    | Reply to a message                                                      | [{bdg-success}`index`](ref-fn-index)  |
| `<resend-message>`              | `Esc e`                                | Use the current message as a template for a new one                     | [{bdg-success}`index`](ref-fn-index)  |
| `<root-message>`                |                                        | Jump to root message in thread                                          | [{bdg-success}`index`](ref-fn-index)  |
| `<save-entry>`                  |                                        | Save message/attachment to a mailbox/file                               | [{bdg-success}`index`](ref-fn-index)  |
| `<save-message>`                | `s`                                    | Save message/attachment to a mailbox/file                               |                                       |
| `<search>`                      | `/`                                    | Search for a regular expression                                         |                                       |
| `<search-next>`                 | `n`                                    | Search for next match                                                   |                                       |
| `<search-opposite>`             |                                        | Search for next match in opposite direction                             |                                       |
| `<search-reverse>`              | `Esc /`                                | Search backwards for a regular expression                               |                                       |
| `<search-toggle>`               | `\\`                                   | Toggle search pattern coloring                                          |                                       |
| `<set-flag>`                    | `w`                                    | Set a status flag on a message                                          | [{bdg-success}`index`](ref-fn-index)  |
| `<shell-escape>`                | `!`                                    | Invoke a command in a subshell                                          | [{bdg-info}`generic`](ref-fn-generic) |
| `<show-log-messages>`           |                                        | Show log (and debug) messages                                           | [{bdg-info}`generic`](ref-fn-generic) |
| `<show-version>`                | `V`                                    | Show the NeoMutt version number and date                                | [{bdg-info}`generic`](ref-fn-generic) |
| `<skip-headers>`                | `H`                                    | Jump to first line after headers                                        |                                       |
| `<skip-quoted>`                 | `S`                                    | Skip beyond quoted text                                                 |                                       |
| `<sort-mailbox>`                | `o`                                    | Sort messages                                                           | [{bdg-success}`index`](ref-fn-index)  |
| `<sort-reverse>`                | `O`                                    | Sort messages in reverse order                                          | [{bdg-success}`index`](ref-fn-index)  |
| `<sync-mailbox>`                | `$`                                    | Save changes to mailbox                                                 | [{bdg-success}`index`](ref-fn-index)  |
| `<tag-message>`                 | `t`                                    | Tag the current entry                                                   | [{bdg-info}`generic`](ref-fn-generic) |
| `<toggle-quoted>`               | `T`                                    | Toggle display of quoted text                                           |                                       |
| `<toggle-write>`                | `%`                                    | Toggle whether the mailbox will be rewritten                            | [{bdg-success}`index`](ref-fn-index)  |
| `<top>`                         | `<Home>`, `^`                          | Jump to the top of the message                                          |                                       |
| `<undelete-message>`            | `u`                                    | Undelete the current entry                                              | [{bdg-success}`index`](ref-fn-index)  |
| `<undelete-subthread>`          | `Esc u`                                | Undelete all messages in subthread                                      | [{bdg-success}`index`](ref-fn-index)  |
| `<undelete-thread>`             | `^U`                                   | Undelete all messages in thread                                         | [{bdg-success}`index`](ref-fn-index)  |
| `<vfolder-from-query>`          |                                        | Generate virtual folder from query                                      | [{bdg-success}`index`](ref-fn-index)  |
| `<vfolder-from-query-readonly>` |                                        | Generate a read-only virtual folder from query                          | [{bdg-success}`index`](ref-fn-index)  |
| `<view-attachments>`            | `v`                                    | Show MIME attachments                                                   |                                       |
| `<view-raw-message>`            |                                        | Show the raw message                                                    | [{bdg-success}`index`](ref-fn-index)  |
| `<what-key>`                    |                                        | Display the keycode for a key press                                     | [{bdg-info}`generic`](ref-fn-generic) |

