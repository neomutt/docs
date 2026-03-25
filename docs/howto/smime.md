---
title: "How to Use S/MIME"
description: Configure and use S/MIME encryption and signing for email in NeoMutt
keywords: [neomutt, smime, certificates, gpgsm, encryption, signing, x509]
---

# How to Use S/MIME

## Prerequisites

- NeoMutt compiled with GPGME support (recommended) or classic S/MIME mode
- An S/MIME certificate (`.p12` file) from a certificate authority
- GnuPG with `gpgsm` installed (for GPGME mode)

## Enabling GPGME

The recommended way to enable S/MIME is to use GPGME:

```neomuttrc
# Enable GPGME
set crypt_use_gpgme
```

If you have complex crypto needs, you can enable "classic mode" by disabling GPGME and setting all `smime_command_*` config options.
For example config, see `smime.rc` in the [Contrib repository](https://github.com/neomutt/neomutt-contrib/).

```neomuttrc
# Use manual crypto functions
unset crypt_use_gpgme
set smime_decrypt_command = "..."
# ...
```

## Configuring Your S/MIME Key

As with OpenPGP, the two most important settings are `$smime_default_key` and `$smime_sign_as`.
To perform encryption and decryption, you must set the first variable.
If you have a separate signing key, or only have a signing key, then set the second.
Most people will only need to set `$smime_default_key`.

```neomuttrc
set smime_default_key = "bb345e23.0"
```

## Importing Keys with GPGME

When using GPGME as the S/MIME backend, keys and certificates are managed by GnuPG.
You can add your key (or certificates) to GnuPG with the command:

```sh
gpgsm --import mykey.p12
```

Note that in order to use the key for signing or encrypting, the root certificate of that key must be trusted, which might involve editing `~/.gnupg/trustlist.txt`.
Consult your documentation of GnuPG for details, in particular `gpgsm`.

## Managing Keys in Classic Mode

In "classic mode", keys and certificates are managed by the `smime_keys` program that comes with NeoMutt.
By default they are stored under `~/.smime/`. (This is set by the `smime.rc` file with `$smime_certificates` and `$smime_keys`.)

1. Initialize the key directory from a shell prompt:

   ```sh
   smime_keys init
   ```

2. Use the program to import and list certificates.

3. Periodically run the following command to update status flags for your certificates:

   ```sh
   smime_keys refresh
   ```

## Sending Signed/Encrypted Messages

If you have told NeoMutt to S/MIME encrypt a message, it will guide you through a key selection process when you try to send the message.
NeoMutt will not ask you any questions about keys which have a certified user ID matching one of the message recipients' mail addresses.
However, there may be situations in which there are several keys, weakly certified user ID fields, or where no matching keys can be found.

In these cases, you are dropped into a menu with a list of keys from which you can select one.
When you quit this menu, or NeoMutt can't find any matching keys, you are prompted for a user ID.
You can abort this prompt using `^G`, and NeoMutt will return to the compose screen.

Once you have successfully finished the key selection, the message will be encrypted using the selected public keys when sent out.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** S/MIME certificate selection menu

**Description:** The NeoMutt S/MIME key selection menu that appears when sending an encrypted message.
The menu lists S/MIME certificates with key IDs, trust information, and associated email addresses.

**Highlights:** The certificate list layout and the prompt for selecting a certificate or entering a user ID manually.
Press `^G` to abort and return to the compose screen.
:::

To ensure you can view encrypted messages you have sent, you may wish to set `$smime_self_encrypt` and `$smime_default_key`.
