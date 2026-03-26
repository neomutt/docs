---
title: Different Mailbox Formats
description: Understand and choose between the four local mailbox formats — mbox, MMDF, MH, and Maildir — supported by NeoMutt
keywords: mailbox, mbox, mmdf, mh, maildir, format, mbox_type, local storage, mail format, file locking, message store, qmail, from_ line, concurrency, header caching
---

# Different Mailbox Formats

NeoMutt supports reading and writing of four different local mailbox formats: mbox, MMDF, MH and Maildir.
The mailbox type is auto detected, so there is no need to use a flag for different mailbox types.
When creating new mailboxes, NeoMutt uses the default specified with the `$mbox_type` variable.
A short description of the formats follows.

## mbox

This is a widely used mailbox format for UNIX.
All messages are stored in a single file.
Each message has a line of the form:

```
From me@ox.ac.uk Fri, 11 Apr 1997 11:44:56 PST
```

to denote the start of a new message (this is often referred to as the "From\_" line).
The mbox format requires mailbox locking, is prone to mailbox corruption with concurrently writing clients or misinterpreted From\_ lines.
Depending on the environment, new mail detection can be unreliable.
Mbox folders are fast to open and easy to archive.

## MMDF

This is a variant of the *mbox* format.
Each message is surrounded by lines containing `^A^A^A^A` (four times control-A's).
The same problems as for mbox apply (also with finding the right message separator as four control-A's may appear in message bodies).

## MH

A radical departure from *mbox* and *MMDF*, a mailbox consists of a directory and each message is stored in a separate file.
The filename indicates the message number (however, this may not correspond to the message number NeoMutt displays).
Deleted messages are renamed with a comma (`,`) prepended to the filename.
NeoMutt detects this type of mailbox by looking for either `.mh_sequences` or `.xmhcache` files (needed to distinguish normal directories from MH mailboxes).
MH is more robust with concurrent clients writing the mailbox, but still may suffer from lost flags; message corruption is less likely to occur than with mbox/mmdf.
It's usually slower to open compared to mbox/mmdf since many small files have to be read (NeoMutt provides [header caching](caching.md) to greatly speed this process up).
Depending on the environment, MH is not very disk-space efficient.

## Maildir

The newest of the mailbox formats, used by the Qmail MTA (a replacement for sendmail).
Similar to *MH*, except that it adds three subdirectories of the mailbox: *tmp*, *new* and *cur*.
Filenames for the messages are chosen in such a way they are unique, even when two programs are writing the mailbox over NFS, which means that no file locking is needed and corruption is very unlikely.
Maildir may be slower to open without caching in NeoMutt, it too is not very disk-space efficient depending on the environment.
Since no additional files are used for metadata (which is embedded in the message filenames) and Maildir is locking-free, it's easy to sync across different machines using file-level synchronization tools.
