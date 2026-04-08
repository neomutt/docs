---
title: Compose Functions
description: Key bindings and functions for editing recipients, attachments, encryption, and sending email in the NeoMutt compose screen
keywords: neomutt, functions, compose, menu, bindings, keys, writing email, message editor, send-message, attach-file, edit-to, edit-subject, pgp-menu, smime-menu, postpone-message, attachments
---

(fn-compose)=
# Compose Functions

Prepare an email before sending it.
You can edit recipients, subject, and headers, attach files, configure encryption, and send or postpone the message.

## Attach Functions

| Function                | Default Keys                           | Description                                          | Inherited From                    |
|-------------------------|----------------------------------------|------------------------------------------------------|-----------------------------------|
| `<attach-file>`         | `a`                                    | Attach files to this message                         |                                   |
| `<attach-key>`          | `Esc k`                                | Attach a PGP public key                              |                                   |
| `<attach-message>`      | `A`                                    | Attach messages to this message                      |                                   |
| `<attach-news-message>` |                                        | Attach news articles to this message                 |                                   |
| `<copy-file>`           | `C`                                    | Save message/attachment to a mailbox/file            |                                   |
| `<detach-file>`         | `D`                                    | Delete the current entry                             |                                   |
| `<edit-content-id>`     | `Esc i`                                | Edit the `Content-ID` of the attachment              |                                   |
| `<edit-description>`    | `d`                                    | Edit attachment description                          |                                   |
| `<edit-encoding>`       | `^E`                                   | Edit attachment transfer-encoding                    |                                   |
| `<edit-language>`       | `^L`                                   | Edit the `Content-Language` of the attachment        |                                   |
| `<edit-mime>`           | `m`                                    | Edit attachment using mailcap entry                  |                                   |
| `<edit-type>`           | `^T`                                   | Edit attachment content type                         |                                   |
| `<filter-entry>`        | `F`                                    | Filter attachment through a shell command            |                                   |
| `<get-attachment>`      | `G`                                    | Get a temporary copy of an attachment                |                                   |
| `<group-alternatives>`  | `&`                                    | Group tagged attachments as 'multipart/alternative'  |                                   |
| `<group-multilingual>`  | `^`                                    | Group tagged attachments as 'multipart/multilingual' |                                   |
| `<group-related>`       | `%`                                    | Group tagged attachments as 'multipart/related'      |                                   |
| `<move-down>`           | `+`                                    | Move an attachment down in the attachment list       |                                   |
| `<move-up>`             | `-`                                    | Move an attachment up in the attachment list         |                                   |
| `<new-mime>`            | `n`                                    | Compose new attachment using mailcap entry           |                                   |
| `<pipe-message>`        | `\|`                                   | Pipe message/attachment to a shell command           |                                   |
| `<print-entry>`         | `l`                                    | Print the current entry                              |                                   |
| `<rename-attachment>`   | `^O`                                   | Send attachment with a different name                |                                   |
| `<tag-entry>`           | `T`                                    | Tag the current entry                                | [{bdg-info}`generic`](fn-generic) |
| `<toggle-disposition>`  | `^D`                                   | Toggle disposition between inline/attachment         |                                   |
| `<toggle-recode>`       |                                        | Toggle recoding of this attachment                   |                                   |
| `<toggle-unlink>`       | `u`                                    | Toggle whether to delete file after sending it       |                                   |
| `<ungroup-attachment>`  | `#`                                    | Ungroup 'multipart' attachment                       |                                   |
| `<update-encoding>`     | `U`                                    | Update an attachment's encoding info                 |                                   |
| `<view-attach>`         | `<Enter>`, `<Return>`, `<KeypadEnter>` | View attachment using mailcap entry if necessary     |                                   |
| `<view-mailcap>`        |                                        | Force viewing of attachment using mailcap            |                                   |
| `<view-pager>`          |                                        | View attachment in pager using copiousoutput mailcap |                                   |
| `<view-text>`           |                                        | View attachment as text                              |                                   |

## Compose Functions

| Function                | Default Keys | Description                                | Inherited From |
|-------------------------|--------------|--------------------------------------------|----------------|
| `<display-toggle-weed>` | `h`          | Display message and toggle header weeding  |                |
| `<edit-file>`           | `Esc e`      | Edit the file to be attached               |                |
| `<edit-headers>`        | `E`          | Edit the message with headers              |                |
| `<edit-message>`        | `e`          | Edit the message                           |                |
| `<exit>`                | `q`          | Exit this menu                             |                |
| `<forget-passphrase>`   | `^F`         | Wipe passphrases from memory               |                |
| `<ispell>`              | `i`          | Run `ispell` on the message                |                |
| `<pipe-entry>`          |              | Pipe message/attachment to a shell command |                |
| `<postpone-message>`    | `P`          | Save this message to send later            |                |
| `<rename-file>`         | `R`          | Rename/move an attached file               |                |
| `<send-message>`        | `y`          | Send the message                           |                |
| `<write-fcc>`           | `w`          | Write the message to a folder              |                |

## Envelope Functions

| Function              | Default Keys | Description                                    | Inherited From |
|-----------------------|--------------|------------------------------------------------|----------------|
| `<autocrypt-menu>`    | `o`          | Show autocrypt compose menu options            |                |
| `<edit-bcc>`          | `b`          | Edit the `Bcc:` list                           |                |
| `<edit-cc>`           | `c`          | Edit the `Cc:` list                            |                |
| `<edit-fcc>`          | `f`          | Enter a file to save a copy of this message in |                |
| `<edit-followup-to>`  |              | Edit the `Followup-to:` field                  |                |
| `<edit-from>`         | `Esc f`      | Edit the `From:` field                         |                |
| `<edit-newsgroups>`   |              | Edit the newsgroups list                       |                |
| `<edit-reply-to>`     | `r`          | Edit the `Reply-to:` field                     |                |
| `<edit-subject>`      | `s`          | Edit the `Subject:` of this message            |                |
| `<edit-to>`           | `t`          | Edit the `To:` list                            |                |
| `<edit-x-comment-to>` |              | Edit the `X-comment-to:` field                 |                |
| `<pgp-menu>`          | `p`          | Show PGP options                               |                |
| `<smime-menu>`        | `S`          | Show S/MIME options                            |                |

## Preview Functions

| Function              | Default Keys | Description                           | Inherited From |
|-----------------------|--------------|---------------------------------------|----------------|
| `<preview-page-down>` | `<PageDown>` | Show the next page of the message     |                |
| `<preview-page-up>`   | `<PageUp>`   | Show the previous page of the message |                |

