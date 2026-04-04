---
title: Menu Options
description: Configuration variables for menu navigation, cursor style, scrolling behavior, and context lines.
keywords: neomutt, menu, arrow_cursor, arrow_string, menu_context, menu_move_off, menu_scroll, navigation, scrolling, cursor style, ui
---

(ref-cfg-menu)=
# Menu Options

(cfg-arrow-cursor)=
## `$arrow_cursor`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set arrow_cursor = no
    ```

When _set_, an arrow ("->") will be used to indicate the current entry in menus instead of highlighting the whole line.
On slow network or modem links this will make response faster because there is less that has to be redrawn on the screen when moving to the next or previous entries in the menu.

--------------------------------------------------------------------------------

(cfg-arrow-string)=
## `$arrow_string`

:Type: [String](type-string)
:Notes: [Not Empty](type-general)
:Default:
    ```neomuttrc
    set arrow_string = "->"
    ```

Specifies the string of arrow_cursor when arrow_cursor enabled.

--------------------------------------------------------------------------------

(cfg-menu-context)=
## `$menu_context`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set menu_context = 0
    ```

This variable controls the number of lines of context that are given when scrolling through menus.
(Similar to [`$pager_context`](cfg-pager-context).)

--------------------------------------------------------------------------------

(cfg-menu-move-off)=
## `$menu_move_off`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set menu_move_off = yes
    ```

When _unset_, the bottom entry of menus will never scroll up past the bottom of the screen, unless there are less entries than lines.
When _set_, the bottom entry may move off the bottom.

--------------------------------------------------------------------------------

(cfg-menu-scroll)=
## `$menu_scroll`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set menu_scroll = no
    ```

When _set_, menus will be scrolled up or down one line when you attempt to move across a screen boundary.
If _unset_, the screen is cleared and the next or previous page of the menu is displayed (useful for slow links to avoid many redraws).

