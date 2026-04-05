---
title: Browser Dialog
description: XXX
keywords: XXX
---

(tour-browser)=
# Browser Dialog

The Browser Dialog lets you navigate the file system or IMAP server to select a mailbox or file.

<div class="term-window">
<div class="term-title">Browser Dialog</div>
<pre class="terminal">
<span> 1     drwxr-xr-x  1 mutt     mutt           0K Mar 27 11:50 ../                                    </span>
<span> 2     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:46 address/                               </span>
<span> 3     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:45 alias/                                 </span>
<span> 4     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:46 attach/                                </span>
<span> 5     -rw-r--r--  1 mutt     mutt          16K Mar 11 15:00 AUTHORS.md                             </span>
<span> 6     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:45 autocrypt/                             </span>
<span > 7     -rw-r--r--  1 mutt     mutt          40K Mar 28 10:33 auto.def                               </span>
<span> 8     drwxr-xr-x  1 mutt     mutt           0K Mar 11 15:00 autosetup/                             </span>
<span> 9     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:46 bcache/                                </span>
<span>10     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:45 browser/                               </span>
<span>11     -rw-------  1 mutt     mutt          10K Mar 28 14:02 browser-shot.log0                      </span>
<span>12     -rw-r--r--  1 mutt     mutt         122K Mar 11 15:00 ChangeLog.md                           </span>
<span>13     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:46 cli/                                   </span>
<span>14     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:46 color/                                 </span>
<span>15     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:46 commands/                              </span>
<span>16     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:45 complete/                              </span>
<span>17     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:45 compmbox/                              </span>
<span>18     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:45 compose/                               </span>
<span>19     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:46 compress/                              </span>
<span>20     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:46 config/                                </span>
<span>21     -rw-r--r--  1 mutt     mutt         4.6K Mar 28 13:45 config.h                               </span>
<span>22     -rw-r--r--  1 mutt     mutt          16K Mar 28 13:45 config.log                             </span>
<span class=" status">Directory [~/work/screenshot], File mask: !^\.[^.]                                                  </span>
<span>                                                                                                    </span>
</pre>
</div>

This dialog is used whenever NeoMutt needs you to choose a file or mailbox — for example, when opening a different mailbox, saving an attachment, or selecting a file to attach to a message.
It shows a directory listing with file permissions, owner, size, and modification date, and supports navigating into subdirectories, going to the parent directory, and filtering entries with a file mask.
When used with IMAP, it displays the folder hierarchy on the remote server, letting you subscribe or unsubscribe to folders.

## See Also

- [Browser Config](ref-cfg-browser)
- [Browser Functions](ref-fn-browser)
  - change dir, descend dir, goto parent, ...
- [Generic Functions](ref-fn-generic)
  - **Menu:** page up/down, search, tagging, ...
  - **Global:** enter command, show log message, ...

