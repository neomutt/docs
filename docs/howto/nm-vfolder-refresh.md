---
title: Refresh Virtual Mailboxes After New Mail
description: Update the Notmuch database and refresh NeoMutt so virtual mailboxes show the latest messages
keywords: notmuch, refresh, notmuch new, sync, virtual mailbox, update, new mail, macro
---

# Refresh Virtual Mailboxes After New Mail

## Prerequisites

1. Notmuch virtual mailboxes configured in NeoMutt (see [Getting Started with Notmuch Virtual Mailboxes](../tutorials/notmuch-virtual-mailboxes)).
2. A mail sync tool like mbsync delivering new messages to your Maildir.

## Update the Notmuch Database

1. After syncing new mail, run:

```sh
notmuch new
```

Expected result: Notmuch indexes any new messages and reports the count.

## Refresh in NeoMutt

NeoMutt shows query results at the time the mailbox was opened.
To pick up new messages:

1. Leave and re-enter the virtual mailbox (press {kbd}`c` then select it again), or
2. Use [`<sync-mailbox>`](fn-sync-mailbox) (`$` by default) to force a refresh.

Expected result: newly indexed messages appear in the virtual mailbox.

## Create a One-Key Sync Macro

1. Add a macro that syncs mail, updates the index, and refreshes the mailbox:

```neomuttrc
macro index o "<shell-escape>mbsync -a && notmuch new<Enter>" "Sync mail and update Notmuch"
```

2. Press {kbd}`o` in the index.

Expected result: new mail is downloaded, indexed, and the current mailbox is refreshed.

If you don't use mbsync, replace `mbsync -a &&` with your sync command, or remove it to run only `notmuch new`.

## Why Mailboxes Don't Update Automatically

NeoMutt queries the Notmuch database when a virtual mailbox is opened.
It does not re-query continuously in the background.
Running `notmuch new` updates the database, and re-entering the mailbox (or syncing) picks up the changes.

See [Set Up Periodic Mail Sync](periodic-sync) to automate the sync and index step.
