---
title: Setting Up Notmuch for Email Search
description: Install Notmuch, create a database from your local Maildir, run your first search, and use virtual mailboxes in NeoMutt
keywords: neomutt, notmuch, search, index, maildir, virtual mailbox, full-text, tagging, tutorial, notmuch-config, notmuch new
diataxis_type: tutorial
---

# Setting Up Notmuch for Email Search

This tutorial walks you through installing Notmuch, indexing your local Maildir, running your first search query, and opening results as a virtual mailbox in NeoMutt.

If you don't have local mail yet, complete [Setting Up Offline Email with mbsync](mbsync-setup) first — Notmuch works on local Maildir, not directly on IMAP.

## Why Use Notmuch?

NeoMutt's built-in search ({kbd}`/` and {kbd}`l`) works well inside a single mailbox, but it can't search across all folders at once and doesn't index message bodies in advance.
Notmuch builds a full-text index of every message in your Maildir tree, so searches return results instantly — even across thousands of messages in many folders.

## Prerequisites

1. A local Maildir tree (e.g. `~/.local/share/mail/you@example.com/`).
2. `notmuch` installed.
3. NeoMutt compiled with Notmuch support.

On Fedora/RHEL:

```sh
sudo dnf install notmuch
```

On Debian/Ubuntu:

```sh
sudo apt install notmuch
```

On macOS:

```sh
brew install notmuch
```

Confirm NeoMutt has Notmuch support:

```sh
neomutt -v | grep notmuch
```

Expected result: you see `+notmuch` in the feature list.

## Create the Notmuch Configuration

1. Run the interactive setup:

```sh
notmuch setup
```

2. Answer the prompts:

- **Your full name:** your name as it appears on outgoing mail.
- **Your primary email address:** your email address.
- **Path to mail:** the root of your Maildir tree, e.g. `~/.local/share/mail`.
- **New message tags:** `unread;inbox` (the defaults are fine).
- **Excluded tags:** `deleted;spam`.

Expected result: Notmuch creates `~/.notmuch-config` (or `$NOTMUCH_CONFIG`).

Alternatively, create the file manually:

```ini
[database]
path=/home/you/.local/share/mail

[user]
name=Your Name
primary_email=you@example.com

[new]
tags=unread;inbox;
ignore=.mbsyncstate;.uidvalidity

[search]
exclude_tags=deleted;spam;

[maildir]
synchronize_flags=true
```

The `ignore` line tells Notmuch to skip mbsync's internal state files so they don't appear as messages.

## Build the Initial Index

1. Index all existing mail:

```sh
notmuch new
```

Expected result: Notmuch scans your Maildir and reports the number of messages indexed.
This may take a minute the first time if you have many messages.

2. Test a search from the command line:

```sh
notmuch search tag:inbox
```

Expected result: a list of threads matching the `inbox` tag.

## Configure NeoMutt to Use Notmuch

1. Add these lines to your `neomuttrc`:

```neomuttrc
set nm_default_url = "notmuch:///home/you/.local/share/mail"
set virtual_spool_file = yes
```

Replace the path with the value you used for `[database] path` above.

2. Add virtual mailboxes for common queries:

```neomuttrc
named-mailboxes "Inbox"  "notmuch://?query=tag:inbox"
named-mailboxes "Unread" "notmuch://?query=tag:unread"
named-mailboxes "Sent"   "notmuch://?query=tag:sent"
```

3. Start NeoMutt.

Expected result: the sidebar (if enabled) or mailbox list shows your virtual mailboxes.
Opening "Inbox" displays all messages tagged `inbox`, regardless of which folder they are physically stored in.

## Run an Ad-Hoc Search

1. Bind a key for live queries if you don't have one:

```neomuttrc
bind index,pager \eX vfolder-from-query
```

2. In NeoMutt, press {kbd}`Alt-X` and type a Notmuch query:

```
from:alice@example.com subject:report date:2w..
```

3. Press `Enter`.

Expected result: a virtual folder opens containing only messages matching the query.

## Keep the Index Up to Date

After syncing new mail with mbsync, update the Notmuch index:

```sh
mbsync -a && notmuch new
```

You can combine this into a single macro in NeoMutt:

```neomuttrc
macro index o "<shell-escape>mbsync -a && notmuch new<Enter>" "Sync mail and update index"
```

## Notmuch Query Examples

| Query                              | Matches                                      |
|------------------------------------|----------------------------------------------|
| `tag:inbox`                        | All messages tagged inbox                    |
| `tag:unread`                       | All unread messages                          |
| `from:alice@example.com`           | Messages from Alice                          |
| `subject:report date:1m..`         | Subject contains "report", within last month |
| `tag:inbox AND NOT tag:newsletter` | Inbox without newsletters                    |

See the `notmuch-search-terms` man page for the full query syntax.

## Next Steps

- "I want to organise mail with tags." Continue with [Organising Email with Tags](tags-workflow).
- "I want to tune Notmuch." See [How to Use Notmuch](../howto/notmuch) and [Notmuch Advanced](../howto/notmuch-advanced).
- "I want to set up mbsync." See [Setting Up Offline Email with mbsync](mbsync-setup).
