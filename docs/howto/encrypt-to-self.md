---
title: "How to Encrypt to Self"
description: Save a self-encrypted copy of outgoing emails and view encryption information
keywords: [neomutt, encrypt-to-self, pgp, smime, fcc, self-encrypt, encryption-info]
---

# How to Encrypt to Self

## The Problem

Once you encrypt an email to someone you cannot read it. This is good for
security, but bad for record-keeping. If you wanted to keep a copy of an
encrypted email you could set `$fcc_clear`.

A better option is to encrypt the saved copy to yourself.

## Setting Up Self-Encryption with S/MIME

1. Enable S/MIME self-encryption:

   ```
   set smime_self_encrypt = yes
   set smime_default_key  = bb345e23.0
   ```

2. If you have a different key for signing, set it separately:

   ```
   set smime_sign_as = "SMIME-SIGNING-KEY"
   ```

## Setting Up Self-Encryption with PGP

1. Enable PGP self-encryption:

   ```
   set pgp_self_encrypt = yes
   set pgp_default_key  = A4AF18C5582473BD35A1E9CE78BB3D480042198E
   ```

2. If you have a different key for signing, set it separately:

   ```
   set pgp_sign_as = "PGP-SIGNING-KEY"
   ```

## Variables

| Name | Type | Default |
|------|------|---------|
| `pgp_default_key` | string | (empty) |
| `pgp_self_encrypt` | boolean | `yes` |
| `pgp_sign_as` | string | (empty) |
| `smime_default_key` | string | (empty) |
| `smime_self_encrypt` | boolean | `yes` |
| `smime_sign_as` | string | (empty) |

## Example neomuttrc

```neomuttrc
# Example NeoMutt config file for the encrypt-to-self feature.

# --------------------------------------------------------------------------
# VARIABLES – shown with their default values
# --------------------------------------------------------------------------
# Save a copy of outgoing email, encrypted to yourself
set pgp_self_encrypt = "yes"
set pgp_default_key = "PGP-KEY"
# set pgp_sign_as = "PGP-SIGNING-KEY"

# Save a copy of outgoing email, encrypted to yourself
set smime_self_encrypt = "yes"
set smime_default_key = "SMIME-KEY"
# set smime_sign_as = "SMIME-SIGNING-KEY"

# vim: filetype=neomuttrc
```

## Known Bugs

None

## Credits

Omen Wild, Richard Russon, Guillaume Brogi

---

## Encryption Information Block

*Show a block of encryption information about a message*

### Support

**Since:** NeoMutt 2024-04-10

**Dependencies:** Gpgme

### Introduction

This feature shows a block of information that provides information about an
encrypted message; mainly about its recipients. Here is an example of such a
block:

```
[-- Begin encryption information --]
Recipient: RSA key, ID 00C14A7DBBDD521C
Recipient: RSA key, ID 0000000000000000
[-- End encryption information --]
```

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Encryption information block in pager

**Description:** The NeoMutt pager displaying a decrypted email with the encryption information block visible. The block shows "[-- Begin encryption information --]" and "[-- End encryption information --]" markers with recipient key details (e.g., "Recipient: RSA key, ID 00C14A7DBBDD521C") between them.

**Highlights:** The encryption information block integrated into the message display, showing how recipient key IDs appear when viewing an encrypted message with `$crypt_encryption_info` enabled.
:::

### Usage

It's enabled by default. The variable to control it is
`crypt_encryption_info`.

### Credits

Alejandro Colomar, Richard Russon, наб
