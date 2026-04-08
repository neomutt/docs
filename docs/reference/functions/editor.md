---
title: Editor Functions
description: Key bindings and functions for the NeoMutt command-line editor including cursor movement, word editing, and tab completion
keywords: neomutt, functions, editor, menu, bindings, keys, text input, command line, cursor movement, tab completion, history, kill-word, backward-char, forward-char, line editing
---

(menu-editor)=
# Editor Functions

The text input line where you type responses to prompts.
It supports cursor movement, word editing, tab-completion, and command history.

| Function            | Default Keys                        | Description                                         |
|---------------------|-------------------------------------|-----------------------------------------------------|
| `<backspace>`       | {kbd}`<Backspace>`, {kbd}`<Delete>` | Delete the char in front of the cursor              |
| `<backward-char>`   | {kbd}`<Left>`, {kbd}`Ctrl-B`        | Move the cursor one character to the left           |
| `<backward-word>`   | {kbd}`Alt-b`                        | Move the cursor to the beginning of the word        |
| `<bol>`             | {kbd}`<Home>`, {kbd}`Ctrl-A`        | Jump to the beginning of the line                   |
| `<capitalize-word>` | {kbd}`Alt-c`                        | Capitalize the word                                 |
| `<complete-query>`  | {kbd}`Ctrl-T`                       | Complete address with query                         |
| `<complete>`        | {kbd}`<Tab>`                        | Complete filename or alias                          |
| `<delete-char>`     | {kbd}`<Delete>`, {kbd}`Ctrl-D`      | Delete the char under the cursor                    |
| `<downcase-word>`   | {kbd}`Alt-l`                        | Convert the word to lower case                      |
| `<eol>`             | {kbd}`<End>`, {kbd}`Ctrl-E`         | Jump to the end of the line                         |
| `<forward-char>`    | {kbd}`<Right>`, {kbd}`Ctrl-F`       | Move the cursor one character to the right          |
| `<forward-word>`    | {kbd}`Alt-f`                        | Move the cursor to the end of the word              |
| `<help>`            | {kbd}`Alt-?`                        | Help screen                                         |
| `<history-down>`    | {kbd}`<Down>`, {kbd}`Ctrl-N`        | Scroll down through the history list                |
| `<history-search>`  | {kbd}`Ctrl-R`                       | Search through the history list                     |
| `<history-up>`      | {kbd}`<Up>`, {kbd}`Ctrl-P`          | Scroll up through the history list                  |
| `<kill-eol>`        | {kbd}`Ctrl-K`                       | Delete chars from cursor to end of line             |
| `<kill-eow>`        | {kbd}`Alt-d`                        | Delete chars from the cursor to the end of the word |
| `<kill-line>`       | {kbd}`Ctrl-U`                       | Delete chars from cursor to beginning of the line   |
| `<kill-whole-line>` |                                     | Delete all chars on the line                        |
| `<kill-word>`       | {kbd}`Ctrl-W`                       | Delete the word in front of the cursor              |
| `<mailbox-cycle>`   | {kbd}`<Space>`                      | Cycle among incoming mailboxes                      |
| `<quote-char>`      | {kbd}`Ctrl-V`                       | Quote the next typed key                            |
| `<redraw-screen>`   | {kbd}`Ctrl-L`                       | Clear and redraw the screen                         |
| `<transpose-chars>` |                                     | Transpose character under cursor with previous      |
| `<upcase-word>`     | {kbd}`Alt-u`                        | Convert the word to upper case                      |

