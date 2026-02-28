---
title: How to Customise Key Bindings
description: Change default key bindings, unbind keys, and manage terminal keybindings in NeoMutt
keywords: bind, unbind, key bindings, keyboard, maps, menus, noop
---

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

# How to Customise Key Bindings

## Syntax

```
bind map [,map ...] key function
unbind {* | map [,map ...]} [key]
```

This command allows you to change the default key bindings (operation invoked when pressing a key).

## Binding a Key Sequence to a Function

The `bind` command allows you to assign a new effect to a key (e.g. `a`) or a key sequence (e.g. `gh` — that is pressing `g` followed by a press of `h`).

```
bind map [,map ...] key function
```

*map* specifies in which menu the binding belongs. Multiple maps may be specified by separating them with commas (no additional whitespace is allowed). The currently defined maps are:

| Map | Description |
|---|---|
| `generic` | Fallback for all other menus except pager and editor. If a key is not defined in another menu, NeoMutt will look for a binding to use in this menu. |
| `alias` | The alias menu is the list of your personal aliases as defined in your `.neomuttrc`. |
| `attach` | The attachment menu is used to access the attachments on received messages. |
| `browser` | Used for both browsing the local directory structure, and for listing all of your incoming mailboxes. |
| `editor` | Used to allow the user to enter a single line of text, such as the *To* or *Subject* prompts in the `compose` menu. |
| `index` | The list of messages contained in a mailbox. |
| `compose` | The screen used when sending a new message. |
| `pager` | The mode used to display message/attachment data, and help listings. |
| `pgp` | Used to select the OpenPGP keys used to encrypt outgoing messages. |
| `smime` | Used to select the OpenSSL certificates used to encrypt outgoing messages. |
| `postpone` | Similar to the index menu, except used when recalling a postponed message. |
| `query` | The browser for results returned by `$query_command`. |

### Specifying Keys

*key* is the key (or key sequence) you wish to bind. To specify a control character, use the sequence `\Cx`, where `x` is the letter of the control character (for example, to specify control-A use `\Ca`). Note that the case of `x` as well as `\C` is ignored, so that `\CA`, `\Ca`, `\cA` and `\ca` are all equivalent. An alternative form is to specify the key as a three digit octal number prefixed with a `\` (for example `\177` is equivalent to `\c?`). You can also use the form `<177>`, which allows octal numbers with an arbitrary number of digits.

#### Symbolic Key Names

| Symbolic name | Meaning |
|---|---|
| `\t` | tab |
| `<tab>` | tab |
| `<backtab>` | backtab / shift-tab |
| `\r` | carriage return |
| `\n` | newline |
| `\e` | escape/alt |
| `<esc>` | escape/alt |
| `<up>` | up arrow |
| `<down>` | down arrow |
| `<left>` | left arrow |
| `<right>` | right arrow |
| `<pageup>` | Page Up |
| `<pagedown>` | Page Down |
| `<backspace>` | Backspace |
| `<delete>` | Delete |
| `<insert>` | Insert |
| `<enter>` | Enter |
| `<return>` | Return |
| `<keypadenter>` | Enter key on numeric keypad |
| `<home>` | Home |
| `<end>` | End |
| `<space>` | Space bar |
| `<f1>` | function key 1 |
| `<f10>` | function key 10 |

The `<what-key>` function can be used to explore keycode and symbolic names for other keys on your keyboard. Executing this function will display information about each key pressed, until terminated by `^G`.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Help screen showing key bindings

**Description:** The NeoMutt help screen (opened with `?`) displaying the list of key bindings for the index menu, showing the key column, function column, and description column.

**Highlights:** How bindings are organized by menu, with default and custom bindings listed together.
:::

*key* does not need to be enclosed in quotes unless it contains a space (" ") or semi-colon (";").

*function* specifies which action to take when *key* is pressed. For a complete list of functions, see the reference. Note that the `bind` command expects *function* to be specified without angle brackets.

The special function `<noop>` unbinds the specified key sequence. It is recommended to use `unbind` instead.

## Unbinding a Key Sequence

To remove a binding of a key or key sequence, `unbind` can be used:

```
unbind {* | map [,map ...]} [key]
```

*map* specifies from which menus the key sequence should be removed. Multiple maps may be specified by separating them with commas (no additional whitespace is allowed). If `*` is given, then the key sequence is removed from all menus.

*key* is the key or key sequence to be unbound. It may be omitted in which case all keybindings in the given menus are removed. To prevent NeoMutt from becoming unusable some fallback key bindings are added afterwards.

### Fallback Key Bindings

| Menu | Key | Bound Function |
|---|---|---|
| generic | &lt;enter&gt; | `<select-entry>` |
| generic | &lt;return&gt; | `<select-entry>` |
| generic | : | `<enter-command>` |
| generic | ? | `<help>` |
| generic | q | `<exit>` |
| editor | &lt;backspace&gt; | `<backspace>` |
| editor | \177 | `<backspace>` |
| index | &lt;enter&gt; | `<display-message>` |
| index | &lt;return&gt; | `<display-message>` |
| pager | ? | `<help>` |
| pager | q | `<exit>` |
| pager | : | `<enter-command>` |

A key binding can also be unbound by mapping it to the special function `<noop>`. It is, however, recommended to use `unbind` instead.

## Enter versus Return

Prior to 2022, NeoMutt used a default ncurses mode (`nl()`). This mode maps keyboard input of either `<Enter>` or `<Return>` to the same value, which NeoMutt interpreted as `<Return>` internally.

However, starting in version 2.2, this mode is turned off, allowing `<Return>` and `<Enter>` to be mapped separately, if desired. The default keyboard mappings set both, but you can override this or create new bindings with one or the other (or both).

Note that in terminal applications, such as NeoMutt, `<Enter>` is the same as `\n` and `^J`; while `<Return>` is the same as `\r` and `^M`.

## Warnings about Duplicated Bindings

Due to a limitation of NeoMutt, creating key bindings, or macros, will overwrite existing mappings with similar, shorter, names.

```
bind index g  group-reply
bind index gg first-entry
```

In this example, the `g` binding will be overwritten and cannot be used. Newer versions of NeoMutt will warn the user about this.

To avoid warnings on startup, first set the shorter binding to `noop` (no operation):

```
bind index g  noop
bind index gg first-entry
```

The same is also possible using `unbind`:

```
unbind index g
bind index gg first-entry
```

## Terminal Keybindings

Some key bindings are controlled by the terminal, and so by default can't be bound inside NeoMutt. These may include `^C`, `^\`, `^Q`, `^S`, `^Z`, and on BSD/Mac `^Y`. These terminal settings can be viewed and changed using the `stty` program.

`stty -a` will list the bound characters (not all of them affect NeoMutt), and what actions they take when pressed. For example, you may see `intr = ^C` in its output. This means typing `^C` will send an interrupt signal. `quit = ^\` means typing `^\` (commonly also `^4`) will send a quit signal.

To unbind a key from an action, you invoke `stty action undef`. For example, `stty quit undef` will unbind `^\` (and `^4`) from sending the quit signal. Once unbound (e.g. by placing that line in your .profile, or in a NeoMutt wrapper script/function) you can use the key sequence in your NeoMutt bindings.
