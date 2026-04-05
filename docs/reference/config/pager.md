---
title: Pager Options
description: Configuration variables for the built-in pager display, wrapping, filtering, search context, and quoting.
keywords: pager, display_filter, pager_context, pager_index_lines, pager_stop, smart_wrap, markers, allow_ansi, smileys, tilde, message viewer, reading
---

(ref-cfg-pager)=
# Pager Options

(cfg-allow-ansi)=
## `$allow_ansi`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set allow_ansi = no
    ```

Controls whether ANSI color codes in messages (and color tags in rich text messages) are to be interpreted.
Messages containing these codes are rare, but if this option is _set_, their text will be colored accordingly.
Note that this may override your color choices, and even present a security problem, since a message could include a line like:

```
[-- PGP output follows ...
```

and give it the same color as your attachment color (see also [`$crypt_timestamp`](cfg-crypt-timestamp)).

--------------------------------------------------------------------------------

(cfg-display-filter)=
## `$display_filter`

:Type: [Command (String)](type-string)
:Default: (empty)
    ```neomuttrc
    set display_filter = ""
    ```

When set, specifies a command used to filter messages.
When a message is viewed it is passed as standard input to [`$display_filter`](cfg-display-filter), and the filtered message is read from the standard output.

When preparing the message, NeoMutt inserts some escape sequences into the text.
They are of the form: `<esc>]9;XXX<bel>` where "XXX" is a random 64-bit number.

If these escape sequences interfere with your filter, they can be removed using a tool like `ansifilter` or `sed 's/^\x1b]9;[0-9]\+\x7//'`

If they are removed, then PGP and MIME headers will no longer be coloured.
This can be fixed by adding this to your config:
`color body magenta default '^\[-- .* --\]$'`.

--------------------------------------------------------------------------------

(cfg-header-color-partial)=
## `$header_color_partial`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set header_color_partial = no
    ```

When _set_, color header regexes behave like color body regexes:
color is applied to the exact text matched by the regex.
When _unset_, color is applied to the entire header.

One use of this option might be to apply color to just the header labels.

See [`color`](cmd-color) for more details.

--------------------------------------------------------------------------------

(cfg-markers)=
## `$markers`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set markers = yes
    ```

Controls the display of wrapped lines in the internal pager.
If set, a "+" marker is displayed at the beginning of wrapped lines.

Also see the [`$smart_wrap`](cfg-smart-wrap) variable.

--------------------------------------------------------------------------------

(cfg-pager)=
## `$pager`

:Type: [Command (String)](type-string)
:Default: (empty)
    ```neomuttrc
    set pager = ""
    ```

This variable specifies which pager you would like to use to view messages.
When empty, NeoMutt will use the built-in pager, otherwise this variable should specify the pathname of the external pager you would like to use.

Using an external pager may have some disadvantages: Additional keystrokes are necessary because you can't call NeoMutt functions directly from the pager, and screen resizes cause lines longer than the screen width to be badly formatted in the help menu.

--------------------------------------------------------------------------------

(cfg-pager-context)=
## `$pager_context`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set pager_context = 0
    ```

This variable controls the number of lines of context that are given when displaying the next or previous page in the internal pager.
By default, NeoMutt will display the line after the last one on the screen at the top of the next page (0 lines of context).

This variable also specifies the amount of context given for search results.
If positive, this many lines will be given before a match, if 0, the match will be top-aligned.

--------------------------------------------------------------------------------

(cfg-pager-format)=
## `$pager_format`

:Type: [Expando](type-expando)
:Default:
    ```neomuttrc
    set pager_format = "-%Z- %C/%m: %-20.20n   %s%*  -- (%P)"
    ```
:Alternative:
    ```neomuttrc
    set pager_format = "-%{combined-flags}- %{number}/%{message-count}: %-20.20{name}   %{subject}%{padding-soft: } -- (%{percentage})"
    ```

Specify the format of the data displayed in the [`Pager Dialog`](tour-pager)'s status bar.

:::{seealso}
- [`$index_format`](cfg-index-format) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-pager-index-lines)=
## `$pager_index_lines`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set pager_index_lines = 0
    ```

Determines the number of lines of a mini-index which is shown when in the pager.
The current message, unless near the top or bottom of the folder, will be roughly one third of the way down this mini-index, giving the reader the context of a few messages before and after the message.
This is useful, for example, to determine how many messages remain to be read in the current thread.
A value of 0 results in no index being shown.

--------------------------------------------------------------------------------

(cfg-pager-read-delay)=
## `$pager_read_delay`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set pager_read_delay = 0
    ```

Determines the number of seconds that must elapse after first opening a new message in the pager before that message will be marked as read.
A value of 0 results in the message being marked read unconditionally; for other values, navigating to another message or exiting the pager before the timeout will leave the message marked unread.
This setting is ignored if [`$pager`](cfg-pager) is set.

--------------------------------------------------------------------------------

(cfg-pager-skip-quoted-context)=
## `$pager_skip_quoted_context`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set pager_skip_quoted_context = 0
    ```

Determines the number of lines of context to show before the unquoted text when using the [`<skip-quoted>`](ref-fn-pager) function.
When set to a positive number at most that many lines of the previous quote are displayed.
If the previous quote is shorter the whole quote is displayed.

--------------------------------------------------------------------------------

(cfg-pager-stop)=
## `$pager_stop`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set pager_stop = no
    ```

When _set_, the internal-pager will **not** move to the next message when you are at the end of a message and invoke the [`<next-page>`](ref-fn-generic)
function.

--------------------------------------------------------------------------------

(cfg-prompt-after)=
## `$prompt_after`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set prompt_after = yes
    ```

If you use an _external_ [`$pager`](cfg-pager), setting this variable will cause NeoMutt to prompt you for a command when the pager exits rather than returning to the index menu.
If _unset_, NeoMutt will return to the index menu when the external pager exits.

--------------------------------------------------------------------------------

(cfg-search-context)=
## `$search_context`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set search_context = 0
    ```

For the pager, this variable specifies the number of lines shown before search results.
By default, search results will be top-aligned.

--------------------------------------------------------------------------------

(cfg-smart-wrap)=
## `$smart_wrap`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set smart_wrap = yes
    ```

Controls the display of lines longer than the screen width in the internal pager.
If _set_, long lines are wrapped at a word boundary.
If _unset_, lines are simply wrapped at the screen edge.
Also see the [`$markers`](cfg-markers) variable.

--------------------------------------------------------------------------------

(cfg-smileys)=
## `$smileys`

:Type: [Regular Expression](type-regex)
:Notes: [Smart Case](type-general)
:Default:
    ```neomuttrc
    set smileys = "(>From )|(:[-^]?[][)(><}{|/DP])"
    ```

The _pager_ uses this variable to catch some common false positives of [`$quote_regex`](cfg-quote-regex), most notably smileys and not consider a line quoted text if it also matches [`$smileys`](cfg-smileys).
This mostly happens at the beginning of a line.

--------------------------------------------------------------------------------

(cfg-tilde)=
## `$tilde`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set tilde = no
    ```

When _set_, the internal-pager will pad blank lines to the bottom of the screen with a tilde ("~").

--------------------------------------------------------------------------------

(cfg-toggle-quoted-show-levels)=
## `$toggle_quoted_show_levels`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set toggle_quoted_show_levels = 0
    ```

Quoted text may be filtered out using the [`<toggle-quoted>`](ref-fn-pager) command.
If set to a number greater than 0, then the [`<toggle-quoted>`](ref-fn-pager) command will only filter out quote levels above this number.

