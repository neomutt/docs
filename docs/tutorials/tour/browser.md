---
title: Browser Dialog
description: The file and mailbox browser used to choose folders, files, and remote mailboxes in NeoMutt.
keywords: browser, file chooser, mailbox browser, imap browser, folder, mask, subscribe
---

(tour-browser)=
# Browser Dialog

## Introduction -- Where am I?

The Browser Dialog is NeoMutt's file and mailbox chooser.
It appears whenever NeoMutt needs you to pick a mailbox, a folder on disk, or a file to attach, save, or inspect.
Depending on the context, it behaves like a local file browser, an IMAP folder browser, or an NNTP/remote mailbox list.

```{include} ../../_screenshots/browser-dialog.html
```

## What am I looking at?

- The main list shows files, directories, or mailboxes, along with metadata such as permissions, owner, size, and modification date where available.
- The highlighted row is the entry that will be opened, attached, or selected.
- The status line shows the current directory or mailbox root and the active file mask.
- On IMAP or NNTP backends, the list represents remote mailboxes rather than local files.
- Prompts for masks, paths, and completion come through the [Message Window](message.md).

## What can I do?

- Move through directories, descend into the current directory, and go back to the parent.
- Filter the listing with a file mask, switch between mailbox-only and all-file views, and sort the results.
- Open the selected mailbox or choose the selected file for the calling action.
- Subscribe, unsubscribe, create, rename, or delete remote mailboxes where the backend supports it.
- Inspect the currently selected path before choosing it.
- Full reference: [Browser Functions](menu-browser), [Generic Functions](menu-generic).

## Where can I go next?

- Selecting a mailbox opens the [Index Dialog](index2.md).
- Selecting a file returns to the caller, such as the [Compose Dialog](compose.md) for attachments or the [Attach Dialog](attach.md) for saving.
- {kbd}`q` cancels and returns to the dialog or prompt that opened the browser.
- Prompts that feed the browser continue in the [Message Window](message.md).

## Where did I come from?

- Startup with `-y` or `-G` can bring you here first.
- The [Index Dialog](index2.md) opens the browser when you change folders and ask for browsing.
- The [Compose Dialog](compose.md) opens it when choosing files to attach or an Fcc folder.
- Any filename or mailbox prompt can drop into the browser when you press {kbd}`?` or trigger completion.

## How do I configure this?

- Start with [Browser Config](ref-cfg-browser), [Conn Options](ref-cfg-conn), and [General Config](ref-cfg-general).
- Common options include [`$browser_sort`](cfg-browser-sort), [`$browser_sort_dirs_first`](cfg-browser-sort-dirs-first), [`$folder_format`](cfg-folder-format), [`$mailbox_folder_format`](cfg-mailbox-folder-format), [`$mask`](cfg-mask), [`$show_only_unread`](cfg-show-only-unread), and [`$folder`](cfg-folder).
- Useful commands include [`:cd`](cmd-cd), [`:mailboxes`](cmd-mailboxes), [`:named-mailboxes`](cmd-named-mailboxes), [`:subscribe-to`](cmd-subscribe-to), and [`:unsubscribe-from`](cmd-unsubscribe-from).
- Colours come from [Colour Objects](ref-colors), especially `indicator`, `status`, `message`, `warning`, and `normal`.
