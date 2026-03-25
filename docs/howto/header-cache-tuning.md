---
title: Tune the Header Cache
description: Choose cache locations, select backends, enable compression, and clean body caches for faster mailbox access
keywords: header cache, hcache, header_cache, message_cache_dir, performance, header_cache_backend, header_cache_compress_method, header_cache_compress_level, message_cache_clean, zstd, compression, tuning, optimization
---

# Tune the Header Cache

## Prerequisites

1. NeoMutt built with a header cache backend.
2. A working cache directory on local storage.

## Choose a Cache Location

1. Pick a directory for caches:

```neomuttrc
set header_cache = "~/.cache/neomutt/hcache"
set message_cache_dir = "~/.cache/neomutt/bcache"
```

2. Restart NeoMutt.

Expected result: NeoMutt creates cache files in the selected locations.

## Select a Backend Explicitly

1. If multiple backends are available, pin one:

```neomuttrc
set header_cache_backend = "lmdb"
```

Expected result: NeoMutt uses the specified backend for header cache storage.

## Enable Cache Compression

1. Turn on compression to reduce disk usage:

```neomuttrc
set header_cache_compress_method = "zstd"
set header_cache_compress_level = 3
```

Expected result: cache files shrink at the cost of extra CPU.

## Keep the Cache Clean

1. For body caches, enable cleaning only when needed:

```neomuttrc
set message_cache_clean = yes
```

2. Disable it again if you notice performance impact.

Expected result: cache files no longer reference messages removed by other clients.

See [How to Set Up Header/Body Caching](caching) for full details and supported backends.
