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

MUTT_FOLDER_HOOK   folder-hook: when entering a mailbox
MUTT_MBOX_HOOK     mbox-hook: move messages after reading them
MUTT_SEND_HOOK     send-hook: when composing a new email
MUTT_FCC_HOOK      fcc-hook: to save outgoing email
MUTT_SAVE_HOOK     save-hook: set a default folder when saving an email
MUTT_CHARSET_HOOK  charset-hook: create a charset alias for malformed emails
MUTT_ICONV_HOOK    iconv-hook: create a system charset alias
MUTT_MESSAGE_HOOK  message-hook: run before displaying a message
MUTT_CRYPT_HOOK    crypt-hook: automatically select a PGP/SMIME key
MUTT_ACCOUNT_HOOK  account-hook: when changing between accounts
MUTT_REPLY_HOOK    reply-hook: when replying to an email
MUTT_SEND2_HOOK    send2-hook: when changing fields in the compose menu
MUTT_OPEN_HOOK     open-hook: to read a compressed mailbox
MUTT_APPEND_HOOK   append-hook: append to a compressed mailbox
MUTT_CLOSE_HOOK    close-hook: write to a compressed mailbox
MUTT_IDXFMTHOOK    index-format-hook: customise the format of the index
MUTT_TIMEOUT_HOOK  timeout-hook: run a command periodically
MUTT_STARTUP_HOOK  startup-hook: run when starting NeoMutt
MUTT_SHUTDOWN_HOOK shutdown-hook: run when leaving NeoMutt

account-hook      MUTT_ACCOUNT_HOOK
charset-hook      MUTT_CHARSET_HOOK
crypt-hook        MUTT_CRYPT_HOOK
fcc-hook          MUTT_FCC_HOOK
fcc-save-hook     MUTT_FCC_HOOK      | MUTT_SAVE_HOOK
folder-hook       MUTT_FOLDER_HOOK
iconv-hook        MUTT_ICONV_HOOK
index-format-hook MUTT_IDXFMTHOOK
mbox-hook         MUTT_MBOX_HOOK
message-hook      MUTT_MESSAGE_HOOK
pgp-hook          MUTT_CRYPT_HOOK
reply-hook        MUTT_REPLY_HOOK
save-hook         MUTT_SAVE_HOOK
send-hook         MUTT_SEND_HOOK
send2-hook        MUTT_SEND2_HOOK
shutdown-hook     MUTT_SHUTDOWN_HOOK
startup-hook      MUTT_STARTUP_HOOK
timeout-hook      MUTT_TIMEOUT_HOOK
unhook

