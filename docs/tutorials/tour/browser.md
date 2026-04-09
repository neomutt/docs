---
title: Browser Dialog
description: The file and mailbox browser used to choose folders, files, and remote mailboxes in NeoMutt.
keywords: browser, file chooser, mailbox browser, imap browser, folder, mask, subscribe
---

(tour-browser)=
# Browser Dialog

## Introduction -- Where am I?

The Browser Dialog is NeoMutt's file and mailbox chooser.
It appears whenever NeoMutt needs you to pick a mailbox, a folder on disk, or a file to attach, save, or inspect.
Depending on the context, it behaves like a local file browser, an IMAP folder browser, or an NNTP/remote mailbox list.

<div class="term-window">
<div class="term-title">Browser Dialog</div>
<pre class="terminal" role="img" aria-label="Screenshot of NeoMutt's Browser Dialog showing a directory listing with file permissions, sizes, dates, and names, plus a status line with the current directory path and file mask.">
<span> 1     drwxr-xr-x  1 mutt     mutt           0K Mar 27 11:50 ../                                    </span>
<span> 2     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:46 address/                               </span>
<span> 3     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:45 alias/                                 </span>
<span> 4     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:46 attach/                                </span>
<span> 5     -rw-r--r--  1 mutt     mutt          16K Mar 11 15:00 AUTHORS.md                             </span>
<span> 6     drwxr-xr-x  1 mutt     mutt           0K Mar 28 13:45 autocrypt/                             </span>
<span> 7     -rw-r--r--  1 mutt     mutt          40K Mar 28 10:33 auto.def                               </span>
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
<span class="status">Directory [~/work/screenshot], File mask: !^\.[^.]                                                  </span>
<span>                                                                                                    </span>
</pre>
</div>

## What am I looking at?

- The main list shows files, directories, or mailboxes, along with metadata such as permissions, owner, size, and modification date where available.
- The highlighted row is the entry that will be opened, attached, or selected.
- The status line shows the current directory or mailbox root and the active file mask.
- On IMAP or NNTP backends, the list represents remote mailboxes rather than local files.
- Prompts for masks, paths, and completion come through the [Message Window](message.md).

## What can I do?

- Move through directories, descend into the current directory, and go back to the parent.
- Filter the listing with a file mask, switch between mailbox-only and all-file views, and sort the results.
- Open the selected mailbox or choose the selected file for the calling action.
- Subscribe, unsubscribe, create, rename, or delete remote mailboxes where the backend supports it.
- Inspect the currently selected path before choosing it.
- Full reference: [Browser Functions](menu-browser), [Generic Functions](menu-generic).

## Where can I go next?

- Selecting a mailbox opens the [Index Dialog](index2.md).
- Selecting a file returns to the caller, such as the [Compose Dialog](compose.md) for attachments or the [Attach Dialog](attach.md) for saving.
- {kbd}`q` cancels and returns to the dialog or prompt that opened the browser.
- Prompts that feed the browser continue in the [Message Window](message.md).

## Where did I come from?

- Startup with `-y` or `-G` can bring you here first.
- The [Index Dialog](index2.md) opens the browser when you change folders and ask for browsing.
- The [Compose Dialog](compose.md) opens it when choosing files to attach or an Fcc folder.
- Any filename or mailbox prompt can drop into the browser when you press {kbd}`?` or trigger completion.

## How do I configure this?

- Start with [Browser Config](ref-cfg-browser), [Conn Options](ref-cfg-conn), and [General Config](ref-cfg-general).
- Common options include [`$browser_sort`](cfg-browser-sort), [`$browser_sort_dirs_first`](cfg-browser-sort-dirs-first), [`$folder_format`](cfg-folder-format), [`$mailbox_folder_format`](cfg-mailbox-folder-format), [`$mask`](cfg-mask), [`$show_only_unread`](cfg-show-only-unread), and [`$folder`](cfg-folder).
- Useful commands include [`:cd`](cmd-cd), [`:mailboxes`](cmd-mailboxes), [`:named-mailboxes`](cmd-named-mailboxes), [`:subscribe-to`](cmd-subscribe-to), and [`:unsubscribe-from`](cmd-unsubscribe-from).
- Colours come from [Colour Objects](ref-colors), especially `indicator`, `status`, `message`, `warning`, and `normal`.
