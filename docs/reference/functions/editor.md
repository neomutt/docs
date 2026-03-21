---
title: Editor Menu
description: Default Keys bindings and functions for the NeoMutt Editor Menu.
keywords: neomutt, functions, editor, menu, bindings, keys, input
---

(menu-editor)=
# Editor Menu

The text input line where you type responses to prompts.
It supports cursor movement, word editing, tab-completion, and command history.

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

| Function            | Default Keys              | Description                                         |
|---------------------|---------------------------|-----------------------------------------------------|
| `<backspace>`       | `<BackSpace>`, `<Delete>` | delete the char in front of the cursor              |
| `<backward-char>`   | `<Left>`, `^B`            | move the cursor one character to the left           |
| `<backward-word>`   | `Esc b`                   | move the cursor to the beginning of the word        |
| `<bol>`             | `<Home>`, `^A`            | jump to the beginning of the line                   |
| `<capitalize-word>` | `Esc c`                   | capitalize the word                                 |
| `<complete-query>`  | `^T`                      | complete address with query                         |
| `<complete>`        | `<Tab>`                   | complete filename or alias                          |
| `<delete-char>`     | `<Delete>`, `^D`          | delete the char under the cursor                    |
| `<downcase-word>`   | `Esc l`                   | convert the word to lower case                      |
| `<eol>`             | `<End>`, `^E`             | jump to the end of the line                         |
| `<forward-char>`    | `<Right>`, `^F`           | move the cursor one character to the right          |
| `<forward-word>`    | `Esc f`                   | move the cursor to the end of the word              |
| `<help>`            | `Esc ?`                   | help screen                                         |
| `<history-down>`    | `<Down>`, `^N`            | scroll down through the history list                |
| `<history-search>`  | `^R`                      | search through the history list                     |
| `<history-up>`      | `<Up>`, `^P`              | scroll up through the history list                  |
| `<kill-eol>`        | `^K`                      | delete chars from cursor to end of line             |
| `<kill-eow>`        | `Esc d`                   | delete chars from the cursor to the end of the word |
| `<kill-line>`       | `^U`                      | delete chars from cursor to beginning the line      |
| `<kill-whole-line>` |                           | delete all chars on the line                        |
| `<kill-word>`       | `^W`                      | delete the word in front of the cursor              |
| `<mailbox-cycle>`   | `<Space>`                 | cycle among incoming mailboxes                      |
| `<quote-char>`      | `^V`                      | quote the next typed key                            |
| `<redraw-screen>`   | `^L`                      | clear and redraw the screen                         |
| `<transpose-chars>` |                           | transpose character under cursor with previous      |
| `<upcase-word>`     | `Esc u`                   | convert the word to upper case                      |

