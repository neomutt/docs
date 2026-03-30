---
title: Attach Functions
description: Key bindings and functions for viewing, saving, printing, and replying from email attachments in NeoMutt
keywords: neomutt, functions, attach, menu, bindings, keys, attachments, save-entry, view-attach, view-mailcap, pipe-message, forward-message, reply, mime
---

(fn-attach)=
# Attach Functions

View and manage the attachments of a received email.
You can save, print, pipe, delete, or open attachments, and reply or forward from this view.

| Function                  | Default Keys                           | Description                                          |
|---------------------------|----------------------------------------|------------------------------------------------------|
| `<bounce-message>`        | `b`                                    | Remail a message to another user                     |
| `<check-traditional-pgp>` | `Esc P`                                | Check for classic PGP                                |
| `<collapse-parts>`        | `v`                                    | Toggle display of subparts                           |
| `<compose-to-sender>`     |                                        | Compose new message to the current message sender    |
| `<delete-entry>`          | `d`                                    | Delete the current entry                             |
| `<display-toggle-weed>`   | `h`                                    | Display message and toggle header weeding            |
| `<edit-type>`             | `^E`                                   | Edit attachment content type                         |
| `<exit>`                  | `q`                                    | Exit this menu                                       |
| `<extract-keys>`          | `^K`                                   | Extract supported public keys                        |
| `<followup-message>`      |                                        | Followup to newsgroup                                |
| `<forget-passphrase>`     | `^F`                                   | Wipe passphrases from memory                         |
| `<forward-message>`       | `f`                                    | Forward a message with comments                      |
| `<forward-to-group>`      |                                        | Forward to newsgroup                                 |
| `<group-chat-reply>`      |                                        | Reply to all recipients preserving To/Cc             |
| `<group-reply>`           | `g`                                    | Reply to all recipients                              |
| `<list-reply>`            | `L`                                    | Reply to specified mailing list                      |
| `<list-subscribe>`        |                                        | Subscribe to a mailing list                          |
| `<list-unsubscribe>`      |                                        | Unsubscribe from a mailing list                      |
| `<pipe-entry>`            |                                        | Pipe message/attachment to a shell command           |
| `<pipe-message>`          | `\|`                                   | Pipe message/attachment to a shell command           |
| `<print-entry>`           | `p`                                    | Print the current entry                              |
| `<reply>`                 | `r`                                    | Reply to a message                                   |
| `<resend-message>`        | `Esc e`                                | Use the current message as a template for a new one  |
| `<save-entry>`            | `s`                                    | Save message/attachment to a mailbox/file            |
| `<undelete-entry>`        | `u`                                    | Undelete the current entry                           |
| `<view-attach>`           | `<Enter>`, `<Return>`, `<KeypadEnter>` | View attachment using mailcap entry if necessary     |
| `<view-mailcap>`          | `m`                                    | Force viewing of attachment using mailcap            |
| `<view-pager>`            |                                        | View attachment in pager using copiousoutput mailcap |
| `<view-text>`             | `T`                                    | View attachment as text                              |

