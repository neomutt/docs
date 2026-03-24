---
title: Editor Menu
description: Default Keys bindings and functions for the NeoMutt Editor Menu.
keywords: neomutt, functions, editor, menu, bindings, keys, input
---

(menu-editor)=
# Editor Menu

The text input line where you type responses to prompts.
It supports cursor movement, word editing, tab-completion, and command history.

| Function            | Default Keys              | Description                                         |
|---------------------|---------------------------|-----------------------------------------------------|
| `<backspace>`       | `<BackSpace>`, `<Delete>` | Delete the char in front of the cursor              |
| `<backward-char>`   | `<Left>`, `^B`            | Move the cursor one character to the left           |
| `<backward-word>`   | `Esc b`                   | Move the cursor to the beginning of the word        |
| `<bol>`             | `<Home>`, `^A`            | Jump to the beginning of the line                   |
| `<capitalize-word>` | `Esc c`                   | Capitalize the word                                 |
| `<complete-query>`  | `^T`                      | Complete address with query                         |
| `<complete>`        | `<Tab>`                   | Complete filename or alias                          |
| `<delete-char>`     | `<Delete>`, `^D`          | Delete the char under the cursor                    |
| `<downcase-word>`   | `Esc l`                   | Convert the word to lower case                      |
| `<eol>`             | `<End>`, `^E`             | Jump to the end of the line                         |
| `<forward-char>`    | `<Right>`, `^F`           | Move the cursor one character to the right          |
| `<forward-word>`    | `Esc f`                   | Move the cursor to the end of the word              |
| `<help>`            | `Esc ?`                   | Help screen                                         |
| `<history-down>`    | `<Down>`, `^N`            | Scroll down through the history list                |
| `<history-search>`  | `^R`                      | Search through the history list                     |
| `<history-up>`      | `<Up>`, `^P`              | Scroll up through the history list                  |
| `<kill-eol>`        | `^K`                      | Delete chars from cursor to end of line             |
| `<kill-eow>`        | `Esc d`                   | Delete chars from the cursor to the end of the word |
| `<kill-line>`       | `^U`                      | Delete chars from cursor to beginning the line      |
| `<kill-whole-line>` |                           | Delete all chars on the line                        |
| `<kill-word>`       | `^W`                      | Delete the word in front of the cursor              |
| `<mailbox-cycle>`   | `<Space>`                 | Cycle among incoming mailboxes                      |
| `<quote-char>`      | `^V`                      | Quote the next typed key                            |
| `<redraw-screen>`   | `^L`                      | Clear and redraw the screen                         |
| `<transpose-chars>` |                           | Transpose character under cursor with previous      |
| `<upcase-word>`     | `Esc u`                   | Convert the word to upper case                      |

