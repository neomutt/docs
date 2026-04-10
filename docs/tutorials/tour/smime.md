---
title: S/MIME Dialog
description: The S/MIME certificate-selection dialog used when NeoMutt needs a certificate for signing or encryption.
keywords: smime, certificate selection, signing, encryption, verify key, x509
---

(tour-smime)=
# S/MIME Dialog

## Introduction -- Where am I?

The S/MIME Dialog is the certificate chooser for S/MIME mail.
It appears when NeoMutt needs you to choose a certificate for encryption or signing and multiple candidates are available.
Unlike the [PGP Dialog](pgp.md), the entries here are X.509-style certificates rather than OpenPGP keys.

```{include} ../../_screenshots/s-mime-dialog.html
```

## What am I looking at?

- Each row is a candidate certificate with key ID, capabilities, validity state, email address, and label.
- The highlighted row is the certificate NeoMutt will use if you select it.
- The status line shows which recipient address the certificate list is matching.

## What can I do?

- Choose the right certificate for encryption or signing.
- Verify the selected certificate before using it.
- View the certificate's user name or label in more detail.
- Cancel and return to the send workflow.
- Full reference: [Smime Functions](menu-smime).

## Where can I go next?

- Selecting a certificate returns you to the [Compose Dialog](compose.md) so sending can continue.
- Verifying a certificate can open one of the [Simple Pagers](simple.md).
- Cancelling returns you to the send flow.

## Where did I come from?

- You typically arrive from the [Compose Dialog](compose.md) when sending with S/MIME enabled.
- If GPGME is the active backend, NeoMutt may show the [GPGME Dialog](gpgme.md) instead of this one.

## How do I configure this?

- Start with [Encryption Config](ref-cfg-ncrypt) and [Send Config](ref-cfg-send).
- Common options include [`$smime_default_key`](cfg-smime-default-key), [`$smime_certificates`](cfg-smime-certificates), [`$smime_keys`](cfg-smime-keys), [`$smime_ask_cert_label`](cfg-smime-ask-cert-label), [`$smime_is_default`](cfg-smime-is-default), and [`$smime_ca_location`](cfg-smime-ca-location).
- Related commands include [`:crypt-hook`](cmd-crypt-hook) and generic [`:set`](cmd-set) configuration.
- Colours come from [Colour Objects](ref-colors), especially `indicator`, `status`, `message`, and `normal`.
