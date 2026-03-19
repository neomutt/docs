---
title: NNTP Options
description: NNTP (Usenet) protocol configuration variables for NeoMutt
keywords: nntp_authenticators, nntp_context, nntp_listgroup, nntp_load_description, nntp_pass, nntp_poll, nntp_user
---

# NNTP Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::


nntp.md
	  { "catchup_newsgroup", DT_QUAD, MUTT_ASKYES, 0, NULL,
	  { "followup_to_poster", DT_QUAD, MUTT_ASKYES, 0, NULL,
	  { "newsgroups_charset", DT_STRING, IP "utf-8", 0, charset_validator,
	  { "newsrc", DT_EXPANDO|D_PATH_FILE, IP "~/.newsrc", IP &NntpFormatDef, NULL,
	  { "news_cache_dir", DT_PATH|D_PATH_DIR, IP "~/.neomutt", 0, NULL,
	  { "news_server", DT_STRING, 0, 0, NULL,
	  { "nntp_authenticators", DT_STRING, 0, 0, NULL,
	  { "nntp_context", DT_LONG|D_INTEGER_NOT_NEGATIVE, 1000, 0, NULL,
	  { "nntp_listgroup", DT_BOOL, true, 0, NULL,
	  { "nntp_load_description", DT_BOOL, true, 0, NULL,
	  { "nntp_pass", DT_STRING|D_SENSITIVE, 0, 0, NULL,
	  { "nntp_poll", DT_NUMBER|D_INTEGER_NOT_NEGATIVE, 60, 0, NULL,
	  { "nntp_user", DT_STRING|D_SENSITIVE, 0, 0, NULL,
	  { "post_moderated", DT_QUAD, MUTT_ASKYES, 0, NULL,
	  { "save_unsubscribed", DT_BOOL, false, 0, NULL,
	  { "show_new_news", DT_BOOL, true, 0, NULL,
	  { "x_comment_to", DT_BOOL, false, 0, NULL,

----------------------------------------------------------------------------------------------------------

(catchup-newsgroup)=
## `$catchup_newsgroup`

- **Type:** quadoption
- **Default:** ask-yes

If this variable is *set*, NeoMutt will mark all articles in newsgroup
as read when you quit the newsgroup (catchup newsgroup).

----------------------------------------------------------------------------------------------------------

(followup-to-poster)=
## `$followup_to_poster`

- **Type:** quadoption
- **Default:** ask-yes

If this variable is *set* and the keyword "poster" is present in
*Followup-To* header, follow-up to newsgroup function is not
permitted.  The message will be mailed to the submitter of the
message via mail.

----------------------------------------------------------------------------------------------------------

(newsgroups-charset)=
## `$newsgroups_charset`

- **Type:** string
- **Default:** "`utf-8`"

Character set of newsgroups descriptions.

----------------------------------------------------------------------------------------------------------

(newsrc)=
## `$newsrc`

- **Type:** path
- **Default:** "`~/.newsrc`"

The file, containing info about subscribed newsgroups - names and
indexes of read articles.  The following printf-style sequence
is understood:

| Short | Long Name     | Description       |
|-------|---------------|------------------|
| `%a` | `%{account}`  | Account url       |
| `%P` | `%{port-if}`  | Port if specified |
| `%p` | `%{port}`     | Port              |
| `%S` | `%{schema}`   | Url schema        |
| `%s` | `%{server}`   | News server name  |
| `%u` | `%{username}` | Username          |

----------------------------------------------------------------------------------------------------------

(news-cache-dir)=
## `$news_cache_dir`

- **Type:** path
- **Default:** "`~/.neomutt`"

This variable pointing to directory where NeoMutt will save cached news
articles and headers in. If *unset*, articles and headers will not be
saved at all and will be reloaded from the server each time.

----------------------------------------------------------------------------------------------------------

(news-server)=
## `$news_server`

- **Type:** string
- **Default:** (empty)

This variable specifies domain name or address of NNTP server.

You can also specify username and an alternative port for each news server,
e.g. `[[s]news://][username[:password]@]server[:port]`

This option can also be set using the command line option "-g", the
environment variable `$NNTPSERVER`, or putting the server name in the
file "/etc/nntpserver".

----------------------------------------------------------------------------------------------------------

(nntp-authenticators)=
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

```neomuttrc
set nntp_authenticators="digest-md5:user"
```

**Note:** NeoMutt will only fall back to other authentication methods if
the previous methods are unavailable. If a method is available but
authentication fails, NeoMutt will not connect to the IMAP server.

----------------------------------------------------------------------------------------------------------

(nntp-context)=
## `$nntp_context`

- **Type:** number (long)
- **Default:** 1000

This variable defines number of articles which will be in index when
newsgroup entered.  If active newsgroup have more articles than this
number, oldest articles will be ignored.  Also controls how many
articles headers will be saved in cache when you quit newsgroup.

----------------------------------------------------------------------------------------------------------

(nntp-listgroup)=
## `$nntp_listgroup`

- **Type:** boolean
- **Default:** yes

This variable controls whether or not existence of each article is
checked when newsgroup is entered.

----------------------------------------------------------------------------------------------------------

(nntp-load-description)=
## `$nntp_load_description`

- **Type:** boolean
- **Default:** yes

This variable controls whether or not descriptions for each newsgroup
must be loaded when newsgroup is added to list (first time list
loading or new newsgroup adding).

----------------------------------------------------------------------------------------------------------

(nntp-pass)=
## `$nntp_pass`

- **Type:** string
- **Default:** (empty)

Your password for NNTP account.

----------------------------------------------------------------------------------------------------------

(nntp-poll)=
## `$nntp_poll`

- **Type:** number
- **Default:** 60

The time in seconds until any operations on newsgroup except post new
article will cause recheck for new news.  If set to 0, NeoMutt will
recheck newsgroup on each operation in index (stepping, read article,
etc.).

----------------------------------------------------------------------------------------------------------

(nntp-user)=
## `$nntp_user`

- **Type:** string
- **Default:** (empty)

Your login name on the NNTP server.  If *unset* and NNTP server requires
authentication, NeoMutt will prompt you for your account name when you
connect to news server.

----------------------------------------------------------------------------------------------------------

(post-moderated)=
## `$post_moderated`

- **Type:** quadoption
- **Default:** ask-yes

If set to *yes*, NeoMutt will post article to newsgroup that have
not permissions to posting (e.g. moderated).  **Note:** if news server
does not support posting to that newsgroup or totally read-only, that
posting will not have an effect.

----------------------------------------------------------------------------------------------------------

(save-unsubscribed)=
## `$save_unsubscribed`

- **Type:** boolean
- **Default:** no

When *set*, info about unsubscribed newsgroups will be saved into
"newsrc" file and into cache.

----------------------------------------------------------------------------------------------------------

(show-new-news)=
## `$show_new_news`

- **Type:** boolean
- **Default:** yes

If *set*, news server will be asked for new newsgroups on entering
the browser.  Otherwise, it will be done only once for a news server.
Also controls whether or not number of new articles of subscribed
newsgroups will be then checked.

----------------------------------------------------------------------------------------------------------

(x-comment-to)=
## `$x_comment_to`

- **Type:** boolean
- **Default:** no

If *set*, NeoMutt will add "X-Comment-To:" field (that contains full
name of original article author) to article that followuped to newsgroup.

