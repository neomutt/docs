---
title: Set Up msmtp with Per-Account Profiles
description: Configure multiple SMTP accounts in msmtp and switch between them automatically in NeoMutt using folder-hooks
keywords: msmtp, sendmail, smtp, per-account, profiles, multiple accounts, folder-hook, send-hook, tls, passwordeval, logging
---

# Set Up msmtp with Per-Account Profiles

## Prerequisites

1. `msmtp` installed and at least one account working.
2. If you are new to msmtp, complete [Setting Up msmtp for Sending](../tutorials/msmtp-setup) first.

## Add Multiple Account Blocks

1. Edit your msmtp config file (`~/.config/msmtp/config` or `~/.msmtprc`):

```
defaults
auth           on
tls            on
tls_trust_file /etc/ssl/certs/ca-certificates.crt
logfile        ~/.config/msmtp/msmtp.log

account        personal
host           smtp.example.com
port           465
tls_starttls   off
from           you@example.com
user           you@example.com
passwordeval   "pass mail/you@example.com"

account        work
host           smtp.company.com
port           587
tls_starttls   on
from           work@company.com
user           work@company.com
passwordeval   "pass mail/work@company.com"

account default : personal
```

The `account default : personal` line sets a fallback account.

Expected result: `msmtp -a personal` and `msmtp -a work` each use the correct server.

## Test Each Account

1. Send a test message from each:

```sh
echo "Test personal" | msmtp -a personal you@example.com
echo "Test work"     | msmtp -a work work@company.com
```

2. Check the log:

```sh
tail ~/.config/msmtp/msmtp.log
```

Expected result: both messages are delivered successfully.

## Switch Accounts in NeoMutt with folder-hook

1. Add folder-hooks that set [`$sendmail`](cfg-sendmail) when you enter each account's mailbox:

```neomuttrc
folder-hook "you@example.com"  "set sendmail='msmtp -a personal'"
folder-hook "work@company.com" "set sendmail='msmtp -a work'"
```

Expected result: composing a message from a work mailbox sends via the work SMTP account.

## Switch Accounts with send-hook

If you want to select the account based on the sender address rather than the current folder:

```neomuttrc
send-hook '~f you@example.com'  "set sendmail='msmtp -a personal'"
send-hook '~f work@company.com' "set sendmail='msmtp -a work'"
```

Expected result: the SMTP account matches the From address on the outgoing message.

## Set a Default Account in NeoMutt

1. Set the default sendmail value before your hooks:

```neomuttrc
set sendmail = "msmtp -a personal"
```

Expected result: messages use the personal account unless a hook overrides it.

## Enable Delivery Logging

The `logfile` line in the msmtp config records every delivery attempt.
Check it when troubleshooting:

```sh
tail -20 ~/.config/msmtp/msmtp.log
```

Expected result: each entry shows the account used, the recipient, and the server response.

See [Setting Up msmtp for Sending](../tutorials/msmtp-setup) for the full setup tutorial and [Hooks](hooks) for more on NeoMutt hooks.
