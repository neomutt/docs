---
title: How to Configure TLS/SNI
description: Set up SSL/TLS encryption and TLS-SNI virtual hosting in NeoMutt
keywords: tls, ssl, starttls, sni, encryption, openssl, gnutls, tunnel, ssl_force_tls
---

# How to Configure TLS/SNI

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

## SSL/TLS Support

If NeoMutt is compiled with IMAP, POP3 and/or SMTP support, it can also be compiled with support for SSL or TLS using either OpenSSL or GnuTLS (by running the *configure* script with the *--ssl=...* option for OpenSSL or *--gnutls=...* for GnuTLS). NeoMutt can then attempt to encrypt communication with remote servers if these protocols are suffixed with "s" for "secure communication".

## STARTTLS

When non-secure URL protocols `imap://`, `pop://`, and `smtp://` are used, the initial connection to the server will be unencrypted. `STARTTLS` can be used to negotiate an encrypted connection after the initial unencrypted connection and exchange.

Two configuration variables control NeoMutt's behavior with `STARTTLS`:

- `$ssl_starttls` will initiate `STARTTLS` if the server advertises support for it.
- `$ssl_force_tls` will always try to initiate it, whether the server advertises support or not.

NeoMutt *highly recommends* setting `$ssl_force_tls` unless you need to connect to an unencrypted server. It's possible for an attacker to spoof interactions during the initial connection and hide support for `STARTTLS`. The only way to prevent these attacks is by forcing `STARTTLS` with the `$ssl_force_tls` configuration variable.

```
set ssl_force_tls = yes
```

## Tunnel

When connecting through a `$tunnel` and `$tunnel_is_secure` is set (the default), NeoMutt will assume the connection to the server through the pipe is already secured. NeoMutt will ignore `$ssl_starttls` and `$ssl_force_tls`, behaving as if TLS has already been negotiated.

When `$tunnel_is_secure` is unset, NeoMutt will respect the values of `$ssl_starttls` and `$ssl_force_tls`. It is *highly recommended* to set `$ssl_force_tls` in this case, to force `STARTTLS` negotiation. Note that doing so will prevent connection to an IMAP server configured for preauthentication (`PREAUTH`). If you use this configuration, it is recommended to use a secure tunnel.

## TLS-SNI Feature

**Dependencies:** OpenSSL

The "TLS-SNI" feature adds support for TLS virtual hosting. If your mail server doesn't support this everything will still work normally.

TLS supports sending the expected server hostname during the handshake, via the SNI extension. This can be used to select a server certificate to issue to the client, permitting virtual-hosting without requiring multiple IP addresses.

This has been tested against Exim 4.80, which optionally logs SNI and can perform vhosting.

### Verifying TLS SNI Support

To verify TLS SNI support by a server, you can use:

```
openssl s_client -host <imap server> -port <port> -tls1 -servername <imap server>
```

### Known Bugs

None

### Credits

Jeremy Katz, Phil Pennock, Richard Russon
