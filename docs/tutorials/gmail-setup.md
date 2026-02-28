---
title: "[TEMPLATE] Setting Up NeoMutt with Gmail"
description: Step-by-step guide to configure NeoMutt for use with Gmail
keywords: [neomutt, gmail, imap, smtp, oauth2, tutorial]
status: template
---

# Setting Up NeoMutt with Gmail

:::{admonition} Diátaxis: Tutorial
:class: note

Write as a **lesson**. Guide the learner through a meaningful exercise step by step.
Use second person ("you"). Show concrete actions and their expected results.
Don't explain concepts — demonstrate them through doing. Start with the simplest case
and build complexity gradually. The reader should feel a sense of accomplishment at the end.
:::

:::{admonition} Template — Content Needed
:class: warning

This page is a **placeholder**. The following content needs to be written:

- Prerequisites (Gmail account, app password or OAuth)
- Creating a minimal neomuttrc for Gmail IMAP
- Setting up SMTP for sending through Gmail
- Configuring OAuth2 authentication (recommended over app passwords)
- Reading your first email from Gmail
- Sending a test email
- Troubleshooting common Gmail issues (2FA, less secure apps, OAuth token refresh)
:::

## Prerequisites

<!-- What the reader needs before starting: a Gmail account, 2FA enabled,
     an app password or OAuth client credentials. -->

## Create a Minimal Configuration for Gmail IMAP

<!-- Walk through writing a neomuttrc that connects to Gmail's IMAP server.
     Show the exact settings: imap_user, folder, spoolfile, etc. -->

## Set Up SMTP for Sending

<!-- Add SMTP settings so the reader can send mail through Gmail.
     Show smtp_url, smtp_pass, and a test send. -->

## Configure OAuth2 Authentication

<!-- Recommended path. Walk through obtaining OAuth2 credentials and
     configuring NeoMutt to use them instead of app passwords. -->

## Read Your First Email

<!-- Have the reader launch NeoMutt, open their inbox, and read a message.
     Describe what they should see on screen. -->

## Send a Test Email

<!-- Compose and send a short test message. Verify it arrives. -->

## Troubleshooting

<!-- Common problems: 2FA blocking access, "less secure apps" setting,
     OAuth token refresh failures, connection timeouts. -->
