---
title: Compose Functions
description: Key bindings and functions for editing recipients, attachments, encryption, and sending email in the NeoMutt compose screen
keywords: neomutt, functions, compose, menu, bindings, keys, writing email, message editor, send-message, attach-file, edit-to, edit-subject, pgp-menu, smime-menu, postpone-message, attachments
---

(menu-compose)=
# Compose Functions

Prepare an email before sending it.
You can edit recipients, subject, and headers, attach files, configure encryption, and send or postpone the message.

## Attach Functions

| Function                | Default Keys                                          | Description                                          | Inherited From                      |
|-------------------------|-------------------------------------------------------|------------------------------------------------------|-------------------------------------|
| `<attach-file>`         | {kbd}`a`                                              | Attach files to this message                         |                                     |
| `<attach-key>`          | {kbd}`Alt-k`                                          | Attach a PGP public key                              |                                     |
| `<attach-message>`      | {kbd}`A`                                              | Attach messages to this message                      |                                     |
| `<attach-news-message>` |                                                       | Attach news articles to this message                 |                                     |
| `<copy-file>`           | {kbd}`C`                                              | Save message/attachment to a mailbox/file            |                                     |
| `<detach-file>`         | {kbd}`D`                                              | Delete the current entry                             |                                     |
| `<edit-content-id>`     | {kbd}`Alt-i`                                          | Edit the `Content-ID` of the attachment              |                                     |
| `<edit-description>`    | {kbd}`d`                                              | Edit attachment description                          |                                     |
| `<edit-encoding>`       | {kbd}`Ctrl-E`                                         | Edit attachment transfer-encoding                    |                                     |
| `<edit-language>`       | {kbd}`Ctrl-L`                                         | Edit the `Content-Language` of the attachment        |                                     |
| `<edit-mime>`           | {kbd}`m`                                              | Edit attachment using mailcap entry                  |                                     |
| `<edit-type>`           | {kbd}`Ctrl-T`                                         | Edit attachment content type                         |                                     |
| `<filter-entry>`        | {kbd}`F`                                              | Filter attachment through a shell command            |                                     |
| `<get-attachment>`      | {kbd}`G`                                              | Get a temporary copy of an attachment                |                                     |
| `<group-alternatives>`  | {kbd}`&`                                              | Group tagged attachments as 'multipart/alternative'  |                                     |
| `<group-multilingual>`  | {kbd}`^`                                              | Group tagged attachments as 'multipart/multilingual' |                                     |
| `<group-related>`       | {kbd}`%`                                              | Group tagged attachments as 'multipart/related'      |                                     |
| `<move-down>`           | {kbd}`+`                                              | Move an attachment down in the attachment list       |                                     |
| `<move-up>`             | {kbd}`-`                                              | Move an attachment up in the attachment list         |                                     |
| `<new-mime>`            | {kbd}`n`                                              | Compose new attachment using mailcap entry           |                                     |
| `<pipe-message>`        | {kbd}`\|`                                             | Pipe message/attachment to a shell command           |                                     |
| `<print-entry>`         | {kbd}`l`                                              | Print the current entry                              |                                     |
| `<rename-attachment>`   | {kbd}`Ctrl-O`                                         | Send attachment with a different name                |                                     |
| `<tag-entry>`           | {kbd}`T`                                              | Tag the current entry                                | [{bdg-info}`generic`](menu-generic) |
| `<toggle-disposition>`  | {kbd}`Ctrl-D`                                         | Toggle disposition between inline/attachment         |                                     |
| `<toggle-recode>`       |                                                       | Toggle recoding of this attachment                   |                                     |
| `<toggle-unlink>`       | {kbd}`u`                                              | Toggle whether to delete file after sending it       |                                     |
| `<ungroup-attachment>`  | {kbd}`#`                                              | Ungroup 'multipart' attachment                       |                                     |
| `<update-encoding>`     | {kbd}`U`                                              | Update an attachment's encoding info                 |                                     |
| `<view-attach>`         | {kbd}`<Enter>`, {kbd}`<Return>`, {kbd}`<KeypadEnter>` | View attachment using mailcap entry if necessary     |                                     |
| `<view-mailcap>`        |                                                       | Force viewing of attachment using mailcap            |                                     |
| `<view-pager>`          |                                                       | View attachment in pager using copiousoutput mailcap |                                     |
| `<view-text>`           |                                                       | View attachment as text                              |                                     |

## Compose Functions

| Function                | Default Keys  | Description                                | Inherited From |
|-------------------------|---------------|--------------------------------------------|----------------|
| `<display-toggle-weed>` | {kbd}`h`      | Display message and toggle header weeding  |                |
| `<edit-file>`           | {kbd}`Alt-e`  | Edit the file to be attached               |                |
| `<edit-headers>`        | {kbd}`E`      | Edit the message with headers              |                |
| `<edit-message>`        | {kbd}`e`      | Edit the message                           |                |
| `<exit>`                | {kbd}`q`      | Exit this menu                             |                |
| `<forget-passphrase>`   | {kbd}`Ctrl-F` | Wipe passphrases from memory               |                |
| `<ispell>`              | {kbd}`i`      | Run `ispell` on the message                |                |
| `<pipe-entry>`          |               | Pipe message/attachment to a shell command |                |
| `<postpone-message>`    | {kbd}`P`      | Save this message to send later            |                |
| `<rename-file>`         | {kbd}`R`      | Rename/move an attached file               |                |
| `<send-message>`        | {kbd}`y`      | Send the message                           |                |
| `<write-fcc>`           | {kbd}`w`      | Write the message to a folder              |                |

## Envelope Functions

| Function              | Default Keys | Description                                    | Inherited From |
|-----------------------|--------------|------------------------------------------------|----------------|
| `<autocrypt-menu>`    | {kbd}`o`     | Show autocrypt compose menu options            |                |
| `<edit-bcc>`          | {kbd}`b`     | Edit the `Bcc:` list                           |                |
| `<edit-cc>`           | {kbd}`c`     | Edit the `Cc:` list                            |                |
| `<edit-fcc>`          | {kbd}`f`     | Enter a file to save a copy of this message in |                |
| `<edit-followup-to>`  |              | Edit the `Followup-to:` field                  |                |
| `<edit-from>`         | {kbd}`Alt-f` | Edit the `From:` field                         |                |
| `<edit-newsgroups>`   |              | Edit the newsgroups list                       |                |
| `<edit-reply-to>`     | {kbd}`r`     | Edit the `Reply-to:` field                     |                |
| `<edit-subject>`      | {kbd}`s`     | Edit the `Subject:` of this message            |                |
| `<edit-to>`           | {kbd}`t`     | Edit the `To:` list                            |                |
| `<edit-x-comment-to>` |              | Edit the `X-comment-to:` field                 |                |
| `<pgp-menu>`          | {kbd}`p`     | Show PGP options                               |                |
| `<smime-menu>`        | {kbd}`S`     | Show S/MIME options                            |                |

## Preview Functions

| Function              | Default Keys      | Description                           | Inherited From |
|-----------------------|-------------------|---------------------------------------|----------------|
| `<preview-page-down>` | {kbd}`<PageDown>` | Show the next page of the message     |                |
| `<preview-page-up>`   | {kbd}`<PageUp>`   | Show the previous page of the message |                |

