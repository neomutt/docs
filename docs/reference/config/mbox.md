---
title: Mbox Options
description: NeoMutt configuration variables for Mbox-format mailbox handling.
keywords: neomutt, mbox, mbox_check_cur, mbox_field_delimiter, mbox_header_cache_verify, mbox_trash, configuration
---

# Mbox Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

--------------------------------------------------------------------------------

(check-mbox-size)=
## `$check_mbox_size`

- **Type:** boolean
- **Default:**
    ```
    set check_mbox_size = no
    ```

When this variable is _set_, NeoMutt will use file size attribute instead of access time when checking for new mail in mbox and mmdf folders.

This variable is _unset_ by default and should only be enabled when new mail detection for these folder types is unreliable or doesn't work.

Note that enabling this variable should happen before any "$mailboxes" directives occur in configuration files regarding mbox or mmdf folders because NeoMutt needs to determine the initial new mail status of such a mailbox by performing a fast mailbox scan when it is defined.
Afterwards the new mail status is tracked by file size changes.

