---
title: Attach Dialog
description: XXX
keywords: XXX
---

(tour-attach)=
# Attach Dialog

The Attachment Selection Dialog lets you view and interact with the attachments of a received email.

<div class="term-window">
<div class="term-title">Attach Dialog</div>
<pre class="terminal">
<span >  I     1 &lt;no description&gt;                                               [multipa/mixed, 7bit, 14K] </span>
<span>  I     2 </span><span class="tree">├─&gt;</span><span>&lt;no description&gt;                                    [text/plain, 7bit, us-ascii, 0.7K] </span>
<span>  A     3 </span><span class="tree">├─&gt;</span><span>misc.md                                          [text/markdown, 7bit, us-ascii, 0.3K] </span>
<span>  A     4 </span><span class="tree">├─&gt;</span><span>welcome.md                                       [text/markdown, 7bit, us-ascii, 1.0K] </span>
<span>  A     5 </span><span class="tree">├─&gt;</span><span>goals.md                                         [text/markdown, 7bit, us-ascii, 1.9K] </span>
<span>  A     6 </span><span class="tree">├─&gt;</span><span>plurals.md                                        [text/markdown, quoted, utf-8, 2.2K] </span>
<span>  A     7 </span><span class="tree">├─&gt;</span><span>coordinating.md                                [text/markdown, quoted, us-ascii, 1.2K] </span>
<span>  A     8 </span><span class="tree">├─&gt;</span><span>power-editing.md                                 [text/markdown, 7bit, us-ascii, 2.0K] </span>
<span>  A     9 </span><span class="tree">└─&gt;</span><span>manager.txt                                          [text/plain, quoted, utf-8, 4.6K] </span>
<span>                                                                                                    </span>
<span class="status">Attachments                                                                                         </span>
<span>                                                                                                    </span>
</pre>
</div>

When reading a message that contains attachments, this dialog presents them in a hierarchical tree showing each part's MIME type, encoding, size, and filename.
You can view individual attachments using the configured mailcap handler, save them to disk, pipe them to an external command, or extract cryptographic keys.
For multipart messages, the tree structure clearly shows how the parts are nested, making it easy to navigate complex emails with many attachments.

## See Also

- [Attach Config](ref-cfg-attach)
- [Attach Functions](ref-fn-attach)
  - edit type, extract keys, ...
- [Generic Functions](ref-fn-generic)
  - **Menu:** page up/down, search, tagging, ...
  - **Global:** enter command, show log message, ...


