---
title: NeoMutt Guide
description: Official NeoMutt documentation — tutorials, how-to guides, explanations, and reference for the terminal email client
keywords: neomutt, email client, terminal, documentation, tutorials, how-to, reference, explanation, mutt, command-line email, text-based email
---

# NeoMutt Guide

Welcome. If you have only used GUI email clients before, you are in the right place.
This guide will help you get a working NeoMutt setup quickly, then show you how to go further.

- **Source:** [github.com/neomutt/neomutt](https://github.com/neomutt/neomutt)
- **Website:** [neomutt.org](https://neomutt.org)

---

::::{grid} 2
:gutter: 3

:::{grid-item-card}
:link: start-here
:link-type: doc
:class-card: dia-start
:columns: 12
✅ **Start Here**
^^^
**Beginner-friendly** — A few questions that route you to the right setup steps.
:::

:::{grid-item-card}
:link: tutorials/index
:link-type: doc
:class-card: dia-tutorial
📖 **Tutorials** - Learning-oriented
^^^
Step-by-step guides that walk you through real tasks from start to finish.
You'll build confidence by doing—learning NeoMutt in a practical, hands-on way, with clear outcomes at each stage.
+++
[Getting Started](tutorials/getting-started) · [First Config](tutorials/first-config) · [Gmail Setup](tutorials/gmail-setup) · [Interface Tour](tut-tour)
:::

:::{grid-item-card}
:link: howto/index
:link-type: doc
:class-card: dia-howto
🔧 **How-To Guides** - Goal-oriented
^^^
Focused instructions for solving specific problems or achieving particular goals.
You'll find direct, task-oriented answers—helping you get things done quickly without unnecessary background detail.
+++
[Colours](howto/colours) · [Key Bindings](howto/key-bindings) · [Hooks](howto/hooks) · [Sidebar](howto/sidebar) · [IMAP](howto/imap) · [SMTP](howto/smtp)
:::

:::{grid-item-card}
:link: explanation/index
:link-type: doc
:class-card: dia-explanation
💡 **Explanation** - Understanding-oriented
^^^
In-depth discussions that explain how and why NeoMutt works the way it does.
You'll gain a deeper understanding of concepts, design decisions, and underlying mechanisms—so you can make better-informed choices.
+++
[Config Paradigms](explanation/config-paradigms) · [Threading](explanation/threading) · [Encryption](explanation/encryption) · [MIME](explanation/mime)
:::

:::{grid-item-card}
:link: reference/index
:link-type: doc
:class-card: dia-reference
📋 **Reference** - Information-oriented
^^^
A complete, factual catalogue of NeoMutt's commands, variables, and configuration options.
You'll get precise, authoritative information you can rely on when you need exact syntax, valid values, or detailed behaviour.
+++
[Config](ref-config) · [Functions](ref-functions) · [Commands](ref-commands) · [Colours](ref-colors) · [Glossary](ref-glossary)
:::

:::{grid-item-card}
:class-card: dia-start
:columns: 12
⌨️ **Keyboard Navigation**
^^^
| Key      | Action        |  | Key                        | Action               |
|----------|---------------|--|----------------------------|----------------------|
| {kbd}`T` | Tutorials     |  | {kbd}`←` {kbd}`h` {kbd}`[` | Previous page        |
| {kbd}`H` | How-To Guides |  | {kbd}`→` {kbd}`l` {kbd}`]` | Next page            |
| {kbd}`E` | Explanation   |  | {kbd}`u`                   | Go up to parent page |
| {kbd}`R` | Reference     |  | {kbd}`U`                   | Section root         |
:::

::::

```{toctree}
---
maxdepth: 1
hidden: true
---
start-here
tutorials/index
howto/index
explanation/index
reference/index
```
