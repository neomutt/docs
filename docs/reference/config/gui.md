---
title: GUI Options
description: Configuration variables for thread display, collapsing, duplicate detection, and thread tree appearance.
keywords: neomutt, gui, threads, collapse_flagged, collapse_unread, duplicate_threads, hide_limited, hide_missing, narrow_tree, strict_threads, sort_re, thread tree
---

(cfg-gui)=
# GUI Options

(beep)=
## `$beep`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set beep = yes
    ```

When this variable is _set_, NeoMutt will beep when an error occurs.

--------------------------------------------------------------------------------

(collapse-flagged)=
## `$collapse_flagged`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set collapse_flagged = yes
    ```

When _unset_, NeoMutt will not collapse a thread if it contains any flagged messages.

--------------------------------------------------------------------------------

(collapse-unread)=
## `$collapse_unread`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set collapse_unread = yes
    ```

When _unset_, NeoMutt will not collapse a thread if it contains any unread messages.

--------------------------------------------------------------------------------

(duplicate-threads)=
## `$duplicate_threads`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set duplicate_threads = yes
    ```

This variable controls whether NeoMutt, when [`$sort`](sort) is set to _threads_, threads messages with the same Message-Id together.
If it is _set_, it will indicate that it thinks they are duplicates of each other with an equals sign in the thread tree.

--------------------------------------------------------------------------------

(hide-limited)=
## `$hide_limited`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set hide_limited = no
    ```

When _set_, NeoMutt will not show the presence of messages that are hidden by limiting, in the thread tree.

--------------------------------------------------------------------------------

(hide-missing)=
## `$hide_missing`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set hide_missing = yes
    ```

When _set_, NeoMutt will not show the presence of missing messages in the thread tree.

--------------------------------------------------------------------------------

(hide-thread-subject)=
## `$hide_thread_subject`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set hide_thread_subject = yes
    ```

When _set_, NeoMutt will not show the subject of messages in the thread tree that have the same subject as their parent or closest previously displayed sibling.

--------------------------------------------------------------------------------

(hide-top-limited)=
## `$hide_top_limited`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set hide_top_limited = no
    ```

When _set_, NeoMutt will not show the presence of messages that are hidden by limiting, at the top of threads in the thread tree.
Note that when [`$hide_limited`](hide-limited) is _set_, this option will have no effect.

--------------------------------------------------------------------------------

(hide-top-missing)=
## `$hide_top_missing`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set hide_top_missing = yes
    ```

When _set_, NeoMutt will not show the presence of missing messages at the top of threads in the thread tree.
Note that when [`$hide_missing`](hide-missing) is _set_, this option will have no effect.

--------------------------------------------------------------------------------

(narrow-tree)=
## `$narrow_tree`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set narrow_tree = no
    ```

This variable, when _set_, makes the thread tree narrower, allowing deeper threads to fit on the screen.

--------------------------------------------------------------------------------

(sort-re)=
## `$sort_re`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set sort_re = yes
    ```

This variable is only useful when sorting by threads with [`$strict_threads`](strict-threads) _unset_.
In that case, it changes the heuristic neomutt uses to thread messages by subject.
With [`$sort_re`](sort-re) _set_, neomutt will only attach a message as the child of another message by subject if the subject of the child message starts with a substring matching the setting of [`$reply_regex`](reply-regex).
With [`$sort_re`](sort-re) _unset_, neomutt will attach the message whether or not this is the case, as long as the non-[`$reply_regex`](reply-regex) parts of both messages are identical.

--------------------------------------------------------------------------------

(strict-threads)=
## `$strict_threads`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set strict_threads = no
    ```

If _set_, threading will only make use of the "In-Reply-To" and "References:" fields when you [`$sort`](sort) by message threads.
By default, messages with the same subject are grouped together in "pseudo threads.".
This may not always be desirable, such as in a personal mailbox where you might have several unrelated messages with the subjects like "hi" which will get grouped together.
:::{seealso}
[`$sort_re`](sort-re) for a less drastic way of controlling this behavior
:::

--------------------------------------------------------------------------------

(thread-received)=
## `$thread_received`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set thread_received = no
    ```

If [`$strict_threads`](strict-threads) is _unset_, then messages may also be grouped by subject.
Unlike threading by "In-Reply-To:" and "References:" header, grouping by subject does not imply a parent-child relation between two messages.

To determine the ancestry between messages grouped by subject, NeoMutt uses their date: only newer messages can be descendants of older ones.

When [`$thread_received`](thread-received) is _set_, NeoMutt uses the date received rather than the date sent when comparing messages for the date.

:::{seealso}
[`$strict_threads`](strict-threads), and [`$sort_re`](sort-re)
:::

