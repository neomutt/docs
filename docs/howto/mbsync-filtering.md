---
title: Configure mbsync to Sync Specific IMAP Folders
description: Include, exclude, and limit IMAP folders synced by mbsync using Patterns, MaxMessages, and Gmail-specific exclusions
keywords: mbsync, isync, patterns, filter, exclude, include, gmail, maxmessages, expireunread, expunge, imap folders, sync, maildir, selective sync
---

# Configure mbsync to Sync Specific IMAP Folders

## Prerequisites

1. A working `~/.mbsyncrc` with at least one Channel that syncs successfully.
2. If you are new to mbsync, complete [Setting Up Offline Email with mbsync](../tutorials/mbsync-setup) first.

## Include and Exclude Folders with Patterns

1. Edit the `Patterns` line in your Channel block:

```
Channel you@example.com
Far :you@example.com-remote:
Near :you@example.com-local:
Patterns *
```

2. Exclude specific folders by prefixing them with `!`:

```
Patterns * !Junk !Trash
```

3. Run `mbsync -a` and confirm the excluded folders are no longer synced.

Expected result: all folders sync except the ones you excluded.

## Include Only Specific Folders

1. List only the folders you want:

```
Patterns INBOX Sent Drafts
```

Expected result: only the named folders are synced.

## Exclude Gmail System Folders

Gmail exposes virtual folders under `[Gmail]/` that can cause duplicate downloads.

1. Exclude the heavy ones:

```
Patterns * !"[Gmail]/All Mail" !"[Gmail]/Important" !"[Gmail]/Starred"
```

Expected result: Gmail labels sync without pulling redundant copies from All Mail.

## Limit the Number of Messages per Folder

1. Set `MaxMessages` on the Channel to keep only recent messages locally:

```
Channel you@example.com
Far :you@example.com-remote:
Near :you@example.com-local:
Patterns *
MaxMessages 1000
ExpireUnread no
```

`MaxMessages` keeps the most recent N messages in the local store.
`ExpireUnread no` prevents unread messages from being expired even if they fall outside the limit.

Expected result: each folder holds at most 1000 messages locally; older messages remain on the server.

## Control Deletion Behaviour with Expunge

1. Set `Expunge` to control when deleted messages are permanently removed:

```
Expunge Both
```

| Value  | Behaviour                                              |
|--------|--------------------------------------------------------|
| `Both` | Remove deleted messages from both local and remote     |
| `Near` | Remove deleted messages from the local store only      |
| `Far`  | Remove deleted messages from the remote server only    |
| `None` | Never permanently remove deleted messages during sync  |

Expected result: deletion propagation matches your preference.

## Sync a Single Channel

1. Name your channels and sync one at a time:

```sh
mbsync you@example.com
```

Expected result: only the named channel syncs, which is faster when you have multiple accounts.

## List Available Remote Folders

1. Run mbsync in list mode to see what the server offers:

```sh
mbsync -l you@example.com
```

Expected result: a list of all remote folders, which helps you decide what to include or exclude in `Patterns`.

## Verify Your Configuration

1. Run mbsync in dry-run mode to preview what it would do:

```sh
mbsync -n -a
```

Expected result: mbsync prints the actions it would take without making changes.

See [Setting Up Offline Email with mbsync](../tutorials/mbsync-setup) for the full setup tutorial.
