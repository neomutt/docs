---
title: Multiple Fcc
description: Save copies of outgoing messages to multiple folders using edit-fcc or fcc-hook in NeoMutt
keywords: fcc, multiple copies, outgoing mail, record, fcc-hook, edit-fcc, compose menu, sent mail, folder, carbon copy
---

# Multiple Fcc

## Introduction

This feature allows the user to save outgoing emails in multiple folders.

Folders should be listed separated by commas, **but no spaces**.

The "fcc" field of an email can be set in two ways:

- The [`<edit-fcc>`](fn-edit-fcc) command in the compose menu (default key: "f")
- Creating a [`:fcc-hook`](cmd-fcc-hook) in your `.neomuttrc`

## See Also

- {ref}`$record <cfg-record>`
- **fcc-hook**

