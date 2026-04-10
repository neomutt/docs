---
title: Certificate Dialog
description: The SSL/TLS certificate review prompt used when NeoMutt cannot verify a server certificate automatically.
keywords: certificate, tls, ssl, verify host, fingerprints, accept once, accept always
---

(tour-certificate)=
# Certificate Dialog

## Introduction -- Where am I?

The Certificate Dialog appears when NeoMutt cannot verify a mail server's TLS certificate automatically.
It pauses the connection so you can inspect the certificate and decide whether to trust it.
You might see it while opening a mailbox, checking mail, or sending through SMTP.

```{include} ../../_screenshots/certificate-dialog.html
```

## What am I looking at?

- The certificate subject tells you which host or service the certificate claims to represent.
- The issuer section shows which certificate authority signed it.
- The validity section shows the start and end dates for the certificate.
- The SHA1 and SHA256 fingerprints give you stable values you can verify out of band.
- The prompt line offers the trust decision: reject, accept once, or accept always.

## What can I do?

- Inspect the certificate's identity, issuer, validity dates, and fingerprints.
- Reject the certificate and stop the connection.
- Accept it for the current session only.
- Accept it permanently so NeoMutt records the certificate for future connections.
- Full reference: [Dialog Functions](menu-dialog).

## Where can I go next?

- Accepting or rejecting returns you to the operation that was trying to connect, usually the [Index Dialog](index2.md), [Browser Dialog](browser.md), or [Compose Dialog](compose.md).
- A permanent accept stores trust information so the dialog does not reappear for the same certificate unless something changes.

## Where did I come from?

- This dialog is entered automatically during an IMAP, POP, SMTP, or NNTP connection when certificate verification is incomplete or fails.
- The immediate caller is often mailbox open, mailbox sync, or message send, not a direct user command.

## How do I configure this?

- Start with [Conn Options](ref-cfg-conn).
- Common options include [`$certificate_file`](cfg-certificate-file), [`$ssl_ca_certificates_file`](cfg-ssl-ca-certificates-file), [`$ssl_use_system_certs`](cfg-ssl-use-system-certs), [`$ssl_verify_host`](cfg-ssl-verify-host), [`$ssl_verify_dates`](cfg-ssl-verify-dates), [`$ssl_starttls`](cfg-ssl-starttls), and [`$ssl_force_tls`](cfg-ssl-force-tls).
- Most policy changes happen through [`:set`](cmd-set) rather than dedicated commands.
- Colours come from [Colour Objects](ref-colors), especially `prompt`, `options`, `message`, `warning`, `error`, and `status`.
