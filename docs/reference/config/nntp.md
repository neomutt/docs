---
title: NNTP Options
description: Config options for NNTP (Usenet) news server connections, newsgroup browsing, and article handling.
keywords: neomutt, nntp, usenet, newsgroups, news_server, newsrc, nntp_authenticators, nntp_poll, catchup_newsgroup, followup_to_poster, news reader, articles
---

(ref-cfg-nntp)=
# NNTP Options

(cfg-catchup-newsgroup)=
## `$catchup_newsgroup`

:Description: Mark all articles as read when leaving a newsgroup
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set catchup_newsgroup = ask-yes
    ```

If this option is _set_, NeoMutt will mark all articles in newsgroup as read when you quit the newsgroup (catchup newsgroup).

--------------------------------------------------------------------------------

(cfg-followup-to-poster)=
## `$followup_to_poster`

:Description: Reply to the poster if "poster" is in the `Followup-To` header
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set followup_to_poster = ask-yes
    ```

If this option is _set_ and the keyword "poster" is present in `Followup-To:` header, follow-up to newsgroup function is not permitted.
The message will be mailed to the submitter of the message via mail.

--------------------------------------------------------------------------------

(cfg-newsgroups-charset)=
## `$newsgroups_charset`

:Description: Character set of newsgroups' descriptions
:Type: [String](type-string)
:Default:
    ```neomuttrc
    set newsgroups_charset = "utf-8"
    ```

Character set of newsgroups descriptions.

--------------------------------------------------------------------------------

(cfg-newsrc)=
## `$newsrc`

:Description: File containing list of subscribed newsgroups
:Type: [Expando](type-expando)
:Notes: [File only](type-path), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set newsrc = "~/.newsrc"
    ```

Specify the format of the filename containing info about subscribed newsgroups - names and indexes of read articles.

**Format Sequences**

| Short | Long Name     | Description       |
|-------|---------------|-------------------|
| `%a`  | `%{account}`  | Account url       |
| `%P`  | `%{port-if}`  | Port if specified |
| `%p`  | `%{port}`     | Port              |
| `%S`  | `%{schema}`   | Url schema        |
| `%s`  | `%{server}`   | News server name  |
| `%u`  | `%{username}` | Username          |

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-news-cache-dir)=
## `$news_cache_dir`

:Description: Directory for cached news articles
:Type: [Path (String)](type-path)
:Notes: [Directory only](type-path)
:Default:
    ```neomuttrc
    set news_cache_dir = "~/.neomutt"
    ```

Point to the directory where NeoMutt saves cached news articles and headers.
If _unset_, articles and headers will not be saved at all and will be reloaded from the server each time.

--------------------------------------------------------------------------------

(cfg-news-server)=
## `$news_server`

:Description: URL of the news server
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set news_server = ""
    ```

Specify the domain name or address of the NNTP server.

You can also specify username and an alternative port for each news server, e.g. `[[s]news://][username[:password]@]server[:port]`

Can also be set using the command line option `-g`, the environment variable [`$NNTPSERVER`](ref-env), or putting the server name in the file `/etc/nntpserver`.

--------------------------------------------------------------------------------

(cfg-nntp-authenticators)=
## `$nntp_authenticators`

:Description: Allowed authentication methods
:Type: [String](type-string)
:Notes: [Case Insensitive](type-general)
:Default: (empty)
    ```neomuttrc
    set nntp_authenticators = ""
    ```

This is a colon-delimited list of authentication methods NeoMutt may attempt to use to log in to a news server, in the order NeoMutt should try them.
Authentication methods are either `user` or any SASL mechanism, e.g. `digest-md5`, `gssapi` or `cram-md5`.
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

(cfg-nntp-context)=
## `$nntp_context`

:Description: Maximum number of articles to list (0 for all articles)
:Type: [Number (Long)](type-long)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set nntp_context = 1000
    ```

Define the number of articles listed in the index when a newsgroup is entered.
If active newsgroup have more articles than this number, oldest articles will be ignored.
Also controls how many articles headers will be saved in cache when you quit newsgroup.

--------------------------------------------------------------------------------

(cfg-nntp-listgroup)=
## `$nntp_listgroup`

:Description: Check all articles when opening a newsgroup
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set nntp_listgroup = yes
    ```

Control whether the existence of each article is checked when a newsgroup is entered.

--------------------------------------------------------------------------------

(cfg-nntp-load-description)=
## `$nntp_load_description`

:Description: Load descriptions for newsgroups when adding to the list
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set nntp_load_description = yes
    ```

Control whether descriptions for each newsgroup are loaded when a newsgroup is added to the list (first time list loading or new newsgroup adding).

--------------------------------------------------------------------------------

(cfg-nntp-pass)=
## `$nntp_pass`

:Description: Password for the news server
:Type: [String](type-string)
:Notes: [Sensitive](type-general)
:Default: (empty)
    ```neomuttrc
    set nntp_pass = ""
    ```

Your password for NNTP account.

--------------------------------------------------------------------------------

(cfg-nntp-poll)=
## `$nntp_poll`

:Description: Interval between checks for new posts
:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set nntp_poll = 60
    ```

The time in seconds until any operations on newsgroup except post new article will cause recheck for new news.
If set to 0, NeoMutt will recheck newsgroup on each operation in index (stepping, read article, etc.).

--------------------------------------------------------------------------------

(cfg-nntp-user)=
## `$nntp_user`

:Description: Username for the news server
:Type: [String](type-string)
:Notes: [Sensitive](type-general)
:Default: (empty)
    ```neomuttrc
    set nntp_user = ""
    ```

Your login name on the NNTP server.
If _unset_ and NNTP server requires authentication, NeoMutt will prompt you for your account name when you connect to news server.

--------------------------------------------------------------------------------

(cfg-post-moderated)=
## `$post_moderated`

:Description: Allow posting to moderated newsgroups
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set post_moderated = ask-yes
    ```

If set to _yes_, NeoMutt will post article to newsgroup that have not permissions to posting (e.g. moderated).

:::{note}
If news server does not support posting to that newsgroup or totally read-only, that posting will not have an effect.
:::

--------------------------------------------------------------------------------

(cfg-save-unsubscribed)=
## `$save_unsubscribed`

:Description: Save a list of unsubscribed newsgroups to the `newsrc`
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set save_unsubscribed = no
    ```

When _set_, info about unsubscribed newsgroups will be saved into [`$newsrc`](cfg-newsrc) file and into cache.

--------------------------------------------------------------------------------

(cfg-show-new-news)=
## `$show_new_news`

:Description: Check for new newsgroups when entering the browser
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set show_new_news = yes
    ```

If _set_, news server will be asked for new newsgroups on entering the browser.
Otherwise, it will be done only once for a news server.
Also controls whether or not number of new articles of subscribed newsgroups will be then checked.

--------------------------------------------------------------------------------

(cfg-x-comment-to)=
## `$x_comment_to`

:Description: Add `X-Comment-To` header that contains article author
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set x_comment_to = no
    ```

If _set_, NeoMutt will add `X-Comment-To:` field (that contains full name of original article author) to an article that followed up to a newsgroup.

