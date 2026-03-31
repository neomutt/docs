# Copilot Instructions — NeoMutt Guide

## Project Overview

This is the official documentation site for [NeoMutt](https://neomutt.org/), a terminal-based email client.
It is built with **Sphinx + MyST Markdown** and hosted on **Read the Docs**.

Live site: **https://docs.neomutt.org/**

## Build Commands

```bash
# Install dependencies
pip install -r docs/requirements.txt

# Build HTML output
make html

# Clean build artifacts
make clean

# Pass extra Sphinx options
make html O="--keep-going"
```

Output lands in `build/html/`.
There are no test or lint commands.

The custom Pygments lexer in `pygments/` is installed automatically by Read the Docs via `.readthedocs.yaml`; for local builds it must be installed manually:

```bash
pip install -e pygments/
```

## Architecture

### Documentation Framework: Diátaxis

All content is organized into four strictly separated categories:

| Directory           | Type        | Purpose                                               |
|---------------------|-------------|-------------------------------------------------------|
| `docs/tutorials/`   | Tutorial    | Learning-oriented, guided walkthroughs                |
| `docs/howto/`       | How-To      | Goal-oriented task recipes                            |
| `docs/explanation/` | Explanation | Conceptual background and discussion                  |
| `docs/reference/`   | Reference   | Technical specifications, config, commands, functions |

Each section's `index.md` contains Diátaxis writing guidelines for that section — read them before adding content.

### Source → Build Pipeline

- Markdown sources in `docs/` use [MyST parser](https://myst-parser.readthedocs.io/) syntax
- Sphinx processes them using `docs/conf.py`
- Custom NeoMutt config syntax highlighter lives in `pygments/neomutt_lexer/lexer.py`
- Static assets (`docs/_static/`) are copied verbatim to output
- Read the Docs rebuilds automatically on push

### Reference Structure

`docs/reference/config/` contains one file per config-option group (e.g. `alias.md`, `color.md`, `core.md`).
These cross-reference commands in `docs/reference/commands/` and functions in `docs/reference/functions/`.
Many of these cross-reference links were broken during the initial DocBook conversion and are still being repaired (see `c1` for the active task list).

## Conventions

### Frontmatter (required on every page)

```yaml
---
title: Human-Readable Title
description: One-line description for SEO
keywords: keyword1, keyword2, keyword3
diataxis_type: tutorial | howto | explanation | reference
---
```

### File Naming

Lowercase with hyphens: `first-config.md`, `gmail-setup.md`.

### Code Blocks

Use `neomuttrc` for NeoMutt configuration snippets — this activates the custom lexer:

````markdown
```neomuttrc
set sort = threads
bind index G last-entry
```
````

### Cross-References

Use relative Markdown links:

```markdown
[Link text](../reference/config/color.md)
[Link text](../reference/config/color.md#some-anchor)
```

### Admonitions

MyST colon-fence syntax is preferred:

```markdown
:::{admonition} Title
:class: note | tip | warning
Content here.
:::
```

Placeholder admonitions used throughout the repo:

- `📷 Screenshot Needed` (class: `tip`) — marks pages needing terminal screenshots
- `[TEMPLATE]` (class: `warning`) — marks pages that need content written

### Grid Cards (sphinx-design)

Used on index pages for navigation:

```markdown
::::{grid} 2
:gutter: 3

:::{grid-item-card} Card Title
:link: target-page
:link-type: doc
:class-card: dia-tutorial

Card body text.
:::
::::
```

### MyST Extensions in Use

`attrs_inline`, `colon_fence`, `deflist`, `fieldlist`, `smartquotes`, `tasklist`

### Search Ranking

Configured in `.readthedocs.yaml`: tutorials rank highest (3), how-to next (2), explanation/reference lower (1), releases/about lowest (−2/−3).
Keep this in mind when deciding where new content belongs.

