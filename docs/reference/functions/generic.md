---
title: Generic Menu
description: Default Keys bindings and functions for the NeoMutt Generic Menu.
keywords: neomutt, functions, generic, menu, bindings, keys
---

(menu-generic)=
# Generic Menu

Not a menu itself, but provides common functions — such as scrolling, searching, and tagging — that are inherited by all other menus (except pager and editor).

The **generic** menu is not a real menu, but specifies common functions (such as
movement) available in all menus except for **pager** and **editor**. Changing
settings for this menu will affect the default bindings for all menus (except as
noted).

| Function              | Default Keys                           | Description                                    |
|-----------------------|----------------------------------------|------------------------------------------------|
| `<bottom-page>`       | `L`                                    | Move to the bottom of the page                 |
| `<check-stats>`       |                                        | Calculate message statistics for all mailboxes |
| `<current-bottom>`    |                                        | Move entry to bottom of screen                 |
| `<current-middle>`    |                                        | Move entry to middle of screen                 |
| `<current-top>`       |                                        | Move entry to top of screen                    |
| `<end-cond>`          |                                        | End of conditional execution (noop)            |
| `<enter-command>`     | `:`                                    | Enter a neomuttrc command                      |
| `<exit>`              |                                        | Exit this menu                                 |
| `<first-entry>`       | `<Home>`, `=`                          | Move to the first entry                        |
| `<half-down>`         | `]`                                    | Scroll down 1/2 page                           |
| `<half-up>`           | `[`                                    | Scroll up 1/2 page                             |
| `<help>`              | `?`                                    | This screen                                    |
| `<jump>`              | `1`,`2`,`3`,`4`,`5`,`6`,`7`,`8`,`9`    | Jump to an index number                        |
| `<last-entry>`        | `<End>`, `*`                           | Move to the last entry                         |
| `<middle-page>`       | `M`                                    | Move to the middle of the page                 |
| `<next-entry>`        | `<Down>`, `j`                          | Move to the next entry                         |
| `<next-line>`         | `>`                                    | Scroll down one line                           |
| `<next-page>`         | `<PageDown>`, `<Right>`, `z`           | Move to the next page                          |
| `<previous-entry>`    | `<Up>`, `k`                            | Move to the previous entry                     |
| `<previous-line>`     | `<`                                    | Scroll up one line                             |
| `<previous-page>`     | `<PageUp>`, `<Left>`, `Z`              | Move to the previous page                      |
| `<redraw-screen>`     | `^L`                                   | Clear and redraw the screen                    |
| `<search>`            | `/`                                    | Search for a regular expression                |
| `<search-next>`       | `n`                                    | Search for next match                          |
| `<search-opposite>`   |                                        | Search for next match in opposite direction    |
| `<search-reverse>`    | `Esc /`                                | Search backwards for a regular expression      |
| `<select-entry>`      | `<Enter>`, `<Return>`, `<KeypadEnter>` | Select the current entry                       |
| `<shell-escape>`      | `!`                                    | Invoke a command in a subshell                 |
| `<show-log-messages>` |                                        | Show log (and debug) messages                  |
| `<show-version>`      | `V`                                    | Show the NeoMutt version number and date       |
| `<tag-entry>`         | `t`                                    | Tag the current entry                          |
| `<tag-prefix>`        | `;`                                    | Apply next function to tagged messages         |
| `<tag-prefix-cond>`   |                                        | Apply next function ONLY to tagged messages    |
| `<top-page>`          | `H`                                    | Move to the top of the page                    |
| `<what-key>`          |                                        | Display the keycode for a key press            |

