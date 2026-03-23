---
title: Commands
description: Index of all NeoMutt configuration commands with syntax and descriptions
keywords: neomutt, commands, configuration, neomuttrc, reference, index
---

# Commands

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

The following are the commands understood by NeoMutt.

| Command                                                                        | Description                                                            |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------|
| `account-hook regex command`                                                   | Execute command when NeoMutt needs to access a matching account        |
| `alias [-group name ...] key address [, address ...]`                          | Define an email alias                                                  |
| `alternates [-group name ...] regex [regex ...]`                               | Define alternate email addresses belonging to the user                 |
| `alternative-order mime-type[/subtype] [...]`                                  | Set preferred order of MIME alternatives                               |
| `alternative_order`                                                            | {bdg-danger-line}`Deprecated` Use `alternative-order` instead          |
| `append-hook regex "shell-command"`                                            | Define command to append to a compressed mailbox                       |
| `attachments ?`                                                                | Query current attachment settings                                      |
| `attachments {+ \| -} disposition mime-type [...]`                             | Configure attachment counting                                          |
| `auto-view mime-type[/subtype] [...]`                                          | Automatically view MIME types using mailcap                            |
| `auto_view`                                                                    | {bdg-danger-line}`Deprecated` Use `auto-view` instead                  |
| `bind map[,map ...] key function`                                              | Bind a key to a function in a map                                      |
| `cd [directory]`                                                               | Change NeoMutt's working directory                                     |
| `charset-hook alias charset`                                                   | Define a charset alias                                                 |
| `close-hook regex "shell-command"`                                             | Define command to close a compressed mailbox                           |
| `color index [attr ...] fg bg [pattern]`                                       | Set colour for index pattern match                                     |
| `color object [attribute ...] foreground background`                           | Set colour for an object                                               |
| `color {header \| body} [attr ...] fg bg regex`                                | Set colour for header/body regex match                                 |
| `crypt-hook regex keyid`                                                       | Associate a key with addresses matching regex                          |
| `echo message`                                                                 | Print a message to the message window                                  |
| `exec function [function ...]`                                                 | Execute one or more functions                                          |
| `fcc-hook pattern mailbox`                                                     | Set default Fcc folder                                                 |
| `fcc-save-hook pattern mailbox`                                                | Set default Fcc and save folder                                        |
| `finish`                                                                       | Stop processing the current config file                                |
| `folder-hook [-noregex] regex command`                                         | Execute command when entering a folder                                 |
| `group [-group name ...] {-rx regex ... \| -addr address ...}`                 | Add addresses/patterns to a group                                      |
| `hdr_order`                                                                    | {bdg-danger-line}`Deprecated` Use `header-order` instead               |
| `header-order header [header ...]`                                             | Set order of displayed headers                                         |
| `hooks`                                                                        | List all defined hooks                                                 |
| `iconv-hook charset local-charset`                                             | Define a charset conversion                                            |
| `ifdef symbol "config-command [args...]"`                                      | Execute command if symbol is defined                                   |
| `ifndef symbol "config-command [args...]"`                                     | Execute command if symbol is not defined                               |
| `ignore string [string ...]`                                                   | Ignore message headers matching string                                 |
| `index-format-hook name [!]pattern format-string`                              | Define conditional index format strings                                |
| `lists [-group name ...] regex [regex ...]`                                    | Define mailing list addresses                                          |
| `lua-source filename`                                                          | Source a Lua script file                                               |
| `lua lua-command`                                                              | Execute a Lua command                                                  |
| `macro map[,map ...] key sequence [description]`                               | Define a keyboard macro                                                |
| `mailboxes [-label label] [-notify\|-nonotify] [-poll\|-nopoll] mailbox [...]` | Define mailboxes to monitor for new mail                               |
| `mailto-allow {* \| header-field ...}`                                         | Allow header fields in mailto: URLs                                    |
| `mailto_allow`                                                                 | {bdg-danger-line}`Deprecated` Use `mailto-allow` instead               |
| `mbox-hook [-noregex] regex mailbox`                                           | Move read messages to a mailbox                                        |
| `message-hook pattern command`                                                 | Execute command when reading a matching message                        |
| `mime-lookup mime-type[/subtype] [...]`                                        | Look up MIME type by file extension                                    |
| `mime_lookup`                                                                  | {bdg-danger-line}`Deprecated` Use `mime-lookup` instead                |
| `mono index-object attribute pattern`                                          | Set monochrome attribute for index match                               |
| `mono object attribute`                                                        | Set monochrome attribute for an object                                 |
| `mono {header \| body} attribute regex`                                        | Set monochrome attribute for header/body match                         |
| `my-header string`                                                             | Add a custom header to outgoing messages                               |
| `my_hdr`                                                                       | {bdg-danger-line}`Deprecated` Use `my-header` instead                  |
| `named-mailboxes [-notify\|-nonotify] [-poll\|-nopoll] label mailbox [...]`    | Define named mailboxes                                                 |
| `nospam {* \| regex}`                                                          | Remove spam detection patterns                                         |
| `open-hook regex "shell-command"`                                              | Define command to open a compressed mailbox                            |
| `push string`                                                                  | Push a string of keystrokes onto the **beginning** of the input buffer |
| `reply-hook pattern command`                                                   | Execute command when replying to a matching message                    |
| `reset variable [variable ...]`                                                | Reset a config option to its default                                   |
| `save-hook pattern mailbox`                                                    | Set default save folder                                                |
| `score pattern value`                                                          | Assign a score to messages matching pattern                            |
| `send-hook pattern command`                                                    | Execute command when sending a matching message                        |
| `send2-hook pattern command`                                                   | Execute command when changing a message during composition             |
| `setenv {variable? \| variable=value}`                                         | Set or query an environment variable                                   |
| `set variable=value [variable+=increment] [variable-=decrement] [...]`         | Assign a value to a config option                                      |
| `set [no\|inv\|&]variable[?] [...]`                                            | Set, query, toggle, or reset a config option                           |
| `shutdown-hook command`                                                        | Execute command at shutdown                                            |
| `sidebar-pin mailbox [mailbox ...]`                                            | Pin a mailbox to the top of the sidebar                                |
| `sidebar-unpin {* \| mailbox ...}`                                             | Unpin a mailbox from the sidebar                                       |
| `sidebar_pin`                                                                  | {bdg-danger-line}`Deprecated` Use `sidebar-pin` instead                |
| `sidebar_unpin`                                                                | {bdg-danger-line}`Deprecated` Use `sidebar-unpin` instead              |
| `source filename [filename ...]`                                               | Read configuration commands from a file                                |
| `spam regex [format]`                                                          | Define a spam detection pattern                                        |
| `startup-hook command`                                                         | Execute command at startup                                             |
| `subject-regex regex replacement`                                              | Define a subject display replacement                                   |
| `subscribe-to imap-folder-uri`                                                 | Subscribe to an IMAP folder                                            |
| `subscribe [-group name ...] regex [regex ...]`                                | Mark mailing lists as subscribed                                       |
| `tag-formats tag format-string [...]`                                          | Define display format for tags                                         |
| `tag-transforms tag transformed-string [...]`                                  | Define display transformation for tags                                 |
| `timeout-hook command`                                                         | Execute command on timeout                                             |
| `toggle variable [variable ...]`                                               | Toggle a boolean config option                                         |
| `unalias {* \| key ...}`                                                       | Remove an email alias                                                  |
| `unalternates {* \| regex ...}`                                                | Remove alternate address patterns                                      |
| `unalternative-order {* \| mime-type[/subtype] ...}`                           | Remove alternative order entries                                       |
| `unalternative_order`                                                          | {bdg-danger-line}`Deprecated` Use `unalternative-order` instead        |
| `unattachments *`                                                              | Remove all attachment rules                                            |
| `unattachments {+ \| -} disposition mime-type [...]`                           | Remove attachment counting rules                                       |
| `unauto-view {* \| mime-type[/subtype] ...}`                                   | Remove auto-view entries                                               |
| `unauto_view`                                                                  | {bdg-danger-line}`Deprecated` Use `unauto-view` instead                |
| `unbind {* \| map[,map ...]} [key]`                                            | Remove a key binding                                                   |
| `uncolor {index \| header \| body} {* \| pattern ...}`                         | Remove colour rules                                                    |
| `ungroup [-group name ...] {* \| -rx regex ... \| -addr address ...}`          | Remove addresses/patterns from a group                                 |
| `unhdr_order`                                                                  | {bdg-danger-line}`Deprecated` Use `unheader-order` instead             |
| `unheader-order {* \| header ...}`                                             | Remove header order entries                                            |
| `unhook {* \| hook-type}`                                                      | Remove hooks                                                           |
| `unignore {* \| string ...}`                                                   | Stop ignoring headers                                                  |
| `unlists {* \| regex ...}`                                                     | Remove mailing list definitions                                        |
| `unmacro {* \| map[,map ...]} [key]`                                           | Remove a keyboard macro                                                |
| `unmailboxes {* \| mailbox ...}`                                               | Remove mailbox definitions                                             |
| `unmailto-allow {* \| header-field ...}`                                       | Disallow header fields in mailto: URLs                                 |
| `unmailto_allow`                                                               | {bdg-danger-line}`Deprecated` Use `unmailto-allow` instead             |
| `unmime-lookup {* \| mime-type[/subtype] ...}`                                 | Remove MIME lookup entries                                             |
| `unmime_lookup`                                                                | {bdg-danger-line}`Deprecated` Use `unmime-lookup` instead              |
| `unmono {index-object \| header \| body} {* \| pattern ...}`                   | Remove monochrome rules                                                |
| `unmy-header {* \| field ...}`                                                 | Remove custom headers                                                  |
| `unmy_hdr`                                                                     | {bdg-danger-line}`Deprecated` Use `unmy-header` instead                |
| `unscore {* \| pattern ...}`                                                   | Remove score entries                                                   |
| `unsetenv variable`                                                            | Remove an environment variable                                         |
| `unset variable [variable ...]`                                                | Unset a boolean config option                                          |
| `unsubject-regex {* \| regex}`                                                 | Remove subject display replacements                                    |
| `unsubscribe-from imap-folder-uri`                                             | Unsubscribe from an IMAP folder                                        |
| `unsubscribe {* \| regex ...}`                                                 | Unsubscribe from mailing lists                                         |
| `version`                                                                      | Display NeoMutt version information                                    |

