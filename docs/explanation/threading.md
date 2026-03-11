---
title: Understanding Threading
description: How NeoMutt organizes messages into threads and the available thread-related functions
keywords: [threading, threads, tree, sort, collapse, subthread, index]
diataxis_type: explanation
---

# Understanding Threading

:::{admonition} Diátaxis: Explanation
:class: note

Write as **discursive discussion**. Explain WHY things are the way they are. Provide context,
background, and history. Connect concepts together. Use "about" framing. It's OK to include
opinion and perspective. Don't include step-by-step instructions — link to tutorials and
how-to guides instead. The reader should come away with deeper understanding.
:::

## Threaded Mode

So-called "threads" provide a hierarchy of messages where replies are linked to their
parent message(s). This organizational form is extremely useful in mailing lists where
different parts of the discussion diverge. NeoMutt displays threads as a tree structure.

In NeoMutt, when a mailbox is sorted by *threads*, there are a few additional functions
available in the *index* and *pager* modes as shown in the table below.

### Thread Mode Keys

| Key | Function | Description |
|-----|----------|-------------|
| ^D | `<delete-thread>` | delete all messages in the current thread |
| ^U | `<undelete-thread>` | undelete all messages in the current thread |
| ^N | `<next-thread>` | jump to the start of the next thread |
| ^P | `<previous-thread>` | jump to the start of the previous thread |
| ^R | `<read-thread>` | mark the current thread as read |
| Esc d | `<delete-subthread>` | delete all messages in the current subthread |
| Esc u | `<undelete-subthread>` | undelete all messages in the current subthread |
| Esc n | `<next-subthread>` | jump to the start of the next subthread |
| Esc p | `<previous-subthread>` | jump to the start of the previous subthread |
| Esc r | `<read-subthread>` | mark the current subthread as read |
| Esc t | `<tag-thread>` | toggle the tag on the current thread |
| Esc v | `<collapse-thread>` | toggle collapse for the current thread |
| Esc V | `<collapse-all>` | toggle collapse for all threads |
| P | `<parent-message>` | jump to parent message in thread |

### Thread Tree Display

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Thread tree visualisation in index

**Description:** The NeoMutt index screen with `set sort=threads` showing a mailbox (ideally a mailing list) with several threaded conversations. The tree should include at least one multi-level thread (3+ depth) with branching replies, a collapsed thread (showing the hidden message count), and a thread with a missing parent (showing the `?` character). The tree-drawing characters (`├─>`, `└─>`, `│`) should be clearly visible.

**Highlights:** The reader should notice the tree structure that visually represents the parent-child reply relationships, how deeper nesting indicates sub-conversations, and the special characters (`?` for missing, `&` for hidden) that indicate thread anomalies.
:::

In the *index*, the subject of threaded children messages will be prepended with thread
tree characters. By default, the subject itself will not be duplicated unless
`$hide_thread_subject` is unset. Special characters will be added to the thread tree as
detailed in the table below.

| Character | Description | Notes |
|-----------|-------------|-------|
| & | hidden message | see `$hide_limited` and `$hide_top_limited` |
| ? | missing message | see `$hide_missing` and `$hide_top_missing` |
| \* | pseudo thread | see `$strict_threads`; not displayed when `$narrow_tree` is set |
| = | duplicate thread | see `$duplicate_threads`; not displayed when `$narrow_tree` is set |

NeoMutt uses Unicode box-drawing characters to draw the thread tree (e.g., `├`, `└`, `│`, `─`). If your terminal does not support Unicode, or you prefer plain ASCII, set the `$ascii_chars` boolean variable to `yes`. This switches the tree characters to ASCII equivalents: `+`, `+`, `|`, and `-` respectively.

### Collapsing Threads

Collapsing a thread displays only the first message in the thread and hides the others.
This is useful when threads contain so many messages that you can only see a handful of
threads on the screen. See %M in `$index_format`. For example, you could use
`%<M?(#%03M)&(%4l)>` in `$index_format` to optionally display the number of hidden
messages if the thread is collapsed. The `%<char?if-part&else-part>` syntax is explained in
detail in the format string conditionals documentation.

### Strict Threading

Technically, every reply should contain a list of its parent messages in the thread tree,
but not all do. In these cases, NeoMutt groups them by subject which can be controlled
using the `$strict_threads` variable.

## Miscellaneous Functions

In addition, the *index* and *pager* menus have these interesting functions:

`<check-stats>`
: Calculate statistics for all monitored mailboxes declared using the `mailboxes` command.
  It will calculate statistics despite `$mail_check_stats` being unset.

`<create-alias>` (default: a)
: Creates a new alias based upon the current message (or prompts for a new one). Once
  editing is complete, an `alias` command is added to the file specified by the
  `$alias_file` variable for future use.

  :::{note}
  NeoMutt does not read the `$alias_file` upon startup so you must explicitly `source` the
  file.
  :::

`<check-traditional-pgp>` (default: Esc P)
: This function will search the current message for content signed or encrypted with PGP
  the "traditional" way, that is, without proper MIME tagging. Technically, this function
  will temporarily change the MIME content types of the body parts containing PGP data;
  this is similar to the `<edit-type>` function's effect.

`<edit-raw-message>`
: This command (available in the index and pager) allows you to edit the raw current
  message as it's present in the mail folder. After you have finished editing, the changed
  message will be appended to the current folder, and the original message will be marked
  for deletion; if the message is unchanged it won't be replaced.

  `<edit>` is a synonym of this for backwards compatibility.

  See also `<edit-or-view-raw-message>`, `<view-raw-message>`.

`<edit>` 
: Alias of `<edit-raw-message>` for backwards compatibility.

`<edit-or-view-raw-message>` (default: e)
: This command (available in the index and pager) is the same as `<edit-raw-message>` if
  the mailbox is writable, otherwise it is the same as `<view-raw-message>`.

`<edit-type>` (default: ^E on the attachment menu, and in the pager and index menus; ^T on the compose menu)
: This command is used to temporarily edit an attachment's content type to fix, for
  instance, bogus character set parameters. When invoked from the index or from the pager,
  you'll have the opportunity to edit the top-level attachment's content type. On the
  attachment menu, you can change any attachment's content type. These changes are not
  persistent, and get lost upon changing folders.

  Note that this command is also available on the compose menu. There, it's used to
  fine-tune the properties of attachments you are going to send.

`<enter-command>` (default: ":")
: This command is used to execute any command you would normally put in a configuration
  file. A common use is to check the settings of variables, or in conjunction with macros
  to change settings on the fly.

`<extract-keys>` (default: ^K)
: This command extracts PGP public keys from the current or tagged message(s) and adds
  them to your PGP public key ring.

`<forget-passphrase>` (default: ^F)
: This command wipes the passphrase(s) from memory. It is useful, if you misspelled the
  passphrase.

`<list-reply>` (default: L)
: Reply to the current or tagged message(s) by extracting any addresses which match the
  regular expressions given by the `lists` or `subscribe` commands, but also honor any
  `Mail-Followup-To` header(s) if the `$honor_followup_to` configuration variable is set.
  In addition, the `List-Post` header field is examined for `mailto:` URLs specifying a
  mailing list address. Using this when replying to messages posted to mailing lists helps
  avoid duplicate copies being sent to the author of the message you are replying to.

`<list-subscribe>`
: Send an email to the address specified in the List-Subscribe header as specified in
  [RFC2369](https://www.rfc-editor.org/rfc/rfc2369.html).

`<list-unsubscribe>`
: Send an email to the address specified in the List-Unsubscribe header as specified in
  [RFC2369](https://www.rfc-editor.org/rfc/rfc2369.html).

`<pipe-message>` (default: |)
: Asks for an external Unix command and pipes the current or tagged message(s) to it. The
  variables `$pipe_decode`, `$pipe_decode_weed`, `$pipe_split`, `$pipe_sep` and `$wait_key`
  control the exact behavior of this function.

`<resend-message>` (default: Esc e)
: NeoMutt takes the current message as a template for a new message. This function is best
  described as "recall from arbitrary folders". It can conveniently be used to forward MIME
  messages while preserving the original mail structure. Note that the amount of headers
  included here depends on the value of the `$weed` variable.

  This function is also available from the attachment menu. You can use this to easily
  resend a message which was included with a bounce message as a `message/rfc822` body
  part.

`<shell-escape>` (default: !)
: Asks for an external Unix command and executes it. The `$wait_key` can be used to control
  whether NeoMutt will wait for a key to be pressed when the command returns (presumably to
  let the user read the output of the command), based on the return status of the named
  command. If no command is given, an interactive shell is executed.

`<skip-headers>` (default: H)
: This function will skip to the first line of the body, past the headers of the current
  message, regardless of current position.

`<view-raw-message>`
: This command (available in the index and pager) opens the raw message read-only in an
  editor. This command does not allow editing the message, use `<edit-raw-message>` for
  this.

  See also `<edit-raw-message>`, `<edit-or-view-raw-message>`.

`<skip-quoted>` (default: S)
: This function will make the internal pager go forward to the next segment of non-quoted
  body text (whether the first line of the body after headers, or following a line of
  quoted text), or print a message if no further unquoted text can be found.

  The variable `$pager_skip_quoted_context` can be used to show some quoted context prior
  to the selected line.

`<toggle-quoted>` (default: T)
: The pager uses the `$quote_regex` variable to detect quoted text when displaying the body
  of the message. This function toggles the display of the quoted material in the message.
  It is particularly useful when being interested in just the response and there is a large
  amount of quoted text in the way.

  The variable `$toggle_quoted_show_levels` can be used to show some context by continuing
  to show that number of levels rather than hiding all quoted levels.
