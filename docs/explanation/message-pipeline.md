---
title: About the Message Processing Pipeline
description: How NeoMutt's pipeline fetches messages from mailbox backends, parses MIME structures, converts charsets, processes headers, and renders in the index and pager
keywords: neomutt, message pipeline, fetching, parsing, mime, charset conversion, header processing, indexing, threading, pager, index, mailbox backends, imap, maildir, display filtering
---

# About the Message Processing Pipeline

NeoMutt's message pipeline is designed for reliability and speed.
It separates fetching, parsing, indexing, and display so each stage can be tuned or replaced without breaking the others.

## From Mailbox to Screen: The Big Picture

When you open a mailbox, NeoMutt reads message metadata, builds an index view, and only parses message bodies when they are displayed.
This keeps navigation fast, even in large mailboxes.
The index and pager are separate views over the same underlying message data, which is why the UI can show message lists and full content without duplicating work.

## Fetching Messages from Backends

Mailbox backends are responsible for retrieving message data.
Local backends read mbox, Maildir, or MH directly from disk, while remote backends (IMAP, POP3, NNTP) fetch message data over the network.
The backend choice affects how quickly new mail appears and what metadata is available for searching.
See [Mailbox Formats](../howto/mailbox-formats) and [IMAP](../howto/imap).

## MIME Parsing and Multipart Handling

Once a message is opened in the pager, NeoMutt parses its MIME structure.
This is how attachments, multipart alternatives, and embedded messages are represented.
The parser decides which parts are rendered inline and which are shown as attachments, with mailcap and MIME configuration controlling the final behavior.
See [MIME](mime) and [MIME Types](../reference/mime-types).

## Character Set Conversion

Messages can use many character sets, and NeoMutt converts them to match your locale.
This is why incorrect terminal encoding can cause unreadable output.
Charset handling is a first-class part of the pipeline because it affects both headers and body content.
See [Charsets](charsets).

## Header Processing and Display Filtering

Headers are parsed early and displayed in the pager, but what you see depends on header weeding, ordering, and custom headers.
This keeps the display focused while still preserving full RFC compliance under the hood.
See [How to Customise Header Display](../howto/header-display).

## The Indexing and Threading Pipeline

The index view is built from message headers and flags.
Threading groups related messages so you can navigate conversations instead of individual messages.
Threading is optional and configurable, and the index can be customized heavily with format strings and patterns.
See [Threading](threading).

## How the Index and Pager Interact

The index and pager are tightly linked.
The pager shows one message, while the index provides context, threading, and message state.
Actions in one view update the other, which is why tag, delete, and read flags appear consistently across the UI.
The separation keeps the UI responsive and makes it possible to use external tools (mailcap, filters) without blocking the index.
