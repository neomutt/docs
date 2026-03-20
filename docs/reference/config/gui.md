---
title: GUI Options
description: Reference for NeoMutt gui configuration variables
keywords: neomutt, configuration, variables, gui, settings
---

# GUI Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::



----------------------------------------------------------------------------------------------------------

(beep)=
## `$beep`

- **Type:** boolean
- **Default:** yes

When this variable is _set_, NeoMutt will beep when an error occurs.

----------------------------------------------------------------------------------------------------------

(collapse-flagged)=
## `$collapse_flagged`

- **Type:** boolean
- **Default:** yes

When _unset_, NeoMutt will not collapse a thread if it contains any flagged messages.

----------------------------------------------------------------------------------------------------------

(collapse-unread)=
## `$collapse_unread`

- **Type:** boolean
- **Default:** yes

When _unset_, NeoMutt will not collapse a thread if it contains any unread messages.

----------------------------------------------------------------------------------------------------------

(duplicate-threads)=
## `$duplicate_threads`

- **Type:** boolean
- **Default:** yes

This variable controls whether NeoMutt, when $$sort is set to _threads_, threads messages with the same Message-Id together.
If it is _set_, it will indicate that it thinks they are duplicates of each other with an equals sign in the thread tree.

----------------------------------------------------------------------------------------------------------

(hide-limited)=
## `$hide_limited`

- **Type:** boolean
- **Default:** no

When _set_, NeoMutt will not show the presence of messages that are hidden by limiting, in the thread tree.

----------------------------------------------------------------------------------------------------------

(hide-missing)=
## `$hide_missing`

- **Type:** boolean
- **Default:** yes

When _set_, NeoMutt will not show the presence of missing messages in the thread tree.

----------------------------------------------------------------------------------------------------------

(hide-thread-subject)=
## `$hide_thread_subject`

- **Type:** boolean
- **Default:** yes

When _set_, NeoMutt will not show the subject of messages in the thread tree that have the same subject as their parent or closest previously displayed sibling.

----------------------------------------------------------------------------------------------------------

(hide-top-limited)=
## `$hide_top_limited`

- **Type:** boolean
- **Default:** no

When _set_, NeoMutt will not show the presence of messages that are hidden by limiting, at the top of threads in the thread tree.
Note that when $$hide_limited is _set_, this option will have no effect.

----------------------------------------------------------------------------------------------------------

(hide-top-missing)=
## `$hide_top_missing`

- **Type:** boolean
- **Default:** yes

When _set_, NeoMutt will not show the presence of missing messages at the top of threads in the thread tree.
Note that when $$hide_missing is _set_, this option will have no effect.

----------------------------------------------------------------------------------------------------------

(narrow-tree)=
## `$narrow_tree`

- **Type:** boolean
- **Default:** no

This variable, when _set_, makes the thread tree narrower, allowing deeper threads to fit on the screen.

----------------------------------------------------------------------------------------------------------

(sort-re)=
## `$sort_re`

- **Type:** boolean
- **Default:** `yes`

This variable is only useful when sorting by threads with $$strict_threads _unset_.
In that case, it changes the heuristic neomutt uses to thread messages by subject.
With $$sort_re _set_, neomutt will only attach a message as the child of another message by subject if the subject of the child message starts with a substring matching the setting of $$reply_regex.
With $$sort_re _unset_, neomutt will attach the message whether or not this is the case, as long as the non-$$reply_regex parts of both messages are identical.

----------------------------------------------------------------------------------------------------------

(strict-threads)=
## `$strict_threads`

- **Type:** boolean
- **Default:** no

If _set_, threading will only make use of the "In-Reply-To" and "References:" fields when you $$sort by message threads.
By default, messages with the same subject are grouped together in "pseudo threads.".
This may not always be desirable, such as in a personal mailbox where you might have several unrelated messages with the subjects like "hi" which will get grouped together.
See also $$sort_re for a less drastic way of controlling this behavior.

----------------------------------------------------------------------------------------------------------

(thread-received)=
## `$thread_received`

- **Type:** boolean
- **Default:** no

If $$strict_threads is _unset_, then messages may also be grouped by subject.
Unlike threading by "In-Reply-To:" and "References:" header, grouping by subject does not imply a parent-child relation between two messages.

To determine the ancestry between messages grouped by subject, NeoMutt uses their date: only newer messages can be descendants of older ones.

When $$thread_received is _set_, NeoMutt uses the date received rather than the date sent when comparing messages for the date.

See also $$strict_threads, and $$sort_re.

