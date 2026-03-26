---
title: Compose to Sender
description: Start a new email to the sender of the current or tagged messages without replying
keywords: compose, sender, new message, tagged messages, compose-to-sender, bind, index, pager, new email, contact sender
---

# Compose to Sender

## Introduction

The compose-to-sender feature adds a new command to start composing a new email to the sender of the current message.
This is not a reply, but a new, separate, message.

It works on tagged messages too, sending one email to all of the senders of the tagged messages.

## Functions

compose-to-sender adds the following function to NeoMutt.
By default, it is not bound to a key.

| Menus       | Function              | Description                                            |
|-------------|-----------------------|--------------------------------------------------------|
| index,pager | `<compose-to-sender>` | compose a new email to the sender of the current email |

## neomuttrc

```neomuttrc
# Example NeoMutt config file for the compose-to-sender feature.

# --------------------------------------------------------------------------
# FUNCTIONS – shown with an example mapping
# --------------------------------------------------------------------------
# Compose a new email (not a reply) to the sender
bind index,pager @ compose-to-sender

# vim: filetype=neomuttrc
```

