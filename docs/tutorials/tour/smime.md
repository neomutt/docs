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

<div class="term-window">
<div class="term-title">S/MIME Dialog</div>
<pre class="terminal" role="img" aria-label="Screenshot of NeoMutt's S/MIME Dialog listing candidate certificates with key IDs, capabilities, validity states such as Verified, Trusted, and Expired, email addresses, and labels.">
<span>0x1A2B3C4D5E6F es Verified   langstroth@langstroth.com           Personal 2025                      </span>
<span>0x2B3C4D5E6F7A es Trusted    l.langstroth@hivemail.org           Work Certificate                   </span>
<span>0x3C4D5E6F7A8B e- Unverified langstroth.bee@apiary.net           Apiary Systems                     </span>
<span>0x4D5E6F7A8B9C -s Expired    rev.langstroth@phila.edu            Old University Key                 </span>
<span>0x5E6F7A8B9C0D es Unknown    langstroth@beekeepers-assoc.org     Association Key                    </span>
<span>0x6F7A8B9C0D1E -- Revoked    ll1851@historical-mail.com          Legacy Key                         </span>
<span>0x7A8B9C0D1E2F es Verified   lorenzo.langstroth@gmail.com        Gmail Key 2024                     </span>
<span>0x8B9C0D1E2F3A es Invalid    langstroth@expired-domain.com       Defunct Org                        </span>
<span>                                                                                                    </span>
<span class="status">S/MIME certificates matching "langstroth@langstroth.com"                                            </span>
<span>                                                                                                    </span>
</pre>
</div>

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
