---
title: Custom Tagging
description: Tag messages for batch operations and use custom backend-based tags with Notmuch and IMAP
keywords: tags, tagging, tag-pattern, tag-prefix, custom tags, notmuch, imap, hidden_tags, tag-transforms, tag-formats, modify-labels
since: 2017-10-13
---

# Custom Tagging

Some backends allow to index and tag mail without storing the tags within the mail envelope. Two backends are currently implementing this feature. Notmuch handles them natively and IMAP stores them in custom IMAP keywords.

## Variables

| Name          | Type   | Default                                                           |
|---------------|--------|-------------------------------------------------------------------|
| `hidden_tags` | string | `unread,draft,flagged,passed,replied,attachment,signed,encrypted` |

## Functions

Notmuch adds the following functions to NeoMutt. By default, none of them are bound to keys.

| Menus       | Function                    | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| index,pager | `<modify-labels>`           | add, remove, or toggle tags: IMAP: edit the tags list Notmuch: [+]\<tag\> to add, -\<tag\> to remove, !\<tag\> to toggle(notmuch) tags. Note: Tab completion of tag names is available                                                                                                                                                                                                                       |
| index,pager | `<modify-labels-then-hide>` | add, remove, or toggle tags IMAP: edit the tags list Notmuch: [+]\<tag\> to add, -\<tag\> to remove, !\<tag\> to toggle labels and then hide or unhide the message by changing the "quasi-deleted" to match if it would be shown when requerying. Normal redisplay rules apply here, so the user must call \<sync-mailbox\> for the changes to be displayed. Note: Tab completion of tag names is available. |

## Commands

```neomuttrc
tag-transforms tag transformed-string { tag transformed-string ...}
tag-formats    tag format-string      { tag format-string ...}
```

## Colors

Adds the objects, below, to index-color feature. The objects can take an optional pattern.

| Object       | Highlights                                   |
|--------------|----------------------------------------------|
| `index_tag`  | an individual message tag, %G, uses tag name |
| `index_tags` | the transformed message tags, %g or %J       |

## neomuttrc

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

## Credits

Mehdi Abaakouk, Richard Russon, Bernard 'Guyzmo' Pratz

