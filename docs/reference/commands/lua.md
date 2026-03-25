---
title: Lua Scripting
description: Commands for executing inline Lua expressions and sourcing Lua script files to extend NeoMutt.
keywords: lua, lua-source, scripting, lua scripting, mutt.set, mutt.get, mutt.message, automation, extensibility, plugins
---

# Lua Scripting

Commands for executing Lua code and scripts.

(cmd-lua)=
## `lua`

Run a Lua expression or call a Lua function.

- `lua <expression>` — execute inline Lua code

```neomuttrc
lua mutt.message("NeoMutt version: " .. mutt.get("version"))
lua mutt.set("sort", "date")
```

(cmd-lua-source)=
## `lua-source`

Execute a Lua script file.

- `lua-source <filename>`

```neomuttrc
lua-source ~/.config/neomutt/init.lua
```

