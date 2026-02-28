---
title: "Header/Cache Variables"
description: "Reference for NeoMutt header and header cache configuration variables."
keywords: "header, cache, variables, neomutt"
---

# Header/Cache Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

## `$header`

- **Type:** boolean
- **Default:** no

When *set*, this variable causes NeoMutt to include the header
of the message you are replying to into the edit buffer.
The [`$weed`](../index.md#weed) setting applies.

## `$header_cache`

- **Type:** path
- **Default:** (empty)

This variable points to the header cache database. If the path points to
an existing directory, NeoMutt will create a dedicated header cache
database per folder. Otherwise, the path points to a regular file, which
will be created as needed and used as a shared global header cache for
all folders.
By default it is *unset* so no header caching will be used.

Header caching can greatly improve speed when opening POP, IMAP
MH or Maildir folders, see "[`caching`](../index.md#caching)" in the NeoMutt Guide for details.

## `$header_cache_backend`

- **Type:** string
- **Default:** (empty)

This variable specifies the header cache backend.  If no backend is
specified, the first available backend will be used in the following order:
tokyocabinet, kyotocabinet, qdbm, rocksdb, gdbm, bdb, tdb, lmdb.

## `$header_cache_compress_level`

- **Type:** number
- **Default:** 1

When NeoMutt is compiled with lz4, zstd or zlib, this option can be used
to setup the compression level.

## `$header_cache_compress_method`

- **Type:** string
- **Default:** (empty)

When NeoMutt is compiled with lz4, zstd or zlib, the header cache backend
can use these compression methods for compressing the cache files.
This results in much smaller cache file sizes and may even improve speed.

## `$header_color_partial`

- **Type:** boolean
- **Default:** no

When *set*, color header regexes behave like color body regexes:
color is applied to the exact text matched by the regex.  When
*unset*, color is applied to the entire header.

One use of this option might be to apply color to just the header labels.

See "[`color`](../index.md#color)" for more details.
