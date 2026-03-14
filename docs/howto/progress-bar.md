---
title: How to Customise the Progress Bar
description: Customise NeoMutt's visual progress bar that appears during slow operations such as indexing large folders.
keywords: progress, progress bar, color, slow operations
---

# How to Customise the Progress Bar

## Screenshot

<div class="term-window index-preview">
  <div class="term-titlebar">
    <span class="blob red"></span>
    <span class="blob yellow"></span>
    <span class="blob green"></span>
    <span class="title">Compose</span>
  </div>
  <pre class="terminal">
<span class="status">q:Quit  d:Del  u:Undel  m:Mail  r:Reply  ?:Help                                                     </span>
<span class="header">        From: </span><span class="normal">Ryan Reynolds &lt;ryanr@yew.com&gt;                                                         </span>
<span class="header">          To: </span><span class="normal">Diane Wiest &lt;dianew@apple.com&gt;, Glenn Close &lt;glennc@kumquat.com&gt;          </span>
<span class="header">          Cc: </span><span class="normal">Jamie Foxx &lt;jamief@olive.com&gt;                                                   </span>
<span class="header">         Bcc: </span><span class="normal">                                                                                      </span>
<span class="header">     Subject: </span><span class="normal">Party in London                                                                       </span>
<span class="header">    Reply-To: </span><span class="normal">                                                                                      </span>
<span class="header">         Fcc: </span><span class="normal">                                                                                      </span>
<span class="header">    Security: </span><span class="sign">Sign</span><span class="normal"> (PGP/MIME)                                                                       </span>
<span class="header">     Sign as: </span><span class="normal">0x54BE8DECB4041D988854E3F2EA0E60D133D46E38                                            </span>
<span class="status">-- Attachments                                                                                      </span>
<span class="normal">- I     1 /tmp/mutt/neomutt-user-12345678                         [text/plain, 7bit, us-ascii, 0.5K]</span>
<span class="normal">  A     2 ~/dress-code.md                                         [text/markdown, 8bit, utf-8, 3.6K]</span>
<span class="status">-- Preview                                                                                          </span>
<span class="normal">Hey guys!                                                                                           </span>
<span class="normal">                                                                                                    </span>
<span class="normal">I've having a small party and you're all invited.                                                   </span>
<span class="normal">Don't forget to bring your Oscars!                                                                  </span>
<span class="normal">                                                                                                    </span>
<span class="normal">RR                                                                                                  </span>
<span class="normal">                                                                                                    </span>
<span class="status">-- NeoMutt: Compose  [Approx. msg size: 4.1K   Atts: 2]---------------------------------------------</span>
<span class="normal">                                                                                                    </span>
</pre>
</div>

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

```neomuttrc
# Example NeoMutt config file for the progress feature.

# The 'progress' feature provides clear visual feedback for
# slow tasks, such as indexing a large folder over the net.

# Set the color of the progress bar
# White text on a red background
color progress white red

# vim: filetype=neomuttrc
```

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Progress bar during folder indexing

**Description:** NeoMutt displaying the visual progress bar at the bottom of the screen while indexing a large mailbox — the bar is partially filled (e.g. 60%) with white text on a red background, showing the operation description and percentage complete.

**Highlights:** The progress bar filling from left to right across the message bar area, with the colour (white on red) making it clearly visible during a slow operation.
:::

## See Also

- [Color command](colours.md)

## Known Bugs

None

## Credits

Rocco Rutte, Vincent Lefevre, Stefan Kuhn, Karel Zak, Richard Russon
