---
title: How to Use Kyoto Cabinet / LMDB
description: Configure Kyoto Cabinet or LMDB as header cache backends for NeoMutt
keywords: kyoto cabinet, lmdb, header cache, hcache, backend, database, tokyocabinet
---

# How to Use Kyoto Cabinet / LMDB

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

## Kyoto Cabinet

**Kyoto Cabinet backend for the header cache**

### Support

**Dependencies:** [Kyoto Cabinet libraries](https://dbmx.net/kyotocabinet/)

To check if NeoMutt supports Kyoto Cabinet, look for:

- "kyoto" in the NeoMutt version.
- "+hcache" in the compile options
- "hcache backend: kyotocabinet" in the NeoMutt version

### Introduction

This feature adds support for using Kyoto Cabinet, the successor to Tokyo Cabinet, as a storage backend for NeoMutt's header cache (hcache). It is enabled at configure time with the *--with-kyotocabinet=\<path\>* switch.

### See Also

- {ref}`Local Caching <caching>`
- [Kyoto Cabinet](https://dbmx.net/kyotocabinet/)

### Known Bugs

None

### Credits

Clemens Lang

## LMDB

**LMDB backend for the header cache**

### Introduction

This feature adds support for using LMDB as a storage backend for NeoMutt's header cache (hcache). It is enabled at configure time with the *--with-lmdb=\<path\>* switch.

:::{note}
It is not recommended to store the lmdb database on a shared drive.
:::

### See Also

- {ref}`Local Caching <caching>`

### Known Bugs

None

### Credits

Pietro Cerutti, Jan-Piet Mens, Clemens Lang
