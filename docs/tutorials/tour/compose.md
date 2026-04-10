---
title: Compose Dialog
description: NeoMutt's compose screen for editing recipients, attachments, crypto settings, and sending mail.
keywords: compose, send menu, envelope, attachments, draft, postpone, pgp, smime, autocrypt
---

(tour-compose)=
# Compose Dialog

## Introduction -- Where am I?

The Compose Dialog is NeoMutt's send menu: the final review and editing screen before a message is sent.
It is where you adjust the envelope, manage attachments, check security settings, and decide whether to send, postpone, or abandon the draft.
You reach it for new mail, replies, forwards, bounces, and recalled drafts.

```{include} _screenshot-compose.html
```

## What am I looking at?

- The help and status text at the top reminds you of the most common compose actions.
- The envelope section holds the message headers such as `From:`, `To:`, `Cc:`, `Bcc:`, `Subject:`, `Reply-To:`, and `Fcc:`.
- The security lines show whether the draft will be signed, encrypted, both, or neither, and which key or certificate will be used.
- The attachments panel lists every attachment, including the message body file, with MIME type, encoding, and size.
- The preview panel shows the current message body so you can review the draft before sending.

## What can I do?

- Edit recipients, sender, subject, reply headers, followup headers, and the Fcc mailbox.
- Edit the message body, invoke an external editor, run spell-checking, or edit the draft with headers.
- Attach files, messages, and keys; reorder attachments; rename or re-encode them; and group them into multipart structures.
- Choose PGP, S/MIME, or Autocrypt options before sending.
- Send now, postpone for later, write a copy to a folder, or quit without sending.
- Full reference: [Compose Functions](menu-compose), [Generic Functions](menu-generic), [Editor Functions](menu-editor).

## Where can I go next?

- `<send-message>`, `<postpone-message>`, and quitting the menu return you to the [Index Dialog](index2.md) after the draft is handled.
- `<attach-file>` and `<edit-fcc>` can open the [Browser Dialog](browser.md) when you ask for browsing with {kbd}`?`.
- `<attach-message>` opens a nested [Index Dialog](index2.md) so you can choose messages to attach.
- Sending encrypted mail may open the [PGP Dialog](pgp.md), [GPGME Dialog](gpgme.md), or [S/MIME Dialog](smime.md).
- Field editing and crypto choice prompts use the [Message Window](message.md).
- Viewing an attachment from the compose menu can open one of the [Simple Pagers](simple.md).

## Where did I come from?

- The [Index Dialog](index2.md) and [Pager Dialog](pager.md) open compose for new mail, replies, forwards, bounces, and resend-style actions.
- The [Postpone Dialog](postpone.md) sends you here when you resume a saved draft.
- Command-line compose-only mode can start directly in this dialog.
- After your external editor exits, NeoMutt returns here for the final review.

## How do I configure this?

- Start with [Compose Config](ref-cfg-compose), [Send Config](ref-cfg-send), and [Encryption Config](ref-cfg-ncrypt).
- Common options include [`$compose_format`](cfg-compose-format), [`$edit_headers`](cfg-edit-headers), [`$editor`](cfg-editor), [`$fast_reply`](cfg-fast-reply), [`$record`](cfg-record), [`$postponed`](cfg-postponed), [`$crypt_auto_encrypt`](cfg-crypt-auto-encrypt), [`$crypt_auto_sign`](cfg-crypt-auto-sign), and [`$abort_noattach`](cfg-abort-noattach).
- Common commands include [`:my-header`](cmd-my-header), [`:send-hook`](cmd-send-hook), [`:reply-hook`](cmd-reply-hook), [`:fcc-hook`](cmd-fcc-hook), and [`:crypt-hook`](cmd-crypt-hook).
- Colours come from [Colour Objects](ref-colors), especially `compose_header`, `compose_security_encrypt`, `compose_security_sign`, `compose_security_both`, `compose_security_none`, `attachment`, `tree`, `indicator`, and `status`.
