---
title: "Address Options"
description: "Reference for NeoMutt address configuration variables."
keywords: "address, contacts, address book, variables, neomutt"
---

# Address Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

--------------------------------------------------------------------------------

(idn-decode)=
## `$idn_decode`

- **Type:** boolean
- **Default:** yes
- **Scope:** IDN only

When _set_, NeoMutt will show you international domain names decoded.
Note: You can use IDNs for addresses even if this is _unset_.
This variable only affects decoding.

--------------------------------------------------------------------------------

(idn-encode)=
## `$idn_encode`

- **Type:** boolean
- **Default:** yes

When _set_, NeoMutt will encode international domain names using IDN.
Unset this if your SMTP server can handle newer (RFC6531) UTF-8 encoded domains.

