---
title: Command-Line Options
description: Complete reference of NeoMutt command-line options and usage syntax
keywords: neomutt, command-line, options, arguments, flags
---

# Command-Line Options

Running `neomutt` with no arguments will make NeoMutt attempt to read your spool mailbox. However, it is possible to read other mailboxes and to send messages from the command line as well.

## Detecting Available Features

NeoMutt supports several optional features that can be enabled or disabled at compile-time.
To see which features are compiled into your NeoMutt binary, run:

```sh
neomutt -v
```

This prints the NeoMutt version, compile-time definitions, and the list of optional
features. Each feature is prefixed with `+` if enabled or `-` if disabled. For example,
if NeoMutt was compiled with GnuTLS instead of OpenSSL:

```diff
-openssl
+gnutls
```

Running `neomutt -vv` shows the full license and copyright information in addition to the
version output.

Common features you may see in `neomutt -v` output include:

| Feature                | Description                    |
|------------------------|--------------------------------|
| `+gnutls` / `+openssl` | TLS encryption support         |
| `+sasl`                | SASL authentication            |
| `+idn` / `+idn2`       | Internationalized domain names |
| `+notmuch`             | Notmuch search integration     |
| `+sidebar`             | Sidebar mailbox list           |
| `+gpgme`               | GnuPG via GPGME                |
| `+lua`                 | Lua scripting                  |

### Conditionalizing Config on Features

You can use the `ifdef` and `ifndef` commands in your config file to conditionally apply
settings based on whether a feature is compiled in:

```neomuttrc
ifdef sidebar 'set sidebar_visible = yes'
ifndef notmuch finish
```

The `finish` command stops reading the current config file, making it easy to guard an
entire file behind a feature check. See the [ifdef how-to guide](../howto/ifdef.md) for
full details and examples.

## Mailto URLs

In addition to accepting a list of email addresses, NeoMutt also accepts a URL with the `mailto:` schema as specified in [RFC2368](https://www.rfc-editor.org/rfc/rfc2368.html). This is useful when configuring a web browser to launch NeoMutt when clicking on mailto links.

```sh
neomutt mailto:some@one.org?subject=test&cc=other@one.org
```
