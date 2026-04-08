---
title: Attach Dialog
description: The attachment browser for viewing, saving, printing, and extracting parts from a message.
keywords: attachments, mime, save, view, mailcap, extract keys, reply
---

(tour-attach)=
# Attach Dialog

## Introduction -- Where am I?

The Attach Dialog is NeoMutt's MIME part browser.
It lists the attachments and multipart structure of the current message so you can inspect, save, view, print, or pipe individual parts.
It is sometimes called the attachment menu or attachment tree.

<div class="term-window">
<div class="term-title">Attach Dialog</div>
<pre class="terminal">
<span>  I     1 &lt;no description&gt;                                               [multipa/mixed, 7bit, 14K] </span>
<span>  I     2 </span><span class="tree">├─&gt;</span><span>&lt;no description&gt;                                    [text/plain, 7bit, us-ascii, 0.7K] </span>
<span>  A     3 </span><span class="tree">├─&gt;</span><span>misc.md                                          [text/markdown, 7bit, us-ascii, 0.3K] </span>
<span>  A     4 </span><span class="tree">├─&gt;</span><span>welcome.md                                       [text/markdown, 7bit, us-ascii, 1.0K] </span>
<span>  A     5 </span><span class="tree">├─&gt;</span><span>goals.md                                         [text/markdown, 7bit, us-ascii, 1.9K] </span>
<span>  A     6 </span><span class="tree">├─&gt;</span><span>plurals.md                                        [text/markdown, quoted, utf-8, 2.2K] </span>
<span>  A     7 </span><span class="tree">├─&gt;</span><span>coordinating.md                                [text/markdown, quoted, us-ascii, 1.2K] </span>
<span>  A     8 </span><span class="tree">├─&gt;</span><span>power-editing.md                                 [text/markdown, 7bit, us-ascii, 2.0K] </span>
<span>  A     9 </span><span class="tree">└─&gt;</span><span>manager.txt                                          [text/plain, quoted, utf-8, 4.6K] </span>
<span>                                                                                                    </span>
<span class="status">Attachments                                                                                         </span>
<span>                                                                                                    </span>
</pre>
</div>

## What am I looking at?

- The main list shows one MIME part per row, including nesting, flags, filename, content type, encoding, character set, and size.
- Tree characters show the structure of multipart messages, so you can tell which parts belong together.
- The highlighted row is the attachment or MIME container NeoMutt will act on.
- The status line identifies the dialog and keeps orientation while you move through a complex message.

## What can I do?

- View an attachment with the internal pager, as plain text, or through a mailcap viewer.
- Save or print the selected part, or pipe it to an external command.
- Reply, forward, group-reply, or bounce while staying focused on the current message's attachments.
- Extract supported public keys from a message and inspect encrypted or signed content.
- Collapse multipart branches to simplify very large attachment trees.
- Full reference: [Attach Functions](menu-attach), [Generic Functions](menu-generic).

## Where can I go next?

- `q` returns to the [Index Dialog](index2.md) or [Pager Dialog](pager.md) that opened the attachment tree.
- Viewing text or copious-output attachments can open one of the [Simple Pagers](simple.md).
- Replying or forwarding opens the [Compose Dialog](compose.md).
- Saving or piping an attachment may briefly use the [Browser Dialog](browser.md) or the [Message Window](message.md) for filenames and commands.

## Where did I come from?

- You usually arrive from the [Index Dialog](index2.md) or [Pager Dialog](pager.md) via `<view-attachments>`.
- The current message context comes with you, so all actions still refer to the message you were reading.

## How do I configure this?

- Start with [Attach Config](ref-cfg-attach), [Send Config](ref-cfg-send), and [MIME Commands](../../reference/commands/mime.md).
- Common options include [`$attach_save_dir`](cfg-attach-save-dir), [`$attach_save_without_prompting`](cfg-attach-save-without-prompting), [`$attach_sep`](cfg-attach-sep), [`$attach_split`](cfg-attach-split), [`$message_format`](cfg-message-format), [`$mime_forward`](cfg-mime-forward), and [`$mime_forward_rest`](cfg-mime-forward-rest).
- Useful commands include [`:attachments`](cmd-attachments), [`:unattachments`](cmd-unattachments), [`:auto-view`](cmd-auto-view), [`:unauto-view`](cmd-unauto-view), [`:alternative-order`](cmd-alternative-order), and [`:mime-lookup`](cmd-mime-lookup).
- Colours come from [Colour Objects](ref-colors), especially `attachment`, `tree`, `indicator`, `status`, and `message`.

