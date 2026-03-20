---
title: "Autocrypt Options"
description: "Reference for NeoMutt autocrypt configuration variables."
keywords: "autocrypt, encryption, variables, neomutt"
---

# Autocrypt Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

--------------------------------------------------------------------------------

(autocrypt)=
## `$autocrypt`

- **Type:** boolean
- **Default:** no

When _set_, enables autocrypt, which provides passive encryption protection with keys exchanged via headers.
See "$autocryptdoc" for more details.
(Autocrypt only)

--------------------------------------------------------------------------------

(autocrypt-acct-format)=
## `$autocrypt_acct_format`

- **Type:** string
- **Default:** "`%4n %-30a %20p %10s`"

This variable describes the format of the "autocrypt account" menu.
The following `printf(3)`-style sequences are understood 

| Short  | Long Name           | Description                                                     |
|--------|---------------------|-----------------------------------------------------------------|
| `%a`   | `%{address}`        | Email address                                                   |
| `%k`   | `%{keyid}`          | GPG keyid                                                       |
| `%n`   | `%{number}`         | Current entry number                                            |
| `%p`   | `%{prefer-encrypt}` | Prefer-encrypt flag                                             |
| `%s`   | `%{enabled}`        | Status flag (active/inactive)                                   |
| `%*X`  | `%{padding-soft:X}` | Soft-fill with character `X` as pad                             |
| `%>X`  | `%{padding-hard:X}` | Right justify the rest of the string and pad with character `X` |
| `%\|X` | `%{padding-eol:X}`  | Pad to the end of the line with character `X`                   |

(Autocrypt only)

--------------------------------------------------------------------------------

(autocrypt-dir)=
## `$autocrypt_dir`

- **Type:** path
- **Default:** "`~/.mutt/autocrypt`"

This variable sets where autocrypt files are stored, including the GPG keyring and SQLite database.
See "$autocryptdoc" for more details.
(Autocrypt only)

--------------------------------------------------------------------------------

(autocrypt-reply)=
## `$autocrypt_reply`

- **Type:** boolean
- **Default:** yes

When _set_, replying to an autocrypt email automatically enables autocrypt in the reply.
You may want to unset this if you're using the same key for autocrypt as normal web-of-trust, so that autocrypt isn't forced on for all encrypted replies.
(Autocrypt only)

