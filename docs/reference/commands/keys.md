---
title: Key Bindings & Macros
description: XXX
keywords: XXX
---

# Key Bindings & Macros

Commands for binding keys to functions and defining keyboard macros.

(cmd-bind)=
## `bind`

Bind a key to a NeoMutt function in one or more keymaps.

- `bind <map> <key> <function>` — bind in a single map
- `bind <map1>,<map2> <key> <function>` — bind in multiple maps

```neomuttrc
bind index g  noop
bind index gg first-entry
bind index G  last-entry
bind pager j  next-line
bind pager k  previous-line
bind index,pager \Cd half-down
bind index,pager \Cu half-up
bind editor <Tab> complete-query
```

(cmd-unbind)=
## `unbind`

Remove a key binding.

- `unbind <map> <key>` — remove a specific binding
- `unbind *` — remove all bindings in all maps

```neomuttrc
unbind index g
unbind index,pager \Cd
```

(cmd-macro)=
## `macro`

Define a keyboard macro — a key that expands to a sequence of keystrokes.

- `macro <map> <key> <sequence>` — define a macro
- `macro <map> <key> <sequence> <description>` — define with a help description

```neomuttrc
macro index A "<save-message>=Archive<enter>"               "archive message"
macro index S "<pipe-message>bogofilter -l<enter><delete-message>" "learn as spam"
macro index,pager B "<view-attachments><search>html<enter><view-mailcap><exit>" "open in browser"
```

(cmd-unmacro)=
## `unmacro`

Remove a keyboard macro.

- `unmacro <map> <key>` — remove a specific macro
- `unmacro *` — remove all macros

```neomuttrc
unmacro index A
```

(cmd-exec)=
## `exec`

Immediately execute one or more NeoMutt functions.

- `exec <function>` — run a single function
- `exec <func1> <func2>` — run multiple functions in sequence

```neomuttrc
exec check-new
exec sync-mailbox first-entry
```

(cmd-push)=
## `push`

Push a string of keystrokes into NeoMutt's input queue, as if the user had typed it.

- `push <string>` — simulate typing

```neomuttrc
push "<save-message>=Archive<enter>"
push "<enter-command>source ~/.config/neomutt/temp.rc<enter>"
```

