---
title: Ncrypt Options
description: NeoMutt configuration variables for Ncrypt-format mailbox handling.
keywords: neomutt, ncrypt, ncrypt_purge, ncrypt_seq_flagged, ncrypt_seq_replied, ncrypt_seq_unseen, configuration
---

# Ncrypt Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

--------------------------------------------------------------------------------

(crypt-confirm-hook)=
## `$crypt_confirm_hook`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set crypt_confirm_hook = yes
    ```

If set, then you will be prompted for confirmation of keys when using the _crypt-hook_ command.
If unset, no such confirmation prompt will be presented.
This is generally considered unsafe, especially where typos are concerned.

--------------------------------------------------------------------------------

(crypt-encryption-info)=
## `$crypt_encryption_info`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set crypt_encryption_info = yes
    ```
- **Scope:** Crypto only

If _set_, NeoMutt will include an informative block before an encrypted part, with details about the encryption.

--------------------------------------------------------------------------------

(crypt-opportunistic-encrypt)=
## `$crypt_opportunistic_encrypt`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set crypt_opportunistic_encrypt = no
    ```
- **Scope:** Crypto only

Setting this variable will cause NeoMutt to automatically enable and disable encryption, based on whether all message recipient keys can be located by NeoMutt.

When this option is enabled, NeoMutt will enable/disable encryption each time the TO, CC, and BCC lists are edited.
If $$edit_headers is set, NeoMutt will also do so each time the message is edited.

While this is set, encryption can't be manually enabled/disabled.
The pgp or smime menus provide a selection to temporarily disable this option for the current message.

If $$crypt_auto_encrypt or $$crypt_reply_encrypt enable encryption for a message, this option will be disabled for that message.
It can be manually re-enabled in the pgp or smime menus.

--------------------------------------------------------------------------------

(crypt-opportunistic-encrypt-strong-keys)=
## `$crypt_opportunistic_encrypt_strong_keys`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set crypt_opportunistic_encrypt_strong_keys = no
    ```

When set, this modifies the behavior of $$crypt_opportunistic_encrypt to only search for "strong keys", that is, keys with full validity according to the web-of-trust algorithm.
A key with marginal or no validity will not enable opportunistic encryption.

For S/MIME, the behavior depends on the backend.
Classic S/MIME will filter for certificates with the 't'(trusted) flag in the .index file.
The GPGME backend will use the same filters as with OpenPGP, and depends on GPGME's logic for assigning the GPGME_VALIDITY_FULL and GPGME_VALIDITY_ULTIMATE validity flag.

--------------------------------------------------------------------------------

(crypt-protected-headers-read)=
## `$crypt_protected_headers_read`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set crypt_protected_headers_read = yes
    ```
- **Scope:** Crypto only

When set, NeoMutt will display protected headers ("Memory Hole") in the pager, When set, NeoMutt will display protected headers in the pager, and will update the index and header cache with revised headers.

Protected headers are stored inside the encrypted or signed part of an email, to prevent disclosure or tampering.
For more information see https://github.com/autocrypt/protected-headers Currently NeoMutt only supports the Subject header.

Encrypted messages using protected headers often substitute the exposed Subject header with a dummy value (see $$crypt_protected_headers_subject).
NeoMutt will update its concept of the correct subject **after** the message is opened, i.e. via the `<display-message>` function.
If you reply to a message before opening it, NeoMutt will end up using the dummy Subject header, so be sure to open such a message first.

--------------------------------------------------------------------------------

(crypt-protected-headers-save)=
## `$crypt_protected_headers_save`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set crypt_protected_headers_save = no
    ```
- **Scope:** Crypto only

When $$crypt_protected_headers_read is set, and a message with a protected Subject is opened, NeoMutt will save the updated Subject into the header cache by default.
This allows searching/limiting based on the protected Subject header if the mailbox is re-opened, without having to re-open the message each time.
However, for mbox/mh mailbox types, or if header caching is not set up, you would need to re-open the message each time the mailbox was reopened before you could see or search/limit on the protected subject again.

When this variable is set, NeoMutt additionally saves the protected Subject back **in the clear-text message headers**.
This provides better usability, but with the tradeoff of reduced security.
The protected Subject header, which may have previously been encrypted, is now stored in clear-text in the message headers.
Copying the message elsewhere, via NeoMutt or external tools, could expose this previously encrypted data.
Please make sure you understand the consequences of this before you enable this variable.

--------------------------------------------------------------------------------

(crypt-protected-headers-subject)=
## `$crypt_protected_headers_subject`

- **Type:** [String](string)
- **Default:**
    ```neomuttrc
    set crypt_protected_headers_subject = "..."
    ```
- **Scope:** Crypto only

When $$crypt_protected_headers_write is set, and the message is marked for encryption, this will be substituted into the Subject field in the message headers.

To prevent a subject from being substituted, unset this variable, or set it to the empty string.

--------------------------------------------------------------------------------

(crypt-protected-headers-weed)=
## `$crypt_protected_headers_weed`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set crypt_protected_headers_weed = no
    ```
- **Scope:** Crypto only

Controls whether NeoMutt will weed protected header fields.

--------------------------------------------------------------------------------

(crypt-protected-headers-write)=
## `$crypt_protected_headers_write`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set crypt_protected_headers_write = yes
    ```
- **Scope:** Crypto only

When set, NeoMutt will generate protected headers for signed and encrypted emails.

Protected headers are stored inside the encrypted or signed part of an email, to prevent disclosure or tampering.
For more information see https://github.com/autocrypt/protected-headers 

Currently NeoMutt only supports the Subject header.

--------------------------------------------------------------------------------

(crypt-timestamp)=
## `$crypt_timestamp`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set crypt_timestamp = yes
    ```
- **Scope:** Crypto only

If _set_, NeoMutt will include a time stamp in the lines surrounding PGP or S/MIME output, so spoofing such lines is more difficult.
If you are using colors to mark these lines, and rely on these, you may _unset_ this setting.

--------------------------------------------------------------------------------

(crypt-use-gpgme)=
## `$crypt_use_gpgme`

- **Type:** [Boolean](bool)
- **Notes:** {ref}`On Startup <general>`
- **Default:**
    ```neomuttrc
    set crypt_use_gpgme = yes
    ```

This variable controls the use of the GPGME-enabled crypto backends.
If it is _set_ and NeoMutt was built with GPGME support, the gpgme code for S/MIME and PGP will be used instead of the classic code.
Note that you need to set this option in .neomuttrc; it won't have any effect when used interactively.

Note that the GPGME backend does not support creating old-style inline (traditional) PGP encrypted or signed messages (see $$pgp_auto_inline).

--------------------------------------------------------------------------------

(crypt-use-pka)=
## `$crypt_use_pka`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set crypt_use_pka = no
    ```

Controls whether NeoMutt uses PKA during signature verification (only supported by the GPGME backend).
See: http://www.g10code.de/docs/pka-intro.de.pdf 

--------------------------------------------------------------------------------

(crypt-verify-sig)=
## `$crypt_verify_sig`

- **Type:** [Quad-Option](quad)
- **Default:**
    ```neomuttrc
    set crypt_verify_sig = yes
    ```
- **Scope:** Crypto only

If _"yes"_, always attempt to verify PGP or S/MIME signatures.
If _"ask-*"_, ask whether or not to verify the signature.
If _"no"_, never attempt to verify cryptographic signatures.

--------------------------------------------------------------------------------

(envelope-from-address)=
## `$envelope_from_address`

- **Type:** {ref}`Address <address>`
- **Default:** (empty)
    ```
    set envelope_from_address = ""
    ```

Manually sets the _envelope_ sender for outgoing messages.
This value is ignored if $$use_envelope_from is _unset_.

--------------------------------------------------------------------------------

(pgp-auto-decode)=
## `$pgp_auto_decode`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pgp_auto_decode = no
    ```

If _set_, NeoMutt will automatically attempt to decrypt traditional PGP messages whenever the user performs an operation which ordinarily would result in the contents of the message being operated on.
For example, if the user displays a pgp-traditional message which has not been manually checked with the `$<check-traditional-pgp>` function, NeoMutt will automatically check the message for traditional pgp.

--------------------------------------------------------------------------------

(pgp-auto-inline)=
## `$pgp_auto_inline`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pgp_auto_inline = no
    ```
- **Scope:** PGP only

This option controls whether NeoMutt generates old-style inline (traditional) PGP encrypted or signed messages under certain circumstances.
This can be overridden by use of the pgp menu, when inline is not required.
The GPGME backend does not support this option.

Note that NeoMutt might automatically use PGP/MIME for messages which consist of more than a single MIME part.
NeoMutt can be configured to ask before sending PGP/MIME messages when inline (traditional) would not work.

Also see the $$pgp_mime_auto variable.

Also note that using the old-style PGP message format is **strongly** **deprecated**.

--------------------------------------------------------------------------------

(pgp-check-exit)=
## `$pgp_check_exit`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pgp_check_exit = yes
    ```
- **Scope:** PGP only

If _set_, NeoMutt will check the exit code of the PGP subprocess when signing or encrypting.
A non-zero exit code means that the subprocess failed.

--------------------------------------------------------------------------------

(pgp-check-gpg-decrypt-status-fd)=
## `$pgp_check_gpg_decrypt_status_fd`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pgp_check_gpg_decrypt_status_fd = yes
    ```
- **Scope:** PGP only

If _set_, NeoMutt will check the status file descriptor output of $$pgp_decrypt_command and $$pgp_decode_command for GnuPG status codes indicating successful decryption.
This will check for the presence of DECRYPTION_OKAY, absence of DECRYPTION_FAILED, and that all PLAINTEXT occurs between the BEGIN_DECRYPTION and END_DECRYPTION status codes.

If _unset_, NeoMutt will instead match the status fd output against $$pgp_decryption_okay.

--------------------------------------------------------------------------------

(pgp-clear-sign-command)=
## `$pgp_clear_sign_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_clear_sign_command = ""
    ```
- **Scope:** PGP only

This format is used to create an old-style "clearsigned" PGP message.
Note that the use of this format is **strongly** **deprecated**.

This is a format string, see the $$pgp_decode_command command for possible `printf(3)`-like sequences.
Note that in this case, %r expands to the search string, which is a list of one or more quoted values such as email address, name, or keyid.

--------------------------------------------------------------------------------

(pgp-decode-command)=
## `$pgp_decode_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_decode_command = ""
    ```
- **Scope:** PGP only

This format strings specifies a command which is used to decode application/pgp attachments.

The PGP command formats have their own set of `printf(3)`-like sequences:

| Short | Long Name           | Description                                                                                               |
|-------|---------------------|-----------------------------------------------------------------------------------------------------------|
| `%a`  | `%{sign-as}`        | Value of [$pgp_sign_as](#pgp-sign-as) if set, otherwise the value of [$pgp_default_key](#pgp-default-key) |
| `%f`  | `%{file-message}`   | Expands to the name of a file containing a message                                                        |
| `%p`  | `%{need-pass}`      | Expands to `PGPPASSFD=0` when a pass phrase is needed, to an empty string otherwise.                      |
|       |                     | Note: This may be used with a `%<...>` construct.                                                         |
| `%r`  | `%{key-ids}`        | One or more key IDs (or fingerprints if available)                                                        |
| `%s`  | `%{file-signature}` | Expands to the name of a file containing the signature part                                               |
|       |                     | of a `multipart/signed` attachment when verifying it                                                      |

--------------------------------------------------------------------------------

(pgp-decryption-okay)=
## `$pgp_decryption_okay`

- **Type:** [Regular Expression](regex)
- **Default:** (empty)
    ```
    set pgp_decryption_okay = ""
    ```
- **Scope:** PGP only

If you assign text to this variable, then an encrypted PGP message is only considered successfully decrypted if the output from $$pgp_decrypt_command contains the text.
This is used to protect against a spoofed encrypted message, with multipart/encrypted headers but containing a block that is not actually encrypted.
(e.g. simply signed and ascii armored text).

Note that if $$pgp_check_gpg_decrypt_status_fd is set, this variable is ignored.

--------------------------------------------------------------------------------

(pgp-decrypt-command)=
## `$pgp_decrypt_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_decrypt_command = ""
    ```
- **Scope:** PGP only

This command is used to decrypt a PGP encrypted message.

This is a format string, see the $$pgp_decode_command command for possible `printf(3)`-like sequences.

Note: When decrypting messages using `gpg`, a pinentry program needs to be invoked unless the password is cached within `gpg-agent`.
Currently, the `pinentry-tty` program (usually distributed with `gpg`) isn't suitable for being invoked by NeoMutt.
You are encouraged to use a different pinentry-program when running NeoMutt in order to avoid problems.

See also: https://github.com/neomutt/neomutt/issues/1014 

--------------------------------------------------------------------------------

(pgp-default-key)=
## `$pgp_default_key`

- **Type:** [String](string)
- **Default:** (empty)
    ```
    set pgp_default_key = ""
    ```
- **Scope:** PGP only

This is the default key-pair to use for PGP operations.
It will be used for encryption (see $$postpone_encrypt and $$pgp_self_encrypt).

It will also be used for signing unless $$pgp_sign_as is set.

--------------------------------------------------------------------------------

(pgp-encrypt-only-command)=
## `$pgp_encrypt_only_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_encrypt_only_command = ""
    ```
- **Scope:** PGP only

This command is used to encrypt a body part without signing it.

This is a format string, see the $$pgp_decode_command command for possible `printf(3)`-like sequences.
Note that in this case, %r expands to the search string, which is a list of one or more quoted values such as email address, name, or keyid.

--------------------------------------------------------------------------------

(pgp-encrypt-sign-command)=
## `$pgp_encrypt_sign_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_encrypt_sign_command = ""
    ```
- **Scope:** PGP only

This command is used to both sign and encrypt a body part.

This is a format string, see the $$pgp_decode_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(pgp-entry-format)=
## `$pgp_entry_format`

- **Type:** [Expando](expando)
- **Notes:** {ref}`Not Empty <general>`
- **Default:**
    ```neomuttrc
    set pgp_entry_format = "%4n %t%f %4l/0x%k %-4a %2c %u"
    ```
- **Scope:** Crypto only or PGP only when GPGME disabled

This variable allows you to customize the PGP key selection menu to your personal taste.
If $$crypt_use_gpgme is _set_, then it applies to S/MIME key selection menu also.
This string is similar to $$index_format, but has its own set of `printf(3)`-like sequences:

| Short    | Long Name              | Description                                                     |
|----------|------------------------|-----------------------------------------------------------------|
| `%a`     | `%{key-algorithm}`     | Algorithm                                                       |
| `%c`     | `%{key-capabilities}`  | Capabilities                                                    |
| `%f`     | `%{key-flags}`         | Flags                                                           |
| `%i`     | `%{key-fingerprint}`   | Key fingerprint (or long key id if non-existent)                |
| `%k`     | `%{key-id}`            | Key id                                                          |
| `%l`     | `%{key-length}`        | Key length                                                      |
| `%n`     | `%{number}`            | Number                                                          |
| `%p`     | `%{protocol}`          | Protocol                                                        |
| `%t`     | `%{trust}`             | Trust/validity of the key-uid association                       |
| `%u`     | `%{user-id}`           | User id                                                         |
| `%A`     | `%{pkey-algorithm}`    | Primary Key Algorithm                                           |
| `%C`     | `%{pkey-capabilities}` | Primary Key Capabilities                                        |
| `%F`     | `%{pkey-flags}`        | Primary Key Flags                                               |
| `%I`     | `%{pkey-fingerprint}`  | Primary Key fingerprint (or long key id if non-existent)        |
| `%K`     | `%{pkey-id}`           | Primary Key id                                                  |
| `%L`     | `%{pkey-length}`       | Primary Key length                                              |
| `%[<s>]` | `%{date}`              | Date of the key where `<s>` is an `strftime(3)` expression      |
| `%*X`    | `%{padding-soft:X}`    | Soft-fill with character `X` as pad                             |
| `%>X`    | `%{padding-hard:X}`    | Right justify the rest of the string and pad with character `X` |
| `%\|X`   | `%{padding-eol:X}`     | Pad to the end of the line with character `X`                   |

See the section "Sending Cryptographically Signed/Encrypted Messages" of the user manual for the meaning of the letters some of these sequences expand to.

--------------------------------------------------------------------------------

(pgp-export-command)=
## `$pgp_export_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_export_command = ""
    ```
- **Scope:** PGP only

This command is used to export a public key from the user's key ring.

This is a format string, see the $$pgp_decode_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(pgp-get-keys-command)=
## `$pgp_get_keys_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_get_keys_command = ""
    ```
- **Scope:** PGP only

This command is invoked whenever NeoMutt needs to fetch the public key associated with an email address.
Of the sequences supported by $$pgp_decode_command, %r is the only `printf(3)`-like sequence used with this format.
Note that in this case, %r expands to the email address, not the public key ID (the key ID is unknown, which is why NeoMutt is invoking this command).

--------------------------------------------------------------------------------

(pgp-good-sign)=
## `$pgp_good_sign`

- **Type:** [Regular Expression](regex)
- **Default:** (empty)
    ```
    set pgp_good_sign = ""
    ```
- **Scope:** PGP only

If you assign a text to this variable, then a PGP signature is only considered verified if the output from $$pgp_verify_command contains the text.
Use this variable if the exit code from the command is 0 even for bad signatures.

--------------------------------------------------------------------------------

(pgp-ignore-subkeys)=
## `$pgp_ignore_subkeys`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pgp_ignore_subkeys = yes
    ```
- **Scope:** PGP only

Setting this variable will cause NeoMutt to ignore OpenPGP subkeys.
Instead, the principal key will inherit the subkeys' capabilities.
_Unset_ this if you want to play interesting key selection games.

--------------------------------------------------------------------------------

(pgp-import-command)=
## `$pgp_import_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_import_command = ""
    ```
- **Scope:** PGP only

This command is used to import a key from a message into the user's public key ring.

This is a format string, see the $$pgp_decode_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(pgp-key-sort)=
## `$pgp_key_sort`

- **Type:** [Sort Order](sort)
- **Notes:** [Reverse](sort)
- **Default:**
    ```neomuttrc
    set pgp_key_sort = "address"
    ```
- **Scope:** PGP only

Specifies how the entries in the pgp menu are sorted.

| Value     | Sort by     |
|-----------|-------------|
| `address` | Address     |
| `date`    | Date        |
| `keyid`   | Key id      |
| `trust`   | Trust level |

--------------------------------------------------------------------------------

(pgp-list-pubring-command)=
## `$pgp_list_pubring_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_list_pubring_command = ""
    ```
- **Scope:** PGP only

This command is used to list the public key ring's contents.
The output format must be analogous to the one used by:

```sh
gpg --list-keys --with-colons --with-fingerprint 
```

Note: gpg's `fixed-list-mode` option should not be used.
It produces a different date format which may result in NeoMutt showing incorrect key generation dates.

This is a format string, see the $$pgp_decode_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(pgp-list-secring-command)=
## `$pgp_list_secring_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_list_secring_command = ""
    ```
- **Scope:** PGP only

This command is used to list the secret key ring's contents.
The output format must be analogous to the one used by:

```sh
gpg --list-keys --with-colons --with-fingerprint 
```

Note: gpg's `fixed-list-mode` option should not be used.
It produces a different date format which may result in NeoMutt showing incorrect key generation dates.

This is a format string, see the $$pgp_decode_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(pgp-long-ids)=
## `$pgp_long_ids`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pgp_long_ids = yes
    ```
- **Scope:** PGP only

If _set_, use 64-bit PGP key IDs, if _unset_ use the normal 32-bit key IDs.
NOTE: Internally, NeoMutt has transitioned to using fingerprints (or long key IDs as a fallback).
This option now only controls the display of key IDs in the key selection menu and a few other places.

--------------------------------------------------------------------------------

(pgp-mime-auto)=
## `$pgp_mime_auto`

- **Type:** [Quad-Option](quad)
- **Default:**
    ```neomuttrc
    set pgp_mime_auto = ask-yes
    ```
- **Scope:** PGP only

This option controls whether NeoMutt will prompt you for automatically sending a (signed/encrypted) message using PGP/MIME when inline (traditional) fails (for any reason).

Also note that using the old-style PGP message format is **strongly** **deprecated**.

--------------------------------------------------------------------------------

(pgp-retainable-sigs)=
## `$pgp_retainable_sigs`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pgp_retainable_sigs = no
    ```
- **Scope:** PGP only

If _set_, signed and encrypted messages will consist of nested `multipart/signed` and `multipart/encrypted` body parts.

This is useful for applications like encrypted and signed mailing lists, where the outer layer (`multipart/encrypted`) can be easily removed, while the inner `multipart/signed` part is retained.

--------------------------------------------------------------------------------

(pgp-self-encrypt)=
## `$pgp_self_encrypt`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pgp_self_encrypt = yes
    ```
- **Scope:** PGP only

When _set_, PGP encrypted messages will also be encrypted using the key in $$pgp_default_key.

--------------------------------------------------------------------------------

(pgp-show-unusable)=
## `$pgp_show_unusable`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pgp_show_unusable = yes
    ```
- **Scope:** PGP only

If _set_, NeoMutt will display non-usable keys on the PGP key selection menu.
This includes keys which have been revoked, have expired, or have been marked as "disabled" by the user.

--------------------------------------------------------------------------------

(pgp-sign-as)=
## `$pgp_sign_as`

- **Type:** [String](string)
- **Default:** (empty)
    ```
    set pgp_sign_as = ""
    ```
- **Scope:** PGP only

If you have a different key pair to use for signing, you should set this to the signing key.
Most people will only need to set $$pgp_default_key.
It is recommended that you use the keyid form to specify your key (e.g.
`0x00112233`).

--------------------------------------------------------------------------------

(pgp-sign-command)=
## `$pgp_sign_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_sign_command = ""
    ```
- **Scope:** PGP only

This command is used to create the detached PGP signature for a `multipart/signed` PGP/MIME body part.

This is a format string, see the $$pgp_decode_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(pgp-strict-enc)=
## `$pgp_strict_enc`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pgp_strict_enc = yes
    ```
- **Scope:** PGP only

If _set_, NeoMutt will automatically encode PGP/MIME signed messages as quoted-printable.
Please note that unsetting this variable may lead to problems with non-verifyable PGP signatures, so only change this if you know what you are doing.

--------------------------------------------------------------------------------

(pgp-timeout)=
## `$pgp_timeout`

- **Type:** [Number (Long)](long)
- **Notes:** {ref}`Not Negative <general>`
- **Default:**
    ```neomuttrc
    set pgp_timeout = 300
    ```
- **Scope:** PGP only

The number of seconds after which a cached passphrase will expire if not used.

--------------------------------------------------------------------------------

(pgp-use-gpg-agent)=
## `$pgp_use_gpg_agent`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pgp_use_gpg_agent = yes
    ```
- **Scope:** PGP only

If _set_, NeoMutt expects a `gpg-agent(1)` process will handle private key passphrase prompts.
If _unset_, NeoMutt will prompt for the passphrase and pass it via stdin to the pgp command.

Note that as of version 2.1, GnuPG automatically spawns an agent and requires the agent be used for passphrase management.
Since that version is increasingly prevalent, this variable now defaults _set_.

NeoMutt works with a GUI or curses pinentry program.
A TTY pinentry should not be used.

If you are using an older version of GnuPG without an agent running, or another encryption program without an agent, you will need to _unset_ this variable.

--------------------------------------------------------------------------------

(pgp-verify-command)=
## `$pgp_verify_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_verify_command = ""
    ```
- **Scope:** PGP only

This command is used to verify PGP signatures.

This is a format string, see the $$pgp_decode_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(pgp-verify-key-command)=
## `$pgp_verify_key_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set pgp_verify_key_command = ""
    ```
- **Scope:** PGP only

This command is used to verify key information from the key selection menu.

This is a format string, see the $$pgp_decode_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(smime-ask-cert-label)=
## `$smime_ask_cert_label`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set smime_ask_cert_label = yes
    ```
- **Scope:** S/MIME only

This flag controls whether you want to be asked to enter a label for a certificate about to be added to the database or not.
It is _set_ by default.

--------------------------------------------------------------------------------

(smime-ca-location)=
## `$smime_ca_location`

- **Type:** [Path (String)](path)
- **Notes:** [File only](path)
- **Default:** (empty)
    ```
    set smime_ca_location = ""
    ```
- **Scope:** S/MIME only

This variable contains the name of either a directory, or a file which contains trusted certificates for use with OpenSSL.

--------------------------------------------------------------------------------

(smime-certificates)=
## `$smime_certificates`

- **Type:** [Path (String)](path)
- **Notes:** [Directory only](path)
- **Default:** (empty)
    ```
    set smime_certificates = ""
    ```
- **Scope:** S/MIME only

Since for S/MIME there is no pubring/secring as with PGP, NeoMutt has to handle storage and retrieval of keys by itself.
This is very basic right now, and keys and certificates are stored in two different directories, both named as the hash-value retrieved from OpenSSL.
There is an index file which contains mailbox-address keyid pairs, and which can be manually edited.
This option points to the location of the certificates.

--------------------------------------------------------------------------------

(smime-decrypt-command)=
## `$smime_decrypt_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set smime_decrypt_command = ""
    ```
- **Scope:** S/MIME only

This format string specifies a command which is used to decrypt `application/pkcs7-mime` attachments.

The OpenSSL command formats have their own set of `printf(3)`-like sequences similar to PGP's:

| Short | Long Name             | Description                                                                                                              |
|-------|-----------------------|--------------------------------------------------------------------------------------------------------------------------|
| `%a`  | `%{algorithm}`        | Algorithm used for encryption                                                                                            |
| `%C`  | `%{certificate-path}` | CA location:  Depending on whether [$smime_ca_location](#smime-ca-location) points to a directory or file,               |
|       |                       | this expands to "-CApath [$smime_ca_location](#smime-ca-location)" or "-CAfile [$smime_ca_location](#smime-ca-location)" |
| `%c`  | `%{certificate-ids}`  | One or more certificate IDs                                                                                              |
| `%d`  | `%{digest-algorithm}` | Message digest algorithm specified with [$smime_sign_digest_alg](#smime-sign-digest-alg)                                 |
| `%f`  | `%{message-file}`     | Expands to the name of a file containing a message                                                                       |
| `%i`  | `%{intermediate-ids}` | Intermediate certificates                                                                                                |
| `%k`  | `%{key}`              | Key-pair specified with [$smime_default_key](#smime-default-key)                                                         |
| `%s`  | `%{signature-file}`   | Expands to the name of a file containing the signature part                                                              |
|       |                       | of a `multipart/signed` attachment when verifying it                                                                     |

For examples on how to configure these formats, see the `smime.rc` in the `samples/` subdirectory which has been installed on your system alongside the documentation.

--------------------------------------------------------------------------------

(smime-decrypt-use-default-key)=
## `$smime_decrypt_use_default_key`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set smime_decrypt_use_default_key = yes
    ```
- **Scope:** S/MIME only

If _set_ (default) this tells NeoMutt to use the default key for decryption.
Otherwise, if managing multiple certificate-key-pairs, NeoMutt will try to use the mailbox-address to determine the key to use.
It will ask you to supply a key, if it can't find one.

--------------------------------------------------------------------------------

(smime-default-key)=
## `$smime_default_key`

- **Type:** [String](string)
- **Default:** (empty)
    ```
    set smime_default_key = ""
    ```
- **Scope:** S/MIME only

This is the default key-pair to use for S/MIME operations, and must be set to the keyid (the hash-value that OpenSSL generates) to work properly.

It will be used for encryption (see $$postpone_encrypt and $$smime_self_encrypt).
If GPGME is enabled, this is the key id displayed by gpgsm.

It will be used for decryption unless $$smime_decrypt_use_default_key is _unset_.

It will also be used for signing unless $$smime_sign_as is set.

--------------------------------------------------------------------------------

(smime-encrypt-command)=
## `$smime_encrypt_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set smime_encrypt_command = ""
    ```
- **Scope:** S/MIME only

This command is used to create encrypted S/MIME messages.

This is a format string, see the $$smime_decrypt_command command for possible `printf(3)`-like sequences.

Encrypt the message to $$smime_default_key too.

--------------------------------------------------------------------------------

(smime-encrypt-with)=
## `$smime_encrypt_with`

- **Type:** [String](string)
- **Default:**
    ```neomuttrc
    set smime_encrypt_with = "aes256"
    ```
- **Scope:** S/MIME only

This sets the algorithm that should be used for encryption.
Valid choices are "aes128", "aes192", "aes256", "des", "des3", "rc2-40", "rc2-64", "rc2-128".

--------------------------------------------------------------------------------

(smime-get-cert-command)=
## `$smime_get_cert_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set smime_get_cert_command = ""
    ```
- **Scope:** S/MIME only

This command is used to extract X509 certificates from a PKCS7 structure.

This is a format string, see the $$smime_decrypt_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(smime-get-cert-email-command)=
## `$smime_get_cert_email_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set smime_get_cert_email_command = ""
    ```
- **Scope:** S/MIME only

This command is used to extract the mail address(es) used for storing X509 certificates, and for verification purposes (to check whether the certificate was issued for the sender's mailbox).

This is a format string, see the $$smime_decrypt_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(smime-get-signer-cert-command)=
## `$smime_get_signer_cert_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set smime_get_signer_cert_command = ""
    ```
- **Scope:** S/MIME only

This command is used to extract only the signers X509 certificate from a S/MIME signature, so that the certificate's owner may get compared to the email's "From:" field.

This is a format string, see the $$smime_decrypt_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(smime-import-cert-command)=
## `$smime_import_cert_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set smime_import_cert_command = ""
    ```
- **Scope:** S/MIME only

This command is used to import a certificate via smime_keys.

This is a format string, see the $$smime_decrypt_command command for possible `printf(3)`-like sequences.
NOTE: %c and %k will default to $$smime_sign_as if set, otherwise $$smime_default_key.

--------------------------------------------------------------------------------

(smime-is-default)=
## `$smime_is_default`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set smime_is_default = no
    ```
- **Scope:** S/MIME only

The default behavior of NeoMutt is to use PGP on all auto-sign/encryption operations.
To override and to use OpenSSL instead this must be _set_.
However, this has no effect while replying, since NeoMutt will automatically select the same application that was used to sign/encrypt the original message.
(Note that this variable can be overridden by unsetting $$crypt_auto_smime.)

--------------------------------------------------------------------------------

(smime-keys)=
## `$smime_keys`

- **Type:** [Path (String)](path)
- **Notes:** [Directory only](path)
- **Default:** (empty)
    ```
    set smime_keys = ""
    ```
- **Scope:** S/MIME only

Since for S/MIME there is no pubring/secring as with PGP, NeoMutt has to handle storage and retrieval of keys/certs by itself.
This is very basic right now, and stores keys and certificates in two different directories, both named as the hash-value retrieved from OpenSSL.
There is an index file which contains mailbox-address keyid pair, and which can be manually edited.
This option points to the location of the private keys.

--------------------------------------------------------------------------------

(smime-pk7out-command)=
## `$smime_pk7out_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set smime_pk7out_command = ""
    ```
- **Scope:** S/MIME only

This command is used to extract PKCS7 structures of S/MIME signatures, in order to extract the public X509 certificate(s).

This is a format string, see the $$smime_decrypt_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(smime-self-encrypt)=
## `$smime_self_encrypt`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set smime_self_encrypt = yes
    ```
- **Scope:** S/MIME only

When _set_, S/MIME encrypted messages will also be encrypted using the certificate in $$smime_default_key.

--------------------------------------------------------------------------------

(smime-sign-as)=
## `$smime_sign_as`

- **Type:** [String](string)
- **Default:** (empty)
    ```
    set smime_sign_as = ""
    ```
- **Scope:** S/MIME only

If you have a separate key to use for signing, you should set this to the signing key.
Most people will only need to set $$smime_default_key.

--------------------------------------------------------------------------------

(smime-sign-command)=
## `$smime_sign_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set smime_sign_command = ""
    ```
- **Scope:** S/MIME only

This command is used to created S/MIME signatures of type `multipart/signed`, which can be read by all mail clients.

This is a format string, see the $$smime_decrypt_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(smime-sign-digest-alg)=
## `$smime_sign_digest_alg`

- **Type:** [String](string)
- **Default:**
    ```neomuttrc
    set smime_sign_digest_alg = "sha256"
    ```
- **Scope:** S/MIME only

This sets the algorithm that should be used for the signature message digest.
Valid choices are "md5", "sha1", "sha224", "sha256", "sha384", "sha512".

--------------------------------------------------------------------------------

(smime-timeout)=
## `$smime_timeout`

- **Type:** [Number](number)
- **Notes:** {ref}`Not Negative <general>`
- **Default:**
    ```neomuttrc
    set smime_timeout = 300
    ```
- **Scope:** S/MIME only

The number of seconds after which a cached passphrase will expire if not used.

--------------------------------------------------------------------------------

(smime-verify-command)=
## `$smime_verify_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set smime_verify_command = ""
    ```
- **Scope:** S/MIME only

This command is used to verify S/MIME signatures of type `multipart/signed`.

This is a format string, see the $$smime_decrypt_command command for possible `printf(3)`-like sequences.

--------------------------------------------------------------------------------

(smime-verify-opaque-command)=
## `$smime_verify_opaque_command`

- **Type:** [Expando (Command String)](expando)
- **Default:** (empty)
    ```
    set smime_verify_opaque_command = ""
    ```
- **Scope:** S/MIME only

This command is used to verify S/MIME signatures of type `application/pkcs7-mime`.

This is a format string, see the $$smime_decrypt_command command for possible `printf(3)`-like sequences.

