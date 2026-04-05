---
title: Pgp Dialog
description: XXX
keywords: XXX
---

(tour-pgp)=
# Pgp Dialog

The PGP Key Selection Dialog lets you choose a PGP key when encrypting or signing a message using NeoMutt's classic (non-GPGME) PGP backend.

<div class="term-window">
<div class="term-title">Pgp Dialog</div>
<pre class="terminal">
<span>   1 +  4096/0x810582F5 RSA  es                                                                     </span>
<span>   2 +  4096/0x810582F5 RSA  es                                                                     </span>
<span>   3 +  4096/0x810582F5 RSA  es                                                                     </span>
<span>   4 +  4096/0x7224725C RSA  es                                                                     </span>
<span>   5 +  4096/0x7224725C RSA  es                                                                     </span>
<span>   6 +  4096/0x7224725C RSA  es Jim Smith (backup) &lt;jim@example.com&gt;                                </span>
<span >   7 +  4096/0x7224725C RSA  es Jim Smith (backup) &lt;jim@example.com&gt;                                </span>
<span>   8 +  4096/0x810582F5 RSA  es James Smith (flatcap) &lt;jim@example.com&gt;                             </span>
<span>   9 +  4096/0x810582F5 RSA  es James Smith (flatcap) &lt;jim@example.com&gt;                             </span>
<span>  10 +  4096/0x810582F5 RSA  es James Smith (flatcap) &lt;jim@example.com&gt;                             </span>
<span>                                                                                                    </span>
<span>                                                                                                    </span>
<span class="status">PGP keys matching &lt;jim@example.com&gt;                                                                 </span>
<span>                                                                                                    </span>
</pre>
</div>

When you send an encrypted or signed message and NeoMutt's built-in PGP support finds multiple matching keys for a recipient, this dialog appears so you can pick the correct one.
Each entry shows the key's trust level, key ID, algorithm, and capabilities (encrypt/sign), along with the associated user ID when available.
You can verify a key's details before selecting it, ensuring the message is secured with the right key.

## See Also

- [Encryption Config](ref-cfg-ncrypt)
- [Pgp Functions](ref-fn-pgp)
  - verify key, view name
- [Generic Functions](ref-fn-generic)
  - **Menu:** page up/down, search, tagging, ...
  - **Global:** enter command, show log message, ...

