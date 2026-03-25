---
title: Setting Up NeoMutt with Office 365
description: Step-by-step guide to configure NeoMutt for use with Microsoft 365
keywords: [neomutt, office365, microsoft, imap, smtp, oauth2, tutorial]
---

# Setting Up NeoMutt with Office 365

This tutorial configures an Exchange Online account using OAuth2 for IMAP and SMTP.
If you're brand new to NeoMutt, read [Getting Started](getting-started) first.

## Prerequisites

1. A Microsoft 365 account (work or school).
2. An Azure app registration for OAuth2 (client ID and secret if required).
3. NeoMutt installed with IMAP and SMTP support.
4. The `mutt_oauth2.py` helper script from the NeoMutt contrib directory.

If you don't already have an Azure app registration, follow the Microsoft docs linked below.

## Configure IMAP Access

1. Add IMAP settings:

```neomuttrc
set imap_user = "you@yourdomain.com"
set folder = "imaps://outlook.office365.com/"
set spoolfile = "+INBOX"
```

2. Confirm NeoMutt can open the mailbox.

Expected result: the Office 365 inbox appears in the index.

## Set Up SMTP for Sending

1. Add SMTP settings:

```neomuttrc
set smtp_url = "smtp://smtp.office365.com:587/"
```

Expected result: NeoMutt is configured to send via Office 365 SMTP.

## Configure OAuth2 Authentication

Office 365 requires OAuth2 for IMAP/SMTP.
Use `mutt_oauth2.py` to obtain tokens.

1. Register an OAuth app in Azure and note the client ID (and secret if used).
2. Authorize tokens with `mutt_oauth2.py` (see its README for the exact command).
3. Configure NeoMutt to use OAuth:

```neomuttrc
set imap_authenticators = "oauthbearer:xoauth2"
set imap_oauth_refresh_command = "/path/to/mutt_oauth2.py you@yourdomain.com.tokens --provider microsoft"
set smtp_oauth_refresh_command = "$imap_oauth_refresh_command"
```

Expected result: NeoMutt authenticates to IMAP and SMTP without storing a password.

For safer storage of secrets, see [Password Manager](../howto/password-manager).

## Read and Send Test Emails

1. Start NeoMutt and open the inbox.
2. Compose a message to yourself and send it.

Expected result: the message appears in Sent Items and arrives in your inbox.

## Handle Calendar Invites

1. Open a message with a calendar invite.
2. Save the `.ics` attachment and open it with your calendar tool.

Expected result: the invite is visible in your calendar tool.

## Troubleshooting

If login fails:

1. Confirm your tenant allows IMAP/SMTP OAuth access.
2. Re-run `mutt_oauth2.py` authorization if tokens expired.
3. Verify server names and ports.

References:

- Exchange Online OAuth2 for IMAP/SMTP: https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth
- Exchange Online server settings: https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/incorrect-settings-in-outlook-desktop-application

## Next Steps

- "I want a quick tour of NeoMutt." See [Getting Started](getting-started).
- "I want to read and send mail." Continue with [Reading Your First Email](first-email) and [Sending Email](sending-email).
- "I want multiple accounts." Continue with [Multiple Accounts](multiple-accounts).
