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


notmuch.md
	  { "nm_config_file", DT_PATH|D_PATH_FILE, IP "auto", 0, NULL,
	  { "nm_config_profile", DT_STRING, 0, 0, NULL,
	  { "nm_db_limit", DT_NUMBER|D_INTEGER_NOT_NEGATIVE, 0, 0, NULL,
	  { "nm_default_url", DT_STRING, 0, 0, nm_default_url_validator,
	  { "nm_exclude_tags", DT_STRING, 0, 0, NULL,
	  { "nm_flagged_tag", DT_STRING, IP "flagged", 0, NULL,
	  { "nm_open_timeout", DT_NUMBER|D_INTEGER_NOT_NEGATIVE, 5, 0, NULL,
	  { "nm_query_type", DT_STRING, IP "messages", 0, NULL,
	  { "nm_query_window_current_position", DT_NUMBER, 0, 0, NULL,
	  { "nm_query_window_current_search", DT_STRING, 0, 0, NULL,
	  { "nm_query_window_duration", DT_NUMBER|D_INTEGER_NOT_NEGATIVE, 0, 0, NULL,
	  { "nm_query_window_enable", DT_BOOL, false, 0, NULL,
	  { "nm_query_window_or_terms", DT_STRING, 0, 0, NULL,
	  { "nm_query_window_timebase", DT_STRING, IP "week", 0, nm_query_window_timebase_validator,
	  { "nm_record_tags", DT_STRING, 0, 0, NULL,
	  { "nm_replied_tag", DT_STRING, IP "replied", 0, NULL,
	  { "nm_unread_tag", DT_STRING, IP "unread", 0, NULL,
	  { "virtual_spool_file", DT_BOOL, false, 0, NULL,
	  { "vfolder_format",     D_INTERNAL_DEPRECATED|DT_STRING, 0,  IP "2018-11-01" },
	  { "nm_default_uri",     DT_SYNONYM, IP "nm_default_url",     IP "2021-02-11" },
	  { "virtual_spoolfile",  DT_SYNONYM, IP "virtual_spool_file", IP "2025-12-08" },

----------------------------------------------------------------------------------------------------------

(nm-config-file)=
## `$nm_config_file`

- **Type:** path
- **Default:** "`auto`"

Configuration file for notmuch. Use 'auto' to detect configuration.

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

This variable specifies the default Notmuch database in format
notmuch://<absolute path>.

----------------------------------------------------------------------------------------------------------

(nm-exclude-tags)=
## `$nm_exclude_tags`

- **Type:** string
- **Default:** (empty)

The messages tagged with these tags are excluded and not loaded
from notmuch DB to NeoMutt unless specified explicitly.

----------------------------------------------------------------------------------------------------------

(nm-flagged-tag)=
## `$nm_flagged_tag`

- **Type:** string
- **Default:** "`flagged`"

This variable specifies notmuch tag which is used for flagged messages. The
variable is used to count flagged messages in DB and set the flagged flag
when modifying tags. All other NeoMutt commands use standard (e.g. maildir)
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

This variable specifies the default query type (threads or messages) used in
notmuch queries.

----------------------------------------------------------------------------------------------------------

(nm-query-window-current-position)=
## `$nm_query_window_current_position`

- **Type:** number
- **Default:** 0

This variable contains the position of the current search for window based
vfolder.

----------------------------------------------------------------------------------------------------------

(nm-query-window-current-search)=
## `$nm_query_window_current_search`

- **Type:** string
- **Default:** (empty)

This variable contains the currently setup notmuch search for window based
vfolder.

----------------------------------------------------------------------------------------------------------

(nm-query-window-duration)=
## `$nm_query_window_duration`

- **Type:** number
- **Default:** 0

This variable sets the time duration of a windowed notmuch query.
Accepted values all non negative integers. A value of 0 disables the feature.

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

This variable contains additional notmuch search terms for messages to be
shown regardless of date.

Example:

Using "notmuch://?query=tag:inbox" as the mailbox and "tag:flagged and
tag:unread" as the or terms, NeoMutt will produce a query window such as:

notmuch://?query=tag:inbox and (date:... or (tag:flagged and tag:unread))

----------------------------------------------------------------------------------------------------------

(nm-query-window-timebase)=
## `$nm_query_window_timebase`

- **Type:** string
- **Default:** "`week`"

This variable sets the time base of a windowed notmuch query.
Accepted values are 'minute', 'hour', 'day', 'week', 'month', 'year'

----------------------------------------------------------------------------------------------------------

(nm-record-tags)=
## `$nm_record_tags`

- **Type:** string
- **Default:** (empty)

This variable specifies the notmuch tag modifications (addition, removal,
toggling) applied to messages added to the NeoMutt record when [`$nm_record`](#nm-record) is
true. See the description of the `<modify-labels>` function for the
syntax.

----------------------------------------------------------------------------------------------------------

(nm-replied-tag)=
## `$nm_replied_tag`

- **Type:** string
- **Default:** "`replied`"

This variable specifies notmuch tag which is used for replied messages. The
variable is used to set the replied flag when modifying tags. All other
NeoMutt commands use standard (e.g. maildir) flags.

----------------------------------------------------------------------------------------------------------

(nm-unread-tag)=
## `$nm_unread_tag`

- **Type:** string
- **Default:** "`unread`"

This variable specifies notmuch tag which is used for unread messages. The
variable is used to count unread messages in DB and set the unread flag when
modifying tags. All other NeoMutt commands use standard (e.g. maildir) flags.

----------------------------------------------------------------------------------------------------------

(virtual-spool-file)=
## `$virtual_spool_file`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will use the first Notmuch virtual mailbox as a
spool file.

