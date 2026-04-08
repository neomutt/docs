---
title: Hooks
description: Execute commands automatically based on mailbox, message, or event triggers using folder-hook, send-hook, and other hooks
keywords: hooks, folder-hook, send-hook, reply-hook, send2-hook, message-hook, crypt-hook, account-hook, timeout-hook, startup-hook, shutdown-hook, new-mail-hook, index-format-hook, unhook, setenv, pattern matching, event triggers, automation
---

# Hooks

A *hook* is a concept found in many other programs which allows you to execute arbitrary commands before performing some operation.
For example, you may wish to tailor your configuration based upon which mailbox you are reading, or to whom you are sending mail.
In the NeoMutt world, a *hook* consists of a regular expression or pattern along with a configuration option/command.

NeoMutt supports the following hooks:

- `account-hook`
- `charset-hook` / `iconv-hook`
- `index-format-hook`
- `crypt-hook`
- `fcc-save-hook` / `fcc-hook` / `save-hook`
- `folder-hook`
- `mbox-hook`
- `message-hook`
- `open-hook` / `close-hook` / `append-hook`
- `reply-hook` / `send-hook` / `send2-hook`
- `timeout-hook` / `startup-hook` / `shutdown-hook`
- `unhook`

To show a list of all the current hooks, run the `hooks` command.

:::{note}
If a hook changes configuration settings, these changes remain effective until the end of the current NeoMutt session.
As this is generally not desired, a "default" hook needs to be added before all other hooks of that type to restore configuration defaults.
:::

## Example: Specifying a Default Hook

```neomuttrc
send-hook . 'unmy-header From:'
send-hook ~C'^b@b\.b$' my-header from: c@c.c
```

In this example, by default the value of [`$from`](cfg-from) and [`$real_name`](cfg-real-name) is not overridden.
When sending messages either To: or Cc: to `<b@b.b>`, the From: header is changed to `<c@c.c>`.

## Message Matching in Hooks

Hooks that act upon messages (`message-hook`, `reply-hook`, `send-hook`, `send2-hook`, `save-hook`, `fcc-hook`, `index-format-hook`) are evaluated in a slightly different manner.
For the other types of hooks, a regular expression is sufficient.
But in dealing with messages a finer grain of control is needed for matching since for different purposes you want to match different criteria.

NeoMutt allows the use of the search pattern language for matching messages in hook commands.
This works in exactly the same way as it would when *limiting* or *searching* the mailbox, except that you are restricted to those operators which match information NeoMutt extracts from the header of the message (i.e., from, to, cc, date, subject, etc.).

For example, if you wanted to set your return address based upon sending mail to a specific address, you could do something like:

```neomuttrc
send-hook '~t ^user@work\.com$' 'my-header From: John Smith <user@host>'
```

However, it is not required that you write the pattern to match using the full searching language.
You can still specify a simple *regular expression* like the other hooks, in which case NeoMutt will translate your pattern into the full language, using the translation specified by the [`$default_hook`](cfg-default-hook) variable.

The default value of [`$default_hook`](cfg-default-hook) is `~f %s | (~b %s & ~A) | (~B %s)`, which means the regex is matched against: the **From** address, OR (**body** AND all messages), OR the **Subject**. 
You can change [`$default_hook`](cfg-default-hook) to alter this implicit expansion behaviour.

## Mailbox Matching in Hooks

Hooks that match against mailboxes (`folder-hook`, `mbox-hook`) apply both regular expression syntax as well as mailbox shortcut expansion on the regex parameter.
There is some overlap between these, so special attention should be paid to the first character of the regex.

```neomuttrc
# Here, ^ will expand to "the current mailbox" not "beginning of string":
folder-hook "^/home/user/Mail/bar" "set sort=threads"
# If you want ^ to be interpreted as "beginning of string", one workaround
# is to enclose the regex in parenthesis:
folder-hook "(^/home/user/Mail/bar)" "set sort=threads"
# This will expand to the default save folder for the alias "imap.example.com", which
# is probably not what you want:
folder-hook "@imap\.example\.com" "set sort=threads"
# A workaround is to use parenthesis or a backslash:
folder-hook "(@imap\.example\.com)" "set sort=threads"
folder-hook '\@imap\.example\.com' "set sort=threads"
```

Keep in mind that mailbox shortcut expansion on the regex parameter takes place when the hook is initially parsed, not when the hook is matching against a mailbox.
When NeoMutt starts up and is reading the .neomuttrc, some mailbox shortcuts may not be usable.

---

## folder-hook — Setting Variables Based Upon Mailbox

### Syntax

```neomuttrc
folder-hook [-noregex] regex command
```

It is often desirable to change settings based on which mailbox you are reading.
The `folder-hook` command provides a method by which you can execute any configuration command.
The *command* is executed before loading any mailboxes matching *regex*.
The `-noregex` switch controls whether *regex* is matched using a simple string comparison or a full regex match.
If a mailbox matches multiple `folder-hook`s, they are executed in the order given in the `.neomuttrc`.

The regex parameter has mailbox shortcut expansion performed on the first character.

:::{note}
If you use the `!` shortcut for [`$spool_file`](cfg-spool-file) at the beginning of *regex*, you must place it inside of double or single quotes in order to distinguish it from the logical *not* operator for the expression.
:::

:::{note}
Settings are *not* restored when you leave the mailbox.
For example, a common action to perform is to change the sorting method based upon the mailbox being read:

```neomuttrc
folder-hook work "set sort=threads"
```

However, the sorting method is not restored to its previous value when reading a different mailbox.
To specify a *default* command, use the regex `.` before other `folder-hook`s adjusting a value on a per-folder basis because `folder-hook`s are evaluated in the order given in the configuration file.
:::

:::{note}
The keyboard buffer will not be processed until after all hooks are run; multiple `push` or `exec` commands will end up being processed in reverse order.
:::

### Example: Setting Sort Method Based on Mailbox Name

```neomuttrc
folder-hook . "set sort=date-sent"
folder-hook work "set sort=threads"
```

This will set the `sort` variable to `date-sent` for all folders but to `threads` for all folders containing "work" in their name.

---

## send-hook / reply-hook / send2-hook — Change Settings Based Upon Message Recipients

### Syntax

```neomuttrc
reply-hook pattern command
send-hook pattern command
send2-hook pattern command
```

These commands can be used to execute arbitrary configuration commands based upon recipients of the message.
*pattern* is used to match the message.
*command* is executed when *pattern* matches.

If the pattern is a plain string, or a regex, it will be expanded to a pattern using [`$default_hook`](cfg-default-hook).

`reply-hook` is matched against the message you are *replying to*, instead of the message you are *sending*.
`send-hook` is matched against all messages, both *new* and *replies*.

:::{note}
`reply-hook`s are matched *before* the `send-hook`, *regardless* of the order specified in the user's configuration file.
However, you can inhibit `send-hook` in the reply case by using the pattern `'! ~Q'` (*not replied*) in the `send-hook` to tell when `reply-hook` have been executed.
:::

`send2-hook` is matched every time a message is changed, either by editing it, or by using the compose menu to change its recipients or subject.
`send2-hook` is executed after `send-hook`, and can, e.g., be used to set parameters such as the [`$sendmail`](cfg-sendmail) variable depending on the message's sender address.

For each type of `send-hook` or `reply-hook`, when multiple matches occur, commands are executed in the order they are specified in the `.neomuttrc` (for that type of hook).

Example: `send-hook work "set mime_forward signature=''"`

Another typical use for this command is to change the values of the [`$attribution_intro`](cfg-attribution-intro), [`$attribution_locale`](cfg-attribution-locale), and [`$signature`](cfg-signature) variables in order to change the language of the attributions and signatures based upon the recipients.

:::{note}
`send-hook`'s are only executed once after getting the initial list of recipients.
They are not executed when resuming a postponed draft.
Adding a recipient after replying or editing the message will not cause any `send-hook` to be executed, similarly if [`$auto_edit`](cfg-auto-edit) is set (as then the initial list of recipients is empty).
Also note that `my-header` commands which modify recipient headers, or the message's subject, don't have any effect on the current message when executed from a `send-hook`.
:::

---

## message-hook — Change Settings Before Formatting a Message

### Syntax

```neomuttrc
message-hook pattern command
```

This command can be used to execute arbitrary configuration commands before viewing or formatting a message based upon information about the message.
*command* is executed if the *pattern* matches the message to be displayed.
When multiple matches occur, commands are executed in the order they are specified in the `.neomuttrc`.

If the pattern is a plain string, or a regex, it will be expanded to a pattern using [`$default_hook`](cfg-default-hook).

Example:

```neomuttrc
message-hook ~A 'set pager=""'
message-hook '~f freshmeat-news' 'set pager="less \"+/^  subject: .*\""'
```

---

## crypt-hook — Choosing the Cryptographic Key of the Recipient

### Syntax

```neomuttrc
crypt-hook regex keyid
```

When encrypting messages with PGP/GnuPG or OpenSSL, you may want to associate a certain key with a given e-mail address automatically, either because the recipient's public key can't be deduced from the destination address, or because, for some reasons, you need to override the key NeoMutt would normally use.
The `crypt-hook` command provides a method by which you can specify the ID of the public key to be used when encrypting messages to a certain recipient.
You may use multiple crypt-hooks with the same regex; multiple matching crypt-hooks result in the use of multiple keyids for a recipient.

During key selection, NeoMutt will confirm whether each crypt-hook is to be used (unless the [`$crypt_confirm_hook`](cfg-crypt-confirm-hook) option is unset).
If all crypt-hooks for a recipient are declined, NeoMutt will use the original recipient address for key selection instead.

The meaning of *keyid* is to be taken broadly in this context: You can either put a numerical key ID or fingerprint here, an e-mail address, or even just a real name.

---

## account-hook — Managing Multiple Accounts

### Syntax

```neomuttrc
account-hook regex command
```

If you happen to have accounts on multiple IMAP, POP and/or SMTP servers, you may find managing all the authentication settings inconvenient and error-prone.
The `account-hook` command may help.
This hook works like `folder-hook` but is invoked whenever NeoMutt needs to access a remote mailbox (including inside the folder browser), not just when you open the mailbox.
This includes (for example) polling for new mail, storing Fcc messages and saving messages to a folder.
As a consequence, `account-hook` should only be used to set connection-related settings such as passwords or tunnel commands but not settings such as sender address or name (because in general it should be considered unpredictable which `account-hook` was last used).

### Examples

```neomuttrc
account-hook . 'unset imap_user; unset imap_pass; unset tunnel'
account-hook imap://host1/ 'set imap_user=me1 imap_pass=foo'
account-hook imap://host2/ 'set tunnel="ssh host2 /usr/libexec/imapd"'
account-hook smtp://user@host3/ 'set tunnel="ssh host3 /usr/libexec/smtpd"'
```

To manage multiple accounts with, for example, different values of [`$record`](cfg-record) or sender addresses, `folder-hook` has to be used together with the `mailboxes` command.

### Managing Multiple Accounts (Full Example)

```neomuttrc
mailboxes imap://user@host1/INBOX
folder-hook imap://user@host1/ 'set folder=imap://host1/ ; set record=+INBOX/Sent'
mailboxes imap://user@host2/INBOX
folder-hook imap://user@host2/ 'set folder=imap://host2/ ; set record=+INBOX/Sent'
```

In this example the folders are defined using `mailboxes` so NeoMutt polls them for new mail.
Each `folder-hook` triggers when one mailbox below each IMAP account is opened and sets [`$folder`](cfg-folder) to the account's root folder.
Next, it sets [`$record`](cfg-record) to the *INBOX/Sent* folder below the newly set [`$folder`](cfg-folder).
Please notice that the value the `+` mailbox shortcut refers to depends on the *current* value of [`$folder`](cfg-folder) and therefore has to be set separately per account.
Setting other values like [`$from`](cfg-from) or [`$signature`](cfg-signature) is analogous to setting [`$record`](cfg-record).

---

## Global Hooks — timeout-hook, startup-hook, shutdown-hook

These hooks are called when global events take place in NeoMutt.

- **timeout-hook** — run a command periodically (every [`$timeout`](cfg-timeout) seconds)
- **startup-hook** — run a command when NeoMutt starts up, before opening the first mailbox
- **shutdown-hook** — run a command when NeoMutt shuts down, before closing the last mailbox

### Syntax

```neomuttrc
timeout-hook command
startup-hook command
shutdown-hook command
```

The commands are NeoMutt commands.
If you want to run an external shell command, you need to run them like this:

```neomuttrc
startup-hook 'echo `action.sh ARGS`'
```

The single quotes prevent the backticks from being expanded.
The `echo` command prevents an empty command error.

### Example Configuration

```neomuttrc
# After $timeout seconds of inactivity, run this NeoMutt command
timeout-hook 'exec sync-mailbox'
# When NeoMutt first loads, run this NeoMutt command
startup-hook 'exec sync-mailbox'
# When NeoMutt quits, run this NeoMutt command
shutdown-hook 'exec sync-mailbox'
```

---

## new-mail-hook — Execute a Command on New Mail

### Introduction

This feature enables the `new_mail_command` setting, which can be used to execute a custom script (e.g. a notification handler) upon receiving a new mail.

The command string can contain expandos, such as `%n` for the number of new messages.
For a complete list, see: [`$status_format`](cfg-status-format).

:::{note}
When the notification is sent, the folder of the new mail is no longer known.
This is a limitation of NeoMutt.
The `%f` expando will show the open folder.

When using Maildir local mailboxes, you must set [`$check_new`](cfg-check-new) config option for this feature to work.
:::

### Linux Example

```neomuttrc
set new_mail_command="notify-send --icon='/home/santiago/Pictures/neomutt.png' \
  'New Email' '%n new messages, %u unread.' &"
```

### macOS Example

Install a command line interface for Notification Center, for example [terminal-notifier](https://github.com/julienXX/terminal-notifier):

```neomuttrc
set new_mail_command="terminal-notifier -title '%v' -subtitle 'New Mail' \
  -message '%n new messages, %u unread.' -activate 'com.apple.Terminal'"
```

### Variables

| Name               | Type   | Default |
|--------------------|--------|---------|
| `new_mail_command` | string | (empty) |

---

## Index Format Hook

### Syntax

```neomuttrc
index-format-hook name [!]pattern format-string
```

`index-format-hook` injects format strings dynamically into [`$index_format`](cfg-index-format) based on pattern matching against the current message.
The `name` argument is referenced inside [`$index_format`](cfg-index-format) as the expando `%@name@`.

Multiple hooks sharing the same `name` are tested in the order they are defined; the first matching *pattern* wins.
If the pattern is a plain string or regex it is expanded via [`$default_hook`](cfg-default-hook).
Best practice is to end the list with a catch-all `~A` pattern so the expando always resolves to something.

### Example: Dynamic date formatting

```neomuttrc
set index_format="%4C %-6@date@ %-15.15F %Z (%4c) %s"

index-format-hook  date  "~d<1d"    "%[%H:%M]"
index-format-hook  date  "~d<1m"    "%[%a %d]"
index-format-hook  date  "~d<1y"    "%[%b %d]"
index-format-hook  date  "~A"       "%[%m/%y]"
```

The `~d<1d` pattern matches messages less than one day old, `~d<1m` less than one month, etc.
The final `~A` (match all) acts as a fallback.

### Example: Flagging messages by sender

```neomuttrc
set index_format="%4C %@subj_flags@%s"

index-format-hook  subj_flags  "~f boss@example.com"    "** BOSS ** "
index-format-hook  subj_flags  "~f spouse@example.com"  ":-) "
```

Without a catch-all `~A` hook, unmatched messages simply produce an empty string for that expando.

---

## Removing Hooks

### Syntax

```neomuttrc
unhook {* | hook-type}
```

This command permits you to flush hooks you have previously defined.
You can either remove all hooks by giving the `*` character as an argument, or you can remove all hooks of a specific type by saying something like `unhook send-hook`.

---

## Managing Environment Variables (setenv)

NeoMutt lets you control the environment it passes to child processes using the `setenv` and `unsetenv` commands.
This is useful for setting variables like `BROWSER`, `EDITOR`, `MAILCAPS`, or any other environment variable that affects helper programs NeoMutt launches.

### Syntax

```neomuttrc
setenv NAME=value
unsetenv NAME
setenv NAME?
```

The variable name must start with a letter or underscore and contain only letters, digits, and underscores.

### Examples

```neomuttrc
setenv BROWSER firefox
setenv ORGANIZATION "The NeoMutt Development Team"
setenv EDITOR vim
unsetenv DISPLAY
```

You can also query the current value of an environment variable by appending `?`:

```neomuttrc
setenv TERM?
```

Running `setenv` with no parameters shows a list of all currently set environment variables.

The old whitespace-separated syntax is also supported for backward compatibility:

```neomuttrc
setenv TERM vt100
setenv ORGANIZATION "The NeoMutt Development Team"
```
