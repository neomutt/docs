---
title: How-To Guides
description: Goal-oriented guides covering mail protocols, encryption, composing, display, MIME, sidebar, configuration, and storage in NeoMutt
---

(how)=
# How-To Guides

:::{tip}
Keyboard: {kbd}`H` jumps here from anywhere · {kbd}`U` returns here from any how-to page
:::

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**.
Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused.
Use numbered steps for procedures.
Don't explain why — link to explanation pages instead.
Keep it focused on the specific task.
Start with prerequisites, give the steps, show the expected result.
:::

How-to guides are **goal-oriented** directions that help you accomplish specific tasks with NeoMutt.
Each guide addresses a real-world problem and provides practical steps to solve it.

## Recent

```{toctree}
---
maxdepth: 1
---
account-cmd
crypto/command-line-crypto
compose/compose-preview
custom-tagging
crypto/encryption-information-block
fuzzy-search
header-cache/header-cache-compression
lua-scripting
pager-read-delay
sidebar/sidebar-search
skip-quoted
use-threads
```

## Offline Email Pipeline

```{toctree}
---
maxdepth: 1
---

mbsync-filtering
msmtp-accounts
periodic-sync
mailbox-discovery
urlview
xdg-layout
```

## Mail Protocols & Authentication

```{toctree}
---
maxdepth: 1
---

imap
imap-performance
pop
smtp
oauth
tls-sni
```

## Encryption & Security

Configure PGP, S/MIME, Autocrypt, and other cryptographic features for signing and encrypting messages.

```{toctree}
---
maxdepth: 1
---

crypto/index
password-manager
```

## Composing & Sending

Step-by-step guides for writing, previewing, and sending messages — from composition flow to templates and forwarding.

```{toctree}
---
maxdepth: 1
---

compose/index
email-template
forwarding-mail
postponing-mail
format-flowed
multiple-fcc
forgotten-attachment
```

## Reading & Display

```{toctree}
---
maxdepth: 1
---

header-display
text-wrapping
threads
threading-scoring-workflows
display-munging
```

## MIME & Attachments

```{toctree}
---
maxdepth: 1
---

mime
mime-multilingual
mailcap-html
```

## Sidebar & UI

Set up, customise, and navigate NeoMutt's sidebar panel, including search, workflows, and colour themes.

```{toctree}
---
maxdepth: 1
---

sidebar/index
colours
progress-bar
sensible-browser
```

## Configuration & Scripting

```{toctree}
---
maxdepth: 1
---

key-bindings
macros
editing
hooks
format-strings
formatting-expandos
conditional-expandos
scoring
spam-filtering
address-groups
address-query
ifdef
lua
logging
backup-config
```

## Mailbox & Storage

```{toctree}
---
maxdepth: 1
---

mailbox-formats
compress
caching
trash-folder
mailboxes
```

## Header Cache

Tune, compress, and choose storage backends for NeoMutt's header cache.

```{toctree}
---
maxdepth: 1
---

header-cache/index
```

## Search & Tagging

```{toctree}
---
maxdepth: 1
---

notmuch
notmuch-advanced
tagging
limit-thread
```

## Notmuch Virtual Mailboxes

Create, organise, and navigate Notmuch virtual mailboxes — from simple unread-mail queries to complex boolean filters and tag-based workflows.

```{toctree}
---
maxdepth: 1
---

nm-vfolder/index
```

## Newsgroups

```{toctree}
---
maxdepth: 1
---

nntp
```

## Address Book

Manage contacts and aliases — define, search, display, and organise alias files and key bindings for quick addressing.

```{toctree}
---
maxdepth: 1
---

address-book
alias/index
```

## Miscellaneous

```{toctree}
---
maxdepth: 1
---

dsn
quasi-delete
reply-xorig
fmemopen
mailto-allow
external-tools
mutt-migration
```
