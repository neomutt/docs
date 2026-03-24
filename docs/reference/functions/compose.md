---
title: Compose Menu
description: Default Keys bindings and functions for the NeoMutt Compose Menu.
keywords: neomutt, functions, compose, menu, bindings, keys, email
---

(menu-compose)=
# Compose Menu

Prepare an email before sending it.
You can edit recipients, subject, and headers, attach files, configure encryption, and send or postpone the message.

| Function                | Default Keys                           | Description                                          | Inhertied from                      |
|-------------------------|----------------------------------------|------------------------------------------------------|-------------------------------------|
| `<attach-file>`         | `a`                                    | Attach files to this message                         |                                     |
| `<attach-key>`          | `Esc k`                                | Attach a PGP public key                              |                                     |
| `<attach-message>`      | `A`                                    | Attach messages to this message                      |                                     |
| `<attach-news-message>` |                                        | Attach news articles to this message                 |                                     |
| `<autocrypt-menu>`      | `o`                                    | Show autocrypt compose menu options                  |                                     |
| `<copy-file>`           | `C`                                    | Save message/attachment to a mailbox/file            |                                     |
| `<detach-file>`         | `D`                                    | Delete the current entry                             |                                     |
| `<display-toggle-weed>` | `h`                                    | Display message and toggle header weeding            |                                     |
| `<edit-bcc>`            | `b`                                    | Edit the BCC list                                    |                                     |
| `<edit-cc>`             | `c`                                    | Edit the CC list                                     |                                     |
| `<edit-content-id>`     | `Esc i`                                | Edit the 'Content-ID' of the attachment              |                                     |
| `<edit-description>`    | `d`                                    | Edit attachment description                          |                                     |
| `<edit-encoding>`       | `^E`                                   | Edit attachment transfer-encoding                    |                                     |
| `<edit-fcc>`            | `f`                                    | Enter a file to save a copy of this message in       |                                     |
| `<edit-file>`           | `Esc e`                                | Edit the file to be attached                         |                                     |
| `<edit-followup-to>`    |                                        | Edit the Followup-To field                           |                                     |
| `<edit-from>`           | `Esc f`                                | Edit the from field                                  |                                     |
| `<edit-headers>`        | `E`                                    | Edit the message with headers                        |                                     |
| `<edit-language>`       | `^L`                                   | Edit the 'Content-Language' of the attachment        |                                     |
| `<edit-message>`        | `e`                                    | Edit the message                                     |                                     |
| `<edit-mime>`           | `m`                                    | Edit attachment using mailcap entry                  |                                     |
| `<edit-newsgroups>`     |                                        | Edit the newsgroups list                             |                                     |
| `<edit-reply-to>`       | `r`                                    | Edit the Reply-To field                              |                                     |
| `<edit-subject>`        | `s`                                    | Edit the subject of this message                     |                                     |
| `<edit-to>`             | `t`                                    | Edit the TO list                                     |                                     |
| `<edit-type>`           | `^T`                                   | Edit attachment content type                         |                                     |
| `<edit-x-comment-to>`   |                                        | Edit the X-Comment-To field                          |                                     |
| `<exit>`                | `q`                                    | Exit this menu                                       |                                     |
| `<filter-entry>`        | `F`                                    | Filter attachment through a shell command            |                                     |
| `<forget-passphrase>`   | `^F`                                   | Wipe passphrases from memory                         |                                     |
| `<get-attachment>`      | `G`                                    | Get a temporary copy of an attachment                |                                     |
| `<group-alternatives>`  | `&`                                    | Group tagged attachments as 'multipart/alternative'  |                                     |
| `<group-multilingual>`  | `^`                                    | Group tagged attachments as 'multipart/multilingual' |                                     |
| `<group-related>`       | `%`                                    | Group tagged attachments as 'multipart/related'      |                                     |
| `<ispell>`              | `i`                                    | Run ispell on the message                            |                                     |
| `<move-down>`           | `+`                                    | Move an attachment down in the attachment list       |                                     |
| `<move-up>`             | `-`                                    | Move an attachment up in the attachment list         |                                     |
| `<new-mime>`            | `n`                                    | Compose new attachment using mailcap entry           |                                     |
| `<pgp-menu>`            | `p`                                    | Show PGP options                                     |                                     |
| `<pipe-entry>`          |                                        | Pipe message/attachment to a shell command           |                                     |
| `<pipe-message>`        | `\|`                                   | Pipe message/attachment to a shell command           |                                     |
| `<postpone-message>`    | `P`                                    | Save this message to send later                      |                                     |
| `<preview-page-down>`   | `<PageDown>`                           | Show the next page of the message                    |                                     |
| `<preview-page-up>`     | `<PageUp>`                             | Show the previous page of the message                |                                     |
| `<print-entry>`         | `l`                                    | Print the current entry                              |                                     |
| `<rename-attachment>`   | `^O`                                   | Send attachment with a different name                |                                     |
| `<rename-file>`         | `R`                                    | Rename/move an attached file                         |                                     |
| `<send-message>`        | `y`                                    | Send the message                                     |                                     |
| `<smime-menu>`          | `S`                                    | Show S/MIME options                                  |                                     |
| `<tag-entry>`           | `T`                                    | Tag the current entry                                | [{bdg-info}`generic`](menu-generic) |
| `<toggle-disposition>`  | `^D`                                   | Toggle disposition between inline/attachment         |                                     |
| `<toggle-recode>`       |                                        | Toggle recoding of this attachment                   |                                     |
| `<toggle-unlink>`       | `u`                                    | Toggle whether to delete file after sending it       |                                     |
| `<ungroup-attachment>`  | `#`                                    | Ungroup 'multipart' attachment                       |                                     |
| `<update-encoding>`     | `U`                                    | Update an attachment's encoding info                 |                                     |
| `<view-attach>`         | `<Enter>`, `<Return>`, `<KeypadEnter>` | View attachment using mailcap entry if necessary     |                                     |
| `<view-mailcap>`        |                                        | Force viewing of attachment using mailcap            |                                     |
| `<view-pager>`          |                                        | View attachment in pager using copiousoutput mailcap |                                     |
| `<view-text>`           |                                        | View attachment as text                              |                                     |
| `<write-fcc>`           | `w`                                    | Write the message to a folder                        |                                     |

