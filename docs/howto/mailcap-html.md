---
title: Render HTML Email with Mailcap
description: Set up mailcap entries and text-mode browsers to render HTML email as plain text in NeoMutt
keywords: mailcap, html, text/html, w3m, lynx, elinks, auto-view, copiousoutput, mailcap_path, mailcap_sanitize, rendering, security, text browser
---

# Render HTML Email with Mailcap

## Prerequisites

1. Install a text-mode browser such as `w3m`, `lynx`, or `elinks`.
2. Locate your mailcap file ([`$mailcap_path`](cfg-mailcap-path)) or decide where to create one.

## Add a Mailcap Entry for HTML

1. Add a `text/html` entry to your mailcap file:

```
text/html; lynx -dump %s; copiousoutput
```

2. Save the mailcap file.

Expected result: NeoMutt can render HTML messages as text using `lynx`.

## Choose a Different Renderer

1. Replace the command with your preferred tool:

```
text/html; w3m -dump -T text/html %s; copiousoutput
```

or

```
text/html; elinks -dump %s; copiousoutput
```

Expected result: HTML rendering uses your preferred program.

## Auto-View HTML Parts

1. Enable autoview for HTML:

```neomuttrc
auto-view text/html
```

2. Open a message with HTML content.

Expected result: NeoMutt renders HTML parts automatically.

## Verify Mailcap Search Order

1. Check where NeoMutt looks for mailcap files:

```sh
neomutt -nF /dev/null -Q mailcap_path
```

Expected result: you see the search path NeoMutt will use for mailcap.

## Keep Mailcap Secure

1. Avoid backticks and untrusted shell expansions inside mailcap entries.
2. Use `mailcap_sanitize` if you need stricter controls on mailcap expansion.

Expected result: HTML rendering works without introducing unsafe command execution.

See also [MIME Types](../reference/mime-types) and [MIME](../explanation/mime).
