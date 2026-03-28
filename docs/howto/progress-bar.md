---
title: Progress Bar
description: Customise the colour of NeoMutt's visual progress bar that appears during slow operations like fetching headers or indexing.
keywords: progress, progress bar, color, slow operations, indexing, fetching, color progress, theming, status indicator
---

# Progress Bar

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

<div class="term-window">
<pre class="terminal">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="progress2">Fetching message headers... 8806</span><span>/37928 (23%)                                                        </span>
</pre>
</div>

## See Also

- [Color command](colours.md)

