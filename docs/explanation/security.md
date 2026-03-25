---
title: Understanding Security
description: Security considerations for NeoMutt including passwords, temporary files, and information leaks
keywords: [security, passwords, temporary files, information leaks, mailto, external applications]
diataxis_type: explanation
---

# Understanding Security

First of all, NeoMutt contains no security holes included by intention but may contain unknown security holes.
As a consequence, please run NeoMutt only with as few permissions as possible.
Especially, do not run NeoMutt as the super user.

When configuring NeoMutt, there are some points to note about secure setups so please read this chapter carefully.

## Passwords

Although NeoMutt can be told the various passwords for accounts, please never store passwords in configuration files.
Besides the fact that the system's operator can always read them, you could forget to mask it out when reporting a bug or asking for help via a mailing list.
Even worse, your mail including your password could be archived by internet search engines, mail-to-news gateways etc.
It may already be too late before you notice your mistake.

## Temporary Files

NeoMutt uses many temporary files for viewing messages, verifying digital signatures, etc
As long as being used, these files are visible by other users and maybe even readable in case of misconfiguration.
Also, a different location for these files may be desired which can be changed via the `$tmp_dir` variable.

## Information Leaks

### Message-Id: Headers

Since 2023-02-18 NeoMutt generates random Message-Id: headers, which do not leak any information beyond their randomness.

### `mailto:`-style Links

As NeoMutt can be set up to be the mail client to handle `mailto:` style links in websites, there are security considerations, too.
Arbitrary header fields can be embedded in these links which could override existing header fields or attach arbitrary files using the Attach: pseudoheader.
This may be problematic if the `$edit-headers` variable is *unset*, i.e. the user doesn't want to see header fields while editing the message and doesn't pay enough attention to the compose menu's listing of attachments.

For example, following a link like

```
mailto:joe@host?Attach=~/.gnupg/secring.gpg
```

will send out the user's private gnupg keyring to `joe@host` if the user doesn't follow the information on screen carefully enough.

To prevent these issues, NeoMutt by default only accepts the `Subject`, `Body`, `Cc`, `In-Reply-To`, and `References` headers.
Allowed headers can be adjusted with the `mailto-allow` and `unmailto-allow` commands.

## External Applications

NeoMutt in many places has to rely on external applications or for convenience supports mechanisms involving external applications.

One of these is the `mailcap` mechanism as defined by [RFC1524](https://www.rfc-editor.org/rfc/rfc1524.html).
Details about a secure use of the mailcap mechanisms is given in the mailcap section of the manual.

Besides the mailcap mechanism, NeoMutt uses a number of other external utilities for operation, for example to provide crypto support, in backtick expansion in configuration files or format string filters.
The same security considerations apply for these as for tools involved via mailcap.
