---
title: Pager Read Delay
description: Configure the pager to preview messages without immediately marking them as read using a time-based delay.
keywords: pager, read delay, preview, pager_read_delay, new message, mark read, unread, pager_index_lines, message status, new flag
since: 2021-06-16
---

# Pager Read Delay 🔥

## Support

**Since:** NeoMutt 2021-06-16

## Introduction

The "Pager Read Delay" feature adds a new config option to allow the pager to operate in a preview mode.
A new message is not marked as read merely because the pager opened it, but only after the pager remains on the message for a given length of time.

## Functions

The "Pager Read Delay" feature adds no new functions to NeoMutt.
Existing pager functions for navigating to a different message now check whether to mark a message as read.

## Variables

The "Pager Read Delay" feature adds one new config option, `$pager_read_delay`, which is an integer for how many seconds the pager must remain on a given message before marking it as read.
The variable defaults to 0 for the original behavior of marking a message as read the moment the pager visits it.

## neomuttrc

```neomuttrc
# Example NeoMutt config file for the pager-read-delay feature.

# Stay at least 5 seconds on a message before the pager marks it as read
set pager_read_delay = 5

# vim: filetype=neomuttrc
```

## Known Bugs

When `$pager_index_lines` is non-zero, the "N" status indicator from the `%Z` expando of {ref}`$index_format <cfg-index-format>` does not actively reflect the current new/read status of the message.

## Credits

Eric Blake
