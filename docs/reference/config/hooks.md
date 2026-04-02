---
title: Hooks Options
description: Configuration variables for hook pattern defaults, outgoing message saving, and fcc behavior.
keywords: neomutt, hooks, default_hook, save_name, force_name, fcc-hook, send-hook, reply-hook, save-hook, pattern matching, outgoing mail
---

(cfg-hooks)=
# Hooks Options

(cfg-default-hook)=
## `$default_hook`

:Type: [String](type-string)
:Default:
    ```neomuttrc
    set default_hook = "~f %s !~P | (~P ~C %s)"
    ```

This variable controls how some hooks are interpreted if their pattern is a plain string or a regex. i.e. they don't contain a pattern, like `~f`

| Affected Hooks     |
|--------------------|
| [`fcc-hook`](cmd-fcc-hook)          |
| [`fcc-save-hook`](cmd-fcc-save-hook)     |
| [`index-format-hook`](cmd-index-format-hook) |
| [`message-hook`](cmd-message-hook)      |
| [`reply-hook`](cmd-reply-hook)        |
| [`save-hook`](cmd-save-hook)         |
| [`send-hook`](cmd-send-hook)         |
| [`send2-hook`](cmd-send2-hook)        |

The hooks are expanded when they are declared, so a hook will be interpreted according to the value of this variable at the time the hook is declared.

The default value matches if the message is either from a user matching the regular expression given, or if it is from you (if the from address matches [`alternates`](cmd-alternates)) and is to or cc'ed to a user matching the given regular expression.

--------------------------------------------------------------------------------

(cfg-force-name)=
## `$force_name`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set force_name = no
    ```

This variable is similar to [`$save_name`](cfg-save-name), except that NeoMutt will store a copy of your outgoing message by the username of the address you are sending to even if that mailbox does not exist.

Also see the [`$record`](cfg-record) variable.

--------------------------------------------------------------------------------

(cfg-save-name)=
## `$save_name`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set save_name = no
    ```

This variable controls how copies of outgoing messages are saved.
When _set_, a check is made to see if a mailbox specified by the recipient address exists (this is done by searching for a mailbox in the [`$folder`](cfg-folder) directory with the _username_ part of the recipient address).  
If the mailbox exists, the outgoing message will be saved to that mailbox, otherwise the message is saved to the [`$record`](cfg-record) mailbox.

Also see the [`$force_name`](cfg-force-name) variable.

