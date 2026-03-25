---
title: "Conn Options"
description: "Configuration variables for network connections, SSL/TLS certificates, tunnels, and socket settings."
keywords: "connection, network, ssl, tls, starttls, certificate, tunnel, socket_timeout, ssl_force_tls, ssl_starttls, preconnect, ipv6, account_command, encryption"
---

# Conn Options

(account-command)=
## `$account_command`

- **Type:** [Command (String)](string)
- **Default:** (empty)
    ```neomuttrc
    set account_command = ""
    ```

If set, this command is used to retrieve account credentials.
The command is invoked passing a number of _--key value_ arguments with the specifics of the account to lookup.
The command writes to standard output a number of _key: value_ lines.
Currently supported arguments are _--hostname_, _--username_, and _--type_, where type can be any of _imap_, _imaps_, _pop_, _pops_, _smtp_, _smtps_, _nntp_, and _nntps_.
Currently supported output lines are _login_, _username_, and _password_.

--------------------------------------------------------------------------------

(certificate-file)=
## `$certificate_file`

- **Type:** [Path (String)](path)
- **Notes:** [File only](path)
- **Default:**
    ```neomuttrc
    set certificate_file = "~/.mutt_certificates"
    ```
- **Scope:** OpenSSL and GnuTLS only

This variable specifies the file where the certificates you trust are saved.
When an unknown certificate is encountered, you are asked if you accept it or not.
If you accept it, the certificate can also be saved in this file and further connections are automatically accepted.

You can also manually add CA certificates in this file.
Any server certificate that is signed with one of these CA certificates is also automatically accepted.

--------------------------------------------------------------------------------

(entropy-file)=
## `$entropy_file`

- **Type:** [Path (String)](path)
- **Notes:** [File only](path)
- **Default:** (empty)
    ```neomuttrc
    set entropy_file = ""
    ```
- **Scope:** OpenSSL only

The file which includes random data that is used to initialize SSL library functions.

--------------------------------------------------------------------------------

(preconnect)=
## `$preconnect`

- **Type:** [String](string)
- **Default:** (empty)
    ```neomuttrc
    set preconnect = ""
    ```

If _set_, a shell command to be executed if NeoMutt fails to establish a connection to the server.
This is useful for setting up secure connections, e.g. with `ssh(1)`.
If the command returns a  nonzero status, NeoMutt gives up opening the server.

Example:
```neomuttrc
set preconnect = "ssh -f -q -L 1234:mailhost.net:143 mailhost.net \(rs sleep 20 < /dev/null > /dev/null" 
```

Mailbox "foo" on "mailhost.net" can now be reached as "{localhost:1234}foo".

Note: For this example to work, you must be able to log in to the remote machine without having to enter a password.

--------------------------------------------------------------------------------

(socket-timeout)=
## `$socket_timeout`

- **Type:** [Number](number)
- **Default:**
    ```neomuttrc
    set socket_timeout = 30
    ```

Causes NeoMutt to timeout any socket connect/read/write operation (for IMAP, POP or SMTP) after this many seconds.
A negative value causes NeoMutt to wait indefinitely.

--------------------------------------------------------------------------------

(ssl-ca-certificates-file)=
## `$ssl_ca_certificates_file`

- **Type:** [Path (String)](path)
- **Notes:** [File only](path)
- **Default:** (empty)
    ```neomuttrc
    set ssl_ca_certificates_file = ""
    ```
- **Scope:** GnuTLS only

This variable specifies a file containing trusted CA certificates.
Any server certificate that is signed with one of these CA certificates is also automatically accepted.

Example:
```neomuttrc
set ssl_ca_certificates_file = /etc/ssl/certs/ca-certificates.crt 
```

--------------------------------------------------------------------------------

(ssl-ciphers)=
## `$ssl_ciphers`

- **Type:** [String](string)
- **Default:** (empty)
    ```neomuttrc
    set ssl_ciphers = ""
    ```

Contains a colon-separated list of ciphers to use when using SSL.
For OpenSSL, see `ciphers(1)` for the syntax of the string.

For GnuTLS, this option will be used in place of "NORMAL" at the start of the priority string.
See `gnutls_priority_init(3)` for the syntax and more details.
(Note: GnuTLS version 2.1.7 or higher is required.)

--------------------------------------------------------------------------------

(ssl-client-cert)=
## `$ssl_client_cert`

- **Type:** [Path (String)](path)
- **Notes:** [File only](path)
- **Default:** (empty)
    ```neomuttrc
    set ssl_client_cert = ""
    ```

The file containing a client certificate and its associated private key.

--------------------------------------------------------------------------------

(ssl-force-tls)=
## `$ssl_force_tls`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set ssl_force_tls = yes
    ```

If this variable is _set_, NeoMutt will require that all connections to remote servers be encrypted.
Furthermore it will attempt to negotiate TLS even if the server does not advertise the capability, since it would otherwise have to abort the connection anyway.
This option supersedes [$ssl_starttls](ssl-starttls).

--------------------------------------------------------------------------------

(ssl-min-dh-prime-bits)=
## `$ssl_min_dh_prime_bits`

- **Type:** [Number](number)
- **Notes:** {ref}`Not Negative <general>`
- **Default:**
    ```neomuttrc
    set ssl_min_dh_prime_bits = 0
    ```
- **Scope:** GnuTLS only

This variable specifies the minimum acceptable prime size (in bits)
for use in any Diffie-Hellman key exchange.
A value of 0 will use the default from the GNUTLS library.

--------------------------------------------------------------------------------

(ssl-starttls)=
## `$ssl_starttls`

- **Type:** [Quad-Option](quad)
- **Default:**
    ```neomuttrc
    set ssl_starttls = yes
    ```

If _set_ (the default), NeoMutt will attempt to use `STARTTLS` on servers advertising the capability.
When _unset_, NeoMutt will not attempt to use `STARTTLS` regardless of the server's capabilities.

**Note** that `STARTTLS` is subject to many kinds of attacks, including the ability of a machine-in-the-middle to suppress the advertising of support.
Setting [$ssl_force_tls](ssl-force-tls) is recommended if you rely on `STARTTLS`.

--------------------------------------------------------------------------------

(ssl-use-system-certs)=
## `$ssl_use_system_certs`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set ssl_use_system_certs = yes
    ```
- **Scope:** GnuTLS only

If set to _yes_, NeoMutt will use CA certificates in the system-wide certificate store when checking if a server certificate is signed by a trusted CA.

--------------------------------------------------------------------------------

(ssl-use-tlsv1-2)=
## `$ssl_use_tlsv1_2`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set ssl_use_tlsv1_2 = yes
    ```

If _set_ , NeoMutt will use TLSv1.2 when communicating with servers that request it.

--------------------------------------------------------------------------------

(ssl-use-tlsv1-3)=
## `$ssl_use_tlsv1_3`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set ssl_use_tlsv1_3 = yes
    ```

If _set_ , NeoMutt will use TLSv1.3 when communicating with servers that request it.

--------------------------------------------------------------------------------

(ssl-verify-dates)=
## `$ssl_verify_dates`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set ssl_verify_dates = yes
    ```

If _set_ (the default), NeoMutt will not automatically accept a server certificate that is either not yet valid or already expired.
You should only unset this for particular known hosts, using the `$<account-hook>` function.

--------------------------------------------------------------------------------

(ssl-verify-host)=
## `$ssl_verify_host`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set ssl_verify_host = yes
    ```

If _set_ (the default), NeoMutt will not automatically accept a server certificate whose host name does not match the host used in your folder URL.
You should only unset this for particular known hosts, using the `$<account-hook>` function.

--------------------------------------------------------------------------------

(ssl-verify-partial-chains)=
## `$ssl_verify_partial_chains`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set ssl_verify_partial_chains = no
    ```
- **Scope:** OpenSSL 1.0.2b and newer only

This option should not be changed from the default unless you understand what you are doing.

Setting this variable to _yes_ will permit verifying partial certification chains, i.e. 
a certificate chain where not the root, but an intermediate certificate CA, or the host certificate, are marked trusted (in [$certificate_file](certificate-file)), without marking the root signing CA as trusted.

--------------------------------------------------------------------------------

(tunnel)=
## `$tunnel`

- **Type:** [Command (String)](string)
- **Default:** (empty)
    ```neomuttrc
    set tunnel = ""
    ```

Setting this variable will cause NeoMutt to open a pipe to a command instead of a raw socket.
You may be able to use this to set up preauthenticated connections to your IMAP/POP3/SMTP server.

Example:
```neomuttrc
set tunnel = "ssh -q mailhost.net /usr/local/libexec/imapd" 
```

Note: For this example to work you must be able to log in to the remote machine without having to enter a password.

When set, NeoMutt uses the tunnel for all remote connections.
Please see "$account-hook" in the manual for how to use different tunnel commands per connection.

--------------------------------------------------------------------------------

(tunnel-is-secure)=
## `$tunnel_is_secure`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set tunnel_is_secure = yes
    ```

When _set_, NeoMutt will assume the [$tunnel](tunnel) connection does not need STARTTLS to be enabled.
It will also allow IMAP PREAUTH server responses inside a $tunnel to proceed.
This is appropriate if [$tunnel](tunnel) uses ssh or directly invokes the server locally.

When _unset_, NeoMutt will negotiate STARTTLS according to the $ssl_starttls and $ssl_force_tls variables.
If $ssl_force_tls is set, NeoMutt will abort connecting if an IMAP server responds with PREAUTH.
This setting is appropriate if [$tunnel](tunnel) does not provide security and could be tampered with by attackers.

--------------------------------------------------------------------------------

(use-ipv6)=
## `$use_ipv6`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set use_ipv6 = yes
    ```

When _set_, NeoMutt will look for IPv6 addresses of hosts it tries to contact.
If this option is _unset_, NeoMutt will restrict itself to IPv4 addresses.
Normally, the default should work.

