---
title: Notmuch
description: Set up Notmuch integration in NeoMutt for full-text email search, virtual folders, tagging, and windowed queries.
keywords: notmuch, search, virtual folder, vfolder, tagging, indexing, full-text search, query, nm_default_url, nm_query_type, nm_query_window, change-vfolder, vfolder-from-query, xapian
---

# Notmuch

## Support

**Dependencies:** Notmuch libraries

## Introduction

Notmuch is an email fulltext indexing and tagging engine.

- For more information, see: [https://notmuchmail.org/](https://notmuchmail.org/)
- More examples: [https://notmuchmail.org/mutttips/](https://notmuchmail.org/mutttips/)

## Using Notmuch

### Folders URL

**notmuch://[\<path\>][?\<item\>=\<name\>[& ...]]**

The \<path\> is an absolute path to the directory where the notmuch database is found as returned by `notmuch config get database.path` command.
Note that the \<path\> should NOT include `.notmuch` directory name.

If the "\<path\>" is not defined then [`$nm_default_url`](cfg-nm-default-url) or [`$folder`](cfg-folder) is used, for example:

```neomuttrc
set nm_default_url = "notmuch:///home/foo/maildir"
named-mailboxes "My INBOX" "notmuch://?query=tag:inbox"
```

### Items

**query=\<string\>**

See SEARCH SYNTAX in notmuch man page.
Don't forget to use operators ("and"/"or") in your queries.

Note that proper URL should not contain blank space and all "bad" chars should be encoded, for example

`tag:AAA and tag:BBB` – encoding -> `tag:AAA%20and%20tag:BBB`

but NeoMutt config file parser is smart enough to accept space in quoted strings.
It means that you can use

`notmuch:///foo?query=tag:AAA and tag:BBB`

in your config files to keep things readable.

For more details about Xapian queries, see: [https://xapian.org/docs/queryparser.html](https://xapian.org/docs/queryparser.html)

**limit=\<number\>**

Restricts number of messages/threads in the result.
The default limit is nm_db_limit.

Due to a limitation with `libnotmuch`, unread and flagged message count may be inaccurate with limit statements
`libnotmuch` cannot return a specific tag count within the first X messages of a query.

**type=\<threads|messages\>**

Reads all matching messages or whole-threads.
The default is 'messages' or nm_query_type.

## Variables

| Name                               | Type    | Default    | Note                                                                                                                                                                                                                                                                                 |
|------------------------------------|---------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `nm_config_file`                   | path    | `auto`     | Configuration file for the notmuch database. Either a path, `auto` for detecting a config. file, or empty for no configuration file. Only useful for notmuch 0.32+.                                                                                                                  |
| `nm_config_profile`                | string  | (empty)    | Configuration profile for the notmuch database. Only useful for notmuch 0.32+.                                                                                                                                                                                                       |
| `nm_db_limit`                      | number  | `0`        |                                                                                                                                                                                                                                                                                      |
| `nm_default_url`                   | string  | (empty)    | Must use format: `notmuch://<absolute path>`                                                                                                                                                                                                                                         |
| `nm_exclude_tags`                  | string  | (empty)    |                                                                                                                                                                                                                                                                                      |
| `nm_flagged_tag`                   | string  | `flagged`  |                                                                                                                                                                                                                                                                                      |
| `nm_open_timeout`                  | number  | `5`        |                                                                                                                                                                                                                                                                                      |
| `nm_query_type`                    | string  | `messages` |                                                                                                                                                                                                                                                                                      |
| `nm_query_window_current_position` | number  | `0`        | Position of current search window                                                                                                                                                                                                                                                    |
| `nm_query_window_current_search`   | string  | (empty)    | Current search parameters                                                                                                                                                                                                                                                            |
| `nm_query_window_duration`         | number  | `0`        | Duration between start and end dates for windowed notmuch query. This corresponds to a bounded notmuch `date:` query. See `notmuch-search-terms` manual page for more info. Value of `0` disables windowed queries unless `nm_query_window_enable=yes`                               |
| `nm_query_window_enable`           | boolean | `no`       | Enables windowed notmuch queries for `nm_query_window_duration = 0`                                                                                                                                                                                                                  |
| `nm_query_window_or_terms`         | string  | (empty)    | Additional notmuch search terms to always include in the window even if they're outside the date range. This turns the window from `date:...` to `date:... or (additional search terms.)` For example, to always include flagged, unread emails, set to `tag:flagged and tag:unread` |
| `nm_query_window_timebase`         | string  | `week`     | Time base for windowed notmuch queries. Must be one of: `hour`, `day`, `week`, `month`, or `year`                                                                                                                                                                                    |
| `nm_record`                        | boolean | `no`       |                                                                                                                                                                                                                                                                                      |
| `nm_record_tags`                   | string  | (empty)    |                                                                                                                                                                                                                                                                                      |
| `nm_unread_tag`                    | string  | `unread`   |                                                                                                                                                                                                                                                                                      |

More variables about tags configuration can be found in **Custom backend Tags Feature**.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Notmuch virtual mailbox view

**Description:** The NeoMutt index showing a virtual folder created from a
Notmuch query (e.g. `tag:inbox`), with the status bar displaying the Notmuch query URL.
Messages from different underlying Maildir folders should be visible together in one unified view.

**Highlights:** How messages from multiple folders are merged into a single virtual view, the Notmuch query shown in the status bar, and the message count reflecting query results rather than a physical folder.
:::

## Functions

Notmuch adds the following functions to NeoMutt.
By default, none of them are bound to keys.

| Menus       | Function                        | Description                                                                                                                                                             |
|-------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| index,pager | `<change-vfolder>`              | Switch to another virtual folder, a new folder maybe be specified by vfolder description (see named-mailboxes) or URL. the default is next vfolder with unread messages |
| index,pager | `<entire-thread>`               | Read entire thread of the current message                                                                                                                               |
| index,pager | `<vfolder-from-query>`          | Generate virtual folder from notmuch search query. Note: TAB completion of 'tag:' names is available.                                                                   |
| index,pager | `<vfolder-from-query-readonly>` | The same as `<vfolder-from-query>`; however, the mailbox will be read-only.                                                                                             |
| index       | `<vfolder-window-forward>`      | Generate virtual folder by moving the query's time window forward                                                                                                       |
| index       | `<vfolder-window-backward>`     | Generate virtual folder by moving the query's time window backward                                                                                                      |
| index       | `<vfolder-window-reset>`        | Generate virtual folder by moving the query's time window to the present                                                                                                |

More functions about tags can be found in **Custom backend Tags Feature**.

## Colors

See **Custom backend Tags colors**.

## neomuttrc

```neomuttrc
# Example NeoMutt config file for the notmuch feature.

# --------------------------------------------------------------------------
# VARIABLES – shown with their default values
# --------------------------------------------------------------------------
# This variable specifies notmuch query limit.
set nm_db_limit = 0
# This variable specifies the default Notmuch database in format:
# notmuch://<absolute path>
set nm_default_url = ""
# The messages tagged with these tags are excluded and not loaded
# from notmuch DB to NeoMutt unless specified explicitly.
set nm_exclude_tags = ""
# This option specifies timeout for Notmuch database. Default is 5 seconds.
set nm_open_timeout = 5
# This variable specifies notmuch query type, supported types: 'threads' and
# 'messages'.
set nm_query_type = messages
# When writing a message in the NeoMutt record (see $record in the NeoMutt docs),
# also add it to the notmuch DB. Replies inherit the tags from the original email.
set nm_record = no
# Tags modifications to the messages stored in the NeoMutt record.
# example:
#   set record = "~/sent-mails"
#   set nm_record = yes
#   set nm_record_tags = "-inbox,archive,me"
set nm_record_tags = ""
# This variable specifies the notmuch tag used for unread messages.
set nm_unread_tag = unread
# setup time window preferences
# first setup the duration, and then the time unit of that duration
# when set to 0 (the default) the search window feature is disabled
# unless explicitly enabled with nm_query_window_enable.
set nm_query_window_enable = yes
set nm_query_window_duration = 2
set nm_query_window_timebase = "week" # or "hour", "day", "week", "month", "year"
# Extend query window to always show mail matching these terms.
set nm_query_window_or_terms = "tag:unread and tag:flagged"
# --------------------------------------------------------------------------
# FUNCTIONS – shown with an example mapping
# --------------------------------------------------------------------------
# Open a different virtual folder
bind index,pager X change-vfolder
# Read entire thread of the current message
bind index,pager + entire-thread
# Generate virtual folder from query
bind index,pager \eX vfolder-from-query
# Generate virtual folder from query with time window
bind index '<' vfolder-window-backward
bind index '>' vfolder-window-forward
# --------------------------------------------------------------------------

# vim: filetype=neomuttrc
```

## See Also

- **Compile-Time Features**

