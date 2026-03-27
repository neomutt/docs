---
title: NNTP Options
description: Configuration variables for NNTP (Usenet) news server connections, newsgroup browsing, and article handling.
keywords: neomutt, nntp, usenet, newsgroups, news_server, newsrc, nntp_authenticators, nntp_poll, catchup_newsgroup, followup_to_poster, news reader, articles
---

(cfg-nntp)=
# NNTP Options

(catchup-newsgroup)=
## `$catchup_newsgroup`

:Type: [Quad-Option](quad)
:Default:
    ```neomuttrc
    set catchup_newsgroup = ask-yes
    ```

If this variable is _set_, NeoMutt will mark all articles in newsgroup as read when you quit the newsgroup (catchup newsgroup).

--------------------------------------------------------------------------------

(followup-to-poster)=
## `$followup_to_poster`

:Type: [Quad-Option](quad)
:Default:
    ```neomuttrc
    set followup_to_poster = ask-yes
    ```

If this variable is _set_ and the keyword "poster" is present in _Followup-To_ header, follow-up to newsgroup function is not permitted.
The message will be mailed to the submitter of the message via mail.

--------------------------------------------------------------------------------

(newsgroups-charset)=
## `$newsgroups_charset`

:Type: [String](string)
:Default:
    ```neomuttrc
    set newsgroups_charset = "utf-8"
    ```

Character set of newsgroups descriptions.

--------------------------------------------------------------------------------

(newsrc)=
## `$newsrc`

:Type: [Expando](expando)
:Notes: [File only](path)
:Default:
    ```neomuttrc
    set newsrc = "~/.newsrc"
    ```

The file, containing info about subscribed newsgroups - names and indexes of read articles.
The following printf-style sequence is understood:

| Short | Long Name     | Description       |
|-------|---------------|-------------------|
| `%a`  | `%{account}`  | Account url       |
| `%P`  | `%{port-if}`  | Port if specified |
| `%p`  | `%{port}`     | Port              |
| `%S`  | `%{schema}`   | Url schema        |
| `%s`  | `%{server}`   | News server name  |
| `%u`  | `%{username}` | Username          |

--------------------------------------------------------------------------------

(news-cache-dir)=
## `$news_cache_dir`

:Type: [Path (String)](path)
:Notes: [Directory only](path)
:Default:
    ```neomuttrc
    set news_cache_dir = "~/.neomutt"
    ```

This variable pointing to directory where NeoMutt will save cached news articles and headers in.
If _unset_, articles and headers will not be saved at all and will be reloaded from the server each time.

--------------------------------------------------------------------------------

(news-server)=
## `$news_server`

:Type: [String](string)
:Default: (empty)
    ```neomuttrc
    set news_server = ""
    ```

This variable specifies domain name or address of NNTP server.

You can also specify username and an alternative port for each news server, e.g. `[[s]news://][username[:password]@]server[:port]`

This option can also be set using the command line option "-g", the environment variable `$$$NNTPSERVER`, or putting the server name in the file "/etc/nntpserver".

--------------------------------------------------------------------------------

(nntp-authenticators)=
## `$nntp_authenticators`

:Type: [String](string)
:Default: (empty)
    ```neomuttrc
    set nntp_authenticators = ""
    ```

This is a colon-delimited list of authentication methods NeoMutt may attempt to use to log in to a news server, in the order NeoMutt should try them.
Authentication methods are either "user" or any SASL mechanism, e.g.
"digest-md5", "gssapi" or "cram-md5".
This option is case-insensitive.
If it's _unset_ (the default)
NeoMutt will try all available methods, in order from most-secure to least-secure.

Example:
```neomuttrc
set nntp_authenticators = "digest-md5:user" 
```

:::{note}
NeoMutt will only fall back to other authentication methods if the previous methods are unavailable.
If a method is available but authentication fails, NeoMutt will not connect to the IMAP server.
:::

--------------------------------------------------------------------------------

(nntp-context)=
## `$nntp_context`

:Type: [Number (Long)](long)
:Notes: {ref}`Not Negative <general>`
:Default:
    ```neomuttrc
    set nntp_context = 1000
    ```

This variable defines number of articles which will be in index when newsgroup entered.
If active newsgroup have more articles than this number, oldest articles will be ignored.
Also controls how many articles headers will be saved in cache when you quit newsgroup.

--------------------------------------------------------------------------------

(nntp-listgroup)=
## `$nntp_listgroup`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set nntp_listgroup = yes
    ```

This variable controls whether or not existence of each article is checked when newsgroup is entered.

--------------------------------------------------------------------------------

(nntp-load-description)=
## `$nntp_load_description`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set nntp_load_description = yes
    ```

This variable controls whether or not descriptions for each newsgroup must be loaded when newsgroup is added to list (first time list loading or new newsgroup adding).

--------------------------------------------------------------------------------

(nntp-pass)=
## `$nntp_pass`

:Type: [String](string)
:Notes: {ref}`Sensitive <general>`
:Default: (empty)
    ```neomuttrc
    set nntp_pass = ""
    ```

Your password for NNTP account.

--------------------------------------------------------------------------------

(nntp-poll)=
## `$nntp_poll`

:Type: [Number](number)
:Notes: {ref}`Not Negative <general>`
:Default:
    ```neomuttrc
    set nntp_poll = 60
    ```

The time in seconds until any operations on newsgroup except post new article will cause recheck for new news.
If set to 0, NeoMutt will recheck newsgroup on each operation in index (stepping, read article, etc.).

--------------------------------------------------------------------------------

(nntp-user)=
## `$nntp_user`

:Type: [String](string)
:Notes: {ref}`Sensitive <general>`
:Default: (empty)
    ```neomuttrc
    set nntp_user = ""
    ```

Your login name on the NNTP server.
If _unset_ and NNTP server requires authentication, NeoMutt will prompt you for your account name when you connect to news server.

--------------------------------------------------------------------------------

(post-moderated)=
## `$post_moderated`

:Type: [Quad-Option](quad)
:Default:
    ```neomuttrc
    set post_moderated = ask-yes
    ```

If set to _yes_, NeoMutt will post article to newsgroup that have not permissions to posting (e.g. moderated).

:::{note}
If news server does not support posting to that newsgroup or totally read-only, that posting will not have an effect.
:::

--------------------------------------------------------------------------------

(save-unsubscribed)=
## `$save_unsubscribed`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set save_unsubscribed = no
    ```

When _set_, info about unsubscribed newsgroups will be saved into "newsrc" file and into cache.

--------------------------------------------------------------------------------

(show-new-news)=
## `$show_new_news`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set show_new_news = yes
    ```

If _set_, news server will be asked for new newsgroups on entering the browser.
Otherwise, it will be done only once for a news server.
Also controls whether or not number of new articles of subscribed newsgroups will be then checked.

--------------------------------------------------------------------------------

(x-comment-to)=
## `$x_comment_to`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set x_comment_to = no
    ```

If _set_, NeoMutt will add "X-Comment-To:" field (that contains full name of original article author) to article that followuped to newsgroup.

