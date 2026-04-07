---
title: Config File Syntax
description: Syntax rules for NeoMutt configuration files, including comments, quoting, backtick substitution, and variable expansion.
keywords: neomutt, config, syntax, neomuttrc, quoting, backticks, variable expansion, line continuation, comments, character set, config_charset, rc file
---

(ref-cfg-syntax)=
# Config File Syntax

An initialization file consists of a series of [commands](../commands/index.md).
Each line of the file may contain one or more commands.
When multiple commands are used, they must be separated by a semicolon (`;`).

```neomuttrc
set real_name='John Smith' ; ignore x-
```

## Comments

The hash mark, or pound sign (`#`), is used as a "comment" character.
You can use it to annotate your initialization file.
All text after the comment character to the end of the line is ignored.

```neomuttrc
my-header X-Disclaimer: Why are you listening to me?   # This is a comment
```

## Quoting

Single quotes (`'`) and double quotes (`"`) can be used to quote strings which contain spaces or other special characters.
The difference between the two types of quotes is similar to that of many popular shell programs, namely that a single quote is used to specify a literal string (one that is not interpreted for shell variables or quoting with a backslash), while double quotes indicate a string for which should be evaluated.
For example, backticks are evaluated inside of double quotes, but *not* for single quotes.

`\` quotes the next character, just like in a shell.
For example, if you want to put quotes `"` inside of a string, you can use `\` to force the next character to be a literal instead of interpreted character.

```neomuttrc
set real_name="John \"anonymous\" Doe"
```

`\\` means to insert a literal `\` into the line.
`\n` and `\r` have their usual C meanings of linefeed and carriage-return, respectively.

## Line Continuation

A `\` at the end of a line can be used to split commands over multiple lines as it "escapes" the line end, provided that the split points don't appear in the middle of command names.
Lines are first concatenated before interpretation so that a multi-line can be commented by commenting out the first line only.

```neomuttrc
set status_format="some very \
long value split \
over several lines"
```

:::{note}
Using `\` at the end of a line *only* removes the newline character.

Any leading whitespace on the following lines will be part of the configuration.
:::

## Backtick Substitution

It is also possible to substitute the output of a Unix command in an initialization file.
This is accomplished by enclosing the command in backticks (`` ` ``).
The output of the Unix command will be substituted before the line is parsed.
Since initialization files are line oriented, only the first line of output from the Unix command will be substituted.

```neomuttrc
my-header X-Operating-System: `uname -a`
```

To avoid the output of backticks being parsed, place them inside double quotes.
This is useful so that special characters in the output (e.g.
`'`, `#`, `$`) are not parsed and interpreted specially by NeoMutt.

```neomuttrc
set imap_pass="`gpg --batch -q --decrypt ~/.neomutt/account.gpg`"
```

## Variable Expansion

Both environment variables and NeoMutt config options can be accessed by prepending `$` to the name of the variable.

```neomuttrc
set record = "+sent_on_$HOSTNAME"
```

This will cause NeoMutt to save outgoing messages to a folder named "sent_on_aurora" if the environment variable `$HOSTNAME` is set to "aurora"

If NeoMutt can't find a matching *config* variable, it will try to find a matching *environment* variable.

NeoMutt expands the variable when it is assigned, not when it is used.
If the value of a variable on the right-hand side of an assignment changes after the assignment, the variable on the left-hand side will not be affected.

## Character Set Handling

All configuration files are expected to be in the current locale as specified by the `$charset` variable which doesn't have a default value since it's determined by NeoMutt at startup.
If a configuration file is not encoded in the same character set the `$config_charset` variable should be used: all lines starting with the next are recoded from `$config_charset` to `$charset`.

This mechanism should be avoided if possible as it has the following implications:

- These variables should be set early in a configuration file with `$charset` preceding `$config_charset` so NeoMutt knows what character set to convert to.
- If `$config_charset` is set, it should be set in each configuration file because the value is global and *not* per configuration file.
- Because NeoMutt first recodes a line before it attempts to parse it, a conversion introducing question marks or other characters as part of errors (unconvertible characters, transliteration) may introduce syntax errors or silently change the meaning of certain tokens (e.g. inserting question marks into regular expressions).
