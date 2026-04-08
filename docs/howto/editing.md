---
title: Edit Input Fields
description: Use NeoMutt's built-in line editor for prompts, with Emacs-style keys, tab completion, and persistent history
keywords: editor, line editor, emacs, keybindings, completion, history, input, editing, tab completion, history_file, save_history, kill-line, bind editor, external editor, word case
---

# Edit Input Fields

## Overview

NeoMutt has a built-in line editor for inputting text wherever you type at a prompt — for example, email addresses in header fields, filenames, search patterns, and command lines.
The key bindings follow Emacs conventions.

## Key Bindings

### Movement

| Key               | Function          | Description                   |
|-------------------|-------------------|-------------------------------|
| {kbd}`^A` or {kbd}`Home`  | [`<bol>`](fn-bol)           | Move to the start of the line |
| {kbd}`^E` or {kbd}`End`   | [`<eol>`](fn-eol)           | Move to the end of the line   |
| {kbd}`^B` or {kbd}`Left`  | [`<backward-char>`](fn-backward-char) | Move back one character       |
| {kbd}`^F` or {kbd}`Right` | [`<forward-char>`](fn-forward-char)  | Move forward one character    |
| {kbd}`Esc B`      | [`<backward-word>`](fn-backward-word) | Move back one word            |
| {kbd}`Esc F`      | [`<forward-word>`](fn-forward-word)  | Move forward one word         |

### Deletion

| Key                | Function        | Description                            |
|--------------------|-----------------|----------------------------------------|
| {kbd}`^D` or {kbd}`Delete` | [`<delete-char>`](fn-delete-char) | Delete the character under the cursor  |
| {kbd}`Backspace`      | [`<backspace>`](fn-backspace) | Delete the character before the cursor |
| {kbd}`^K`               | [`<kill-eol>`](fn-kill-eol)    | Delete to the end of the line          |
| {kbd}`^U`               | [`<kill-line>`](fn-kill-line)   | Delete the entire line                 |
| {kbd}`^W`               | [`<kill-word>`](fn-kill-word)   | Delete the word before the cursor      |
| {kbd}`Esc d`       | [`<kill-eow>`](fn-kill-eow)    | Delete to the end of the word          |

### Word Case

| Key     | Function            | Description                |
|---------|---------------------|----------------------------|
| {kbd}`Esc u` | [`<upcase-word>`](fn-upcase-word)     | Convert word to upper case |
| {kbd}`Esc l` | [`<downcase-word>`](fn-downcase-word)   | Convert word to lower case |
| {kbd}`Esc c` | [`<capitalize-word>`](fn-capitalize-word) | Capitalize the word        |

### Miscellaneous

| Key        | Function       | Description                        |
|------------|----------------|------------------------------------|
| {kbd}`^V`       | [`<quote-char>`](fn-quote-char) | Quote (escape) the next typed key  |
| {kbd}`^G`       | n/a            | Abort the current prompt or action |
| {kbd}`Return` | n/a            | Confirm / finish editing           |

## Tab Completion

Press {kbd}`<Tab>` to trigger completion.
What gets completed depends on context:

- **Filenames** — completes paths in the filesystem
- **Aliases** — completes known address aliases
- **Labels** — completes mailbox labels

Press {kbd}`^T` to run an address query (using [`$query_command`](cfg-query-command)) and complete from the results.

## History Navigation

NeoMutt keeps a separate history list for each input category (addresses, filenames, patterns, shell commands, mailboxes, config commands, and everything else).
The number of history entries is controlled by [`$history`](cfg-history).

| Key      | Function           | Description                             |
|----------|--------------------|-----------------------------------------|
| {kbd}`Up`   | [`<history-up>`](fn-history-up)     | Recall the previous string from history |
| {kbd}`Down` | [`<history-down>`](fn-history-down)   | Recall the next string from history     |
| {kbd}`^R`     | [`<history-search>`](fn-history-search) | Search history using the current input  |

NeoMutt remembers what you were typing as you cycle through history, and wraps back to your original entry.

To make history persistent across sessions, set:

```neomuttrc
set history_file = ~/.config/neomutt/history
set save_history = 100
```

To remove all duplicate entries (not just consecutive ones):

```neomuttrc
set history_remove_dups
```

Entries starting with a space are silently ignored — useful in macros to avoid polluting history with transient values.

## Remapping Editor Keys

Use the [`:bind`](cmd-bind) command with the `editor` map to remap any function.
For example, to make {kbd}`Delete` behave like {kbd}`Backspace` (deleting the character *before* the cursor instead of *under* it):

```neomuttrc
bind editor <delete> backspace
```

## Using an External Editor

Set [`$editor`](cfg-editor) to launch an external editor for composing message bodies:

```neomuttrc
set editor = "vim"
```

The built-in line editor is still used for all prompt fields (To, Subject, etc.).
The external editor is invoked only for the message body when composing.
