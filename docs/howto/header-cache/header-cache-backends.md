---
title: Kyoto Cabinet / LMDB
description: Set up Kyoto Cabinet or LMDB as storage backends for the NeoMutt header cache
keywords: kyoto cabinet, lmdb, header cache, hcache, backend, database, tokyocabinet, storage, compile option, --with-kyotocabinet, --with-lmdb, caching, key-value store
---

# Kyoto Cabinet / LMDB

## Kyoto Cabinet

**Kyoto Cabinet backend for the header cache**

### Support

**Dependencies:** [Kyoto Cabinet libraries](https://dbmx.net/kyotocabinet/)

To check if NeoMutt supports Kyoto Cabinet, look for:

- "kyoto" in the NeoMutt version.
- "+hcache" in the compile options
- "hcache backend: kyotocabinet" in the NeoMutt version

### Introduction

This feature adds support for using Kyoto Cabinet, the successor to Tokyo Cabinet, as a storage backend for NeoMutt's header cache (hcache).
It is enabled at configure time with the *--with-kyotocabinet=\<path\>* switch.

### See Also

- [Local Caching](../caching.md)
- [Kyoto Cabinet](https://dbmx.net/kyotocabinet/)

### Credits

Clemens Lang

## LMDB

**LMDB backend for the header cache**

### Introduction

This feature adds support for using LMDB as a storage backend for NeoMutt's header cache (hcache).
It is enabled at configure time with the *--with-lmdb=\<path\>* switch.

:::{note}
It is not recommended to store the lmdb database on a shared drive.
:::

### See Also

- [Local Caching](../caching.md)

