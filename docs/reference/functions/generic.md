---
title: Generic Menu
description: Default key bindings and functions for the NeoMutt Generic Menu.
keywords: neomutt, functions, generic, menu, bindings, keys
---

# Generic Menu

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

The **generic** menu is not a real menu, but specifies common functions (such as
movement) available in all menus except for **pager** and **editor**. Changing
settings for this menu will affect the default bindings for all menus (except as
noted).

The *generic* menu is not a real menu. It defines common functions (such as
movement) available in all menus except *pager* and *editor*. Changing bindings
here affects the defaults for all other menus (except as noted).


| Function              | Default Key     | Description                                    |
|-----------------------|-----------------|------------------------------------------------|
| `<bottom-page>`       | `L`             | move to the bottom of the page                 |
| `<check-stats>`       |                 | calculate message statistics for all mailboxes |
| `<current-bottom>`    |                 | move entry to bottom of screen                 |
| `<current-middle>`    |                 | move entry to middle of screen                 |
| `<current-top>`       |                 | move entry to top of screen                    |
| `<end-cond>`          |                 | end of conditional execution (noop)            |
| `<enter-command>`     | `:`             | enter a neomuttrc command                      |
| `<exit>`              |                 | exit this menu                                 |
| `<first-entry>`       | `<Home>`        | move to the first entry                        |
| `<first-entry>`       | `=`             | move to the first entry                        |
| `<half-down>`         | `]`             | scroll down 1/2 page                           |
| `<half-up>`           | `[`             | scroll up 1/2 page                             |
| `<help>`              | `?`             | this screen                                    |
| `<jump>`              |                 | jump to an index number                        |
| `<last-entry>`        | `<End>`         | move to the last entry                         |
| `<last-entry>`        | `*`             | move to the last entry                         |
| `<middle-page>`       | `M`             | move to the middle of the page                 |
| `<next-entry>`        | `<Down>`        | move to the next entry                         |
| `<next-entry>`        | `j`             | move to the next entry                         |
| `<next-line>`         | `>`             | scroll down one line                           |
| `<next-page>`         | `<Pagedown>`    | move to the next page                          |
| `<next-page>`         | `<Right>`       | move to the next page                          |
| `<next-page>`         | `z`             | move to the next page                          |
| `<previous-entry>`    | `<Up>`          | move to the previous entry                     |
| `<previous-entry>`    | `k`             | move to the previous entry                     |
| `<previous-line>`     | `<`             | scroll up one line                             |
| `<previous-page>`     | `<Left>`        | move to the previous page                      |
| `<previous-page>`     | `<Pageup>`      | move to the previous page                      |
| `<previous-page>`     | `Z`             | move to the previous page                      |
| `<redraw-screen>`     | `^L`            | clear and redraw the screen                    |
| `<search>`            | `/`             | search for a regular expression                |
| `<search-next>`       | `n`             | search for next match                          |
| `<search-opposite>`   |                 | search for next match in opposite direction    |
| `<search-reverse>`    | `Esc /`         | search backwards for a regular expression      |
| `<select-entry>`      | `<Enter>`       | select the current entry                       |
| `<select-entry>`      | `<Keypadenter>` | select the current entry                       |
| `<select-entry>`      | `<Return>`      | select the current entry                       |
| `<shell-escape>`      | `!`             | invoke a command in a subshell                 |
| `<show-log-messages>` |                 | show log (and debug) messages                  |
| `<show-version>`      | `V`             | show the NeoMutt version number and date       |
| `<tag-entry>`         | `t`             | tag the current entry                          |
| `<tag-prefix>`        | `;`             | apply next function to tagged messages         |
| `<tag-prefix-cond>`   |                 | apply next function ONLY to tagged messages    |
| `<top-page>`          | `H`             | move to the top of the page                    |
| `<what-key>`          |                 | display the keycode for a key press            |
