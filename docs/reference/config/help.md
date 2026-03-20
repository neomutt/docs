---
title: Help Options
description: Reference for NeoMutt help configuration variables
keywords: neomutt, configuration, variables, help, settings
---

# Help Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

--------------------------------------------------------------------------------

(help)=
## `$help`

- **Type:** boolean
- **Default:**
    ```neomuttrc
    set help = yes
    ```

When _set_, help lines describing the bindings for the major functions provided by each menu are displayed on the first line of the screen.

**Note:** The binding will not be displayed correctly if the function is bound to a sequence rather than a single keystroke.
Also, the help line may not be updated if a binding is changed while NeoMutt is running.
Since this variable is primarily aimed at new users, neither of these should present a major problem.

