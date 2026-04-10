---
title: Postpone Dialog
description: The draft picker used when recalling postponed messages in NeoMutt.
keywords: postpone, drafts, recall, postponed mailbox, resume compose
---

(tour-postpone)=
# Postpone Dialog

## Introduction -- Where am I?

The Postpone Dialog appears when you recall a postponed message and there is more than one saved draft to choose from.
It lets you browse the postponed mailbox, find the right draft, and reopen it for editing.
You can think of it as NeoMutt's draft picker.

```{include} ../../_screenshots/postpone-dialog.html
```

## What am I looking at?

- Each line is a postponed draft, shown with familiar index-style fields such as date, flags, recipient, subject, and size.
- The highlighted row is the draft that will be resumed or deleted.
- The status line identifies the postponed mailbox.

## What can I do?

- Select a postponed draft and reopen it for editing.
- Delete or undelete drafts you no longer want.
- Use the list as a quick overview of which drafts are waiting to be finished.
- Full reference: [Postpone Functions](menu-postpone), [Generic Functions](menu-generic).

## Where can I go next?

- Selecting a draft opens the [Compose Dialog](compose.md).
- Cancelling returns you to the [Index Dialog](index2.md) or [Pager Dialog](pager.md) that initiated recall.

## Where did I come from?

- You arrive from the [Index Dialog](index2.md) or [Pager Dialog](pager.md) after `<recall-message>` when NeoMutt finds multiple postponed drafts.
- If there is only one postponed draft, NeoMutt usually skips this dialog and goes straight to [Compose Dialog](compose.md).

## How do I configure this?

- Start with [Compose Config](ref-cfg-compose), [Send Config](ref-cfg-send), and [General Config](ref-cfg-general).
- Common options include [`$postpone`](cfg-postpone), [`$postponed`](cfg-postponed), [`$recall`](cfg-recall), [`$postpone_encrypt`](cfg-postpone-encrypt), and [`$postpone_encrypt_as`](cfg-postpone-encrypt-as).
- Draft handling is usually tuned through generic configuration commands such as [`:set`](cmd-set), along with hooks such as [`:fcc-hook`](cmd-fcc-hook) when you care about saved copies.
- Colours come from [Colour Objects](ref-colors), especially `index`, `index_date`, `index_flags`, `index_author`, `index_subject`, `index_size`, `indicator`, and `status`.
