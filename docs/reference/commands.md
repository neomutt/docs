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

| Command                                                                                       | Description                                                                 |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [`account-hook regex command`](commands/hooks)                                                     | Execute command when NeoMutt needs to access a matching account             |
| [`alias [-group name ...] key address [, address ...]`](commands/alias)                            | Define an email alias                                                       |
| [`alternates [-group name ...] regex [regex ...]`](commands/alias)                                 | Define alternate email addresses belonging to the user                      |
| [`alternative-order mime-type[/subtype] [...]`](commands/mime)                                     | Set preferred order of MIME alternatives                                    |
| `alternative_order`                                                                           | {bdg-danger-line}`Deprecated` Use [`alternative-order`](commands/mime) instead   |
| [`append-hook regex "shell-command"`](commands/compress)                                           | Define command to append to a compressed mailbox                            |
| [`attachments ?`](commands/mime)                                                                   | Query current attachment settings                                           |
| [`attachments {+ \| -} disposition mime-type [...]`](commands/mime)                                | Configure attachment counting                                               |
| [`auto-view mime-type[/subtype] [...]`](commands/mime)                                             | Automatically view MIME types using mailcap                                 |
| `auto_view`                                                                                   | {bdg-danger-line}`Deprecated` Use [`auto-view`](commands/mime) instead           |
| [`bind map[,map ...] key function`](commands/keys)                                                 | Bind a key to a function in a map                                           |
| [`cd [directory]`](commands/core)                                                                  | Change NeoMutt's working directory                                          |
| [`charset-hook alias charset`](commands/hooks)                                                     | Define a charset alias                                                      |
| [`close-hook regex "shell-command"`](commands/compress)                                            | Define command to close a compressed mailbox                                |
| [`color index [attr ...] fg bg [pattern]`](commands/color)                                         | Set colour for index pattern match                                          |
| [`color object [attribute ...] foreground background`](commands/color)                             | Set colour for an object                                                    |
| [`color {header \| body} [attr ...] fg bg regex`](commands/color)                                  | Set colour for header/body regex match                                      |
| [`crypt-hook regex keyid`](commands/hooks)                                                         | Associate a key with addresses matching regex                               |
| [`echo message`](commands/core)                                                                    | Print a message to the message window                                       |
| [`exec function [function ...]`](commands/keys)                                                    | Execute one or more functions                                               |
| [`fcc-hook pattern mailbox`](commands/hooks)                                                       | Set default Fcc folder                                                      |
| [`fcc-save-hook pattern mailbox`](commands/hooks)                                                  | Set default Fcc and save folder                                             |
| [`finish`](commands/core)                                                                          | Stop processing the current config file                                     |
| [`folder-hook [-noregex] regex command`](commands/hooks)                                           | Execute command when entering a folder                                      |
| [`group [-group name ...] {-rx regex ... \| -addr address ...}`](commands/alias)                   | Add addresses/patterns to a group                                           |
| `hdr_order`                                                                                   | {bdg-danger-line}`Deprecated` Use [`header-order`](commands/email) instead       |
| [`header-order header [header ...]`](commands/email)                                               | Set order of displayed headers                                              |
| [`hooks`](commands/hooks)                                                                          | List all defined hooks                                                      |
| [`iconv-hook charset local-charset`](commands/hooks)                                               | Define a charset conversion                                                 |
| [`ifdef symbol "config-command [args...]"`](commands/core)                                         | Execute command if symbol is defined                                        |
| [`ifndef symbol "config-command [args...]"`](commands/core)                                        | Execute command if symbol is not defined                                    |
| [`ignore string [string ...]`](commands/email)                                                     | Ignore message headers matching string                                      |
| [`index-format-hook name [!]pattern format-string`](commands/hooks)                                | Define conditional index format strings                                     |
| [`lists [-group name ...] regex [regex ...]`](commands/lists)                                      | Define mailing list addresses                                               |
| [`lua lua-command`](commands/lua)                                                                  | Execute a Lua command                                                       |
| [`lua-source filename`](commands/lua)                                                              | Source a Lua script file                                                    |
| [`macro map[,map ...] key sequence [description]`](commands/keys)                                  | Define a keyboard macro                                                     |
| [`mailboxes [-label label] [-notify\|-nonotify] [-poll\|-nopoll] mailbox [...]`](commands/mailbox) | Define mailboxes to monitor for new mail                                    |
| [`mailto-allow {* \| header-field ...}`](commands/mime)                                            | Allow header fields in mailto: URLs                                         |
| `mailto_allow`                                                                                | {bdg-danger-line}`Deprecated` Use [`mailto-allow`](commands/mime) instead        |
| [`mbox-hook [-noregex] regex mailbox`](commands/hooks)                                             | Move read messages to a mailbox                                             |
| [`message-hook pattern command`](commands/hooks)                                                   | Execute command when reading a matching message                             |
| [`mime-lookup mime-type[/subtype] [...]`](commands/mime)                                           | Look up MIME type by file extension                                         |
| `mime_lookup`                                                                                 | {bdg-danger-line}`Deprecated` Use [`mime-lookup`](commands/mime) instead         |
| [`mono index-object attribute pattern`](commands/color)                                            | Set monochrome attribute for index match                                    |
| [`mono object attribute`](commands/color)                                                          | Set monochrome attribute for an object                                      |
| [`mono {header \| body} attribute regex`](commands/color)                                          | Set monochrome attribute for header/body match                              |
| [`my-header string`](commands/send)                                                                | Add a custom header to outgoing messages                                    |
| `my_hdr`                                                                                      | {bdg-danger-line}`Deprecated` Use [`my-header`](commands/send) instead           |
| [`named-mailboxes [-notify\|-nonotify] [-poll\|-nopoll] label mailbox [...]`](commands/mailbox)    | Define named mailboxes                                                      |
| [`nospam {* \| regex}`](commands/spam)                                                             | Remove spam detection patterns                                              |
| [`open-hook regex "shell-command"`](commands/compress)                                             | Define command to open a compressed mailbox                                 |
| [`push string`](commands/keys)                                                                     | Push a string of keystrokes onto the **beginning** of the input buffer      |
| [`reply-hook pattern command`](commands/hooks)                                                     | Execute command when replying to a matching message                         |
| [`reset variable [variable ...]`](commands/config)                                                 | Reset a config option to its default                                        |
| [`save-hook pattern mailbox`](commands/hooks)                                                      | Set default save folder                                                     |
| [`score pattern value`](commands/spam)                                                             | Assign a score to messages matching pattern                                 |
| [`send-hook pattern command`](commands/hooks)                                                      | Execute command when sending a matching message                             |
| [`send2-hook pattern command`](commands/hooks)                                                     | Execute command when changing a message during composition                  |
| [`set variable=value [variable+=increment] [variable-=decrement] [...]`](commands/config)          | Assign a value to a config option                                           |
| [`set [no\|inv\|&]variable[?] [...]`](commands/config)                                             | Set, query, toggle, or reset a config option                                |
| [`setenv {variable? \| variable=value}`](commands/config)                                          | Set or query an environment variable                                        |
| [`shutdown-hook command`](commands/hooks)                                                          | Execute command at shutdown                                                 |
| [`sidebar-pin mailbox [mailbox ...]`](commands/sidebar)                                            | Pin a mailbox to the top of the sidebar                                     |
| [`sidebar-unpin {* \| mailbox ...}`](commands/sidebar)                                             | Unpin a mailbox from the sidebar                                            |
| `sidebar_pin`                                                                                 | {bdg-danger-line}`Deprecated` Use [`sidebar-pin`](commands/sidebar) instead      |
| `sidebar_unpin`                                                                               | {bdg-danger-line}`Deprecated` Use [`sidebar-unpin`](commands/sidebar) instead    |
| [`source filename [filename ...]`](commands/core)                                                  | Read configuration commands from a file                                     |
| [`spam regex [format]`](commands/spam)                                                             | Define a spam detection pattern                                             |
| [`startup-hook command`](commands/hooks)                                                           | Execute command at startup                                                  |
| [`subject-regex regex replacement`](commands/email)                                                | Define a subject display replacement                                        |
| [`subscribe [-group name ...] regex [regex ...]`](commands/lists)                                  | Mark mailing lists as subscribed                                            |
| [`subscribe-to imap-folder-uri`](commands/imap)                                                    | Subscribe to an IMAP folder                                                 |
| [`tag-formats tag format-string [...]`](commands/tags)                                             | Define display format for tags                                              |
| [`tag-transforms tag transformed-string [...]`](commands/tags)                                     | Define display transformation for tags                                      |
| [`timeout-hook command`](commands/hooks)                                                           | Execute command on timeout                                                  |
| [`toggle variable [variable ...]`](commands/config)                                                | Toggle a boolean config option                                              |
| [`unalias {* \| key ...}`](commands/alias)                                                         | Remove an email alias                                                       |
| [`unalternates {* \| regex ...}`](commands/alias)                                                  | Remove alternate address patterns                                           |
| [`unalternative-order {* \| mime-type[/subtype] ...}`](commands/mime)                              | Remove alternative order entries                                            |
| `unalternative_order`                                                                         | {bdg-danger-line}`Deprecated` Use [`unalternative-order`](commands/mime) instead |
| [`unattachments *`](commands/mime)                                                                 | Remove all attachment rules                                                 |
| [`unattachments {+ \| -} disposition mime-type [...]`](commands/mime)                              | Remove attachment counting rules                                            |
| [`unauto-view {* \| mime-type[/subtype] ...}`](commands/mime)                                      | Remove auto-view entries                                                    |
| `unauto_view`                                                                                 | {bdg-danger-line}`Deprecated` Use [`unauto-view`](commands/mime) instead         |
| [`unbind {* \| map[,map ...]} [key]`](commands/keys)                                               | Remove a key binding                                                        |
| [`uncolor {index \| header \| body} {* \| pattern ...}`](commands/color)                           | Remove colour rules                                                         |
| [`ungroup [-group name ...] {* \| -rx regex ... \| -addr address ...}`](commands/alias)            | Remove addresses/patterns from a group                                      |
| `unhdr_order`                                                                                 | {bdg-danger-line}`Deprecated` Use [`unheader-order`](commands/email) instead     |
| [`unheader-order {* \| header ...}`](commands/email)                                               | Remove header order entries                                                 |
| [`unhook {* \| hook-type}`](commands/hooks)                                                        | Remove hooks                                                                |
| [`unignore {* \| string ...}`](commands/email)                                                     | Stop ignoring headers                                                       |
| [`unlists {* \| regex ...}`](commands/lists)                                                       | Remove mailing list definitions                                             |
| [`unmacro {* \| map[,map ...]} [key]`](commands/keys)                                              | Remove a keyboard macro                                                     |
| [`unmailboxes {* \| mailbox ...}`](commands/mailbox)                                               | Remove mailbox definitions                                                  |
| [`unmailto-allow {* \| header-field ...}`](commands/mime)                                          | Disallow header fields in mailto: URLs                                      |
| `unmailto_allow`                                                                              | {bdg-danger-line}`Deprecated` Use [`unmailto-allow`](commands/mime) instead      |
| [`unmime-lookup {* \| mime-type[/subtype] ...}`](commands/mime)                                    | Remove MIME lookup entries                                                  |
| `unmime_lookup`                                                                               | {bdg-danger-line}`Deprecated` Use [`unmime-lookup`](commands/mime) instead       |
| [`unmono {index-object \| header \| body} {* \| pattern ...}`](commands/color)                     | Remove monochrome rules                                                     |
| [`unmy-header {* \| field ...}`](commands/send)                                                    | Remove custom headers                                                       |
| `unmy_hdr`                                                                                    | {bdg-danger-line}`Deprecated` Use [`unmy-header`](commands/send) instead         |
| [`unscore {* \| pattern ...}`](commands/spam)                                                      | Remove score entries                                                        |
| [`unset variable [variable ...]`](commands/config)                                                 | Unset a boolean config option                                               |
| [`unsetenv variable`](commands/config)                                                             | Remove an environment variable                                              |
| [`unsubject-regex {* \| regex}`](commands/email)                                                   | Remove subject display replacements                                         |
| [`unsubscribe {* \| regex ...}`](commands/lists)                                                   | Unsubscribe from mailing lists                                              |
| [`unsubscribe-from imap-folder-uri`](commands/imap)                                                | Unsubscribe from an IMAP folder                                             |
| [`version`](commands/core)                                                                         | Display NeoMutt version information                                         |
