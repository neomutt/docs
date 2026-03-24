---
title: "Address Options"
description: "Reference for NeoMutt address configuration variables."
keywords: "address, contacts, address book, variables, neomutt"
---

# Address Options

--------------------------------------------------------------------------------

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

