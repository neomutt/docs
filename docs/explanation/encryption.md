---
title: Understanding Encryption
description: How NeoMutt encrypts and signs email using GPGME, OpenPGP, and S/MIME, including classic mode and the command-line crypto feature
keywords: encryption, gpgme, pgp, smime, signing, cryptography, security, $pgp_default_key, $smime_default_key, crypt_use_gpgme, pinentry, gnupg, cli-crypto, digital signatures
diataxis_type: explanation
---

# Understanding Encryption

NeoMutt supports encrypting and signing emails when used interactively.
In batch mode, cryptographic operations are disabled, so these options can't be used to sign an email sent via a cron job, for instance.

The recommended way to enable OpenPGP and S/MIME is to use GPGME.
This library is integrated into NeoMutt and can perform all the common crypto functions the user will need.

```neomuttrc
# Enable GPGME
set crypt_use_gpgme
```

If you have complex crypto needs, then you can enable the "classic mode" by disabling GPGME and setting all `pgp_command_*` and `smime_command_*` config options.

For example config, see: `gpg.rc` and `smime.rc` in the [Contrib repository](https://github.com/neomutt/neomutt-contrib/).

```neomuttrc
# Use manual crypto functions
unset crypt_use_gpgme
set pgp_clear_sign_command = "..."
# ...
set smime_decrypt_command = "..."
# ...
```

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Encrypted and signed message indicators

**Description:** The NeoMutt index screen showing several messages with different security states: a PGP-signed message (showing the signature status flag), a PGP-encrypted message, and an unsigned/unencrypted message for contrast.
Then the pager view of a signed message showing the signature verification status line (e.g. "Good signature from...").

**Highlights:** The reader should notice the security indicator flags in the index (e.g. "s" for signed, "S" for encrypted) and the signature verification output in the pager, showing how NeoMutt surfaces cryptographic status to the user.
:::

## OpenPGP Configuration

The two most important settings are `$pgp_default_key` and `$pgp_sign_as`.
To perform encryption, you must set the first variable.
If you have a separate signing key, or only have a signing key, then set the second.
Most people will only need to set `$pgp_default_key`.

Starting with version 2.1.0, GnuPG automatically uses an `agent` to prompt for your passphrase.
If you are using a version older than that, you'll need to ensure an agent is running (alternatively, you can unset `$pgp_use_gpg_agent` and NeoMutt will prompt you for your passphrase).
The agent in turn uses a `pinentry` program to display the prompt.
There are many different kinds of pinentry programs that can be used: qt, gtk2, gnome3, fltk, and curses.
However, NeoMutt does *not* work properly with the tty pinentry program.
Please ensure you have one of the GUI or curses pinentry programs installed and configured to be the default for your system.

## S/MIME Configuration

As with OpenPGP, the two most important settings are `$smime_default_key` and `$smime_sign_as`.
To perform encryption and decryption, you must set the first variable.
If you have a separate signing key, or only have a signing key, then set the second.
Most people will only need to set `$smime_default_key`.

When using GPGME as S/MIME backend, keys and certificates are managed by GnuPG.
You can add your key (or certificates) to GnuPG with the command `gpgsm --import mykey.p12`.
Note that in order to use the key for signing or encrypting, the root certificate of that key must be trusted, which might involve editing `~/.gnupg/trustlist.txt`.
Consult your documentation of GnuPG for details, in particular `gpgsm`.

In "classic mode", keys and certificates are managed by the `smime_keys` program that comes with NeoMutt.
By default they are stored under `~/.smime/`. (This is set by the `smime.rc` file with `$smime_certificates` and `$smime_keys`.) To initialize this directory, use the command `smime_keys init` from a shell prompt.
The program can then be used to import and list certificates.
You may also want to periodically run `smime_keys refresh` to update status flags for your certificates.

## Command-line Crypto (-C) Feature

*Enable message security in modes that by default don't enable it*

### Support

**Since:** NeoMutt 2024-01-21

**Dependencies:** Gpgme

### Introduction

This feature allows enabling message security in modes that don't enable it by default.
Those include batch mode, sending a postponed message, and resending a message.

This allows using NeoMutt as a driver for git-send-email(1), to send patches in signed and/or encrypted mail.

### Usage

To send an email from a file, enabling cryptographic operations as when sending interactively, simply use the `-C` flag.

```sh
$ neomutt -C -H - < /mail/to/be/sent
```neomuttrc

### neomuttrc

```
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

### gitconfig

```dosini
# Example .gitconfig config file for the cli-crypto feature.

[sendemail]
sendmailcmd = neomutt -C -H - && true
```

## Credits

Alejandro Colomar, Richard Russon, Jenya Sovetkin
