---
title: Avoid Common Crypto Pitfalls
description: Fix the most common OpenPGP and S/MIME issues in NeoMutt
keywords: gpgme, pgp, smime, pinentry, gpg-agent, crypto
---

# Avoid Common Crypto Pitfalls

## Prerequisites

1. NeoMutt built with crypto support.
2. GnuPG installed.

## Fix Pinentry Problems

NeoMutt does not work with the `tty` pinentry program.

1. Install a GUI or curses pinentry (for example `pinentry-curses`).
2. Configure `gpg-agent`:

```sh
pinentry-program /usr/bin/pinentry-curses
```

Expected result: passphrase prompts appear correctly when signing or decrypting.

## Prefer GPGME Over Classic Mode

1. Enable GPGME:

```neomuttrc
set crypt_use_gpgme
```

2. Restart NeoMutt.

Expected result: OpenPGP and S/MIME use the modern GPGME backend.

## Ensure Keys Are Available

1. Verify your default keys are set:

```neomuttrc
set pgp_default_key = "YOURKEYID"
set smime_default_key = "YOURCERTID"
```

Expected result: NeoMutt can pick keys without prompting every time.

## Resolve S/MIME Trust Issues

1. If S/MIME certificates are not trusted, import root certificates into GnuPG (`gpgsm --import`).
2. Verify the trust list if signatures fail.

Expected result: S/MIME verification succeeds for trusted senders.

See [How to Use PGP Encryption](pgp) and [How to Use S/MIME](smime).
