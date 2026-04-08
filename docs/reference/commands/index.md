---
title: Commands
description: Complete reference index of all NeoMutt configuration commands with syntax, descriptions, and links to details.
keywords: neomutt, commands, configuration, neomuttrc, reference, index, directives, command list, config commands, syntax reference, command summary
---

(ref-commands)=
# Commands

The following are the commands understood by NeoMutt.

---

[Alias](ref-cmd-alias)
[Color](ref-cmd-color)
[Compress](ref-cmd-compress)
[Config](ref-cmd-config)
[Core](ref-cmd-core)
[Email](ref-cmd-email)
[Hooks](ref-cmd-hooks)
[Imap](ref-cmd-imap)
[Keys](ref-cmd-keys)
[Lists](ref-cmd-lists)
[Lua](ref-cmd-lua)
[Mailbox](ref-cmd-mailbox)
[Mime](ref-cmd-mime)
[Send](ref-cmd-send)
[Sidebar](ref-cmd-sidebar)
[Spam](ref-cmd-spam)
[Tags](ref-cmd-tags)

---

| Command                                                                                            | Description                                                                      |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [`account-hook regex command`](cmd-account-hook)                                                   | Execute command when NeoMutt needs to access a matching account                  |
| [`alias [-group name ...] key address [, address ...]`](cmd-alias)                                 | Define an email alias                                                            |
| [`alternates [-group name ...] regex [regex ...]`](cmd-alternates)                                 | Define alternate email addresses belonging to the user                           |
| [`alternative-order mime-type[/subtype] [...]`](cmd-alternative-order)                             | Set preferred order of MIME alternatives                                         |
| `alternative_order`                                                                                | {bdg-warning-line}`Renamed to:` [`alternative-order`](cmd-alternative-order)     |
| [`append-hook regex "shell-command"`](cmd-append-hook)                                             | Define command to append to a compressed mailbox                                 |
| [`attachments ?`](cmd-attachments)                                                                 | Query current attachment settings                                                |
| [`attachments {+ \| -} disposition mime-type [...]`](cmd-attachments)                              | Configure attachment counting                                                    |
| [`auto-view mime-type[/subtype] [...]`](cmd-auto-view)                                             | Automatically view MIME types using mailcap                                      |
| `auto_view`                                                                                        | {bdg-warning-line}`Renamed to:` [`auto-view`](cmd-auto-view)                     |
| [`bind map[,map ...] key function`](cmd-bind)                                                      | Bind a key to a function in a map                                                |
| [`cd [directory]`](cmd-cd)                                                                         | Change NeoMutt's working directory                                               |
| [`charset-hook alias charset`](cmd-charset-hook)                                                   | Define a charset alias                                                           |
| [`close-hook regex "shell-command"`](cmd-close-hook)                                               | Define command to close a compressed mailbox                                     |
| [`color index [attr ...] fg bg [pattern]`](cmd-color)                                              | Set colour for index pattern match                                               |
| [`color object [attribute ...] foreground background`](cmd-color)                                  | Set colour for an object                                                         |
| [`color {header \| body} [attr ...] fg bg regex`](cmd-color)                                       | Set colour for header/body regex match                                           |
| [`crypt-hook regex keyid`](cmd-crypt-hook)                                                         | Associate a key with addresses matching regex                                    |
| [`echo message`](cmd-echo)                                                                         | Print a message to the message window                                            |
| [`exec function [function ...]`](cmd-exec)                                                         | Execute one or more functions                                                    |
| [`fcc-hook pattern mailbox`](cmd-fcc-hook)                                                         | Set default Fcc folder                                                           |
| [`fcc-save-hook pattern mailbox`](cmd-fcc-save-hook)                                               | Set default Fcc and save folder                                                  |
| [`finish`](cmd-finish)                                                                             | Stop processing the current config file                                          |
| [`folder-hook [-noregex] regex command`](cmd-folder-hook)                                          | Execute command when entering a folder                                           |
| [`group [-group name ...] {-rx regex ... \| -addr address ...}`](cmd-group)                        | Add addresses/patterns to a group                                                |
| `hdr_order`                                                                                        | {bdg-warning-line}`Renamed to:` [`header-order`](cmd-header-order)               |
| [`header-order header [header ...]`](cmd-header-order)                                             | Set order of displayed headers                                                   |
| [`hooks`](cmd-hooks)                                                                               | List all defined hooks                                                           |
| [`iconv-hook charset local-charset`](cmd-iconv-hook)                                               | Define a charset conversion                                                      |
| [`ifdef symbol "config-command [args...]"`](cmd-ifdef)                                             | Execute command if symbol is defined                                             |
| [`ifndef symbol "config-command [args...]"`](cmd-ifndef)                                           | Execute command if symbol is not defined                                         |
| [`ignore string [string ...]`](cmd-ignore)                                                         | Ignore message headers matching string                                           |
| [`index-format-hook name [!]pattern format-string`](cmd-index-format-hook)                         | Define conditional index format strings                                          |
| [`lists [-group name ...] regex [regex ...]`](cmd-lists)                                           | Define mailing list addresses                                                    |
| [`lua lua-command`](cmd-lua)                                                                       | Execute a Lua command                                                            |
| [`lua-source filename`](cmd-lua-source)                                                            | Source a Lua script file                                                         |
| [`macro map[,map ...] key sequence [description]`](cmd-macro)                                      | Define a keyboard macro                                                          |
| [`mailboxes [-label label] [-notify\|-nonotify] [-poll\|-nopoll] mailbox [...]`](cmd-mailboxes)    | Define mailboxes to monitor for new mail                                         |
| [`mailto-allow {* \| header-field ...}`](cmd-mailto-allow)                                         | Allow header fields in mailto: URLs                                              |
| `mailto_allow`                                                                                     | {bdg-warning-line}`Renamed to:` [`mailto-allow`](cmd-mailto-allow)               |
| [`mbox-hook [-noregex] regex mailbox`](cmd-mbox-hook)                                              | Move read messages to a mailbox                                                  |
| [`message-hook pattern command`](cmd-message-hook)                                                 | Execute command when reading a matching message                                  |
| [`mime-lookup mime-type[/subtype] [...]`](cmd-mime-lookup)                                         | Look up MIME type by file extension                                              |
| `mime_lookup`                                                                                      | {bdg-warning-line}`Renamed to:` [`mime-lookup`](cmd-mime-lookup)                 |
| [`mono index-object attribute pattern`](cmd-mono)                                                  | Set monochrome attribute for index match                                         |
| [`mono object attribute`](cmd-mono)                                                                | Set monochrome attribute for an object                                           |
| [`mono {header \| body} attribute regex`](cmd-mono)                                                | Set monochrome attribute for header/body match                                   |
| [`my-header string`](cmd-my-header)                                                                | Add a custom header to outgoing messages                                         |
| `my_hdr`                                                                                           | {bdg-warning-line}`Renamed to:` [`my-header`](cmd-my-header)                     |
| [`named-mailboxes [-notify\|-nonotify] [-poll\|-nopoll] label mailbox [...]`](cmd-named-mailboxes) | Define named mailboxes                                                           |
| [`nospam {* \| regex}`](cmd-nospam)                                                                | Remove spam detection patterns                                                   |
| [`open-hook regex "shell-command"`](cmd-open-hook)                                                 | Define command to open a compressed mailbox                                      |
| [`push string`](cmd-push)                                                                          | Push a string of keystrokes onto the **beginning** of the input buffer           |
| [`reply-hook pattern command`](cmd-reply-hook)                                                     | Execute command when replying to a matching message                              |
| [`reset variable [variable ...]`](cmd-reset)                                                       | Reset a config option to its default                                             |
| [`save-hook pattern mailbox`](cmd-save-hook)                                                       | Set default save folder                                                          |
| [`score pattern value`](cmd-score)                                                                 | Assign a score to messages matching pattern                                      |
| [`send-hook pattern command`](cmd-send-hook)                                                       | Execute command when sending a matching message                                  |
| [`send2-hook pattern command`](cmd-send2-hook)                                                     | Execute command when changing a message during composition                       |
| [`set variable=value [variable+=increment] [variable-=decrement] [...]`](cmd-set)                  | Assign a value to a config option                                                |
| [`set [no\|inv\|&]variable[?] [...]`](cmd-set)                                                     | Set, query, toggle, or reset a config option                                     |
| [`setenv {variable? \| variable=value}`](cmd-setenv)                                               | Set or query an environment variable                                             |
| [`shutdown-hook command`](cmd-shutdown-hook)                                                       | Execute command at shutdown                                                      |
| [`sidebar-pin mailbox [mailbox ...]`](cmd-sidebar-pin)                                             | Pin a mailbox to the top of the sidebar                                          |
| [`sidebar-unpin {* \| mailbox ...}`](cmd-sidebar-unpin)                                            | Unpin a mailbox from the sidebar                                                 |
| `sidebar_pin`                                                                                      | {bdg-warning-line}`Renamed to:` [`sidebar-pin`](cmd-sidebar-pin)                 |
| `sidebar_unpin`                                                                                    | {bdg-warning-line}`Renamed to:` [`sidebar-unpin`](cmd-sidebar-unpin)             |
| [`source filename [filename ...]`](cmd-source)                                                     | Read configuration commands from a file                                          |
| [`spam regex [format]`](cmd-spam)                                                                  | Define a spam detection pattern                                                  |
| [`startup-hook command`](cmd-startup-hook)                                                         | Execute command at startup                                                       |
| [`subject-regex regex replacement`](cmd-subject-regex)                                             | Define a subject display replacement                                             |
| [`subscribe [-group name ...] regex [regex ...]`](cmd-subscribe)                                   | Mark mailing lists as subscribed                                                 |
| [`subscribe-to imap-folder-uri`](cmd-subscribe-to)                                                 | Subscribe to an IMAP folder                                                      |
| [`tag-formats tag format-string [...]`](cmd-tag-formats)                                           | Define display format for tags                                                   |
| [`tag-transforms tag transformed-string [...]`](cmd-tag-transforms)                                | Define display transformation for tags                                           |
| [`timeout-hook command`](cmd-timeout-hook)                                                         | Execute command on timeout                                                       |
| [`toggle variable [variable ...]`](cmd-toggle)                                                     | Toggle a boolean config option                                                   |
| [`unalias {* \| key ...}`](cmd-unalias)                                                            | Remove an email alias                                                            |
| [`unalternates {* \| regex ...}`](cmd-unalternates)                                                | Remove alternate address patterns                                                |
| [`unalternative-order {* \| mime-type[/subtype] ...}`](cmd-unalternative-order)                    | Remove alternative order entries                                                 |
| `unalternative_order`                                                                              | {bdg-warning-line}`Renamed to:` [`unalternative-order`](cmd-unalternative-order) |
| [`unattachments *`](cmd-unattachments)                                                             | Remove all attachment rules                                                      |
| [`unattachments {+ \| -} disposition mime-type [...]`](cmd-unattachments)                          | Remove attachment counting rules                                                 |
| [`unauto-view {* \| mime-type[/subtype] ...}`](cmd-unauto-view)                                    | Remove auto-view entries                                                         |
| `unauto_view`                                                                                      | {bdg-warning-line}`Renamed to:` [`unauto-view`](cmd-unauto-view)                 |
| [`unbind {* \| map[,map ...]} [key]`](cmd-unbind)                                                  | Remove a key binding                                                             |
| [`uncolor {index \| header \| body} {* \| pattern ...}`](cmd-uncolor)                              | Remove colour rules                                                              |
| [`ungroup [-group name ...] {* \| -rx regex ... \| -addr address ...}`](cmd-ungroup)               | Remove addresses/patterns from a group                                           |
| `unhdr_order`                                                                                      | {bdg-warning-line}`Renamed to:` [`unheader-order`](cmd-unheader-order)           |
| [`unheader-order {* \| header ...}`](cmd-unheader-order)                                           | Remove header order entries                                                      |
| [`unhook {* \| hook-type}`](cmd-unhook)                                                            | Remove hooks                                                                     |
| [`unignore {* \| string ...}`](cmd-unignore)                                                       | Stop ignoring headers                                                            |
| [`unlists {* \| regex ...}`](cmd-unlists)                                                          | Remove mailing list definitions                                                  |
| [`unmacro {* \| map[,map ...]} [key]`](cmd-unmacro)                                                | Remove a keyboard macro                                                          |
| [`unmailboxes {* \| mailbox ...}`](cmd-unmailboxes)                                                | Remove mailbox definitions                                                       |
| [`unmailto-allow {* \| header-field ...}`](cmd-unmailto-allow)                                     | Disallow header fields in mailto: URLs                                           |
| `unmailto_allow`                                                                                   | {bdg-warning-line}`Renamed to:` [`unmailto-allow`](cmd-unmailto-allow)           |
| [`unmime-lookup {* \| mime-type[/subtype] ...}`](cmd-unmime-lookup)                                | Remove MIME lookup entries                                                       |
| `unmime_lookup`                                                                                    | {bdg-warning-line}`Renamed to:` [`unmime-lookup`](cmd-unmime-lookup)             |
| [`unmono {index-object \| header \| body} {* \| pattern ...}`](cmd-unmono)                         | Remove monochrome rules                                                          |
| [`unmy-header {* \| field ...}`](cmd-unmy-header)                                                  | Remove custom headers                                                            |
| `unmy_hdr`                                                                                         | {bdg-warning-line}`Renamed to:` [`unmy-header`](cmd-unmy-header)                 |
| [`unscore {* \| pattern ...}`](cmd-unscore)                                                        | Remove score entries                                                             |
| [`unset variable [variable ...]`](cmd-unset)                                                       | Unset a boolean config option                                                    |
| [`unsetenv variable`](cmd-unsetenv)                                                                | Remove an environment variable                                                   |
| [`unsubject-regex {* \| regex}`](cmd-unsubject-regex)                                              | Remove subject display replacements                                              |
| [`unsubscribe {* \| regex ...}`](cmd-unsubscribe)                                                  | Unsubscribe from mailing lists                                                   |
| [`unsubscribe-from imap-folder-uri`](cmd-unsubscribe-from)                                         | Unsubscribe from an IMAP folder                                                  |
| [`version`](cmd-version)                                                                           | Display NeoMutt version information                                              |

```{toctree}
---
maxdepth: 1
hidden:
---
alias
color
compress
config
core
email
hooks
imap
keys
lists
lua
mailbox
mime
send
sidebar
spam
tags
```

