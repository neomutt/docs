---
title: Auto-Discover and List IMAP Mailboxes
description: Populate the mailboxes list automatically using IMAP subscriptions, mbsync, scripted discovery, and named-mailboxes
keywords: mailboxes, named-mailboxes, imap, mbsync, auto-discover, imap_check_subscribed, sidebar, folder browser, scripted, dynamic mailboxes
---

# Auto-Discover and List IMAP Mailboxes

## Prerequisites

1. NeoMutt configured with at least one IMAP or local Maildir account.
2. If using mbsync, a working `~/.mbsyncrc`.

## Use IMAP Subscribed Folders

If you read mail directly from an IMAP server, NeoMutt can ask the server for its list of subscribed folders.

1. Enable subscription checking:

```neomuttrc
set imap_check_subscribed
```

Expected result: NeoMutt adds all server-subscribed folders to its mailbox list, as if you had run [`:mailboxes`](cmd-mailboxes) for each one.

## Browse and Subscribe on the Server

1. Open the folder browser with {kbd}`c` then {kbd}`?` (or press {kbd}`y`).
2. Press {kbd}`s` on a folder to subscribe, or {kbd}`u` to unsubscribe.
3. Toggle the view to show only subscribed folders with [`<toggle-subscribed>`](fn-toggle-subscribed).

Expected result: the subscription list on the server is updated and NeoMutt reflects the change.

## Discover Local Folders from mbsync

If you use mbsync to sync to a local Maildir, you can generate the [`:mailboxes`](cmd-mailboxes) command from the directory tree.

1. Add a command that lists your synced folders:

```neomuttrc
mailboxes `find ~/.local/share/mail/you@example.com -type d -name cur -printf '%h\n' | sort`
```

This finds every Maildir folder (each has a `cur/` subdirectory) and returns the parent path.

Expected result: all synced folders appear in the mailbox list and sidebar.

## Use mbsync's Channel List

1. List the folders a channel knows about:

```sh
mbsync -l you@example.com
```

2. Use the output in a helper script that generates [`:mailboxes`](cmd-mailboxes) commands, then source it:

```neomuttrc
source "~/.config/neomutt/gen-mailboxes.sh|"
```

Expected result: the mailbox list stays in sync with whatever mbsync knows about.

## Add Friendly Names with named-mailboxes

1. Replace raw paths with labelled entries:

```neomuttrc
named-mailboxes "Inbox"   "+INBOX"
named-mailboxes "Sent"    "+Sent"
named-mailboxes "Drafts"  "+Drafts"
named-mailboxes "Trash"   "+Trash"
```

Expected result: the sidebar and browser show readable names instead of folder paths.

## Combine Labels with Scripted Discovery

1. Write a script that outputs [`:named-mailboxes`](cmd-named-mailboxes) commands:

```sh
#!/bin/sh
# gen-mailboxes.sh — output named-mailboxes for each Maildir folder
MAILDIR="$HOME/.local/share/mail/you@example.com"
for dir in "$MAILDIR"/*/cur; do
    folder="$(basename "$(dirname "$dir")")"
    printf 'named-mailboxes "%s" "+%s"\n' "$folder" "$folder"
done
```

2. Source it from your config:

```neomuttrc
source "~/.config/neomutt/gen-mailboxes.sh|"
```

Expected result: new folders created by mbsync appear automatically with readable names.

## Refresh Mailboxes After Sync

If new folders appear after running mbsync, re-source the mailbox list without restarting NeoMutt:

```neomuttrc
macro index o "<shell-escape>mbsync -a && notmuch new<Enter><enter-command>source ~/.config/neomutt/gen-mailboxes.sh|<Enter>" "Sync and refresh mailboxes"
```

Expected result: pressing {kbd}`o` syncs mail and updates the mailbox list in one step.

See [Configure Mailboxes](mailboxes) for the full [`:mailboxes`](cmd-mailboxes) command reference and [Sidebar](sidebar/sidebar) for display options.
