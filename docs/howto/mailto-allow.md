---
title: Use Mailto-Allow
description: Control which header fields NeoMutt accepts from mailto URLs for security
keywords: mailto, mailto-allow, unmailto-allow, header, security, URL
---

# Use Mailto-Allow

## Usage

```neomuttrc
mailto-allow { * | header-field... }
unmailto-allow { * | header-field... }
```

:::{note}
Before 2026-01-13, these commands were called `mailto_allow` and `unmailto_allow`.
:::

As a security measure, NeoMutt will only add user-approved header fields from a `mailto:` URL.
This is necessary since NeoMutt will handle certain header fields, such as `Attach:`, in a special way.
The `mailto-allow` and `unmailto-allow` commands allow the user to modify the list of approved headers.

NeoMutt initializes the default list to contain only the `Subject` and `Body` header fields, which are the only requirement specified by the `mailto:` specification in [RFC2368](https://www.rfc-editor.org/rfc/rfc2368.html), and the `Cc`, `In-Reply-To`, `References` headers to aid with replies to mailing lists.
