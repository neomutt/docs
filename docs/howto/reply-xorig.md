---
title: How to Reply with Original Address
description: Configure NeoMutt to reply using the X-Original-To header as the From address
keywords: reply, x-original-to, from, header, reply_with_xorig
---

# How to Reply with Original Address

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

*Direct reply to email using X-Original-To header*

## Introduction

Adds a `reply_with_xorig` for NeoMutt configuration files. If enabled, allows to reply to an
email using the email address in the first `X-Original-To:` header of a mail as the `From:`
header of the answer.

## Variables

| Name | Type | Default |
|------|------|---------|
| `reply_with_xorig` | Boolean | `no` |

## neomuttrc

```neomuttrc
# Example NeoMutt config file for the reply-with-xorig feature.

# --------------------------------------------------------------------------
# VARIABLES – shown with their default values
# --------------------------------------------------------------------------
# Use X-Original-To header to reply when reverse is disabled or no alternate
# is found.
set reply_with_xorig = "yes"

# vim: filetype=neomuttrc
```

## Credits

Pierre-Elliott Bécue
