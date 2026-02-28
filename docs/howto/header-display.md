---
title: How to Customise Header Display
description: Control which message headers are shown, their order, and add custom headers in NeoMutt
keywords: headers, ignore, unignore, header-order, my-header, display, weeding
---

# How to Customise Header Display

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

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

```
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

```
# Sven's draconian header weeding
ignore *
unignore from date subject to cc
unignore organization organisation x-mailer: x-newsreader: x-mailing-list:
unignore posted-to:
```
:::

The above example will show "From:" headers as well as mbox "From\_" lines. To
hide the latter, instead use `unignore from: date subject to cc` on the second
line.

## Ordering Displayed Headers

**Usage:**

```
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

```
header-order From Date: From: To: Cc: Subject:
```
:::

## User-Defined Headers

**Usage:**

```
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

```
my-header Organization: A Really Big Company, Anytown, USA
```

:::{note}
Space characters are *not* allowed between the keyword and the colon (":").
The standard for electronic mail (RFC2822) says that space is illegal there, so
NeoMutt enforces the rule.
:::

If you would like to add a header field to a single message, you should either
set the {ref}`$edit_headers <edit-headers>` variable, or use the
`<edit-headers>` function (default: "E") in the compose menu so that you can
edit the header of your message along with the body.

To remove user defined header fields, use the `unmy-header` command. You may
specify an asterisk ("*") to remove all header fields, or the fields to remove.
For example, to remove all "To" and "Cc" header fields, you could use:

```
unmy-header to cc
```
