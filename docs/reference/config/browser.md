---
title: Browser Options
description: NeoMutt configuration variables for the file browser display and sorting.
keywords: neomutt, browser, browser_abbreviate_mailboxes, browser_sort, browser_sort_dirs_first, configuration
---

# Browser Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

--------------------------------------------------------------------------------

(browser-abbreviate-mailboxes)=
## `$browser_abbreviate_mailboxes`

- **Type:** boolean
- **Default:**
    ```neomuttrc
    set browser_abbreviate_mailboxes = yes
    ```

When this variable is _set_, NeoMutt will abbreviate mailbox names in the browser mailbox list, using '~' and '=' shortcuts.

The default `"alpha"` setting of $$browser_sort uses locale-based sorting (using `strcoll(3)`), which ignores some punctuation.
This can lead to some situations where the order doesn't make intuitive sense.
In those cases, it may be desirable to _unset_ this variable.

--------------------------------------------------------------------------------

(browser-sort)=
## `$browser_sort`

- **Type:** sort order
- **Notes:** Sort Reverse
- **Default:**
    ```neomuttrc
    set browser_sort = "alpha"
    ```

Specifies how to sort entries in the file browser.

| Value      | Sort by               |
|------------|-----------------------|
| `alpha`    | Name                  |
| `count`    | Total message count   |
| `date`     | Date                  |
| `desc`     | Description           |
| `size`     | Count of new messages |
| `new`      | Size                  |
| `unsorted` | Unsorted              |

| Deprecated Value | Use this instead |
|------------------|------------------|
| `unread`         | `new`            |

--------------------------------------------------------------------------------

(browser-sort-dirs-first)=
## `$browser_sort_dirs_first`

- **Type:** boolean
- **Default:**
    ```neomuttrc
    set browser_sort_dirs_first = no
    ```

If this variable is _set_, the browser will group directories before files.

--------------------------------------------------------------------------------

(folder-format)=
## `$folder_format`

- **Type:** expando
- **Notes:** Not empty
- **Default:**
    ```neomuttrc
    set folder_format = "%2C %t %N %F %2l %-8.8u %-8.8g %8s %d %i"
    ```

This variable allows you to customize the file browser display to your personal taste.
This string is similar to $$index_format, but has its own set of `printf(3)`-like sequences:

| Short    | Long Name           | Description                                                                                          |
|----------|---------------------|------------------------------------------------------------------------------------------------------|
| `%a`     | `%{notify}`         | Alert: 1 if user is notified of new mail                                                             |
| `%C`     | `%{number}`         | Current file number                                                                                  |
| `%D`     | `%{date}`           | Date/time folder was last modified using [$date_format](#date-format).                               |
|          |                     | It is recommended to use `%[fmt]` instead, where `fmt` is the value of [$date_format](#date-format). |
| `%d`     | `%{date-format}`    | Date/time folder was last modified                                                                   |
| `%F`     | `%{file-mode}`      | File permissions                                                                                     |
| `%f`     | `%{filename}`       | Filename (`/` is appended to directory names,                                                        |
|          |                     | `@` to symbolic links and `*` to executable files)                                                   |
| `%g`     | `%{file-group}`     | Group name (or numeric gid, if missing)                                                              |
| `%i`     | `%{description}`    | Description of the folder                                                                            |
| `%l`     | `%{hard-links}`     | Number of hard links                                                                                 |
| `%m`     | `%{message-count}`  | Number of messages in the mailbox                                                                    |
| `%N`     | `%{new-mail}`       | `N` if mailbox has new mail, ` ` (space) otherwise                                                   |
| `%n`     | `%{unread-count}`   | Number of unread messages in the mailbox                                                             |
| `%p`     | `%{poll}`           | Poll: 1 if Mailbox is checked for new mail                                                           |
| `%s`     | `%{file-size}`      | Size in bytes (see **Size Format**)                                                                  |
| `%t`     | `%{tagged}`         | `*` if the file is tagged, blank otherwise                                                           |
| `%u`     | `%{file-owner}`     | Owner name (or numeric uid, if missing)                                                              |
| `%[fmt]` |                     | Date/time folder was last modified using an `strftime(3)` expression                                 |
| `%*X`    | `%{padding-soft:X}` | Soft-fill with character `X` as pad                                                                  |
| `%>X`    | `%{padding-hard:X}` | Right justify the rest of the string and pad with character `X`                                      |
| `%\|X`   | `%{padding-eol:X}`  | Pad to the end of the line with character `X`                                                        |

For an explanation of "soft-fill", see the $$index_format documentation.

* = can be optionally printed if nonzero

%m, %n, and %N only work for monitored mailboxes.
%m requires [$mail_check_stats](#mail-check-stats) to be set.
%n requires [$mail_check_stats](#mail-check-stats) to be set (except for IMAP mailboxes).

--------------------------------------------------------------------------------

(group-index-format)=
## `$group_index_format`

- **Type:** expando
- **Notes:** Not empty
- **Default:**
    ```neomuttrc
    set group_index_format = "%4C %M%N %5s  %-45.45f %d"
    ```

This variable allows you to customize the newsgroup browser display to your personal taste.
This string is similar to "$index_format", but has its own set of printf()-like sequences:

| Short  | Long Name           | Description                                                          |
|--------|---------------------|----------------------------------------------------------------------|
| `%a`   | `%{notify}`         | Alert: 1 if user is notified of new mail                             |
| `%C`   | `%{number}`         | Current newsgroup number                                             |
| `%d`   | `%{description}`    | Description of newsgroup (becomes from server)                       |
| `%f`   | `%{newsgroup}`      | Newsgroup name                                                       |
| `%M`   | `%{flags}`          | `-` if newsgroup not allowed for direct post (moderated for example) |
| `%N`   | `%{flags2}`         | `N` if newsgroup is new, `u` if unsubscribed, ` ` (space) otherwise  |
| `%n`   | `%{new-count}`      | Number of new articles in newsgroup                                  |
| `%p`   | `%{poll}`           | Poll: 1 if Mailbox is checked for new mail                           |
| `%s`   | `%{unread-count}`   | Number of unread articles in newsgroup                               |
| `%*X`  | `%{padding-soft:X}` | Soft-fill with character `X` as pad                                  |
| `%>X`  | `%{padding-hard:X}` | Right justify the rest of the string and pad with character `X`      |
| `%\|X` | `%{padding-eol:X}`  | Pad to the end of the line with character `X`                        |

--------------------------------------------------------------------------------

(mailbox-folder-format)=
## `$mailbox_folder_format`

- **Type:** expando
- **Notes:** Not empty
- **Default:**
    ```neomuttrc
    set mailbox_folder_format = "%2C %<n?%6n&      > %6m %i"
    ```

This variable allows you to customize the file browser display to your personal taste.
It's only used to customize network mailboxes (e.g. imap).
This string is identical in formatting to the one used by "$$folder_format".

--------------------------------------------------------------------------------

(mask)=
## `$mask`

- **Type:** regular expression
- **Notes:** Match Case, Allow Not, No Sub-match
- **Default:**
    ```neomuttrc
    set mask = "!^\\.[^.]"
    ```

A regular expression used in the file browser, optionally preceded by the _not_ operator "!".  Only files whose names match this mask will be shown.
The match is always case-sensitive.

--------------------------------------------------------------------------------

(show-only-unread)=
## `$show_only_unread`

- **Type:** boolean
- **Default:**
    ```neomuttrc
    set show_only_unread = no
    ```

If _set_, only subscribed newsgroups that contain unread articles will be displayed in browser.

