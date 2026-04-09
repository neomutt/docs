---
title: Setting Up Offline Email with mbsync
description: Sync a remote IMAP account to a local Maildir using mbsync (isync), then read mail offline in NeoMutt
keywords: neomutt, mbsync, isync, offline, imap, maildir, sync, local mail, mbsyncrc, channel, store, tutorial
diataxis_type: tutorial
---

# Setting Up Offline Email with mbsync

This tutorial walks you through syncing a remote IMAP account to a local Maildir so you can read and search mail offline.
You'll install mbsync, write a configuration, run your first sync, and point NeoMutt at the local copy.

If you haven't connected to your mail server at all yet, start with [Writing Your First Configuration](first-config) to confirm your credentials work.

## Why Use mbsync?

NeoMutt can read mail directly from an IMAP server, but that requires a network connection for every operation.
With mbsync you keep a full local copy of your mailbox in Maildir format.
NeoMutt reads from the local copy, so navigation and searching are instant.
You run mbsync periodically to pull new mail and push changes back.

## Prerequisites

1. A working IMAP account (server, username, and password).
2. `mbsync` (provided by the `isync` package) installed on your system.
3. NeoMutt installed.

On Fedora/RHEL:

```sh
sudo dnf install isync
```

On Debian/Ubuntu:

```sh
sudo apt install isync
```

On macOS:

```sh
brew install isync
```

## Create the Local Mail Directory

1. Create a directory for your mail.
   The example below follows the XDG convention, but any path works:

```sh
mkdir -p ~/.local/share/mail/you@example.com
```

## Write the mbsync Configuration

1. Create the file `~/.mbsyncrc`:

```
# Remote IMAP account
IMAPStore you@example.com-remote
Host imap.example.com
Port 993
User you@example.com
PassCmd "pass you@example.com"
SSLType IMAPS
CertificateFile /etc/ssl/certs/ca-certificates.crt

# Local Maildir store
MaildirStore you@example.com-local
Subfolders Verbatim
Path ~/.local/share/mail/you@example.com/
Inbox ~/.local/share/mail/you@example.com/INBOX

# Sync channel
Channel you@example.com
Expunge Both
Far :you@example.com-remote:
Near :you@example.com-local:
Patterns *
Create Both
SyncState *
```

Replace the server, user, and password command with your own values.

### Understanding the Key Settings

| Setting            | Purpose                                                 |
|--------------------|---------------------------------------------------------|
| `IMAPStore`        | Defines the remote side — server, credentials, and TLS  |
| `MaildirStore`     | Defines the local side — where Maildir folders are kept |
| `Channel`          | Links the two stores and controls sync behaviour        |
| `PassCmd`          | Runs a command to retrieve your password (see below)    |
| `Patterns *`       | Sync all folders; adjust this to include or exclude     |
| `Expunge Both`     | Delete messages on both sides when they are removed     |
| `Create Both`      | Create new folders on either side automatically         |
| `Subfolders Verbatim` | Keep the server's folder hierarchy as-is             |

For `PassCmd`, you can use any command that prints your password to stdout.
Common choices:

```
PassCmd "pass you@example.com"
PassCmd "gpg --batch -q --decrypt ~/.mbsync-pass.gpg"
PassCmd "secret-tool lookup service imap user you@example.com"
```

See [Password Manager](../howto/password-manager) for more options.

### Certificate File

The `CertificateFile` path varies by distribution:

| Distribution     | Path                                    |
|------------------|-----------------------------------------|
| Debian / Ubuntu  | `/etc/ssl/certs/ca-certificates.crt`    |
| Fedora / RHEL    | `/etc/pki/tls/certs/ca-bundle.crt`      |
| Arch Linux       | `/etc/ssl/certs/ca-certificates.crt`    |
| macOS (Homebrew) | `/usr/local/etc/openssl/cert.pem`       |

## Run Your First Sync

1. Run mbsync for all channels:

```sh
mbsync -a
```

2. Check that mail appeared in your local directory:

```sh
ls ~/.local/share/mail/you@example.com/
```

Expected result: you see an `INBOX` directory and any other server folders, each containing `cur/`, `new/`, and `tmp/` subdirectories.

If mbsync reports an authentication error, check your `PassCmd` by running it manually in your shell.

## Point NeoMutt at the Local Maildir

1. Add these settings to your `neomuttrc`:

```neomuttrc
set folder    = "~/.local/share/mail/you@example.com"
set spoolfile = "+INBOX"
set mbox_type = Maildir
set postponed = "+Drafts"
set record    = "+Sent"
set trash     = "+Trash"
```

2. Start NeoMutt:

```sh
neomutt
```

Expected result: your inbox appears instantly from the local Maildir.

## Sync New Mail

Whenever you want fresh mail, run:

```sh
mbsync -a
```

You can trigger this from inside NeoMutt with a macro:

```neomuttrc
macro index o "<shell-escape>mbsync -a<Enter>" "Sync all mail with mbsync"
```

Press {kbd}`o` in the index to sync without leaving NeoMutt.

## Exclude Specific Folders

If your server has folders you don't need locally, adjust the `Patterns` line:

```
Patterns * !"[Gmail]/All Mail" !"[Gmail]/Important"
```

This syncs everything except the named folders.

## Next Steps

- "I want to send mail from the local setup." Continue with [Setting Up msmtp for Sending](msmtp-setup).
- "I want full-text search on the local mail." Continue with [Setting Up Notmuch for Email Search](notmuch-setup).
- "I want to secure my passwords." See [Password Manager](../howto/password-manager).
- "I want to automate syncing." See [Integrate External Tools](../howto/external-tools).
