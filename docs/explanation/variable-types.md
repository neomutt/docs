---
title: Understanding Variable Types
description: How NeoMutt configuration variables work, including types, commands, and user-defined variables
keywords: [variables, set, unset, reset, toggle, boolean, number, string, quadoption, configuration]
diataxis_type: explanation
---

# Understanding Variable Types

:::{admonition} Diátaxis: Explanation
:class: note

Write as **discursive discussion**. Explain WHY things are the way they are. Provide context,
background, and history. Connect concepts together. Use "about" framing. It's OK to include
opinion and perspective. Don't include step-by-step instructions — link to tutorials and
how-to guides instead. The reader should come away with deeper understanding.
:::

## Variable Types

NeoMutt supports these types of configuration variables:

boolean
: A boolean expression, either "yes" or "no".

number
: A signed integer number in the range -32768 to 32767.

number (long)
: A signed integer number in the range -2147483648 to 2147483647.

string
: Arbitrary text.

path
: A specialized string for representing paths including support for mailbox shortcuts as
  well as tilde ("~") for a user's home directory and more.

quadoption
: Like a boolean but triggers a prompt when set to "ask-yes" or "ask-no" with "yes" and
  "no" preselected respectively.

sort order
: A specialized string allowing only particular words as values depending on the variable.

regular expression
: A regular expression.

folder type
: Specifies the type of folder to use: *mbox*, *mmdf*, *mh* or *maildir*. Currently only
  used to determine the type for newly created folders.

e-mail address
: An email address either with or without real_name. The older
  `user@example.org (Joe User)` form is supported but strongly deprecated.

user-defined
: Arbitrary text, see [User-Defined Variables](#user-defined-variables) for details.

## Commands

The following commands are available to manipulate and query variables:

```neomuttrc
set [no|inv|&]variable [?]
set variable=value
set variable+=increment
set variable-=decrement
unset variable [variable ...]
reset variable [variable ...]
toggle variable [variable ...]
set variable ?
```neomuttrc

This command is used to set (and unset) configuration variables. There are several basic
types of variables: boolean, number, string, string list and quadoption. *boolean* variables
can be *set* (true) or *unset* (false). *number* variables can be assigned a positive
integer value. The value of numeric variables can be incremented `+=` and decremented `-=`.
*String list* variables use `+=` for appending to the string list and `-=` for removal from
the string list. *string* variables consist of any number of printable characters and must
be enclosed in quotes if they contain spaces or tabs. You may also use the escape sequences
"\\n" and "\\t" for newline and tab, respectively. Content of a *string* variable can be
extended using `+=`. *quadoption* variables are used to control whether or not to be
prompted for certain actions, or to specify a default action. A value of *yes* will cause
the action to be carried out automatically as if you had answered yes to the question.
Similarly, a value of *no* will cause the action to be carried out as if you had answered
"no." A value of *ask-yes* will cause a prompt with a default answer of "yes" and *ask-no*
will provide a default answer of "no."

Prefixing a variable with "no" will unset it. Example: `set noask_bcc`.

For *boolean* variables, you may optionally prefix the variable name with `inv` to toggle
the value (on or off). This is useful when writing macros. Example: `set invsmart_wrap`.

The `toggle` command automatically prepends the `inv` prefix to all specified variables.

The `unset` command automatically prepends the `no` prefix to all specified variables.

Using the `<enter-command>` function in the *index* menu, you can query the value of a
variable by suffixing the name of the variable with a question mark:

```neomuttrc
set allow_8bit?
```neomuttrc

The old prefix query syntax (`set ?allow_8bit`) is also still supported.

The question mark is actually only required for boolean and quadoption variables.

The `reset` command resets all given variables to the compile time defaults (hopefully
mentioned in this manual). If you use the command `set` and prefix the variable with "&"
this has the same behavior as the `reset` command.

With the `reset` command there exists the special variable "all", which allows you to reset
all variables to their system defaults.

(user-defined-variables)=
## User-Defined Variables

### Introduction

Along with the variables listed in the Configuration variables section, NeoMutt supports
user-defined variables with names starting with `my_` as in, for example, `my_cfgdir`.

The `set` command either creates a custom `my_` variable or changes its value if it exists
already. Use of `+=` will adjust a custom variable using the same behavior as a string
variable, by appending additional characters (this is true even if the current contents of
the variable resemble an integer, which is different than the behavior of `+=` on built-in
numeric variables). The `unset` and `reset` commands remove the variable entirely.

Since user-defined variables are expanded in the same way that environment variables are
(except for the shell-escape command and backtick expansion), this feature can be used to
make configuration files more readable.

### Examples

The following example defines and uses the variable `my_cfgdir` to abbreviate the calls of
the `source` command:

```neomuttrc
set my_cfgdir = $HOME/neomutt/config
source $my_cfgdir/hooks $my_cfgdir/macros
# more source commands...
```neomuttrc

A custom variable can also be used in macros to backup the current value of another
variable. In the following example, the value of the `$delete` is changed temporarily while
its original value is saved as `my_delete`. After the macro has executed all commands, the
original value of `$delete` is restored.

```neomuttrc
macro pager ,x '\
<enter-command>set my_delete=$delete<enter>\
<enter-command>set delete=yes<enter>\
...\
<enter-command>set delete=$my_delete<enter>'
```neomuttrc

Since NeoMutt expands such values already when parsing the configuration file(s), the value
of `$my_delete` in the last example would be the value of `$delete` exactly as it was at
that point during parsing the configuration file. If another statement would change the
value for `$delete` later in the same or another file, it would have no effect on
`$my_delete`. However, the expansion can be deferred to runtime, as shown in the next
example, when escaping the dollar sign.

```neomuttrc
macro pager <PageDown> "\
<enter-command> set my_old_pager_stop=\$pager_stop pager_stop<Enter>\
<next-page>\
<enter-command> set pager_stop=\$my_old_pager_stop<Enter>\
<enter-command> unset my_old_pager_stop<Enter>"
```neomuttrc

Note that there is a space between `<enter-command>` and the `set` configuration command,
preventing NeoMutt from recording the `macro`'s commands into its history.

## Type Conversions

Variables are always assigned string values which NeoMutt parses into its internal
representation according to the type of the variable, for example an integer number for
numeric types. For all queries (including $-expansion) the value is converted from its
internal type back into string. As a result, any variable can be assigned any value given
that its content is valid for the target. This also counts for custom variables which are of
type string. In case of parsing errors, NeoMutt will print error messages. The example
below demonstrates type conversions.

```neomuttrc
set my_lines = "5"                # value is string "5"
set pager_index_lines = $my_lines # value is integer 5
set my_sort = "date-received"     # value is string "date-received"
set sort = "last-$my_sort"        # value is sort last-date-received
set my_inc = $read_inc            # value is string "10" (default of $read_inc)
set my_foo = $my_inc              # value is string "10"
```neomuttrc

These assignments are all valid. If, however, the value of `$my_lines` would have been
"five" (or something else that cannot be parsed into a number), the assignment to
`$pager_index_lines` would have produced an error message.

Type conversion applies to all configuration commands which take arguments. But please note
that every expanded value of a variable is considered just a single token. A working example
is:

```neomuttrc
set my_pattern = "~A"
set my_number = "10"
# same as: score ~A +10
score $my_pattern +$my_number
```neomuttrc

What does *not* work is:

```neomuttrc
set my_mx = "+mailbox1 +mailbox2"
mailboxes $my_mx +mailbox3
```

because the value of `$my_mx` is interpreted as a single mailbox named "+mailbox1
+mailbox2" and not two distinct mailboxes.
