---
title: Writing Your First Configuration
description: Learn where NeoMutt looks for config files and how to write your first neomuttrc
keywords: [neomutt, configuration, neomuttrc, config, tutorial, setup]
diataxis_type: tutorial
---

# Writing Your First Configuration

:::{admonition} Diátaxis: Tutorial
:class: note

Write as a **lesson**. Guide the learner through a meaningful exercise step by step.
Use second person ("you"). Show concrete actions and their expected results.
Don't explain concepts — demonstrate them through doing. Start with the simplest case
and build complexity gradually. The reader should feel a sense of accomplishment at the end.
:::

NeoMutt is highly configurable because it's *meant* to be customized to your needs and
preferences. However, this configurability can make it difficult when just getting started.
A few sample neomuttrc files are available in the
[Contrib Repo](https://github.com/neomutt/neomutt-contrib).

## Location of Initialization Files

When NeoMutt starts up it looks for two configuration files – one "system" file and one "user"
file.

NeoMutt first reads the system configuration file, then the user configuration file. The two
files are merged in the sense that "last setting wins". That is, if a setting is defined in
both files, the user configuration file's value for that setting is the one that takes
precedence and becomes effective.

NeoMutt searches for several different file names when looking for config. It looks for
NeoMutt config files before Mutt config files and versioned config before plain config. For
example:

| Config file name |
|------------------|
| neomuttrc |
| muttrc |

This allows the user to create separate NeoMutt and Mutt config files on the same system.

### Location of System Config Files

NeoMutt will search for a system config file in a `neomutt` directory in several places.
First it searches the locations specified in the `XDG_CONFIG_DIRS` environment variable, which
defaults to `/etc/xdg`. Next, it looks in `/etc`. Finally, it tries `/usr/share`.

The system config file will not be read if the "-n" option is used on the command line.

NeoMutt will read just one file, the first file it finds, from the list below.

| File Location | Notes |
|---------------|-------|
| /etc/xdg/neomutt/neomuttrc | |
| /etc/xdg/neomutt/Muttrc | Note the case of the filename |
| /etc/neomuttrc | |
| /etc/Muttrc | Note the case of the filename |
| /usr/share/neomutt/neomuttrc | |
| /usr/share/neomutt/Muttrc | Note the case of the filename |

### Location of User Config Files

NeoMutt will search for a user config file in several places. First it looks in the directory
specified in the `XDG_CONFIG_HOME` environment variable, which defaults to
`~/.config/neomutt`. Next, it looks in `~` (your home directory). Finally, it tries
`~/.neomutt`.

You may specify your own location for the user config file using the "-F" option on the
command line.

NeoMutt will read just one file, the first file it finds, from the list below.

| File Location |
|---------------|
| ~/.config/neomutt/neomuttrc |
| ~/.config/neomutt/muttrc |
| ~/.config/mutt/neomuttrc |
| ~/.config/mutt/muttrc |
| ~/.neomutt/neomuttrc |
| ~/.neomutt/muttrc |
| ~/.mutt/neomuttrc |
| ~/.mutt/muttrc |
| ~/.neomuttrc |
| ~/.muttrc |

### Config Priority

The majority of NeoMutt's config will be read from two files: the system config in `/etc` and
the user config in, e.g. `~/.neomuttrc`.

The last file that gets read will overwrite any settings from previous config files. This
means that an administrator can set some defaults which the user can override.

Additionally, there are a handful of config items which can be set using an environment
variable. They have a lower priority than the NeoMutt config files: `$editor`, `$from`,
`$mailcap_path`, `$news_server`, `$shell`, `$spool_file`, `$tmp_dir`.

Finally, it's possible to set some variables directly on the command-line using the `-e`
option.

| Priority | Where | Example |
|----------|-------|---------|
| Highest | Command line | `neomutt -e 'set from="John Doe <john@example.com>"'` |
| | User Config | `~/.neomuttrc` |
| | System Config | `/etc/neomuttrc` |
| | Environment | `export EDITOR="/usr/bin/vim"` |
| Lowest | Built-in | Defaults hard-coded into NeoMutt |

## Syntax of Initialization Files

An initialization file consists of a series of commands. Each line of the file may contain one
or more commands. When multiple commands are used, they must be separated by a semicolon
(";").

**Example: Multiple configuration commands per line**

```
set real_name='John Smith' ; ignore x-
```

The hash mark, or pound sign ("#"), is used as a "comment" character. You can use it to
annotate your initialization file. All text after the comment character to the end of the line
is ignored.

**Example: Commenting configuration files**

```
my-header X-Disclaimer: Why are you listening to me?   # This is a comment
```

Single quotes ("'") and double quotes (""") can be used to quote strings which contain spaces
or other special characters. The difference between the two types of quotes is similar to that
of many popular shell programs, namely that a single quote is used to specify a literal string
(one that is not interpreted for shell variables or quoting with a backslash [see next
paragraph]), while double quotes indicate a string for which should be evaluated. For example,
backticks are evaluated inside of double quotes, but *not* for single quotes.

"\\" quotes the next character, just like in a shell. For example, if want to put quotes """
inside of a string, you can use "\\" to force the next character to be a literal instead of
interpreted character.

**Example: Escaping quotes in configuration files**

```
set real_name="John \"anonymous\" Doe"
```

"\\\\" means to insert a literal "\\" into the line. "\\n" and "\\r" have their usual
C meanings of linefeed and carriage-return, respectively.

A "\\" at the end of a line can be used to split commands over multiple lines as it "escapes"
the line end, provided that the split points don't appear in the middle of command names.
Lines are first concatenated before interpretation so that a multi-line can be commented by
commenting out the first line only.

**Example: Splitting long configuration commands over several lines**

```
set status_format="some very \
long value split \
over several lines"
```

:::{note}
Using "\\" at the end of a line *only* removes the newline character.

Any leading whitespace on the following lines will be part of the configuration.
:::

It is also possible to substitute the output of a Unix command in an initialization file.
This is accomplished by enclosing the command in backticks (\`\`). The output of the Unix
command will be substituted before the line is parsed. Since initialization files are line
oriented, only the first line of output from the Unix command will be substituted.

**Example: Using external command's output in configuration files**

```
my-header X-Operating-System: `uname -a`
```

To avoid the output of backticks being parsed, place them inside double quotes. For example,
the output of the gpg decryption is assigned directly to $imap_pass, so that special
characters in the password (e.g. "'", "#", "$") are not parsed and interpreted specially by
neomutt.

**Example: Preventing the output of backticks from being parsed**

```
set imap_pass="`gpg --batch -q --decrypt ~/.neomutt/account.gpg`"
```

Both environment variables and NeoMutt variables can be accessed by prepending "$" to the name
of the variable. For example,

**Example: Using environment variables in configuration files**

```
set record = "+sent_on_$HOSTNAME"
```

will cause NeoMutt to save outgoing messages to a folder named "sent\_on\_kremvax" if the
environment variable `$HOSTNAME` is set to "kremvax." (See `$record` for details.)

If NeoMutt can't find a matching *config* variable, it will try to find a matching
*environment* variable.

NeoMutt expands the variable when it is assigned, not when it is used. If the value of
a variable on the right-hand side of an assignment changes after the assignment, the variable
on the left-hand side will not be affected.

The commands understood by NeoMutt are explained in the next paragraphs. For a complete list,
see the command reference.

All configuration files are expected to be in the current locale as specified by the
`$charset` variable which doesn't have a default value since it's determined by NeoMutt at
startup. If a configuration file is not encoded in the same character set the
`$config_charset` variable should be used: all lines starting with the next are recoded from
`$config_charset` to `$charset`.

This mechanism should be avoided if possible as it has the following implications:

- These variables should be set early in a configuration file with `$charset` preceding
  `$config_charset` so NeoMutt knows what character set to convert to.
- If `$config_charset` is set, it should be set in each configuration file because the value
  is global and *not* per configuration file.
- Because NeoMutt first recodes a line before it attempts to parse it, a conversion
  introducing question marks or other characters as part of errors (unconvertible characters,
  transliteration) may introduce syntax errors or silently change the meaning of certain
  tokens (e.g. inserting question marks into regular expressions).
