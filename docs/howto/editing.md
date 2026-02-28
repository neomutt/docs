---
title: How to Edit Input Fields
description: Use NeoMutt's built-in line editor for prompts, header fields, and search
keywords: editor, line editor, emacs, keybindings, completion, history, input, editing
---

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

# How to Edit Input Fields

## Overview

NeoMutt has a built-in line editor for inputting text wherever you type at a prompt — for
example, email addresses in header fields, filenames, search patterns, and command lines.
The key bindings follow Emacs conventions.

## Key Bindings

### Movement

| Key | Function | Description |
|-----|----------|-------------|
| `^A` or `<Home>` | `<bol>` | Move to the start of the line |
| `^E` or `<End>` | `<eol>` | Move to the end of the line |
| `^B` or `<Left>` | `<backward-char>` | Move back one character |
| `^F` or `<Right>` | `<forward-char>` | Move forward one character |
| `Esc B` | `<backward-word>` | Move back one word |
| `Esc F` | `<forward-word>` | Move forward one word |

### Deletion

| Key | Function | Description |
|-----|----------|-------------|
| `^D` or `<Delete>` | `<delete-char>` | Delete the character under the cursor |
| `<BackSpace>` | `<backspace>` | Delete the character before the cursor |
| `^K` | `<kill-eol>` | Delete to the end of the line |
| `^U` | `<kill-line>` | Delete the entire line |
| `^W` | `<kill-word>` | Delete the word before the cursor |
| `Esc d` | `<kill-eow>` | Delete to the end of the word |

### Word Case

| Key | Function | Description |
|-----|----------|-------------|
| `Esc u` | `<upcase-word>` | Convert word to upper case |
| `Esc l` | `<downcase-word>` | Convert word to lower case |
| `Esc c` | `<capitalize-word>` | Capitalize the word |

### Miscellaneous

| Key | Function | Description |
|-----|----------|-------------|
| `^V` | `<quote-char>` | Quote (escape) the next typed key |
| `^G` | n/a | Abort the current prompt or action |
| `<Return>` | n/a | Confirm / finish editing |

## Tab Completion

Press `<Tab>` to trigger completion. What gets completed depends on context:

- **Filenames** — completes paths in the filesystem
- **Aliases** — completes known address aliases
- **Labels** — completes mailbox labels

Press `^T` to run an address query (using `$query_command`) and complete from the results.

## History Navigation

NeoMutt keeps a separate history list for each input category (addresses, filenames,
patterns, shell commands, mailboxes, config commands, and everything else). The number
of history entries is controlled by `$history`.

| Key | Function | Description |
|-----|----------|-------------|
| `<Up>` | `<history-up>` | Recall the previous string from history |
| `<Down>` | `<history-down>` | Recall the next string from history |
| `^R` | `<history-search>` | Search history using the current input |

NeoMutt remembers what you were typing as you cycle through history, and wraps back to
your original entry.

To make history persistent across sessions, set:

```
set history_file = ~/.config/neomutt/history
set save_history = 100
```

To remove all duplicate entries (not just consecutive ones):

```
set history_remove_dups
```

Entries starting with a space are silently ignored — useful in macros to avoid polluting
history with transient values.

## Remapping Editor Keys

Use the `bind` command with the `editor` map to remap any function. For example, to make
`<Delete>` behave like `<BackSpace>` (deleting the character *before* the cursor instead
of *under* it):

```
bind editor <delete> backspace
```

## Using an External Editor

Set `$editor` to launch an external editor for composing message bodies:

```
set editor = "vim"
```

The built-in line editor is still used for all prompt fields (To, Subject, etc.).
The external editor is invoked only for the message body when composing.
