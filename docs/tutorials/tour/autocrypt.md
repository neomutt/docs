---
title: Autocrypt Dialog
description: The Autocrypt account manager for reviewing and toggling automatic encryption accounts.
keywords: autocrypt, encryption, account manager, prefer-encrypt, key exchange
---

(tour-autocrypt)=
# Autocrypt Dialog

## Introduction -- Where am I?

The Autocrypt Dialog manages the local accounts NeoMutt uses for Autocrypt.
Autocrypt is an opportunistic email-encryption standard that exchanges public keys automatically in message headers.
This dialog is where you review which addresses participate and how strongly they prefer encryption.

<div class="term-window">
<div class="term-title">Autocrypt Dialog</div>
<pre class="terminal">
<span>   1 john@example.com                     prefer encrypt     active                                 </span>
<span>   2 rich@flatcap.org                     prefer encrypt     active                                 </span>
<span>                                                                                                    </span>
<span>                                                                                                    </span>
<span class="status">Autocrypt Accounts                                                                                  </span>
<span>                                                                                                    </span>
</pre>
</div>

## What am I looking at?

- Each row shows an Autocrypt account email address, its encryption preference, and whether the account is active.
- The highlighted row is the account that will be toggled or deleted.
- The status line keeps the focus on account management rather than message reading.

## What can I do?

- Create a new Autocrypt account.
- Toggle whether the current account is active.
- Toggle the account's prefer-encrypt setting.
- Delete accounts that are no longer needed.
- Full reference: [Autocrypt Functions](menu-autocrypt).

## Where can I go next?

- `q` returns to the [Index Dialog](index2.md).
- The effect of your changes is usually seen later in the [Compose Dialog](compose.md) when sending mail.

## Where did I come from?

- You normally arrive from the [Index Dialog](index2.md) via `<autocrypt-acct-menu>`.
- Some Autocrypt-related compose workflows start in [Compose Dialog](compose.md), but account management itself lives here.

## How do I configure this?

- Start with [Autocrypt Config](ref-cfg-autocrypt), [Encryption Config](ref-cfg-ncrypt), and [Send Config](ref-cfg-send).
- Common options include [`$autocrypt`](cfg-autocrypt), [`$autocrypt_acct_format`](cfg-autocrypt-acct-format), [`$autocrypt_dir`](cfg-autocrypt-dir), and [`$autocrypt_reply`](cfg-autocrypt-reply).
- Per-account or per-message behavior can also be influenced with generic commands such as [`:set`](cmd-set), [`:send-hook`](cmd-send-hook), and [`:crypt-hook`](cmd-crypt-hook).
- Colours come from [Colour Objects](ref-colors), especially `indicator`, `status`, `message`, and `normal`.
