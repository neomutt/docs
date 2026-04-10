---
title: Pattern Dialog
description: The pattern helper that lists NeoMutt's search and limit operators for quick insertion at prompts.
keywords: pattern, search syntax, limit, filter, query helper, message patterns
---

(tour-pattern)=
# Pattern Dialog

## Introduction -- Where am I?

The Pattern Dialog is NeoMutt's built-in pattern cheat sheet and inserter.
It appears while you are building a search, limit, tag, delete-pattern, or other pattern-based command and want help with the available pattern operators.
Instead of memorising every `~x` code, you can browse and insert the right one from here.

```{include} ../../_screenshots/pattern-dialog.html
```

## What am I looking at?

- Each row shows a pattern number, the pattern expression, and a human-readable description.
- The highlighted row is the pattern that will be inserted into the active prompt.
- The status line identifies the dialog as a patterns reference.
- The prompt line below shows the live pattern you are building in the caller.

## What can I do?

- Browse the full list of available pattern operators and their meanings.
- Insert a pattern fragment into the active prompt.
- Search through the list if you remember part of a description but not the exact code.
- Use it as a learning aid while you build more complex searches and limits.
- Full reference: [Pattern Syntax](ref-patterns), [Dialog Functions](menu-dialog), [Generic Functions](menu-generic).

## Where can I go next?

- Selecting an entry returns you to the prompt in the [Message Window](message.md) with the chosen pattern inserted.
- Cancelling returns you to the same prompt without changing it.

## Where did I come from?

- Pattern-aware prompts in the [Index Dialog](index2.md), [Alias Dialog](alias.md), and [Query Dialog](query.md) can open this helper.
- You commonly reach it while entering limits, tag patterns, delete patterns, score patterns, or search expressions.

## How do I configure this?

- Start with [Pattern Options](ref-cfg-pattern) and [Pattern Syntax](ref-patterns).
- Common options include [`$pattern_format`](cfg-pattern-format), [`$simple_search`](cfg-simple-search), [`$external_search_command`](cfg-external-search-command), and [`$thorough_search`](cfg-thorough-search).
- Pattern-driven workflows often combine with commands such as [`:score`](cmd-score), [`:unscore`](cmd-unscore), [`:color`](cmd-color), [`:mailboxes`](cmd-mailboxes), and the hook commands in [Commands](ref-commands).
- Colours come from [Colour Objects](ref-colors), especially `indicator`, `status`, `prompt`, `search`, and `message`.
