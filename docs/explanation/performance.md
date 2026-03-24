---
title: Understanding Performance Tuning
description: How to optimize NeoMutt performance for reading mailboxes, remote folders, and searching
keywords: [performance, tuning, header cache, body cache, search, imap, maildir]
diataxis_type: explanation
---

# Understanding Performance Tuning

## Reading and Writing Mailboxes

NeoMutt's performance when reading mailboxes can be improved in two ways:

1. For remote folders (IMAP and POP) as well as folders using one-file-per-message storage
   (Maildir and MH), NeoMutt's performance can be greatly improved using header caching,
   using a single database per folder.

2. NeoMutt provides the `$read_inc` and `$write_inc` variables to specify at which rate to
   update progress counters. If these values are too low, NeoMutt may spend more time on
   updating the progress counter than it spends on actually reading/writing folders.

   For example, when opening a maildir folder with a few thousand messages, the default
   value for `$read_inc` may be too low. It can be tuned on a folder-basis using
   `folder-hook`s:

   ```
   # use very high $read_inc to speed up reading hcache'd maildirs
   folder-hook . 'set read_inc=1000'
   # use lower value for reading slower remote IMAP folders
   folder-hook ^imap 'set read_inc=100'
   # use even lower value for reading even slower remote POP folders
   folder-hook ^pop 'set read_inc=1'
   ```

These settings work on a per-message basis. However, as messages may greatly differ in size
and certain operations are much faster than others, even per-folder settings of the
increment variables may not be desirable as they produce either too few or too many progress
updates. Thus, NeoMutt allows limiting the number of progress updates per second it'll
actually send to the terminal using the `$time_inc` variable.

## Reading Messages from Remote Folders

Reading messages from remote folders such as IMAP and POP can be slow especially for large
mailboxes since NeoMutt only caches a very limited number of recently viewed messages
(usually 10) per session (so that it will be gone for the next session.)

To improve performance and permanently cache whole messages and headers, please refer to
body caching and header caching for details.

Additionally, it may be worth trying some of NeoMutt's experimental features.
`$imap_qresync` (which requires header caching) can provide a huge speed boost opening
mailboxes if your IMAP server supports it. `$imap_deflate` enables compression, which can
also noticeably reduce download time for large mailboxes and messages.

## Searching and Limiting

When searching mailboxes either via a search or a limit action, for some patterns NeoMutt
distinguishes between regular expression and string searches. For regular expressions,
patterns are prefixed with "~" and with "=" for string searches.

Even though a regular expression search is fast, it's several times slower than a pure
string search which is noticeable especially on large folders. As a consequence, a string
search should be used instead of a regular expression search if the user already knows
enough about the search pattern.

For example, when limiting a large folder to all messages sent to or by an author, it's
much faster to search for the initial part of an e-mail address via `=Luser@` instead of
`~Luser@`. This is especially true for searching message bodies since a larger amount of
input has to be searched.

As for regular expressions, a lower case string search pattern makes NeoMutt perform a
case-insensitive search except for IMAP (because for IMAP NeoMutt performs server-side
searches which don't support case-insensitivity).
