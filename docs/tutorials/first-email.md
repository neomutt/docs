---
title: Reading Your First Email
description: Learn to navigate the message index, read messages in the pager, and work with threaded conversations
keywords: [neomutt, reading, email, index, pager, threads, tutorial]
diataxis_type: tutorial
---

# Reading Your First Email

This tutorial shows you how to read mail in NeoMutt using the message list (Index) and the
message view (Pager). You'll open a message, move around, and use search.

If you don't see any mail yet, finish your setup first in [Writing Your First Configuration](first-config)
or the guided [Start Here](../start-here) page.

What you'll do:

1. Open a message from the Index.
2. Read it in the Pager and move around.
3. Search for a message by keyword.

If you want only the basics, you can stop after the "Most Common Pager Keys" section. The
rest of the page is optional detail.

## The Message Index

Common keys used to navigate through and manage messages in the index are shown below. How
messages are presented in the index menu can be customized using the `$index_format` variable.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** The Message Index with email list

**Description:** The NeoMutt Message Index showing a mailbox with several emails, displaying message numbers, status flags (N for new, O for old, ! for flagged, r for replied), dates, sender names, message sizes, and subjects.

**Highlights:** The meaning of the flag column — how different status indicators (new, old, replied, flagged, tagged) appear next to each message in the list.
:::

| Key | Description |
|-----|-------------|
| c | change to a different mailbox |
| Esc c | change to a folder in read-only mode |
| C | copy the current message to another mailbox |
| Esc C | decode a message and copy it to a folder |
| Esc s | decode a message and save it to a folder |
| D | delete messages matching a pattern |
| d | delete the current message |
| F | mark as important |
| l | show messages matching a pattern |
| N | mark message as new |
| o | change the current sort method |
| O | reverse sort the mailbox |
| q | save changes and exit |
| s | save-message |
| T | tag messages matching a pattern |
| t | toggle the tag on a message |
| Esc t | toggle tag on entire message thread |
| U | undelete messages matching a pattern |
| u | undelete-message |
| v | view-attachments |
| x | abort changes and exit |
| \<Return\> | display-message |
| \<Tab\> | Jump to the next new or unread message |
| @ | show the author's full e-mail address |
| $ | Save changes to mailbox |
| / | search |
| Esc / | search-reverse |
| ^L | Clear and redraw the screen |
| ^T | untag messages matching a pattern |

In addition to who sent the message and the subject, a short summary of the disposition of
each message is printed beside the message number. Zero or more of the "flags" shown below
may appear, some of which can be turned on or off using these functions: `<set-flag>` and
`<clear-flag>` bound by default to "w" and "W" respectively.

Furthermore, the recipient flags reflect who the message is addressed to. They can be
customized with the `$to_chars` variable.

### Message Status Flags

| Flag | Description |
|------|-------------|
| D | message is deleted (is marked for deletion) |
| d | message has attachments marked for deletion |
| K | contains a PGP public key |
| N | message is new |
| O | message is old |
| P | message is PGP encrypted |
| r | message has been replied to |
| S | message is signed, and the signature is successfully verified |
| s | message is signed |
| ! | message is flagged |
| \* | message is tagged |
| n | thread contains new messages (only if collapsed) |
| o | thread contains old messages (only if collapsed) |

### Message Recipient Flags

| Flag | Description |
|------|-------------|
| + | message is to you and you only |
| T | message is to you, but also to or CC'ed to others |
| C | message is CC'ed to you |
| F | message is from you |
| L | message is sent to a subscribed mailing list |
| R | message has your address in the Reply-To field |

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Index showing status and recipient flags

**Description:** A close-up of the NeoMutt Index flag columns, with messages displaying a variety of status flags (N, O, D, r, !) and recipient flags (+, T, C, F, L) so the reader can see how flags combine in practice.

**Highlights:** How the status flag and recipient flag columns sit side by side, and how different flag combinations help the user quickly identify message state and relevance.
:::

## The Pager

By default, NeoMutt uses its built-in pager to display the contents of messages (an external
pager such as `less(1)` can be configured, see `$pager` variable). The pager is very similar
to the Unix program `less(1)` though not nearly as featureful.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** The Pager displaying an email

**Description:** The NeoMutt Pager showing a message with headers (From, To, Date, Subject) at the top, followed by the email body text. Show quoted text (lines starting with >) in a different color and a URL highlighted in the body.

**Highlights:** The header section at the top, the colored quoted text showing reply depth, and how the pager status line at the bottom indicates the current scroll position.
:::

### Most Common Pager Keys

| Key | Description |
|-----|-------------|
| \<Return\> | go down one line |
| \<Space\> | display the next page (or next message if at the end of a message) |
| \- | go back to the previous page |
| n | Search for next match |
| S | Skip beyond quoted text |
| T | Toggle display of quoted text |
| ? | show keybindings |
| / | regular expression search |
| Esc / | backward regular expression search |
| \\ | toggle highlighting of search matches |
| ^ | Jump to the top of the message |

In addition to the key bindings above, many of the functions from the index menu are also
available in the pager, such as `<delete-message>` or `<copy-message>` (this is one advantage
over using an external pager to view messages).

Also, the internal pager supports a couple other advanced features. For one, you can set
`$pager_read_delay` to operate in a preview mode, where new messages are not marked read
unless you remain on the message for a certain length of time. Additionally, it will accept
and translate the "standard" nroff sequences for bold and underline. These sequences are
a series of either the letter, backspace ("^H"), the letter again for bold or the letter,
backspace, "\_" for denoting underline. NeoMutt will attempt to display these in bold and
underline respectively if your terminal supports them. If not, you can use the bold and
underline color objects to specify a `color` or mono attribute for them.

Additionally, the internal pager supports the ANSI escape sequences for character attributes.
NeoMutt translates them into the correct color and character settings. The sequences NeoMutt
supports are:

```
\e[ Ps; Ps; ...  Ps;m
```

where *Ps* can be one of the codes shown below.

### ANSI Escape Sequences

| Escape code | Description |
|-------------|-------------|
| 0 | All attributes off |
| 1 | Bold on |
| 3 | Italics on |
| 4 | Underline on |
| 5 | Blink on |
| 7 | Reverse video on |
| 3 *\<color\>* | Foreground color is *\<color\>* |
| 4 *\<color\>* | Background color is *\<color\>* |

### Color Sequences

| Color code | Color |
|------------|-------|
| 0 | Black |
| 1 | Red |
| 2 | Green |
| 3 | Yellow |
| 4 | Blue |
| 5 | Magenta |
| 6 | Cyan |
| 7 | White |

NeoMutt uses these attributes for handling `text/enriched` messages, and they can also be used
by an external autoview script for highlighting purposes.

:::{note}
If you change the colors for your display, for example by changing the color associated with
color2 for your xterm, then that color will be used instead of green.
:::

:::{note}
Note that the search commands in the pager take regular expressions, which are not quite the
same as the more complex patterns used by the search command in the index. This is because
patterns are used to select messages by criteria whereas the pager already displays a selected
message.
:::

## Threaded Mode

So-called "threads" provide a hierarchy of messages where replies are linked to their parent
message(s). This organizational form is extremely useful in mailing lists where different
parts of the discussion diverge. NeoMutt displays threads as a tree structure.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Threaded message view in the Index

**Description:** The NeoMutt Index sorted by threads, showing a tree structure with parent messages and indented replies using tree-drawing characters (├─, └─, │). Include a thread with multiple levels of replies and at least one collapsed thread showing the hidden message count.

**Highlights:** The visual tree hierarchy connecting replies to parent messages, how subjects are deduplicated in threads, and how a collapsed thread displays its message count.
:::

In NeoMutt, when a mailbox is sorted by *threads*, there are a few additional functions
available in the *index* and *pager* modes as shown below.

### Thread Mode Keys

| Key | Function | Description |
|-----|----------|-------------|
| ^D | `<delete-thread>` | delete all messages in the current thread |
| ^U | `<undelete-thread>` | undelete all messages in the current thread |
| ^N | `<next-thread>` | jump to the start of the next thread |
| ^P | `<previous-thread>` | jump to the start of the previous thread |
| ^R | `<read-thread>` | Mark the current thread as read |
| Esc d | `<delete-subthread>` | delete all messages in the current subthread |
| Esc u | `<undelete-subthread>` | undelete all messages in the current subthread |
| Esc n | `<next-subthread>` | jump to the start of the next subthread |
| Esc p | `<previous-subthread>` | jump to the start of the previous subthread |
| Esc r | `<read-subthread>` | Mark the current subthread as read |
| Esc t | `<tag-thread>` | toggle the tag on the current thread |
| Esc v | `<collapse-thread>` | toggle collapse for the current thread |
| Esc V | `<collapse-all>` | toggle collapse for all threads |
| P | `<parent-message>` | Jump to parent message in thread |

In the *index*, the subject of threaded children messages will be prepended with thread tree
characters. By default, the subject itself will not be duplicated unless
`$hide_thread_subject` is unset. Special characters will be added to the thread tree as
detailed below.

### Special Thread Characters

| Character | Description | Notes |
|-----------|-------------|-------|
| & | hidden message | see `$hide_limited` and `$hide_top_limited` |
| ? | missing message | see `$hide_missing` and `$hide_top_missing` |
| \* | pseudo thread | see `$strict_threads`; not displayed when `$narrow_tree` is set |
| = | duplicate thread | see `$duplicate_threads`; not displayed when `$narrow_tree` is set |

Collapsing a thread displays only the first message in the thread and hides the others. This
is useful when threads contain so many messages that you can only see a handful of threads on
the screen. See %M in `$index_format`. For example, you could use
`%<M?(#%03M)&(%4l)>` in `$index_format` to optionally display the number of hidden messages
if the thread is collapsed. The `%<char?if-part&else-part>` syntax is explained in detail in
format string conditionals.

Technically, every reply should contain a list of its parent messages in the thread tree, but
not all do. In these cases, NeoMutt groups them by subject which can be controlled using the
`$strict_threads` variable.

## Miscellaneous Functions

In addition, the *index* and *pager* menus have these interesting functions:

`<check-stats>`
: Calculate statistics for all monitored mailboxes declared using the `mailboxes` command. It
  will calculate statistics despite `$mail_check_stats` being unset.

`<create-alias>` (default: a)
: Creates a new alias based upon the current message (or prompts for a new one). Once editing
  is complete, an `alias` command is added to the file specified by the `$alias_file` variable
  for future use.

  :::{note}
  NeoMutt does not read the `$alias_file` upon startup so you must explicitly `source` the
  file.
  :::

`<check-traditional-pgp>` (default: Esc P)
: This function will search the current message for content signed or encrypted with PGP the
  "traditional" way, that is, without proper MIME tagging. Technically, this function will
  temporarily change the MIME content types of the body parts containing PGP data; this is
  similar to the `<edit-type>` function's effect.

`<edit-raw-message>`
: This command (available in the index and pager) allows you to edit the raw current message
  as it's present in the mail folder. After you have finished editing, the changed message
  will be appended to the current folder, and the original message will be marked for
  deletion; if the message is unchanged it won't be replaced.

  `<edit>` is a synonym of this for backwards compatibility.

  See also `<edit-or-view-raw-message>`, `<view-raw-message>`.

`<edit>`
: Alias of `<edit-raw-message>` for backwards compatibility.

`<edit-or-view-raw-message>` (default: e)
: This command (available in the index and pager) is the same as `<edit-raw-message>` if the
  mailbox is writable, otherwise it is the same as `<view-raw-message>`.

`<edit-type>` (default: ^E on the attachment menu, and in the pager and index menus; ^T on the compose menu)
: This command is used to temporarily edit an attachment's content type to fix, for instance,
  bogus character set parameters. When invoked from the index or from the pager, you'll have
  the opportunity to edit the top-level attachment's content type. On the attachment menu, you
  can change any attachment's content type. These changes are not persistent, and get lost
  upon changing folders.

  Note that this command is also available on the compose menu. There, it's used to fine-tune
  the properties of attachments you are going to send.

`<enter-command>` (default: ":")
: This command is used to execute any command you would normally put in a configuration file.
  A common use is to check the settings of variables, or in conjunction with macros to change
  settings on the fly.

`<extract-keys>` (default: ^K)
: This command extracts PGP public keys from the current or tagged message(s) and adds them
  to your PGP public key ring.

`<forget-passphrase>` (default: ^F)
: This command wipes the passphrase(s) from memory. It is useful, if you misspelled the
  passphrase.

`<list-reply>` (default: L)
: Reply to the current or tagged message(s) by extracting any addresses which match the
  regular expressions given by the `lists` or `subscribe` commands, but also honor any
  `Mail-Followup-To` header(s) if the `$honor_followup_to` configuration variable is set. In
  addition, the `List-Post` header field is examined for `mailto:` URLs specifying a mailing
  list address. Using this when replying to messages posted to mailing lists helps avoid
  duplicate copies being sent to the author of the message you are replying to.

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

  This function is also available from the attachment menu. You can use this to easily resend
  a message which was included with a bounce message as a `message/rfc822` body part.

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
  editor. This command does not allow editing the message, use `<edit-raw-message>` for this.

  See also `<edit-raw-message>`, `<edit-or-view-raw-message>`.

`<skip-quoted>` (default: S)
: This function will make the internal pager go forward to the next segment of non-quoted
  body text (whether the first line of the body after headers, or following a line of quoted
  text), or print a message if no further unquoted text can be found.

  The variable `$pager_skip_quoted_context` can be used to show some quoted context prior to
  the selected line.

`<toggle-quoted>` (default: T)
: The pager uses the `$quote_regex` variable to detect quoted text when displaying the body
  of the message. This function toggles the display of the quoted material in the message. It
  is particularly useful when being interested in just the response and there is a large
  amount of quoted text in the way.

  The variable `$toggle_quoted_show_levels` can be used to show some context by continuing to
  show that number of levels rather than hiding all quoted levels.

## Next Steps

- "I want to send a message." Continue with [Sending Your First Email](sending-email).
- "I want to search and filter faster." Continue with [Searching and Filtering Email](searching-email).
- "I want a key reference." See [Shortcuts Reference](../reference/shortcuts).
