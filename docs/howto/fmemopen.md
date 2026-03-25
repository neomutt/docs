---
title: How to Use fmemopen
description: Enable the fmemopen feature to replace temporary files with memory buffers for faster searches
keywords: fmemopen, open_memstream, glibc, performance, thorough_search, compile-time
---

# How to Use fmemopen

*Replace some temporary files with memory buffers*

## Support

**Dependencies:** : `open_memstream()`, `fmemopen()` from glibc

This feature can be enabled by running `configure` with the option `--fmemopen`

## Introduction

The "fmemopen" feature speeds up some searches.

This feature changes a few places where NeoMutt creates temporary files.
It replaces them with in-memory buffers.
This should improve the performance when searching the header or body using the `$thorough_search` option.

There are no user-configurable parts.

This feature depends on `open_memstream()` and `fmemopen()`.
They are provided by glibc.
Without them, NeoMutt will simply create temporary files.

## See Also

- **Compile-Time Features**
- `fmemopen(3)`

## Known Bugs

[debian bug 834408](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=834408)

## Credits

Julius Plenz, Richard Russon
