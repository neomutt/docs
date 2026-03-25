---
title: How to Customise the Progress Bar
description: Customise NeoMutt's visual progress bar that appears during slow operations such as indexing large folders.
keywords: progress, progress bar, color, slow operations
---

# How to Customise the Progress Bar

The "progress" feature shows a visual progress bar on slow tasks, such as indexing a large folder over the net.

## Colors

| Name       | Default Color | Description         |
|------------|---------------|---------------------|
| `progress` | default       | Visual progress bar |

## neomuttrc

```neomuttrc
# Set the color of the progress bar
# White text on a red background
color progress white red
```

## Screenshot

<div class="term-window index-preview"> <div class="term-titlebar"> <span class="blob red"></span> <span class="blob yellow"></span> <span class="blob green"></span> <span class="title">Progress</span> </div> <pre class="terminal"> <span class="normal">                                                                                                    </span> <span class="normal">                                                                                                    </span> <span class="normal progress2">Fetching message headers... 8806</span><span class="normal">/37928 (23%)                                                              </span> </pre> </div>

## See Also

- [Color command](colours.md)

