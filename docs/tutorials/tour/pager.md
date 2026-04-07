---
title: Pager Dialog
description: NeoMutt's message-reading view for scrolling, searching, and acting on the current email.
keywords: pager, reader, message view, search, quoted text, reply, save, attachments
---

(tour-pager)=
# Pager Dialog

## Introduction -- Where am I?

The Pager Dialog is NeoMutt's message-reading view.
It shows one email in detail and lets you read the headers and body without losing access to message-level actions.
Depending on your layout, it may appear as a split view underneath the index or as the main focus of the screen.

<div class="term-window">
<div class="term-title">Index / Pager Dialog</div>
<pre class="terminal">
<span class="index index_date">25-Feb</span><span class="index"> </span><span class="index index_flags">   </span><span class="index"> </span><span class="index index_author">Ben Stiller              </span><span class="index">  </span><span class="index tree">    └─&gt;</span><span class="index index_subject">Re: The Princess Bride</span><span class="index">                           (</span><span class="index index_size">0.5K</span><span class="index">)</span>
<span class="index index_date">02-Mar</span><span class="index"> </span><span class="index index_flags">   </span><span class="index"> </span><span class="index index_author">Paul Rudd                </span><span class="index">  </span><span class="index tree">      └─&gt;</span><span class="index">                                               (</span><span class="index index_size">0.6K</span><span class="index">)</span>
<span class="index index_date">04-Mar</span><span class="index"> </span><span class="index index_flags">   </span><span class="index"> </span><span class="index index_author">Billy Crystal            </span><span class="index">  </span><span class="index tree">        └─&gt;</span><span class="index">                                             (</span><span class="index index_size">0.6K</span><span class="index">)</span>
<span class="index index_date">02-Mar</span><span class="index"> </span><span class="index index_flags">   </span><span class="index"> </span><span class="index index_author">Jodie Foster             </span><span class="index">  </span><span class="index index_subject">The Silence of the Lambs</span><span class="index">                                (</span><span class="index index_size">0.5K</span><span class="index">)</span>
<span class="index index_date">04-Mar</span><span class="index"> </span><span class="index index_flags">   </span><span class="index"> </span><span class="index index_author">Anthony Hopkins          </span><span class="index">  </span><span class="index tree">└─&gt;</span><span class="index">                                                     (</span><span class="index index_size">0.9K</span><span class="index">)</span>
<span class="index index_date">06-Mar</span><span class="index"> </span><span class="index index_flags">   </span><span class="index"> </span><span class="index index_author">Jodie Foster             </span><span class="index">  </span><span class="index tree">  └─&gt;</span><span class="index">                                                   (</span><span class="index index_size">0.7K</span><span class="index">)</span>
<span class="index index_date">07-Mar</span><span class="index"> </span><span class="index index_flags">   </span><span class="index"> </span><span class="index index_author">Anthony Hopkins          </span><span class="index">  </span><span class="index tree">    └─&gt;</span><span class="index">                                                 (</span><span class="index index_size">0.6K</span><span class="index">)</span>
<span class="index index_date">09-Mar</span><span class="index"> </span><span class="index index_flags">   </span><span class="index"> </span><span class="index index_author">Rami Malek               </span><span class="index">  </span><span class="index index_subject">Mr. Robot</span><span class="index">                                               (</span><span class="index index_size">0.6K</span><span class="index">)</span>
<span class="index index_date">10-Mar</span><span class="index"> </span><span class="index index_flags">   </span><span class="index"> </span><span class="index index_author">Natasha Lyonne           </span><span class="index">  </span><span class="index tree">└─&gt;</span><span class="index">                                                     (</span><span class="index index_size">0.6K</span><span class="index">)</span>
<span class="index index_date">12-Mar</span><span class="index"> </span><span class="index index_flags">   </span><span class="index"> </span><span class="index index_author">Elisabeth Moss           </span><span class="index">  </span><span class="index tree">  └─&gt;</span><span class="index">                                                   (</span><span class="index index_size">0.9K</span><span class="index">)</span>
<span class="status">-- ~/mail/conversation [Msgs:48/48 50K]   (last-date/date)                                   (87%)  </span>
<span class="hdrdefault">Date: Mon, 02 Mar 2026 13:00:00 GMT</span><span>                                                                 </span>
<span class="header">From: Jodie Foster &lt;jf@tangerine.com&gt;</span><span>                                                               </span>
<span class="hdrdefault">To: Anthony Hopkins &lt;ah@cherry.com&gt;</span><span>                                                                 </span>
<span class="header">Subject: The Silence of the Lambs</span><span>                                                                   </span>
<span>                                                                                                    </span>
<span>Anthony,                                                                                            </span>
<span>                                                                                                    </span>
<span>It's been over thirty years since The Silence of the Lambs and I still                              </span>
<span>get asked about it every single week. The film refuses to age.                                      </span>
<span>                                                                                                    </span>
<span>I was thinking about our first scene together — Clarice walking down                                </span>
<span class="status">-   - 36/48: Jodie Foster           The Silence of the Lambs                                -- (65%)</span>
<span>                                                                                                    </span>
</pre>
</div>

## What am I looking at?

- The header area shows the important message headers such as Date, From, To, and Subject.
- The body area displays the message text, quoted replies, signatures, and any ANSI colour sequences that NeoMutt renders.
- The pager status line shows which message you are reading, where you are in the mailbox, and how far through the message you have scrolled.
- In split mode, the [Index Dialog](index2.md) remains visible above the pager so you can keep message context while reading.
- The [Sidebar Panel](sidebar.md) and [Message Window](message.md) can still appear around the pager when enabled.

## What can I do?

- Scroll by line, half-page, page, or jump straight to the top, bottom, headers, or first unquoted text.
- Search inside the current message, repeat searches, and toggle quoted-text visibility.
- Reply, group-reply, list-reply, forward, bounce, save, print, pipe, label, or delete the message without going back to the index first.
- Move directly to the next or previous message, thread, subthread, or unread message while staying in reading mode.
- Open the [Attach Dialog](attach.md), create an alias from the sender, or inspect the raw message.
- Full reference: [Pager Functions](ref-fn-pager), [Index Functions](ref-fn-index), [Sidebar Functions](ref-fn-sidebar), [Generic Functions](ref-fn-generic).

## Where can I go next?

- `q` or `x` returns to the [Index Dialog](index2.md).
- `<reply>`, `<group-reply>`, `<list-reply>`, `<forward-message>`, `<mail>`, and `<bounce-message>` open the [Compose Dialog](compose.md).
- `<view-attachments>` opens the [Attach Dialog](attach.md).
- `?`, `<show-log-messages>`, and `V` open one of the [Simple Pagers](simple.md).
- `:` and `/` use the [Message Window](message.md) for commands and searches.
- Many mailbox-changing functions forwarded from the index can take you to the [Browser Dialog](browser.md) or another mailbox.

## Where did I come from?

- You usually arrive from the [Index Dialog](index2.md) via `<display-message>`.
- If you stay inside the pager and move to the next or previous message, you are still following the same index mailbox context.
- Some workflows return here after raw-message viewing or after dismissing short-lived prompts in the [Message Window](message.md).

## How do I configure this?

- Start with [Pager Config](ref-cfg-pager) and [General Config](ref-cfg-general).
- Common options include [`$pager_format`](cfg-pager-format), [`$pager_index_lines`](cfg-pager-index-lines), [`$smart_wrap`](cfg-smart-wrap), [`$markers`](cfg-markers), [`$quote_regex`](cfg-quote-regex), [`$header`](cfg-header), and [`$weed`](cfg-weed).
- Header display can be shaped with [`:ignore`](cmd-ignore), [`:unignore`](cmd-unignore), [`:header-order`](cmd-header-order), and [`:unheader-order`](cmd-unheader-order).
- Colours come from [Colour Objects](ref-colors), especially `header`, `hdrdefault`, `body`, `quoted0` through `quoted9`, `signature`, `search`, `markers`, `tilde`, `tree`, and `status`.
