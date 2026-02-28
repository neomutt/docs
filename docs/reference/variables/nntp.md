---
title: NNTP Variables
description: NNTP (Usenet) protocol configuration variables for NeoMutt
keywords: nntp_authenticators, nntp_context, nntp_listgroup, nntp_load_description, nntp_pass, nntp_poll, nntp_user
---

# NNTP Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

## `$nntp_authenticators`

- **Type:** string
- **Default:** (empty)

This is a colon-delimited list of authentication methods NeoMutt may
attempt to use to log in to a news server, in the order NeoMutt should
try them.  Authentication methods are either "user" or any
SASL mechanism, e.g. "digest-md5", "gssapi" or "cram-md5".
This option is case-insensitive.  If it's *unset* (the default)
NeoMutt will try all available methods, in order from most-secure to
least-secure.

Example:


```
set nntp_authenticators="digest-md5:user"
```


**Note:** NeoMutt will only fall back to other authentication methods if
the previous methods are unavailable. If a method is available but
authentication fails, NeoMutt will not connect to the IMAP server.

## `$nntp_context`

- **Type:** number (long)
- **Default:** 1000

This variable defines number of articles which will be in index when
newsgroup entered.  If active newsgroup have more articles than this
number, oldest articles will be ignored.  Also controls how many
articles headers will be saved in cache when you quit newsgroup.

## `$nntp_listgroup`

- **Type:** boolean
- **Default:** yes

This variable controls whether or not existence of each article is
checked when newsgroup is entered.

## `$nntp_load_description`

- **Type:** boolean
- **Default:** yes

This variable controls whether or not descriptions for each newsgroup
must be loaded when newsgroup is added to list (first time list
loading or new newsgroup adding).

## `$nntp_pass`

- **Type:** string
- **Default:** (empty)

Your password for NNTP account.

## `$nntp_poll`

- **Type:** number
- **Default:** 60

The time in seconds until any operations on newsgroup except post new
article will cause recheck for new news.  If set to 0, NeoMutt will
recheck newsgroup on each operation in index (stepping, read article,
etc.).

## `$nntp_user`

- **Type:** string
- **Default:** (empty)

Your login name on the NNTP server.  If *unset* and NNTP server requires
authentication, NeoMutt will prompt you for your account name when you
connect to news server.
