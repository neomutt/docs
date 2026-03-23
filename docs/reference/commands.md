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

```{toctree}
---
maxdepth: 1
hidden:
---
commands/alias
commands/color
commands/compress
commands/config
commands/core
commands/email
commands/hooks
commands/imap
commands/keys
commands/lists
commands/lua
commands/mailbox
commands/mime
commands/send
commands/sidebar
commands/spam
commands/tags
```

The following are the commands understood by NeoMutt.

| Command                                                                                            | Description                                                                                |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [`account-hook regex command`](cmd-account-hook)                                                   | Execute command when NeoMutt needs to access a matching account                            |
| [`alias [-group name ...] key address [, address ...]`](cmd-alias)                                 | Define an email alias                                                                      |
| [`alternates [-group name ...] regex [regex ...]`](cmd-alternates)                                 | Define alternate email addresses belonging to the user                                     |
| [`alternative-order mime-type[/subtype] [...]`](cmd-alternative-order)                             | Set preferred order of MIME alternatives                                                   |
| `alternative_order`                                                                                | {bdg-danger-line}`Deprecated` Use [`alternative-order`](cmd-alternative-order) instead     |
| [`append-hook regex "shell-command"`](cmd-append-hook)                                             | Define command to append to a compressed mailbox                                           |
| [`attachments ?`](cmd-attachments)                                                                 | Query current attachment settings                                                          |
| [`attachments {+ \| -} disposition mime-type [...]`](cmd-attachments)                              | Configure attachment counting                                                              |
| [`auto-view mime-type[/subtype] [...]`](cmd-auto-view)                                             | Automatically view MIME types using mailcap                                                |
| `auto_view`                                                                                        | {bdg-danger-line}`Deprecated` Use [`auto-view`](cmd-auto-view) instead                     |
| [`bind map[,map ...] key function`](cmd-bind)                                                      | Bind a key to a function in a map                                                          |
| [`cd [directory]`](cmd-cd)                                                                         | Change NeoMutt's working directory                                                         |
| [`charset-hook alias charset`](cmd-charset-hook)                                                   | Define a charset alias                                                                     |
| [`close-hook regex "shell-command"`](cmd-close-hook)                                               | Define command to close a compressed mailbox                                               |
| [`color index [attr ...] fg bg [pattern]`](cmd-color)                                              | Set colour for index pattern match                                                         |
| [`color object [attribute ...] foreground background`](cmd-color)                                  | Set colour for an object                                                                   |
| [`color {header \| body} [attr ...] fg bg regex`](cmd-color)                                       | Set colour for header/body regex match                                                     |
| [`crypt-hook regex keyid`](cmd-crypt-hook)                                                         | Associate a key with addresses matching regex                                              |
| [`echo message`](cmd-echo)                                                                         | Print a message to the message window                                                      |
| [`exec function [function ...]`](cmd-exec)                                                         | Execute one or more functions                                                              |
| [`fcc-hook pattern mailbox`](cmd-fcc-hook)                                                         | Set default Fcc folder                                                                     |
| [`fcc-save-hook pattern mailbox`](cmd-fcc-save-hook)                                               | Set default Fcc and save folder                                                            |
| [`finish`](cmd-finish)                                                                             | Stop processing the current config file                                                    |
| [`folder-hook [-noregex] regex command`](cmd-folder-hook)                                          | Execute command when entering a folder                                                     |
| [`group [-group name ...] {-rx regex ... \| -addr address ...}`](cmd-group)                        | Add addresses/patterns to a group                                                          |
| `hdr_order`                                                                                        | {bdg-danger-line}`Deprecated` Use [`header-order`](cmd-header-order) instead               |
| [`header-order header [header ...]`](cmd-header-order)                                             | Set order of displayed headers                                                             |
| [`hooks`](cmd-hooks)                                                                               | List all defined hooks                                                                     |
| [`iconv-hook charset local-charset`](cmd-iconv-hook)                                               | Define a charset conversion                                                                |
| [`ifdef symbol "config-command [args...]"`](cmd-ifdef)                                             | Execute command if symbol is defined                                                       |
| [`ifndef symbol "config-command [args...]"`](cmd-ifndef)                                           | Execute command if symbol is not defined                                                   |
| [`ignore string [string ...]`](cmd-ignore)                                                         | Ignore message headers matching string                                                     |
| [`index-format-hook name [!]pattern format-string`](cmd-index-format-hook)                         | Define conditional index format strings                                                    |
| [`lists [-group name ...] regex [regex ...]`](cmd-lists)                                           | Define mailing list addresses                                                              |
| [`lua lua-command`](cmd-lua)                                                                       | Execute a Lua command                                                                      |
| [`lua-source filename`](cmd-lua-source)                                                            | Source a Lua script file                                                                   |
| [`macro map[,map ...] key sequence [description]`](cmd-macro)                                      | Define a keyboard macro                                                                    |
| [`mailboxes [-label label] [-notify\|-nonotify] [-poll\|-nopoll] mailbox [...]`](cmd-mailboxes)    | Define mailboxes to monitor for new mail                                                   |
| [`mailto-allow {* \| header-field ...}`](cmd-mailto-allow)                                         | Allow header fields in mailto: URLs                                                        |
| `mailto_allow`                                                                                     | {bdg-danger-line}`Deprecated` Use [`mailto-allow`](cmd-mailto-allow) instead               |
| [`mbox-hook [-noregex] regex mailbox`](cmd-mbox-hook)                                              | Move read messages to a mailbox                                                            |
| [`message-hook pattern command`](cmd-message-hook)                                                 | Execute command when reading a matching message                                            |
| [`mime-lookup mime-type[/subtype] [...]`](cmd-mime-lookup)                                         | Look up MIME type by file extension                                                        |
| `mime_lookup`                                                                                      | {bdg-danger-line}`Deprecated` Use [`mime-lookup`](cmd-mime-lookup) instead                 |
| [`mono index-object attribute pattern`](cmd-mono)                                                  | Set monochrome attribute for index match                                                   |
| [`mono object attribute`](cmd-mono)                                                                | Set monochrome attribute for an object                                                     |
| [`mono {header \| body} attribute regex`](cmd-mono)                                                | Set monochrome attribute for header/body match                                             |
| [`my-header string`](cmd-my-header)                                                                | Add a custom header to outgoing messages                                                   |
| `my_hdr`                                                                                           | {bdg-danger-line}`Deprecated` Use [`my-header`](cmd-my-header) instead                     |
| [`named-mailboxes [-notify\|-nonotify] [-poll\|-nopoll] label mailbox [...]`](cmd-named-mailboxes) | Define named mailboxes                                                                     |
| [`nospam {* \| regex}`](cmd-nospam)                                                                | Remove spam detection patterns                                                             |
| [`open-hook regex "shell-command"`](cmd-open-hook)                                                 | Define command to open a compressed mailbox                                                |
| [`push string`](cmd-push)                                                                          | Push a string of keystrokes onto the **beginning** of the input buffer                     |
| [`reply-hook pattern command`](cmd-reply-hook)                                                     | Execute command when replying to a matching message                                        |
| [`reset variable [variable ...]`](cmd-reset)                                                       | Reset a config option to its default                                                       |
| [`save-hook pattern mailbox`](cmd-save-hook)                                                       | Set default save folder                                                                    |
| [`score pattern value`](cmd-score)                                                                 | Assign a score to messages matching pattern                                                |
| [`send-hook pattern command`](cmd-send-hook)                                                       | Execute command when sending a matching message                                            |
| [`send2-hook pattern command`](cmd-send2-hook)                                                     | Execute command when changing a message during composition                                 |
| [`set variable=value [variable+=increment] [variable-=decrement] [...]`](cmd-set)                  | Assign a value to a config option                                                          |
| [`set [no\|inv\|&]variable[?] [...]`](cmd-set)                                                     | Set, query, toggle, or reset a config option                                               |
| [`setenv {variable? \| variable=value}`](cmd-setenv)                                               | Set or query an environment variable                                                       |
| [`shutdown-hook command`](cmd-shutdown-hook)                                                       | Execute command at shutdown                                                                |
| [`sidebar-pin mailbox [mailbox ...]`](cmd-sidebar-pin)                                             | Pin a mailbox to the top of the sidebar                                                    |
| [`sidebar-unpin {* \| mailbox ...}`](cmd-sidebar-unpin)                                            | Unpin a mailbox from the sidebar                                                           |
| `sidebar_pin`                                                                                      | {bdg-danger-line}`Deprecated` Use [`sidebar-pin`](cmd-sidebar-pin) instead                 |
| `sidebar_unpin`                                                                                    | {bdg-danger-line}`Deprecated` Use [`sidebar-unpin`](cmd-sidebar-unpin) instead             |
| [`source filename [filename ...]`](cmd-source)                                                     | Read configuration commands from a file                                                    |
| [`spam regex [format]`](cmd-spam)                                                                  | Define a spam detection pattern                                                            |
| [`startup-hook command`](cmd-startup-hook)                                                         | Execute command at startup                                                                 |
| [`subject-regex regex replacement`](cmd-subject-regex)                                             | Define a subject display replacement                                                       |
| [`subscribe [-group name ...] regex [regex ...]`](cmd-subscribe)                                   | Mark mailing lists as subscribed                                                           |
| [`subscribe-to imap-folder-uri`](cmd-subscribe-to)                                                 | Subscribe to an IMAP folder                                                                |
| [`tag-formats tag format-string [...]`](cmd-tag-formats)                                           | Define display format for tags                                                             |
| [`tag-transforms tag transformed-string [...]`](cmd-tag-transforms)                                | Define display transformation for tags                                                     |
| [`timeout-hook command`](cmd-timeout-hook)                                                         | Execute command on timeout                                                                 |
| [`toggle variable [variable ...]`](cmd-toggle)                                                     | Toggle a boolean config option                                                             |
| [`unalias {* \| key ...}`](cmd-unalias)                                                            | Remove an email alias                                                                      |
| [`unalternates {* \| regex ...}`](cmd-unalternates)                                                | Remove alternate address patterns                                                          |
| [`unalternative-order {* \| mime-type[/subtype] ...}`](cmd-unalternative-order)                    | Remove alternative order entries                                                           |
| `unalternative_order`                                                                              | {bdg-danger-line}`Deprecated` Use [`unalternative-order`](cmd-unalternative-order) instead |
| [`unattachments *`](cmd-unattachments)                                                             | Remove all attachment rules                                                                |
| [`unattachments {+ \| -} disposition mime-type [...]`](cmd-unattachments)                          | Remove attachment counting rules                                                           |
| [`unauto-view {* \| mime-type[/subtype] ...}`](cmd-unauto-view)                                    | Remove auto-view entries                                                                   |
| `unauto_view`                                                                                      | {bdg-danger-line}`Deprecated` Use [`unauto-view`](cmd-unauto-view) instead                 |
| [`unbind {* \| map[,map ...]} [key]`](cmd-unbind)                                                  | Remove a key binding                                                                       |
| [`uncolor {index \| header \| body} {* \| pattern ...}`](cmd-uncolor)                              | Remove colour rules                                                                        |
| [`ungroup [-group name ...] {* \| -rx regex ... \| -addr address ...}`](cmd-ungroup)               | Remove addresses/patterns from a group                                                     |
| `unhdr_order`                                                                                      | {bdg-danger-line}`Deprecated` Use [`unheader-order`](cmd-unheader-order) instead           |
| [`unheader-order {* \| header ...}`](cmd-unheader-order)                                           | Remove header order entries                                                                |
| [`unhook {* \| hook-type}`](cmd-unhook)                                                            | Remove hooks                                                                               |
| [`unignore {* \| string ...}`](cmd-unignore)                                                       | Stop ignoring headers                                                                      |
| [`unlists {* \| regex ...}`](cmd-unlists)                                                          | Remove mailing list definitions                                                            |
| [`unmacro {* \| map[,map ...]} [key]`](cmd-unmacro)                                                | Remove a keyboard macro                                                                    |
| [`unmailboxes {* \| mailbox ...}`](cmd-unmailboxes)                                                | Remove mailbox definitions                                                                 |
| [`unmailto-allow {* \| header-field ...}`](cmd-unmailto-allow)                                     | Disallow header fields in mailto: URLs                                                     |
| `unmailto_allow`                                                                                   | {bdg-danger-line}`Deprecated` Use [`unmailto-allow`](cmd-unmailto-allow) instead           |
| [`unmime-lookup {* \| mime-type[/subtype] ...}`](cmd-unmime-lookup)                                | Remove MIME lookup entries                                                                 |
| `unmime_lookup`                                                                                    | {bdg-danger-line}`Deprecated` Use [`unmime-lookup`](cmd-unmime-lookup) instead             |
| [`unmono {index-object \| header \| body} {* \| pattern ...}`](cmd-unmono)                         | Remove monochrome rules                                                                    |
| [`unmy-header {* \| field ...}`](cmd-unmy-header)                                                  | Remove custom headers                                                                      |
| `unmy_hdr`                                                                                         | {bdg-danger-line}`Deprecated` Use [`unmy-header`](cmd-unmy-header) instead                 |
| [`unscore {* \| pattern ...}`](cmd-unscore)                                                        | Remove score entries                                                                       |
| [`unset variable [variable ...]`](cmd-unset)                                                       | Unset a boolean config option                                                              |
| [`unsetenv variable`](cmd-unsetenv)                                                                | Remove an environment variable                                                             |
| [`unsubject-regex {* \| regex}`](cmd-unsubject-regex)                                              | Remove subject display replacements                                                        |
| [`unsubscribe {* \| regex ...}`](cmd-unsubscribe)                                                  | Unsubscribe from mailing lists                                                             |
| [`unsubscribe-from imap-folder-uri`](cmd-unsubscribe-from)                                         | Unsubscribe from an IMAP folder                                                            |
| [`version`](cmd-version)                                                                           | Display NeoMutt version information                                                        |
