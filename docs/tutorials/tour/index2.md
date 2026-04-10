---
title: Index Dialog
description: The main NeoMutt mailbox view for browsing, sorting, tagging, and opening messages.
keywords: index, mailbox, message list, threads, sort, tags, limit, reply, pager
---

(tour-index)=
# Index Dialog

## Introduction -- Where am I?

The Index Dialog is NeoMutt's home screen: the mailbox view where you browse messages one line at a time.
It is also called the message index, the mailbox index, or simply "the index".
Most workflows start here, and most of the other dialogs eventually return here.

```{include} ../../_screenshots/index.html
```

## What am I looking at?

- The main panel is the message list, with one row per message showing date, flags, author, subject, thread tree, and size.
- The highlighted row is the current message; threaded mailboxes use the tree glyphs to show parent and child relationships.
- The status line summarizes the current mailbox, message counts, sort mode, and your position in the list.
- Depending on your setup, the [Sidebar Panel](sidebar.md) may appear beside the index and the [Pager Dialog](pager.md) may be embedded below it.
- Temporary prompts, search input, and status messages appear in the [Message Window](message.md).

## What can I do?

- Open the current message in the [Pager Dialog](pager.md) with `<display-message>`.
- Compose new mail or respond to existing mail with `<mail>`, `<reply>`, `<group-reply>`, `<list-reply>`, `<forward-message>`, `<bounce-message>`, and `<compose-to-sender>`.
- Organize mail by deleting, undeleting, saving, copying, piping, printing, labeling, tagging, and syncing messages.
- Change the view by limiting, searching, sorting, threading, collapsing threads, and jumping between unread or tagged mail.
- Open related tools such as the [Attach Dialog](attach.md), [Query Dialog](query.md), [Autocrypt Dialog](autocrypt.md), help pages, and the command line.
- Full reference: [Index Functions](menu-index), [Generic Functions](menu-generic), [Sidebar Functions](menu-sidebar).

## Where can I go next?

- `<display-message>` opens the [Pager Dialog](pager.md).
- `<mail>`, `<reply>`, `<group-reply>`, `<list-reply>`, `<forward-message>`, `<bounce-message>`, and `<compose-to-sender>` open the [Compose Dialog](compose.md).
- `<recall-message>` resumes a draft; if there is more than one postponed draft, NeoMutt shows the [Postpone Dialog](postpone.md) first.
- `<change-folder>` can open the [Browser Dialog](browser.md) when you ask for mailbox browsing with {kbd}`?`.
- `<view-attachments>` opens the [Attach Dialog](attach.md).
- `<query>` opens the [Query Dialog](query.md).
- `<autocrypt-acct-menu>` opens the [Autocrypt Dialog](autocrypt.md).
- {kbd}`?`, `<show-log-messages>`, `:set`, `:bind`, `:macro`, `:version`, and `:color` open the [Simple Pagers](simple.md).
- {kbd}`:`, {kbd}`/`, and {kbd}`l` use the [Message Window](message.md).
- TLS or certificate problems may interrupt the flow with the [Certificate Dialog](certificate.md).

## Where did I come from?

- Normal startup usually lands here directly.
- Selecting a mailbox in the [Browser Dialog](browser.md) opens the index for that mailbox.
- Quitting the [Pager Dialog](pager.md) returns to the index.
- Sending, postponing, or aborting in the [Compose Dialog](compose.md) returns here.
- Exiting the [Attach Dialog](attach.md), [Query Dialog](query.md), [Autocrypt Dialog](autocrypt.md), or other short-lived dialogs usually brings you back here.
- Accepting or rejecting a certificate normally returns to the operation that was trying to show, sync, or open this mailbox.

## How do I configure this?

- Start with [Index Config](ref-cfg-index), [General Config](ref-cfg-general), and [Sidebar Config](ref-cfg-sidebar).
- Common options include [`$index_format`](cfg-index-format), [`$status_format`](cfg-status-format), [`$sort`](cfg-sort), [`$sort_aux`](cfg-sort-aux), [`$use_threads`](cfg-use-threads), [`$collapse_all`](cfg-collapse-all), [`$hide_thread_subject`](cfg-hide-thread-subject), and [`$resolve`](cfg-resolve).
- Mailbox lists and labels are shaped by [`:mailboxes`](cmd-mailboxes), [`:named-mailboxes`](cmd-named-mailboxes), and [`:index-format-hook`](cmd-index-format-hook).
- Colours come from [Colour Objects](ref-colors), especially `index`, `index_author`, `index_date`, `index_flags`, `index_subject`, `index_size`, `index_label`, `tree`, `indicator`, and `status`.
