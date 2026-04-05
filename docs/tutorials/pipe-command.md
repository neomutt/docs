---
title: Pipe Commands
description: How to use shell commands in place of static config values by appending a trailing pipe character
keywords: neomutt, pipe, command, signature, dynamic, shell, config
---

(tut-pipe-command)=
# Pipe Commands

Some NeoMutt config options can run a shell command and use its output instead of a static value.
You enable this by ending the value with a `|` (pipe) character.

This tutorial walks through the most common use case: generating your email signature dynamically.

---

## Step 1 — A Static Signature

The simplest signature setup points `$signature` at a plain text file:

```neomuttrc
set signature = "~/.signature"
```

The file `~/.signature` might contain:

```text
Regards,
Alice
```

Every outgoing email gets the same signature.

---

## Step 2 — Make It Dynamic with a Pipe

Suppose you want your signature to include today's date, a quote of the day, or different content depending on the recipient.
Instead of a static file, you can point `$signature` at a script — just add `|` at the end:

```neomuttrc
set signature = "~/.mutt/gen-sig.sh|"
```

NeoMutt will:

1. Strip the trailing `|`
2. Execute `~/.mutt/gen-sig.sh` as a shell command
3. Read its standard output as the signature text

---

## Step 3 — Write the Script

Create the script `~/.mutt/gen-sig.sh`:

```bash
#!/bin/sh
echo "Regards,"
echo "Alice"
echo ""
echo "Sent on $(date '+%A, %d %B %Y')"
```

Make it executable:

```console
$ chmod +x ~/.mutt/gen-sig.sh
```

Now every email will have a signature like:

```text
Regards,
Alice

Sent on Monday, 07 April 2025
```

---

## Step 4 — Test It

You can verify your script works by running it directly:

```console
$ ~/.mutt/gen-sig.sh
Regards,
Alice

Sent on Monday, 07 April 2025
```

Then compose a test message in NeoMutt and check that the signature appears correctly at the bottom of the message body.

---

## How It Works

NeoMutt supports the trailing pipe in two categories of config options:

**Path options** (like `$signature`)
: The value is treated as a command.
  NeoMutt runs it and reads the full output as if it were a file.

**Expando options** (like `$index_format`, `$status_format`, and others)
: After NeoMutt expands the format string, if the result ends with `|`, the expanded string is executed as a command and the first line of output replaces it.

:::{seealso}
- [Config Types — Pipe Support](type-pipe) lists both mechanisms and all supported options
:::
