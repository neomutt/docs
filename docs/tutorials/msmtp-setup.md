---
title: Setting Up msmtp for Sending
description: Configure msmtp as an external SMTP relay and connect it to NeoMutt using set sendmail
keywords: neomutt, msmtp, sendmail, smtp, sending, relay, tls, external mta, tutorial, offline sending, queue
diataxis_type: tutorial
---

# Setting Up msmtp for Sending

This tutorial sets up msmtp as an external mail sender for NeoMutt.
You'll install msmtp, write a configuration, send a test message, and connect it to NeoMutt.

NeoMutt has built-in SMTP support (see [Set Up SMTP](../howto/smtp)), but using an external tool like msmtp gives you logging, queuing, and per-account profiles independent of NeoMutt's config.
This is the approach used by tools like mutt-wizard.

## Prerequisites

1. A working mail account with SMTP access (server, port, username, and password).
2. `msmtp` installed on your system.
3. NeoMutt installed.

On Fedora/RHEL:

```sh
sudo dnf install msmtp
```

On Debian/Ubuntu:

```sh
sudo apt install msmtp
```

On macOS:

```sh
brew install msmtp
```

## Write the msmtp Configuration

1. Create the file `~/.config/msmtp/config` (or `~/.msmtprc`):

```
# Default settings applied to all accounts
defaults
auth           on
tls            on
tls_trust_file /etc/ssl/certs/ca-certificates.crt
logfile        ~/.config/msmtp/msmtp.log

# Account definition
account        you@example.com
host           smtp.example.com
port           465
tls_starttls   off
from           you@example.com
user           you@example.com
passwordeval   "pass you@example.com"
```

Replace the server, port, user, and password command with your values.

### Understanding the Key Settings

| Setting          | Purpose                                                   |
|------------------|-----------------------------------------------------------|
| `auth on`        | Enable SMTP authentication                                |
| `tls on`         | Enable TLS encryption                                     |
| `tls_starttls`   | `off` for implicit TLS (port 465); `on` for STARTTLS (port 587) |
| `tls_trust_file` | Path to system CA certificates (see the table below)      |
| `passwordeval`   | Runs a command to retrieve your password                  |
| `logfile`        | Where msmtp writes delivery logs                          |

### Port and TLS Combinations

| Port | Protocol       | `tls_starttls` |
|------|----------------|-----------------|
| 465  | Implicit TLS   | `off`           |
| 587  | STARTTLS       | `on`            |

### Certificate File

The `tls_trust_file` path varies by distribution:

| Distribution     | Path                                    |
|------------------|-----------------------------------------|
| Debian / Ubuntu  | `/etc/ssl/certs/ca-certificates.crt`    |
| Fedora / RHEL    | `/etc/pki/tls/certs/ca-bundle.crt`      |
| Arch Linux       | `/etc/ssl/certs/ca-certificates.crt`    |
| macOS (Homebrew) | `/usr/local/etc/openssl/cert.pem`       |

### Password Retrieval

For `passwordeval`, use any command that prints your password to stdout:

```
passwordeval "pass you@example.com"
passwordeval "gpg --batch -q --decrypt ~/.smtp-pass.gpg"
passwordeval "secret-tool lookup service smtp user you@example.com"
```

See [Password Manager](../howto/password-manager) for more options.

## Secure the Configuration File

msmtp requires that its config file is not world-readable:

```sh
chmod 600 ~/.config/msmtp/config
```

## Send a Test Message

1. Send a test email from the command line:

```sh
echo "Test from msmtp" | msmtp you@example.com
```

2. Check the log file for confirmation:

```sh
cat ~/.config/msmtp/msmtp.log
```

Expected result: the log shows a successful delivery and the message arrives in your inbox.

If delivery fails, check the error in the log.
Common problems are wrong port/TLS settings or an incorrect password command.

## Connect msmtp to NeoMutt

1. Add this line to your `neomuttrc`:

```neomuttrc
set sendmail = "msmtp -a you@example.com"
```

The `-a` flag selects the msmtp account by name.

2. Compose and send a message in NeoMutt (press `m`).

Expected result: NeoMutt hands the message to msmtp for delivery.

## Add a Second Account

1. Append another account block to your msmtp config:

```
account        work@company.com
host           smtp.company.com
port           587
tls_starttls   on
from           work@company.com
user           work@company.com
passwordeval   "pass work@company.com"
```

2. Switch accounts in NeoMutt using a folder-hook:

```neomuttrc
folder-hook "work@company.com" "set sendmail='msmtp -a work@company.com'"
folder-hook "you@example.com"  "set sendmail='msmtp -a you@example.com'"
```

Expected result: NeoMutt uses the right SMTP account for each mailbox.

See [Managing Multiple Email Accounts](multiple-accounts) for the complete multi-account setup.

## Next Steps

- "I want to read mail offline too." See [Setting Up Offline Email with mbsync](mbsync-setup).
- "I want to use NeoMutt's built-in SMTP instead." See [Set Up SMTP](../howto/smtp).
- "I want to secure my passwords." See [Password Manager](../howto/password-manager).
