---
title: hooks
description: YYY
keywords: [neomutt]
sidebar: true
difficulty: Beginner
time: 5 minutes
diataxis: Tutorial
last_updated: 2025-12-14
---

# Hooks

MUTT_FOLDER_HOOK               folder-hook       When entering a mailbox
MUTT_MBOX_HOOK                 mbox-hook         Move messages after reading them
MUTT_SEND_HOOK                 send-hook         When composing a new email
MUTT_FCC_HOOK                  fcc-hook          To save outgoing email
MUTT_FCC_HOOK | MUTT_SAVE_HOOK fcc-save-hook     Both fcc- and save-hook
MUTT_SAVE_HOOK                 save-hook         Set a default folder when saving an email
MUTT_CHARSET_HOOK              charset-hook      Create a charset alias for malformed emails
MUTT_ICONV_HOOK                iconv-hook        Create a system charset alias
MUTT_MESSAGE_HOOK              message-hook      Run before displaying a message
MUTT_CRYPT_HOOK                crypt-hook        Automatically select a PGP/SMIME key
MUTT_ACCOUNT_HOOK              account-hook      When changing between accounts
MUTT_REPLY_HOOK                reply-hook        When replying to an email
MUTT_SEND2_HOOK                send2-hook        When changing fields in the compose menu
MUTT_IDXFMTHOOK                index-format-hook Customise the format of the index
MUTT_TIMEOUT_HOOK              timeout-hook      Run a command periodically
MUTT_STARTUP_HOOK              startup-hook      Run when starting NeoMutt
MUTT_SHUTDOWN_HOOK             shutdown-hook     Run when leaving NeoMutt

MUTT_OPEN_HOOK                 open-hook         To read a compressed mailbox
MUTT_APPEND_HOOK               append-hook       Append to a compressed mailbox
MUTT_CLOSE_HOOK                close-hook        Write to a compressed mailbox

unhook

MUTT_CRYPT_HOOK pgp-hook (synonym for crypt-hook)

