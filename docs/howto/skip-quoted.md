---
title: How to Use Skip-Quoted
description: Manage quoted text display in the NeoMutt pager with skip-quoted, toggle-quoted, and skip-headers
keywords: skip-quoted, toggle-quoted, skip-headers, pager, quoted text, pager_skip_quoted_context, toggle_quoted_show_levels
---

# How to Use Skip-Quoted

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

## Support

**Since:** `$skip_quoted_offset` in NeoMutt 2016-03-28,
`$toggle_quoted_show_levels` in NeoMutt 2019-10-25,
`<skip-headers>` in NeoMutt 2021-02-05

## Introduction

When viewing an email, the `<skip-quoted>` function (by default the `S` key)
will scroll past any email headers or quoted text. Sometimes, a little context
is useful. By setting the `$skip_quoted_offset` variable, you can select how
much of the quoted text is left visible.

When using the `<toggle-quoted>` function (by default the `T` key), it can be
convenient to hide text that has been quoted multiple times while still leaving
quoted text that is relevant to the unquoted reply intact. This can be done by
setting the `$toggle_quoted_show_levels` variable.

Also, it can be handy to jump directly to the start of the email body with the
`<skip-headers>` function (by default the `H` key).

## Functions

| Menus | Default Key | Function | Description |
|-------|-------------|----------|-------------|
| pager | H | `<skip-headers>` | jump to first line after headers |

## Variables

| Name | Type | Default |
|------|------|---------|
| `pager_skip_quoted_context` | number | 0 |
| `skip_quoted_offset` | synonym | pager_skip_quoted_context |
| `toggle_quoted_show_levels` | number | 0 |

## neomuttrc

```bash
# Example NeoMutt config file for the skip-quoted feature.

# The 'S' (skip-quoted) command scrolls the pager past the quoted text (usually
# indented with '> '. Setting 'pager_skip_quoted_context leaves some lines
# of quoted text on screen for context.

# Show three quoted lines before the reply
set pager_skip_quoted_context = 3

# The 'T' (toggle-quoted) command hides quoted text, but can
# be limited to only hiding deeply-nested quotes.

# Preserve the first level of quoted text
set toggle_quoted_show_levels = 1

# vim: syntax=neomuttrc
```

## Known Bugs

None

## Credits

David Sterba, Richard Russon
