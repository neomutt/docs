---
title: Alias Dialog
description: NeoMutt's personal address book view for browsing, selecting, and mailing saved aliases.
keywords: alias, address book, contacts, compose, recipient completion, groups
---

(tour-alias)=
# Alias Dialog

## Introduction -- Where am I?

The Alias Dialog is NeoMutt's built-in address book.
It lists the aliases you have defined in your configuration and lets you choose one or more recipients when addressing a message.
You may also hear it described as the alias menu or contact list.

```{include} ../../_screenshots/alias-dialog.html
```

## What am I looking at?

- The main list shows each alias key, the expanded real name and address, and any tags or groups.
- The highlighted row is the alias that will be inserted or acted on.
- The status line shows the current limit or sort state.
- The prompt line at the bottom reminds you which field is currently being completed.

## What can I do?

- Select one or more aliases to insert into a `To:`, `Cc:`, or `Bcc:` field.
- Compose a new message directly to the currently selected alias with `<mail>`.
- Limit, sort, tag, delete, and undelete alias entries while you browse.
- Use the dialog as a quick way to inspect how an alias expands before sending mail.
- Full reference: [Alias Functions](menu-alias), [Generic Functions](menu-generic).

## Where can I go next?

- Selecting entries usually returns you to the [Compose Dialog](compose.md) or the [Message Window](message.md) prompt that asked for recipients.
- `<mail>` opens the [Compose Dialog](compose.md) directly.
- {kbd}`q` cancels and returns to the caller without inserting anything.

## Where did I come from?

- Address completion in the [Message Window](message.md) can open this dialog when NeoMutt finds multiple alias matches.
- Editing recipient fields in the [Compose Dialog](compose.md) can lead here through completion.
- Some setups also bind `<alias-dialog>` from the [Index Dialog](index2.md) so you can browse aliases explicitly.

## How do I configure this?

- Start with [Alias Config](ref-cfg-alias).
- Common options include [`$alias_file`](cfg-alias-file), [`$alias_format`](cfg-alias-format), and [`$alias_sort`](cfg-alias-sort).
- Alias data is maintained with [`:alias`](cmd-alias), [`:unalias`](cmd-unalias), [`:group`](cmd-group), [`:ungroup`](cmd-ungroup), [`:alternates`](cmd-alternates), and [`:unalternates`](cmd-unalternates).
- Colours come from [Colour Objects](ref-colors), especially `indicator`, `status`, `prompt`, `message`, and `normal`.
