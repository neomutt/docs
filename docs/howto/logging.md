---
title: How to Use Logging and Debugging
description: Configure and use NeoMutt's logging and debugging features to diagnose issues
keywords: logging, debugging, debug, error, log messages, neomuttdebug
---

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

# How to Use Logging and Debugging

## Log Message Types

NeoMutt has different types of logging/error messages:

- **Primitive Errors** — errors emitted by C library functions such as `fopen()`.
- **Errors**
- **Warnings**
- **Message** — Informational messages such as `Sorting mailbox...`.
- **Debug** — Debug messages usually only interesting while debugging.

## Viewing Log Messages

These log messages are shown in the command bar at the bottom of the UI (usually below the status line). Errors are shown in a different colour than the other message types.

To adjust the colours used for display:

```
color error ...
color message ...
```

See the description of `color` for the precise syntax.

The command bar shows only the last message. To show the last 100 messages (this includes all types of messages from debug to error), use the `<show-log-messages>` function.

## Enabling Debug Logging

1. Debug messages are not shown by default. Set the debug log level with the `-d` command line parameter at startup:

   ```
   neomutt -d 2
   ```

2. The `-d` parameter expects a debug level which can range from 1 to 5 and affects verbosity of the debug messages. A value of **2** is recommended to start with.

3. If debug logging is enabled, all log messages (i.e. errors, warnings, ..., debug) are additionally written to the file `~/.neomuttdebug0`.
