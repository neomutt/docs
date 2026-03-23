---
title: Lua Scripting
description: XXX
keywords: XXX
---

# Lua Scripting

Commands for executing Lua code and scripts.

## `lua`

Run a Lua expression or call a Lua function.

- `lua <expression>` — execute inline Lua code

```neomuttrc
lua mutt.message("NeoMutt version: " .. mutt.get("version"))
lua mutt.set("sort", "date")
```

## `lua-source`

Execute a Lua script file.

- `lua-source <filename>`

```neomuttrc
lua-source ~/.config/neomutt/init.lua
```

