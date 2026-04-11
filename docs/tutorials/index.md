---
title: Tutorials
description: Learning-oriented tutorials that guide you step by step through configuring and using NeoMutt
---

(tut)=
# Tutorials

:::{tip}
Keyboard: {kbd}`T` jumps here from anywhere · {kbd}`U` returns here from any tutorial page
:::

:::{admonition} Diátaxis: Tutorial
:class: note

Write as **guided learning**.
Assume the reader is new to the topic and needs a clear path to build understanding through practice.
Teach by doing: introduce a small, concrete goal and walk through it step by step, explaining just enough along the way to support the task.
Structure content as a sequence of progressive steps, where each builds on the last and leads to a meaningful outcome.

Focus on the learner's experience: what they will do, see, and achieve at each stage.
Keep the scope narrow and self-contained, with minimal prerequisites.
Avoid deep dives into theory or exhaustive detail — link to explanation and reference material for that.
By the end, the reader should have completed something real and gained confidence to continue.
:::

Tutorials are **learning-oriented** lessons that guide you step by step through using NeoMutt.
Start here if you're new to NeoMutt.

Not sure where to begin?
Start with [Start Here](../start-here) for a guided path, or pick the question that matches you:

- "I just want NeoMutt to work with my mail account." Start with [Writing Your First Configuration](first-config).
- "I use Gmail." Go to [Gmail Setup](gmail-setup).
- "I use Office 365." Go to [Office 365 Setup](office365-setup).
- "I have my own IMAP server." Start with [Writing Your First Configuration](first-config), then see [IMAP](../howto/imap).

## Getting Started

```{toctree}
---
maxdepth: 1
---
tour/index.md
getting-started
first-config
first-email
sending-email
```

## Service-Specific Setup

```{toctree}
---
maxdepth: 1
---

gmail-setup
office365-setup
multiple-accounts
```

## Format Strings

```{toctree}
---
maxdepth: 1
---

conditional-expandos
pipe-command
```

## Offline Email Pipeline

```{toctree}
---
maxdepth: 1
---

pass-setup
mbsync-setup
msmtp-setup
notmuch-setup
```

## HTML & Links

```{toctree}
---
maxdepth: 1
---

html-and-urls
```

## Address Book

```{toctree}
---
maxdepth: 1
---

address-book
```

## Notmuch Virtual Mailboxes

```{toctree}
---
maxdepth: 1
---

notmuch-virtual-mailboxes
```

## Workflows

```{toctree}
---
maxdepth: 1
---

searching-email
tags-workflow
```
