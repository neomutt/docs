---
title: History Options
description: NeoMutt configuration variables for command history buffer and persistence.
keywords: neomutt, history, history_file, history_format, history_remove_dups, configuration
---

# History Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

(history)=
## `$history`

- **Type:** number
- **Default:** `10`

This variable controls the size (in number of strings remembered) of the string history buffer per category. The buffer is cleared each time the variable is set.

Note that strings (e.g. commands) starting with a space are never recorded in the history. This is for example useful to prevent leaking sensitive information into the history file or for one off tests.

Also note that a string is not added to the history if it exactly matches its immediate predecessor, e.g. executing the same command twice in a row results in only one copy being added to the history. To prevent duplicates over all entries use [`$history_remove_dups`](#history-remove-dups).

(history-file)=
## `$history_file`

- **Type:** path
- **Default:** `"~/.mutthistory"`

The file in which NeoMutt will save its history.

Also see `$save_history`.

(history-format)=
## `$history_format`

- **Type:** string
- **Default:** `"%s"`

Controls the format of the entries of the history list. This string is similar to `$index_format`, but has its own set of `printf(3)`-like sequences:

| Short | Long Name | Description |
|-------|-----------|-------------|
| `%C` | `%{number}` | Line number |
| `%s` | `%{match}` | History match |
| `%*X` | `%{padding-soft}` | Soft-fill with character `X` as pad |
| `%>X` | `%{padding-hard}` | Right justify the rest of the string and pad with character `X` |
| `%\|X` | `%{padding-eol}` | Pad to the end of the line with character `X` |

(history-remove-dups)=
## `$history_remove_dups`

- **Type:** boolean
- **Default:** `no`

When *set*, all of the string history will be scanned for duplicates when a new entry is added. Duplicate entries in the [`$history_file`](#history-file) will also be removed when it is periodically compacted.
