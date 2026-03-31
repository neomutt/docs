---
title: Autocrypt Options
description: Configuration variables for the Autocrypt automatic key exchange and encryption feature.
keywords: autocrypt, encryption, automatic encryption, key exchange, autocrypt_dir, autocrypt_reply, autocrypt_acct_format, gpg, passive encryption, e2e
---

(cfg-autocrypt)=
# Autocrypt Options

(autocrypt)=
## `$autocrypt`

:Type: [Boolean](bool)
:Scope: Autocrypt only
:Default:
    ```neomuttrc
    set autocrypt = no
    ```

When _set_, enables autocrypt, which provides passive encryption protection with keys exchanged via headers.
See "$autocryptdoc" for more details.

--------------------------------------------------------------------------------

(autocrypt-acct-format)=
## `$autocrypt_acct_format`

:Type: [Expando](expando)
:Scope: Autocrypt only
:Default:
    ```neomuttrc
    set autocrypt_acct_format = "%4n %-30a %20p %10s"
    ```
:Alternative:
    ```neomuttrc
    set autocrypt_acct_format = "%4{number} %-30{address} %20{prefer-encrypt} %10{enabled}"
    ```

This variable describes the format of the "autocrypt account" menu.
The following `printf(3)`-style sequences are understood:

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

--------------------------------------------------------------------------------

(autocrypt-dir)=
## `$autocrypt_dir`

:Type: [Path (String)](path)
:Notes: [Directory only](path)
:Scope: Autocrypt only
:Default:
    ```neomuttrc
    set autocrypt_dir = "~/.mutt/autocrypt"
    ```

This variable sets where autocrypt files are stored, including the GPG keyring and SQLite database.
See "$autocryptdoc" for more details.

--------------------------------------------------------------------------------

(autocrypt-reply)=
## `$autocrypt_reply`

:Type: [Boolean](bool)
:Scope: Autocrypt only
:Default:
    ```neomuttrc
    set autocrypt_reply = yes
    ```

When _set_, replying to an autocrypt email automatically enables autocrypt in the reply.
You may want to unset this if you're using the same key for autocrypt as normal web-of-trust, so that autocrypt isn't forced on for all encrypted replies.

