---
title: Pattern Options
description: Configuration variables for search patterns, external search commands, simple search expansion, and thorough search.
keywords: pattern, search, simple_search, thorough_search, external_search_command, pattern_format, limit, filtering, regex, mairix, indexer
---

(cfg-pattern)=
# Pattern Options

(cfg-external-search-command)=
## `$external_search_command`

:Type: [Command (String)](type-string)
:Default: (empty)
    ```neomuttrc
    set external_search_command = ""
    ```

If set, contains the name of the external program used by "~I" patterns.
This will usually be a wrapper script around mairix, mu, or similar indexers other than notmuch (for which there is optional special support).

Here is an example how it works.
Let's assume [`$external_search_command`](cfg-external-search-command) is set to "mairix_filter", and mairix_filter is a script which runs the old but well loved mairix indexer with the arguments given to mairix_filter, in the "raw" mode of mairix, producing on the standard output a list of Message-IDs, one per line.

If possible, it also filters down the results coming from mairix such that only messages in the current folder remain.
It can do this because it gets a hidden first argument which is the path to the folder.
(This can be the type of clean and simple script called a _one-liner_.)

Now if NeoMutt gets a limit or tag command followed by the pattern "~I '-t s:bleeping='", mairix_filter runs mairix with the arguments from inside the quotes (the quotes are needed because of the space after "-t"), mairix finds all messages with "bleeping" in the Subject plus all messages sharing threads with these and outputs their file names, and mairix_filter translates the file names into Message-IDs.
Finally, NeoMutt reads the Message-IDs and targets the matching messages with the command given to it.

You, the user, still have to rewrite the mairix_filter script to match the behavior of your indexer, but this should help users of indexers other than notmuch to integrate them cleanly with NeoMutt.

--------------------------------------------------------------------------------

(cfg-pattern-format)=
## `$pattern_format`

:Type: [Expando](type-expando)
:Default:
    ```neomuttrc
    set pattern_format = "%2n %-15e  %d"
    ```
:Alternative:
    ```neomuttrc
    set pattern_format = "%2{number} %-15{expression}  %{description}"
    ```

This variable describes the format of the "pattern completion" menu.
The following `printf(3)`-style sequences are understood:

| Short  | Long Name           | Description                                                     |
|--------|---------------------|-----------------------------------------------------------------|
| `%d`   | `%{description}`    | Pattern description                                             |
| `%e`   | `%{expression}`     | Pattern expression                                              |
| `%n`   | `%{number}`         | Index number                                                    |
| `%*X`  | `%{padding-soft:X}` | Soft-fill with character `X` as pad                             |
| `%>X`  | `%{padding-hard:X}` | Right justify the rest of the string and pad with character `X` |
| `%\|X` | `%{padding-eol:X}`  | Pad to the end of the line with character `X`                   |

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-simple-search)=
## `$simple_search`

:Type: [String](type-string)
:Default:
    ```neomuttrc
    set simple_search = "~f %s | ~s %s"
    ```

Specifies how NeoMutt should expand a simple search into a real search pattern.
A simple search is one that does not contain any of the "~" pattern operators.
See "$patterns" for more information on search patterns.

simple_search applies to several functions, e.g. [`<delete-pattern>`](fn-index), [`<limit>`](fn-alias), searching in the index, and all of the index colors.

For example, if you simply type "joe" at a search or limit prompt, NeoMutt will automatically expand it to the value specified by this variable by replacing "%s" with the supplied string.
For the default value, "joe" would be expanded to: "~f joe | ~s joe".

--------------------------------------------------------------------------------

(cfg-thorough-search)=
## `$thorough_search`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set thorough_search = yes
    ```

Affects the `~b`, `~B`, and `~h` search operations described in section "$patterns".  
If _set_, the headers and body/attachments of messages to be searched are decoded before searching.
If _unset_, messages are searched as they appear in the folder.

Users searching attachments or for non-ASCII characters should _set_ this value because decoding also includes MIME parsing/decoding and possible character set conversions.
Otherwise NeoMutt will attempt to match against the raw message received (for example quoted-printable encoded or with encoded headers) which may lead to incorrect search results.

