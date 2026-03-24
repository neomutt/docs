---
title: About NeoMutt
description: Introduction to NeoMutt, its community resources, and how to contribute
keywords: [neomutt, introduction, mailing lists, contributing, copyright]
diataxis_type: explanation
---

# About NeoMutt

**NeoMutt** is a small but very powerful text-based MIME mail client. NeoMutt is highly
configurable, and is well suited to the mail power user with advanced features like key
bindings, keyboard macros, mail threading, regular expression searches and a powerful
pattern matching language for selecting groups of messages.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** NeoMutt index view overview

**Description:** The NeoMutt index screen showing a mailbox with a variety of messages — some read, some unread, some flagged, some threaded — with the status bar and mini-help line visible. A typical mailbox with 20+ messages demonstrating the default layout.

**Highlights:** The reader should notice the key areas of the TUI: the message list (index) with status flags, the status bar at the bottom showing mailbox info, and the mini-help line showing available key bindings.
:::

## NeoMutt Home Page

The homepage can be found at [https://neomutt.org](https://neomutt.org).

## Mailing Lists

- `neomutt-users@neomutt.org` — help, bug reports and feature requests. To subscribe to
  this list, please send a mail to `neomutt-users-request@neomutt.org` with the subject
  "subscribe".

- `neomutt-devel@neomutt.org` — development mailing list. To subscribe to this list,
  please send a mail to `neomutt-devel-request@neomutt.org` with the subject "subscribe".

## NeoMutt Online Resources

Issue Tracking System
: Bugs may be reported on the devel mailing list, or on GitHub:
  [https://github.com/neomutt/neomutt/issues](https://github.com/neomutt/neomutt/issues)

IRC
: For the IRC user community, visit channel *#neomutt* on
  [irc.libera.chat](https://web.libera.chat/#neomutt).

## Contributing to NeoMutt

There are various ways to contribute to the NeoMutt project.

Especially for new users it may be helpful to meet other new and experienced users to chat
about NeoMutt, talk about problems and share tricks.

Since translations of NeoMutt into other languages are highly appreciated, the NeoMutt
developers always look for skilled translators that help improve and continue to maintain
stale translations.

For contributing code patches for new features and bug fixes, please refer to the developer
pages at [https://neomutt.org/dev.html](https://neomutt.org/dev.html) for more details.

## Typographical Conventions

This section lists typographical conventions followed throughout this manual. See the table
below for typographical conventions for special terms.

| Item | Refers to... |
|------|-------------|
| `printf(3)` | UNIX manual pages, execute `man 3 printf` |
| `<PageUp>` | named keys |
| `<create-alias>` | named NeoMutt function |
| `^G` | Control+G key combination |
| $mail_check | NeoMutt configuration option |
| `$HOME` | environment variable |

Examples are presented as:

```
neomutt -v
```

Within command synopsis, curly brackets ("{}") denote a set of options of which one is
mandatory, square brackets ("[]") denote optional arguments, three dots denote that the
argument may be repeated arbitrary times.

## Copyright

NeoMutt is Copyright © 2015-2026 Richard Russon and friends.

This program is free software; you can redistribute it and/or modify it under the terms of
the GNU General Public License as published by the Free Software Foundation; either version
2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program;
if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
Boston, MA 02110-1301, USA.

## Acknowledgements

The following people have been very helpful to the development of Mutt, on which NeoMutt is
based:

Kari Hurtta, Vikas Agnihotri, Francois Berjon, Aric Blumer, John Capo, David Champion,
Brendan Cully, Liviu Daia, Thomas E. Dickey, David DeSimone, Nickolay N. Dudorov,
Ruslan Ermilov, Edmund Grimley Evans, Michael Finken, Sven Guckes, Lars Hecking,
Mark Holloman, Andreas Holzmann, Marco d'Itri, Björn Jacke, Byrial Jensen, David Jeske,
Christophe Kalt, Tommi Komulainen, Felix von Leitner (a.k.a Fefe), Brandon Long,
Jimmy Mäkelä, Lars Marowsky-Bree, Kevin J. McCarthy, Thomas Mike Michlmayr,
Andrew W. Nosenko, David O'Brien, Clint Olsen, Park Myeong Seok, Thomas Parmelan,
Ollivier Robert, Thomas Roessler, Roland Rosenfeld, Rocco Rutte, TAKIZAWA Takashi,
Allain Thivillon, Gero Treuner, Vsevolod Volkov, Ken Weinert.
