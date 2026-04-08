---
title: Attach Functions
description: Key bindings and functions for viewing, saving, printing, and replying from email attachments in NeoMutt
keywords: neomutt, functions, attach, menu, bindings, keys, attachments, save-entry, view-attach, view-mailcap, pipe-message, forward-message, reply, mime
---

(menu-attach)=
# Attach Functions

View and manage the attachments of a received email.
You can save, print, pipe, delete, or open attachments, and reply or forward from this view.

| Function                  | Default Keys                                          | Description                                          |
|---------------------------|-------------------------------------------------------|------------------------------------------------------|
| `<bounce-message>`        | {kbd}`b`                                              | Remail a message to another user                     |
| `<check-traditional-pgp>` | {kbd}`Alt-P`                                          | Check for classic PGP                                |
| `<collapse-parts>`        | {kbd}`v`                                              | Toggle display of subparts                           |
| `<compose-to-sender>`     |                                                       | Compose new message to the current message sender    |
| `<delete-entry>`          | {kbd}`d`                                              | Delete the current entry                             |
| `<display-toggle-weed>`   | {kbd}`h`                                              | Display message and toggle header weeding            |
| `<edit-type>`             | {kbd}`Ctrl-E`                                         | Edit attachment content type                         |
| `<exit>`                  | {kbd}`q`                                              | Exit this menu                                       |
| `<extract-keys>`          | {kbd}`Ctrl-K`                                         | Extract supported public keys                        |
| `<followup-message>`      |                                                       | Followup to newsgroup                                |
| `<forget-passphrase>`     | {kbd}`Ctrl-F`                                         | Wipe passphrases from memory                         |
| `<forward-message>`       | {kbd}`f`                                              | Forward a message with comments                      |
| `<forward-to-group>`      |                                                       | Forward to newsgroup                                 |
| `<group-chat-reply>`      |                                                       | Reply to all recipients preserving `To:`/`Cc:`       |
| `<group-reply>`           | {kbd}`g`                                              | Reply to all recipients                              |
| `<list-reply>`            | {kbd}`L`                                              | Reply to specified mailing list                      |
| `<list-subscribe>`        |                                                       | Subscribe to a mailing list                          |
| `<list-unsubscribe>`      |                                                       | Unsubscribe from a mailing list                      |
| `<pipe-entry>`            |                                                       | Pipe message/attachment to a shell command           |
| `<pipe-message>`          | {kbd}`\|`                                             | Pipe message/attachment to a shell command           |
| `<print-entry>`           | {kbd}`p`                                              | Print the current entry                              |
| `<reply>`                 | {kbd}`r`                                              | Reply to a message                                   |
| `<resend-message>`        | {kbd}`Alt-e`                                          | Use the current message as a template for a new one  |
| `<save-entry>`            | {kbd}`s`                                              | Save message/attachment to a mailbox/file            |
| `<undelete-entry>`        | {kbd}`u`                                              | Undelete the current entry                           |
| `<view-attach>`           | {kbd}`<Enter>`, {kbd}`<Return>`, {kbd}`<KeypadEnter>` | View attachment using mailcap entry if necessary     |
| `<view-mailcap>`          | {kbd}`m`                                              | Force viewing of attachment using mailcap            |
| `<view-pager>`            |                                                       | View attachment in pager using copiousoutput mailcap |
| `<view-text>`             | {kbd}`T`                                              | View attachment as text                              |

