---
title: Notmuch Options
description: Config options for Notmuch integration, including database settings, tags, query windows, and virtual mailboxes.
keywords: notmuch, search, indexing, tagging, virtual mailbox, nm_default_url, nm_query_type, nm_exclude_tags, nm_unread_tag, vfolder, full-text search, email tags
---

(ref-cfg-notmuch)=
# Notmuch Options

(cfg-nm-config-file)=
## `$nm_config_file`

:Description: Configuration file for notmuch. Use `auto` to detect configuration.
:Type: [Path (String)](type-path)
:Notes: [File only](type-path)
:Default:
    ```neomuttrc
    set nm_config_file = "auto"
    ```

Configuration file for notmuch.
Use 'auto' to detect configuration.

--------------------------------------------------------------------------------

(cfg-nm-config-profile)=
## `$nm_config_profile`

:Description: Configuration profile for notmuch.
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set nm_config_profile = ""
    ```

Configuration profile for notmuch.

--------------------------------------------------------------------------------

(cfg-nm-db-limit)=
## `$nm_db_limit`

:Description: Default limit for Notmuch queries
:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set nm_db_limit = 0
    ```

This option specifies the default limit used in notmuch queries.

--------------------------------------------------------------------------------

(cfg-nm-default-url)=
## `$nm_default_url`

:Description: Path to the Notmuch database
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set nm_default_url = ""
    ```

This option specifies the default Notmuch database in format `notmuch://<absolute path>`

--------------------------------------------------------------------------------

(cfg-nm-exclude-tags)=
## `$nm_exclude_tags`

:Description: Exclude messages with these tags
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set nm_exclude_tags = ""
    ```

The messages tagged with these tags are excluded and not loaded from notmuch DB to NeoMutt unless specified explicitly.

--------------------------------------------------------------------------------

(cfg-nm-flagged-tag)=
## `$nm_flagged_tag`

:Description: Tag to use for flagged messages
:Type: [String](type-string)
:Notes: [Case Sensitive](type-general)
:Default:
    ```neomuttrc
    set nm_flagged_tag = "flagged"
    ```

This option specifies notmuch tag which is used for flagged messages.
The option is used to count flagged messages in DB and set the flagged flag when modifying tags.
All other NeoMutt commands use standard (e.g. maildir) flags.

--------------------------------------------------------------------------------

(cfg-nm-open-timeout)=
## `$nm_open_timeout`

:Description: Database timeout
:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set nm_open_timeout = 5
    ```

This option specifies the timeout for database open in seconds.

--------------------------------------------------------------------------------

(cfg-nm-query-type)=
## `$nm_query_type`

:Description: Default query type: `threads` or `messages`
:Type: [Enumeration](type-enum)
:Notes: [Case Sensitive](type-general)
:Default:
    ```neomuttrc
    set nm_query_type = messages
    ```

Default query type used in notmuch queries.

| Value      | Description                                    |
|------------|------------------------------------------------|
| `messages` | Only return matching messages                  |
| `threads`  | Return entire thread of every matching message |

--------------------------------------------------------------------------------

(cfg-nm-query-window-current-position)=
## `$nm_query_window_current_position`

:Description: Position of current search window
:Type: [Number](type-number)
:Default:
    ```neomuttrc
    set nm_query_window_current_position = 0
    ```

This option contains the position of the current search for window based vfolder.

--------------------------------------------------------------------------------

(cfg-nm-query-window-current-search)=
## `$nm_query_window_current_search`

:Description: Current search parameters
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set nm_query_window_current_search = ""
    ```

This option contains the currently setup notmuch search for window based vfolder.

--------------------------------------------------------------------------------

(cfg-nm-query-window-duration)=
## `$nm_query_window_duration`

:Description: Time duration of the current search window
:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set nm_query_window_duration = 0
    ```

This option sets the time duration of a windowed notmuch query.
Accepted values all non negative integers.
A value of 0 disables the feature.

--------------------------------------------------------------------------------

(cfg-nm-query-window-enable)=
## `$nm_query_window_enable`

:Description: Enable query windows
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set nm_query_window_enable = no
    ```

This option enables windowed notmuch queries even if window duration is 0.

--------------------------------------------------------------------------------

(cfg-nm-query-window-or-terms)=
## `$nm_query_window_or_terms`

:Description: Additional notmuch search terms for messages to be shown regardless of date
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set nm_query_window_or_terms = ""
    ```

This option contains additional notmuch search terms for messages to be shown regardless of date.

Example:

Using `notmuch://?query=tag:inbox` as the mailbox and `tag:flagged and tag:unread` as the or terms,
NeoMutt will produce a query window such as: `notmuch://?query=tag:inbox and (date:... or (tag:flagged and tag:unread))`

--------------------------------------------------------------------------------

(cfg-nm-query-window-timebase)=
## `$nm_query_window_timebase`

:Description: Units for the time duration
:Type: [Enumeration](type-enum)
:Notes: [Case Sensitive](type-general)
:Default:
    ```neomuttrc
    set nm_query_window_timebase = week
    ```

This option sets the time base of a windowed notmuch query.

| Accepted Values |
|-----------------|
| `hour`          |
| `day`           |
| `week`          |
| `month`         |
| `year`          |

--------------------------------------------------------------------------------

(cfg-nm-record-tags)=
## `$nm_record_tags`

:Description: Tags to apply to the [`$record`](cfg-record) mailbox (sent mail)
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set nm_record_tags = ""
    ```

This option specifies the notmuch tag modifications (addition, removal, toggling) applied to messages added to the NeoMutt record when [`$nm_record`](cfg-nm-record) is true.

:::{seealso}
[`<modify-labels>`](ref-fn-index) function for the syntax
:::

--------------------------------------------------------------------------------

(cfg-nm-replied-tag)=
## `$nm_replied_tag`

:Description: Tag to use for replied messages
:Type: [String](type-string)
:Notes: [Case Sensitive](type-general)
:Default:
    ```neomuttrc
    set nm_replied_tag = "replied"
    ```

This option specifies notmuch tag which is used for replied messages.
The option is used to set the replied flag when modifying tags.
All other NeoMutt commands use standard (e.g. maildir) flags.

--------------------------------------------------------------------------------

(cfg-nm-unread-tag)=
## `$nm_unread_tag`

:Description: Tag to use for unread messages
:Type: [String](type-string)
:Notes: [Case Sensitive](type-general)
:Default:
    ```neomuttrc
    set nm_unread_tag = "unread"
    ```

This option specifies notmuch tag which is used for unread messages.
The option is used to count unread messages in DB and set the unread flag when modifying tags.
All other NeoMutt commands use standard (e.g. maildir) flags.

--------------------------------------------------------------------------------

(cfg-virtual-spool-file)=
## `$virtual_spool_file`

:Description: Use the first virtual mailbox as a spool file
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set virtual_spool_file = no
    ```

When _set_, NeoMutt will use the first Notmuch virtual mailbox as a spool file.

