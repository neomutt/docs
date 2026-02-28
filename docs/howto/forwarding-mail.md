---
title: How to Forward and Bounce Mail
description: Forward or bounce existing messages to new recipients in NeoMutt
keywords: forward, bounce, resend, mime-forward, inline forward
---

# How to Forward and Bounce Mail

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

Bouncing and forwarding let you send an existing message to recipients that you specify.
Bouncing a message sends a verbatim copy of a message to alternative addresses as if they were
the message's original recipients specified in the Bcc header. Forwarding a message, on the
other hand, allows you to modify the message before it is resent (for example, by adding your
own comments). Bouncing is done using the `<bounce-message>` function and forwarding using the
`<forward-message>` function bound to "b" and "f" respectively.

## Forwarding Methods

Forwarding can be done by including the original message in the new message's body (surrounded
by indicating lines: see {ref}`$forward_attribution_intro <forward-attribution-intro>` and
{ref}`$forward_attribution_trailer <forward-attribution-trailer>`) or including it as a MIME
attachment, depending on the value of the {ref}`$mime_forward <mime-forward>` variable. Decoding
of attachments, like in the pager, can be controlled by the
{ref}`$forward_decode <forward-decode>` and {ref}`$mime_forward_decode <mime-forward-decode>`
variables, respectively. The desired forwarding format may depend on the content, therefore
{ref}`$mime_forward <mime-forward>` is a quadoption which, for example, can be set to "ask-no".

## Default Inline Forwarding

NeoMutt's default ({ref}`$mime_forward <mime-forward>`="no" and
{ref}`$forward_decode <forward-decode>`="yes") is to use standard inline forwarding. In that
mode all text-decodable parts are included in the new message body. Other attachments from
the original email can also be attached to the new message, based on the quadoption
{ref}`$forward_attachments <forward-attachments>`.

## Header Inclusion

The inclusion of headers is controlled by the current setting of the
{ref}`$weed <weed>` variable, unless {ref}`$mime_forward <mime-forward>` is set. The subject
of the email is controlled by {ref}`$forward_format <forward-format>`.

## Threading Forwarded Messages

By default a forwarded message does not reference the messages it contains. When
{ref}`$forward_references <forward-references>` is set, a forwarded message includes the
"In-Reply-To:" and "References:" headers, just like a reply would. Hence the forwarded message
becomes part of the original thread instead of starting a new one.

## Editing the Forwarded Message

Editing the message to forward follows the same procedure as sending or replying to a message
does, but can be disabled via the quadoption {ref}`$forward_edit <forward-edit>`.
