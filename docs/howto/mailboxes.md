---
title: Configure Mailboxes
description: Monitor incoming mail, configure spool mailboxes with mbox-hook, detect new mail, and control polling intervals
keywords: mailboxes, named-mailboxes, unmailboxes, mbox-hook, spool, new mail, monitoring, label, notify, poll, mail_check, new_mail_command, inotify, mail_check_stats, check_mbox_size, sidebar, initial folder, address normalization
---

# Configure Mailboxes

## Using Multiple Spool Mailboxes

```neomuttrc
mbox-hook [-noregex] regex mailbox
```

This command is used to move read messages from a specified mailbox to a different mailbox automatically when you quit or change folders
*regex* is used to specify the mailbox to treat as a "spool" mailbox and *mailbox* specifies where mail should be saved when read.
The *-noregex* switch controls whether *regex* is matched using a simple string comparison or a full regex match.

The regex parameter has **mailbox shortcut** expansion performed on the first character.
See **mailbox-hook** for more details.

Note that execution of mbox-hooks is dependent on the [`$move`](cfg-move) configuration variable.
If set to "no" (the default), mbox-hooks will not be executed.

Unlike some of the other *hook* commands, only the *first* matching regex is used (it is not possible to save read mail in more than a single mailbox).

## Monitoring Incoming Mail

```neomuttrc
mailboxes [-label label] [-nolabel] [-notify] [-nonotify] [-poll] [-nopoll] mailbox [...]
named-mailboxes [-notify] [-nonotify] [-poll] [-nopoll] label mailbox [label mailbox ...]
unmailboxes { * | mailbox [...] }
```

This command specifies folders which can receive mail and which will be checked for new messages periodically.

The `-label` argument can be used to specify an alternative label to print in the sidebar or mailbox browser instead of the mailbox path.
A label may be removed via the `-nolabel` argument.
If unspecified, an existing mailbox label will be unchanged.

Use `-nonotify` to disable notifying when new mail arrives.
The `-notify` argument can be used to re-enable notifying for an existing mailbox.
If unspecified: a new mailbox will notify by default, while an existing mailbox will be unchanged.

To disable polling, specify `-nopoll` before the mailbox name.
The `-poll` argument can be used to re-enable polling for an existing mailbox.
If unspecified: a new mailbox will poll by default, while an existing mailbox will be unchanged.

*folder* can either be a local file or directory (Mbox/Mmdf or Maildir/Mh).
If NeoMutt was built with POP and/or IMAP support, *folder* can also be a POP/IMAP folder URL.
The URL syntax is described in **URL syntax**, POP and IMAP are described in [POP](pop.md) and [IMAP](imap.md) respectively.

NeoMutt provides a number of advanced features for handling (possibly many) folders and new mail within them, please refer to **new mail** for details (including in what situations and how often NeoMutt checks for new mail).
Additionally, [`$new_mail_command`](cfg-new-mail-command) can be used to run a command when new mail is detected.

The `unmailboxes` command is used to remove a token from the list of folders which receive mail.
`unmailboxes` can be used on the mailbox path, [`$folder`](cfg-folder)-abbreviated path, or description.
Use `unmailboxes *` to remove all tokens.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Mailbox browser with named mailboxes

**Description:** The NeoMutt mailbox browser (opened with `c?` or the
`<browser>` function) showing a list of monitored mailboxes configured via
`named-mailboxes`, displaying the custom label names (e.g. "My INBOX", "Work
Mail") instead of raw folder paths, along with message counts and new mail
indicators.

**Highlights:** How `-label` / `named-mailboxes` labels replace raw paths in the browser, the new mail flag column, and the folder size or message count columns.
:::

:::{note}
The folders in the `mailboxes` command are resolved when the command is executed, so if these names contain **shortcut characters** (such as `=` and `!`), any variable definition that affects these characters (like [`$folder`](cfg-folder) and [`$spool_file`](cfg-spool-file)) should be set before the `mailboxes` command.
If none of these shortcuts are used, a local path should be absolute as otherwise NeoMutt tries to find it relative to the directory from where NeoMutt was started which may not always be desired.
:::

---

## Address Normalization

NeoMutt normalizes all email addresses to their simplest canonical form.
If an address contains a display name, the form `Joe User <joe@example.com>` is used; otherwise just the bare address `joe@example.com` (without angle brackets) is used.

This normalization applies to all headers NeoMutt generates, including aliases.

---

## Initial Folder Selection

The folder NeoMutt opens at startup is determined in the following order of precedence (highest to lowest):

1. The mailbox given with the `-f` command-line option (highest priority).
2. The `$MAIL` environment variable, if set.
3. The `$MAILDIR` environment variable, if set.
4. The compile-time mail spool (`/var/spool/mail/$USER` or similar; last fallback).
5. The [`$spool_file`](cfg-spool-file) config option overrides the compile-time default spool location.

## New Mail Detection

### How Detection Works by Format

NeoMutt detects new mail differently depending on the mailbox format:

**Mbox / Mmdf** NeoMutt compares the file's access time against its modification time.
A folder is considered to have new mail if it was modified more recently than it was last accessed.
External tools (e.g. `biff`, `frm`) that read the mailbox without resetting its access time can prevent detection.
Backup tools and filesystems mounted with `noatime` can have the same effect.

NeoMutt resets the access time correctly when there is at least one unread, non-deleted, non-old message remaining in the folder.

If mtime/atime-based detection is unreliable in your setup, use file-size tracking instead:

```neomuttrc
set check_mbox_size
```

Note that `check_mbox_size` won't detect changes that leave the file size unchanged.

**Maildir** New mail is assumed if the `new/` subdirectory contains at least one message that is not marked deleted (see [`$maildir_trash`](cfg-maildir-trash)).

**MH** A mailbox has new mail if there is at least one message in the unseen sequence defined by [`$mh_seq_unseen`](cfg-mh-seq-unseen).

**IMAP** NeoMutt uses recent message counts reported by the server.
If [`$imap_idle`](cfg-imap-idle) is set, NeoMutt uses the IMAP IDLE extension when the server advertises it, for lower-latency notification.

**POP3** NeoMutt does not poll POP3 folders for new mail — it only checks the currently open folder.

### Controlling Notification Scope

Set [`$mail_check_recent`](cfg-mail-check-recent) (on by default) to be notified only about mail that arrived since you last opened the mailbox.
Unset it to be notified of all new mail regardless:

```neomuttrc
unset mail_check_recent
```

Run a command whenever new mail arrives in the current inbox:

```neomuttrc
set new_mail_command = "notify-send 'New mail in NeoMutt'"
```

### Polling Interval

NeoMutt polls monitored mailboxes while idle in the index.
The check interval is:

- **Local and IMAP folders** — [`$mail_check`](cfg-mail-check) (seconds, default 5)
- **POP folders** — [`$pop_check_interval`](cfg-pop-check-interval)

Mailboxes added with `-nopoll` are excluded from polling.

To also check all subscribed IMAP folders (not just those in `mailboxes`):

```neomuttrc
set imap_check_subscribed
```

### Inotify (Linux)

When NeoMutt is compiled with inotify support, it receives immediate kernel notifications for new mail in locally monitored folders — no polling delay.
This works for mail delivered by a local agent; it does not work for remote delivery over NFS or similar.

Inotify debug output is available at log level 3 (`-d3` on the command line).

### Message Counts in the Sidebar

Enable periodic calculation of unread, flagged, and total message counts:

```neomuttrc
set mail_check_stats
set mail_check_stats_interval = 60   # seconds between recalculations
```

These counts are used by the sidebar.
Control their display via [`$sidebar_format`](cfg-sidebar-format).
IMAP mailboxes support unread and total counts only.
