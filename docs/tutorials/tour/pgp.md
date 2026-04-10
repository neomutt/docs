---
title: PGP Dialog
description: The classic OpenPGP key-selection dialog used when NeoMutt needs you to choose a key manually.
keywords: pgp, openpgp, key selection, verify key, classic pgp backend, encryption
---

(tour-pgp)=
# PGP Dialog

## Introduction -- Where am I?

The PGP Dialog is the classic OpenPGP key chooser.
It appears when NeoMutt's built-in PGP backend needs you to choose a key for signing or encryption.
If you are using GPGME instead, you will usually see the [GPGME Dialog](gpgme.md) instead of this one.

```{include} ../../_screenshots/pgp-dialog.html
```

## What am I looking at?

- Each row is a candidate key, showing trust, key size, key ID, algorithm, capabilities, and user ID.
- The highlighted row is the key NeoMutt will use if you select it.
- The status line shows which recipient address or search is being matched.

## What can I do?

- Choose the correct public key for encryption or the correct secret key identity for signing.
- Verify the selected key before using it.
- View the key's user ID in more detail.
- Cancel key selection and return to the sending workflow.
- Full reference: [Pgp Functions](menu-pgp).

## Where can I go next?

- Selecting a key returns you to the [Compose Dialog](compose.md) so sending can continue.
- Verifying a key can open one of the [Simple Pagers](simple.md).
- Cancelling returns you to the send flow without choosing a key.

## Where did I come from?

- You typically arrive from the [Compose Dialog](compose.md) when sending a signed or encrypted message.
- This dialog is most likely when NeoMutt is using the classic PGP backend rather than GPGME.

## How do I configure this?

- Start with [Encryption Config](ref-cfg-ncrypt) and [Send Config](ref-cfg-send).
- Common options include [`$crypt_use_gpgme`](cfg-crypt-use-gpgme), [`$pgp_default_key`](cfg-pgp-default-key), [`$pgp_entry_format`](cfg-pgp-entry-format), [`$pgp_key_sort`](cfg-pgp-key-sort), [`$pgp_long_ids`](cfg-pgp-long-ids), and [`$pgp_show_unusable`](cfg-pgp-show-unusable).
- Related commands include [`:crypt-hook`](cmd-crypt-hook) and generic [`:set`](cmd-set) configuration.
- Colours come from [Colour Objects](ref-colors), especially `indicator`, `status`, `message`, and `normal`.
