---
title: Sort Options
description: NeoMutt configuration variables for controlling message sort order in the index menu.
keywords: neomutt, sort, sort_aux, sort_re, threading, index, configuration
---

# Sort Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

(sort)=
## `$sort`

- **Type:** sort order
- **Default:** `date`

Specifies how to sort messages in the "index" menu.

| Value | Sort by |
|-------|---------|
| `date` | The date the email was sent |
| `date-received` | When the message was delivered locally |
| `from` | The email's From field |
| `label` | The email's label |
| `score` | The email's score |
| `size` | The size of the email |
| `spam` | The email's spam score |
| `subject` | The email's subject |
| `threads` | Email threads |
| `to` | The email's To field |
| `unsorted` | The order the messages appear in the mailbox |

| Deprecated Value | Use this instead |
|------------------|-----------------|
| `date-sent` | `date` |
| `mailbox-order` | `unsorted` |

You may optionally use the "reverse-" prefix to specify reverse sorting order, or the "last-" prefix to sort threads based on the corresponding attribute of the last descendant rather than the thread root. If both prefixes are in use, "reverse-" must come before "last-". The "last-" prefix has no effect on a flat view.

Any ties in the primary sort are broken by [`$sort_aux`](#sort-aux). When [`$use_threads`](../options) is "threads" or "reverse", `$sort` controls the sorting between threads, and [`$sort_aux`](#sort-aux) controls the sorting within a thread.

The values of "threads" and "reverse-threads" are legacy options, which cause the value of `$sort_aux` to also control sorting between threads, and they may not be used with the "last-" prefix. The preferred way to enable a threaded view is via `$use_threads`. This variable can also be set via the `<sort-mailbox>` and `<sort-reverse>` functions.

:::{note}
When `$use_threads` is "threads", the last thread sorts to the bottom; when it is "reversed", the last thread sorts to the top. The use of "reverse-" in `$sort` swaps which end the last thread will sort to.
:::

See the "Use Threads Feature" section for further explanation and examples: <https://neomutt.org/feature/use-threads>

(sort-aux)=
## `$sort_aux`

- **Type:** sort order
- **Default:** `date`

This provides a secondary sort for messages in the "index" menu, used when the `$sort` value is equal for two messages.

When sorting by threads, this variable controls how subthreads are sorted within a single thread (for the order between threads, see `$sort`). This can be set to any value that `$sort` can, including with the use of "reverse-" and "last-" prefixes, except for variations using "threads" (in that case, NeoMutt will just use "date"). For instance,

```neomuttrc
set sort_aux=last-date-received
```

would mean that if a new message is received in a thread, that subthread becomes the last one displayed (or the first, if you have "`set use_threads=reverse`".) When using `$use_threads`, it is more common to use "last-" with `$sort` and not with `$sort_aux`.

See the "Use Threads Feature" section for further explanation and examples: <https://neomutt.org/feature/use-threads>

(sort-re)=
## `$sort_re`

- **Type:** boolean
- **Default:** `yes`

This variable is only useful when sorting by threads with `$strict_threads` *unset*. In that case, it changes the heuristic NeoMutt uses to thread messages by subject. With `$sort_re` *set*, NeoMutt will only attach a message as the child of another message by subject if the subject of the child message starts with a substring matching the setting of `$reply_regex`. With `$sort_re` *unset*, NeoMutt will attach the message whether or not this is the case, as long as the non-`$reply_regex` parts of both messages are identical.
