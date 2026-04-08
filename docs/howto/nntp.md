---
title: NNTP (Usenet)
description: Configure NeoMutt to read, post, and manage Usenet newsgroups via NNTP with subscriptions, caching, and threading.
keywords: nntp, usenet, newsgroups, newsrc, news server, subscribe, catchup, post, followup, news_cache_dir, nntp_poll, group_index_format, change-newsgroup, articles
---

# NNTP (Usenet)

## Introduction

NeoMutt can read from a news server using NNTP.

The default news server can be obtained from the `$NNTPSERVER` environment variable or from the `/etc/nntpserver` file.
Like in other news readers, information about the subscribed newsgroups is saved in the file specified by the [`$newsrc`](cfg-newsrc) variable.
You can open a newsgroup with the function [`<change-newsgroup>`](fn-change-newsgroup).

When browsing the list of newsgroups on the server the function [`<subscribe>`](fn-subscribe) can be used to tell NeoMutt the groups of interest to you.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Newsgroup browser

**Description:** The NeoMutt newsgroup browser showing a list of available NNTP newsgroups from the server, with columns for newsgroup name, number of articles, and description.
Some groups should be marked as subscribed.

**Highlights:** The group list layout with subscription status indicators, article counts per group, and the newsgroup description column loaded via [`$nntp_load_description`](cfg-nntp-load-description).
:::

This list is stored in the [`$newsrc`](cfg-newsrc) file, so NeoMutt remembers it across invocations (see also [`$save_unsubscribed`](cfg-save-unsubscribed)).
With the [`<unsubscribe>`](fn-unsubscribe) function a group can be deleted from that list.
You can also specify the list of interesting groups with the [`mailboxes`](mailboxes) command in your config file.

When checking for new messages, NeoMutt only polls the subscribed newsgroups.

The variable [`$news_cache_dir`](cfg-news-cache-dir) can be used to point to a directory.
NeoMutt will create a hierarchy of subdirectories named like the account and newsgroup the cache is for.
The hierarchy is also used to store header cache if NeoMutt was compiled with [header cache](caching.md) support.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Newsgroup article list

**Description:** The NeoMutt index view after opening a newsgroup, showing a list of articles/posts with columns for number, flags, date, author, and subject — similar to the email index but for NNTP articles, with threaded display enabled.

**Highlights:** How the article index resembles the email index, threaded article display with tree indicators, and the newsgroup name shown in the status bar.
:::

## Variables

| Name                    | Type    | Default                    |
|-------------------------|---------|----------------------------|
| `ask_followup_to`       | boolean | `no`                       |
| `ask_x_comment_to`      | boolean | `no`                       |
| `catchup_newsgroup`     | quad    | `ask-yes`                  |
| `followup_to_poster`    | quad    | `ask-yes`                  |
| `group_index_format`    | string  | `%4C %M%N %5s %-45.45f %d` |
| `inews_command`         | string  | (empty)                    |
| `newsgroups_charset`    | string  | `utf-8`                    |
| `newsrc`                | string  | `~/.newsrc`                |
| `news_cache_dir`        | string  | `~/.neomutt`               |
| `news_server`           | string  | (empty)                    |
| `nntp_authenticators`   | string  | (empty)                    |
| `nntp_context`          | number  | `1000`                     |
| `nntp_listgroup`        | boolean | `yes`                      |
| `nntp_load_description` | boolean | `yes`                      |
| `nntp_pass`             | string  | (empty)                    |
| `nntp_poll`             | number  | `60`                       |
| `nntp_user`             | string  | (empty)                    |
| `post_moderated`        | quad    | `ask-yes`                  |
| `save_unsubscribed`     | boolean | `no`                       |
| `show_new_news`         | boolean | `yes`                      |
| `show_only_unread`      | boolean | `no`                       |
| `x_comment_to`          | boolean | `no`                       |

## Functions

NNTP adds the following functions to NeoMutt.
By default, none of them are bound to keys.

| Menus              | Function                      | Description                                    |
|--------------------|-------------------------------|------------------------------------------------|
| browser,index      | [`<catchup>`](fn-catchup)                   | Mark all articles in newsgroup as read         |
| index,pager        | [`<change-newsgroup>`](fn-change-newsgroup)          | Open a different newsgroup                     |
| compose            | [`<edit-followup-to>`](fn-edit-followup-to)          | Edit the Followup-To field                     |
| compose            | [`<edit-newsgroups>`](fn-edit-newsgroups)           | Edit the newsgroups list                       |
| compose            | [`<edit-x-comment-to>`](fn-edit-x-comment-to)         | Edit the X-Comment-To field                    |
| attach,index,pager | [`<followup-message>`](fn-followup-message)          | Followup to newsgroup                          |
| index,pager        | [`<post-message>`](fn-post-message)              | Post message to newsgroup                      |
| browser            | [`<reload-active>`](fn-reload-active)             | Load list of all newsgroups from NNTP server   |
| browser            | [`<subscribe>`](fn-subscribe)                 | Subscribe to current mbox (IMAP/NNTP only)     |
| browser            | [`<subscribe-pattern>`](fn-subscribe-pattern)         | Subscribe to newsgroups matching a pattern     |
| browser            | [`<uncatchup>`](fn-uncatchup)                 | Mark all articles in newsgroup as unread       |
| browser            | [`<unsubscribe>`](fn-unsubscribe)               | Unsubscribe from current mbox (IMAP/NNTP only) |
| browser            | [`<unsubscribe-pattern>`](fn-unsubscribe-pattern)       | Unsubscribe from newsgroups matching a pattern |
| index,pager        | [`<change-newsgroup-readonly>`](fn-change-newsgroup-readonly) | Open a different newsgroup in read only mode   |
| attach,index,pager | [`<forward-to-group>`](fn-forward-to-group)          | Forward to newsgroup                           |
| index              | [`<get-children>`](fn-get-children)              | Get all children of the current message        |
| index              | [`<get-parent>`](fn-get-parent)                | Get parent of the current message              |
| index              | [`<reconstruct-thread>`](fn-reconstruct-thread)        | Reconstruct thread containing current message  |
| index              | [`<get-message>`](fn-get-message)               | Get message with Message-ID                    |

## neomuttrc

```neomuttrc
# Example NeoMutt config file for the nntp feature.

# --------------------------------------------------------------------------
# VARIABLES – shown with their default values
# --------------------------------------------------------------------------
set ask_followup_to = no
set ask_x_comment_to = no
set catchup_newsgroup = ask-yes
set followup_to_poster = ask-yes
set group_index_format = '%4C %M%N %5s  %-45.45f %d'
set inews_command = ''
set newsgroups_charset = utf-8
set newsrc = '~/.newsrc'
set news_cache_dir = '~/.neomutt'
set news_server = ''
set nntp_authenticators = ''
set nntp_context = 1000
set nntp_listgroup = yes
set nntp_load_description = yes
set nntp_pass = ''
set nntp_poll = 60
set nntp_user = ''
set post_moderated = ask-yes
set save_unsubscribed = no
set show_new_news = yes
set show_only_unread = no
set x_comment_to = no
# --------------------------------------------------------------------------
# FUNCTIONS – shown with an example mapping
# --------------------------------------------------------------------------
# Mark all articles in newsgroup as read
bind browser,index y catchup
# Open a different newsgroup
bind index,pager i change-newsgroup
# Edit the Followup-To field
bind compose o edit-followup-to
# Edit the newsgroups list
bind compose N edit-newsgroups
# Edit the X-Comment-To field
bind compose x edit-x-comment-to
# Followup to newsgroup
bind attach,index,pager F followup-message
# Post message to newsgroup
bind index,pager P post-message
# Load list of all newsgroups from NNTP server
bind browser g reload-active
# Subscribe to current mbox (IMAP/NNTP only)
bind browser s subscribe
# Subscribe to newsgroups matching a pattern
bind browser S subscribe-pattern
# Mark all articles in newsgroup as unread
bind browser Y uncatchup
# Unsubscribe from current mbox (IMAP/NNTP only)
bind browser u unsubscribe
# Unsubscribe from newsgroups matching a pattern
bind browser U unsubscribe-pattern
# Open a different newsgroup in read only mode
bind index,pager \ei change-newsgroup-readonly
# Forward to newsgroup
bind attach,index,pager \eF forward-to-group
# Get all children of the current message
# bind index ??? get-children
# Get parent of the current message
bind index \eG get-parent
# Reconstruct thread containing current message
# bind index ??? reconstruct-thread
# Get message with Message-ID
bind index \CG get-message
# --------------------------------------------------------------------------

# vim: filetype=neomuttrc
```

