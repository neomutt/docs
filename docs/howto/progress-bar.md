---
title: How to Customise the Progress Bar
description: Customise NeoMutt's visual progress bar that appears during slow operations such as indexing large folders.
keywords: progress, progress bar, color, slow operations
---

# How to Customise the Progress Bar

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

The "progress" feature shows a visual progress bar on slow tasks, such as indexing a large folder over the net.

## Colors

| Name | Default Color | Description |
|------|---------------|-------------|
| `progress` | default | Visual progress bar |

## neomuttrc

```bash
# Example NeoMutt config file for the progress feature.

# The 'progress' feature provides clear visual feedback for
# slow tasks, such as indexing a large folder over the net.

# Set the color of the progress bar
# White text on a red background
color progress white red

# vim: syntax=neomuttrc
```

## See Also

- [Color command](colours.md)

## Known Bugs

None

## Credits

Rocco Rutte, Vincent Lefevre, Stefan Kuhn, Karel Zak, Richard Russon
