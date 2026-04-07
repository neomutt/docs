---
title: Sidebar Options
description: Configuration variables for the sidebar panel, including visibility, width, formatting, sorting, and indentation.
keywords: sidebar, sidebar_visible, sidebar_width, sidebar_format, sidebar_sort, sidebar_short_path, sidebar_folder_indent, folder list, navigation panel, mailbox list
---

(ref-cfg-sidebar)=
# Sidebar Options

(cfg-sidebar-component-depth)=
## `$sidebar_component_depth`

:Description: Strip leading path components from sidebar folders
:Type: [Number](type-number)
:Default:
    ```neomuttrc
    set sidebar_component_depth = 0
    ```

By default the sidebar will show the mailbox's path, relative to the [`$folder`](cfg-folder) variable.
This specifies the number of parent directories to hide from display in the sidebar.
For example: If a maildir is normally displayed in the sidebar as dir1/dir2/dir3/maildir, setting `set sidebar_component_depth = 2` will display it as dir3/maildir, having truncated the 2 highest directories.

:::{seealso}
[`$sidebar_short_path`](cfg-sidebar-short-path)
:::

--------------------------------------------------------------------------------

(cfg-sidebar-delim-chars)=
## `$sidebar_delim_chars`

:Description: Characters that separate nested folders
:Type: [String](type-string)
:Notes: [Case Sensitive](type-general)
:Default:
    ```neomuttrc
    set sidebar_delim_chars = "/."
    ```

This contains the list of characters which you would like to treat as folder separators for displaying paths in the sidebar.

Local mail is often arranged in directories: `dir1/dir2/mailbox`.

```neomuttrc
set sidebar_delim_chars = '/'
```

IMAP mailboxes are often named: 'folder1.folder2.mailbox'.

```neomuttrc
set sidebar_delim_chars = '.'
```

:::{seealso}
[`$sidebar_short_path`](cfg-sidebar-short-path), [`$sidebar_folder_indent`](cfg-sidebar-folder-indent), [`$sidebar_indent_string`](cfg-sidebar-indent-string)
:::

--------------------------------------------------------------------------------

(cfg-sidebar-divider-char)=
## `$sidebar_divider_char`

:Description: Character to draw between the sidebar and index
:Type: [String](type-string)
:Default:
    ```neomuttrc
    set sidebar_divider_char = "│" # Unicode: Box Drawings Light Vertical, U+2502
    ```

This specifies the characters to be drawn between the sidebar (when visible) and the other NeoMutt panels.
ASCII and Unicode line-drawing characters are supported.

The divider char can be set to an empty string for some extra space.
If empty, setting the `sidebar_background` color may help distinguish the sidebar from other panels.

--------------------------------------------------------------------------------

(cfg-sidebar-folder-indent)=
## `$sidebar_folder_indent`

:Description: Indent nested folders
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set sidebar_folder_indent = no
    ```

Set this to indent mailboxes in the sidebar.

:::{seealso}
[`$sidebar_short_path`](cfg-sidebar-short-path), [`$sidebar_indent_string`](cfg-sidebar-indent-string), [`$sidebar_delim_chars`](cfg-sidebar-delim-chars)
:::

--------------------------------------------------------------------------------

(cfg-sidebar-format)=
## `$sidebar_format`

:Description: Format string for the [Sidebar](tour-sidebar)
:Type: [Expando](type-expando)
:Notes: [Not Empty](type-general), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set sidebar_format = "%D%*  %n"
    ```
:Alternative:
    ```neomuttrc
    set sidebar_format = "%{description}%{padding-soft: } %{new-mail}"
    ```

Specify the format of the data displayed in the [`Sidebar Panel`](tour-sidebar).

**Format Sequences**

| Short  | Long Name           | Cur | Description                                                                                |
|--------|---------------------|-----|--------------------------------------------------------------------------------------------|
| `%a`   | `%{notify}`         |     | Alert: 1 if user is notified of new mail                                                   |
| `%B`   | `%{name}`           |     | Name of the mailbox                                                                        |
| `%D`   | `%{description}`    |     | Descriptive name of the mailbox                                                            |
| `%d`   | `%{deleted-count}`  | Cur | Number of deleted messages in the mailbox                                                  |
| `%F`   | `%{flagged-count}`  |     | Number of flagged messages in the mailbox                                                  |
| `%L`   | `%{limited-count}`  | Cur | Number of messages after limiting                                                          |
| `%N`   | `%{new-mail}`       |     | Number of unread messages in the mailbox (seen or unseen)                                  |
| `%n`   | `%{unread-count}`   |     | `N` if mailbox has new mail, ` ` (space) otherwise                                         |
| `%o`   | `%{old-count}`      |     | Number of old messages in the mailbox (unread, seen)                                       |
| `%p`   | `%{poll}`           |     | Poll: 1 if Mailbox is checked for new mail                                                 |
| `%r`   | `%{read-count}`     |     | Number of read messages in the mailbox (read, seen)                                        |
| `%S`   | `%{message-count}`  |     | Size of mailbox (total number of messages)                                                 |
| `%t`   | `%{tagged-count}`   | Cur | Number of tagged messages in the mailbox                                                   |
| `%Z`   | `%{unseen-count}`   |     | Number of new messages in the mailbox (unread, unseen)                                     |
| `%!`   | `%{flagged}`        |     | `!`: one flagged message; `!!`: two flagged messages; `n!`: n flagged messages (for n > 2) |
| `%*X`  | `%{padding-soft:X}` |     | Soft-fill with character `X` as pad                                                        |
| `%>X`  | `%{padding-hard:X}` |     | Right justify the rest of the string and pad with character `X`                            |
| `%\|X` | `%{padding-eol:X}`  |     | Pad to the end of the line with character `X`                                              |

**Cur** = Only applicable to the current folder

In order to use %S, %N, %F, and %!, [`$mail_check_stats`](cfg-mail-check-stats) must be _set_.
When thus set, a suggested value for this option is `%B%<F? [%F]>%* %<N?%N/>%S`.

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)

[`$sidebar_short_path`](cfg-sidebar-short-path)
:::

--------------------------------------------------------------------------------

(cfg-sidebar-indent-string)=
## `$sidebar_indent_string`

:Description: Indent nested folders using this string
:Type: [String](type-string)
:Default:
    ```neomuttrc
    set sidebar_indent_string = "  " # Two spaces
    ```

This specifies the string that is used to indent mailboxes in the sidebar.
It defaults to two spaces.

:::{seealso}
[`$sidebar_short_path`](cfg-sidebar-short-path), [`$sidebar_folder_indent`](cfg-sidebar-folder-indent), [`$sidebar_delim_chars`](cfg-sidebar-delim-chars)
:::

--------------------------------------------------------------------------------

(cfg-sidebar-new-mail-only)=
## `$sidebar_new_mail_only`

:Description: Only show folders with new/flagged email
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set sidebar_new_mail_only = no
    ```

When set, the sidebar will only display mailboxes containing new, or flagged, mail.

:::{seealso}
[`:sidebar-pin`](cmd-sidebar-pin), [`$sidebar_non_empty_mailbox_only`](cfg-sidebar-non-empty-mailbox-only)
:::

--------------------------------------------------------------------------------

(cfg-sidebar-next-new-wrap)=
## `$sidebar_next_new_wrap`

:Description: Wrap around when searching for the next mailbox with new email
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set sidebar_next_new_wrap = no
    ```

When set, the [`<sidebar-next-new>`](ref-fn-sidebar) command will not stop at the end of the list of mailboxes, but wrap around to the beginning.
The [`<sidebar-prev-new>`](ref-fn-sidebar) command is similarly affected, wrapping around to the end of the list.

--------------------------------------------------------------------------------

(cfg-sidebar-non-empty-mailbox-only)=
## `$sidebar_non_empty_mailbox_only`

:Description: Only show folders with a non-zero number of emails
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set sidebar_non_empty_mailbox_only = no
    ```

When set, the sidebar will only display mailboxes that contain one or more mails.

:::{seealso}
[`$sidebar_new_mail_only`](cfg-sidebar-new-mail-only), [`:sidebar-pin`](cmd-sidebar-pin)
:::

--------------------------------------------------------------------------------

(cfg-sidebar-on-right)=
## `$sidebar_on_right`

:Description: Display the sidebar on the right
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set sidebar_on_right = no
    ```

When set, the sidebar will appear on the right-hand side of the screen.

--------------------------------------------------------------------------------

(cfg-sidebar-short-path)=
## `$sidebar_short_path`

:Description: Abbreviate the paths using the [`$folder`](cfg-folder) variable
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set sidebar_short_path = no
    ```

By default the sidebar will show the mailbox's path, relative to the [`$folder`](cfg-folder) variable.
Setting `set sidebar_shortpath = yes` will shorten the names relative to the previous name.
Here's an example:

| shortpath=no   | shortpath=yes | shortpath=yes, folderindent=yes, indentstr=".." |
|----------------|---------------|-------------------------------------------------|
| `fruit`        | `fruit`       | `fruit`                                         |
| `fruit.apple`  | `apple`       | `..apple`                                       |
| `fruit.banana` | `banana`      | `..banana`                                      |
| `fruit.cherry` | `cherry`      | `..cherry`                                      |

:::{seealso}
[`$sidebar_delim_chars`](cfg-sidebar-delim-chars), [`$sidebar_folder_indent`](cfg-sidebar-folder-indent), [`$sidebar_indent_string`](cfg-sidebar-indent-string), [`$sidebar_component_depth`](cfg-sidebar-component-depth)
:::

--------------------------------------------------------------------------------

(cfg-sidebar-sort)=
## `$sidebar_sort`

:Description: Sort method for the [Sidebar](tour-sidebar)
:Type: [Sort Order](type-sort-order)
:Default:
    ```neomuttrc
    set sidebar_sort = unsorted
    ```

Specifies how to sort mailbox entries in the sidebar.

| Value      | Sort by                                 |
|------------|-----------------------------------------|
| `count`    | Total message count                     |
| `desc`     | Mailbox description                     |
| `flagged`  | Count of flagged messages               |
| `path`     | Mailbox path (alphabetically)           |
| `unread`   | Count of unread messages                |
| `unsorted` | The order the mailboxes were configured |

| Deprecated Value | Use this instead |
|------------------|------------------|
| `alpha`          | `path`           |
| `mailbox-order`  | `unsorted`       |
| `name`           | `path`           |
| `new`            | `unread`         |

--------------------------------------------------------------------------------

(cfg-sidebar-visible)=
## `$sidebar_visible`

:Description: Show the [Sidebar](tour-sidebar)
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set sidebar_visible = no
    ```

This specifies whether or not to show sidebar.
The sidebar shows a list of all your mailboxes.

:::{seealso}
[`$sidebar_format`](cfg-sidebar-format), [`$sidebar_width`](cfg-sidebar-width)
:::

--------------------------------------------------------------------------------

(cfg-sidebar-width)=
## `$sidebar_width`

:Description: Width of the sidebar
:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set sidebar_width = 30
    ```

This controls the width of the sidebar.
It is measured in screen columns.
For example: `set sidebar_width = 20` could display 20 ASCII characters, or 10 Chinese characters.

