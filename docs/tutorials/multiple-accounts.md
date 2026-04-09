---
title: Managing Multiple Email Accounts
description: Configure two or more IMAP accounts and switch between them using folder-hook, account-hook, and the sidebar
keywords: neomutt, multiple accounts, folder-hook, account-hook, send-hook, sidebar, named-mailboxes, identity, credentials, imap, account switching, multi-account
---

# Managing Multiple Email Accounts

In this tutorial you will configure two IMAP accounts and switch between them reliably.

If you haven't connected a first account yet, start with [Writing Your First Configuration](first-config) or the guided [Start Here](../start-here) page.

## Why Multiple Accounts?

You might have a personal and a work account, or multiple accounts for different roles.
NeoMutt can switch settings automatically based on the mailbox you enter.

If one of your accounts is Gmail or Office 365, follow those setup tutorials for the provider-specific settings, then return here to combine them.

## Set Up Folder-Hooks for Account Switching

1. Add two folder hooks, one per account:

```neomuttrc
folder-hook imaps://imap.work.example/ "set folder=imaps://imap.work.example/; set spoolfile=+INBOX; set record=+Sent; set from=work@example.com; set signature=~/.neomutt/sig-work"
folder-hook imaps://imap.personal.example/ "set folder=imaps://imap.personal.example/; set spoolfile=+INBOX; set record=+Sent; set from=me@example.com; set signature=~/.neomutt/sig-personal"
```

2. Restart NeoMutt.

Expected result: when you enter a mailbox on each server, the identity settings change automatically.

## Use Account-Hook for Credentials

1. Add account hooks to set credentials per server:

```neomuttrc
account-hook imaps://imap.work.example/ "set imap_user=work@example.com"
account-hook imaps://imap.personal.example/ "set imap_user=me@example.com"
```

2. Use `account_command` or encrypted helpers for passwords.

Expected result: NeoMutt uses the right credentials for each server.

## Organise Mailboxes per Account

1. Declare mailboxes for each account:

```neomuttrc
mailboxes imaps://imap.work.example/INBOX
mailboxes imaps://imap.personal.example/INBOX
```

2. Add labels if you want friendly names:

```neomuttrc
named-mailboxes "Work INBOX" "imaps://imap.work.example/INBOX"
named-mailboxes "Personal INBOX" "imaps://imap.personal.example/INBOX"
```

Expected result: both accounts appear in mailbox lists and the sidebar.

## Configure Sender Identities

1. Set identity variables inside each `folder-hook`.
2. Optionally add a `send-hook` for specific addresses:

```neomuttrc
send-hook '~f work@example.com' "set from=work@example.com"
```

Expected result: the correct sender appears in outgoing mail.

## Switch Between Accounts

1. Open the Work INBOX, then switch to Personal INBOX.
2. Press `?` to verify the active settings if needed.

Expected result: each mailbox uses its own identity and settings.

## Use the Sidebar for Navigation

1. Enable the sidebar:

```neomuttrc
set sidebar_visible
```

2. Use sidebar navigation keys to move between mailboxes.

Expected result: you can switch accounts without typing mailbox URLs.

## Next Steps

- "I want to send from the right identity every time." See [Config Paradigms](../explanation/config-paradigms) and [Hooks](../howto/hooks).
- "I want to make mailbox switching easier." See [Sidebar Workflows](../howto/sidebar/sidebar-workflows).
