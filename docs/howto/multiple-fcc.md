---
title: How to Use Multiple Fcc
description: Save copies of outgoing mail to multiple folders in NeoMutt
keywords: fcc, multiple copies, outgoing mail, record, fcc-hook
---

# How to Use Multiple Fcc

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

## Introduction

This feature allows the user to save outgoing emails in multiple folders.

Folders should be listed separated by commas, **but no spaces**.

The "fcc" field of an email can be set in two ways:

- The `<edit-fcc>` command in the compose menu (default key: "f")
- Creating a `fcc-hook` in your `.neomuttrc`

## See Also

- {ref}`$record <record>`
- **fcc-hook**

## Known Bugs

None

## Credits

Omen Wild, Richard Russon
