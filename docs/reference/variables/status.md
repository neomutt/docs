---
title: Status Variables
description: NeoMutt configuration variables for the status bar display and formatting.
keywords: neomutt, status, status_chars, status_format, status_on_top, configuration
---

# Status Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

## `$status_chars`

- **Type:** character string
- **Default:** `"-*%A"`

Controls the characters used by the "%r" indicator in [`$status_format`](#status_format).

| Character | Default | Description |
|-----------|---------|-------------|
| 1 | `-` | Mailbox is unchanged |
| 2 | `*` | Mailbox has been changed and needs to be resynchronized |
| 3 | `%` | Mailbox is read-only, or will not be written when exiting. (You can toggle whether to write changes to a mailbox with the `<toggle-write>` operation, bound by default to "%") |
| 4 | `A` | Folder opened in attach-message mode. (Certain operations like composing a new mail, replying, forwarding, etc. are not permitted in this mode) |

## `$status_format`

- **Type:** string
- **Default:** `"-%r-NeoMutt: %D [Msgs:%<M?%M/>%m%<n? New:%n>%<o? Old:%o>%<d? Del:%d>%<F? Flag:%F>%<t? Tag:%t>%<p? Post:%p>%<b? Inc:%b>%<l? %l>]---(%<T?%T/>%s/%S)-%>-(%P)---"`

Controls the format of the status line displayed in the "index" menu. This string is similar to `$index_format`, but has its own set of `printf(3)`-like sequences:

| Short | Long Name | Description |
|-------|-----------|-------------|
| `%b` | `%{unread-mailboxes}` | Number of mailboxes with new mail |
| `%D` | `%{description}` | Description of the mailbox |
| `%d` | `%{deleted-count}` | Number of deleted messages |
| `%f` | `%{flagged-count}` | Full pathname of the current mailbox |
| `%F` | `%{mailbox-path}` | Number of flagged messages |
| `%h` | `%{hostname}` | Local hostname |
| `%l` | `%{limit-size}` | Size (in bytes) of the current mailbox (see formatstrings-size) |
| `%L` | `%{mailbox-size}` | Size (in bytes) of the messages shown (i.e., which match the current limit) (see formatstrings-size) |
| `%m` | `%{limit-count}` | Number of messages in the mailbox |
| `%M` | `%{message-count}` | Number of messages shown (i.e., which match the current limit) |
| `%n` | `%{new-count}` | Number of new messages in the mailbox (unread, unseen) |
| `%o` | `%{old-count}` | Number of old messages in the mailbox (unread, seen) |
| `%P` | `%{percentage}` | Percentage of the way through the index |
| `%p` | `%{postponed-count}` | Number of postponed messages |
| `%r` | `%{read-count}` | Modified/read-only/won't-write/attach-message indicator, according to [`$status_chars`](#status_chars) |
| `%R` | `%{readonly}` | Number of read messages in the mailbox (read, seen) |
| `%S` | `%{sort-aux}` | Current aux sorting method (`$sort_aux`) |
| `%s` | `%{sort}` | Current sorting mode (`$sort`) |
| `%T` | `%{use-threads}` | Current threading mode (`$use_threads`) |
| `%t` | `%{tagged-count}` | Number of tagged messages in the mailbox |
| `%u` | `%{unread-count}` | Number of unread messages in the mailbox (seen or unseen) |
| `%v` | `%{limit-pattern}` | NeoMutt version string |
| `%V` | `%{version}` | Currently active limit pattern, if any |
| `%*X` | `%{padding-soft}` | Soft-fill with character `X` as pad |
| `%>X` | `%{padding-hard}` | Right justify the rest of the string and pad with character `X` |
| `%\|X` | `%{padding-eol}` | Pad to the end of the line with character `X` |

For an explanation of "soft-fill", see the `$index_format` documentation.

\* = can be optionally printed if nonzero

Some of the above sequences can be used to optionally print a string if their value is nonzero. For example, you may only want to see the number of flagged messages if such messages exist, since zero is not particularly meaningful. To optionally print a string based upon one of the above sequences, the following construct is used:

`%<sequence_char?optional_string>`

where *sequence_char* is a character from the table above, and *optional_string* is the string you would like printed if *sequence_char* is nonzero. *optional_string* **may** contain other sequences as well as normal text.

Here is an example illustrating how to optionally print the number of new messages in a mailbox:

`%<n?%n new messages>`

You can also switch between two strings using the following construct:

`%<sequence_char?if_string&else_string>`

If the value of *sequence_char* is non-zero, *if_string* will be expanded, otherwise *else_string* will be expanded.

As another example, here is how to show either `$sort` and `$sort_aux` or `$use_threads` and `$sort`, based on whether threads are enabled with `$use_threads`:

`%<T?%s/%S&%T/%s>`

You can force the result of any `printf(3)`-like sequence to be lowercase by prefixing the sequence character with an underscore ("\_") sign. For example, if you want to display the local hostname in lowercase, you would use: "`%_h`".

If you prefix the sequence character with a colon (":") character, NeoMutt will replace any dots in the expansion by underscores. This might be helpful with IMAP folders that don't like dots in folder names.

## `$status_on_top`

- **Type:** boolean
- **Default:** `no`

Setting this variable causes the "status bar" to be displayed on the first line of the screen rather than near the bottom. If `$help` is *set* too, it'll be placed at the bottom.
