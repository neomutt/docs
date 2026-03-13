---
title: How to Use Lua Scripting
description: Embed Lua scripts in NeoMutt to get/set config options and run commands
keywords: lua, lua-source, scripting, embedded lua, automation
---

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

# How to Use Lua Scripting

## Introduction

Lua is a simple scripting language that's frequently embedded into other programs, such as NeoVim. It allows users to customise the behaviour of the host program.

In NeoMutt, Lua can be used to get/set config options and run commands.

## Commands

```neomuttrc
lua "lua-commands"
lua-source filename
```

## Usage

### Running Lua Inline

A simple example of running some Lua commands in NeoMutt:

```
# In NeoMutt, make the Sidebar wider
:lua "local x = mutt.get('sidebar_width'); x = x + 5; mutt.set('sidebar_width', x)"
```

### Using a Lua Script File

1. Create a local Lua script, `sw.lua`:

   ```lua
   -- Make the sidebar wider
   function sw()
       local width = mutt.get('sidebar_width')
       width = width + 5
       mutt.set('sidebar_width', width)
   end
   ```

2. Alter your NeoMutt config to add:

   ```
   # Load the script once
   lua-source "sw.lua"

   # Create a binding to run the function in the script
   macro index <F1> "<enter-command>lua 'sw()'<enter>
   ```

## Limitations

Currently, the Lua scripting is very limited. It doesn't have any way to interact with the objects within NeoMutt: the Mailboxes, the Emails, etc. Beyond that, there's almost zero documentation.

This state is changing. There is some new work coming to NeoMutt that exposes the Accounts, Mailboxes and Emails to Lua. This would allow the user to perform meaningful actions.

See: [https://github.com/neomutt/neomutt/pull/4707](https://github.com/neomutt/neomutt/pull/4707)

## Credits

Richard Russon, Bernard Pratz, Rayford Shireman, Darshit Shah
