---
title: Header Cache Compression
description: Compress the NeoMutt header cache with lz4, zlib, or zstd to reduce disk usage and speed up large mailboxes
keywords: header cache, hcache, compression, lz4, zlib, zstd, header_cache_compress_method, header_cache_compress_level, performance, disk space, large mailbox
since: 2020-03-01
---

# Header Cache Compression

The Header Cache Compression feature can be used for speeding up the loading of large mailboxes. Also the space used on disk can be shrunk by about 50% — depending on the compression method being used.

The implementation sits on top of the header caching functions.
So the header cache compression can be used together with all available database backends.

## Variables

| Name                           | Type   | Default |
|--------------------------------|--------|---------|
| `header_cache_compress_method` | string | (empty) |
| `header_cache_compress_level`  | number | `1`     |

The `header_cache_compress_method` can be *(empty)* — which means that no header cache compression should be used. But when set to *lz4*, *zlib* or *zstd* — then the compression is turned on.

The `header_cache_compress_level` defines the compression level, which should be used together with the selected `header_cache_compress_method`. Here is an overview of the possible settings:

| Method Name | Min | Max |
|-------------|-----|-----|
| `lz4`       | 1   | 12  |
| `zlib`      | 1   | 9   |
| `zstd`      | 1   | 22  |

## neomuttrc

```neomuttrc
# Example NeoMutt config file for the header cache compression feature.

# --------------------------------------------------------------------------
# VARIABLES – shown with their default values
# --------------------------------------------------------------------------
set header_cache_compress_level  = 1
set header_cache_compress_method = ""

# vim: filetype=neomuttrc
```

## Credits

Tino Reichardt
