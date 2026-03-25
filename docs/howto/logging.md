---
title: Use Logging and Debugging
description: View log messages, enable debug logging with -d, and configure error and message colours in NeoMutt
keywords: logging, debugging, debug, error, warning, log messages, neomuttdebug, show-log-messages, debug level, -d, color error, color message, troubleshooting, diagnostics
---

# Use Logging and Debugging

## Log Message Types

NeoMutt has different types of logging/error messages:

- **Primitive Errors** — errors emitted by C library functions such as `fopen()`.
- **Errors**
- **Warnings**
- **Message** — Informational messages such as `Sorting mailbox...`.
- **Debug** — Debug messages usually only interesting while debugging.

## Viewing Log Messages

These log messages are shown in the command bar at the bottom of the UI (usually below the status line).
Errors are shown in a different colour than the other message types.

To adjust the colours used for display:

```neomuttrc
color error ...
color message ...
```

See the description of `color` for the precise syntax.

The command bar shows only the last message.
To show the last 100 messages (this includes all types of messages from debug to error), use the `<show-log-messages>` function.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Log messages display

**Description:** The NeoMutt log messages view (accessed via `<show-log-messages>`) showing a scrollable list of recent log entries with a mix of message types — informational messages, warnings, and errors — each prefixed with a timestamp and severity indicator.

**Highlights:** How errors are displayed in a distinct colour, the chronological ordering of log entries, and the command bar at the bottom showing the most recent message.
:::

## Enabling Debug Logging

1. Debug messages are not shown by default. Set the debug log level with the `-d` command line parameter at startup:

   ```sh
   neomutt -d 2
   ```

2. The `-d` parameter expects a debug level which can range from 1 to 5 and affects verbosity of the debug messages.
   A value of **2** is recommended to start with.

3. If debug logging is enabled, all log messages (i.e. errors, warnings, ..., debug) are additionally written to the file `~/.neomuttdebug0`.
