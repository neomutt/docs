---
title: "Notmuch Options"
description: "Reference for NeoMutt Notmuch integration configuration variables."
keywords: "notmuch, search, indexing, variables, neomutt"
---

# Notmuch Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::



----------------------------------------------------------------------------------------------------------

(nm-config-file)=
## `$nm_config_file`

- **Type:** path
- **Default:** "`auto`"

Configuration file for notmuch.
Use 'auto' to detect configuration.

----------------------------------------------------------------------------------------------------------

(nm-config-profile)=
## `$nm_config_profile`

- **Type:** string
- **Default:** (empty)

Configuration profile for notmuch.

----------------------------------------------------------------------------------------------------------

(nm-db-limit)=
## `$nm_db_limit`

- **Type:** number
- **Default:** 0

This variable specifies the default limit used in notmuch queries.

----------------------------------------------------------------------------------------------------------

(nm-default-url)=
## `$nm_default_url`

- **Type:** string
- **Default:** (empty)

This variable specifies the default Notmuch database in format notmuch://<absolute path>.

----------------------------------------------------------------------------------------------------------

(nm-exclude-tags)=
## `$nm_exclude_tags`

- **Type:** string
- **Default:** (empty)

The messages tagged with these tags are excluded and not loaded from notmuch DB to NeoMutt unless specified explicitly.

----------------------------------------------------------------------------------------------------------

(nm-flagged-tag)=
## `$nm_flagged_tag`

- **Type:** string
- **Default:** "`flagged`"

This variable specifies notmuch tag which is used for flagged messages.
The variable is used to count flagged messages in DB and set the flagged flag when modifying tags.
All other NeoMutt commands use standard (e.g. maildir)
flags.

----------------------------------------------------------------------------------------------------------

(nm-open-timeout)=
## `$nm_open_timeout`

- **Type:** number
- **Default:** 5

This variable specifies the timeout for database open in seconds.

----------------------------------------------------------------------------------------------------------

(nm-query-type)=
## `$nm_query_type`

- **Type:** string
- **Default:** "`messages`"

This variable specifies the default query type (threads or messages) used in notmuch queries.

----------------------------------------------------------------------------------------------------------

(nm-query-window-current-position)=
## `$nm_query_window_current_position`

- **Type:** number
- **Default:** 0

This variable contains the position of the current search for window based vfolder.

----------------------------------------------------------------------------------------------------------

(nm-query-window-current-search)=
## `$nm_query_window_current_search`

- **Type:** string
- **Default:** (empty)

This variable contains the currently setup notmuch search for window based vfolder.

----------------------------------------------------------------------------------------------------------

(nm-query-window-duration)=
## `$nm_query_window_duration`

- **Type:** number
- **Default:** 0

This variable sets the time duration of a windowed notmuch query.
Accepted values all non negative integers.
A value of 0 disables the feature.

----------------------------------------------------------------------------------------------------------

(nm-query-window-enable)=
## `$nm_query_window_enable`

- **Type:** boolean
- **Default:** no

This variable enables windowed notmuch queries even if window duration is 0.

----------------------------------------------------------------------------------------------------------

(nm-query-window-or-terms)=
## `$nm_query_window_or_terms`

- **Type:** string
- **Default:** (empty)

This variable contains additional notmuch search terms for messages to be shown regardless of date.

Example:

Using "notmuch://?query=tag:inbox" as the mailbox and "tag:flagged and tag:unread" as the or terms, NeoMutt will produce a query window such as:

notmuch://?query=tag:inbox and (date:... or (tag:flagged and tag:unread))

----------------------------------------------------------------------------------------------------------

(nm-query-window-timebase)=
## `$nm_query_window_timebase`

- **Type:** string
- **Default:** "`week`"

This variable sets the time base of a windowed notmuch query.
Accepted values are 'minute', 'hour', 'day', 'week', 'month', 'year'.

----------------------------------------------------------------------------------------------------------

(nm-record-tags)=
## `$nm_record_tags`

- **Type:** string
- **Default:** (empty)

This variable specifies the notmuch tag modifications (addition, removal, toggling) applied to messages added to the NeoMutt record when $$nm_record is true.
See the description of the `<modify-labels>` function for the syntax.

----------------------------------------------------------------------------------------------------------

(nm-replied-tag)=
## `$nm_replied_tag`

- **Type:** string
- **Default:** "`replied`"

This variable specifies notmuch tag which is used for replied messages.
The variable is used to set the replied flag when modifying tags.
All other NeoMutt commands use standard (e.g. maildir) flags.

----------------------------------------------------------------------------------------------------------

(nm-unread-tag)=
## `$nm_unread_tag`

- **Type:** string
- **Default:** "`unread`"

This variable specifies notmuch tag which is used for unread messages.
The variable is used to count unread messages in DB and set the unread flag when modifying tags.
All other NeoMutt commands use standard (e.g. maildir) flags.

----------------------------------------------------------------------------------------------------------

(virtual-spool-file)=
## `$virtual_spool_file`

- **Type:** boolean
- **Default:** no

When _set_, NeoMutt will use the first Notmuch virtual mailbox as a spool file.

