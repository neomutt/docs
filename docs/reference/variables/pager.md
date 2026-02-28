---
title: "Pager Variables"
description: "Reference for NeoMutt pager configuration variables."
keywords: "pager, reading, display, variables, neomutt"
---

# Pager Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

(pager)=
## `$pager`

- **Type:** command
- **Default:** (empty)

This variable specifies which pager you would like to use to view
messages. When empty, NeoMutt will use the built-in pager, otherwise this
variable should specify the pathname of the external pager you would
like to use.

Using an external pager may have some disadvantages: Additional
keystrokes are necessary because you can't call NeoMutt functions
directly from the pager, and screen resizes cause lines longer than
the screen width to be badly formatted in the help menu.

(pager-context)=
## `$pager_context`

- **Type:** number
- **Default:** 0

This variable controls the number of lines of context that are given
when displaying the next or previous page in the internal pager.  By
default, NeoMutt will display the line after the last one on the screen
at the top of the next page (0 lines of context).

This variable also specifies the amount of context given for search
results. If positive, this many lines will be given before a match,
if 0, the match will be top-aligned.

(pager-format)=
## `$pager_format`

- **Type:** string
- **Default:** "`-%Z- %C/%m: %-20.20n   %s%*  -- (%P)`"

This variable controls the format of the one-line message "status"
displayed before each message in either the internal or an external
pager.  The valid sequences are listed in the [`$index_format`](#index-format)
section.

(pager-index-lines)=
## `$pager_index_lines`

- **Type:** number
- **Default:** 0

Determines the number of lines of a mini-index which is shown when in
the pager.  The current message, unless near the top or bottom of the
folder, will be roughly one third of the way down this mini-index,
giving the reader the context of a few messages before and after the
message.  This is useful, for example, to determine how many messages
remain to be read in the current thread.  A value of 0 results in no index
being shown.

(pager-read-delay)=
## `$pager_read_delay`

- **Type:** number
- **Default:** 0

Determines the number of seconds that must elapse after first
opening a new message in the pager before that message will be
marked as read.  A value of 0 results in the message being marked
read unconditionally; for other values, navigating to another
message or exiting the pager before the timeout will leave the
message marked unread.  This setting is ignored if [`$pager`](#pager) is set.

(pager-skip-quoted-context)=
## `$pager_skip_quoted_context`

- **Type:** number
- **Default:** 0

Determines the number of lines of context to show before the
unquoted text when using the `<skip-quoted>` function. When set
to a positive number at most that many lines of the previous quote
are displayed. If the previous quote is shorter the whole quote is
displayed.

(pager-stop)=
## `$pager_stop`

- **Type:** boolean
- **Default:** no

When *set*, the internal-pager will *not* move to the next message
when you are at the end of a message and invoke the `<next-page>`
function.
