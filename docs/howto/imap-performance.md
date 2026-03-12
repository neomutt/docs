---
title: How to Troubleshoot IMAP Performance
description: Diagnose slow IMAP connections and tune NeoMutt IMAP settings
keywords: imap, performance, imap_keep_alive, imap_idle, imap_fetch_chunk_size, timeout
---

# How to Troubleshoot IMAP Performance

## Prerequisites

1. You can connect to your IMAP server with NeoMutt.
2. You can reproduce the slowdown (opening a mailbox, checking for new mail, or searching).

## Reduce Polling Overhead

1. Tune the global polling intervals:

```neomuttrc
set mail_check = 90
set timeout = 15
```

Expected result: NeoMutt checks for new mail less frequently, reducing idle overhead.

## Avoid Hanging Connections

1. Ensure keep-alives are frequent enough for your server:

```neomuttrc
set imap_keep_alive = 300
```

Expected result: servers are less likely to disconnect idle sessions.

## Disable IMAP IDLE if It Freezes

1. If the UI stalls while waiting for new mail, disable IDLE:

```neomuttrc
unset imap_idle
```

Expected result: NeoMutt uses polling instead of IDLE, which can be more reliable on some servers.

## Limit Large Fetches

1. If opening large mailboxes times out, fetch headers in chunks:

```neomuttrc
set imap_fetch_chunk_size = 200
```

Expected result: header downloads are split into smaller requests.

## Enable Compression

1. If bandwidth is a bottleneck, enable IMAP compression:

```neomuttrc
set imap_deflate = yes
```

Expected result: large mailbox operations use less bandwidth.

## Reduce Connection Churn

1. Avoid opening new IMAP connections just to check mail:

```neomuttrc
set imap_passive = yes
```

Expected result: NeoMutt only checks mail over existing connections.

See [How to Set Up IMAP](imap) and [IMAP Variables](../reference/options/imap) for full details.
