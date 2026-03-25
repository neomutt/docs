---
title: "Address Options"
description: "Configuration variables for international domain name (IDN) encoding and decoding in email addresses."
keywords: "address, idn, international domain name, idn_decode, idn_encode, encoding, utf-8, rfc6531, email address"
---

# Address Options

(idn-decode)=
## `$idn_decode`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set idn_decode = yes
    ```
- **Scope:** IDN only

When _set_, NeoMutt will show you international domain names decoded.
Note: You can use IDNs for addresses even if this is _unset_.
This variable only affects decoding.

--------------------------------------------------------------------------------

(idn-encode)=
## `$idn_encode`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set idn_encode = yes
    ```

When _set_, NeoMutt will encode international domain names using IDN.
Unset this if your SMTP server can handle newer ([RFC6531](https://www.rfc-editor.org/rfc/rfc6531.html)) UTF-8 encoded domains.

