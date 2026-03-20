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

--------------------------------------------------------------------------------

(history)=
## `$history`

- **Type:** number
- **Notes:** Not negative
- **Default:**
    ```
    set history = 10
    ```

This variable controls the size (in number of strings remembered) of the string history buffer per category.
The buffer is cleared each time the variable is set.

Note that strings (e.g. commands) starting with a space are never recorded in the history.
This is for example useful to prevent leaking sensitive information into the history file or for one off tests.

Also note that a string is not added to the history if it exactly matches its immediate predecessor, e.g. executing the same command twice in a row results in only one copy being added to the history.
To prevent duplicates over all entries use $$history_remove_dups.

--------------------------------------------------------------------------------

(history-file)=
## `$history_file`

- **Type:** path (string)
- **Notes:** File only
- **Default:**
    ```
    set history_file = "~/.mutthistory"
    ```

The file in which NeoMutt will save its history.

Also see $$save_history.

--------------------------------------------------------------------------------

(history-format)=
## `$history_format`

- **Type:** expando
- **Default:**
    ```
    set history_format = "%s"
    ```

Controls the format of the entries of the history list.
This string is similar to $$index_format, but has its own set of `printf(3)`-like sequences:

| Short  | Long Name           | Description                                                     |
|--------|---------------------|-----------------------------------------------------------------|
| `%C`   | `%{number}`         | Line number                                                     |
| `%s`   | `%{match}`          | History match                                                   |
| `%*X`  | `%{padding-soft:X}` | Soft-fill with character `X` as pad                             |
| `%>X`  | `%{padding-hard:X}` | Right justify the rest of the string and pad with character `X` |
| `%\|X` | `%{padding-eol:X}`  | Pad to the end of the line with character `X`                   |

--------------------------------------------------------------------------------

(history-remove-dups)=
## `$history_remove_dups`

- **Type:** boolean
- **Default:**
    ```
    set history_remove_dups = no
    ```

When _set_, all of the string history will be scanned for duplicates when a new entry is added.
Duplicate entries in the $$history_file will also be removed when it is periodically compacted.

--------------------------------------------------------------------------------

(save-history)=
## `$save_history`

- **Type:** number
- **Notes:** Not negative
- **Default:**
    ```
    set save_history = 0
    ```

This variable controls the size of the history (per category) saved in the $$history_file file.

Setting this to a value greater than $$history is possible.
However, there will never be more than $$history entries to select from even if more are recorded in the history file.

