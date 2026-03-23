---
title: Sending & Custom Headers
description: XXX
keywords: XXX
---

# Sending & Custom Headers

Commands for adding custom headers to outgoing messages.

(cmd-my-header)=
## `my-header`

Add a custom header to all outgoing messages.

- `my-header <header>: <value>` — add a header

```neomuttrc
my-header X-Mailer: NeoMutt
my-header X-Editor: vim
my-header Organization: NeoMutt Foundation
```

(cmd-unmy-header)=
## `unmy-header`

Remove a previously added custom header.

- `unmy-header *` — remove all custom headers
- `unmy-header <field>` — remove a specific header

```neomuttrc
unmy-header *
unmy-header X-Editor
```

