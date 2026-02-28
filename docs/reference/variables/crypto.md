---
title: Crypto Variables
description: General cryptography configuration variables for NeoMutt
keywords: crypt_auto_encrypt, crypt_auto_pgp, crypt_auto_sign, crypt_auto_smime, crypt_chars, crypt_confirm_hook, crypt_encryption_info, crypt_opportunistic_encrypt, crypt_opportunistic_encrypt_strong_keys, crypt_protected_headers_read, crypt_protected_headers_save, crypt_protected_headers_subject, crypt_protected_headers_weed, crypt_protected_headers_write, crypt_reply_encrypt, crypt_reply_sign, crypt_reply_sign_encrypted, crypt_timestamp, crypt_use_gpgme, crypt_use_pka, crypt_verify_sig
---

# Crypto Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

(crypt-auto-encrypt)=
## `$crypt_auto_encrypt`

- **Type:** boolean
- **Default:** no

Setting this variable will cause NeoMutt to always attempt to PGP
encrypt outgoing messages.  This is probably only useful in
connection to the `send-hook` command.  It can be overridden
by use of the pgp menu, when encryption is not required or
signing is requested as well.  If [$smime_is_default](#smime-is-default) is *set*,
then OpenSSL is used instead to create S/MIME messages and
settings can be overridden by use of the smime menu instead.
(Crypto only)

(crypt-auto-pgp)=
## `$crypt_auto_pgp`

- **Type:** boolean
- **Default:** yes

This variable controls whether or not NeoMutt may automatically enable
PGP encryption/signing for messages.  See also [$crypt_auto_encrypt](#crypt-auto-encrypt),
[$crypt_reply_encrypt](#crypt-reply-encrypt),
[$crypt_auto_sign](#crypt-auto-sign), [$crypt_reply_sign](#crypt-reply-sign) and [$smime_is_default](#smime-is-default).

(crypt-auto-sign)=
## `$crypt_auto_sign`

- **Type:** boolean
- **Default:** no

Setting this variable will cause NeoMutt to always attempt to
cryptographically sign outgoing messages.  This can be overridden
by use of the pgp menu, when signing is not required or
encryption is requested as well. If [$smime_is_default](#smime-is-default) is *set*,
then OpenSSL is used instead to create S/MIME messages and settings can
be overridden by use of the smime menu instead of the pgp menu.
(Crypto only)

(crypt-auto-smime)=
## `$crypt_auto_smime`

- **Type:** boolean
- **Default:** yes

This variable controls whether or not NeoMutt may automatically enable
S/MIME encryption/signing for messages. See also [$crypt_auto_encrypt](#crypt-auto-encrypt),
[$crypt_reply_encrypt](#crypt-reply-encrypt),
[$crypt_auto_sign](#crypt-auto-sign), [$crypt_reply_sign](#crypt-reply-sign) and [$smime_is_default](#smime-is-default).

(crypt-chars)=
## `$crypt_chars`

- **Type:** character string
- **Default:** "`SPsK `"

Controls the characters used in cryptography flags.



| **Character** | **Default** | **Description** |
| 1 | S | The mail is signed, and the signature is successfully verified. |
| 2 | P | The mail is PGP encrypted. |
| 3 | s | The mail is signed. |
| 4 | K | The mail contains a PGP public key. |
| 5 | <space> | The mail has no crypto info. |


(crypt-confirm-hook)=
## `$crypt_confirm_hook`

- **Type:** boolean
- **Default:** yes

If set, then you will be prompted for confirmation of keys when using
the *crypt-hook* command.  If unset, no such confirmation prompt will
be presented.  This is generally considered unsafe, especially where
typos are concerned.

(crypt-encryption-info)=
## `$crypt_encryption_info`

- **Type:** boolean
- **Default:** yes

If *set*, NeoMutt will include an informative block
before an encrypted part,
with details about the encryption.
(Crypto only)

(crypt-opportunistic-encrypt)=
## `$crypt_opportunistic_encrypt`

- **Type:** boolean
- **Default:** no

Setting this variable will cause NeoMutt to automatically enable and
disable encryption, based on whether all message recipient keys
can be located by NeoMutt.

When this option is enabled, NeoMutt will enable/disable encryption
each time the TO, CC, and BCC lists are edited.  If
[$edit_headers](#edit-headers) is set, NeoMutt will also do so each time the message
is edited.

While this is set, encryption can't be manually enabled/disabled.
The pgp or smime menus provide a selection to temporarily disable
this option for the current message.

If [$crypt_auto_encrypt](#crypt-auto-encrypt) or [$crypt_reply_encrypt](#crypt-reply-encrypt) enable encryption for
a message, this option will be disabled for that message.  It can
be manually re-enabled in the pgp or smime menus.
(Crypto only)

(crypt-opportunistic-encrypt-strong-keys)=
## `$crypt_opportunistic_encrypt_strong_keys`

- **Type:** boolean
- **Default:** no

When set, this modifies the behavior of [$crypt_opportunistic_encrypt](#crypt-opportunistic-encrypt)
to only search for "strong keys", that is, keys with full validity
according to the web-of-trust algorithm.  A key with marginal or no
validity will not enable opportunistic encryption.

For S/MIME, the behavior depends on the backend.  Classic S/MIME will
filter for certificates with the 't'(trusted) flag in the .index file.
The GPGME backend will use the same filters as with OpenPGP, and depends
on GPGME's logic for assigning the GPGME_VALIDITY_FULL and
GPGME_VALIDITY_ULTIMATE validity flag.

(crypt-protected-headers-read)=
## `$crypt_protected_headers_read`

- **Type:** boolean
- **Default:** yes

When set, NeoMutt will display protected headers ("Memory Hole") in the
pager, When set, NeoMutt will display protected headers in the pager, and
will update the index and header cache with revised headers.

Protected headers are stored inside the encrypted or signed part of an
email, to prevent disclosure or tampering.
For more information see [https://github.com/autocrypt/protected-headers](https://github.com/autocrypt/protected-headers)
Currently NeoMutt only supports the Subject header.

Encrypted messages using protected headers often substitute the exposed
Subject header with a dummy value (see [$crypt_protected_headers_subject](#crypt-protected-headers-subject)).
NeoMutt will update its concept of the correct subject **after** the
message is opened, i.e. via the `<display-message>` function.
If you reply to a message before opening it, NeoMutt will end up using
the dummy Subject header, so be sure to open such a message first.
(Crypto only)

(crypt-protected-headers-save)=
## `$crypt_protected_headers_save`

- **Type:** boolean
- **Default:** no

When [$crypt_protected_headers_read](#crypt-protected-headers-read) is set, and a message with a
protected Subject is opened, NeoMutt will save the updated Subject
into the header cache by default.  This allows searching/limiting
based on the protected Subject header if the mailbox is
re-opened, without having to re-open the message each time.
However, for mbox/mh mailbox types, or if header caching is not
set up, you would need to re-open the message each time the
mailbox was reopened before you could see or search/limit on the
protected subject again.

When this variable is set, NeoMutt additionally saves the protected
Subject back **in the clear-text message headers**.  This
provides better usability, but with the tradeoff of reduced
security.  The protected Subject header, which may have
previously been encrypted, is now stored in clear-text in the
message headers.  Copying the message elsewhere, via NeoMutt or
external tools, could expose this previously encrypted data.
Please make sure you understand the consequences of this before
you enable this variable.
(Crypto only)

(crypt-protected-headers-subject)=
## `$crypt_protected_headers_subject`

- **Type:** string
- **Default:** "`...`"

When [$crypt_protected_headers_write](#crypt-protected-headers-write) is set, and the message is marked
for encryption, this will be substituted into the Subject field in the
message headers.

To prevent a subject from being substituted, unset this variable, or set it
to the empty string.
(Crypto only)

(crypt-protected-headers-weed)=
## `$crypt_protected_headers_weed`

- **Type:** boolean
- **Default:** no

Controls whether NeoMutt will weed protected header fields.
(Crypto only)

(crypt-protected-headers-write)=
## `$crypt_protected_headers_write`

- **Type:** boolean
- **Default:** yes

When set, NeoMutt will generate protected headers for signed and encrypted
emails.

Protected headers are stored inside the encrypted or signed part of an
email, to prevent disclosure or tampering.
For more information see [https://github.com/autocrypt/protected-headers](https://github.com/autocrypt/protected-headers)

Currently NeoMutt only supports the Subject header.
(Crypto only)

(crypt-reply-encrypt)=
## `$crypt_reply_encrypt`

- **Type:** boolean
- **Default:** yes

If *set*, automatically PGP or OpenSSL encrypt replies to messages which
are encrypted. (Crypto only)

(crypt-reply-sign)=
## `$crypt_reply_sign`

- **Type:** boolean
- **Default:** no

If *set*, automatically PGP or OpenSSL sign replies to messages which are
signed.

**Note:** this does not work on messages that are encrypted
*and* signed!
(Crypto only)

(crypt-reply-sign-encrypted)=
## `$crypt_reply_sign_encrypted`

- **Type:** boolean
- **Default:** no

If *set*, automatically PGP or OpenSSL sign replies to messages
which are encrypted. This makes sense in combination with
[$crypt_reply_encrypt](#crypt-reply-encrypt), because it allows you to sign all
messages which are automatically encrypted.  This works around
the problem noted in [$crypt_reply_sign](#crypt-reply-sign), that NeoMutt is not able
to find out whether an encrypted message is also signed.
(Crypto only)

(crypt-timestamp)=
## `$crypt_timestamp`

- **Type:** boolean
- **Default:** yes

If *set*, NeoMutt will include a time stamp in the lines surrounding
PGP or S/MIME output, so spoofing such lines is more difficult.
If you are using colors to mark these lines, and rely on these,
you may *unset* this setting.
(Crypto only)

(crypt-use-gpgme)=
## `$crypt_use_gpgme`

- **Type:** boolean
- **Default:** yes

This variable controls the use of the GPGME-enabled crypto backends. If it is
*set* and NeoMutt was built with GPGME support, the gpgme code for S/MIME
and PGP will be used instead of the classic code. Note that you need to set
this option in .neomuttrc; it won't have any effect when used interactively.

Note that the GPGME backend does not support creating old-style inline
(traditional) PGP encrypted or signed messages (see [$pgp_auto_inline](#pgp-auto-inline)).

(crypt-use-pka)=
## `$crypt_use_pka`

- **Type:** boolean
- **Default:** no

Controls whether NeoMutt uses PKA during signature verification
(only supported by the GPGME backend).
See: [http://www.g10code.de/docs/pka-intro.de.pdf](http://www.g10code.de/docs/pka-intro.de.pdf)

(crypt-verify-sig)=
## `$crypt_verify_sig`

- **Type:** quadoption
- **Default:** yes

If *"yes"*, always attempt to verify PGP or S/MIME signatures.
If *"ask-*"*, ask whether or not to verify the signature.
If *"no"*, never attempt to verify cryptographic signatures.
(Crypto only)
