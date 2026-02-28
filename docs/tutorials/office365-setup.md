---
title: "[TEMPLATE] Setting Up NeoMutt with Office 365"
description: Step-by-step guide to configure NeoMutt for use with Microsoft 365
keywords: [neomutt, office365, microsoft, imap, smtp, oauth2, tutorial]
status: template
---

# Setting Up NeoMutt with Office 365

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

- Prerequisites (Microsoft 365 account, OAuth registration)
- Configuring IMAP access for Office 365
- Setting up SMTP for Office 365
- OAuth2 authentication with Microsoft (required since Basic Auth deprecation)
- Reading and sending test emails
- Handling calendar invites and meeting requests
- Troubleshooting common Office 365 issues
:::

## Prerequisites

<!-- What the reader needs: a Microsoft 365 account, an Azure AD app
     registration for OAuth2 (required since Basic Auth was deprecated). -->

## Configure IMAP Access

<!-- Walk through the neomuttrc settings for Office 365 IMAP:
     folder, spoolfile, imap_user, and OAuth2 token helper. -->

## Set Up SMTP for Sending

<!-- Add SMTP settings for Office 365. Show smtp_url and authentication. -->

## Configure OAuth2 Authentication

<!-- Step-by-step Azure AD app registration, obtaining client ID/secret,
     and configuring NeoMutt's OAuth2 token script. Required path. -->

## Read and Send Test Emails

<!-- Launch NeoMutt, read a message, compose and send a test reply. -->

## Handle Calendar Invites

<!-- Brief guidance on viewing calendar invites and meeting requests
     that arrive as email attachments (ICS files). -->

## Troubleshooting

<!-- Common problems: OAuth token expiry, tenant restrictions,
     conditional access policies, MFA prompts. -->
