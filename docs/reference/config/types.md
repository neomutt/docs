---
title: Config Types
description: Reference for all NeoMutt configuration variable types, including boolean, number, string, path, regex, and sort order.
keywords: neomutt, config types, boolean, number, string, path, regex, quad, expando, sort order, enumeration, mbtable, slist, myvar, data types
---

(ref-cfg-types)=
# Config Types

NeoMutt configuration options are settings that control how the program behaves, and each one has a defined type that determines what kind of value it can accept.
For example, some options are simple on/off switches, some expect numbers, and others require text or file paths.
Because NeoMutt knows the expected type of each option, it can check your input when you set it and warn you if something isn't valid.
This helps catch mistakes early - like entering text where a number is needed or using an unsupported value - so your configuration works as intended and is easier to troubleshoot.

(type-general)=
## General Flags

These flags can be applied to different config option types.  
They can restrict the possible values or change the option's behaviour.

:Case Sensitive:
    The case of the string matters.

:Case Insensitive:
    The case of the string does not matter.

:Charset Single:
    Only one character encoding is allowed.  
    You can't provide a list of alternatives; you must pick exactly one.

:Charset Strict:
    NeoMutt will be extra strict when checking the encoding name, rejecting anything that isn't a well-known, valid character set.

:Localised String:
    The default value of this setting can be translated into your language, so it may appear differently depending on your locale.

:Not Empty:
    The setting must have a value - you're not allowed to leave it blank.  
    NeoMutt will reject an empty string.

:Not Negative:
    The number must be zero or positive.  
    Negative values are not accepted.

:On Startup:
    This setting can only be changed when NeoMutt first starts up.  
    Once it's running, the value is locked and can't be modified.

:Sensitive:
    The value contains something private, like a password.  
    NeoMutt takes care not to display or log it.

:Smart Case:
    Case-sensitive, if the string contains any upper-case letters.  
    Case-insensitive, if the string is entirely lowercase.

(type-address)=
## Address

- Address - An email address, like `user@example.com`.  
  NeoMutt checks that it's properly formatted.

```neomuttrc
# Example address
set from = "John Smith <js@example.com>"
```

(type-bool)=
## Boolean

- Boolean - A simple on/off switch.  
  Boolean types do not need to be quoted.

Allowed values:

| Enabled | Disabled |
|---------|----------|
| `yes`   | `no`     |
| `y`     | `n`      |
| `on`    | `off`    |
| `true`  | `false`  |
| `1`     | `0`      |

```neomuttrc
# Example boolean
set sidebar_visible = yes
```

(type-enum)=
## Enumeration

- Enum - A choice from a fixed list of named options.  
  Think of it like a dropdown menu - you pick one of the allowed values and nothing else.  
  Enum types do not need to be quoted.

The values for an enumeration depend on the config option.

```neomuttrc
# Example enumeration
set mbox_type = maildir
```

(type-expando)=
## Expando String

- Expando - A formatting template that uses special placeholders (like `%s` or `%d`) which NeoMutt fills in with real information.  
  For example, the subject line or sender's name can be plugged into a display format.

The expandos available depend on the config option.

```neomuttrc
set alias_format = "%3i %f%t %-15a %-56A | %C%> %Y"
```

(type-long)=
## Long Number

- Long - A large number.  
  It works just like a regular number but can hold much bigger values for settings that need them.

```neomuttrc
# Example long
set pgp_timeout = 86400 # 1 day
```

(type-mbtable)=
## Multi-Byte Character String

- MBTable - A table of characters used to customise the display.

The number of characters in the string depends on the config option.

```neomuttrc
# Example mbtable
set flag_chars = "*!DdrONon- "
```

(type-myvar)=
## MyVar Custom String

- MyVar - A user-defined variable (always starting with `my_`).  
  You can create your own named values to store information and reuse it elsewhere in your configuration.

```neomuttrc
# Example myvar
set my_name = "Rich"
```

(type-number)=
## Number

- Number - A whole number.
  NeoMutt makes sure the value falls within an allowed range, so you can't accidentally set something impossibly high or low.

```neomuttrc
# Example number
set wrap = 80
```

(type-pipe)=
## Pipe Support

Some config options allow their value to end with a `|` (pipe) character.
When NeoMutt sees a trailing pipe, it treats the value as a shell command: it runs the command and uses its output in place of the literal value.

There are two mechanisms, depending on the option type:

- **Path options** — If a [Path](type-path) value ends with `|`, the path (minus the pipe) is executed as a shell command and the output is read as if it were a file.

- **Expando options** — If an [Expando](type-expando) value ends with `|` after expansion, the entire rendered string (minus the pipe) is executed as a shell command and the first line of output replaces the string.

```neomuttrc
# Path example: generate a signature dynamically
set signature = "~/.mutt/gen-sig.sh|"

# Expando example: use an external command for the status bar
set status_format = "my-status-command %m messages|"
```

:::{seealso}
[Pipe Command Tutorial](tut-pipe-command)
:::

(type-path)=
## Path String

- Path - A location of a file or folder on your computer, like `/home/you/Mail`.  
  NeoMutt will automatically expand shortcuts such as `~` (your home directory).

**Modifiers**

- **Dir** - The path must point to a folder (directory), not a file.
- **File** - The path must point to a file, not a folder.

```neomuttrc
# Example path
set signature = "~/.signature"
```

(type-quad)=
## Quadoption

- Quad - A four-way choice, for enabling features.  
  Before using a feature NeoMutt will check the value.  
  Quad types do not need to be quoted.

Allowed values:

| Value     | Meaning                  |
|-----------|--------------------------|
| `yes`     | Enabled, don't ask       |
| `no`      | Disabled, don't ask      |
| `ask-yes` | Ask, defaulting to 'yes' |
| `ask-no`  | Ask, defaulting to 'no'  |

```neomuttrc
# Example quad
set quit = ask-yes
```

(type-regex)=
## Regular Expression

- Regex - A search pattern used to match text.  
  For example, you can tell NeoMutt to highlight messages whose subject line contains certain words.

**Modifiers**

- **Match Case** - The search pattern pays attention to upper and lower case.  
  By default patterns ignore case, but this flag makes A and a different.
- **Allow Not** - The pattern is allowed to start with !, which means "match everything that does not fit this pattern."
- **No Sub** - NeoMutt only cares whether the pattern matched or not - it doesn't bother remembering which part of the text matched.  
  This is a behind-the-scenes performance detail.

```neomuttrc
# Example regex
set quote_regex = "^([ \t]*[|>:}#])+"
```

(type-slist)=
## String list

- String List - A list of text values separated by commas, spaces or colons.  
  This lets you specify multiple items - for example, a list of preferred character encodings - in a single setting.  
  The separator character depends on the config option.

**Modifiers**

- **Separator:** Space / Comma / Colon - Controls what character separates items in the list.  

- **Allow Dupes** - The same value is allowed to appear more than once in the list.  
  Without this flag, duplicates are silently removed.

- **Allow Empty** - The list is allowed to have no items at all.  
  Without this flag, at least one entry is required.

- **Case Sensitive** - When checking for duplicates or looking up values, ABC and abc are treated as different.  
  Without this flag they'd be considered the same.

```neomuttrc
# Example slist
set hidden_tags = "unread,draft,flagged,passed,replied,attachment,signed,encrypted"
```

(type-sort-order)=
## Sort Order

- Sort - A sorting method that controls the order things appear in, such as sorting messages by date, subject, or sender.  
  Sort options do not need to be quoted.

The values for a sort depend on the config option.

**Modifiers**

- **Last** - Allows the sort method to be prefixed with `last-`, which changes it to sort by the most recent item in a thread rather than the first.
- **Reverse** - Allows the sort method to be prefixed with `reverse-`, which flips the order (e.g. newest-first instead of oldest-first).

```neomuttrc
# Example sort
set sort = reverse-date
```

(type-string)=
## String

- String - A free-form piece of text.
  This is the most flexible type - you can type whatever value the setting calls for.

**Modifiers**

- **Mailbox** - The string represents a mailbox name.  
  NeoMutt treats it specially and won't expand it as a file path.
- **Command** - The string is a shell command that NeoMutt will run for you, rather than just a piece of text.

```neomuttrc
# Example string
set arrow_string = "->"
```

