---
title: Email Body Templates
description: Control how NeoMutt assembles the body of new, reply, and forwarded emails — greeting, attribution, quoted text, and signature
keywords: reply, forward, compose, greeting, signature, sig_dashes, sig_on_top, attribution_intro, attribution_trailer, attribution_locale, forward_attribution_intro, forward_attribution_trailer, forward_format, forward_quote, indent_string, template, layout
---

# Email Body Templates

When you compose a new email, reply to a message, or forward one, NeoMutt assembles a template for the message body before opening your editor.
This guide shows you how to control each part of that template.

## Body Layout

The template is built from several blocks.
Their order depends on the action you're performing and your settings.

### New Email

```
┍Greeting
│ (your cursor starts here)
┕Signature
```

### Reply

```
┍Greeting
│Attribution Intro
│> Quoted original message
│Attribution Trailer
┕Signature
```

### Reply (`$sig_on_top` enabled)

```
┍Greeting
│Signature
│Attribution Intro
│> Quoted original message
┕Attribution Trailer
```

### Forward (inline)

```
┍Greeting
│Forward Intro
│Original message text
│Forward Trailer
┕Signature
```

### Forward (inline, `$forward_quote` enabled)

```
┍Greeting
│Forward Intro
│> Quoted original message
│Forward Trailer
┕Signature
```

## Greeting

The `$greeting` line is placed at the very top of every message — new, reply, or forward.
It supports expandos that reference the recipient, so you can personalise it.

```neomuttrc
set greeting = "Hi %n,"
```

This produces, for example:

```
Hi Alice,
```

## Attribution (Replies)

When you reply to a message, NeoMutt wraps the quoted original text between two attribution lines.

### Attribution Intro

`$attribution_intro` is placed **before** the quoted text.
The default is:

```neomuttrc
set attribution_intro = "On %d, %n wrote:"
```

This produces something like:

```
On Mon, 31 Mar 2025, Alice wrote:
```

### Attribution Trailer

`$attribution_trailer` is placed **after** the quoted text.
By default it is empty.
Set it if you'd like closing text after the quoted block:

```neomuttrc
set attribution_trailer = "-- end of quoted message from %n --"
```

### Attribution Locale

`$attribution_locale` controls the locale used when formatting dates in `$attribution_intro` and `$attribution_trailer`.
This affects how the `%d` expando renders:

```neomuttrc
set attribution_locale = "de_DE.UTF-8"
```

With this setting, the date in the attribution intro would be formatted according to German conventions.

## Quoting (Indent String)

`$indent_string` is the prefix added to each line of the original message when quoting it in a reply.
The default is `"> "`:

```neomuttrc
set indent_string = "> "
```

A reply then looks like:

```
On Mon, 31 Mar 2025, Alice wrote:
> Thanks for getting back to me.
> I'll review the document tonight.
```

## Forwarding

### Forward Subject

`$forward_format` controls the **Subject** line of forwarded messages.
It does not affect the message body:

```neomuttrc
set forward_format = "[%a: %s]"
```

This produces a subject like `[alice@example.com: Meeting notes]`.

### Forward Intro and Trailer

`$forward_attribution_intro` and `$forward_attribution_trailer` wrap the forwarded message body, similar to how attribution lines wrap replies:

```neomuttrc
set forward_attribution_intro = "----- Forwarded message from %f -----"
set forward_attribution_trailer = "----- End forwarded message -----"
```

The result:

```
----- Forwarded message from Alice Langley <alice@example.com> -----

(original message text)

----- End forwarded message -----
```

Both expandos also honour `$attribution_locale` for date formatting.

### Forward Quoting

By default, forwarded text is included verbatim.
Set `$forward_quote` to prefix each line with `$indent_string`, just like a reply:

```neomuttrc
set forward_quote = yes
```

## Signature

`$signature` points to a file (or a command) whose contents are appended to the message:

```neomuttrc
set signature = "~/.signature"
```

### Signature Separator

`$sig_dashes` (enabled by default) inserts the standard `-- ` separator line before your signature.
Disable it if your signature file already contains the separator or you don't want one:

```neomuttrc
set sig_dashes = no
```

### Signature Placement

By default the signature goes **below** the quoted text.
Enable `$sig_on_top` to place it **above** the quoted text, between the greeting and the attribution — this is the "top-posting" style:

```neomuttrc
set sig_on_top = yes
```

## Putting It All Together

Here is a complete example for replies in bottom-posting style:

```neomuttrc
set greeting             = "Hi %n,"
set attribution_intro    = "On %d, %n wrote:"
set attribution_trailer  = ""
set indent_string        = "> "
set signature            = "~/.signature"
set sig_dashes           = yes
set sig_on_top           = no
```

The resulting reply template:

```
Hi Alice,
On Mon, 31 Mar 2025, Alice wrote:
> Thanks for getting back to me.
> I'll review the document tonight.

-- 
Bob
```

And a top-posting configuration:

```neomuttrc
set sig_on_top = yes
```

```
Hi Alice,
-- 
Bob
On Mon, 31 Mar 2025, Alice wrote:
> Thanks for getting back to me.
> I'll review the document tonight.
```

## Which Options Apply Where

| Config Variable                 | New Email | Reply | Forward |
|---------------------------------|:---------:|:-----:|:-------:|
| `$greeting`                     | ✓         | ✓     | ✓       |
| `$attribution_intro`            |           | ✓     |         |
| `$attribution_trailer`          |           | ✓     |         |
| `$attribution_locale`           |           | ✓     | ✓       |
| `$indent_string`                |           | ✓     | ✓ ^1^   |
| `$forward_attribution_intro`    |           |       | ✓       |
| `$forward_attribution_trailer`  |           |       | ✓       |
| `$forward_format`               |           |       | ✓ ^2^   |
| `$forward_quote`                |           |       | ✓       |
| `$signature`                    | ✓         | ✓     | ✓       |
| `$sig_dashes`                   | ✓         | ✓     | ✓       |
| `$sig_on_top`                   | ✓         | ✓     | ✓       |

^1^ Only when `$forward_quote` is enabled.
^2^ Controls the Subject line, not the body.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Reply template in the editor

**Description:** The NeoMutt editor showing a reply message with the
greeting ("Hi Alice,"), attribution intro ("On …, Alice wrote:"), quoted
original text prefixed with "> ", and the signature block below,
separated by "-- ".

**Highlights:** Each labelled section of the template: greeting,
attribution intro, quoted text with indent string, and signature with
sig-dashes separator.
:::

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Forward template in the editor

**Description:** The NeoMutt editor showing a forwarded message with the
greeting, forward attribution intro ("--- Forwarded message from …"),
the original message body, the forward attribution trailer
("--- End forwarded message ---"), and the signature.

**Highlights:** The difference from a reply — forward intro/trailer
instead of attribution intro/trailer, and unquoted body text (with
`$forward_quote` disabled).
:::

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Signature placement — top vs bottom

**Description:** Two side-by-side NeoMutt editor views of the same reply:
one with `$sig_on_top = no` (signature after the quoted text) and one
with `$sig_on_top = yes` (signature between the greeting and the quoted
text).

**Highlights:** The position of the "-- " separator and signature text
relative to the quoted block.
:::

## See Also

- {doc}`/howto/compose-flow` — the full step-by-step composition sequence
- {doc}`/howto/forwarding-mail` — forwarding methods and MIME vs inline
- {doc}`/howto/format-strings` — how expandos like `%n` and `%d` work

