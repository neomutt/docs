---
title: How to Create Keyboard Macros
description: Create and manage keyboard macros to automate repeated actions in NeoMutt
keywords: macro, unmacro, keyboard macros, automation, key sequences
---

# How to Create Keyboard Macros

## Syntax

```neomuttrc
macro map [,map ...] key sequence [description]
unmacro {* | map [,map ...]} [key]
```

Macros are a convenient way to automate various actions.

## Creating a Key Macro

This command allows you to create a macro:

```neomuttrc
macro map [,map ...] key sequence [description]
```

Macros are useful when you would like a single key to perform a series of actions. 
When you press *key* in menu *map*, NeoMutt will behave as if you had typed *sequence*. 
So if you have a common sequence of commands you type, you can create a macro to execute those commands with a single key or fewer keys.

*map* is the map which the macro will be bound in. 
Multiple maps may be specified by separating multiple menu arguments by commas. 
Whitespace may not be used in between the menu arguments and the commas separating them.

*key* and *sequence* are expanded by the same rules as the key bindings with some additions. 
The first is that control characters in *sequence* can also be specified as `^x`. 
In order to get a caret ("^") you need to use `^^`. 
Secondly, to specify a certain key such as *up* or to invoke a function directly, you can use the format `<key name>` and `<function name>`. 
For a listing of key names see the section on key bindings. 
Functions are listed in the reference.

The advantage with using function names directly is that the macros will work regardless of the current key bindings, so they are not dependent on the user having particular key definitions. 
This makes them more robust and portable, and also facilitates defining of macros in files used by more than one user (e.g., the system neomuttrc).

Optionally you can specify a descriptive text after *sequence*, which is shown in the help screens if they contain a description.

:::{note}
Macro definitions (if any) listed in the help screen(s), are silently truncated at the screen width, and are not wrapped.
:::

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Macros displayed in the help screen

**Description:** The NeoMutt help screen (opened with `?`) showing a section of macro definitions, with the key sequence, the expanded macro body (possibly truncated), and the optional description text.

**Highlights:** How macro descriptions appear alongside key bindings, and how long macro sequences are truncated at the screen edge.
:::

## Removing a Key Macro

This command will remove a macro:

```neomuttrc
unmacro map [,map ...] key sequence
```

*map* specifies from which menus the macro should be removed. 
Multiple menus may be specified by separating them with commas (no additional whitespace is allowed). 
If `*` is given, then the macro is removed from all menus. 
Valid menu names and their description are listed in the `bind` section.

*key* is the key or key sequence to be unbound. It may be omitted in which case all macros in the given menus are removed.

:::{note}
Missing key sequence in unmacro command means unmacro all macros in menus given in *map*.
:::
