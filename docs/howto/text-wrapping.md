---
title: Text Wrapping
description: Control how NeoMutt wraps long lines in the pager, including wrap width, smart word-boundary wrapping, line markers, `format=flowed` reflowing, and tilde padding.
keywords: wrap, reflow_wrap, markers, smart_wrap, tilde, pager, line wrapping, word wrap, format=flowed, reflow
---

(how-text-wrapping)=
# Text Wrapping

NeoMutt provides several options to control how long lines are displayed in the [Pager](tour-pager).

This guide covers the wrap width, `format=flowed` reflowing, word-boundary wrapping, line continuation markers, and tilde padding.

## Variables

| Name                              | Type    | Default |
|-----------------------------------|---------|---------|
| [`$markers`](cfg-markers)         | boolean | `yes`   |
| [`$reflow_wrap`](cfg-reflow-wrap) | number  | `78`    |
| [`$smart_wrap`](cfg-smart-wrap)   | boolean | `yes`   |
| [`$tilde`](cfg-tilde)             | boolean | `no`    |
| [`$wrap`](cfg-wrap)               | number  | `0`     |

## Wrap Width (`$wrap`)

[`$wrap`](cfg-wrap) controls the column at which NeoMutt wraps lines in the pager.

- **Positive value** — wrap at exactly that column
- **Negative value** — wrap leaving that many columns of space on the right
- **Zero (default)** — wrap at the terminal width

### Example: `set wrap = 40`

Text is hard-wrapped at column 40:

<div class="term-window">
<div class="term-title">Text Wrapping</div>
<pre class="terminal">
<span>It is a truth universally acknowledged,                                         </span>
<span>that a single man in possession of a                                            </span>
<span>good fortune, must be in want of a                                              </span>
<span>wife. However little known the feelings                                         </span>
<span>or views of such a man may be on his                                            </span>
<span>first entering a neighbourhood, this                                            </span>
<span>truth is so well fixed in the minds of                                          </span>
<span>the surrounding families, that he is                                            </span>
<span>considered as the rightful property of                                          </span>
<span>some one or other of their daughters.                                           </span>
<span>         |         |         |         |         |         |         |         |</span>
<span>       10|       20|       30|       40|       50|       60|       70|       80|</span>
</pre>
</div>

### Example: `set wrap = -10`

On an 80-column terminal, text wraps at column 70, leaving 10 columns empty on the right:

<div class="term-window">
<div class="term-title">Text Wrapping</div>
<pre class="terminal">
<span>It is a truth universally acknowledged, that a single man in                    </span>
<span>possession of a good fortune, must be in want of a wife. However                </span>
<span>little known the feelings or views of such a man may be on his first            </span>
<span>entering a neighbourhood, this truth is so well fixed in the minds of           </span>
<span>the surrounding families, that he is considered as the rightful                 </span>
<span>property of some one or other of their daughters.                               </span>
<span>         |         |         |         |         |         |         |         |</span>
<span>       10|       20|       30|       40|       50|       60|       70|       80|</span>
</pre>
</div>

### Example: `set wrap = 0`

Text wraps at the full terminal width (80 columns shown):

<div class="term-window">
<div class="term-title">Text Wrapping</div>
<pre class="terminal">
<span>It is a truth universally acknowledged, that a single man in possession of a    </span>
<span>good fortune, must be in want of a wife. However little known the feelings or   </span>
<span>views of such a man may be on his first entering a neighbourhood, this truth is </span>
<span>so well fixed in the minds of the surrounding families, that he is considered   </span>
<span>as the rightful property of some one or other of their daughters.               </span>
<span>         |         |         |         |         |         |         |         |</span>
<span>       10|       20|       30|       40|       50|       60|       70|       80|</span>
</pre>
</div>

## Reflow Wrap (`$reflow_wrap`)

[`$reflow_wrap`](cfg-reflow-wrap) sets the paragraph width when reformatting `format=flowed` messages (requires [`$reflow_text`](cfg-reflow-text) to be set).

- **Positive value** — paragraph width relative to the left margin
- **Negative value** — paragraph width relative to the right margin
- **Zero** — wrap at the terminal's right margin

:::{important}
Reflowed paragraphs are still subject to `$wrap`.
If `$reflow_wrap` is wider than `$wrap`, each reflowed line will be split again by `$wrap`, producing uneven line lengths.
For example, `set reflow_wrap = 40` with `set wrap = 30` produces alternating lines of 30 and 10 characters.
:::

### Example: `set reflow_wrap = 40`

A `format=flowed` paragraph is reflowed to 40-character lines:

<div class="term-window">
<div class="term-title">Text Wrapping</div>
<pre class="terminal">
<span>It is a truth universally acknowledged,                                        </span>
<span>that a single man in possession of a                                           </span>
<span>good fortune, must be in want of a wife.                                       </span>
<span>         |         |         |         |         |         |         |         |</span>
<span>       10|       20|       30|       40|       50|       60|       70|       80|</span>
</pre>
</div>

### Example: `set reflow_wrap = 72`

The same paragraph reflowed at 72 characters:

<div class="term-window">
<div class="term-title">Text Wrapping</div>
<pre class="terminal">
<span>It is a truth universally acknowledged, that a single man in possession         </span>
<span>of a good fortune, must be in want of a wife. However little known the          </span>
<span>feelings or views of such a man may be on his first entering a                  </span>
<span>neighbourhood, this truth is so well fixed in the minds of the                  </span>
<span>surrounding families, that he is considered as the rightful property of         </span>
<span>some one or other of their daughters.                                           </span>
<span>         |         |         |         |         |         |         |         |</span>
<span>       10|       20|       30|       40|       50|       60|       70|       80|</span>
</pre>
</div>

## Smart Wrap (`$smart_wrap`)

[`$smart_wrap`](cfg-smart-wrap) controls whether long lines wrap at a word boundary or at the screen edge.
It is enabled by default.

### Example: `set smart_wrap = yes` (default)

The line breaks at a space between words:

<div class="term-window">
<div class="term-title">Text Wrapping</div>
<pre class="terminal">
<span>It is a truth universally acknowledged, that a single man in possession of a    </span>
<span>good fortune, must be in want of a wife. However little known the feelings or   </span>
<span>views of such a man may be on his first entering a neighbourhood, this truth is </span>
<span>so well fixed in the minds of the surrounding families, that he is considered as</span>
<span>the rightful property of some one or other of their daughters.                  </span>
</pre>
</div>

### Example: `set smart_wrap = no`

The line breaks exactly at the screen edge, splitting words mid-character:

<div class="term-window">
<div class="term-title">Text Wrapping</div>
<pre class="terminal">
<span>It is a truth universally acknowledged, that a single man in possession of a goo</span>
<span>d fortune, must be in want of a wife. However little known the feelings or views</span>
<span>of such a man may be on his first entering a neighbourhood, this truth is so wel</span>
<span>l fixed in the minds of the surrounding families, that he is considered as the r</span>
<span>ightful property of some one or other of their daughters.                       </span>
</pre>
</div>

## Markers (`$markers`)

[`$markers`](cfg-markers) controls whether a `+` character is shown at the start of continuation lines when a line wraps in the pager.
It is enabled by default.

### Example: `set markers = yes` (default)

Wrapped lines are prefixed with `+`:

<div class="term-window">
<div class="term-title">Text Wrapping</div>
<pre class="terminal">
<span>It is a truth universally acknowledged, that a single man in possession of a    </span>
<span><span class="markers">+</span>good fortune, must be in want of a wife. However little known the feelings or  </span>
<span><span class="markers">+</span>views of such a man may be on his first entering a neighbourhood, this truth   </span>
<span><span class="markers">+</span>is so well fixed in the minds of the surrounding families, that he is          </span>
<span><span class="markers">+</span>considered as the rightful property of some one or other of their daughters.   </span>
</pre>
</div>

### Example: `set markers = no`

No prefix on continuation lines:

<div class="term-window">
<div class="term-title">Text Wrapping</div>
<pre class="terminal">
<span>It is a truth universally acknowledged, that a single man in possession of a    </span>
<span>good fortune, must be in want of a wife. However little known the feelings or   </span>
<span>views of such a man may be on his first entering a neighbourhood, this truth    </span>
<span>is so well fixed in the minds of the surrounding families, that he is           </span>
<span>considered as the rightful property of some one or other of their daughters.    </span>
</pre>
</div>


:::{tip}
`$markers` and `$smart_wrap` work together.
A common combination is `set smart_wrap = yes` with `set markers = no` for clean word-wrapped output without visual clutter.
:::

## Tilde (`$tilde`)

[`$tilde`](cfg-tilde) pads blank lines at the bottom of the pager with `~` characters, similar to Vim's display of lines past the end of a file.
It is disabled by default.

### Example: `set tilde = no` (default)

After the message ends, remaining screen lines are blank:

<div class="term-window">
<div class="term-title">Text Wrapping</div>
<pre class="terminal">
<span>It is a truth universally acknowledged, that a single man in possession of a    </span>
<span>good fortune, must be in want of a wife.                                        </span>
<span>                                                                                </span>
<span>                                                                                </span>
<span>                                                                                </span>
</pre>
</div>

### Example: `set tilde = yes`

Blank lines below the message are filled with `~`:

<div class="term-window">
<div class="term-title">Text Wrapping</div>
<pre class="terminal">
<span>It is a truth universally acknowledged, that a single man in possession of a    </span>
<span>good fortune, must be in want of a wife.                                        </span>
<span><span class="tilde">~</span>                                                                               </span>
<span><span class="tilde">~</span>                                                                               </span>
<span><span class="tilde">~</span>                                                                               </span>
</pre>
</div>

## neomuttrc

```neomuttrc
# Example NeoMutt config file for text wrapping.

# Wrap at 80 columns (the default wraps at terminal width)
set wrap = 0

# Reflow `format=flowed` paragraphs at 72 characters
set reflow_text = yes
set reflow_wrap = 72

# Wrap long lines at word boundaries
set smart_wrap = yes

# Don't show '+' markers on wrapped lines
set markers = no

# Pad blank lines below messages with '~'
set tilde = yes

# vim: filetype=neomuttrc
```

## See Also

- {doc}`format-flowed` — composing and displaying `format=flowed` messages
- {doc}`skip-quoted` — managing quoted text display in the pager
