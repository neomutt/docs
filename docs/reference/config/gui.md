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


gui.md
	  { "beep", DT_BOOL, true, 0, NULL,
	  { "collapse_flagged", DT_BOOL, true, 0, NULL,
	  { "collapse_unread", DT_BOOL, true, 0, NULL,
	  { "duplicate_threads", DT_BOOL, true, 0, NULL,
	  { "hide_limited", DT_BOOL, false, 0, NULL,
	  { "hide_missing", DT_BOOL, true, 0, NULL,
	  { "hide_thread_subject", DT_BOOL, true, 0, NULL,
	  { "hide_top_limited", DT_BOOL, false, 0, NULL,
	  { "hide_top_missing", DT_BOOL, true, 0, NULL,
	  { "narrow_tree", DT_BOOL, false, 0, NULL,
	  { "sort_re", DT_BOOL, true, 0, NULL,
	  { "strict_threads", DT_BOOL, false, 0, NULL,
	  { "thread_received", DT_BOOL, false, 0, NULL,

----------------------------------------------------------------------------------------------------------

(beep)=
## `$beep`

- **Type:** boolean
- **Default:** yes

When this variable is *set*, NeoMutt will beep when an error occurs.

----------------------------------------------------------------------------------------------------------

(collapse-flagged)=
## `$collapse_flagged`

- **Type:** boolean
- **Default:** yes

When *unset*, NeoMutt will not collapse a thread if it contains any
flagged messages.

----------------------------------------------------------------------------------------------------------

(collapse-unread)=
## `$collapse_unread`

- **Type:** boolean
- **Default:** yes

When *unset*, NeoMutt will not collapse a thread if it contains any
unread messages.

----------------------------------------------------------------------------------------------------------

(duplicate-threads)=
## `$duplicate_threads`

- **Type:** boolean
- **Default:** yes

This variable controls whether NeoMutt, when `$sort` is set to *threads*,
threads messages with the same Message-Id together. If it is *set*, it
will indicate that it thinks they are duplicates of each other with an equals
sign in the thread tree.

----------------------------------------------------------------------------------------------------------

(hide-limited)=
## `$hide_limited`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will not show the presence of messages that are
hidden by limiting, in the thread tree.

----------------------------------------------------------------------------------------------------------

(hide-missing)=
## `$hide_missing`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will not show the presence of missing messages in the
thread tree.

----------------------------------------------------------------------------------------------------------

(hide-thread-subject)=
## `$hide_thread_subject`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will not show the subject of messages in the thread
tree that have the same subject as their parent or closest previously
displayed sibling.

----------------------------------------------------------------------------------------------------------

(hide-top-limited)=
## `$hide_top_limited`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will not show the presence of messages that are
hidden by limiting, at the top of threads in the thread tree. Note that when
[$hide_limited](#hide-limited) is *set*, this option will have no effect.

----------------------------------------------------------------------------------------------------------

(hide-top-missing)=
## `$hide_top_missing`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will not show the presence of missing messages at the
top of threads in the thread tree.  Note that when [$hide_missing](#hide-missing) is
*set*, this option will have no effect.

----------------------------------------------------------------------------------------------------------

(narrow-tree)=
## `$narrow_tree`

- **Type:** boolean
- **Default:** no

This variable, when *set*, makes the thread tree narrower, allowing
deeper threads to fit on the screen.

----------------------------------------------------------------------------------------------------------

(sort-re)=
## `$sort_re`

- **Type:** boolean
- **Default:** `yes`

This variable is only useful when sorting by threads with `$strict_threads` *unset*. In that case, it changes the heuristic NeoMutt uses to thread messages by subject. With `$sort_re` *set*, NeoMutt will only attach a message as the child of another message by subject if the subject of the child message starts with a substring matching the setting of `$reply_regex`. With `$sort_re` *unset*, NeoMutt will attach the message whether or not this is the case, as long as the non-`$reply_regex` parts of both messages are identical.

----------------------------------------------------------------------------------------------------------

(strict-threads)=
## `$strict_threads`

- **Type:** boolean
- **Default:** no

If *set*, threading will only make use of the "In-Reply-To" and
"References:" fields when you `$sort` by message threads.  By
default, messages with the same subject are grouped together in
"pseudo threads.". This may not always be desirable, such as in a
personal mailbox where you might have several unrelated messages with
the subjects like "hi" which will get grouped together. See also
[$sort_re](#sort-re) for a less drastic way of controlling this
behavior.

----------------------------------------------------------------------------------------------------------

(thread-received)=
## `$thread_received`

- **Type:** boolean
- **Default:** no

If [$strict_threads](#strict-threads) is *unset*, then messages may also be grouped by
subject.  Unlike threading by "In-Reply-To:" and "References:" header,
grouping by subject does not imply a parent-child relation between two
messages.

To determine the ancestry between messages grouped by subject, NeoMutt uses
their date: only newer messages can be descendants of older ones.

When [$thread_received](#thread-received) is *set*, NeoMutt uses the date received rather
than the date sent when comparing messages for the date.

See also [$strict_threads](#strict-threads), and [$sort_re](#sort-re).

