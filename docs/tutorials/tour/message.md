---
title: Message Window
description: XXX
keywords: XXX
---

(tour-message)=
# Message Window

overview...

<div class="term-window">
<div class="term-title">Message Window</div>
<pre class="terminal">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">Status Bar                                                                                          </span>
<span>Message Window                                                                                      </span>
</pre>
</div>

- [Editor Functions](fn-editor)
  - backspace, forward word, ...

## Enter Command

Function `<enter-command>` (Key: {kbd}`:`)

<div class="term-window">
<pre class="terminal">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">:</span><span>echo "hello"                                                                                       </span>
</pre>
</div>

## Yes / No / Help

<div class="term-window">
<pre class="terminal">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">Exit NeoMutt without saving? ([yes]/no):</span><span>                                                            </span>
</pre>
</div>

<div class="term-window">
<pre class="terminal">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">Quit NeoMutt? ([no]/yes/?): </span><span>                                                                        </span>
</pre>
</div>

<div class="term-window">
<pre class="terminal">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span>$quit - Prompt before exiting NeoMutt                                                               </span>
<span>https://neomutt.org/guide/reference#quit                                                            </span>
<span class="prompt">Quit NeoMutt? ([no]/yes/?): </span><span>                                                                        </span>
</pre>
</div>

## Multi-choice



<div class="term-window">
<pre class="terminal">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">PGP (e)ncrypt, (s)ign, sign (a)s, (b)oth, s/(m)ime or (c)lear? </span><span>                                     </span>
</pre>
</div>

<div class="term-window">
<pre class="terminal">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">PGP </span><span class="prompt options">e</span><span class="prompt">ncrypt, </span><span class="prompt options">s</span><span class="prompt">ign, sign </span><span class="prompt options">a</span><span class="prompt">s, </span><span class="prompt options">b</span><span class="prompt">oth, s/</span><span class="prompt options">m</span><span class="prompt">ime or </span><span class="prompt options">c</span><span class="prompt">lear?</span><span>                                                  </span>
</pre>
</div>

## Custom Flags

<div class="term-window">
<pre class="terminal">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">Set flag? (D/N/O/r/*/!):</span><span>                                                                            </span>
</pre>
</div>

## Free Form Question

<div class="term-window">
<pre class="terminal">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">Search for: </span><span>                                                                                        </span>
</pre>
</div>

## Progress Bar

<div class="term-window">
<pre class="terminal">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="progress2">Fetching message headers... 8806</span><span>/37928 (23%)                                                        </span>
</pre>
</div>

## What Key?

```
:exec what-key
```

<div class="term-window">
<pre class="terminal">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span>Char = f, Octal = 146, Decimal = 102                                                                </span>
<span>Enter keys (^G to abort):                                                                           </span>
</pre>
</div>

