---
title: Configuration Variables
description: XXX
keywords: XXX
---

# Configuration Variables

Commands for setting, unsetting, and resetting config options and environment variables.

## `set`

Set the value of a config variable.

- `set <variable> = <value>` — assign a value
- `set <variable>` — set a boolean to true
- `set no<variable>` — set a boolean to false
- `set inv<variable>` — toggle a boolean
- `set <variable> += <value>` — append to a string, or add to a number
- `set <variable> -= <value>` — remove from a string, or subtract from a number
- `set <variable>?` — display the current value

```neomuttrc
set sort = reverse-date
set editor = "vim +/^$ ++1"
set real_name = "Jane Doe"
set folder = "imaps://mail.example.com/INBOX"
set beep_new
set nomarkers
set invhelp
set index_format += " %g"
set sort?
```

## `unset`

Reset a config option to false (booleans) or empty (strings).

- `unset <variable>` — clear a single variable
- `unset <var1> <var2>` — clear multiple variables

```neomuttrc
unset imap_pass
unset imap_authenticators smtp_authenticators
```

## `reset`

Reset a config option to its initial (default) value.

- `reset <variable>` — reset one variable
- `reset <var1> <var2>` — reset multiple variables

```neomuttrc
reset sort
reset index_format status_format
```

## `toggle`

Toggle the value of a boolean or quad-option variable.

- `toggle <variable>` — flip the value

```neomuttrc
toggle sidebar_visible
toggle help
```

## `setenv`

Set or query an environment variable.

- `setenv <variable>=<value>` — set a value
- `setenv <variable>?` — display the current value

```neomuttrc
setenv EDITOR=vim
setenv MAIL_DIR=/home/user/Mail
setenv EDITOR?
```

## `unsetenv`

Remove an environment variable.

- `unsetenv <variable>` — unset the variable

```neomuttrc
unsetenv MAIL_DIR
```

