---
title: How to Use Message Tagging
description: Tag messages for batch operations and use custom backend-based tags with Notmuch and IMAP
keywords: tags, tagging, tag-pattern, tag-prefix, custom tags, notmuch, imap, hidden_tags, tag-transforms, tag-formats, modify-labels
---

# How to Use Message Tagging

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

## Using Tags

Sometimes it is desirable to perform an operation on a group of messages all at once rather than one at a time. An example might be to save messages to a mailing list to a separate folder, or to delete all messages with a given subject. To tag all messages matching a pattern, use the `<tag-pattern>` function, which is bound to "shift-T" by default. Patterns are completable in the editor menu. Invoke the `<complete>` function (by default bound to "Tab") after typing `~` to get a selectable list. Or you can select individual messages by hand using the `<tag-message>` function, which is bound to "t" by default. See [patterns](../reference/patterns.md) for NeoMutt's pattern matching syntax.

Once you have tagged the desired messages, you can use the "tag-prefix" operator, which is the ";" (semicolon) key by default.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Tagged messages in the index

**Description:** The NeoMutt index view showing several messages that have been tagged (marked with `*` in the tag indicator column) using `<tag-message>` or `<tag-pattern>`, with untagged messages shown without the marker for contrast.

**Highlights:** The `*` tag indicator in the flags column, how tagged messages are visually distinguished from untagged ones, and the status bar showing the count of tagged messages.
:::

When the "tag-prefix" operator is used, the *next* operation will be applied to all tagged messages if that operation can be used in that manner. If the `$auto_tag` variable is set, the next operation applies to the tagged messages automatically, without requiring the "tag-prefix".

In `macro` or `push` commands, you can use the `<tag-prefix-cond>` operator. If there are no tagged messages, NeoMutt will "eat" the rest of the macro to abort its execution. NeoMutt will stop "eating" the macro when it encounters the `<end-cond>` operator; after this operator the rest of the macro will be executed as normal.

## Custom Backend-Based Tags

Some backends allow to index and tag mail without storing the tags within the mail envelope. Two backends are currently implementing this feature. Notmuch handles them natively and IMAP stores them in custom IMAP keywords.

### Variables

| Name | Type | Default |
|------|------|---------|
| `hidden_tags` | string | `unread,draft,flagged,passed,replied,attachment,signed,encrypted` |

### Functions

Notmuch adds the following functions to NeoMutt. By default, none of them are bound to keys.

| Menus | Function | Description |
|-------|----------|-------------|
| index,pager | `<modify-labels>` | add, remove, or toggle tags: IMAP: edit the tags list Notmuch: [+]\<tag\> to add, -\<tag\> to remove, !\<tag\> to toggle(notmuch) tags. Note: Tab completion of tag names is available |
| index,pager | `<modify-labels-then-hide>` | add, remove, or toggle tags IMAP: edit the tags list Notmuch: [+]\<tag\> to add, -\<tag\> to remove, !\<tag\> to toggle labels and then hide or unhide the message by changing the "quasi-deleted" to match if it would be shown when requerying. Normal redisplay rules apply here, so the user must call \<sync-mailbox\> for the changes to be displayed. Note: Tab completion of tag names is available. |

### Commands

```neomuttrc
tag-transforms tag transformed-string { tag transformed-string ...}
tag-formats    tag format-string      { tag format-string ...}
```

### Colors

Adds the objects, below, to index-color feature. The objects can take an optional pattern.

| Object | Highlights |
|--------|-----------|
| `index_tag` | an individual message tag, %G, uses tag name |
| `index_tags` | the transformed message tags, %g or %J |

### neomuttrc

```neomuttrc
# Example NeoMutt config file for the custom tags feature.

# VARIABLES – shown with their default values
# --------------------------------------------------------------------------
# This variable specifies private notmuch tags which should not be printed
# on screen (index, pager).
set hidden_tags = "unread,draft,flagged,passed,replied,attachment,signed,encrypted"
# --------------------------------------------------------------------------
# FUNCTIONS – shown with an example mapping
# --------------------------------------------------------------------------
# modify (notmuch/imap) tags
bind index,pager ` modify-labels
# modify (notmuch/imap) tag non-interactively.
macro index,pager tt "<modify-labels>!todo\n" "Toggle the 'todo' tag"
# modify labels and then hide message
# bind index,pager ??? modify-labels-then-hide
# --------------------------------------------------------------------------
# COMMANDS – shown with an example
# --------------------------------------------------------------------------
# Replace some tags with icons
# tag-transforms tag transformed-string { tag transformed-string ...}
# tag-transforms "inbox"   "i"   \
#                "unread"  "u"   \
#                "replied" "↻ "  \
#                "sent"    "➥ "  \
#                "todo"    "T"   \
#                "deleted" "DEL" \
#                "invites" "CAL"

# The formats must start with 'G' and the entire sequence is case sensitive.
# tag-formats tag format-string { tag format-string ...}
# tag-formats "inbox"   "GI" \
#             "unread"  "GU" \
#             "replied" "GR" \
#             "sent"    "GS" \
#             "todo"    "Gt" \
#             "deleted" "GD" \
#             "invites" "Gi"

# Now instead of using '%g' or '%J' in your $index_format, which lists all tags
# in a non-deterministic order, you can something like the following which puts
# a transformed tag name in a specific spot on the index line:
# set index_format='%4C %S %[%y.%m.%d] %-18.18n %<GU?%GU& > %<GR?%GR& > %<GI?%GI& > %s'

# The %G formatting sequence may display all tags including tags hidden by
# hidden_tags.
#
# --------------------------------------------------------------------------
# COLORS – some unpleasant examples are given
# --------------------------------------------------------------------------
# These symbols are added to the index-color feature:
# an individual message tag, %G, uses tag name
color index_tag red white "inbox"
# the transformed message tags, %g
color index_tags green default
# --------------------------------------------------------------------------

# vim: filetype=neomuttrc
```

### Credits

Mehdi Abaakouk, Richard Russon, Bernard 'Guyzmo' Pratz

---

## Marking Messages

There are times when it is useful to ask NeoMutt to "remember" which message you are currently looking at while you move elsewhere in your mailbox. You can do this with the `<mark-message>` function, which is bound to the `~` key by default.

### Workflow

1. Press `~` to mark the current message and enter an identifier (e.g. `a`).
2. Navigate freely within your mailbox.
3. Press `'a` to jump back to the marked message.

Message marking is implemented as a shortcut for defining a macro that returns you to the current message by searching for its Message-ID. You can choose a different prefix key by setting the `$mark_macro_prefix` variable.

### Variables

| Name | Type | Default |
|---|---|---|
| `mark_macro_prefix` | string | `'` |
