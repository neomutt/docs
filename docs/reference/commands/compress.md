---
title: Compressed Mailboxes
description: XXX
keywords: XXX
---

# Compressed Mailboxes

Commands for defining how to open, close, and append to compressed mailboxes.

## `open-hook`

Define the command used to decompress a mailbox for reading.

- `open-hook <regex> <shell-command>`

```neomuttrc
open-hook  '\\.gz$'  "gzip --stdout --decompress '%f' > '%t'"
open-hook  '\\.bz2$' "bzip2 --stdout --decompress '%f' > '%t'"
open-hook  '\\.xz$'  "xz --stdout --decompress '%f' > '%t'"
```

## `close-hook`

Define the command used to compress a mailbox after changes.

- `close-hook <regex> <shell-command>`

```neomuttrc
close-hook '\\.gz$'  "gzip --stdout '%t' > '%f'"
close-hook '\\.bz2$' "bzip2 --stdout '%t' > '%f'"
close-hook '\\.xz$'  "xz --stdout '%t' > '%f'"
```

## `append-hook`

Define the command used to append messages to a compressed mailbox without
a full decompress/recompress cycle.

- `append-hook <regex> <shell-command>`

```neomuttrc
append-hook '\\.gz$' "gzip --stdout '%t' >> '%f'"
```

