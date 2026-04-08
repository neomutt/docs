---
title: Skip-Quoted
description: Manage quoted text display in the NeoMutt pager with skip-quoted, toggle-quoted, and skip-headers
keywords: skip-quoted, toggle-quoted, skip-headers, pager, quoted text, pager_skip_quoted_context, toggle_quoted_show_levels
since: 2021-02-05
---

# Skip-Quoted 🔥

## Support

**Since:** NeoMutt 2021-02-05

## Introduction

When viewing an email, the `<skip-quoted>` function (by default the `S` key) will scroll past any email headers or quoted text.
Sometimes, a little context is useful.
By setting the `$skip_quoted_offset` variable, you can select how much of the quoted text is left visible.

When using the `<toggle-quoted>` function (by default the `T` key), it can be convenient to hide text that has been quoted multiple times while still leaving quoted text that is relevant to the unquoted reply intact.
This can be done by setting the `$toggle_quoted_show_levels` variable.

Also, it can be handy to jump directly to the start of the email body with the `<skip-headers>` function (by default the `H` key).

## Functions

| Menus | Default Key | Function         | Description                      |
|-------|-------------|------------------|----------------------------------|
| pager | `H`         | `<skip-headers>` | Jump to first line after headers |

## Variables

| Name                        | Type    | Default                   |
|-----------------------------|---------|---------------------------|
| `pager_skip_quoted_context` | number  | 0                         |
| `skip_quoted_offset`        | synonym | pager_skip_quoted_context |
| `toggle_quoted_show_levels` | number  | 0                         |

## neomuttrc

```neomuttrc
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

# vim: filetype=neomuttrc
```

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Pager with quoted text and skip-quoted context

**Description:** NeoMutt pager showing a reply message with multiple levels of quoted text (>, >>, >>>) in different colours.
The `pager_skip_quoted_context` is set to 3, so after pressing {kbd}`S`, the pager shows the last 3 lines of quoted text above the new reply content.

**Highlights:** The coloured quote levels providing visual depth, and the context lines that remain visible after skip-quoted — showing how the reader retains just enough quoted context to follow the conversation.
:::

## Credits

David Sterba, Richard Russon
