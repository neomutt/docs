---
title: Mailbox Shortcuts
description: Reference for NeoMutt mailbox path shortcuts and special characters
keywords: neomutt, shortcuts, mailbox, path, folder
---

# Mailbox Shortcuts

There are a number of built in shortcuts which refer to specific mailboxes. These shortcuts can be used anywhere you are prompted for a file or mailbox path or in path-related configuration variables. Note that these only work at the beginning of a string.

## Shortcut Reference

| Shortcut    | Refers to...                                                         |
|-------------|----------------------------------------------------------------------|
| `!`         | Your `$spool_file` (incoming) mailbox                                |
| `>`         | Your `$mbox` file                                                    |
| `<`         | Your `$record` file                                                  |
| `^`         | The current mailbox                                                  |
| `-` or `!!` | The file you've last visited                                         |
| `~`         | Your home directory                                                  |
| `=` or `+`  | Your `$folder` directory                                             |
| *@alias*    | To the default save folder as determined by the address of the alias |

## Usage Example

To store a copy of outgoing messages in the folder they were composed in, a `folder-hook` can be used to set `$record`:

```neomuttrc
folder-hook . 'set record=^'
```

:::{note}
The current mailbox shortcut, `^`, has no value in some cases. No mailbox is opened when NeoMutt is invoked to send an email from the command-line. In interactive mode, NeoMutt reads the muttrc before opening the mailbox, so immediate expansion won't work as expected either. This can be an issue when trying to directly assign to `$record`, but also affects the `fcc-hook` mailbox, which is expanded immediately too. The folder-hook example above works because the command is executed later, when the folder-hook fires.
:::
