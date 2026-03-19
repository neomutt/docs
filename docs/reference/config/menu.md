---
title: Menu Options
description: NeoMutt configuration variables for Menu-format mailbox handling.
keywords: neomutt, menu, menu_check_cur, menu_field_delimiter, menu_header_cache_verify, menu_trash, configuration
---

# Menu Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::


menu.md
	  { "arrow_cursor", DT_BOOL, false, 0, NULL,
	  { "arrow_string", DT_STRING|D_NOT_EMPTY, IP "->", 0, NULL,
	  { "menu_context", DT_NUMBER|D_INTEGER_NOT_NEGATIVE, 0, 0, NULL,
	  { "menu_move_off", DT_BOOL, true, 0, NULL,
	  { "menu_scroll", DT_BOOL, false, 0, NULL,

----------------------------------------------------------------------------------------------------------

(arrow-cursor)=
## `$arrow_cursor`

- **Type:** boolean
- **Default:** no

When *set*, an arrow ("->") will be used to indicate the current entry
in menus instead of highlighting the whole line.  On slow network or modem
links this will make response faster because there is less that has to
be redrawn on the screen when moving to the next or previous entries
in the menu.

----------------------------------------------------------------------------------------------------------

(arrow-string)=
## `$arrow_string`

- **Type:** string
- **Default:** "`->`"

Specifies the string of arrow_cursor when arrow_cursor enabled.

----------------------------------------------------------------------------------------------------------

(menu-context)=
## `$menu_context`

- **Type:** number
- **Default:** 0

This variable controls the number of lines of context that are given
when scrolling through menus. (Similar to [$pager_context](#pager-context).)

----------------------------------------------------------------------------------------------------------

(menu-move-off)=
## `$menu_move_off`

- **Type:** boolean
- **Default:** yes

When *unset*, the bottom entry of menus will never scroll up past
the bottom of the screen, unless there are less entries than lines.
When *set*, the bottom entry may move off the bottom.

----------------------------------------------------------------------------------------------------------

(menu-scroll)=
## `$menu_scroll`

- **Type:** boolean
- **Default:** no

When *set*, menus will be scrolled up or down one line when you
attempt to move across a screen boundary.  If *unset*, the screen
is cleared and the next or previous page of the menu is displayed
(useful for slow links to avoid many redraws).

