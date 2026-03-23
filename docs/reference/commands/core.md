---
title: Core Commands
description: XXX
keywords: XXX
---

# Core Commands

Commands for configuration, scripting, and general NeoMutt control.

## `cd`

Change NeoMutt's current working directory.

- `cd <directory>` — change to a specific directory
- `cd` — change to the home directory

```neomuttrc
cd ~/Mail
cd /tmp
cd
```

## `echo`

Print a message to the status line.  Useful for debugging config files.

- `echo <message>` — display a message string

```neomuttrc
echo "NeoMutt config loaded successfully"
echo "Current editor: $editor"
```

## `finish`

Stop reading the current config file.  Useful inside `ifdef`/`ifndef` blocks
to skip the rest of a conditionally-sourced file.

```neomuttrc
ifndef imap 'finish'
```

## `ifdef`

Conditionally run a config command if a symbol (variable, feature, command) is defined.

- `ifdef <symbol> '<command>'` — run a command if the symbol exists

```neomuttrc
ifdef imap   'source ~/.config/neomutt/imap.rc'
ifdef sidebar 'source ~/.config/neomutt/sidebar.rc'
ifdef notmuch 'source ~/.config/neomutt/notmuch.rc'
```

## `ifndef`

Conditionally run a command if a symbol is **not** defined.

- `ifndef <symbol> '<command>'` — run a command if the symbol is missing

```neomuttrc
ifndef sidebar 'echo "Sidebar support is not available"'
ifndef imap    'set spoolfile = ~/Mail/INBOX'
```

## `source`

Read and execute commands from an external config file.

- `source <filename>` — execute a config file
- `source <file1> <file2>` — execute multiple files in order

```neomuttrc
source ~/.config/neomutt/colors.rc
source ~/.config/neomutt/hooks.rc ~/.config/neomutt/keys.rc
source "gpg --quiet --decrypt ~/.config/neomutt/passwords.gpg|"
```

## `version`

Show NeoMutt version and build information in the pager.

```neomuttrc
version
```

