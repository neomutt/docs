---
title: Generic Functions
description: Common key bindings for scrolling, searching, tagging, and navigation inherited by all NeoMutt menus
keywords: neomutt, functions, generic, menu, bindings, keys, scrolling, searching, tagging, navigation, inherited, select-entry, next-page, previous-page, enter-command, tag-entry
---

(menu-generic)=
# Generic Functions

Not a menu itself, but provides common functions — such as scrolling, searching, and tagging — that are inherited by all other menus (except pager and editor).

The **generic** menu is not a real menu, but specifies common functions (such as
movement) available in all menus except for **pager** and **editor**. Changing
settings for this menu will affect the default bindings for all menus (except as
noted).

## Global

| Function              | Default Keys | Description                                    |
|-----------------------|--------------|------------------------------------------------|
| `<check-stats>`       |              | Calculate message statistics for all mailboxes |
| `<enter-command>`     | `:`          | Enter a neomuttrc command                      |
| `<exit>`              |              | Exit this menu                                 |
| `<help>`              | `?`          | Show the help screen                           |
| `<redraw-screen>`     | `^L`         | Clear and redraw the screen                    |
| `<shell-escape>`      | `!`          | Invoke a command in a subshell                 |
| `<show-log-messages>` |              | Show log (and debug) messages                  |
| `<show-version>`      | `V`          | Show the NeoMutt version number and date       |
| `<what-key>`          |              | Display the keycode for a key press            |

## Menu Movement

| Function           | Default Keys                           | Description                    |
|--------------------|----------------------------------------|--------------------------------|
| `<bottom-page>`    | `L`                                    | Move to the bottom of the page |
| `<current-bottom>` |                                        | Move entry to bottom of screen |
| `<current-middle>` |                                        | Move entry to middle of screen |
| `<current-top>`    |                                        | Move entry to top of screen    |
| `<first-entry>`    | `<Home>`, `=`                          | Move to the first entry        |
| `<half-down>`      | `]`                                    | Scroll down 1/2 page           |
| `<half-up>`        | `[`                                    | Scroll up 1/2 page             |
| `<jump>`           | `1`,`2`,`3`,`4`,`5`,`6`,`7`,`8`,`9`    | Jump to an index number        |
| `<last-entry>`     | `<End>`, `*`                           | Move to the last entry         |
| `<middle-page>`    | `M`                                    | Move to the middle of the page |
| `<next-entry>`     | `<Down>`, `j`                          | Move to the next entry         |
| `<next-line>`      | `>`                                    | Scroll down one line           |
| `<next-page>`      | `<PageDown>`, `<Right>`, `z`           | Move to the next page          |
| `<previous-entry>` | `<Up>`, `k`                            | Move to the previous entry     |
| `<previous-line>`  | `<`                                    | Scroll up one line             |
| `<previous-page>`  | `<PageUp>`, `<Left>`, `Z`              | Move to the previous page      |
| `<select-entry>`   | `<Enter>`, `<Return>`, `<KeypadEnter>` | Select the current entry       |
| `<top-page>`       | `H`                                    | Move to the top of the page    |

## Searching

| Function            | Default Keys | Description                                 |
|---------------------|--------------|---------------------------------------------|
| `<search>`          | `/`          | Search for a regular expression             |
| `<search-next>`     | `n`          | Search for next match                       |
| `<search-opposite>` |              | Search for next match in opposite direction |
| `<search-reverse>`  | `Esc /`      | Search backwards for a regular expression   |

## Tagging

| Function            | Default Keys | Description                                 |
|---------------------|--------------|---------------------------------------------|
| `<end-cond>`        |              | End of conditional execution (noop)         |
| `<tag-entry>`       | `t`          | Tag the current entry                       |
| `<tag-prefix>`      | `;`          | Apply next function to tagged messages      |
| `<tag-prefix-cond>` |              | Apply next function ONLY to tagged messages |

