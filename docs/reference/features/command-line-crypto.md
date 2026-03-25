---
title: Command-line Crypto
description: Enable PGP signing and encryption when sending email from the command line, batch mode, or git-send-email
keywords: encryption, gpgme, pgp, smime, signing, crypto, security, batch mode, command line, cli-crypto, git-send-email, crypt_autosign, crypt_opportunistic_encrypt, -C flag
since: 2024-01-21
---

# Command-line Crypto

*Enable message security in modes that by default don't enable it*

## Support

**Since:** NeoMutt 2024-01-21

**Dependencies:** Gpgme

## Introduction

This feature allows enabling message security in modes that don't enable it by default.
Those include batch mode, sending a postponed message, and resending a message.

This allows using NeoMutt as a driver for git-send-email(1), to send patches in signed
and/or encrypted mail.

## Usage

To send an email from a file, enabling cryptographic operations as when sending
interactively, simply use the `-C` flag.

```sh
$ neomutt -C -H - < /mail/to/be/sent
```neomuttrc

## neomuttrc

```neomuttrc
# Example NeoMutt config file for the cli-crypto feature.

set pgp_default_key = "1111111111111111111111111111111111111111"
# Sign all mail
set crypt_autosign = yes
# Encrypt mail if all recipients have valid public keys
set crypt_opportunistic_encrypt = yes
# Self encrypt mail
set crypt_self_encrypt = yes

# vim: filetype=neomuttrc
```

## gitconfig

```dosini
# Example .gitconfig config file for the cli-crypto feature.

[sendemail]
sendmailcmd = neomutt -C -H - && true
```

## Credits

Alejandro Colomar, Richard Russon, Jenya Sovetkin
