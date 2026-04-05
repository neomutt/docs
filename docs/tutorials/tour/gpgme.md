---
title: Gpgme Dialog
description: XXX
keywords: XXX
---

(tour-gpgme)=
# Gpgme Dialog

The GPGME Key Selection Dialog lets you choose a PGP or S/MIME key when encrypting or signing a message using the GPGME library.

<div class="term-window">
<div class="term-title">Gpgme Dialog</div>
<pre class="terminal">
<span>   1 u  4096/0x7224725C RSA  es Jim Smith (backup) &lt;jim@example.com&gt;                                </span>
<span>   2 u  4096/0x7224725C RSA  es Jim Smith (backup) &lt;jim@example.com&gt;                                </span>
<span>   3 f  4096/0x810582F5 RSA  es James Smith (flatcap) &lt;jim@example.com&gt;                             </span>
<span>   4 f  4096/0x810582F5 RSA  es James Smith (flatcap) &lt;jim@example.com&gt;                             </span>
<span >   5 f  4096/0x810582F5 RSA  es James Smith (flatcap) &lt;jim@example.com&gt;                             </span>
<span>                                                                                                    </span>
<span class="status">PGP keys matching &lt;jim@example.com&gt;                                                                 </span>
<span>                                                                                                    </span>
</pre>
</div>

When you compose a message with encryption or signing enabled and GPGME is configured as the cryptographic backend, this dialog appears to let you pick the right key.
It lists matching keys with their trust level, key ID, algorithm, capabilities (encrypt/sign), and the associated user IDs.
You can verify a key's details or view its user name before making your selection, ensuring you encrypt to the correct recipient or sign with the intended identity.

## See Also

- [Encryption Config](ref-cfg-ncrypt)
- [Pgp Functions](ref-fn-pgp)
  - verify key, view name
- [Smime Functions](ref-fn-smime)
  - verify key, view name
- [Generic Functions](ref-fn-generic)
  - **Menu:** page up/down, search, tagging, ...
  - **Global:** enter command, show log message, ...

