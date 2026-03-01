---
title: "SSL/TLS Variables"
description: "Reference for NeoMutt SSL/TLS configuration variables."
keywords: "ssl, tls, encryption, certificates, variables, neomutt"
---

# SSL/TLS Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

(ssl-ca-certificates-file)=
## `$ssl_ca_certificates_file`

- **Type:** path
- **Default:** (empty)

This variable specifies a file containing trusted CA certificates.
Any server certificate that is signed with one of these CA
certificates is also automatically accepted. (GnuTLS only)

Example:

```neomuttrc
set ssl_ca_certificates_file=/etc/ssl/certs/ca-certificates.crt
```

(ssl-ciphers)=
## `$ssl_ciphers`

- **Type:** string
- **Default:** (empty)

Contains a colon-separated list of ciphers to use when using SSL.
For OpenSSL, see `ciphers(1)` for the syntax of the string.

For GnuTLS, this option will be used in place of "NORMAL" at the
start of the priority string.  See `gnutls_priority_init(3)` for the
syntax and more details. (Note: GnuTLS version 2.1.7 or higher is
required.)

(ssl-client-cert)=
## `$ssl_client_cert`

- **Type:** path
- **Default:** (empty)

The file containing a client certificate and its associated private
key.

(ssl-force-tls)=
## `$ssl_force_tls`

- **Type:** boolean
- **Default:** yes

If this variable is *set*, NeoMutt will require that all connections
to remote servers be encrypted. Furthermore it will attempt to
negotiate TLS even if the server does not advertise the capability,
since it would otherwise have to abort the connection anyway. This
option supersedes [`$ssl_starttls`](#ssl-starttls).

(ssl-min-dh-prime-bits)=
## `$ssl_min_dh_prime_bits`

- **Type:** number
- **Default:** 0

This variable specifies the minimum acceptable prime size (in bits)
for use in any Diffie-Hellman key exchange. A value of 0 will use
the default from the GNUTLS library. (GnuTLS only)

(ssl-starttls)=
## `$ssl_starttls`

- **Type:** quadoption
- **Default:** yes

If *set* (the default), NeoMutt will attempt to use `STARTTLS` on
servers advertising the capability. When *unset*, NeoMutt will not
attempt to use `STARTTLS` regardless of the server's capabilities.

*Note* that `STARTTLS` is subject to many kinds of
attacks, including the ability of a machine-in-the-middle to
suppress the advertising of support.  Setting [`$ssl_force_tls`](#ssl-force-tls) is
recommended if you rely on `STARTTLS`.

(ssl-use-system-certs)=
## `$ssl_use_system_certs`

- **Type:** boolean
- **Default:** yes

If set to *yes*, NeoMutt will use CA certificates in the
system-wide certificate store when checking if a server certificate
is signed by a trusted CA. (OpenSSL only)

(ssl-use-tlsv1-2)=
## `$ssl_use_tlsv1_2`

- **Type:** boolean
- **Default:** yes

If *set* , NeoMutt will use TLSv1.2 when communicating with servers that
request it.

(ssl-use-tlsv1-3)=
## `$ssl_use_tlsv1_3`

- **Type:** boolean
- **Default:** yes

If *set* , NeoMutt will use TLSv1.3 when communicating with servers that
request it.

(ssl-verify-dates)=
## `$ssl_verify_dates`

- **Type:** boolean
- **Default:** yes

If *set* (the default), NeoMutt will not automatically accept a server
certificate that is either not yet valid or already expired. You should
only unset this for particular known hosts, using the
`[`<account-hook>`](#account-hook)` function.

(ssl-verify-host)=
## `$ssl_verify_host`

- **Type:** boolean
- **Default:** yes

If *set* (the default), NeoMutt will not automatically accept a server
certificate whose host name does not match the host used in your folder
URL. You should only unset this for particular known hosts, using
the `[`<account-hook>`](#account-hook)` function.

(ssl-verify-partial-chains)=
## `$ssl_verify_partial_chains`

- **Type:** boolean
- **Default:** no

This option should not be changed from the default unless you understand
what you are doing.

Setting this variable to *yes* will permit verifying partial
certification chains, i. e. a certificate chain where not the root,
but an intermediate certificate CA, or the host certificate, are
marked trusted (in [`$certificate_file`](#certificate-file)), without marking the root
signing CA as trusted.

(OpenSSL 1.0.2b and newer only).
