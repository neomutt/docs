---
title: Setting Up NeoMutt with Gmail
description: Step-by-step guide to configure NeoMutt for use with Gmail
keywords: [neomutt, gmail, imap, smtp, oauth2, tutorial]
---

# Setting Up NeoMutt with Gmail

This tutorial walks you through a working Gmail setup using IMAP + SMTP and OAuth2.
If you're brand new to NeoMutt, read [Getting Started](getting-started) first.

## Prerequisites

1. A Gmail account.
2. IMAP enabled in Gmail settings.
3. OAuth2 credentials for Gmail, or an app password if your account allows it.
4. NeoMutt installed with IMAP and SMTP support.

If you're unsure about any prerequisite, the links in the References section point to Gmail's
current instructions.

## Create a Minimal Configuration for Gmail IMAP

1. Create a minimal Gmail config:

```neomuttrc
set imap_user = "you@gmail.com"
set folder = "imaps://imap.gmail.com/"
set spoolfile = "+INBOX"
set postponed = "+[Gmail]/Drafts"
set record = "+[Gmail]/Sent Mail"
set trash = "+[Gmail]/Trash"
```

If your Gmail labels use different names, adjust the folder paths accordingly.

2. Start NeoMutt and confirm the mailbox opens.

Expected result: your Gmail inbox appears in the index.

## Set Up SMTP for Sending

1. Add SMTP settings:

```neomuttrc
set smtp_url = "smtps://you@gmail.com@smtp.gmail.com:465/"
```

2. If you are using app passwords, add:

```neomuttrc
set smtp_pass = "your-app-password"
```

Expected result: NeoMutt can send mail via Gmail SMTP.

## Configure OAuth2 Authentication

Gmail supports OAuth2 SASL for IMAP and SMTP. NeoMutt delegates token handling to an external helper. The NeoMutt repo includes `mutt_oauth2.py` for this purpose.

1. Generate tokens using `mutt_oauth2.py` (see the script README for details).
2. Configure NeoMutt to use OAuth:

```neomuttrc
set imap_authenticators = "oauthbearer:xoauth2"
set imap_oauth_refresh_command = "/path/to/mutt_oauth2.py you@gmail.com.tokens"
set smtp_oauth_refresh_command = "$imap_oauth_refresh_command"
```

Expected result: NeoMutt authenticates without storing a long-lived password.

For safer storage of secrets, see [Password Manager](../howto/password-manager).

## Read Your First Email

1. Start NeoMutt.
2. Open the inbox and press `Enter` on a message.

Expected result: the pager shows the message content.

## Send a Test Email

1. Press `m` to compose a new message.
2. Send it to yourself.

Expected result: the message arrives in your inbox and appears in the Sent folder.

## Troubleshooting

If authentication fails:

1. Confirm IMAP access is enabled in Gmail settings.
2. Re-run `mutt_oauth2.py` authorization if tokens expired.
3. If using app passwords, confirm 2-step verification is enabled and the app password is valid.

References:

- Gmail IMAP settings and server details: https://support.google.com/a/answer/9003945
- Gmail OAuth2 and IMAP/SMTP configuration: https://developers.google.com/gmail/imap/imap-smtp
- App passwords: https://support.google.com/accounts/answer/185833

## Next Steps

- "I want a quick tour of NeoMutt." See [Getting Started](getting-started).
- "I want to read and send mail." Continue with [Reading Your First Email](first-email) and [Sending Email](sending-email).
- "I want to search and filter." Continue with [Searching and Filtering Email](searching-email).
