---
title: URL Syntax
description: Reference for URL syntax used in NeoMutt for IMAP, POP3, and SMTP connections including authentication and port options
keywords: neomutt, url, imap, pop3, smtp, protocol, syntax, ssl, tls, authentication, username, password, port, server
---

# URL Syntax

NeoMutt optionally supports the IMAP, POP3 and SMTP protocols which require to access servers using URLs. The canonical syntax for specifying URLs in NeoMutt is (an item enclosed in `[]` means it is optional and may be omitted):

```
proto[s]://[username[:password]@]server[:port][/path]
```

## Protocol

*proto* is the communication protocol: `imap` for IMAP, `pop` for POP3 and `smtp` for SMTP. If `s` for "secure communication" is appended, NeoMutt will attempt to establish an encrypted communication using SSL or TLS.

## Authentication

Since all protocols supported by NeoMutt support/require authentication, login credentials may be specified in the URL. This has the advantage that multiple IMAP, POP3 or SMTP servers may be specified (which isn't possible using, for example, `$imap_user`). The username may contain the `@` symbol being used by many mail systems as part of the login name. The special characters `/` (`%2F`), `:` (`%3A`) and `%` (`%25`) have to be URL-encoded in usernames using the `%`-notation.

A password can be given, too but is not recommended if the URL is specified in a configuration file on disk.

## Port

If no port number is given, NeoMutt will use the system's default for the given protocol (usually consulting `/etc/services`).

## Path

The optional path is only relevant for IMAP and ignored elsewhere.

## Examples

```
pops://host/
imaps://user@host/INBOX/Sent
smtp://user@host:587/
```
