---
title: Address Options
description: Configuration variables for international domain name (IDN) encoding and decoding in email addresses.
keywords: address, idn, international domain name, idn_decode, idn_encode, encoding, utf-8, rfc6531, email address
---

(ref-cfg-address)=
# Address Options

(cfg-idn-decode)=
## `$idn_decode`

:Description: Decode international domain names
:Type: [Boolean](type-bool)
:Scope: IDN only
:Default:
    ```neomuttrc
    set idn_decode = yes
    ```

When _set_, NeoMutt will show you international domain names decoded.

This variable only affects decoding.

:::{note}
You can use IDNs for addresses even if this is _unset_.
:::

--------------------------------------------------------------------------------

(cfg-idn-encode)=
## `$idn_encode`

:Description: Encode international domain names
:Type: [Boolean](type-bool)
:Scope: IDN only
:Default:
    ```neomuttrc
    set idn_encode = yes
    ```

When _set_, NeoMutt will encode international domain names using IDN.

Unset this if your SMTP server can handle newer ([RFC6531](https://www.rfc-editor.org/rfc/rfc6531.html)) UTF-8 encoded domains.

