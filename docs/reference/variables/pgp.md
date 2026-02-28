---
title: PGP Variables
description: PGP encryption and signing configuration variables for NeoMutt
keywords: pgp_auto_decode, pgp_auto_inline, pgp_check_exit, pgp_check_gpg_decrypt_status_fd, pgp_clear_sign_command, pgp_decode_command, pgp_decrypt_command, pgp_decryption_okay, pgp_default_key, pgp_encrypt_only_command, pgp_encrypt_sign_command, pgp_entry_format, pgp_export_command, pgp_get_keys_command, pgp_good_sign, pgp_ignore_subkeys, pgp_import_command, pgp_key_sort, pgp_list_pubring_command, pgp_list_secring_command, pgp_long_ids, pgp_mime_auto, pgp_reply_inline, pgp_retainable_sigs, pgp_self_encrypt, pgp_show_unusable, pgp_sign_as, pgp_sign_command, pgp_strict_enc, pgp_timeout, pgp_use_gpg_agent, pgp_verify_command, pgp_verify_key_command
---

# PGP Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

(pgp-auto-decode)=
## `$pgp_auto_decode`

- **Type:** boolean
- **Default:** no

If *set*, NeoMutt will automatically attempt to decrypt traditional PGP
messages whenever the user performs an operation which ordinarily would
result in the contents of the message being operated on. For example, if the
user displays a pgp-traditional message which has not been manually checked
with the `[<check-traditional-pgp>](#check-traditional-pgp)` function, NeoMutt will automatically
check the message for traditional pgp.

(pgp-auto-inline)=
## `$pgp_auto_inline`

- **Type:** boolean
- **Default:** no

This option controls whether NeoMutt generates old-style inline
(traditional) PGP encrypted or signed messages under certain
circumstances.  This can be overridden by use of the pgp menu,
when inline is not required.  The GPGME backend does not support
this option.

Note that NeoMutt might automatically use PGP/MIME for messages
which consist of more than a single MIME part.  NeoMutt can be
configured to ask before sending PGP/MIME messages when inline
(traditional) would not work.

Also see the [$pgp_mime_auto](#pgp-mime-auto) variable.

Also note that using the old-style PGP message format is **strongly**
**deprecated**.
(PGP only)

(pgp-check-exit)=
## `$pgp_check_exit`

- **Type:** boolean
- **Default:** yes

If *set*, NeoMutt will check the exit code of the PGP subprocess when
signing or encrypting.  A non-zero exit code means that the
subprocess failed.
(PGP only)

(pgp-check-gpg-decrypt-status-fd)=
## `$pgp_check_gpg_decrypt_status_fd`

- **Type:** boolean
- **Default:** yes

If *set*, NeoMutt will check the status file descriptor output
of [$pgp_decrypt_command](#pgp-decrypt-command) and [$pgp_decode_command](#pgp-decode-command) for GnuPG status codes
indicating successful decryption.  This will check for the presence of
DECRYPTION_OKAY, absence of DECRYPTION_FAILED, and that all
PLAINTEXT occurs between the BEGIN_DECRYPTION and END_DECRYPTION
status codes.

If *unset*, NeoMutt will instead match the status fd output
against [$pgp_decryption_okay](#pgp-decryption-okay).
(PGP only)

(pgp-clear-sign-command)=
## `$pgp_clear_sign_command`

- **Type:** command
- **Default:** (empty)

This format is used to create an old-style "clearsigned" PGP
message.  Note that the use of this format is **strongly**
**deprecated**.

This is a format string, see the [$pgp_decode_command](#pgp-decode-command) command for
possible `printf(3)`-like sequences.
Note that in this case, %r expands to the search string, which is a list of
one or more quoted values such as email address, name, or keyid.
(PGP only)

(pgp-decode-command)=
## `$pgp_decode_command`

- **Type:** command
- **Default:** (empty)

This format strings specifies a command which is used to decode
application/pgp attachments.

The PGP command formats have their own set of `printf(3)`-like
sequences:



| **Short** | **Long Name** | **Description** |
| `%a` | `%{sign-as}` | Value of [$pgp_sign_as](#pgp-sign-as) if set, otherwise the value of [$pgp_default_key](#pgp-default-key) |
| `%f` | `%{file-message}` | Expands to the name of a file containing a message |
| `%p` | `%{need-pass}` | Expands to `PGPPASSFD=0` when a pass phrase is needed, to an empty string otherwise. |
|  |  | Note: This may be used with a `%<...>` construct. |
| `%r` | `%{key-ids}` | One or more key IDs (or fingerprints if available) |
| `%s` | `%{file-signature}` | Expands to the name of a file containing the signature part |
|  |  | of a `multipart/signed` attachment when verifying it |


(PGP only)

(pgp-decrypt-command)=
## `$pgp_decrypt_command`

- **Type:** command
- **Default:** (empty)

This command is used to decrypt a PGP encrypted message.

This is a format string, see the [$pgp_decode_command](#pgp-decode-command) command for
possible `printf(3)`-like sequences.
(PGP only)

Note: When decrypting messages using `gpg`, a pinentry program needs to
be invoked unless the password is cached within `gpg-agent`.
Currently, the `pinentry-tty` program (usually distributed with
`gpg`) isn't suitable for being invoked by NeoMutt.  You are encouraged
to use a different pinentry-program when running NeoMutt in order to avoid
problems.

See also: [https://github.com/neomutt/neomutt/issues/1014](https://github.com/neomutt/neomutt/issues/1014)

(pgp-decryption-okay)=
## `$pgp_decryption_okay`

- **Type:** regular expression
- **Default:** (empty)

If you assign text to this variable, then an encrypted PGP
message is only considered successfully decrypted if the output
from [$pgp_decrypt_command](#pgp-decrypt-command) contains the text.  This is used to
protect against a spoofed encrypted message, with multipart/encrypted
headers but containing a block that is not actually encrypted.
(e.g. simply signed and ascii armored text).

Note that if [$pgp_check_gpg_decrypt_status_fd](#pgp-check-gpg-decrypt-status-fd) is set, this variable
is ignored.
(PGP only)

(pgp-default-key)=
## `$pgp_default_key`

- **Type:** string
- **Default:** (empty)

This is the default key-pair to use for PGP operations.  It will be
used for encryption (see [$postpone_encrypt](#postpone-encrypt) and [$pgp_self_encrypt](#pgp-self-encrypt)).

It will also be used for signing unless [$pgp_sign_as](#pgp-sign-as) is set.

(PGP only)

(pgp-encrypt-only-command)=
## `$pgp_encrypt_only_command`

- **Type:** command
- **Default:** (empty)

This command is used to encrypt a body part without signing it.

This is a format string, see the [$pgp_decode_command](#pgp-decode-command) command for
possible `printf(3)`-like sequences.
Note that in this case, %r expands to the search string, which is a list of
one or more quoted values such as email address, name, or keyid.
(PGP only)

(pgp-encrypt-sign-command)=
## `$pgp_encrypt_sign_command`

- **Type:** command
- **Default:** (empty)

This command is used to both sign and encrypt a body part.

This is a format string, see the [$pgp_decode_command](#pgp-decode-command) command for
possible `printf(3)`-like sequences.
(PGP only)

(pgp-entry-format)=
## `$pgp_entry_format`

- **Type:** string
- **Default:** "`%4n %t%f %4l/0x%k %-4a %2c %u`"

This variable allows you to customize the PGP key selection menu to
your personal taste. If [$crypt_use_gpgme](#crypt-use-gpgme) is *set*, then it applies
to S/MIME key selection menu also. This string is similar to [$index_format](#index-format),
but has its own set of `printf(3)`-like sequences:



| **Short** | **Long Name** | **Description** |
| `%a` | `%{key-algorithm}` | Algorithm |
| `%c` | `%{key-capabilities}` | Capabilities |
| `%f` | `%{key-flags}` | Flags |
| `%i` | `%{key-fingerprint}` | Key fingerprint (or long key id if non-existent) |
| `%k` | `%{key-id}` | Key id |
| `%l` | `%{key-length}` | Key length |
| `%n` | `%{number}` | Number |
| `%p` | `%{protocol}` | Protocol |
| `%t` | `%{trust}` | Trust/validity of the key-uid association |
| `%u` | `%{user-id}` | User id |
| `%A` | `%{pkey-algorithm}` | Primary Key Algorithm |
| `%C` | `%{pkey-capabilities}` | Primary Key Capabilities |
| `%F` | `%{pkey-flags}` | Primary Key Flags |
| `%I` | `%{pkey-fingerprint}` | Primary Key fingerprint (or long key id if non-existent) |
| `%K` | `%{pkey-id}` | Primary Key id |
| `%L` | `%{pkey-length}` | Primary Key length |
| `%[<s>]` | `%{date}` | Date of the key where `<s>` is an `strftime(3)` expression |
| `%*X` | `%{padding-soft}` | Soft-fill with character `X` as pad |
| `%>X` | `%{padding-hard}` | Right justify the rest of the string and pad with character `X` |
| `%|X` | `%{padding-eol}` | Pad to the end of the line with character `X` |


See the section "Sending Cryptographically Signed/Encrypted Messages" of the
user manual for the meaning of the letters some of these sequences expand
to.

(Crypto only) or (PGP only when GPGME disabled)

(pgp-export-command)=
## `$pgp_export_command`

- **Type:** command
- **Default:** (empty)

This command is used to export a public key from the user's
key ring.

This is a format string, see the [$pgp_decode_command](#pgp-decode-command) command for
possible `printf(3)`-like sequences.
(PGP only)

(pgp-get-keys-command)=
## `$pgp_get_keys_command`

- **Type:** command
- **Default:** (empty)

This command is invoked whenever NeoMutt needs to fetch the public key
associated with an email address. Of the sequences supported by
[$pgp_decode_command](#pgp-decode-command), %r is the only `printf(3)`-like sequence used with
this format. Note that in this case, %r expands to the email address, not the
public key ID (the key ID is unknown, which is why NeoMutt is invoking this
command). (PGP only)

(pgp-good-sign)=
## `$pgp_good_sign`

- **Type:** regular expression
- **Default:** (empty)

If you assign a text to this variable, then a PGP signature is only
considered verified if the output from [$pgp_verify_command](#pgp-verify-command) contains
the text. Use this variable if the exit code from the command is 0
even for bad signatures.
(PGP only)

(pgp-ignore-subkeys)=
## `$pgp_ignore_subkeys`

- **Type:** boolean
- **Default:** yes

Setting this variable will cause NeoMutt to ignore OpenPGP subkeys. Instead,
the principal key will inherit the subkeys' capabilities.  *Unset* this
if you want to play interesting key selection games.
(PGP only)

(pgp-import-command)=
## `$pgp_import_command`

- **Type:** command
- **Default:** (empty)

This command is used to import a key from a message into
the user's public key ring.

This is a format string, see the [$pgp_decode_command](#pgp-decode-command) command for
possible `printf(3)`-like sequences.
(PGP only)

(pgp-key-sort)=
## `$pgp_key_sort`

- **Type:** sort order
- **Default:** address

Specifies how the entries in the pgp menu are sorted.



| **Value** | **Sort by** |
| `address` | Address |
| `date` | Date |
| `keyid` | Key id |
| `trust` | Trust level |


Prefixing the value with `reverse-` sorts the entries in reverse order,
e.g. `set pgp_key_sort = "reverse-date"`

(PGP only)

(pgp-list-pubring-command)=
## `$pgp_list_pubring_command`

- **Type:** command
- **Default:** (empty)

This command is used to list the public key ring's contents.  The
output format must be analogous to the one used by


```
gpg --list-keys --with-colons --with-fingerprint
```


Note: gpg's `fixed-list-mode` option should not be used.  It
produces a different date format which may result in NeoMutt showing
incorrect key generation dates.

This is a format string, see the [$pgp_decode_command](#pgp-decode-command) command for
possible `printf(3)`-like sequences.
(PGP only)

(pgp-list-secring-command)=
## `$pgp_list_secring_command`

- **Type:** command
- **Default:** (empty)

This command is used to list the secret key ring's contents.  The
output format must be analogous to the one used by:


```
gpg --list-keys --with-colons --with-fingerprint
```


Note: gpg's `fixed-list-mode` option should not be used.  It
produces a different date format which may result in NeoMutt showing
incorrect key generation dates.

This is a format string, see the [$pgp_decode_command](#pgp-decode-command) command for
possible `printf(3)`-like sequences.
(PGP only)

(pgp-long-ids)=
## `$pgp_long_ids`

- **Type:** boolean
- **Default:** yes

If *set*, use 64-bit PGP key IDs, if *unset* use the normal 32-bit
key IDs. NOTE: Internally, NeoMutt has transitioned to using fingerprints (or
long key IDs as a fallback). This option now only controls the display of key
IDs in the key selection menu and a few other places. (PGP only)

(pgp-mime-auto)=
## `$pgp_mime_auto`

- **Type:** quadoption
- **Default:** ask-yes

This option controls whether NeoMutt will prompt you for
automatically sending a (signed/encrypted) message using
PGP/MIME when inline (traditional) fails (for any reason).

Also note that using the old-style PGP message format is **strongly**
**deprecated**.
(PGP only)

(pgp-reply-inline)=
## `$pgp_reply_inline`

- **Type:** boolean
- **Default:** no

Setting this variable will cause NeoMutt to always attempt to
create an inline (traditional) message when replying to a
message which is PGP encrypted/signed inline.  This can be
overridden by use of the pgp menu, when inline is not
required.  This option does not automatically detect if the
(replied-to) message is inline; instead it relies on NeoMutt
internals for previously checked/flagged messages.

Note that NeoMutt might automatically use PGP/MIME for messages
which consist of more than a single MIME part.  NeoMutt can be
configured to ask before sending PGP/MIME messages when inline
(traditional) would not work.

Also see the [$pgp_mime_auto](#pgp-mime-auto) variable.

Also note that using the old-style PGP message format is **strongly**
**deprecated**.
(PGP only)

(pgp-retainable-sigs)=
## `$pgp_retainable_sigs`

- **Type:** boolean
- **Default:** no

If *set*, signed and encrypted messages will consist of nested
`multipart/signed` and `multipart/encrypted` body parts.

This is useful for applications like encrypted and signed mailing
lists, where the outer layer (`multipart/encrypted`) can be easily
removed, while the inner `multipart/signed` part is retained.
(PGP only)

(pgp-self-encrypt)=
## `$pgp_self_encrypt`

- **Type:** boolean
- **Default:** yes

When *set*, PGP encrypted messages will also be encrypted
using the key in [$pgp_default_key](#pgp-default-key).
(PGP only)

(pgp-show-unusable)=
## `$pgp_show_unusable`

- **Type:** boolean
- **Default:** yes

If *set*, NeoMutt will display non-usable keys on the PGP key selection
menu.  This includes keys which have been revoked, have expired, or
have been marked as "disabled" by the user.
(PGP only)

(pgp-sign-as)=
## `$pgp_sign_as`

- **Type:** string
- **Default:** (empty)

If you have a different key pair to use for signing, you should
set this to the signing key.  Most people will only need to set
[$pgp_default_key](#pgp-default-key).  It is recommended that you use the keyid form
to specify your key (e.g. `0x00112233`).
(PGP only)

(pgp-sign-command)=
## `$pgp_sign_command`

- **Type:** command
- **Default:** (empty)

This command is used to create the detached PGP signature for a
`multipart/signed` PGP/MIME body part.

This is a format string, see the [$pgp_decode_command](#pgp-decode-command) command for
possible `printf(3)`-like sequences.
(PGP only)

(pgp-strict-enc)=
## `$pgp_strict_enc`

- **Type:** boolean
- **Default:** yes

If *set*, NeoMutt will automatically encode PGP/MIME signed messages as
quoted-printable.  Please note that unsetting this variable may
lead to problems with non-verifyable PGP signatures, so only change
this if you know what you are doing.
(PGP only)

(pgp-timeout)=
## `$pgp_timeout`

- **Type:** number (long)
- **Default:** 300

The number of seconds after which a cached passphrase will expire if
not used.
(PGP only)

(pgp-use-gpg-agent)=
## `$pgp_use_gpg_agent`

- **Type:** boolean
- **Default:** yes

If *set*, NeoMutt expects a `gpg-agent(1)` process will handle
private key passphrase prompts.  If *unset*, NeoMutt will prompt
for the passphrase and pass it via stdin to the pgp command.

Note that as of version 2.1, GnuPG automatically spawns an agent
and requires the agent be used for passphrase management.  Since
that version is increasingly prevalent, this variable now
defaults *set*.

NeoMutt works with a GUI or curses pinentry program.  A TTY pinentry
should not be used.

If you are using an older version of GnuPG without an agent running,
or another encryption program without an agent, you will need to
*unset* this variable.
(PGP only)

(pgp-verify-command)=
## `$pgp_verify_command`

- **Type:** command
- **Default:** (empty)

This command is used to verify PGP signatures.

This is a format string, see the [$pgp_decode_command](#pgp-decode-command) command for
possible `printf(3)`-like sequences.
(PGP only)

(pgp-verify-key-command)=
## `$pgp_verify_key_command`

- **Type:** command
- **Default:** (empty)

This command is used to verify key information from the key selection
menu.

This is a format string, see the [$pgp_decode_command](#pgp-decode-command) command for
possible `printf(3)`-like sequences.
(PGP only)
