---
title: Command-Line Options
description: Complete reference of NeoMutt command-line options and usage syntax
keywords: neomutt, command-line, options, arguments, flags
---

# Command-Line Options

## Overview

NeoMutt has **four modes** of operation:

| Mode   | Purpose                                 | Activated by                       |
|--------|-----------------------------------------|------------------------------------|
| `help` | Display version, license, or usage info | `-h`, `-v`, `-vv`                  |
| `info` | Query config options and aliases        | `-A`, `-D`, `-DD`, `-Q`            |
| `send` | Compose and send an email               | `-s`, `-a`, `-c`, `-b`, `-H`, `-i` |
| `tui`  | Start the Terminal User Interface       | Default (no arguments)             |

The default mode, when no arguments are given, is **tui**.

In addition, there are **shared options** that apply to all modes.  These
control config files, extra commands, mailbox type, and debug logging.

All options have both short (`-X`) and long (`--name`) forms.  The two forms
are interchangeable and may be freely mixed on the same command line.

> **Note:** The `=` syntax is **not** supported.  For example,
> `--config=file` is invalid.  Use `--config file` instead.

---

## Shared Options

Shared options may be combined with any mode.  They control which config
files are loaded, allow extra config commands, and configure debug logging.

| Short | Long                 | Argument    | Description                              |
|-------|----------------------|-------------|------------------------------------------|
| `-n`  | `--no-system-config` |             | Don't read the system config file        |
| `-F`  | `--config`           | `<file>`    | Use this user config file (repeatable)   |
| `-e`  | `--command`          | `<command>` | Run an extra config command (repeatable) |
| `-m`  | `--mbox-type`        | `<type>`    | Set the default mailbox type             |
| `-d`  | `--debug-level`      | `<level>`   | Set logging level                        |
| `-l`  | `--debug-file`       | `<file>`    | Set logging file                         |

### Config Files

By default, NeoMutt loads one system config file (e.g. `/etc/neomuttrc`)
and one user config file (e.g. `~/.neomuttrc`).

- `-n` prevents the system config file from being loaded.
- `-F` replaces the default user config file.  It may be specified multiple
  times; each file is loaded in order.

```sh
# Skip the system config
neomutt --no-system-config

# Use a custom config file
neomutt --config ~/.config/neomutt/work.rc

# Load multiple config files
neomutt --config work.rc --config colours.rc
```

### Extra Commands

The `-e` option runs config commands after all config files have been loaded.
It may be specified multiple times.

```sh
# Override a config option
neomutt --command 'set ask_cc = yes'

# Run multiple commands
neomutt -e 'set sort = threads' -e 'set markers = no'
```

### Mailbox Type

The `-m` option sets the default mailbox type.  Valid values are:
`maildir`, `mbox`, `mh`, `mmdf`.

```sh
neomutt --mbox-type maildir
```

### Debug Logging

The `-d` option sets the logging level: `0` (off), `1` (low) through `5`
(high).  The `-l` option sets the log file; the default is
`~/.neomuttdebug0`.

```sh
# Enable moderate logging
neomutt --debug-level 2

# Maximum logging to a custom file
neomutt --debug-level 5 --debug-file /tmp/neomutt.log
```

---

## Help Mode

Help mode displays usage information, the NeoMutt version, or the license
text.  NeoMutt prints the requested information and exits.

| Short | Long        | Argument | Description                          |
|-------|-------------|----------|--------------------------------------|
| `-h`  | `--help`    |          | Overview of command-line options     |
| `-h`  | `--help`    | `<mode>` | Detailed help for a mode             |
| `-v`  | `--version` |          | NeoMutt version and build parameters |
| `-vv` | `--license` |          | NeoMutt copyright and license        |

### Detailed Help

The `-h` option accepts an optional mode name for more detailed help.
Valid mode names are: `shared`, `help`, `info`, `send`, `tui`, `all`.

```sh
# Show the overview
neomutt --help

# Detailed help for send mode
neomutt --help send

# Show help for all modes
neomutt --help all
```

### Version and License

Using `-v` once prints the version.  Using `-v` twice (i.e. `-vv`) prints
the license.  The long option `--license` is equivalent to `-vv`.

```sh
neomutt --version
neomutt -vv
neomutt --license
```

---

## Info Mode

Info mode queries NeoMutt's configuration and exits.  It is useful for
scripting and debugging config problems.

| Short | Long                    | Argument         | Description                         |
|-------|-------------------------|------------------|-------------------------------------|
| `-A`  | `--alias`               | `<alias> [...]`  | Lookup email aliases                |
| `-D`  | `--dump-config`         |                  | Dump all config options             |
| `-DD` | `--dump-changed-config` |                  | Dump only changed config options    |
| `-Q`  | `--query`               | `<option> [...]` | Query config options                |
| `-O`  | `--with-docs`           |                  | Add one-liner documentation         |
| `-S`  | `--hide-sensitive`      |                  | Hide the value of sensitive options |

### Alias Lookup

The `-A` option looks up one or more email aliases.  Multiple aliases can be
specified as space-separated arguments.  The argument list is terminated by
`--` or another option flag.

```sh
# Lookup a single alias
neomutt --alias flatcap

# Lookup multiple aliases
neomutt --alias flatcap gahr rocco
```

### Dump Config

Using `-D` once dumps all config options.  Using `-D` twice (i.e. `-DD`)
dumps only the options that differ from their defaults.  The long option
`--dump-changed-config` is equivalent to `-DD`.

```sh
# Dump all config
neomutt --dump-config

# Dump only changed options
neomutt -DD
neomutt --dump-changed-config
```

### Query Config

The `-Q` option queries one or more specific config options.  Multiple
option names can be specified as space-separated arguments.  The argument
list is terminated by `--` or another option flag.

```sh
# Query a single option
neomutt --query sort

# Query multiple options
neomutt --query alias_format index_format
```

### Modifiers: `-O` and `-S`

The `-O` and `-S` options modify the output of `-D` and `-Q`.

- `-O` adds a one-liner documentation comment above each option.
- `-S` hides the values of sensitive options (e.g. passwords).

These modifiers may be combined.

```sh
# Dump config with documentation
neomutt --dump-config --with-docs

# Dump changed config, hiding sensitive values
neomutt --dump-changed-config --hide-sensitive

# Query options with docs and hidden secrets
neomutt --with-docs --query alias_format index_format
```

---

## Send Mode

Send mode composes and sends an email from the command line.  If any
required parts are missing (e.g. no recipients or no subject), NeoMutt will
start the TUI to prompt for them.

| Short | Long             | Argument       | Description                               |
|-------|------------------|----------------|-------------------------------------------|
| `-a`  | `--attach`       | `<file> [...]` | Attach files (terminated by `--` or `-X`) |
| `-b`  | `--bcc`          | `<address>`    | Add a Bcc: address                        |
| `-C`  | `--crypto`       |                | Use crypto (signing/encryption)           |
| `-c`  | `--cc`           | `<address>`    | Add a Cc: address                         |
| `-E`  | `--edit-message` |                | Edit message (draft/include)              |
| `-H`  | `--draft`        | `<file>`       | Use a draft email file                    |
| `-i`  | `--include`      | `<file>`       | Include a body file                       |
| `-s`  | `--subject`      | `<subject>`    | Set the Subject: header                   |
|       | `--`             | `<addr> [...]` | Add To: addresses                         |

### Addresses

To: addresses may appear in **two** places on the command line:

1. **Before any options** — leading non-option arguments are treated as
   To: addresses.
2. **After `--`** — trailing arguments after the `--` separator are treated
   as To: addresses.

Aliases defined in the config may be used in place of email addresses.

```sh
# Address before options
neomutt flatcap --subject 'Meeting Notes'

# Address after --
neomutt --subject 'Meeting Notes' -- flatcap@example.com

# Multiple recipients
neomutt --subject 'Team Update' -- alice@example.com bob@example.com
```

### Attachments

The `-a` option accepts multiple space-separated file arguments.  The file
list is terminated by `--` or another option flag.

```sh
# Attach a single file
neomutt --subject 'Report' --attach report.pdf -- boss@example.com

# Attach multiple files
neomutt --subject 'Receipts' --attach receipt1.pdf receipt2.pdf -- rocco

# Attach files, then add addresses after --
neomutt --attach photo1.jpg photo2.jpg -- friends@example.com
```

### Drafts and Includes

A **draft file** (`-H`) is a complete email with headers and body.  An
**include file** (`-i`) provides only the body text.

The `-E` option enables editing of the draft or include file in the
composer before sending.

```sh
# Send from a draft file
neomutt --draft ~/drafts/proposal.eml

# Include a body file and set the subject
neomutt --include meeting-notes.txt --subject 'Notes' -- team@example.com

# Edit the draft before sending
neomutt --edit-message --draft ~/drafts/proposal.eml
```

### Piping Input

Email body text can be piped via stdin:

```sh
echo 'Build succeeded' | neomutt --subject 'CI Report' -- dev@example.com

cat secret.txt | neomutt gahr --subject 'Secret' --crypto
```

### Combined Example

```sh
neomutt jim@example.com \
  --cc bob@example.com \
  --bcc alice@example.com \
  --subject 'Party Planning' \
  --include party-details.txt \
  --attach map.pdf guest-list.csv
```

---

## TUI Mode

TUI mode starts NeoMutt's Terminal User Interface.  This is the default
when no command-line arguments are given.  By default, NeoMutt opens the
Index Dialog with the `$spool_file` mailbox.

| Short | Long               | Argument    | Description                       |
|-------|--------------------|-------------|-----------------------------------|
| `-f`  | `--folder`         | `<mailbox>` | Open this mailbox                 |
| `-G`  | `--nntp-browser`   |             | Open NNTP browser                 |
| `-g`  | `--nntp-server`    | `<server>`  | Use this NNTP server              |
| `-p`  | `--postponed`      |             | Resume postponed email            |
| `-R`  | `--read-only`      |             | Open mailbox read-only            |
| `-y`  | `--browser`        |             | Open mailbox browser              |
| `-Z`  | `--check-new-mail` |             | Check for new mail (exit if none) |
| `-z`  | `--check-any-mail` |             | Check for any mail (exit if none) |

### Opening a Mailbox

```sh
# Open a specific mailbox
neomutt --folder ~/Mail/inbox

# Open read-only
neomutt --folder ~/Mail/archive --read-only
```

### Mail Checks

The `-Z` and `-z` options cause NeoMutt to check a mailbox before starting.
If the condition is not met, NeoMutt exits immediately.

- `-Z` checks for **new** (unread) mail.
- `-z` checks for **any** mail.

```sh
# Only start if there is new mail
neomutt --check-new-mail

# Only start if there is any mail in a specific folder
neomutt --folder ~/Mail/work --check-any-mail
```

### Postponed Messages

The `-p` option resumes editing a previously postponed email.

```sh
neomutt --postponed
```

### Mailbox Browser

The `-y` option opens the mailbox browser instead of going directly to a
mailbox.

```sh
neomutt --browser
```

### NNTP (Usenet)

The `-G` option opens the NNTP newsgroup browser.  The `-g` option
specifies an NNTP server to connect to.

```sh
# Open the NNTP browser
neomutt --nntp-browser

# Connect to a specific news server
neomutt --nntp-server news.example.com
```

---

## Parsing Behavior

This section describes how NeoMutt interprets the command line.

### Option Syntax

NeoMutt uses `getopt_long` for command-line parsing.  All short options have
equivalent long options.

- Short options use a single dash: `-s 'Hello'`
- Long options use a double dash: `--subject 'Hello'`
- **The `=` sign is not supported**.  `--subject='Hello'` is invalid and
  will produce an error.

### Leading Arguments

Any arguments that appear **before** the first option flag are treated as
To: addresses and activate send mode.

```sh
# 'alice@example.com' is a To: address (appears before -s)
neomutt alice@example.com -s 'Hello'
```

### Trailing Arguments

Arguments that appear **after `--`** are treated as To: addresses.

```sh
neomutt --subject 'Hello' -- alice@example.com bob@example.com
```

### Multi-Value Options (Mop Up)

Three options accept multiple space-separated arguments:

| Option | Long       | Collects until    |
|--------|------------|-------------------|
| `-A`   | `--alias`  | `--` or next `-X` |
| `-Q`   | `--query`  | `--` or next `-X` |
| `-a`   | `--attach` | `--` or next `-X` |

The argument list for these options ends when `--` or another option
beginning with `-` is encountered.

```sh
# -A collects both 'flatcap' and 'gahr'
neomutt --alias flatcap gahr

# -a collects both files, then -- separates addresses
neomutt --attach notes.txt slides.pdf -- team@example.com
```

### Double-Flag Options

Two options change meaning when specified twice:

| Once | Twice | Long Equivalent                           | Effect                    |
|------|-------|-------------------------------------------|---------------------------|
| `-v` | `-vv` | `--version` / `--license`                 | Version → License         |
| `-D` | `-DD` | `--dump-config` / `--dump-changed-config` | All config → Changed only |

```sh
# Version
neomutt -v

# License (double -v)
neomutt -vv
```

### Error Handling

If NeoMutt encounters an unknown option or a missing required argument, it
prints an error message and shows the help overview.

```sh
# Unknown option — prints error and help
neomutt --foobar

# Missing argument — prints error and help
neomutt --config
```

---

## Quick Reference

```
neomutt [<address> ...] [options] [-- <address> ...]

Shared:
  -n, --no-system-config            Don't read system config file
  -F, --config <file>               Use this user config file (repeatable)
  -e, --command <command>           Run extra config command (repeatable)
  -m, --mbox-type <type>            Set default mailbox type
  -d, --debug-level <level>         Set logging level (0-5)
  -l, --debug-file <file>           Set logging file

Help:
  -h, --help [<mode>]               Show help (modes: shared, help, info, send, tui, all)
  -v, --version                     Show version
  -vv, --license                    Show license

Info:
  -A, --alias <alias> [...]         Lookup email aliases
  -D, --dump-config                 Dump all config options
  -DD, --dump-changed-config        Dump changed config options
  -Q, --query <option> [...]        Query config options
  -O, --with-docs                   Add one-liner documentation (modifies -D, -Q)
  -S, --hide-sensitive              Hide sensitive values (modifies -D, -Q)

Send:
  -a, --attach <file> [...]         Attach files
  -b, --bcc <address>               Add Bcc: address
  -C, --crypto                      Use crypto (signing/encryption)
  -c, --cc <address>                Add Cc: address
  -E, --edit-message                Edit draft/include before sending
  -H, --draft <file>                Use draft email file
  -i, --include <file>              Include body file
  -s, --subject <subject>           Set Subject: header

TUI:
  -f, --folder <mailbox>            Open this mailbox
  -G, --nntp-browser                Open NNTP browser
  -g, --nntp-server <server>        Use this NNTP server
  -p, --postponed                   Resume postponed email
  -R, --read-only                   Open mailbox read-only
  -y, --browser                     Open mailbox browser
  -Z, --check-new-mail              Check for new mail (exit if none)
  -z, --check-any-mail              Check for any mail (exit if none)
```

---

## See Also

- Config files: <https://neomutt.org/guide/configuration>
- NeoMutt manual: <https://neomutt.org/guide/>
- Source: `cli/parse.c`, `cli/objects.h`, `usage.c`
