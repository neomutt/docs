---
title: Forward and Bounce Mail
description: Forward messages inline or as MIME attachments, and bounce messages to new recipients
keywords: forward, bounce, resend, mime_forward, inline forward, forward_decode, forward_attachments, forward_format, forward_references, bounce-message, forward-message, weed, forward_edit
---

# Forward and Bounce Mail

Bouncing and forwarding let you send an existing message to recipients that you specify.
Bouncing a message sends a verbatim copy of a message to alternative addresses as if they were the message's original recipients specified in the Bcc header.
Forwarding a message, on the other hand, allows you to modify the message before it is resent (for example, by adding your own comments).
Bouncing is done using the `<bounce-message>` function and forwarding using the `<forward-message>` function bound to "b" and "f" respectively.

## Forwarding Methods

Forwarding can be done by including the original message in the new message's body (surrounded by indicating lines: see `$forward_attribution_intro` and `$forward_attribution_trailer`) or including it as a MIME attachment, depending on the value of the `$mime_forward` variable.
Decoding of attachments, like in the pager, can be controlled by the `$forward_decode` and `$mime_forward_decode` variables, respectively.
The desired forwarding format may depend on the content, therefore `$mime_forward` is a quadoption which, for example, can be set to "ask-no".

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Inline forward vs MIME forward in compose

**Description:** Two NeoMutt compose screens contrasting the forwarding methods: (1) inline forward (`$mime_forward`=no) with the original message text included in the body between attribution intro/trailer lines, and (2) MIME forward (`$mime_forward`=yes) with the original message listed as an attached message/rfc822 entry in the attachment list.

**Highlights:** The structural difference between inline forwarding (original text in the message body) and MIME forwarding (original message as an attachment), helping the reader choose the appropriate method.
:::

## Default Inline Forwarding

NeoMutt's default (`$mime_forward`="no" and `$forward_decode`="yes") is to use standard inline forwarding.
In that mode all text-decodable parts are included in the new message body.
Other attachments from the original email can also be attached to the new message, based on the quadoption `$forward_attachments`.

## Header Inclusion

The inclusion of headers is controlled by the current setting of the `$weed` variable, unless `$mime_forward` is set.
The subject of the email is controlled by `$forward_format`.

## Threading Forwarded Messages

By default a forwarded message does not reference the messages it contains.
When `$forward_references` is set, a forwarded message includes the `In-Reply-To:` and `References:` headers, just like a reply would.
Hence the forwarded message becomes part of the original thread instead of starting a new one.

## Editing the Forwarded Message

Editing the message to forward follows the same procedure as sending or replying to a message does, but can be disabled via the quadoption `$forward_edit`.
