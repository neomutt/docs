---
title: Smime Dialog
description: XXX
keywords: XXX
---

(tour-smime)=
# Smime Dialog

The S/MIME Key Selection Dialog lets you choose an S/MIME certificate when encrypting or signing a message.

<div class="term-window">
<div class="term-title">Smime Dialog</div>
<pre class="terminal">
<span >0x1A2B3C4D5E6F es Verified   langstroth@langstroth.com           Personal 2025                      </span>
<span>0x2B3C4D5E6F7A es Trusted    l.langstroth@hivemail.org           Work Certificate                   </span>
<span>0x3C4D5E6F7A8B e- Unverified langstroth.bee@apiary.net           Apiary Systems                     </span>
<span>0x4D5E6F7A8B9C -s Expired    rev.langstroth@phila.edu            Old University Key                 </span>
<span>0x5E6F7A8B9C0D es Unknown    langstroth@beekeepers-assoc.org     Association Key                    </span>
<span>0x6F7A8B9C0D1E -- Revoked    ll1851@historical-mail.com          Legacy Key                         </span>
<span>0x7A8B9C0D1E2F es Verified   lorenzo.langstroth@gmail.com        Gmail Key 2024                     </span>
<span>0x8B9C0D1E2F3A es Invalid    langstroth@expired-domain.com       Defunct Org                        </span>
<span>                                                                                                    </span>
<span class="status">S/MIME certificates matching "langstroth@langstroth.com"                                            </span>
<span>                                                                                                    </span>
</pre>
</div>

When you send a message with S/MIME security enabled and multiple certificates match a recipient's address, this dialog lists them so you can pick the right one.
Each entry shows the certificate's key ID, capabilities (encrypt/sign), verification status (Verified, Trusted, Expired, Revoked, etc.), email address, and a label.
This lets you confirm the certificate's validity and choose the correct identity before securing your message.

## See Also

- [Encryption Config](ref-cfg-ncrypt)
- [Smime Functions](ref-fn-smime)
  - verify key, view name
- [Generic Functions](ref-fn-generic)
  - **Menu:** page up/down, search, tagging, ...
  - **Global:** enter command, show log message, ...

