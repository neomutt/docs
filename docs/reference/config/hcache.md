---
title: Hcache Options
description: Reference for NeoMutt Hcache configuration variables
keywords: neomutt, configuration, variables, Hcache, settings
---

# Hcache Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::


hcache.md
	  { "header_cache", DT_PATH, 0, 0, NULL,
	  { "header_cache_backend", DT_STRING, 0, 0, hcache_validator,
	  { "header_cache_compress_method", DT_STRING, 0, 0, compress_method_validator,
	  { "header_cache_compress_level", DT_NUMBER|D_INTEGER_NOT_NEGATIVE, 1, 0, compress_level_validator,
	  { "header_cache_compress", D_INTERNAL_DEPRECATED|DT_BOOL, 0, IP "2020-03-25" },
	  { "header_cache_pagesize", D_INTERNAL_DEPRECATED|DT_LONG, 0, IP "2020-03-25" },

----------------------------------------------------------------------------------------------------------

(header-cache)=
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
MH or Maildir folders, see **caching** in the NeoMutt Guide for details.

----------------------------------------------------------------------------------------------------------

(header-cache-backend)=
## `$header_cache_backend`

- **Type:** string
- **Default:** (empty)

This variable specifies the header cache backend.  If no backend is
specified, the first available backend will be used in the following order:
tokyocabinet, kyotocabinet, qdbm, rocksdb, gdbm, bdb, tdb, lmdb.

----------------------------------------------------------------------------------------------------------

(header-cache-compress-method)=
## `$header_cache_compress_method`

- **Type:** string
- **Default:** (empty)

When NeoMutt is compiled with lz4, zstd or zlib, the header cache backend
can use these compression methods for compressing the cache files.
This results in much smaller cache file sizes and may even improve speed.

----------------------------------------------------------------------------------------------------------

(header-cache-compress-level)=
## `$header_cache_compress_level`

- **Type:** number
- **Default:** 1

When NeoMutt is compiled with lz4, zstd or zlib, this option can be used
to setup the compression level.

