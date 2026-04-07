---
title: Browser Options
description: Config options for the file and mailbox browser display, sorting, formatting, and newsgroup listing.
keywords: neomutt, browser, file browser, folder_format, browser_sort, browser_sort_dirs_first, mask, group_index_format, mailbox_folder_format, directory listing, newsgroup browser
---

(ref-cfg-browser)=
# Browser Options

(cfg-browser-abbreviate-mailboxes)=
## `$browser_abbreviate_mailboxes`

:Description: Abbreviate mailboxes using `~` and `=` in the browser
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set browser_abbreviate_mailboxes = yes
    ```

When this option is _set_, NeoMutt will abbreviate mailbox names in the browser mailbox list, using `~` and `=` shortcuts.

The default `alpha` setting of [`$browser_sort`](cfg-browser-sort) uses locale-based sorting (using [`strcoll(3)`](https://man7.org/linux/man-pages/man3/strcoll.3.html)), which ignores some punctuation.
This can lead to some situations where the order doesn't make intuitive sense.
In those cases, it may be desirable to _unset_ this option.

--------------------------------------------------------------------------------

(cfg-browser-sort)=
## `$browser_sort`

:Description: Sort method for the browser
:Type: [Sort Order](type-sort-order)
:Notes: [Reverse](type-sort-order)
:Default:
    ```neomuttrc
    set browser_sort = alpha
    ```

Specifies how to sort entries in the file browser.

| Value      | Sort by               |
|------------|-----------------------|
| `alpha`    | Name                  |
| `count`    | Total message count   |
| `date`     | Date                  |
| `desc`     | Description           |
| `size`     | Size                  |
| `new`      | Count of new messages |
| `unsorted` | Unsorted              |

| Deprecated Value | Use this instead |
|------------------|------------------|
| `unread`         | `new`            |

--------------------------------------------------------------------------------

(cfg-browser-sort-dirs-first)=
## `$browser_sort_dirs_first`

:Description: Group directories before files in the browser
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set browser_sort_dirs_first = no
    ```

If this option is _set_, the browser will group directories before files.

--------------------------------------------------------------------------------

(cfg-folder-format)=
## `$folder_format`

:Description: Format string for the [Browser Dialog](tour-browser)'s display of folders
:Type: [Expando](type-expando)
:Notes: [Not Empty](type-general), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set folder_format = "%2C %t %N %F %2l %-8.8u %-8.8g %8s %d %i"
    ```
:Alternative:
    ```neomuttrc
    set folder_format = "%2{number} %{tagged} %{new-mail} %{file-mode} %2{hard-links} %-8.8{file-owner} %-8.8{file-group} %8{file-size} %{date} %{description}"
    ```

Specify the format of local files/dirs displayed in the [`Browser Dialog`](tour-browser).

**Format Sequences**

| Short    | Long Name           | Description                                                                                               |
|----------|---------------------|-----------------------------------------------------------------------------------------------------------|
| `%a`     | `%{notify}`         | Alert: 1 if user is notified of new mail                                                                  |
| `%C`     | `%{number}`         | Current file number                                                                                       |
| `%D`     | `%{date}`           | Date/time folder was last modified using [`$date_format`](cfg-date-format).                               |
|          |                     | It is recommended to use `%[fmt]` instead, where `fmt` is the value of [`$date_format`](cfg-date-format). |
| `%d`     | `%{date-format}`    | Date/time folder was last modified                                                                        |
| `%F`     | `%{file-mode}`      | File permissions                                                                                          |
| `%f`     | `%{filename}`       | Filename (`/` is appended to directory names, `@` to symbolic links and `*` to executable files)          |
| `%g`     | `%{file-group}`     | Group name (or numeric gid, if missing)                                                                   |
| `%i`     | `%{description}`    | Description of the folder                                                                                 |
| `%l`     | `%{hard-links}`     | Number of hard links                                                                                      |
| `%m`     | `%{message-count}`  | Number of messages in the mailbox                                                                         |
| `%N`     | `%{new-mail}`       | `N` if mailbox has new mail, ` ` (space) otherwise                                                        |
| `%n`     | `%{unread-count}`   | Number of unread messages in the mailbox                                                                  |
| `%p`     | `%{poll}`           | Poll: 1 if Mailbox is checked for new mail                                                                |
| `%s`     | `%{file-size}`      | Size in bytes (see {ref}`how-bytes-size`)                                                                 |
| `%t`     | `%{tagged}`         | `*` if the file is tagged, blank otherwise                                                                |
| `%u`     | `%{file-owner}`     | Owner name (or numeric uid, if missing)                                                                   |
| `%[fmt]` |                     | Date/time folder was last modified using an [`strftime(3)`](exp-strftime) expression                      |
| `%*X`    | `%{padding-soft:X}` | Soft-fill with character `X` as pad                                                                       |
| `%>X`    | `%{padding-hard:X}` | Right justify the rest of the string and pad with character `X`                                           |
| `%\|X`   | `%{padding-eol:X}`  | Pad to the end of the line with character `X`                                                             |

`%m`, `%n`, and `%N` only work for monitored mailboxes.
`%m` requires [`$mail_check_stats`](cfg-mail-check-stats) to be set.
`%n` requires [`$mail_check_stats`](cfg-mail-check-stats) to be set (except for IMAP mailboxes).

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-group-index-format)=
## `$group_index_format`

:Description: Format string for the [Browser Dialog](tour-browser)'s display of newsgroups
:Type: [Expando](type-expando)
:Notes: [Not Empty](type-general), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set group_index_format = "%4C %M%N %5s  %-45.45f %d"
    ```
:Alternative:
    ```neomuttrc
    set group_index_format = "%4{number} %{flags}%{flags2} %5{unread-count}  %-45.45{newsgroup} %{description}"
    ```

Specify the format of newsgroups displayed in the [`Browser Dialog`](tour-browser).

**Format Sequences**

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

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-mailbox-folder-format)=
## `$mailbox_folder_format`

:Description: Format string for the [Browser Dialog](tour-browser)'s display of mailbox folders
:Type: [Expando](type-expando)
:Notes: [Not Empty](type-general), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set mailbox_folder_format = "%2C %<n?%6n&      > %6m %i"
    ```
:Alternative:
    ```neomuttrc
    set mailbox_folder_format = "%2{number} %<n?%6{unread-count}&      > %6{message-count} %{description}"
    ```

Specify the format of network mailboxes, e.g. IMAP, displayed in the [`Browser Dialog`](tour-browser).

:::{seealso}
- [`$folder_format`](cfg-folder-format) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-mask)=
## `$mask`

:Description: Only display files/dirs matching this regex in the browser
:Type: [Regular Expression](type-regex)
:Notes: [Case Sensitive](type-general), [Match Case](type-regex), [Allow Not](type-regex), [No Sub](type-regex)
:Default:
    ```neomuttrc
    set mask = "!^\\.[^.]"
    ```

A regular expression used in the file browser, optionally preceded by the _not_ operator `!`.
Only files whose names match this mask will be shown.

--------------------------------------------------------------------------------

(cfg-show-only-unread)=
## `$show_only_unread`

:Description: Only show subscribed newsgroups with unread articles
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set show_only_unread = no
    ```

If _set_, only subscribed newsgroups that contain unread articles will be displayed in browser.

