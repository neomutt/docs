---
title: How to Compose to Sender
description: Send new mail to the sender of the current message in NeoMutt
keywords: compose, sender, new message, tagged messages
---

# How to Compose to Sender

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

## Introduction

The compose-to-sender feature adds a new command to start composing a new email to the sender
of the current message. This is not a reply, but a new, separate, message.

It works on tagged messages too, sending one email to all of the senders of the tagged messages.

## Functions

compose-to-sender adds the following function to NeoMutt. By default, it is not bound to a key.

| Menus       | Function                 | Description                                              |
|-------------|--------------------------|----------------------------------------------------------|
| index,pager | `<compose-to-sender>`    | compose a new email to the sender of the current email   |

## neomuttrc

```
# Example NeoMutt config file for the compose-to-sender feature.

# --------------------------------------------------------------------------
# FUNCTIONS – shown with an example mapping
# --------------------------------------------------------------------------
# Compose a new email (not a reply) to the sender
bind index,pager @ compose-to-sender

# vim: syntax=neomuttrc
```

## Known Bugs

None

## Credits

Brian Medley, Guillaume Brogi
