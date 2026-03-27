---
title: Hcache Options
description: Configuration variables for the header cache database, backend selection, and compression settings.
keywords: neomutt, header cache, hcache, header_cache, header_cache_backend, compression, lz4, zstd, zlib, performance, caching, database
---

# Hcache Options

(header-cache)=
## `$header_cache`

:Type: [Path (String)](path)
:Default: (empty)
    ```neomuttrc
    set header_cache = ""
    ```

This variable points to the header cache database.
If the path points to an existing directory, NeoMutt will create a dedicated header cache database per folder.
Otherwise, the path points to a regular file, which will be created as needed and used as a shared global header cache for all folders.
By default it is _unset_ so no header caching will be used.

Header caching can greatly improve speed when opening POP, IMAP MH or Maildir folders, see "$caching" in the NeoMutt Guide for details.

--------------------------------------------------------------------------------

(header-cache-backend)=
## `$header_cache_backend`

:Type: [String](string)
:Default: (empty)
    ```neomuttrc
    set header_cache_backend = ""
    ```

This variable specifies the header cache backend.
If no backend is specified, the first available backend will be used in the following order:

| Order        |
|--------------|
| tokyocabinet |
| kyotocabinet |
| qdbm         |
| rocksdb      |
| gdbm         |
| bdb          |
| tdb          |
| lmdb         |

--------------------------------------------------------------------------------

(header-cache-compress-level)=
## `$header_cache_compress_level`

:Type: [Number](number)
:Notes: {ref}`Not Negative <general>`
:Default:
    ```neomuttrc
    set header_cache_compress_level = 1
    ```

When NeoMutt is compiled with lz4, zstd or zlib, this option can be used to setup the compression level.

--------------------------------------------------------------------------------

(header-cache-compress-method)=
## `$header_cache_compress_method`

:Type: [String](string)
:Default: (empty)
    ```neomuttrc
    set header_cache_compress_method = ""
    ```

When NeoMutt is compiled with lz4, zstd or zlib, the header cache backend can use these compression methods for compressing the cache files.
This results in much smaller cache file sizes and may even improve speed.

