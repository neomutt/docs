---
title: GPGME Dialog
description: The unified GPGME key-selection dialog for choosing OpenPGP or S/MIME keys during send.
keywords: gpgme, pgp, smime, key selection, verify key, unified crypto backend
---

(tour-gpgme)=
# GPGME Dialog

## Introduction -- Where am I?

The GPGME Dialog is the key chooser used when NeoMutt relies on the GPGME library for cryptography.
It can represent either OpenPGP or S/MIME keys, depending on what the current send operation needs.
In other words, it is the modern, unified version of the backend-specific [PGP Dialog](pgp.md) and [S/MIME Dialog](smime.md).

<div class="term-window">
<div class="term-title">GPGME Dialog</div>
<pre class="terminal">
<span>   1 u  4096/0x7224725C RSA  es Jim Smith (backup) &lt;jim@example.com&gt;                                </span>
<span>   2 u  4096/0x7224725C RSA  es Jim Smith (backup) &lt;jim@example.com&gt;                                </span>
<span>   3 f  4096/0x810582F5 RSA  es James Smith (flatcap) &lt;jim@example.com&gt;                             </span>
<span>   4 f  4096/0x810582F5 RSA  es James Smith (flatcap) &lt;jim@example.com&gt;                             </span>
<span>   5 f  4096/0x810582F5 RSA  es James Smith (flatcap) &lt;jim@example.com&gt;                             </span>
<span>                                                                                                    </span>
<span class="status">PGP keys matching &lt;jim@example.com&gt;                                                                 </span>
<span>                                                                                                    </span>
</pre>
</div>

## What am I looking at?

- Each row is a candidate key or certificate, showing trust, key size, key ID, algorithm, capabilities, and user ID.
- The highlighted row is the identity GPGME will use for the current send step.
- The status line shows which address or lookup produced the candidate list.

## What can I do?

- Choose the correct key or certificate for encryption or signing.
- Verify key details before accepting them.
- Inspect the selected identity's displayed user name.
- Cancel and return to the send workflow.
- Full reference: [Pgp Functions](menu-pgp), [Smime Functions](menu-smime).

## Where can I go next?

- Selecting a key returns you to the [Compose Dialog](compose.md) so sending can proceed.
- Verifying a key can open one of the [Simple Pagers](simple.md).
- Cancelling returns you to the compose/send flow without a final key choice.

## Where did I come from?

- You typically arrive from the [Compose Dialog](compose.md) during sending when [`$crypt_use_gpgme`](cfg-crypt-use-gpgme) is enabled.
- The exact crypto mode may have started as a PGP choice or an S/MIME choice in compose.

## How do I configure this?

- Start with [Encryption Config](ref-cfg-ncrypt) and [Send Config](ref-cfg-send).
- Common options include [`$crypt_use_gpgme`](cfg-crypt-use-gpgme), [`$crypt_auto_encrypt`](cfg-crypt-auto-encrypt), [`$crypt_auto_sign`](cfg-crypt-auto-sign), [`$pgp_default_key`](cfg-pgp-default-key), and [`$smime_default_key`](cfg-smime-default-key).
- Related commands include [`:crypt-hook`](cmd-crypt-hook) and generic [`:set`](cmd-set) configuration.
- Colours come from [Colour Objects](ref-colors), especially `indicator`, `status`, `message`, and `normal`.
