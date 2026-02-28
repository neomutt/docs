---
title: About NeoMutt's Architecture [TEMPLATE]
description: How NeoMutt's codebase is organized and why
---

# About NeoMutt's Architecture [TEMPLATE]

:::{admonition} Diátaxis: Explanation
:class: note

Write as **discursive discussion**. Explain WHY things are the way they are. Provide context,
background, and history. Connect concepts together. Use "about" framing. It's OK to include
opinion and perspective. Don't include step-by-step instructions — link to tutorials and
how-to guides instead. The reader should come away with deeper understanding.
:::

This page needs content covering the following topics:

- Overview of NeoMutt's C codebase structure
- Library modules (libmutt, libemail, libconn, libncrypt, libgui)
- The configuration system (variable parsing and type handling)
- How mailbox backends work (Maildir, mbox, IMAP, Notmuch, POP3)
- Pattern matching engine and limit expressions
- The curses-based GUI system
- Build system and compilation dependencies
- Source: GitHub repo at https://github.com/neomutt/neomutt

## Suggested Section Headings

### Codebase Overview

### Library Modules

### The Configuration System

### Mailbox Backends

### The MIME Parser

### Pattern Matching Engine

### The GUI and Curses Layer

### Build System and Dependencies
