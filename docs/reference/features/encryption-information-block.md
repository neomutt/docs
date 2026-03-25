---
title: Encryption Information Block
description: Display a block showing encryption recipient key details when viewing an encrypted message in NeoMutt
keywords: neomutt, encryption, pgp, smime, gpgme, crypt_encryption_info, recipient keys, encrypted message, pager, security, decryption
since: 2024-04-10
---

# Encryption Information Block

*Show a block of encryption information about a message*

## Support

**Since:** NeoMutt 2024-04-10

**Dependencies:** Gpgme

## Introduction

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

## Usage

It's enabled by default. The variable to control it is
`crypt_encryption_info`.

## Credits

Alejandro Colomar, Richard Russon, наб
