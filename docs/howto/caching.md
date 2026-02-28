---
title: How to Set Up Header/Body Caching
description: Configure header caching and body caching to speed up opening large folders, plus header cache compression options
keywords: header cache, body cache, caching, hcache, message cache, lz4, zlib, zstd, compression, performance
---

# How to Set Up Header/Body Caching

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

NeoMutt contains two types of local caching: *(1)* the so-called "header caching" and *(2)* the so-called "body caching" which are both described in this section.

Header caching is optional as it depends on external libraries, body caching is always enabled if NeoMutt is compiled with POP and/or IMAP support as these use it (body caching requires no external library).

## Header Caching

NeoMutt provides optional support for caching message headers for the following types of folders: IMAP, POP, Maildir and MH. Header caching greatly speeds up opening large folders because for remote folders, headers usually only need to be downloaded once. For Maildir and MH, reading the headers from a single file is much faster than looking at possibly thousands of single files (since Maildir and MH use one file per message.)

Header caching can be enabled by configuring one of the database backends. One of bdb, gdbm, kyotocabinet, lmdb, qdbm, rocksdb, tdb, tokyocabinet.

If enabled, `$header_cache` can be used to either point to a file or a directory. If set to point to a file, one database file for all folders will be used (which may result in lower performance), but one file per folder if it points to a directory.

Additionally, `$header_cache_backend` can be set to specify which backend to use. The list of available backends can be specified at configure time with a set of `--with-<backend>` options. Currently, the following backends are supported: bdb, gdbm, kyotocabinet, lmdb, qdbm, rocksdb, tdb, tokyocabinet.

Take a look at the benchmark script provided in the following repository: [contrib-hcache-benchmark](https://github.com/neomutt/contrib-hcache-benchmark). There you can find a way of finding the storage backend for your needs.

## Body Caching

Both cache methods can be combined using the same directory for storage (and for IMAP/POP even provide meaningful file names) which simplifies manual maintenance tasks.

In addition to caching message headers only, NeoMutt can also cache whole message bodies. This results in faster display of messages for POP and IMAP folders because messages usually have to be downloaded only once.

For configuration, the variable `$message_cache_dir` must point to a directory. There, NeoMutt will create a hierarchy of subdirectories named like the account and mailbox path the cache is for.

## Cache Directories

For using both, header and body caching, `$header_cache` and `$message_cache_dir` can be safely set to the same value.

In a header or body cache directory, NeoMutt creates a directory hierarchy named like: `proto:user@hostname` where `proto` is either "pop" or "imap." Within there, for each folder, NeoMutt stores messages in single files and header caches in files with the ".hcache" extension. All files can be removed as needed if the consumed disk space becomes an issue as NeoMutt will silently fetch missing items again. Pathnames are always stored in UTF-8 encoding.

For Maildir and MH, the header cache files are named after the MD5 checksum of the path.

## Maintenance

NeoMutt does not (yet) support maintenance features for header cache database files so that files have to be removed in case they grow too big. It depends on the database library used for header caching whether disk space freed by removing messages is reused.

For body caches, NeoMutt can keep the local cache in sync with the remote mailbox if the `$message_cache_clean` variable is set. Cleaning means to remove messages from the cache which are no longer present in the mailbox which only happens when other mail clients or instances of NeoMutt using a different body cache location delete messages (NeoMutt itself removes deleted messages from the cache when syncing a mailbox). As cleaning can take a noticeable amount of time, it should not be set in general but only occasionally.

## Header Cache Compression

The Header Cache Compression feature can be used for speeding up the loading of large mailboxes. Also the space used on disk can be shrunk by about 50% — depending on the compression method being used.

The implementation sits on top of the header caching functions. So the header cache compression can be used together with all available database backends.

### Variables

| Name | Type | Default |
|------|------|---------|
| `header_cache_compress_method` | string | (empty) |
| `header_cache_compress_level` | number | `1` |

The `header_cache_compress_method` can be *(empty)* — which means that no header cache compression should be used. But when set to *lz4*, *zlib* or *zstd* — then the compression is turned on.

The `header_cache_compress_level` defines the compression level, which should be used together with the selected `header_cache_compress_method`. Here is an overview of the possible settings:

| Method Name | Min | Max |
|-------------|-----|-----|
| `lz4`       | 1   | 12  |
| `zlib`      | 1   | 9   |
| `zstd`      | 1   | 22  |

### neomuttrc

```
# Example NeoMutt config file for the header cache compression feature.

# --------------------------------------------------------------------------
# VARIABLES – shown with their default values
# --------------------------------------------------------------------------
set header_cache_compress_level = 1
set header_cache_compress_method = ""

# vim: syntax=neomuttrc
```

### Known Bugs

None

### Credits

Tino Reichardt
