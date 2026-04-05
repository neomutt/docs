---
title: Certificate Dialog
description: XXX
keywords: XXX
---

(tour-certificate)=
# Certificate Dialog

The Certificate Verification Dialog lets you inspect and accept or reject an SSL/TLS certificate.

<div class="term-window">
<div class="term-title">Certificate Dialog</div>
<pre class="terminal">
<span>This certificate belongs to:                                                                        </span>
<span>   example.com                                                                                      </span>
<span>                                                                                                    </span>
<span>This certificate was issued by:                                                                     </span>
<span>   E8                                                                                               </span>
<span>   Let's Encrypt                                                                                    </span>
<span>   US                                                                                               </span>
<span>                                                                                                    </span>
<span>This certificate is valid                                                                           </span>
<span>   from Sun, 1 Mar 2026 15:00:34 UTC                                                                </span>
<span>     to Sat, 30 May 2026 15:00:33 UTC                                                               </span>
<span>                                                                                                    </span>
<span>SHA1 Fingerprint: B595 6DBF 0240 8B06 6481 3DAB 08CB EFAF 1AE1 9C6B                                 </span>
<span>SHA256 Fingerprint: F9C2 6A4E 658A 9E31 E7D6 C4F8 133A 8935                                         </span>
<span>                    F9E7 CC96 DE36 03B1 6FFE C50A EC84 0ED4                                         </span>
<span>                                                                                                    </span>
<span class="status">SSL Certificate check (certificate 1 of 1 in chain)                                                 </span>
<span>(r)eject, accept (o)nce, (a)ccept always                                                            </span>
</pre>
</div>

When NeoMutt connects to a mail server over an encrypted connection and encounters a certificate it cannot automatically verify, this dialog is displayed.
It shows the certificate's owner, issuer, validity period, and fingerprints (SHA1 and SHA256) so you can confirm the server's identity.
You can reject the certificate, accept it for the current session only, or accept it permanently so you won't be prompted again for the same certificate.

## See Also

- [Dialog Functions](ref-fn-dialog)
  - quit, exit
- [Generic Functions](ref-fn-generic)
  - **Menu:** page up/down, search, tagging, ...
  - **Global:** enter command, show log message, ...

