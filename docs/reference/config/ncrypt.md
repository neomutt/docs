---
title: Ncrypt Options
description: Config options for PGP and S/MIME cryptography, signing, encryption, GPGME, and protected headers.
keywords: neomutt, ncrypt, pgp, smime, gpgme, encryption, signing, cryptography, crypt_opportunistic_encrypt, protected headers, certificates, security
---

(ref-cfg-ncrypt)=
# Ncrypt Options

(cfg-crypt-confirm-hook)=
## `$crypt_confirm_hook`

:Description: Prompt the user to confirm keys before use
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set crypt_confirm_hook = yes
    ```

If set, then you will be prompted for confirmation of keys when using the _crypt-hook_ command.
If unset, no such confirmation prompt will be presented.
This is generally considered unsafe, especially where typos are concerned.

--------------------------------------------------------------------------------

(cfg-crypt-encryption-info)=
## `$crypt_encryption_info`

:Description: Add an informative block with details about the encryption
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_encryption_info = yes
    ```

If _set_, NeoMutt will include an informative block before an encrypted part, with details about the encryption.

--------------------------------------------------------------------------------

(cfg-crypt-opportunistic-encrypt)=
## `$crypt_opportunistic_encrypt`

:Description: Enable encryption when the recipient's key is available
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_opportunistic_encrypt = no
    ```

Setting this option will cause NeoMutt to automatically enable and disable encryption, based on whether all message recipient keys can be located by NeoMutt.

When this option is enabled, NeoMutt will enable/disable encryption each time the `To:`, `Cc:`, and `Bcc:` lists are edited.
If [`$edit_headers`](cfg-edit-headers) is set, NeoMutt will also do so each time the message is edited.

While this is set, encryption can't be manually enabled/disabled.
The pgp or smime menus provide a selection to temporarily disable this option for the current message.

If [`$crypt_auto_encrypt`](cfg-crypt-auto-encrypt) or [`$crypt_reply_encrypt`](cfg-crypt-reply-encrypt) enable encryption for a message, this option will be disabled for that message.
It can be manually re-enabled in the pgp or smime menus.

--------------------------------------------------------------------------------

(cfg-crypt-opportunistic-encrypt-strong-keys)=
## `$crypt_opportunistic_encrypt_strong_keys`

:Description: Enable encryption only when strong a key is available
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set crypt_opportunistic_encrypt_strong_keys = no
    ```

When set, this modifies the behavior of [`$crypt_opportunistic_encrypt`](cfg-crypt-opportunistic-encrypt) to only search for "strong keys", that is, keys with full validity according to the web-of-trust algorithm.
A key with marginal or no validity will not enable opportunistic encryption.

For S/MIME, the behavior depends on the backend.
Classic S/MIME will filter for certificates with the `t` (trusted) flag in the .index file.
The GPGME backend will use the same filters as with OpenPGP, and depends on GPGME's logic for assigning the GPGME_VALIDITY_FULL and GPGME_VALIDITY_ULTIMATE validity flag.

--------------------------------------------------------------------------------

(cfg-crypt-protected-headers-read)=
## `$crypt_protected_headers_read`

:Description: Display protected headers (Memory Hole) in the pager
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_protected_headers_read = yes
    ```

When set, NeoMutt will display protected headers ("Memory Hole") in the pager, and will update the index and header cache with revised headers.

Protected headers are stored inside the encrypted or signed part of an email, to prevent disclosure or tampering.
For more information see <https://github.com/autocrypt/protected-headers> Currently NeoMutt only supports the Subject header.

Encrypted messages using protected headers often substitute the exposed Subject header with a dummy value (see [`$crypt_protected_headers_subject`](cfg-crypt-protected-headers-subject)).
NeoMutt will update its concept of the correct subject **after** the message is opened, i.e. via the [`<display-message>`](ref-fn-index) function.
If you reply to a message before opening it, NeoMutt will end up using the dummy Subject header, so be sure to open such a message first.

--------------------------------------------------------------------------------

(cfg-crypt-protected-headers-save)=
## `$crypt_protected_headers_save`

:Description: Save the cleartext `Subject:` with the headers
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_protected_headers_save = no
    ```

When [`$crypt_protected_headers_read`](cfg-crypt-protected-headers-read) is set, and a message with a protected Subject is opened, NeoMutt will save the updated Subject into the header cache by default.
This allows searching/limiting based on the protected Subject header if the mailbox is re-opened, without having to re-open the message each time.
However, for mbox/mh mailbox types, or if header caching is not set up, you would need to re-open the message each time the mailbox was reopened before you could see or search/limit on the protected subject again.

When this option is set, NeoMutt additionally saves the protected Subject back **in the clear-text message headers**.
This provides better usability, but with the tradeoff of reduced security.
The protected Subject header, which may have previously been encrypted, is now stored in clear-text in the message headers.
Copying the message elsewhere, via NeoMutt or external tools, could expose this previously encrypted data.
Please make sure you understand the consequences of this before you enable this option.

--------------------------------------------------------------------------------

(cfg-crypt-protected-headers-subject)=
## `$crypt_protected_headers_subject`

:Description: Use this as the subject for encrypted emails
:Type: [String](type-string)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_protected_headers_subject = "..."
    ```

When [`$crypt_protected_headers_write`](cfg-crypt-protected-headers-write) is set, and the message is marked for encryption, this will be substituted into the Subject field in the message headers.

To prevent a subject from being substituted, unset this option, or set it to the empty string.

--------------------------------------------------------------------------------

(cfg-crypt-protected-headers-weed)=
## `$crypt_protected_headers_weed`

:Description: Controls whether NeoMutt will weed protected header fields
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_protected_headers_weed = no
    ```

Controls whether NeoMutt will weed protected header fields.

--------------------------------------------------------------------------------

(cfg-crypt-protected-headers-write)=
## `$crypt_protected_headers_write`

:Description: Generate protected header (Memory Hole) for signed and encrypted emails
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_protected_headers_write = yes
    ```

When set, NeoMutt will generate protected headers for signed and encrypted emails.

Protected headers are stored inside the encrypted or signed part of an email, to prevent disclosure or tampering.
For more information see <https://github.com/autocrypt/protected-headers>

Currently NeoMutt only supports the Subject header.

--------------------------------------------------------------------------------

(cfg-crypt-timestamp)=
## `$crypt_timestamp`

:Description: Add a timestamp to PGP or SMIME output to prevent spoofing
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_timestamp = yes
    ```

If _set_, NeoMutt will include a time stamp in the lines surrounding PGP or S/MIME output, so spoofing such lines is more difficult.
If you are using colors to mark these lines, and rely on these, you may _unset_ this setting.

--------------------------------------------------------------------------------

(cfg-crypt-use-gpgme)=
## `$crypt_use_gpgme`

:Description: Use GPGME crypto backend
:Type: [Boolean](type-bool)
:Notes: [On Startup](type-general)
:Default:
    ```neomuttrc
    set crypt_use_gpgme = yes
    ```

Control the use of the GPGME-enabled crypto backends.
If it is _set_ and NeoMutt was built with GPGME support, the gpgme code for S/MIME and PGP will be used instead of the classic code.

:::{note}
You need to set this option in `.neomuttrc`; it won't have any effect when used interactively.
:::

:::{note}
The GPGME backend does not support creating old-style inline (traditional) PGP encrypted or signed messages (see [`$pgp_auto_inline`](cfg-pgp-auto-inline)).
:::

--------------------------------------------------------------------------------

(cfg-crypt-use-pka)=
## `$crypt_use_pka`

:Description: Use GPGME to use PKA (lookup PGP keys using DNS)
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set crypt_use_pka = no
    ```

Controls whether NeoMutt uses PKA during signature verification (only supported by the GPGME backend).

:::{seealso}
<http://www.g10code.de/docs/pka-intro.de.pdf>
:::

--------------------------------------------------------------------------------

(cfg-crypt-verify-sig)=
## `$crypt_verify_sig`

:Description: Verify PGP or SMIME signatures
:Type: [Quad-Option](type-quad)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_verify_sig = yes
    ```

| Value   | Meaning                                           |
|---------|---------------------------------------------------|
| `yes`   | Always attempt to verify PGP or S/MIME signatures |
| `ask-*` | Ask whether or not to verify the signature        |
| `no`    | Never attempt to verify cryptographic signatures  |

--------------------------------------------------------------------------------

(cfg-envelope-from-address)=
## `$envelope_from_address`

:Description: Manually set the sender for outgoing messages
:Type: [Address](type-address)
:Default: (empty)
    ```neomuttrc
    set envelope_from_address = ""
    ```

Manually sets the _envelope_ sender for outgoing messages.
This value is ignored if [`$use_envelope_from`](cfg-use-envelope-from) is _unset_.

--------------------------------------------------------------------------------

(cfg-pgp-auto-decode)=
## `$pgp_auto_decode`

:Description: Automatically decrypt PGP messages
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set pgp_auto_decode = no
    ```

If _set_, NeoMutt will automatically attempt to decrypt traditional PGP messages whenever the user performs an operation which ordinarily would result in the contents of the message being operated on.
For example, if the user displays a pgp-traditional message which has not been manually checked with the [`<check-traditional-pgp>`](ref-fn-attach) function, NeoMutt will automatically check the message for traditional pgp.

--------------------------------------------------------------------------------

(cfg-pgp-auto-inline)=
## `$pgp_auto_inline`

:Description: Use old-style inline PGP messages (not recommended)
:Type: [Boolean](type-bool)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_auto_inline = no
    ```

Control whether NeoMutt generates old-style inline (traditional) PGP encrypted or signed messages under certain circumstances.
This can be overridden by use of the pgp menu, when inline is not required.
The GPGME backend does not support this option.

:::{note}
NeoMutt might automatically use PGP/MIME for messages which consist of more than a single MIME part.
NeoMutt can be configured to ask before sending PGP/MIME messages when inline (traditional) would not work.
:::

:::{seealso}
[`$pgp_mime_auto`](cfg-pgp-mime-auto)
:::

:::{warning}
Using the old-style PGP message format is **strongly** **deprecated**
:::

--------------------------------------------------------------------------------

(cfg-pgp-check-exit)=
## `$pgp_check_exit`

:Description: Check the exit code of PGP subprocess
:Type: [Boolean](type-bool)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_check_exit = yes
    ```

If _set_, NeoMutt will check the exit code of the PGP subprocess when signing or encrypting.
A non-zero exit code means that the subprocess failed.

--------------------------------------------------------------------------------

(cfg-pgp-check-gpg-decrypt-status-fd)=
## `$pgp_check_gpg_decrypt_status_fd`

:Description: File descriptor used for status info
:Type: [Boolean](type-bool)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_check_gpg_decrypt_status_fd = yes
    ```

If _set_, NeoMutt will check the status file descriptor output of [`$pgp_decrypt_command`](cfg-pgp-decrypt-command) and [`$pgp_decode_command`](cfg-pgp-decode-command) for GnuPG status codes indicating successful decryption.
This will check for the presence of DECRYPTION_OKAY, absence of DECRYPTION_FAILED, and that all PLAINTEXT occurs between the BEGIN_DECRYPTION and END_DECRYPTION status codes.

If _unset_, NeoMutt will instead match the status fd output against [`$pgp_decryption_okay`](cfg-pgp-decryption-okay).

--------------------------------------------------------------------------------

(cfg-pgp-clear-sign-command)=
## `$pgp_clear_sign_command`

:Description: External command to inline-sign a message
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_clear_sign_command = ""
    ```

:::{warning}
This format is used to create an old-style "clearsigned" PGP message.
Using the old-style PGP message format is **strongly** **deprecated**
:::

:::{note}
In this case, `%r` expands to the search string, which is a list of one or more quoted values such as email address, name, or keyid.
:::

:::{seealso}
- [`$pgp_decode_command`](cfg-pgp-decode-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pgp-decode-command)=
## `$pgp_decode_command`

:Description: External command to decode a PGP attachment
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_decode_command = ""
    ```

Specify the format of a command used to decode application/pgp attachments.

**Format Sequences**

| Short | Long Name         | Description                                                                                                         |
|-------|-------------------|---------------------------------------------------------------------------------------------------------------------|
| `%a`  | `%{sign-as}`      | Value of [`$pgp_sign_as`](cfg-pgp-sign-as) if set, otherwise the value of [`$pgp_default_key`](cfg-pgp-default-key) |
| `%f`  | `%{file-message}` | Expands to the name of a file containing a message                                                                  |
| `%p`  | `%{need-pass}`    | Expands to `PGPPASSFD=0` when a pass phrase is needed, to an empty string otherwise.                                |
| `%r`  | `%{key-ids}`      | One or more key IDs (or fingerprints if available) of a `multipart/signed` attachment when verifying it             |

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pgp-decryption-okay)=
## `$pgp_decryption_okay`

:Description: Text indicating a successful decryption
:Type: [Regular Expression](type-regex)
:Notes: [Smart Case](type-general)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_decryption_okay = ""
    ```

If you assign text to this option, then an encrypted PGP message is only considered successfully decrypted if the output from [`$pgp_decrypt_command`](cfg-pgp-decrypt-command) contains the text.
This is used to protect against a spoofed encrypted message, with multipart/encrypted headers but containing a block that is not actually encrypted.
(e.g. simply signed and ascii armored text).

:::{note}
If [`$pgp_check_gpg_decrypt_status_fd`](cfg-pgp-check-gpg-decrypt-status-fd) is set, this option is ignored.
:::

--------------------------------------------------------------------------------

(cfg-pgp-decrypt-command)=
## `$pgp_decrypt_command`

:Description: External command to decrypt a PGP message
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_decrypt_command = ""
    ```

This command is used to decrypt a PGP encrypted message.

:::{note}
When decrypting messages using `gpg`, a pinentry program needs to be invoked unless the password is cached within `gpg-agent`.
:::

Currently, the `pinentry-tty` program (usually distributed with `gpg`) isn't suitable for being invoked by NeoMutt.
You are encouraged to use a different pinentry-program when running NeoMutt in order to avoid problems.

:::{seealso}
- [`$pgp_decode_command`](cfg-pgp-decode-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
- <https://github.com/neomutt/neomutt/issues/1014>
:::

--------------------------------------------------------------------------------

(cfg-pgp-default-key)=
## `$pgp_default_key`

:Description: Default key to use for PGP operations
:Type: [String](type-string)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_default_key = ""
    ```

This is the default key-pair to use for PGP operations.
It will be used for encryption (see [`$postpone_encrypt`](cfg-postpone-encrypt) and [`$pgp_self_encrypt`](cfg-pgp-self-encrypt)).

It will also be used for signing unless [`$pgp_sign_as`](cfg-pgp-sign-as) is set.

--------------------------------------------------------------------------------

(cfg-pgp-encrypt-only-command)=
## `$pgp_encrypt_only_command`

:Description: External command to encrypt, but not sign a message
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_encrypt_only_command = ""
    ```

This command is used to encrypt a body part without signing it.

:::{note}
In this case, %r expands to the search string, which is a list of one or more quoted values such as email address, name, or keyid.
:::

:::{seealso}
- [`$pgp_decode_command`](cfg-pgp-decode-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pgp-encrypt-sign-command)=
## `$pgp_encrypt_sign_command`

:Description: External command to encrypt and sign a message
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_encrypt_sign_command = ""
    ```

This command is used to both sign and encrypt a body part.

:::{seealso}
- [`$pgp_decode_command`](cfg-pgp-decode-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pgp-entry-format)=
## `$pgp_entry_format`

:Description: Format string for the [PGP Key Dialog](tour-pgp)
:Type: [Expando](type-expando)
:Notes: [Not Empty](type-general), [Pipe Support](type-pipe)
:Scope: Crypto only or PGP only when GPGME disabled
:Default:
    ```neomuttrc
    set pgp_entry_format = "%4n %t%f %4l/0x%k %-4a %2c %u"
    ```
:Alternative:
    ```neomuttrc
    set pgp_entry_format = "%4{number} %{trust}%{key-flags} %4{key-length}/0x%{key-id} %-4{key-algorithm} %2{key-capabilities} %{user-id}"
    ```

Specify the format of the data displayed in the [`Pgp Dialog`](tour-pgp) and [`Gpgme Dialog`](tour-gpgme).

If [`$crypt_use_gpgme`](cfg-crypt-use-gpgme) is _set_, then it applies to S/MIME key selection menu also.

**Format Sequences**

| Short    | Long Name              | Description                                                                |
|----------|------------------------|----------------------------------------------------------------------------|
| `%a`     | `%{key-algorithm}`     | Algorithm                                                                  |
| `%c`     | `%{key-capabilities}`  | Capabilities                                                               |
| `%f`     | `%{key-flags}`         | Flags                                                                      |
| `%i`     | `%{key-fingerprint}`   | Key fingerprint (or long key id if non-existent)                           |
| `%k`     | `%{key-id}`            | Key id                                                                     |
| `%l`     | `%{key-length}`        | Key length                                                                 |
| `%n`     | `%{number}`            | Number                                                                     |
| `%p`     | `%{protocol}`          | Protocol                                                                   |
| `%t`     | `%{trust}`             | Trust/validity of the key-uid association                                  |
| `%u`     | `%{user-id}`           | User id                                                                    |
| `%A`     | `%{pkey-algorithm}`    | Primary Key Algorithm                                                      |
| `%C`     | `%{pkey-capabilities}` | Primary Key Capabilities                                                   |
| `%F`     | `%{pkey-flags}`        | Primary Key Flags                                                          |
| `%I`     | `%{pkey-fingerprint}`  | Primary Key fingerprint (or long key id if non-existent)                   |
| `%K`     | `%{pkey-id}`           | Primary Key id                                                             |
| `%L`     | `%{pkey-length}`       | Primary Key length                                                         |
| `%[fmt]` | `%{date}`              | Date of the key where `fmt` is an [`strftime(3)`](exp-strftime) expression |
| `%*X`    | `%{padding-soft:X}`    | Soft-fill with character `X` as padding                                    |
| `%>X`    | `%{padding-hard:X}`    | Right justify the rest of the string and pad with character `X`            |
| `%\|X`   | `%{padding-eol:X}`     | Pad to the end of the line with character `X`                              |

See the section "Sending Cryptographically Signed/Encrypted Messages" of the user manual for the meaning of the letters some of these sequences expand to.

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pgp-export-command)=
## `$pgp_export_command`

:Description: External command to export a public key from the user's keyring
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_export_command = ""
    ```

This command is used to export a public key from the user's key ring.

:::{seealso}
- [`$pgp_decode_command`](cfg-pgp-decode-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pgp-get-keys-command)=
## `$pgp_get_keys_command`

:Description: External command to download a key for an email address
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_get_keys_command = ""
    ```

This command is invoked whenever NeoMutt needs to fetch the public key associated with an email address.

:::{note}
Only The `%r` expando is used with this format.
In this case, %r expands to the email address, not the public key ID (the key ID is unknown, which is why NeoMutt is invoking this command).
:::

:::{seealso}
- [`$pgp_decode_command`](cfg-pgp-decode-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pgp-good-sign)=
## `$pgp_good_sign`

:Description: Text indicating a good signature
:Type: [Regular Expression](type-regex)
:Notes: [Smart Case](type-general)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_good_sign = ""
    ```

If you assign a text to this option, then a PGP signature is only considered verified if the output from [`$pgp_verify_command`](cfg-pgp-verify-command) contains the text.
Use this option if the exit code from the command is 0 even for bad signatures.

--------------------------------------------------------------------------------

(cfg-pgp-ignore-subkeys)=
## `$pgp_ignore_subkeys`

:Description: Only use the principal PGP key
:Type: [Boolean](type-bool)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_ignore_subkeys = yes
    ```

Setting this option will cause NeoMutt to ignore OpenPGP subkeys.
Instead, the principal key will inherit the subkeys' capabilities.
_Unset_ this if you want to play interesting key selection games.

--------------------------------------------------------------------------------

(cfg-pgp-import-command)=
## `$pgp_import_command`

:Description: External command to import a key into the user's keyring
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_import_command = ""
    ```

This command is used to import a key from a message into the user's public key ring.

:::{seealso}
- [`$pgp_decode_command`](cfg-pgp-decode-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pgp-key-sort)=
## `$pgp_key_sort`

:Description: Sort order for PGP keys
:Type: [Sort Order](type-sort-order)
:Notes: [Reverse](type-sort-order)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_key_sort = address
    ```

Specifies how the entries in the pgp menu are sorted.

| Value     | Sort by     |
|-----------|-------------|
| `address` | Address     |
| `date`    | Date        |
| `keyid`   | Key id      |
| `trust`   | Trust level |

--------------------------------------------------------------------------------

(cfg-pgp-list-pubring-command)=
## `$pgp_list_pubring_command`

:Description: External command to list the public keys in a user's keyring
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_list_pubring_command = ""
    ```

This command is used to list the public key ring's contents.
The output format must be analogous to the one used by:

```sh
gpg --list-keys --with-colons --with-fingerprint
```

:::{note}
gpg's `fixed-list-mode` option should not be used.
It produces a different date format which may result in NeoMutt showing incorrect key generation dates.
:::

:::{seealso}
- [`$pgp_decode_command`](cfg-pgp-decode-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pgp-list-secring-command)=
## `$pgp_list_secring_command`

:Description: External command to list the private keys in a user's keyring
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_list_secring_command = ""
    ```

This command is used to list the secret key ring's contents.
The output format must be analogous to the one used by:

```sh
gpg --list-keys --with-colons --with-fingerprint
```

:::{note}
gpg's `fixed-list-mode` option should not be used.
It produces a different date format which may result in NeoMutt showing incorrect key generation dates.
:::

:::{seealso}
- [`$pgp_decode_command`](cfg-pgp-decode-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pgp-long-ids)=
## `$pgp_long_ids`

:Description: Display long PGP key IDs to the user
:Type: [Boolean](type-bool)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_long_ids = yes
    ```

If _set_, use 64-bit PGP key IDs, if _unset_ use the normal 32-bit key IDs.

:::{note}
Internally, NeoMutt has transitioned to using fingerprints (or long key IDs as a fallback).
Now only controls the display of key IDs in the key selection menu and a few other places.
:::

--------------------------------------------------------------------------------

(cfg-pgp-mime-auto)=
## `$pgp_mime_auto`

:Description: Prompt the user to use MIME if inline PGP fails
:Type: [Quad-Option](type-quad)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_mime_auto = ask-yes
    ```

Control whether NeoMutt prompts to automatically send a (signed/encrypted) message using PGP/MIME when inline (traditional) fails (for any reason).

:::{warning}
Using the old-style PGP message format is **strongly** **deprecated**
:::

--------------------------------------------------------------------------------

(cfg-pgp-retainable-sigs)=
## `$pgp_retainable_sigs`

:Description: Create nested multipart/signed or encrypted messages
:Type: [Boolean](type-bool)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_retainable_sigs = no
    ```

If _set_, signed and encrypted messages will consist of nested `multipart/signed` and `multipart/encrypted` body parts.

This is useful for applications like encrypted and signed mailing lists, where the outer layer (`multipart/encrypted`) can be easily removed, while the inner `multipart/signed` part is retained.

--------------------------------------------------------------------------------

(cfg-pgp-self-encrypt)=
## `$pgp_self_encrypt`

:Description: Encrypted messages will also be encrypted to [`$pgp_default_key`](cfg-pgp-default-key) too
:Type: [Boolean](type-bool)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_self_encrypt = yes
    ```

When _set_, PGP encrypted messages will also be encrypted using the key in [`$pgp_default_key`](cfg-pgp-default-key).

--------------------------------------------------------------------------------

(cfg-pgp-show-unusable)=
## `$pgp_show_unusable`

:Description: Show non-usable keys in the key selection
:Type: [Boolean](type-bool)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_show_unusable = yes
    ```

If _set_, NeoMutt will display non-usable keys on the PGP key selection menu.
This includes keys which have been revoked, have expired, or have been marked as "disabled" by the user.

--------------------------------------------------------------------------------

(cfg-pgp-sign-as)=
## `$pgp_sign_as`

:Description: Use this alternative key for signing messages
:Type: [String](type-string)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_sign_as = ""
    ```

If you have a different key pair to use for signing, you should set this to the signing key.
Most people will only need to set [`$pgp_default_key`](cfg-pgp-default-key).
It is recommended that you use the keyid form to specify your key (e.g. `0x00112233`).

--------------------------------------------------------------------------------

(cfg-pgp-sign-command)=
## `$pgp_sign_command`

:Description: External command to create a detached PGP signature
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_sign_command = ""
    ```

This command is used to create the detached PGP signature for a `multipart/signed` PGP/MIME body part.

:::{seealso}
- [`$pgp_decode_command`](cfg-pgp-decode-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pgp-strict-enc)=
## `$pgp_strict_enc`

:Description: Encode PGP signed messages with quoted-printable (don't unset)
:Type: [Boolean](type-bool)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_strict_enc = yes
    ```

If _set_, NeoMutt will automatically encode PGP/MIME signed messages as quoted-printable.

:::{warning}
Unsetting this option may lead to problems with non-verifyable PGP signatures, so only change this if you know what you are doing
:::

--------------------------------------------------------------------------------

(cfg-pgp-timeout)=
## `$pgp_timeout`

:Description: Time in seconds to cache a passphrase
:Type: [Number (Long)](type-long)
:Notes: [Not Negative](type-general)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_timeout = 300
    ```

The number of seconds after which a cached passphrase will expire if not used.

--------------------------------------------------------------------------------

(cfg-pgp-use-gpg-agent)=
## `$pgp_use_gpg_agent`

:Description: Use a PGP agent for caching passwords
:Type: [Boolean](type-bool)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_use_gpg_agent = yes
    ```

If _set_, NeoMutt expects a `gpg-agent(1)` process will handle private key passphrase prompts.
If _unset_, NeoMutt will prompt for the passphrase and pass it via stdin to the pgp command.

:::{note}
As of version 2.1, GnuPG automatically spawns an agent and requires the agent be used for passphrase management.
Since that version is increasingly prevalent, this option now defaults _set_.
:::

NeoMutt works with a GUI or curses pinentry program.
A TTY pinentry should not be used.

If you are using an older version of GnuPG without an agent running, or another encryption program without an agent, you will need to _unset_ this option.

--------------------------------------------------------------------------------

(cfg-pgp-verify-command)=
## `$pgp_verify_command`

:Description: External command to verify PGP signatures
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_verify_command = ""
    ```

This command is used to verify PGP signatures.

:::{seealso}
- [`$pgp_decode_command`](cfg-pgp-decode-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pgp-verify-key-command)=
## `$pgp_verify_key_command`

:Description: External command to verify key information
:Type: [Expando (Command String)](type-expando)
:Scope: PGP only
:Default: (empty)
    ```neomuttrc
    set pgp_verify_key_command = ""
    ```

This command is used to verify key information from the key selection menu.

:::{seealso}
- [`$pgp_decode_command`](cfg-pgp-decode-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-smime-ask-cert-label)=
## `$smime_ask_cert_label`

:Description: Prompt the user for a label for SMIME certificates
:Type: [Boolean](type-bool)
:Scope: S/MIME only
:Default:
    ```neomuttrc
    set smime_ask_cert_label = yes
    ```

This flag controls whether you want to be asked to enter a label for a certificate about to be added to the database or not.
It is _set_ by default.

--------------------------------------------------------------------------------

(cfg-smime-ca-location)=
## `$smime_ca_location`

:Description: File containing trusted certificates
:Type: [Path (String)](type-path)
:Notes: [File only](type-path)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_ca_location = ""
    ```

Specify either a directory or a file containing trusted certificates for use with OpenSSL.

--------------------------------------------------------------------------------

(cfg-smime-certificates)=
## `$smime_certificates`

:Description: File containing user's public certificates
:Type: [Path (String)](type-path)
:Notes: [Directory only](type-path)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_certificates = ""
    ```

Since for S/MIME there is no pubring/secring as with PGP, NeoMutt has to handle storage and retrieval of keys by itself.
This is very basic right now, and keys and certificates are stored in two different directories, both named as the hash-value retrieved from OpenSSL.
There is an index file which contains mailbox-address keyid pairs, and which can be manually edited.
Point to the location of the certificates.

--------------------------------------------------------------------------------

(cfg-smime-decrypt-command)=
## `$smime_decrypt_command`

:Description: External command to decrypt an SMIME message
:Type: [Expando (Command String)](type-expando)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_decrypt_command = ""
    ```

Specify the format of a command used to decrypt `application/pkcs7-mime` attachments.

**Format Sequences**

| Short | Long Name             | Description                                                                                                                        |
|-------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------|
| `%a`  | `%{algorithm}`        | Algorithm used for encryption                                                                                                      |
| `%C`  | `%{certificate-path}` | CA location:  Depending on whether [`$smime_ca_location`](cfg-smime-ca-location) points to a directory or file,                    |
|       |                       | this expands to "-CApath [`$smime_ca_location`](cfg-smime-ca-location)" or "-CAfile [`$smime_ca_location`](cfg-smime-ca-location)" |
| `%c`  | `%{certificate-ids}`  | One or more certificate IDs                                                                                                        |
| `%d`  | `%{digest-algorithm}` | Message digest algorithm specified with [`$smime_sign_digest_alg`](cfg-smime-sign-digest-alg)                                      |
| `%f`  | `%{message-file}`     | Expands to the name of a file containing a message                                                                                 |
| `%i`  | `%{intermediate-ids}` | Intermediate certificates                                                                                                          |
| `%k`  | `%{key}`              | Key-pair specified with [`$smime_default_key`](cfg-smime-default-key)                                                              |
| `%s`  | `%{signature-file}`   | Expands to the name of a file containing the signature part                                                                        |
|       |                       | of a `multipart/signed` attachment when verifying it                                                                               |

For examples on how to configure these formats, see the `smime.rc` in the `samples/` subdirectory which has been installed on your system alongside the documentation.

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-smime-decrypt-use-default-key)=
## `$smime_decrypt_use_default_key`

:Description: Use the default key for decryption
:Type: [Boolean](type-bool)
:Scope: S/MIME only
:Default:
    ```neomuttrc
    set smime_decrypt_use_default_key = yes
    ```

If _set_ (default) this tells NeoMutt to use the default key for decryption.
Otherwise, if managing multiple certificate-key-pairs, NeoMutt will try to use the mailbox-address to determine the key to use.
It will ask you to supply a key, if it can't find one.

--------------------------------------------------------------------------------

(cfg-smime-default-key)=
## `$smime_default_key`

:Description: Default key for SMIME operations
:Type: [String](type-string)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_default_key = ""
    ```

This is the default key-pair to use for S/MIME operations, and must be set to the keyid (the hash-value that OpenSSL generates) to work properly.

It will be used for encryption (see [`$postpone_encrypt`](cfg-postpone-encrypt) and [`$smime_self_encrypt`](cfg-smime-self-encrypt)).
If GPGME is enabled, this is the key id displayed by gpgsm.

It will be used for decryption unless [`$smime_decrypt_use_default_key`](cfg-smime-decrypt-use-default-key) is _unset_.

It will also be used for signing unless [`$smime_sign_as`](cfg-smime-sign-as) is set.

--------------------------------------------------------------------------------

(cfg-smime-encrypt-command)=
## `$smime_encrypt_command`

:Description: External command to encrypt a message
:Type: [Expando (Command String)](type-expando)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_encrypt_command = ""
    ```

This command is used to create encrypted S/MIME messages.

Encrypt the message to [`$smime_default_key`](cfg-smime-default-key) too.

:::{seealso}
- [`$smime_decrypt_command`](cfg-smime-decrypt-command) for a full list of expandos
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-smime-encrypt-with)=
## `$smime_encrypt_with`

:Description: Algorithm for encryption
:Type: [String](type-string)
:Scope: S/MIME only
:Default:
    ```neomuttrc
    set smime_encrypt_with = "aes256"
    ```

This sets the algorithm that should be used for encryption.

| Algorithms | Notes                  |
|------------|------------------------|
| `aes256`   | Recommended            |
| `aes192`   |                        |
| `aes128`   | Still strong           |
| `des3`     | Legacy fallback        |
| `des`      | Unsafe: **Do not use** |
| `rc2-40`   | Unsafe: **Do not use** |
| `rc2-64`   | Unsafe: **Do not use** |
| `rc2-128`  | Unsafe: **Do not use** |

--------------------------------------------------------------------------------

(cfg-smime-get-cert-command)=
## `$smime_get_cert_command`

:Description: External command to extract a certificate from a message
:Type: [Expando (Command String)](type-expando)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_get_cert_command = ""
    ```

This command is used to extract X509 certificates from a PKCS7 structure.

:::{seealso}
- [`$smime_decrypt_command`](cfg-smime-decrypt-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-smime-get-cert-email-command)=
## `$smime_get_cert_email_command`

:Description: External command to get a certificate for an email
:Type: [Expando (Command String)](type-expando)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_get_cert_email_command = ""
    ```

This command is used to extract the mail address(es) used for storing X509 certificates, and for verification purposes (to check whether the certificate was issued for the sender's mailbox).

:::{seealso}
- [`$smime_decrypt_command`](cfg-smime-decrypt-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-smime-get-signer-cert-command)=
## `$smime_get_signer_cert_command`

:Description: External command to extract a certificate from an email
:Type: [Expando (Command String)](type-expando)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_get_signer_cert_command = ""
    ```

This command is used to extract only the signers X509 certificate from a S/MIME signature, so that the certificate's owner may get compared to the email's `From:` field.

:::{seealso}
- [`$smime_decrypt_command`](cfg-smime-decrypt-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-smime-import-cert-command)=
## `$smime_import_cert_command`

:Description: External command to import a certificate
:Type: [Expando (Command String)](type-expando)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_import_cert_command = ""
    ```

This command is used to import a certificate via smime_keys.

:::{note}
`%c` and `%k` will default to [`$smime_sign_as`](cfg-smime-sign-as) if set, otherwise [`$smime_default_key`](cfg-smime-default-key).
:::

:::{seealso}
- [`$smime_decrypt_command`](cfg-smime-decrypt-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-smime-is-default)=
## `$smime_is_default`

:Description: Use SMIME rather than PGP by default
:Type: [Boolean](type-bool)
:Scope: S/MIME only
:Default:
    ```neomuttrc
    set smime_is_default = no
    ```

The default behavior of NeoMutt is to use PGP on all auto-sign/encryption operations.
To override and to use OpenSSL instead this must be _set_.
However, this has no effect while replying, since NeoMutt will automatically select the same application that was used to sign/encrypt the original message.

:::{note}
Can be overridden by unsetting [`$crypt_auto_smime`](cfg-crypt-auto-smime)
:::

--------------------------------------------------------------------------------

(cfg-smime-keys)=
## `$smime_keys`

:Description: File containing user's private certificates
:Type: [Path (String)](type-path)
:Notes: [Directory only](type-path)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_keys = ""
    ```

Since for S/MIME there is no pubring/secring as with PGP, NeoMutt has to handle storage and retrieval of keys/certs by itself.
This is very basic right now, and stores keys and certificates in two different directories, both named as the hash-value retrieved from OpenSSL.
There is an index file which contains mailbox-address keyid pair, and which can be manually edited.
Point to the location of the private keys.

--------------------------------------------------------------------------------

(cfg-smime-pk7out-command)=
## `$smime_pk7out_command`

:Description: External command to extract a public certificate
:Type: [Expando (Command String)](type-expando)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_pk7out_command = ""
    ```

This command is used to extract PKCS7 structures of S/MIME signatures, in order to extract the public X509 certificate(s).

:::{seealso}
- [`$smime_decrypt_command`](cfg-smime-decrypt-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-smime-self-encrypt)=
## `$smime_self_encrypt`

:Description: Encrypted messages will also be encrypt to [`$smime_default_key`](cfg-smime-default-key) too
:Type: [Boolean](type-bool)
:Scope: S/MIME only
:Default:
    ```neomuttrc
    set smime_self_encrypt = yes
    ```

When _set_, S/MIME encrypted messages will also be encrypted using the certificate in [`$smime_default_key`](cfg-smime-default-key).

--------------------------------------------------------------------------------

(cfg-smime-sign-as)=
## `$smime_sign_as`

:Description: Use this alternative key for signing messages
:Type: [String](type-string)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_sign_as = ""
    ```

If you have a separate key to use for signing, you should set this to the signing key.
Most people will only need to set [`$smime_default_key`](cfg-smime-default-key).

--------------------------------------------------------------------------------

(cfg-smime-sign-command)=
## `$smime_sign_command`

:Description: External command to sign a message
:Type: [Expando (Command String)](type-expando)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_sign_command = ""
    ```

This command is used to created S/MIME signatures of type `multipart/signed`, which can be read by all mail clients.

:::{seealso}
- [`$smime_decrypt_command`](cfg-smime-decrypt-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-smime-sign-digest-alg)=
## `$smime_sign_digest_alg`

:Description: Digest algorithm
:Type: [String](type-string)
:Scope: S/MIME only
:Default:
    ```neomuttrc
    set smime_sign_digest_alg = "sha256"
    ```

This sets the algorithm that should be used for the signature message digest.

| Algorithms | Notes                  |
|------------|------------------------|
| `sha512`   |                        |
| `sha384`   |                        |
| `sha256`   | Recommended default    |
| `sha224`   |                        |
| `sha1`     | Unsafe: **Do not use** |
| `md5`      | Unsafe: **Do not use** |

--------------------------------------------------------------------------------

(cfg-smime-timeout)=
## `$smime_timeout`

:Description: Time in seconds to cache a passphrase
:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Scope: S/MIME only
:Default:
    ```neomuttrc
    set smime_timeout = 300
    ```

The number of seconds after which a cached passphrase will expire if not used.

--------------------------------------------------------------------------------

(cfg-smime-verify-command)=
## `$smime_verify_command`

:Description: External command to verify a signed message
:Type: [Expando (Command String)](type-expando)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_verify_command = ""
    ```

This command is used to verify S/MIME signatures of type `multipart/signed`.

:::{seealso}
- [`$smime_decrypt_command`](cfg-smime-decrypt-command) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-smime-verify-opaque-command)=
## `$smime_verify_opaque_command`

:Description: External command to verify a signature
:Type: [Expando (Command String)](type-expando)
:Scope: S/MIME only
:Default: (empty)
    ```neomuttrc
    set smime_verify_opaque_command = ""
    ```

This command is used to verify S/MIME signatures of type `application/pkcs7-mime`.

:::{seealso}
- [`$smime_decrypt_command`](cfg-smime-decrypt-command) for a full list of expandos
 -**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

