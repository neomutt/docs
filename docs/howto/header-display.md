---
title: How to Customise Header Display
description: Control which message headers are shown, their order, and add custom headers in NeoMutt
keywords: headers, ignore, unignore, header-order, my-header, display, weeding
---

# How to Customise Header Display

## Header Display

When displaying a message in the pager, NeoMutt folds long header lines at
{ref}`$wrap <wrap>` columns. Though there are precise rules about where to
break and how, NeoMutt always folds headers using a tab for readability.

:::{note}
The sending side is not affected by this — NeoMutt tries to implement
standards-compliant folding.
:::

Despite not being a real header, NeoMutt will also display an mbox "From\_"
line in the pager along with other headers. This line can be manipulated with
`ignore`/`unignore` and `header-order`/`unheader-order` commands.

## Selecting Headers

**Usage:**

```neomuttrc
ignore string [string ...]
unignore { * | string ... }
```

Messages often have many header fields added by automatic processing systems,
or which may not seem useful to display on the screen. This command allows you
to specify header fields which you don't normally want to see in the pager.

You do not need to specify the full header field name. For example,
`ignore content-` will ignore all header fields that begin with the string
"content-". `ignore *` will ignore all headers.

To remove a previously added token from the list, use the `unignore` command.
The `unignore` command will make NeoMutt display headers matching the given
string. For example, if you do `ignore x-` it is possible to `unignore x-mailer`.

`unignore *` will remove all tokens from the ignore list.

:::{admonition} Example: Header weeding
:class: tip

```neomuttrc
# Sven's draconian header weeding
ignore *
unignore from date subject to cc
unignore organization organisation x-mailer: x-newsreader: x-mailing-list:
unignore posted-to:
```
:::

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Before/after header weeding

**Description:** Two pager views side by side (or stacked): one showing a message with all default headers visible, the other showing the same message after applying `ignore *` and selective `unignore` — only From, Date, Subject, To, Cc, and a few X- headers remain.

**Highlights:** The dramatic reduction in header clutter — the weeded view shows only the essential headers the user chose to keep.
:::

The above example will show "From:" headers as well as mbox "From\_" lines. To
hide the latter, instead use `unignore from: date subject to cc` on the second
line.

## Ordering Displayed Headers

**Usage:**

```neomuttrc
header-order header [header ...]
unheader-order { * | header ... }
```

:::{note}
Before 2026-01-13, these commands were called `hdr_order` and `unhdr_order`.
:::

With the `header-order` command you can specify an order in which NeoMutt will
attempt to present these headers to you when viewing messages.

`unheader-order *` will clear all previous headers from the order list, thus
removing the header order effects set by the system-wide startup file.

:::{admonition} Example: Configuring header display order
:class: tip

```neomuttrc
header-order From Date: From: To: Cc: Subject:
```
:::

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Custom header display order

**Description:** Pager view of a message where `header-order` has been applied — headers appear in the configured sequence (From\_, Date:, From:, To:, Cc:, Subject:) rather than the order they appear in the raw message.

**Highlights:** The logical reading order of headers — the most important fields (sender, date, subject) appear first, matching the configured `header-order`.
:::

## User-Defined Headers

**Usage:**

```neomuttrc
my-header string
unmy-header { * | field ... }
```

:::{note}
Before 2026-01-13, these commands were called `my_hdr` and `unmy_hdr`.
:::

The `my-header` command allows you to create your own header fields which will
be added to every message you send and appear in the editor if
{ref}`$edit_headers <edit-headers>` is set.

For example, if you would like to add an "Organization:" header field to all of
your outgoing messages, you can put something like the following in your
`.neomuttrc`:

```neomuttrc
my-header Organization: A Really Big Company, Anytown, USA
```

:::{note}
Space characters are *not* allowed between the keyword and the colon (":").
The standard for electronic mail ([RFC2822](https://www.rfc-editor.org/rfc/rfc2822.html)) says that space is illegal there, so
NeoMutt enforces the rule.
:::

If you would like to add a header field to a single message, you should either
set the {ref}`$edit_headers <edit-headers>` variable, or use the
`<edit-headers>` function (default: "E") in the compose menu so that you can
edit the header of your message along with the body.

To remove user defined header fields, use the `unmy-header` command. You may
specify an asterisk ("*") to remove all header fields, or the fields to remove.
For example, to remove all "To" and "Cc" header fields, you could use:

```neomuttrc
unmy-header to cc
```

## Editing Raw Messages

NeoMutt provides four related functions for accessing the raw [RFC2822](https://www.rfc-editor.org/rfc/rfc2822.html) source
of a message:

| Function | Description |
|----------|-------------|
| `<view-raw-message>` | Open the raw message source in the pager (read-only). |
| `<edit-raw-message>` | Open the raw message in `$editor`; the edited result replaces the original in the mailbox. |
| `<edit>` | Alias for `<edit-raw-message>` (retained for backwards compatibility). |
| `<edit-or-view-raw-message>` | Uses `<edit-raw-message>` if the folder is writable, otherwise falls back to `<view-raw-message>`. |

:::{note}
`<edit-raw-message>` modifies the message in place in the mailbox. Use
`<view-raw-message>` if you only want to inspect the source without making
changes.
:::
