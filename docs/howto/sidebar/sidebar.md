---
title: Sidebar
description: Set up and customise NeoMutt's Sidebar panel to list mailboxes, navigate between them, configure sorting, and apply colour themes.
keywords: sidebar, mailbox, navigation, sidebar_visible, sidebar_format, sidebar_sort, sidebar_width, sidebar-pin, sidebar-open, sidebar-next, sidebar-toggle-visible, colors, mail_check_stats
---

# Sidebar

The Sidebar shows a list of all your mailboxes.
The list can be turned on and off, it can be themed and the list style can be configured.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Sidebar overview with mailbox list

**Description:** NeoMutt index view with the sidebar visible on the left side, showing a list of mailboxes (Inbox, Sent, Drafts, Trash, and several mailing list folders).
The sidebar shows mailbox names with unread/total message counts.
One mailbox is highlighted (the cursor), another is indicated (the currently open mailbox).
The divider character separates the sidebar from the index panel on the right.

**Highlights:** The overall layout — sidebar panel on the left with the divider character, the highlight bar on one mailbox, the indicator on the open mailbox, and message counts displayed via [`$sidebar_format`](cfg-sidebar-format).
:::

If you want a simple introduction with examples see the Sidebar Howto.
If you just want to get started, you could use the sample [neomuttrc](#sidebar-neomuttrc) below.

## Variables

| Name                             | Type    | Default           |
|----------------------------------|---------|-------------------|
| `sidebar_component_depth`        | number  | `0`               |
| `sidebar_delim_chars`            | string  | `/.`              |
| `sidebar_divider_char`           | string  | `\|`              |
| `sidebar_folder_indent`          | boolean | `no`              |
| `sidebar_format`                 | string  | `%D%* %n`         |
| `sidebar_indent_string`          | string  | `  ` (two spaces) |
| `sidebar_new_mail_only`          | boolean | `no`              |
| `sidebar_next_new_wrap`          | boolean | `no`              |
| `sidebar_non_empty_mailbox_only` | boolean | `no`              |
| `sidebar_on_right`               | boolean | `no`              |
| `sidebar_short_path`             | boolean | `no`              |
| `sidebar_sort`                   | enum    | `unsorted`        |
| `sidebar_visible`                | boolean | `no`              |
| `sidebar_width`                  | number  | `20`              |

For more details, and examples, about the [`$sidebar_format`](cfg-sidebar-format), see the Sidebar Intro.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Sidebar with short paths and folder indentation

**Description:** NeoMutt sidebar showing mailboxes with `sidebar_short_path=yes`
and `sidebar_folder_indent=yes` enabled — nested IMAP folders or Maildir
subfolders appear with abbreviated names and indentation showing their hierarchy
(e.g. "lists" at the top level, then "  neomutt-devel" and "  neomutt-users"
indented beneath it).

**Highlights:** The indented folder hierarchy in the sidebar — how `sidebar_short_path` abbreviates long paths and `sidebar_folder_indent` with `sidebar_indent_string` creates a visual tree of nested mailboxes.
:::

## Functions

Sidebar adds the following functions to NeoMutt.
By default, none of them are bound to keys.

| Menus       | Function                   | Description                                          |
|-------------|----------------------------|------------------------------------------------------|
| index,pager | [`<sidebar-next>`](fn-sidebar-next)           | Move the highlight to next mailbox                   |
| index,pager | [`<sidebar-next-new>`](fn-sidebar-next-new)       | Move the highlight to next mailbox with new mail     |
| index,pager | [`<sidebar-open>`](fn-sidebar-open)           | Open highlighted mailbox                             |
| index,pager | [`<sidebar-page-down>`](fn-sidebar-page-down)      | Scroll the Sidebar down 1 page                       |
| index,pager | [`<sidebar-page-up>`](fn-sidebar-page-up)        | Scroll the Sidebar up 1 page                         |
| index,pager | [`<sidebar-prev>`](fn-sidebar-prev)           | Move the highlight to previous mailbox               |
| index,pager | [`<sidebar-prev-new>`](fn-sidebar-prev-new)       | Move the highlight to previous mailbox with new mail |
| index,pager | [`<sidebar-toggle-visible>`](fn-sidebar-toggle-visible) | Make the Sidebar (in)visible                         |

## Commands

Usage:

```neomuttrc
sidebar-pin <mailbox> [<mailbox> ...]
sidebar-unpin { * | <mailbox> [<mailbox> ...] }
```

:::{note}
Before 2026-01-13, these commands were called `sidebar_pin` and `sidebar_unpin`.
:::

This command specifies mailboxes that will always be displayed in the sidebar, even if [`$sidebar_new_mail_only`](cfg-sidebar-new-mail-only) is set and the mailbox does not contain new mail.

The [`:sidebar-unpin`](cmd-sidebar-unpin) command is used to remove a mailbox from the list of always displayed mailboxes.
Use `sidebar-unpin *` to remove all mailboxes.

## Colors

| Name                 | Default Color       | Description                                                      |
|----------------------|---------------------|------------------------------------------------------------------|
| `sidebar_background` | default             | The entire sidebar panel                                         |
| `sidebar_divider`    | default             | The dividing line between the Sidebar and the Index/Pager panels |
| `sidebar_flagged`    | default             | Mailboxes containing flagged mail                                |
| `sidebar_highlight`  | underline           | Cursor to select a mailbox                                       |
| `sidebar_indicator`  | neomutt `indicator` | The mailbox open in the Index panel                              |
| `sidebar_new`        | default             | Mailboxes containing new mail                                    |
| `sidebar_ordinary`   | default             | Mailboxes that have no new/flagged mails, etc.                   |
| `sidebar_spool_file` | default             | Mailbox that receives incoming mail                              |
| `sidebar_unread`     | default             | Mailboxes containing unread mail                                 |

If the `sidebar_indicator` color isn't set, then the default NeoMutt indicator color will be used (the color used in the index panel).

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Sidebar colour scheme

**Description:** NeoMutt sidebar with a custom colour theme applied — mailboxes with new mail appear in green (`sidebar_new`), flagged-mail mailboxes in red (`sidebar_flagged`), the currently open mailbox is highlighted with `sidebar_indicator`, the cursor/highlight bar is visible on a different mailbox (`sidebar_highlight`), and the divider line uses a contrasting colour (`sidebar_divider`).

**Highlights:** The distinct colour coding — how different sidebar colour objects (new, flagged, indicator, highlight, ordinary, divider) work together to convey mailbox status at a glance.
:::

## Sort

| Sort       | Description                            |
|------------|----------------------------------------|
| `alpha`    | Alphabetically by path or label        |
| `count`    | Total number of messages               |
| `desc`     | Descriptive name of the mailbox        |
| `flagged`  | Number of flagged messages             |
| `name`     | Alphabetically by path or label        |
| `new`      | Number of unread messages              |
| `path`     | Alphabetically by path (ignores label) |
| `unread`   | Number of unread messages              |
| `unsorted` | Order of the [`:mailboxes`](cmd-mailboxes) command |

(sidebar-neomuttrc)=
## neomuttrc

```neomuttrc
# Example NeoMutt config file for the sidebar feature.

# --------------------------------------------------------------------------
# VARIABLES – shown with their default values
# --------------------------------------------------------------------------
# Should the Sidebar be shown?
set sidebar_visible = no
# How wide should the Sidebar be in screen columns?

# Note: Some characters, e.g. Chinese, take up two columns each.
set sidebar_width = 20
# Should the mailbox paths be abbreviated?
set sidebar_short_path = no
# Number of top-level mailbox path subdirectories to truncate for display
set sidebar_component_depth = 0
# When abbreviating mailbox path names, use any of these characters as path
# separators. Only the part after the last separators will be shown.
# For file folders '/' is good. For IMAP folders, often '.' is useful.
set sidebar_delim_chars = '/.'
# If the mailbox path is abbreviated, should it be indented?
set sidebar_folder_indent = no
# Indent mailbox paths with this string.
set sidebar_indent_string = '  '
# Make the Sidebar only display mailboxes that contain new, or flagged,
# mail.
set sidebar_new_mail_only = no
# Any mailboxes that are pinned will always be visible, even if the
# sidebar_new_mail_only option is enabled.
set sidebar_non_empty_mailbox_only = no
# Only show mailboxes that contain some mail
sidebar-pin '/home/user/mailbox1'
sidebar-pin '/home/user/mailbox2'
# When searching for mailboxes containing new mail, should the search wrap
# around when it reaches the end of the list?
set sidebar_next_new_wrap = no
# Show the Sidebar on the right-hand side of the screen
set sidebar_on_right = no
# The character to use as the divider between the Sidebar and the other NeoMutt
# panels.
set sidebar_divider_char = '|'
# Enable extended mailbox mode to calculate total, new, and flagged
# message counts for each mailbox.
set mail_check_stats
# Display the Sidebar mailboxes using this format string.
set sidebar_format = '%B%<F? [%F]>%* %<N?%N/>%S'
# Sort the mailboxes in the Sidebar using this method:
#       count    – total number of messages
#       flagged  – number of flagged messages
#       unread   – number of unread messages
#       path     – mailbox path
#       unsorted – do not sort the mailboxes
set sidebar_sort = 'unsorted'
# --------------------------------------------------------------------------
# FUNCTIONS – shown with an example mapping
# --------------------------------------------------------------------------
# Move the highlight to the previous mailbox
bind index,pager \Cp sidebar-prev
# Move the highlight to the next mailbox
bind index,pager \Cn sidebar-next
# Open the highlighted mailbox
bind index,pager \Co sidebar-open
# Move the highlight to the previous page
# This is useful if you have a LOT of mailboxes.
bind index,pager <F3> sidebar-page-up
# Move the highlight to the next page
# This is useful if you have a LOT of mailboxes.
bind index,pager <F4> sidebar-page-down
# Move the highlight to the previous mailbox containing new, or flagged,
# mail.
bind index,pager <F5> sidebar-prev-new
# Move the highlight to the next mailbox containing new, or flagged, mail.
bind index,pager <F6> sidebar-next-new
# Toggle the visibility of the Sidebar.
bind index,pager B sidebar-toggle-visible
# --------------------------------------------------------------------------
# COLORS – some unpleasant examples are given
# --------------------------------------------------------------------------
# Note: All color operations are of the form:
#       color OBJECT FOREGROUND BACKGROUND
# Color of the current, open, mailbox
# Note: This is a general NeoMutt option which colors all selected items.
color indicator cyan black
# Sidebar-specific color of the selected item
color sidebar_indicator cyan black
# Color of the highlighted, but not open, mailbox.
color sidebar_highlight black color8
# Color of the entire Sidebar panel
color sidebar_background default black
# Color of the divider separating the Sidebar from NeoMutt panels
color sidebar_divider color8 black
# Color to give mailboxes containing flagged mail
color sidebar_flagged red black
# Color to give mailboxes containing new mail
color sidebar_new green black
# Color to give mailboxes containing no new/flagged mail, etc.
color sidebar_ordinary color245 default
# Color to give the spool_file mailbox
color sidebar_spool_file color207 default
# Color to give mailboxes containing no unread mail
color sidebar_unread color136 default
# --------------------------------------------------------------------------

# vim: filetype=neomuttrc
```

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Fully configured sidebar

**Description:** NeoMutt with the complete sidebar configuration from the neomuttrc example applied — sidebar visible on the left with custom width, format string showing flagged counts and new/total (`%B%<F? [%F]>%* %<N?%N/>%S`), colour-coded mailboxes, key bindings active, and the divider separating sidebar from the index panel showing a threaded mailbox.

**Highlights:** The complete sidebar experience — formatted mailbox names with conditional flagged counts, new/total message numbers right-aligned, colour-coded status, and the spatial relationship between the sidebar panel, divider, and index panel.
:::

## See Also

- Regular Expressions
- Patterns
- [Color command](../colours.md)
- notmuch feature
