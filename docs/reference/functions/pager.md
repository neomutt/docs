---
title: Pager Menu
description: Default Keys bindings and functions for the NeoMutt Pager Menu.
keywords: neomutt, functions, pager, menu, bindings, keys, reading
---

(menu-pager)=
# Pager Menu

The email reading view that displays a message's contents.
You can scroll, search within the text, and perform many of the same actions as the index.

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

| Function                        | Default Keys                           | Description                                                             | Inherited From                      |
|---------------------------------|----------------------------------------|-------------------------------------------------------------------------|-------------------------------------|
| `<bottom>`                      | `<End>`                                | jump to the bottom of the message                                       |                                     |
| `<bounce-message>`              | `b`                                    | remail a message to another user                                        | [{bdg-success}`index`](menu-index)  |
| `<break-thread>`                | `#`                                    | break the thread in two                                                 | [{bdg-success}`index`](menu-index)  |
| `<change-folder>`               | `c`                                    | open a different folder                                                 | [{bdg-success}`index`](menu-index)  |
| `<change-folder-readonly>`      | `Esc c`                                | open a different folder in read only mode                               | [{bdg-success}`index`](menu-index)  |
| `<change-newsgroup>`            |                                        | open a different newsgroup                                              | [{bdg-success}`index`](menu-index)  |
| `<change-newsgroup-readonly>`   |                                        | open a different newsgroup in read only mode                            | [{bdg-success}`index`](menu-index)  |
| `<change-vfolder>`              |                                        | open a different virtual folder                                         | [{bdg-success}`index`](menu-index)  |
| `<check-stats>`                 |                                        | calculate message statistics for all mailboxes                          | [{bdg-info}`generic`](menu-generic) |
| `<check-traditional-pgp>`       | `Esc P`                                | check for classic PGP                                                   | [{bdg-success}`index`](menu-index)  |
| `<clear-flag>`                  | `W`                                    | clear a status flag from a message                                      | [{bdg-success}`index`](menu-index)  |
| `<compose-to-sender>`           |                                        | compose new message to the current message sender                       | [{bdg-success}`index`](menu-index)  |
| `<copy-message>`                | `C`                                    | copy a message to a file/mailbox                                        | [{bdg-success}`index`](menu-index)  |
| `<create-alias>`                | `a`                                    | create an alias from a message sender                                   | [{bdg-success}`index`](menu-index)  |
| `<decode-copy>`                 | `Esc C`                                | make decoded (text/plain) copy                                          | [{bdg-success}`index`](menu-index)  |
| `<decode-save>`                 | `Esc s`                                | make decoded copy (text/plain) and delete                               | [{bdg-success}`index`](menu-index)  |
| `<decrypt-copy>`                |                                        | make decrypted copy                                                     | [{bdg-success}`index`](menu-index)  |
| `<decrypt-save>`                |                                        | make decrypted copy and delete                                          | [{bdg-success}`index`](menu-index)  |
| `<delete-message>`              | `d`                                    | delete the current entry                                                | [{bdg-success}`index`](menu-index)  |
| `<delete-subthread>`            | `Esc d`                                | delete all messages in subthread                                        | [{bdg-success}`index`](menu-index)  |
| `<delete-thread>`               | `^D`                                   | delete all messages in thread                                           | [{bdg-success}`index`](menu-index)  |
| `<display-address>`             | `@`                                    | display full address of sender                                          | [{bdg-success}`index`](menu-index)  |
| `<display-toggle-weed>`         | `h`                                    | display message and toggle header weeding                               | [{bdg-success}`index`](menu-index)  |
| `<edit>`                        |                                        | edit the raw message (edit and edit-raw-message are synonyms)           | [{bdg-success}`index`](menu-index)  |
| `<edit-label>`                  | `Y`                                    | add, change, or delete a message's label                                | [{bdg-success}`index`](menu-index)  |
| `<edit-or-view-raw-message>`    | `e`                                    | edit the raw message if the mailbox is not read-only, otherwise view it | [{bdg-success}`index`](menu-index)  |
| `<edit-raw-message>`            |                                        | edit the raw message (edit and edit-raw-message are synonyms)           | [{bdg-success}`index`](menu-index)  |
| `<edit-type>`                   | `^E`                                   | edit attachment content type                                            | [{bdg-success}`index`](menu-index)  |
| `<enter-command>`               | `:`                                    | enter a neomuttrc command                                               | [{bdg-info}`generic`](menu-generic) |
| `<entire-thread>`               |                                        | read entire thread of the current message                               | [{bdg-success}`index`](menu-index)  |
| `<exit>`                        | `q`, `x`                               | exit this menu                                                          |                                     |
| `<extract-keys>`                | `^K`                                   | extract supported public keys                                           | [{bdg-success}`index`](menu-index)  |
| `<flag-message>`                | `F`                                    | toggle a message's 'important' flag                                     | [{bdg-success}`index`](menu-index)  |
| `<followup-message>`            |                                        | followup to newsgroup                                                   | [{bdg-success}`index`](menu-index)  |
| `<forget-passphrase>`           | `^F`                                   | wipe passphrases from memory                                            | [{bdg-success}`index`](menu-index)  |
| `<forward-message>`             | `f`                                    | forward a message with comments                                         | [{bdg-success}`index`](menu-index)  |
| `<forward-to-group>`            |                                        | forward to newsgroup                                                    | [{bdg-success}`index`](menu-index)  |
| `<group-chat-reply>`            |                                        | reply to all recipients preserving To/Cc                                | [{bdg-success}`index`](menu-index)  |
| `<group-reply>`                 | `g`                                    | reply to all recipients                                                 | [{bdg-success}`index`](menu-index)  |
| `<half-down>`                   |                                        | scroll down 1/2 page                                                    |                                     |
| `<half-up>`                     |                                        | scroll up 1/2 page                                                      |                                     |
| `<help>`                        | `?`                                    | this screen                                                             |                                     |
| `<imap-fetch-mail>`             |                                        | force retrieval of mail from IMAP server                                | [{bdg-success}`index`](menu-index)  |
| `<imap-logout-all>`             |                                        | logout from all IMAP servers                                            | [{bdg-success}`index`](menu-index)  |
| `<jump>`                        | `1`,`2`,`3`,`4`,`5`,`6`,`7`,`8`,`9`    | jump to an index number                                                 | [{bdg-info}`generic`](menu-generic) |
| `<link-threads>`                | `&`                                    | link tagged message to the current one                                  | [{bdg-success}`index`](menu-index)  |
| `<list-reply>`                  | `L`                                    | reply to specified mailing list                                         | [{bdg-success}`index`](menu-index)  |
| `<list-subscribe>`              |                                        | subscribe to a mailing list                                             | [{bdg-success}`index`](menu-index)  |
| `<list-unsubscribe>`            |                                        | unsubscribe from a mailing list                                         | [{bdg-success}`index`](menu-index)  |
| `<mail>`                        | `m`                                    | compose a new mail message                                              | [{bdg-success}`index`](menu-index)  |
| `<mail-key>`                    | `Esc k`                                | mail a PGP public key                                                   | [{bdg-success}`index`](menu-index)  |
| `<mailbox-list>`                | `.`                                    | list mailboxes with new mail                                            | [{bdg-success}`index`](menu-index)  |
| `<mark-as-new>`                 | `N`                                    | toggle a message's 'new' flag                                           | [{bdg-success}`index`](menu-index)  |
| `<modify-labels>`               |                                        | modify (notmuch/imap) tags                                              | [{bdg-success}`index`](menu-index)  |
| `<modify-labels-then-hide>`     |                                        | modify (notmuch/imap) tags and then hide message                        | [{bdg-success}`index`](menu-index)  |
| `<modify-tags>`                 |                                        | modify (notmuch/imap) tags                                              | [{bdg-success}`index`](menu-index)  |
| `<modify-tags-then-hide>`       |                                        | modify (notmuch/imap) tags and then hide message                        | [{bdg-success}`index`](menu-index)  |
| `<next-entry>`                  | `J`                                    | move to the next entry                                                  | [{bdg-info}`generic`](menu-generic) |
| `<next-line>`                   | `<Enter>`, `<Return>`, `<KeypadEnter>` | scroll down one line                                                    |                                     |
| `<next-new>`                    |                                        | jump to the next new message                                            | [{bdg-success}`index`](menu-index)  |
| `<next-new-then-unread>`        | `<Tab>`                                | jump to the next new or unread message                                  | [{bdg-success}`index`](menu-index)  |
| `<next-page>`                   | `<PageDown>` , `<Space>`               | move to the next page                                                   |                                     |
| `<next-subthread>`              | `Esc n`                                | jump to the next subthread                                              | [{bdg-success}`index`](menu-index)  |
| `<next-thread>`                 | `^N`                                   | jump to the next thread                                                 | [{bdg-success}`index`](menu-index)  |
| `<next-undeleted>`              | `<Down>`, `<Right>`, `j`               | move to the next undeleted message                                      | [{bdg-success}`index`](menu-index)  |
| `<next-unread>`                 |                                        | jump to the next unread message                                         | [{bdg-success}`index`](menu-index)  |
| `<next-unread-mailbox>`         |                                        | open next mailbox with new mail                                         | [{bdg-success}`index`](menu-index)  |
| `<parent-message>`              | `P`                                    | jump to parent message in thread                                        | [{bdg-success}`index`](menu-index)  |
| `<pipe-entry>`                  |                                        | pipe message/attachment to a shell command                              | [{bdg-success}`index`](menu-index)  |
| `<pipe-message>`                | `\|`                                   | pipe message/attachment to a shell command                              | [{bdg-success}`index`](menu-index)  |
| `<post-message>`                |                                        | post message to newsgroup                                               | [{bdg-success}`index`](menu-index)  |
| `<previous-entry>`              | `K`                                    | move to the previous entry                                              | [{bdg-info}`generic`](menu-generic) |
| `<previous-line>`               | `<BackSpace>`                          | scroll up one line                                                      |                                     |
| `<previous-new>`                |                                        | jump to the previous new message                                        | [{bdg-success}`index`](menu-index)  |
| `<previous-new-then-unread>`    |                                        | jump to the previous new or unread message                              | [{bdg-success}`index`](menu-index)  |
| `<previous-page>`               | `<PageUp>`, `-`                        | move to the previous page                                               |                                     |
| `<previous-subthread>`          | `Esc p`                                | jump to previous subthread                                              | [{bdg-success}`index`](menu-index)  |
| `<previous-thread>`             | `^P`                                   | jump to previous thread                                                 | [{bdg-success}`index`](menu-index)  |
| `<previous-undeleted>`          | `<Up>`, `<Left>`, `k`                  | move to the previous undeleted message                                  | [{bdg-success}`index`](menu-index)  |
| `<previous-unread>`             |                                        | jump to the previous unread message                                     | [{bdg-success}`index`](menu-index)  |
| `<print-entry>`                 |                                        | print the current entry                                                 | [{bdg-success}`index`](menu-index)  |
| `<print-message>`               | `p`                                    | print the current entry                                                 | [{bdg-success}`index`](menu-index)  |
| `<purge-message>`               |                                        | delete the current entry, bypassing the trash folder                    | [{bdg-success}`index`](menu-index)  |
| `<purge-thread>`                |                                        | delete the current thread, bypassing the trash folder                   | [{bdg-success}`index`](menu-index)  |
| `<quasi-delete>`                |                                        | delete from NeoMutt, don't touch on disk                                | [{bdg-success}`index`](menu-index)  |
| `<quit>`                        | `Q`                                    | save changes to mailbox and quit                                        | [{bdg-success}`index`](menu-index)  |
| `<read-subthread>`              | `Esc r`                                | mark the current subthread as read                                      | [{bdg-success}`index`](menu-index)  |
| `<read-thread>`                 | `^R`                                   | mark the current thread as read                                         | [{bdg-success}`index`](menu-index)  |
| `<recall-message>`              | `R`                                    | recall a postponed message                                              | [{bdg-success}`index`](menu-index)  |
| `<reconstruct-thread>`          |                                        | reconstruct thread containing current message                           | [{bdg-success}`index`](menu-index)  |
| `<redraw-screen>`               | `^L`                                   | clear and redraw the screen                                             | [{bdg-info}`generic`](menu-generic) |
| `<reply>`                       | `r`                                    | reply to a message                                                      | [{bdg-success}`index`](menu-index)  |
| `<resend-message>`              | `Esc e`                                | use the current message as a template for a new one                     | [{bdg-success}`index`](menu-index)  |
| `<root-message>`                |                                        | jump to root message in thread                                          | [{bdg-success}`index`](menu-index)  |
| `<save-entry>`                  |                                        | save message/attachment to a mailbox/file                               | [{bdg-success}`index`](menu-index)  |
| `<save-message>`                | `s`                                    | save message/attachment to a mailbox/file                               |                                     |
| `<search>`                      | `/`                                    | search for a regular expression                                         |                                     |
| `<search-next>`                 | `n`                                    | search for next match                                                   |                                     |
| `<search-opposite>`             |                                        | search for next match in opposite direction                             |                                     |
| `<search-reverse>`              | `Esc /`                                | search backwards for a regular expression                               |                                     |
| `<search-toggle>`               | `\\`                                   | toggle search pattern coloring                                          |                                     |
| `<set-flag>`                    | `w`                                    | set a status flag on a message                                          | [{bdg-success}`index`](menu-index)  |
| `<shell-escape>`                | `!`                                    | invoke a command in a subshell                                          | [{bdg-info}`generic`](menu-generic) |
| `<show-log-messages>`           |                                        | show log (and debug) messages                                           | [{bdg-info}`generic`](menu-generic) |
| `<show-version>`                | `V`                                    | show the NeoMutt version number and date                                | [{bdg-info}`generic`](menu-generic) |
| `<skip-headers>`                | `H`                                    | jump to first line after headers                                        |                                     |
| `<skip-quoted>`                 | `S`                                    | skip beyond quoted text                                                 |                                     |
| `<sort-mailbox>`                | `o`                                    | sort messages                                                           | [{bdg-success}`index`](menu-index)  |
| `<sort-reverse>`                | `O`                                    | sort messages in reverse order                                          | [{bdg-success}`index`](menu-index)  |
| `<sync-mailbox>`                | `$`                                    | save changes to mailbox                                                 | [{bdg-success}`index`](menu-index)  |
| `<tag-message>`                 | `t`                                    | tag the current entry                                                   | [{bdg-info}`generic`](menu-generic) |
| `<toggle-quoted>`               | `T`                                    | toggle display of quoted text                                           |                                     |
| `<toggle-write>`                | `%`                                    | toggle whether the mailbox will be rewritten                            | [{bdg-success}`index`](menu-index)  |
| `<top>`                         | `<Home>`, `^`                          | jump to the top of the message                                          |                                     |
| `<undelete-message>`            | `u`                                    | undelete the current entry                                              | [{bdg-success}`index`](menu-index)  |
| `<undelete-subthread>`          | `Esc u`                                | undelete all messages in subthread                                      | [{bdg-success}`index`](menu-index)  |
| `<undelete-thread>`             | `^U`                                   | undelete all messages in thread                                         | [{bdg-success}`index`](menu-index)  |
| `<vfolder-from-query>`          |                                        | generate virtual folder from query                                      | [{bdg-success}`index`](menu-index)  |
| `<vfolder-from-query-readonly>` |                                        | generate a read-only virtual folder from query                          | [{bdg-success}`index`](menu-index)  |
| `<view-attachments>`            | `v`                                    | show MIME attachments                                                   |                                     |
| `<view-raw-message>`            |                                        | show the raw message                                                    | [{bdg-success}`index`](menu-index)  |
| `<what-key>`                    |                                        | display the keycode for a key press                                     | [{bdg-info}`generic`](menu-generic) |

