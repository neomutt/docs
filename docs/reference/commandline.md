---
title: Command-Line Options
description: Complete reference of NeoMutt command-line options and usage syntax
keywords: neomutt, command-line, options, arguments, flags
---

# Command-Line Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

Running `neomutt` with no arguments will make NeoMutt attempt to read your spool mailbox. However, it is possible to read other mailboxes and to send messages from the command line as well.

## Detecting Available Features

NeoMutt supports several optional features that can be enabled or disabled at compile-time.
To see which features are compiled into your NeoMutt binary, run:

```
neomutt -v
```

This prints the NeoMutt version, compile-time definitions, and the list of optional
features. Each feature is prefixed with `+` if enabled or `-` if disabled. For example,
if NeoMutt was compiled with GnuTLS instead of OpenSSL:

```
-openssl +gnutls
```

Running `neomutt -vv` shows the full license and copyright information in addition to the
version output.

Common features you may see in `neomutt -v` output include:

| Feature | Description |
|---------|-------------|
| `+gnutls` / `+openssl` | TLS encryption support |
| `+sasl` | SASL authentication |
| `+idn` / `+idn2` | Internationalized domain names |
| `+notmuch` | Notmuch search integration |
| `+sidebar` | Sidebar mailbox list |
| `+gpgme` | GnuPG via GPGME |
| `+lua` | Lua scripting |

### Conditionalizing Config on Features

You can use the `ifdef` and `ifndef` commands in your config file to conditionally apply
settings based on whether a feature is compiled in:

```
ifdef sidebar 'set sidebar_visible = yes'
ifndef notmuch finish
```

The `finish` command stops reading the current config file, making it easy to guard an
entire file behind a feature check. See the [ifdef how-to guide](../howto/ifdef.md) for
full details and examples.

## Options

| Option | Description |
|--------|-------------|
| `--` | Special argument forces NeoMutt to stop option parsing and treat remaining arguments as `address`es even if they start with a dash |
| `-A`, `--alias` *alias* | Print an expanded version of the given `alias` to stdout and exit |
| `-a`, `--attach` *file* | Attach one or more `file`s to a message (must be the last option). Add any addresses after the **`--`** argument |
| `-b`, `--bcc` *address* | Specify a blind carbon copy (Bcc) recipient |
| `-C`, `--crypto` | Enable cryptographic operations in the cases in which they're disabled by default. Those include batch mode, sending a postponed message, and resending a message |
| `-c`, `--cc` *address* | Specify a carbon copy (Cc) recipient |
| `-D`, `--dump-config` | Dump all config options as **name=value** pairs to stdout |
| `-DD`, `--dump-changed-config` | Dump all changed config options as **name=value** pairs to stdout |
| `-D -O`, `--with-docs` | Like **-D**, but show one-liner documentation |
| `-D -S`, `--hide-sensitive` | Like **-D**, but hide the value of sensitive config options |
| `-d`, `--debug-level` *level* | Log debugging output to a file (default is `~/.neomuttdebug0`). The `level` can range from 1–5 and affects verbosity (a value of 2 is recommended) |
| `-E`, `--edit-message` | Edit `draft` (**-H**) or `include` (**-i**) file during message composition |
| `-e`, `--command` *command* | Specify a `command` to be run after reading the config files |
| `-F`, `--config` *config* | Specify an alternative initialization file to read |
| `-f`, `--folder` *mailbox* | Specify a `mailbox` to load |
| `-G`, `--nntp-browser` | Start NeoMutt with a listing of subscribed newsgroups |
| `-g`, `--nntp-server` *server* | Like **-G**, but start at specified news `server` |
| `-H`, `--draft` *draft* | Specify a `draft` file with header and body for message composing |
| `-h`, `--help` | Print this help message and exit |
| `-i`, `--include` *include* | Specify an `include` file to be embedded in the body of a message |
| `-l`, `--debug-file` *file* | Specify a `file` for debugging output (default `~/.neomuttdebug0`). NeoMutt keeps up to five debug logs before overriding the oldest file |
| `-m`, `--mbox-type` *type* | Specify a default mailbox format `type` for newly created folders. The `type` is either MH, MMDF, Maildir or mbox (case-insensitive) |
| `-n`, `--no-system-config` | Do not read the system-wide configuration file |
| `-p`, `--postponed` | Resume a prior postponed message, if any |
| `-Q`, `--query` *variable* | Query a configuration `variable` and print its value to stdout (after the config has been read and any commands executed). Adding `-O` will display one-liner documentation |
| `-R`, `--read-only` | Open mailbox in read-only mode |
| `-s`, `--subject` *subject* | Specify a `subject` (must be enclosed in quotes if it has spaces) |
| `-v`, `--version` | Print the NeoMutt version and compile-time definitions and exit |
| `-vv`, `--license` | Print the NeoMutt license and copyright information and exit |
| `-y`, `--browser` | Start NeoMutt with a listing of all defined mailboxes |
| `-Z`, `--check-new-mail` | Open the first mailbox with new message or exit immediately with exit code 1 if none is found in all defined mailboxes |
| `-z`, `--check-any-mail` | Open the first or specified (**-f**) mailbox if it holds any message or exit immediately with exit code 1 otherwise |

## Command Syntax

To read messages in a mailbox or exit immediately:

```
neomutt [-nz] [-F config] [-m type] [-f mailbox]
```

To compose a new message:

```
neomutt [-Enx] [-F config] [-b address] [-c address] [-H draft] [-i include] [-s subject] [-a file [...] --] {address | mailto_url} [...]
```

NeoMutt also supports a "batch" mode to send prepared messages. Simply redirect input from the file you wish to send. For example:

```
neomutt -s "data set for run #2" professor@bigschool.edu < ~/run2.dat
```

This will send a message to `<professor@bigschool.edu>` with a subject of "data set for run #2". In the body of the message will be the contents of the file "~/run2.dat".

## Include and Draft Files

An include file passed with `-i` will be used as the body of the message. When combined with `-E`, the include file will be directly edited during message composition. The file will be modified regardless of whether the message is sent or aborted.

A draft file passed with `-H` will be used as the initial header and body for the message. Multipart messages can be used as a draft file, and are processed the same in interactive and batch mode; they are not passed through untouched. For example, encrypted draft files will be decrypted. When combined with `-E`, the draft file will be updated to the final state of the message after composition, regardless of whether the message is sent, aborted, or even postponed. Note that if the message is sent encrypted or signed, the draft file will be saved that way too.

## Attachments

All files passed with `-a` *file* will be attached as a MIME part to the message. To attach a single or several files, use `--` to separate files and recipient addresses:

```
neomutt -a image.png -- some@one.org
```

or

```
neomutt -a *.png -- some@one.org
```

:::{note}
The `-a` option must be last in the option list.
:::

## Mailto URLs

In addition to accepting a list of email addresses, NeoMutt also accepts a URL with the `mailto:` schema as specified in [RFC2368](https://www.rfc-editor.org/rfc/rfc2368.html). This is useful when configuring a web browser to launch NeoMutt when clicking on mailto links.

```
neomutt mailto:some@one.org?subject=test&cc=other@one.org
```
