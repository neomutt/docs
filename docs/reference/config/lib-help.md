---
title: Help Options
description: Configuration variable controlling the display of the key binding help line at the top of the screen.
keywords: neomutt, help, help line, key bindings, menu help, status line, beginner, onscreen help
---

# Help Options

(help)=
## `$help`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set help = yes
    ```

When _set_, help lines describing the bindings for the major functions provided by each menu are displayed on the first line of the screen.

:::{note}
The binding will not be displayed correctly if the function is bound to a sequence rather than a single keystroke.
Also, the help line may not be updated if a binding is changed while NeoMutt is running.
Since this variable is primarily aimed at new users, neither of these should present a major problem.
:::

