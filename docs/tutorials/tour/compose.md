---
title: Compose Dialog
description: XXX
keywords: XXX
---

(tour-compose)=
# Compose Dialog

The Compose Dialog is the final review screen before sending an email.

<div class="term-window">
<div class="term-title">Compose Dialog</div>
<pre class="terminal">
<span class="status">q:Quit  d:Del  u:Undel  m:Mail  r:Reply  ?:Help                                                     </span>
<span class="header">        From: </span><span>Ryan Reynolds &lt;ryanr@yew.com&gt;                                                         </span>
<span class="header">          To: </span><span>Diane Wiest &lt;dianew@apple.com&gt;, Glenn Close &lt;glennc@kumquat.com&gt;                      </span>
<span class="header">          Cc: </span><span>Jamie Foxx &lt;jamief@olive.com&gt;                                                         </span>
<span class="header">         Bcc: </span><span>                                                                                      </span>
<span class="header">     Subject: </span><span>Party in London                                                                       </span>
<span class="header">    Reply-To: </span><span>                                                                                      </span>
<span class="header">         Fcc: </span><span>                                                                                      </span>
<span class="header">    Security: </span><span class="sign">Sign</span><span> (PGP/MIME)                                                                       </span>
<span class="header">     Sign as: </span><span>0x54BE8DECB4041D988854E3F2EA0E60D133D46E38                                            </span>
<span class="status">-- Attachments                                                                                      </span>
<span>- I     1 /tmp/mutt/neomutt-user-12345678                         [text/plain, 7bit, us-ascii, 0.5K]</span>
<span>  A     2 ~/dress-code.md                                         [text/markdown, 8bit, utf-8, 3.6K]</span>
<span class="status">-- Preview                                                                                          </span>
<span>Hey guys!                                                                                           </span>
<span>                                                                                                    </span>
<span>I've having a small party and you're all invited.                                                   </span>
<span>Don't forget to bring your Oscars!                                                                  </span>
<span>                                                                                                    </span>
<span>RR                                                                                                  </span>
<span>                                                                                                    </span>
<span class="status">-- NeoMutt: Compose  [Approx. msg size: 4.1K   Atts: 2]---------------------------------------------</span>
<span>                                                                                                    </span>
</pre>
</div>

This is where you edit the message envelope — the From, To, Cc, Bcc, Subject, Reply-To, and Fcc fields — and manage the list of attachments.
You can add, remove, and reorder attachments, edit the message body, and configure security settings such as PGP or S/MIME signing and encryption.
A preview pane at the bottom shows the message body, and a status bar displays the approximate message size and attachment count.
When everything looks right, you send the message from this dialog.

## See Also

- [Compose Config](ref-cfg-compose)
- [Compose Functions](ref-fn-compose)
  - **Attach:** attach file, attach message, ...
  - **Compose:** edit message, send message, ...
  - **Envelope:** edit from, edit subject, ...
  - **Preview:** page down, page up
- [Generic Functions](ref-fn-generic)
  - **Menu:** page up/down, search, tagging, ...
  - **Global:** enter command, show log message, ...

