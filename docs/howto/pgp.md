---
title: "How to Use PGP Encryption"
description: Configure and use OpenPGP encryption for signing and encrypting email in NeoMutt
keywords: [neomutt, pgp, openpgp, gpg, gpgme, encryption, signing, keys]
---

# How to Use PGP Encryption

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

## Prerequisites

- NeoMutt compiled with GPGME support (recommended) or classic PGP mode
- GnuPG installed (version 2.1.0 or later recommended for automatic agent support)
- A PGP key pair generated with `gpg --gen-key`

## Enabling GPGME

The recommended way to enable OpenPGP is to use GPGME:

```
# Enable GPGME
set crypt_use_gpgme
```

If you have complex crypto needs, you can enable "classic mode" by disabling
GPGME and setting all `pgp_command_*` config variables. For example config,
see `gpg.rc` in the [Contrib repository](https://github.com/neomutt/neomutt-contrib/).

```
# Use manual crypto functions
unset crypt_use_gpgme
set pgp_clear_sign_command = "..."
...
```

## Configuring Your PGP Key

The two most important settings are `$pgp_default_key` and `$pgp_sign_as`.
To perform encryption, you must set the first variable. If you have a separate
signing key, or only have a signing key, then set the second. Most people will
only need to set `$pgp_default_key`.

```
set pgp_default_key = "A4AF18C5582473BD35A1E9CE78BB3D480042198E"
```

## Configuring GnuPG Agent and Pinentry

Starting with version 2.1.0, GnuPG automatically uses an `agent` to prompt
for your passphrase. If you are using a version older than that, you'll need
to ensure an agent is running (alternatively, you can unset `$pgp_use_gpg_agent`
and NeoMutt will prompt you for your passphrase). The agent in turn uses a
`pinentry` program to display the prompt.

There are many different kinds of pinentry programs that can be used: qt, gtk2,
gnome3, fltk, and curses. However, NeoMutt does *not* work properly with the
tty pinentry program. Please ensure you have one of the GUI or curses pinentry
programs installed and configured to be the default for your system.

## Sending Cryptographically Signed/Encrypted Messages

If you have told NeoMutt to PGP encrypt a message, it will guide you through
a key selection process when you try to send the message. NeoMutt will not ask
you any questions about keys which have a certified user ID matching one of the
message recipients' mail addresses. However, there may be situations in which
there are several keys, weakly certified user ID fields, or where no matching
keys can be found.

In these cases, you are dropped into a menu with a list of keys from which you
can select one. When you quit this menu, or NeoMutt can't find any matching
keys, you are prompted for a user ID. You can, as usual, abort this prompt
using `^G`. When you do so, NeoMutt will return to the compose screen.

Once you have successfully finished the key selection, the message will be
encrypted using the selected public keys when sent out.

To ensure you can view encrypted messages you have sent, you may wish to set
`$pgp_self_encrypt` and `$pgp_default_key` for PGP, or `$smime_self_encrypt`
and `$smime_default_key` for S/MIME.

## Key Selection Menu

Most fields of the entries in the key selection menu (see also
`$pgp_entry_format`) have obvious meanings. The following sections explain the
capabilities, flags, and validity fields.

### PGP Key Menu Flags

The flags sequence (`%f`) will expand to one of the following flags:

| Flag | Description |
|------|-------------|
| R | The key has been revoked and can't be used. |
| X | The key is expired and can't be used. |
| d | You have marked the key as disabled. |
| c | There are unknown critical self-signature packets. |

### Key Capabilities

The capabilities field (`%c`) expands to a two-character sequence representing
a key's capabilities.

The first character gives the key's encryption capabilities:

- `-` — the key cannot be used for encryption
- `.` — marked as a signature key in one of the user IDs, but may also be used for encryption
- `e` — the key can be used for encryption

The second character indicates the key's signing capabilities:

- `-` — not for signing
- `.` — marked as an encryption key in one of the user IDs
- `s` — the key can be used for signing

### Key Validity

The validity field (`%t`) indicates how well-certified a user ID is. Its values
depend on the backend used. Note that S/MIME (which uses X509 certificates) has
no concept of validity, so this field simply shows `x`.

| Flag (classic PGP) | Flag (GPGME) | Description |
|---------------------|--------------|-------------|
| N/A | ? | unknown validity |
| ? | q | undefined validity |
| - | n | never valid key (untrusted association) |
| (space) | m | marginal validity (partially trusted) |
| + | f | full validity (fully trusted) |
| N/A | u | ultimate validity |
| N/A | x | the entry is an X509 certificate (S/MIME) |
