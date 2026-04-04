---
title: Notmuch Options
description: Configuration variables for Notmuch integration, including database settings, tags, query windows, and virtual mailboxes.
keywords: notmuch, search, indexing, tagging, virtual mailbox, nm_default_url, nm_query_type, nm_exclude_tags, nm_unread_tag, vfolder, full-text search, email tags
---

(ref-cfg-notmuch)=
# Notmuch Options

(cfg-nm-config-file)=
## `$nm_config_file`

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

:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set nm_config_profile = ""
    ```

Configuration profile for notmuch.

--------------------------------------------------------------------------------

(cfg-nm-db-limit)=
## `$nm_db_limit`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set nm_db_limit = 0
    ```

This variable specifies the default limit used in notmuch queries.

--------------------------------------------------------------------------------

(cfg-nm-default-url)=
## `$nm_default_url`

:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set nm_default_url = ""
    ```

This variable specifies the default Notmuch database in format notmuch://<absolute path>.

--------------------------------------------------------------------------------

(cfg-nm-exclude-tags)=
## `$nm_exclude_tags`

:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set nm_exclude_tags = ""
    ```

The messages tagged with these tags are excluded and not loaded from notmuch DB to NeoMutt unless specified explicitly.

--------------------------------------------------------------------------------

(cfg-nm-flagged-tag)=
## `$nm_flagged_tag`

:Type: [String](type-string)
:Notes: [Case Sensitive](type-general)
:Default:
    ```neomuttrc
    set nm_flagged_tag = "flagged"
    ```

This variable specifies notmuch tag which is used for flagged messages.
The variable is used to count flagged messages in DB and set the flagged flag when modifying tags.
All other NeoMutt commands use standard (e.g. maildir)
flags.

--------------------------------------------------------------------------------

(cfg-nm-open-timeout)=
## `$nm_open_timeout`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set nm_open_timeout = 5
    ```

This variable specifies the timeout for database open in seconds.

--------------------------------------------------------------------------------

(cfg-nm-query-type)=
## `$nm_query_type`

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

:Type: [Number](type-number)
:Default:
    ```neomuttrc
    set nm_query_window_current_position = 0
    ```

This variable contains the position of the current search for window based vfolder.

--------------------------------------------------------------------------------

(cfg-nm-query-window-current-search)=
## `$nm_query_window_current_search`

:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set nm_query_window_current_search = ""
    ```

This variable contains the currently setup notmuch search for window based vfolder.

--------------------------------------------------------------------------------

(cfg-nm-query-window-duration)=
## `$nm_query_window_duration`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set nm_query_window_duration = 0
    ```

This variable sets the time duration of a windowed notmuch query.
Accepted values all non negative integers.
A value of 0 disables the feature.

--------------------------------------------------------------------------------

(cfg-nm-query-window-enable)=
## `$nm_query_window_enable`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set nm_query_window_enable = no
    ```

This variable enables windowed notmuch queries even if window duration is 0.

--------------------------------------------------------------------------------

(cfg-nm-query-window-or-terms)=
## `$nm_query_window_or_terms`

:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set nm_query_window_or_terms = ""
    ```

This variable contains additional notmuch search terms for messages to be shown regardless of date.

Example:

Using "notmuch://?query=tag:inbox" as the mailbox and "tag:flagged and tag:unread" as the or terms, NeoMutt will produce a query window such as:

notmuch://?query=tag:inbox and (date:... or (tag:flagged and tag:unread))

--------------------------------------------------------------------------------

(cfg-nm-query-window-timebase)=
## `$nm_query_window_timebase`

:Type: [Enumeration](type-enum)
:Notes: [Case Sensitive](type-general)
:Default:
    ```neomuttrc
    set nm_query_window_timebase = week
    ```

This variable sets the time base of a windowed notmuch query.

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

:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set nm_record_tags = ""
    ```

This variable specifies the notmuch tag modifications (addition, removal, toggling) applied to messages added to the NeoMutt record when [`$nm_record`](cfg-nm-record) is true.
See the description of the [`<modify-labels>`](ref-fn-index) function for the syntax.

--------------------------------------------------------------------------------

(cfg-nm-replied-tag)=
## `$nm_replied_tag`

:Type: [String](type-string)
:Notes: [Case Sensitive](type-general)
:Default:
    ```neomuttrc
    set nm_replied_tag = "replied"
    ```

This variable specifies notmuch tag which is used for replied messages.
The variable is used to set the replied flag when modifying tags.
All other NeoMutt commands use standard (e.g. maildir) flags.

--------------------------------------------------------------------------------

(cfg-nm-unread-tag)=
## `$nm_unread_tag`

:Type: [String](type-string)
:Notes: [Case Sensitive](type-general)
:Default:
    ```neomuttrc
    set nm_unread_tag = "unread"
    ```

This variable specifies notmuch tag which is used for unread messages.
The variable is used to count unread messages in DB and set the unread flag when modifying tags.
All other NeoMutt commands use standard (e.g. maildir) flags.

--------------------------------------------------------------------------------

(cfg-virtual-spool-file)=
## `$virtual_spool_file`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set virtual_spool_file = no
    ```

When _set_, NeoMutt will use the first Notmuch virtual mailbox as a spool file.

