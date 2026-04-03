---
title: Hooks
description: Commands that trigger actions on events like entering a folder, sending mail, connecting to accounts, startup, shutdown, and timeouts.
keywords: hooks, account-hook, folder-hook, send-hook, send2-hook, reply-hook, message-hook, save-hook, fcc-hook, fcc-save-hook, mbox-hook, charset-hook, iconv-hook, crypt-hook, index-format-hook, startup-hook, shutdown-hook, timeout-hook, unhook, event triggers
---

(ref-cmd-hooks)=
# Hooks

Commands that trigger actions on specific events, patterns, or conditions.

(cmd-account-hook)=
## `account-hook`

Run a command when connecting to an account whose URL matches a regex.

- `account-hook <regex> <command>` — match against the account URL

```neomuttrc
account-hook imaps://user@work.example.com  'set imap_pass = "s3cret"'
account-hook .                               'unset imap_pass'
```

(cmd-folder-hook)=
## `folder-hook`

Run a command when entering a mailbox whose path matches a regex.

- `folder-hook <regex> <command>` — match against the folder path
- `folder-hook -noregex <string> <command>` — match as a literal string

```neomuttrc
folder-hook .          'set sort = date'
folder-hook INBOX     'set sort = reverse-date'
folder-hook neomutt-devel 'set strict_threads; set sort = threads'
folder-hook -noregex ~/Mail/work 'set from = "jane@work.example.com"'
```

(cmd-send-hook)=
## `send-hook`

Run a command when composing a new message or reply that matches a pattern.

- `send-hook <pattern> <command>` — match against the message being composed

```neomuttrc
send-hook .                    'set signature = ~/.signature'
send-hook '~t boss@company'   'set from = "jane@company.com"'
send-hook '~t @example\\.com' 'set pgp_auto_sign'
```

(cmd-send2-hook)=
## `send2-hook`

Run a command whenever a composed message is edited (every time the editor returns).

- `send2-hook <pattern> <command>` — match against the edited message

```neomuttrc
send2-hook . 'source ~/.config/neomutt/compose-hooks.rc'
```

(cmd-reply-hook)=
## `reply-hook`

Run a command when replying to a message that matches a pattern.
Runs before `send-hook`.

- `reply-hook <pattern> <command>`

```neomuttrc
reply-hook '~f boss@company' 'set from = "jane@company.com"'
```

(cmd-message-hook)=
## `message-hook`

Run a command when viewing a message that matches a pattern.

- `message-hook <pattern> <command>`

```neomuttrc
message-hook .            'reset pager_stop'
message-hook '~f admin@'  'set pager_stop'
```

(cmd-save-hook)=
## `save-hook`

Set the default save folder when saving messages that match a pattern.

- `save-hook <pattern> <mailbox>`

```neomuttrc
save-hook '~f boss@company'    =work.boss
save-hook '~t neomutt-devel@'  =lists.neomutt
save-hook .                    =saved
```

(cmd-fcc-hook)=
## `fcc-hook`

Set the sent-mail (Folder Carbon Copy) folder for outgoing messages
matching a pattern.

- `fcc-hook <pattern> <mailbox>`

```neomuttrc
fcc-hook '~t @company\\.com'  =sent.work
fcc-hook .                    =Sent
```

(cmd-fcc-save-hook)=
## `fcc-save-hook`

Shorthand — equivalent to setting both `fcc-hook` and `save-hook` with the
same pattern and mailbox.

- `fcc-save-hook <pattern> <mailbox>`

```neomuttrc
fcc-save-hook '~f boss@company' =work.boss
fcc-save-hook .                 =saved
```

(cmd-mbox-hook)=
## `mbox-hook`

When leaving a mailbox that matches a regex, move read messages to another
mailbox.

- `mbox-hook <regex> <mailbox>`

```neomuttrc
mbox-hook =INBOX   =mbox
mbox-hook =Lists/dev =Lists/dev.old
```

(cmd-charset-hook)=
## `charset-hook`

Define a charset alias — map a mis-labelled charset to one NeoMutt understands.

- `charset-hook <alias> <charset>`

```neomuttrc
charset-hook x-unknown      windows-1252
charset-hook gb2312         gb18030
```

(cmd-iconv-hook)=
## `iconv-hook`

Define a system-specific alias for a character set.

- `iconv-hook <charset> <local-charset>`

```neomuttrc
iconv-hook iso-8859-1 iso-8859-15
```

(cmd-crypt-hook)=
## `crypt-hook`

Specify which cryptographic key ID to use for recipients matching a regex.

- `crypt-hook <regex> <keyid>`

```neomuttrc
crypt-hook alice@example.com 0xDEADBEEF
crypt-hook .                 0x12345678
```

(cmd-index-format-hook)=
## `index-format-hook`

Create a named format string that can be used in `$index_format` and varies
based on message patterns.

- `index-format-hook <name> <pattern> <format-string>` — define a rule
- `index-format-hook <name> !<pattern> <format-string>` — negate the pattern (else clause)

```neomuttrc
index-format-hook date "~d<1d" "%[%H:%M]"
index-format-hook date "~d<1y" "%[%b %d]"
index-format-hook date "~A"    "%[%Y-%m]"
```

(cmd-startup-hook)=
## `startup-hook`

Run a command once when NeoMutt starts up, after all config files are read.

- `startup-hook <command>`

```neomuttrc
startup-hook 'echo "Welcome back!"'
startup-hook 'source ~/.config/neomutt/runtime.rc'
```

(cmd-shutdown-hook)=
## `shutdown-hook`

Run a command just before NeoMutt exits.

- `shutdown-hook <command>`

```neomuttrc
shutdown-hook 'echo "Goodbye!"'
```

(cmd-timeout-hook)=
## `timeout-hook`

Run a command when NeoMutt is idle and the `$timeout` timer expires.

- `timeout-hook <command>`

```neomuttrc
timeout-hook 'exec check-stats'
```

(cmd-unhook)=
## `unhook`

Remove all hooks of a given type, or remove all hooks.

- `unhook *` — remove all hooks
- `unhook <hook-type>` — remove all hooks of that type

```neomuttrc
unhook *
unhook send-hook
unhook folder-hook
```

(cmd-hooks)=
## `hooks`

Display a list of all currently defined hooks.

```neomuttrc
hooks
```

