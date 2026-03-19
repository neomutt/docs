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


address.md
	  { "idn_decode", DT_BOOL, true, 0, NULL,
	  { "idn_encode", DT_BOOL, true, 0, NULL,

----------------------------------------------------------------------------------------------------------

(idn-decode)=
## `$idn_decode`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will show you international domain names decoded.
Note: You can use IDNs for addresses even if this is *unset*.
This variable only affects decoding. (IDN only)

----------------------------------------------------------------------------------------------------------

(idn-encode)=
## `$idn_encode`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will encode international domain names using
IDN.  Unset this if your SMTP server can handle newer ([RFC6531](https://www.rfc-editor.org/rfc/rfc6531.html))
UTF-8 encoded domains. (IDN only)

