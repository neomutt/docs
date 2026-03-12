---
title: S/MIME Options
description: S/MIME encryption and signing configuration variables for NeoMutt
keywords: smime_ask_cert_label, smime_ca_location, smime_certificates, smime_decrypt_command, smime_decrypt_use_default_key, smime_default_key, smime_encrypt_command, smime_encrypt_with, smime_get_cert_command, smime_get_cert_email_command, smime_get_signer_cert_command, smime_import_cert_command, smime_is_default, smime_keys, smime_pk7out_command, smime_self_encrypt, smime_sign_as, smime_sign_command, smime_sign_digest_alg, smime_timeout, smime_verify_command, smime_verify_opaque_command
---

# S/MIME Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

(smime-ask-cert-label)=
## `$smime_ask_cert_label`

- **Type:** boolean
- **Default:** yes

This flag controls whether you want to be asked to enter a label
for a certificate about to be added to the database or not. It is
*set* by default.
(S/MIME only)

(smime-ca-location)=
## `$smime_ca_location`

- **Type:** path
- **Default:** (empty)

This variable contains the name of either a directory, or a file which
contains trusted certificates for use with OpenSSL.
(S/MIME only)

(smime-certificates)=
## `$smime_certificates`

- **Type:** path
- **Default:** (empty)

Since for S/MIME there is no pubring/secring as with PGP, NeoMutt has to
handle storage and retrieval of keys by itself. This is very basic right now,
and keys and certificates are stored in two different directories, both named
as the hash-value retrieved from OpenSSL. There is an index file which
contains mailbox-address keyid pairs, and which can be manually edited. This
option points to the location of the certificates. (S/MIME only)

(smime-decrypt-command)=
## `$smime_decrypt_command`

- **Type:** command
- **Default:** (empty)

This format string specifies a command which is used to decrypt
`application/pkcs7-mime` attachments.

The OpenSSL command formats have their own set of `printf(3)`-like
sequences similar to PGP's:

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


For examples on how to configure these formats, see the `smime.rc` in
the `samples/` subdirectory which has been installed on your system
alongside the documentation.
(S/MIME only)

(smime-decrypt-use-default-key)=
## `$smime_decrypt_use_default_key`

- **Type:** boolean
- **Default:** yes

If *set* (default) this tells NeoMutt to use the default key for
decryption. Otherwise, if managing multiple certificate-key-pairs, NeoMutt
will try to use the mailbox-address to determine the key to use. It will ask
you to supply a key, if it can't find one. (S/MIME only)

(smime-default-key)=
## `$smime_default_key`

- **Type:** string
- **Default:** (empty)

This is the default key-pair to use for S/MIME operations, and must be
set to the keyid (the hash-value that OpenSSL generates) to work properly.

It will be used for encryption (see [$postpone_encrypt](#postpone-encrypt) and
[$smime_self_encrypt](#smime-self-encrypt)). If GPGME is enabled, this is the key id displayed
by gpgsm.

It will be used for decryption unless [$smime_decrypt_use_default_key](#smime-decrypt-use-default-key)
is *unset*.

It will also be used for signing unless [$smime_sign_as](#smime-sign-as) is set.

(S/MIME only)

(smime-encrypt-command)=
## `$smime_encrypt_command`

- **Type:** command
- **Default:** (empty)

This command is used to create encrypted S/MIME messages.

This is a format string, see the [$smime_decrypt_command](#smime-decrypt-command) command for
possible `printf(3)`-like sequences.
(S/MIME only)

Encrypt the message to [$smime_default_key](#smime-default-key) too.
(S/MIME only)

(smime-encrypt-with)=
## `$smime_encrypt_with`

- **Type:** string
- **Default:** "`aes256`"

This sets the algorithm that should be used for encryption. Valid choices are
"aes128", "aes192", "aes256", "des", "des3", "rc2-40", "rc2-64", "rc2-128".
(S/MIME only)

(smime-get-cert-command)=
## `$smime_get_cert_command`

- **Type:** command
- **Default:** (empty)

This command is used to extract X509 certificates from a PKCS7 structure.

This is a format string, see the [$smime_decrypt_command](#smime-decrypt-command) command for
possible `printf(3)`-like sequences.
(S/MIME only)

(smime-get-cert-email-command)=
## `$smime_get_cert_email_command`

- **Type:** command
- **Default:** (empty)

This command is used to extract the mail address(es) used for storing
X509 certificates, and for verification purposes (to check whether the
certificate was issued for the sender's mailbox).

This is a format string, see the [$smime_decrypt_command](#smime-decrypt-command) command for
possible `printf(3)`-like sequences.
(S/MIME only)

(smime-get-signer-cert-command)=
## `$smime_get_signer_cert_command`

- **Type:** command
- **Default:** (empty)

This command is used to extract only the signers X509 certificate from a
S/MIME signature, so that the certificate's owner may get compared to the
email's "From:" field.

This is a format string, see the [$smime_decrypt_command](#smime-decrypt-command) command for
possible `printf(3)`-like sequences.
(S/MIME only)

(smime-import-cert-command)=
## `$smime_import_cert_command`

- **Type:** command
- **Default:** (empty)

This command is used to import a certificate via smime_keys.

This is a format string, see the [$smime_decrypt_command](#smime-decrypt-command) command for
possible `printf(3)`-like sequences.  NOTE: %c and %k will default
to [$smime_sign_as](#smime-sign-as) if set, otherwise [$smime_default_key](#smime-default-key).
(S/MIME only)

(smime-is-default)=
## `$smime_is_default`

- **Type:** boolean
- **Default:** no

The default behavior of NeoMutt is to use PGP on all auto-sign/encryption
operations. To override and to use OpenSSL instead this must be *set*.
However, this has no effect while replying, since NeoMutt will automatically
select the same application that was used to sign/encrypt the original
message. (Note that this variable can be overridden by unsetting
[$crypt_auto_smime](#crypt-auto-smime).) (S/MIME only)

(smime-keys)=
## `$smime_keys`

- **Type:** path
- **Default:** (empty)

Since for S/MIME there is no pubring/secring as with PGP, NeoMutt has to
handle storage and retrieval of keys/certs by itself. This is very basic
right now, and stores keys and certificates in two different directories,
both named as the hash-value retrieved from OpenSSL. There is an index file
which contains mailbox-address keyid pair, and which can be manually edited.
This option points to the location of the private keys. (S/MIME only)

(smime-pk7out-command)=
## `$smime_pk7out_command`

- **Type:** command
- **Default:** (empty)

This command is used to extract PKCS7 structures of S/MIME signatures,
in order to extract the public X509 certificate(s).

This is a format string, see the [$smime_decrypt_command](#smime-decrypt-command) command for
possible `printf(3)`-like sequences.
(S/MIME only)

(smime-self-encrypt)=
## `$smime_self_encrypt`

- **Type:** boolean
- **Default:** yes

When *set*, S/MIME encrypted messages will also be encrypted
using the certificate in [$smime_default_key](#smime-default-key).
(S/MIME only)

(smime-sign-as)=
## `$smime_sign_as`

- **Type:** string
- **Default:** (empty)

If you have a separate key to use for signing, you should set this
to the signing key. Most people will only need to set [$smime_default_key](#smime-default-key).
(S/MIME only)

(smime-sign-command)=
## `$smime_sign_command`

- **Type:** command
- **Default:** (empty)

This command is used to created S/MIME signatures of type
`multipart/signed`, which can be read by all mail clients.

This is a format string, see the [$smime_decrypt_command](#smime-decrypt-command) command for
possible `printf(3)`-like sequences.
(S/MIME only)

(smime-sign-digest-alg)=
## `$smime_sign_digest_alg`

- **Type:** string
- **Default:** "`sha256`"

This sets the algorithm that should be used for the signature message digest.
Valid choices are "md5", "sha1", "sha224", "sha256", "sha384", "sha512".
(S/MIME only)

(smime-timeout)=
## `$smime_timeout`

- **Type:** number
- **Default:** 300

The number of seconds after which a cached passphrase will expire if
not used.
(S/MIME only)

(smime-verify-command)=
## `$smime_verify_command`

- **Type:** command
- **Default:** (empty)

This command is used to verify S/MIME signatures of type
`multipart/signed`.

This is a format string, see the [$smime_decrypt_command](#smime-decrypt-command) command for
possible `printf(3)`-like sequences.
(S/MIME only)

(smime-verify-opaque-command)=
## `$smime_verify_opaque_command`

- **Type:** command
- **Default:** (empty)

This command is used to verify S/MIME signatures of type
`application/pkcs7-mime`.

This is a format string, see the [$smime_decrypt_command](#smime-decrypt-command) command for
possible `printf(3)`-like sequences.
(S/MIME only)
