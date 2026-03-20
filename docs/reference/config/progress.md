---
title: Progress Options
description: Progress protocol configuration variables for NeoMutt
keywords: pop_auth_try_all, pop_authenticators, pop_check_interval, pop_delete, pop_host, pop_last, pop_oauth_refresh_command, pop_pass, pop_reconnect, pop_user
---

# Progress Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

--------------------------------------------------------------------------------

(net-inc)=
## `$net_inc`

- **Type:** number
- **Default:** 10

Operations that expect to transfer a large amount of data over the network will update their progress every $$net_inc kilobytes.
If set to 0, no progress messages will be displayed.

See also $$read_inc, $$write_inc and $$net_inc.

--------------------------------------------------------------------------------

(read-inc)=
## `$read_inc`

- **Type:** number
- **Default:** 10

If set to a value greater than 0, NeoMutt will display which message it is currently on when reading a mailbox or when performing search actions such as search and limit.
The message is printed after this many messages have been read or searched (e.g., if set to 25, NeoMutt will print a message when it is at message 25, and then again when it gets to message 50).
This variable is meant to indicate progress when reading or searching large mailboxes which may take some time.
When set to 0, only a single message will appear before the reading the mailbox.

Also see the $$write_inc, $$net_inc and $$time_inc variables and the "$tuning" section of the manual for performance considerations.

--------------------------------------------------------------------------------

(time-inc)=
## `$time_inc`

- **Type:** number
- **Default:** 0

Along with $$read_inc, $$write_inc, and $$net_inc, this variable controls the frequency with which progress updates are displayed.
It suppresses updates less than $$time_inc milliseconds apart.
This can improve throughput on systems with slow terminals, or when running NeoMutt on a remote system.

Also see the "$tuning" section of the manual for performance considerations.

--------------------------------------------------------------------------------

(write-inc)=
## `$write_inc`

- **Type:** number
- **Default:** 10

When writing a mailbox, a message will be printed every $$write_inc messages to indicate progress.
If set to 0, only a single message will be displayed before writing a mailbox.

Also see the $$read_inc, $$net_inc and $$time_inc variables and the "$tuning" section of the manual for performance considerations.

