---
title: Customise Key Bindings
description: Assign functions to keys, unbind defaults, handle key sequences, and manage terminal key conflicts in NeoMutt
keywords: bind, unbind, key bindings, keyboard, maps, menus, noop, key sequence, generic, index, pager, compose, attach, editor, browser, symbolic key names, what-key, terminal, stty, enter, return
---

# Customise Key Bindings

## Syntax

```neomuttrc
bind map [,map ...] key function
unbind {* | map [,map ...]} [key]
```

The [`:bind`](cmd-bind) command allows you to change the default key bindings (operation invoked when pressing a key).

## Binding a Key Sequence to a Function

The [`:bind`](cmd-bind) command allows you to assign a new effect to a key (e.g. {kbd}`a`) or a key sequence (e.g. {kbd}`gh` — that is pressing {kbd}`g` followed by a press of {kbd}`h`).

```neomuttrc
bind map [,map ...] key function
```

*map* specifies in which menu the binding belongs.
Multiple maps may be specified by separating them with commas (no additional whitespace is allowed).
The currently defined maps are:

| Map        | Description                                                                                                                                         |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `generic`  | Fallback for all other menus except pager and editor. If a key is not defined in another menu, NeoMutt will look for a binding to use in this menu. |
| `alias`    | The alias menu is the list of your personal aliases as defined in your `.neomuttrc`.                                                                |
| `attach`   | The attachment menu is used to access the attachments on received messages.                                                                         |
| `browser`  | Used for both browsing the local directory structure, and for listing all of your incoming mailboxes.                                               |
| `editor`   | Used to allow the user to enter a single line of text, such as the *To* or *Subject* prompts in the `compose` menu.                                 |
| `index`    | The list of messages contained in a mailbox.                                                                                                        |
| `compose`  | The screen used when sending a new message.                                                                                                         |
| `pager`    | The mode used to display message/attachment data, and help listings.                                                                                |
| `pgp`      | Used to select the OpenPGP keys used to encrypt outgoing messages.                                                                                  |
| `smime`    | Used to select the OpenSSL certificates used to encrypt outgoing messages.                                                                          |
| `postpone` | Similar to the index menu, except used when recalling a postponed message.                                                                          |
| `query`    | The browser for results returned by [`$query_command`](cfg-query-command).                                                                                               |

### Specifying Keys

*key* is the key (or key sequence) you wish to bind.
To specify a control character, use the sequence `\Cx`, where `x` is the letter of the control character (for example, to specify control-A use `\Ca`).
Note that the case of `x` as well as `\C` is ignored, so that `\CA`, `\Ca`, `\cA` and `\ca` are all equivalent.
An alternative form is to specify the key as a three digit octal number prefixed with a `\` (for example `\177` is equivalent to `\c?`).
You can also use the form {kbd}`<177>`, which allows octal numbers with an arbitrary number of digits.

#### Symbolic Key Names

| Symbolic name   | Meaning                     |
|-----------------|-----------------------------|
| `\t`            | tab                         |
| {kbd}`<Tab>`         | tab                         |
| {kbd}`Shift-Tab`     | backtab / shift-tab         |
| `\r`            | carriage return             |
| `\n`            | newline                     |
| `\e`            | escape/alt                  |
| {kbd}`Escape`         | escape/alt                  |
| {kbd}`Up`          | up arrow                    |
| {kbd}`Down`        | down arrow                  |
| {kbd}`Left`        | left arrow                  |
| {kbd}`Right`       | right arrow                 |
| {kbd}`Page Up`      | Page Up                     |
| {kbd}`Page Down`    | Page Down                   |
| {kbd}`Backspace`   | Backspace                   |
| {kbd}`Delete`      | Delete                      |
| {kbd}`Insert`      | Insert                      |
| {kbd}`Enter`       | Enter                       |
| {kbd}`Return`      | Return                      |
| {kbd}`Keypad Enter` | Enter key on numeric keypad |
| {kbd}`Home`        | Home                        |
| {kbd}`End`         | End                         |
| {kbd}`Space`       | Space bar                   |
| {kbd}`F1`          | function key 1              |
| {kbd}`F10`         | function key 10             |

The [`<what-key>`](fn-what-key) function can be used to explore keycode and symbolic names for other keys on your keyboard.
Executing this function will display information about each key pressed, until terminated by {kbd}`Ctrl-G`.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Help screen showing key bindings

**Description:** The NeoMutt help screen (opened with {kbd}`?`) displaying the list of key bindings for the index menu, showing the key column, function column, and description column.

**Highlights:** How bindings are organized by menu, with default and custom bindings listed together.
:::

*key* does not need to be enclosed in quotes unless it contains a space (" ") or semi-colon (";").

*function* specifies which action to take when *key* is pressed.
For a complete list of functions, see the reference.
Note that the [`:bind`](cmd-bind) command expects *function* to be specified without angle brackets.

The special function `<noop>` unbinds the specified key sequence.
It is recommended to use [`:unbind`](cmd-unbind) instead.

## Unbinding a Key Sequence

To remove a binding of a key or key sequence, [`:unbind`](cmd-unbind) can be used:

```neomuttrc
unbind {* | map [,map ...]} [key]
```

*map* specifies from which menus the key sequence should be removed.
Multiple maps may be specified by separating them with commas (no additional whitespace is allowed).
If `*` is given, then the key sequence is removed from all menus.

*key* is the key or key sequence to be unbound.
It may be omitted in which case all keybindings in the given menus are removed.
To prevent NeoMutt from becoming unusable some fallback key bindings are added afterwards.

### Fallback Key Bindings

| Menu    | Key               | Bound Function      |
|---------|-------------------|---------------------|
| generic | {kbd}`Enter`     | [`<select-entry>`](fn-select-entry)      |
| generic | {kbd}`Return`    | [`<select-entry>`](fn-select-entry)      |
| generic | {kbd}`:`         | [`<enter-command>`](fn-enter-command)    |
| generic | {kbd}`?`         | [`<help>`](fn-help)                      |
| generic | {kbd}`q`         | [`<exit>`](fn-exit)                      |
| editor  | {kbd}`Backspace` | [`<backspace>`](fn-backspace)            |
| editor  | `\177`           | [`<backspace>`](fn-backspace)            |
| index   | {kbd}`Enter`     | [`<display-message>`](fn-display-message) |
| index   | {kbd}`Return`    | [`<display-message>`](fn-display-message) |
| pager   | {kbd}`?`         | [`<help>`](fn-help)                      |
| pager   | {kbd}`q`         | [`<exit>`](fn-exit)                      |
| pager   | {kbd}`:`         | [`<enter-command>`](fn-enter-command)    |

A key binding can also be unbound by mapping it to the special function `<noop>`.
It is, however, recommended to use [`:unbind`](cmd-unbind) instead.

## Enter versus Return

Prior to 2022, NeoMutt used a default ncurses mode (`nl()`).
This mode maps keyboard input of either {kbd}`Enter` or {kbd}`Return` to the same value, which NeoMutt interpreted as {kbd}`Return` internally.

However, starting in version 2.2, this mode is turned off, allowing {kbd}`Return` and {kbd}`Enter` to be mapped separately, if desired.
The default keyboard mappings set both, but you can override this or create new bindings with one or the other (or both).

Note that in terminal applications, such as NeoMutt, {kbd}`Enter` is the same as `\n` and {kbd}`Ctrl-J`; while {kbd}`Return` is the same as `\r` and {kbd}`Ctrl-M`.

## Warnings about Duplicated Bindings

Due to a limitation of NeoMutt, creating key bindings, or macros, will overwrite existing mappings with similar, shorter, names.

```neomuttrc
bind index g  group-reply
bind index gg first-entry
```

In this example, the {kbd}`g` binding will be overwritten and cannot be used.
Newer versions of NeoMutt will warn the user about this.

To avoid warnings on startup, first set the shorter binding to `<noop>` (no operation):

```neomuttrc
bind index g  noop
bind index gg first-entry
```

The same is also possible using [`:unbind`](cmd-unbind):

```neomuttrc
unbind index g
bind index gg first-entry
```

## Terminal Keybindings

Some key bindings are controlled by the terminal, and so by default can't be bound inside NeoMutt.
These may include {kbd}`Ctrl-C`, {kbd}`^\`, {kbd}`Ctrl-Q`, {kbd}`Ctrl-S`, {kbd}`Ctrl-Z`, and on BSD/Mac {kbd}`Ctrl-Y`.
These terminal settings can be viewed and changed using the `stty` program.

`stty -a` will list the bound characters (not all of them affect NeoMutt), and what actions they take when pressed.
For example, you may see `intr = ^C` in its output.
This means typing {kbd}`Ctrl-C` will send an interrupt signal.
`quit = ^\` means typing {kbd}`^\` (commonly also {kbd}`^4`) will send a quit signal.

To unbind a key from an action, you invoke `stty action undef`.
For example, `stty quit undef` will unbind {kbd}`^\` (and {kbd}`^4`) from sending the quit signal.
Once unbound (e.g. by placing that line in your `.profile`, or in a NeoMutt wrapper script/function) you can use the key sequence in your NeoMutt bindings.
