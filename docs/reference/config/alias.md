---
title: Alias Options
description: Config options for managing email aliases, address queries, and alias display formatting.
keywords: alias, address book, contacts, alias_file, alias_format, alias_sort, query_command, query_format, nicknames, address lookup
---

(ref-cfg-alias)=
# Alias Options

(cfg-alias-file)=
## `$alias_file`

:Description: Save new aliases to this file
:Type: [Path (String)](type-path)
:Notes: [File only](type-path)
:Default:
    ```neomuttrc
    set alias_file = "~/.neomuttrc"
    ```

The default file in which to save aliases created by [`<create-alias>`](menu-alias).
Entries added to this file are encoded in the character set specified by [`$config_charset`](cfg-config-charset) if it is _set_ or the current character set otherwise.

The default for this option is the currently used neomuttrc file, or `~/.neomuttrc` if no user neomuttrc was found.

:::{note}
NeoMutt will not automatically source this file; you must explicitly use [`:source`](cmd-source) for it to be executed in case this option points to a dedicated alias file.
:::

--------------------------------------------------------------------------------

(cfg-alias-format)=
## `$alias_format`

:Description: Format string for the [Alias Dialog](tour-alias)
:Type: [Expando](type-expando)
:Notes: [Not Empty](type-general), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set alias_format = "%3i %f%t %-15a %-56A | %C%> %Y"
    ```
:Alternative:
    ```neomuttrc
    set alias_format = "%3{number} %{flags}%{tagged} %-15{alias} %-56{address} | %{comment}%{padding-hard: }%{tags}"
    ```

Specify the format of the data displayed in the [`Alias Dialog`](tour-alias).

**Format Sequences**

| Short  | Long Name           | Description                                                     |
|--------|---------------------|-----------------------------------------------------------------|
| `%A`   | `%{address}`        | Full Address (Name and Email)                                   |
| `%a`   | `%{alias}`          | Alias name                                                      |
| `%C`   | `%{comment}`        | Comment                                                         |
| `%E`   | `%{email}`          | Email Address                                                   |
| `%f`   | `%{flags}`          | Flags - currently, a `d` for an alias marked for deletion       |
| `%i`   | `%{number}`         | Index number                                                    |
| `%N`   | `%{name}`           | Real name                                                       |
| `%t`   | `%{tagged}`         | Alias is tagged (selected)                                      |
| `%Y`   | `%{tags}`           | User-defined tags (labels)                                      |
| `%*X`  | `%{padding-soft:X}` | Soft-fill with character `X` as padding                         |
| `%>X`  | `%{padding-hard:X}` | Right justify the rest of the string and pad with character `X` |
| `%\|X` | `%{padding-eol:X}`  | Pad to the end of the line with character `X`                   |

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

The following sequences are deprecated; they will be removed in the future.

| Deprecated | Action           |
|------------|------------------|
| `%c`       | Use `%C` instead |
| `%n`       | Use `%i` instead |
| `%r`       | Use `%A` instead |

--------------------------------------------------------------------------------

(cfg-alias-sort)=
## `$alias_sort`

:Description: Sort method for the [Alias Dialog](tour-alias)
:Type: [Sort Order](type-sort-order)
:Notes: [Reverse](type-sort-order)
:Default:
    ```neomuttrc
    set alias_sort = alias
    ```

Specifies how the entries in the [Alias](tour-alias) and [Query](tour-query) Dialogs are sorted.

| Value      | Sort by                               |
|------------|---------------------------------------|
| `alias`    | Alias short name                      |
| `email`    | Email Address                         |
| `name`     | Real Name                             |
| `unsorted` | The order the Aliases were configured |

| Deprecated Value | Use this instead |
|------------------|------------------|
| `address`        | `email`          |

:::{note}
If _set_, this overrides the order of entries returned by the [`$query_command`](cfg-query-command).
:::

--------------------------------------------------------------------------------

(cfg-query-command)=
## `$query_command`

:Description: External command to query an external address book
:Type: [Command (String)](type-string)
:Default: (empty)
    ```neomuttrc
    set query_command = ""
    ```

This specifies the command NeoMutt will use to make external address queries.
The string may contain a `%s`, which will be substituted with the query string the user types.
NeoMutt will add quotes around the string substituted for `%s` automatically according to shell quoting rules, so you should avoid adding your own.
If no `%s` is found in the string, NeoMutt will append the user's query to the end of the string.

:::{seealso}
[External Address Queries](how-address-query)
:::

--------------------------------------------------------------------------------

(cfg-query-format)=
## `$query_format`

:Description: Format string for the [Query Dialog](tour-query) (address book)
:Type: [Expando](type-expando)
:Notes: [Not Empty](type-general), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set query_format = "%3i %t %-25N %-25E | %C%> %Y"
    ```
:Alternative:
    ```neomuttrc
    set query_format = "%3{number} %{tagged} %-25{name} %-25{email} | %{comment}%{padding-hard: }%{tags}"
    ```

Specify the format of the data displayed in the [`Query Dialog`](tour-query).

**Format Sequences**

| Short  | Long Name           | Description                                                     |
|--------|---------------------|-----------------------------------------------------------------|
| `%A`   | `%{address}`        | Full Address (Name and Email)                                   |
| `%C`   | `%{comment}`        | Comment                                                         |
| `%E`   | `%{email}`          | Email Address                                                   |
| `%i`   | `%{number}`         | Index number                                                    |
| `%N`   | `%{name}`           | Real name                                                       |
| `%t`   | `%{tagged}`         | Alias is tagged (selected)                                      |
| `%Y`   | `%{tags}`           | User-defined tags (labels)                                      |
| `%*X`  | `%{padding-soft:X}` | Soft-fill with character `X` as padding                         |
| `%>X`  | `%{padding-hard:X}` | Right justify the rest of the string and pad with character `X` |
| `%\|X` | `%{padding-eol:X}`  | Pad to the end of the line with character `X`                   |

The following sequences are deprecated; they will be removed in the future.

| Deprecated | Action           |
|------------|------------------|
| `%a`       | Use `%E` instead |
| `%c`       | Use `%i` instead |
| `%e`       | Use `%C` instead |
| `%n`       | Use `%N` instead |

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

