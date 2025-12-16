# Commands

| Command               | Description                                                            |
| :-------------------- | :--------------------------------------------------------------------- |
| `account-hook`        | Run a command when switching to a matching account                     |
| `alias`               | Define an alias (name to email address)                                |
| `alternates`          | Define a list of alternate email addresses for the user                |
| `alternative_order`   | Set preference order for multipart alternatives                        |
| `append-hook`         | Define command to append to a compressed mailbox                       |
| `attachments`         | Set attachment counting rules                                          |
| `auto_view`           | Automatically display specified MIME types inline                      |
| `bind`                | Bind a key to a function                                               |
| `cd`                  | Change NeoMutt's current working directory                             |
| `charset-hook`        | Define charset alias for languages                                     |
| `close-hook`          | Define command to close a compressed mailbox                           |
| `color`               | Define colors for the user interface                                   |
| `crypt-hook`          | Specify which keyid to use for recipients matching regex               |
| `echo`                | Print a message to the status line                                     |
| `exec`                | Execute a function                                                     |
| `fcc-hook`            | Pattern rule to set the save location for outgoing mail                |
| `fcc-save-hook`       | Equivalent to both `fcc-hook` and `save-hook`                          |
| `finish`              | Stop reading current config file                                       |
| `folder-hook`         | Run a command upon entering a folder matching regex                    |
| `group`               | Add addresses to an address group                                      |
| `hdr_order`           | Define custom order of headers displayed                               |
| `iconv-hook`          | Define a system-specific alias for a character set                     |
| `ifdef`               | Conditionally include config commands if symbol defined                |
| `ifndef`              | Conditionally include if symbol is not defined                         |
| `ignore`              | Hide specified headers when displaying messages                        |
| `index-format-hook`   | Create dynamic index format strings                                    |
| `lists`               | Add address to the list of mailing lists                               |
| `lua`                 | Run a Lua expression or call a Lua function                            |
| `lua-source`          | Execute a Lua script file                                              |
| `macro`               | Define a keyboard macro                                                |
| `mailboxes`           | Define a list of mailboxes to watch                                    |
| `mailto_allow`        | Permit specific header-fields in mailto URL processing                 |
| `mbox-hook`           | On leaving a mailbox, move read messages matching a regex              |
| `message-hook`        | Run a command when viewing a message matching patterns                 |
| `mime_lookup`         | Map specified MIME types/subtypes to display handlers                  |
| `mono`                | **Deprecated**: Use `color`                                            |
| `my_hdr`              | Add a custom header to outgoing messages                               |
| `named-mailboxes`     | Define a list of labelled mailboxes to watch                           |
| `nospam`              | Remove a spam detection rule                                           |
| `open-hook`           | Define command to open a compressed mailbox                            |
| `pgp-hook`            | **Deprecated**: Use `crypt-hook`                                       |
| `push`                | Push a string into NeoMutt's input queue (simulate typing)             |
| `reply-hook`          | Run a command when replying to messages matching a pattern             |
| `reset`               | Reset a config option to its initial value                             |
| `save-hook`           | Set default save folder for messages                                   |
| `score`               | Set a score value on emails matching a pattern                         |
| `send-hook`           | Run a command when sending a message, new or reply, matching a pattern |
| `send2-hook`          | Run command whenever a composed message is edited                      |
| `set`                 | Set a config variable                                                  |
| `setenv`              | Set an environment variable                                            |
| `shutdown-hook`       | Run a command before NeoMutt exits                                     |
| `sidebar_pin`         | Pin a mailbox in the sidebar (keep visible)                            |
| `sidebar_unpin`       | Unpin a previously pinned mailbox in the sidebar                       |
| `sidebar_whitelist`   | **Deprecated**: Use `sidebar_pin`                                      |
| `source`              | Read and execute commands from a config file                           |
| `spam`                | Define rules to parse spam detection headers                           |
| `startup-hook`        | Run a command when NeoMutt starts up                                   |
| `subjectrx`           | Apply regex-based rewriting to message subjects                        |
| `subscribe`           | Add address to the list of subscribed mailing lists                    |
| `subscribe-to`        | Subscribe to an IMAP mailbox                                           |
| `tag-formats`         | Define expandos tags                                                   |
| `tag-transforms`      | Rules to transform tags into icons                                     |
| `timeout-hook`        | Run a command after a specified timeout or idle period                 |
| `toggle`              | Toggle the value of a boolean/quad config option                       |
| `unalias`             | Remove an alias definition                                             |
| `unalternates`        | Remove addresses from `alternates` list                                |
| `unalternative_order` | Remove MIME types from preference order                                |
| `unattachments`       | Remove attachment counting rules                                       |
| `unauto_view`         | Remove MIME types from `auto_view` list                                |
| `unbind`              | Remove a key binding                                                   |
| `uncolor`             | Remove a `color` definition                                            |
| `ungroup`             | Remove addresses from an address `group`                               |
| `unhdr_order`         | Remove header from `hdr_order` list                                    |
| `unhook`              | Remove hooks of a given type                                           |
| `unignore`            | Remove a header from the `hdr_order` list                              |
| `unlists`             | Remove address from the list of mailing lists                          |
| `unmacro`             | Remove a keyboard `macro`                                              |
| `unmailboxes`         | Remove mailboxes from the watch list                                   |
| `unmailto_allow`      | Disallow header-fields in mailto processing                            |
| `unmime_lookup`       | Remove custom MIME-type handlers                                       |
| `unmono`              | **Deprecated**: Use `uncolor`                                          |
| `unmy_hdr`            | Remove a header previously added with `my_hdr`                         |
| `unscore`             | Remove scoring rules for matching patterns                             |
| `unset`               | Reset a config option to false/empty                                   |
| `unsetenv`            | Unset an environment variable                                          |
| `unsidebar_whitelist` | **Deprecated**: Use `sidebar_unpin`                                    |
| `unsubjectrx`         | Remove subject-rewriting rules                                         |
| `unsubscribe`         | Remove address from the list of subscribed mailing lists               |
| `unsubscribe-from`    | Unsubscribe from an IMAP mailbox                                       |
| `unvirtual-mailboxes` | **Deprecated**: Use `unmailboxes`                                      |
| `version`             | Show NeoMutt version and build information                             |
| `virtual-mailboxes`   | **Deprecated**: Use `mailboxes`/`named-mailboxes`                      |

