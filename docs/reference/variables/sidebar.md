---
title: "Sidebar Variables"
description: "Reference for NeoMutt sidebar configuration variables."
keywords: "sidebar, navigation, variables, neomutt"
---

# Sidebar Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

(sidebar-component-depth)=
## `$sidebar_component_depth`

- **Type:** number
- **Default:** 0

By default the sidebar will show the mailbox's path, relative to the
[`$folder`](#folder) variable. This specifies the number of parent directories to hide
from display in the sidebar. For example: If a maildir is normally
displayed in the sidebar as dir1/dir2/dir3/maildir, setting
`sidebar_component_depth=2` will display it as dir3/maildir, having
truncated the 2 highest directories.

*See also:* [`$sidebar_short_path`](#sidebar-short-path)

(sidebar-delim-chars)=
## `$sidebar_delim_chars`

- **Type:** string
- **Default:** "`/.`"

This contains the list of characters which you would like to treat
as folder separators for displaying paths in the sidebar.

Local mail is often arranged in directories: 'dir1/dir2/mailbox'.

```
set sidebar_delim_chars='/'
```

IMAP mailboxes are often named: 'folder1.folder2.mailbox'.

```
set sidebar_delim_chars='.'
```

*See also:* [`$sidebar_short_path`](#sidebar-short-path), [`$sidebar_folder_indent`](#sidebar-folder-indent),
[`$sidebar_indent_string`](#sidebar-indent-string).

(sidebar-divider-char)=
## `$sidebar_divider_char`

- **Type:** string
- **Default:** "`|`"

The default is a Unicode vertical line.

This specifies the characters to be drawn between the sidebar (when
visible) and the other NeoMutt panels. ASCII and Unicode line-drawing
characters are supported.

The divider char can be set to an empty string for some extra space.
If empty, setting the sidebar_background color may help distinguish the
sidebar from other panels.

(sidebar-folder-indent)=
## `$sidebar_folder_indent`

- **Type:** boolean
- **Default:** no

Set this to indent mailboxes in the sidebar.

*See also:* [`$sidebar_short_path`](#sidebar-short-path), [`$sidebar_indent_string`](#sidebar-indent-string),
[`$sidebar_delim_chars`](#sidebar-delim-chars).

(sidebar-format)=
## `$sidebar_format`

- **Type:** string
- **Default:** "`%D%*  %n`"

This variable allows you to customize the sidebar display. This string is
similar to [`$index_format`](#index-format), but has its own set of `printf(3)`-like
sequences:

*Short* *Long Name*        *Cur* *Description*

`%a`    `%{notify}`                  Alert: 1 if user is notified of new mail

`%B`    `%{name}`                    Name of the mailbox

`%D`    `%{description}`             Descriptive name of the mailbox

`%d`    `%{deleted-count}` Cur       Number of deleted messages in the mailbox

`%F`    `%{flagged-count}`           Number of flagged messages in the mailbox

`%L`    `%{limited-count}` Cur       Number of messages after limiting

`%N`    `%{new-mail}`                Number of unread messages in the mailbox (seen or unseen)

`%n`    `%{unread-count}`            `N` if mailbox has new mail, ` ` (space) otherwise

`%o`    `%{old-count}`               Number of old messages in the mailbox (unread, seen)

`%p`    `%{poll}`                    Poll: 1 if Mailbox is checked for new mail

`%r`    `%{read-count}`              Number of read messages in the mailbox (read, seen)

`%S`    `%{message-count}`           Size of mailbox (total number of messages)

`%t`    `%{tagged-count}`  Cur       Number of tagged messages in the mailbox

`%Z`    `%{unseen-count}`            Number of new messages in the mailbox (unread, unseen)

`%!`    `%{flagged}`                 `!` : one flagged message

                                             `!!` : two flagged messages

                                             `n!` : n flagged messages (for n > 2)

`%*X`   `%{padding-soft}`            Soft-fill with character `X` as pad

`%>X`   `%{padding-hard}`            Right justify the rest of the string and pad with character `X`

`%|X`   `%{padding-eol}`             Pad to the end of the line with character `X`

*Cur* = Only applicable to the current folder

In order to use %S, %N, %F, and %!, [`$mail_check_stats`](#mail-check-stats) must
be *set*.  When thus set, a suggested value for this option is
"%B%<F? [%F]>%* %<N?%N/>%S".

(sidebar-indent-string)=
## `$sidebar_indent_string`

- **Type:** string
- **Default:** "`  `"

This specifies the string that is used to indent mailboxes in the sidebar.
It defaults to two spaces.

*See also:* [`$sidebar_short_path`](#sidebar-short-path), [`$sidebar_folder_indent`](#sidebar-folder-indent),
[`$sidebar_delim_chars`](#sidebar-delim-chars).

(sidebar-new-mail-only)=
## `$sidebar_new_mail_only`

- **Type:** boolean
- **Default:** no

When set, the sidebar will only display mailboxes containing new, or
flagged, mail.

*See also:* `sidebar-pin`, [`$sidebar_non_empty_mailbox_only`](#sidebar-non-empty-mailbox-only).

(sidebar-next-new-wrap)=
## `$sidebar_next_new_wrap`

- **Type:** boolean
- **Default:** no

When set, the `<sidebar-next-new>` command will not stop at the end of
the list of mailboxes, but wrap around to the beginning. The
`<sidebar-prev-new>` command is similarly affected, wrapping around to
the end of the list.

(sidebar-non-empty-mailbox-only)=
## `$sidebar_non_empty_mailbox_only`

- **Type:** boolean
- **Default:** no

When set, the sidebar will only display mailboxes that contain one or more
mails.

*See also:* [`$sidebar_new_mail_only`](#sidebar-new-mail-only), `sidebar-pin`.

(sidebar-on-right)=
## `$sidebar_on_right`

- **Type:** boolean
- **Default:** no

When set, the sidebar will appear on the right-hand side of the screen.

(sidebar-short-path)=
## `$sidebar_short_path`

- **Type:** boolean
- **Default:** no

By default the sidebar will show the mailbox's path, relative to the
[`$folder`](#folder) variable. Setting `sidebar_shortpath=yes` will shorten the
names relative to the previous name. Here's an example:

*shortpath=no* *shortpath=yes* *shortpath=yes, folderindent=yes, indentstr=".."*

`fruit`        `fruit`         `fruit`

`fruit.apple`  `apple`         `..apple`

`fruit.banana` `banana`        `..banana`

`fruit.cherry` `cherry`        `..cherry`

*See also:* [`$sidebar_delim_chars`](#sidebar-delim-chars), [`$sidebar_folder_indent`](#sidebar-folder-indent),
[`$sidebar_indent_string`](#sidebar-indent-string), [`$sidebar_component_depth`](#sidebar-component-depth).

(sidebar-sort)=
## `$sidebar_sort`

- **Type:** sort order
- **Default:** unsorted

Specifies how to sort mailbox entries in the sidebar.

*Value*    *Sort by*

`count`    Total message count

`desc`     Mailbox description

`flagged`  Count of flagged messages

`path`     Mailbox path (alphabetically)

`unread`   Count of unread messages

`unsorted` The order the mailboxes were configured

*Deprecated Value* *Use this instead*

`alpha`            `path`

`mailbox-order`    `unsorted`

`name`             `path`

`new`              `unread`

(sidebar-visible)=
## `$sidebar_visible`

- **Type:** boolean
- **Default:** no

This specifies whether or not to show sidebar. The sidebar shows a list of
all your mailboxes.

*See also:* [`$sidebar_format`](#sidebar-format), [`$sidebar_width`](#sidebar-width)

(sidebar-width)=
## `$sidebar_width`

- **Type:** number
- **Default:** 30

This controls the width of the sidebar.  It is measured in screen columns.
For example: sidebar_width=20 could display 20 ASCII characters, or 10
Chinese characters.
