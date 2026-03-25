---
title: Use Threads
description: Configure flat, threaded, or reverse-threaded message views independently from sort order in NeoMutt
keywords: threads, threading, use_threads, sort, sort_aux, sort-mailbox, sort-reverse, flat view, reverse threads, thread tree, conversation view, message ordering, status_format
since: 2021-08-01
---

# Use Threads

**Since:** NeoMutt 2021-08-01

## Introduction

The "Use Threads" feature adds a new config option to allow more precise
control of how threads are displayed in the index. Whether threads are in use
is now orthogonal from how messages are sorted.

## Functions

The "Use Threads" feature adds no new functions to NeoMutt. The existing
functions `<sort-mailbox>` and `<sort-reverse>` are updated to toggle the
state of `$use_threads` once it has been set, while preserving
backwards-compatible behavior on `$sort` if this feature is not used.

## Variables

The "Use Threads" feature adds one new config option,
{ref}`$use_threads <use-threads>`, which is an enumeration of possible thread
views. The variable defaults to unset for the original behavior of overloading
{ref}`$sort=threads <sort>` to enable sorting. It can be set to `flat` (or
`no`) for an unthreaded view based on `$sort`, to `threads` (or `yes`) for a
threaded view where roots appear above children, or to `reverse` for a threaded
view where children appear above roots.

When sorting by threads, the value of {ref}`$sort <sort>` determines which
thread floats to the top. If `$sort` does not contain `reverse-`, the latest
thread goes to the bottom for `use_threads=threads` and to the top for
`use_threads=reverse`; the direction of float is swapped if `$sort` also uses
`reverse-`. If `$sort` includes `last-`, the overall thread is sorted by its
descendant at any depth which would sort last in a flat view; otherwise, the
overall thread is sorted solely by the thread root. The `last-` prefix is
ignored when `use_threads=flat`.

Within a single thread, the value of `$sort_aux` determines
how siblings are sorted. The same prefixes apply as for `$sort`, although it is
less common to use the `last-` prefix.

The "Use Threads" feature also modifies the existing config option
`$status_format`, adding the `%T` expando which shows the
current threading method.

## Use Threads Variable

| Name          | Type | Default |
|---------------|------|---------|
| `use_threads` | enum | `unset` |

## neomuttrc

```neomuttrc
# Example NeoMutt config file for the use-threads feature.

# ------------------------------------------------------------
# Default configuration: flat view sorted by date
# selecting threads with <sort-mailbox> changes $sort
#set use_threads=unset sort=date sort_aux=date
# Modern configuration: explicit flat view sorted by date
# selecting threads with <sort-mailbox> changes $use_threads
set use_threads=no sort=date sort_aux=date
#   Anne     12:01  cover letter for thread 1
#   Anne     12:02  part 1 of thread 1
#   Anne     12:03  part 2 of thread 1
#   Anne     12:04  part 3 of thread 1
#   Barbara  12:05  thread 2
#   Claire   12:06  thread 3
#   Diane    12:07  re: part 2 of thread 1
#   Erica    12:08  re: thread 2

# ------------------------------------------------------------
# Legacy configuration: sorting threads by date started
#set sort=threads sort_aux=date
# Modern configuration for the same
# Latest root message sorts last
set use_threads=yes sort=date sort_aux=date
#   Anne     12:01  cover letter for thread 1
#   Anne     12:02  |->part 1 of thread 1
#   Anne     12:03  |->part 2 of thread 1
#   Diane    12:07  | `->re: part 2 of thread 1
#   Anne     12:04  `->part 3 of thread 1
#   Barbara  12:05  thread 2
#   Erica    12:08  `->re: thread 2
#   Claire   12:06  thread 3

# ------------------------------------------------------------
# Legacy configuration: display threads upside-down
#set sort=reverse-threads sort_aux=date
# Modern configuration for the same
# Latest root message sorts first
set use_threads=reverse sort=date sort_aux=date
#   Claire   12:06  thread 3
#   Erica    12:08  ,->re: thread 2
#   Barbara  12:05  thread 2
#   Anne     12:04  ,->part 3 of thread 1
#   Diane    12:07  | ,->re: part 2 of thread 1
#   Anne     12:03  |->part 2 of thread 1
#   Anne     12:02  |->part 1 of thread 1
#   Anne     12:01  cover letter for thread 1

# ------------------------------------------------------------
# Legacy configuration: recently active thread/subthread first
#set sort=threads sort_aux=reverse-last-date
# Modern configuration for the same
# Note that subthreads are also rearranged
set use_threads=threads sort=reverse-last-date sort_aux=reverse-last-date
#   Barbara  12:05  thread 2
#   Erica    12:08  `->re: thread 2
#   Anne     12:01  cover letter for thread 1
#   Anne     12:03  |->part 2 of thread 1
#   Diane    12:07  | `->re: part 2 of thread 1
#   Anne     12:04  |->part 3 of thread 1
#   Anne     12:02  `->part 1 of thread 1
#   Claire   12:06  thread 3

# ------------------------------------------------------------
# Modern configuration: threads keep date order, recently active thread last
# (not possible with legacy configuration)
set use_threads=threads sort=last-date sort_aux=date
#   Claire   12:06  thread 3
#   Anne     12:01  cover letter for thread 1
#   Anne     12:02  |->part 1 of thread 1
#   Anne     12:03  |->part 2 of thread 1
#   Diane    12:07  | `->re: part 2 of thread 1
#   Anne     12:04  `->part 3 of thread 1
#   Barbara  12:05  thread 2
#   Erica    12:08  `->re: thread 2

# vim: filetype=neomuttrc
```

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Flat vs threaded vs reverse threading modes

**Description:** Three NeoMutt index views of the same mailbox: (1) `use_threads=no` showing flat chronological order, (2) `use_threads=yes` showing threaded view with tree characters and roots above children, (3) `use_threads=reverse` showing inverted threads with children above roots.

**Highlights:** The difference in message ordering and the tree-drawing characters (`|->`, `` `-> ``, `,->`) — particularly how the same messages appear in completely different positions depending on the threading mode.
:::

## Known Bugs

Even though `use_threads` accepts the values `yes` and `no`, it does not behave
like a boolean or quad-option variable. A bare `set use_threads` performs a
query rather than setting it to `yes`, and the variable is not usable with
`toggle`.

## Credits

Eric Blake
