---
title: History Options
description: Configuration variables for command-line history size, persistence, formatting, and duplicate removal.
keywords: neomutt, history, history_file, history_format, history_remove_dups, save_history, command history, input history, recall, buffer
---

(ref-cfg-history)=
# History Options

(cfg-history)=
## `$history`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set history = 10
    ```

This variable controls the size (in number of strings remembered) of the string history buffer per category.
The buffer is cleared each time the variable is set.

Note that strings (e.g. commands) starting with a space are never recorded in the history.
This is for example useful to prevent leaking sensitive information into the history file or for one off tests.

Also note that a string is not added to the history if it exactly matches its immediate predecessor, e.g. executing the same command twice in a row results in only one copy being added to the history.
To prevent duplicates over all entries use [`$history_remove_dups`](cfg-history-remove-dups).

--------------------------------------------------------------------------------

(cfg-history-file)=
## `$history_file`

:Type: [Path (String)](type-path)
:Notes: [File only](type-path)
:Default:
    ```neomuttrc
    set history_file = "~/.mutthistory"
    ```

The file in which NeoMutt will save its history.

Also see [`$save_history`](cfg-save-history).

--------------------------------------------------------------------------------

(cfg-history-format)=
## `$history_format`

:Type: [Expando](type-expando)
:Notes: [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set history_format = "%s"
    ```
:Alternative:
    ```neomuttrc
    set history_format = "%{match}"
    ```

Specify the format of the data displayed in the [`History Dialog`](tour-history).

**Format Sequences**

| Short  | Long Name           | Description                                                     |
|--------|---------------------|-----------------------------------------------------------------|
| `%C`   | `%{number}`         | Line number                                                     |
| `%s`   | `%{match}`          | History match                                                   |
| `%*X`  | `%{padding-soft:X}` | Soft-fill with character `X` as pad                             |
| `%>X`  | `%{padding-hard:X}` | Right justify the rest of the string and pad with character `X` |
| `%\|X` | `%{padding-eol:X}`  | Pad to the end of the line with character `X`                   |

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-history-remove-dups)=
## `$history_remove_dups`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set history_remove_dups = no
    ```

When _set_, all of the string history will be scanned for duplicates when a new entry is added.
Duplicate entries in the [`$history_file`](cfg-history-file) will also be removed when it is periodically compacted.

--------------------------------------------------------------------------------

(cfg-save-history)=
## `$save_history`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set save_history = 0
    ```

This variable controls the size of the history (per category) saved in the [`$history_file`](cfg-history-file) file.

Setting this to a value greater than [`$history`](cfg-history) is possible.
However, there will never be more than [`$history`](cfg-history) entries to select from even if more are recorded in the history file.

