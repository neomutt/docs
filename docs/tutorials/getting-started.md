---
title: Getting Started with NeoMutt
description: A first-steps tutorial introducing NeoMutt's core concepts, screens, and menus
keywords: [neomutt, getting started, tutorial, index, pager, sidebar, menus]
diataxis_type: tutorial
---

# Getting Started with NeoMutt

This tutorial gives you a friendly tour of NeoMutt's main screens and the keys you'll use
every day. You'll launch NeoMutt, move around, and find help when you need it.

If you haven't configured an account yet, start with [Writing Your First Configuration](first-config)
or the guided [Start Here](../start-here) page, then come back for the tour.

The keybindings shown here are the defaults. Your system may differ. In any menu, press `?`
to see the current bindings for your setup.

Start NeoMutt by running `neomutt` in your terminal.

## Quick Tour

1. Start NeoMutt and wait for the message list (the Index).
2. Press `?` to open the help screen and note the keys for moving up and down and for quitting.
3. Use `j` and `k` to move the selection. Use the help screen to find the key that opens a message.
4. In the message view (the Pager), press `?` again to see its keys, then press `q` to return.
5. Press `q` to quit when you're done.

If you want more depth on the screens and menus, keep reading.

## Core Concepts

NeoMutt is a text-based application which interacts with users through different menus which
are mostly line-/entry-based or page-based. A line-based menu is the so-called "index" menu
(listing all messages of the currently opened folder) or the "alias" menu (allowing you to
select recipients from a list). Examples for page-based menus are the "pager" (showing one
message at a time) or the "help" menu listing all available key bindings.

The user interface consists of a context sensitive help line at the top, the menu's contents
followed by a context sensitive status line and finally the command line. The command line is
used to display informational and error messages as well as for prompts and for entering
interactive commands.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** NeoMutt overall UI layout

**Description:** A full terminal window showing NeoMutt's main interface with the context-sensitive help line at the top, the message index in the center, the status line near the bottom, and the command line at the very bottom.

**Highlights:** The four distinct areas of the UI — help line, menu content, status line, and command line — should each be clearly visible and identifiable.
:::

NeoMutt is configured through variables which, if the user wants to permanently use
a non-default value, are written to configuration files. NeoMutt supports a rich config file
syntax to make even complex configuration files readable and commentable.

Because NeoMutt allows for customizing almost all key bindings, there are so-called
"functions" which can be executed manually (using the command line) or in macros. Macros allow
the user to bind a sequence of commands to a single key or a short key sequence instead of
repeating a sequence of actions over and over.

Many commands (such as saving or copying a message to another folder) can be applied to
a single message or a set of messages (so-called "tagged" messages). To help selecting
messages, NeoMutt provides a rich set of message patterns (such as recipients, sender, body
contents, date sent/received, etc.) which can be combined into complex expressions using the
boolean *and* and *or* operations as well as negating. These patterns can also be used to
(for example) search for messages or to limit the index to show only matching messages.

NeoMutt supports a "hook" concept which allows the user to execute arbitrary configuration
commands and functions in certain situations such as entering a folder, starting a new message
or replying to an existing one. These hooks can be used to highly customize NeoMutt's
behavior including managing multiple identities, customizing the display for a folder or even
implementing auto-archiving based on a per-folder basis and much more.

Besides an interactive mode, NeoMutt can also be used as a command-line tool to send messages.

## Screens and Menus

### Index

The index is the screen that you usually see first when you start NeoMutt. It gives an
overview over your emails in the currently opened mailbox. By default, this is your system
mailbox. The information you see in the index is a list of emails, each with its number on the
left, its flags (new email, important email, email that has been forwarded or replied to,
tagged email, ...), the date when email was sent, its sender, the email size, and the subject.
Additionally, the index also shows thread hierarchies: when you reply to an email, and the
other person replies back, you can see the other person's email in a "sub-tree" below. This is
especially useful for personal email between a group of people or when you've subscribed to
mailing lists.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** The Index screen

**Description:** The NeoMutt Index screen showing a list of emails with message numbers, status flags (N for new, r for replied, ! for flagged), dates, sender names, sizes, and subjects. Include some threaded messages to show the tree hierarchy with reply indentation.

**Highlights:** The columnar layout of the message list — flags, date, sender, size, and subject — plus how threads are visually represented with tree characters.
:::

### Pager

The pager is responsible for showing the email content. On the top of the pager you have an
overview over the most important email headers like the sender, the recipient, the subject,
and much more information. How much information you actually see depends on your
configuration, which we'll describe below.

Below the headers, you see the email body which usually contains the message. If the email
contains any attachments, you will see more information about them below the email body, or,
if the attachments are text files, you can view them directly in the pager.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** The Pager screen

**Description:** The NeoMutt Pager displaying an email message, with header fields (From, To, Subject, Date) at the top, the message body below, and the status line at the bottom showing the current position in the message.

**Highlights:** The separation between email headers and body content, the status line showing progress through the message, and any color highlighting of quoted text or URLs.
:::

To give the user a good overview, it is possible to configure NeoMutt to show different things
in the pager with different colors. Virtually everything that can be described with a regular
expression can be colored, e.g. URLs, email addresses or smileys.

### File Browser

The file browser is the interface to the local or remote file system. When selecting
a mailbox to open, the browser allows custom sorting of items, limiting the items shown by
a regular expression and a freely adjustable format of what to display in which way. It also
allows for easy navigation through the file system when selecting file(s) to attach to
a message, select multiple files to attach and many more.

Some mail systems can nest mail folders inside other mail folders. The normal open entry
commands in NeoMutt will open the mail folder and you can't see the sub-folders. If you
instead use the `<descend-directory>` function it will go into the directory and not open it
as a mail directory.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** The File Browser screen

**Description:** The NeoMutt File Browser showing a list of mailboxes or directories, with columns for file size, date, and name. Show a mix of directories and mail folders to illustrate navigation.

**Highlights:** How mailboxes and directories are listed, the sorting columns, and the navigation prompt at the bottom for selecting a mailbox to open.
:::

### Sidebar

The Sidebar shows a list of all your mailboxes. The list can be turned on and off, it can be
themed and the list style can be configured.

This part of the manual is suitable for beginners. If you already know NeoMutt you could skip
ahead to the main Sidebar guide. If you just want to get started, you could use the sample
Sidebar neomuttrc.

**Let's turn on the Sidebar:**

```neomuttrc
set sidebar_visible
set sidebar_format = "%B%<F? [%F]>%* %<N?%N/>%S"
set mail_check_stats
```

You will see something like this. A list of mailboxes on the left. A list of emails, from the
selected mailbox, on the right.

```
Fruit [1]     3/8|  1    + Jan 24  Rhys Lee         (192)  Yew
Animals [1]   2/6|  2    + Feb 11  Grace Hall       (167)  Ilama
Cars            4|  3      Feb 23  Aimee Scott      (450)  Nectarine
Seas          1/7|  4    ! Feb 28  Summer Jackson   (264)  Lemon
                 |  5      Mar 07  Callum Harrison  (464)  Raspberry
                 |  6 N  + Mar 24  Samuel Harris    (353)  Tangerine
                 |  7 N  + Sep 05  Sofia Graham     (335)  Cherry
                 |  8 N    Sep 16  Ewan Brown       (105)  Ugli
                 |
                 |
```

This user has four mailboxes: "Fruit", "Cars", "Animals" and "Seas".

The current, open, mailbox is "Fruit". We can also see information about the other mailboxes.
For example: The "Animals" mailbox contains, 1 flagged email, 2 new emails out of a total of
6 emails.

#### Navigation

The Sidebar adds some new functions to NeoMutt.

The user pressed the "c" key to `<change-folder>` to the "Animals" mailbox. The Sidebar
automatically updated the indicator to match.

```
Fruit [1]     3/8|  1      Jan 03  Tia Gibson       (362)  Caiman
Animals [1]   2/6|  2    + Jan 22  Rhys Lee         ( 48)  Dolphin
Cars            4|  3    ! Aug 16  Ewan Brown       (333)  Hummingbird
Seas          1/7|  4      Sep 25  Grace Hall       ( 27)  Capybara
                 |  5 N  + Nov 12  Evelyn Rogers    (453)  Tapir
                 |  6 N  + Nov 16  Callum Harrison  (498)  Hedgehog
                 |
                 |
                 |
                 |
```

Let's map some functions:

```neomuttrc
bind index,pager \CP sidebar-prev       # Ctrl-P – Previous Mailbox
bind index,pager \CN sidebar-next       # Ctrl-N – Next Mailbox
bind index,pager \CO sidebar-open       # Ctrl-O – Open Highlighted Mailbox
```

Pressing "Ctrl-N" (Next mailbox) twice will move the Sidebar **highlight** down to the "Seas"
mailbox.

```
Fruit [1]     3/8|  1      Jan 03  Tia Gibson       (362)  Caiman
Animals [1]   2/6|  2    + Jan 22  Rhys Lee         ( 48)  Dolphin
Cars            4|  3    ! Aug 16  Ewan Brown       (333)  Hummingbird
Seas          1/7|  4      Sep 25  Grace Hall       ( 27)  Capybara
                 |  5 N  + Nov 12  Evelyn Rogers    (453)  Tapir
                 |  6 N  + Nov 16  Callum Harrison  (498)  Hedgehog
                 |
                 |
                 |
                 |
```

:::{note}
Functions `<sidebar-next>` and `<sidebar-prev>` move the Sidebar **highlight**. They
**do not** change the open mailbox.
:::

Press "Ctrl-O" (`<sidebar-open>`) to open the highlighted mailbox.

```
Fruit [1]     3/8|  1    ! Mar 07  Finley Jones     (139)  Molucca Sea
Animals [1]   2/6|  2    + Mar 24  Summer Jackson   ( 25)  Arafura Sea
Cars            4|  3    + Feb 28  Imogen Baker     (193)  Pechora Sea
Seas          1/7|  4 N  + Feb 23  Isla Hussain     (348)  Balearic Sea
                 |
                 |
                 |
                 |
                 |
                 |
```

#### Features

The Sidebar shows a list of mailboxes in a panel.

Everything about the Sidebar can be configured.

**State of the Sidebar**
- Visibility
- Width

**Which mailboxes are displayed**
- Display all
- Limit to mailboxes with new mail
- Pin mailboxes to display always

**The order in which mailboxes are displayed**
- Unsorted (order of mailboxes commands)
- Sorted alphabetically
- Sorted by number of new mails

**Color**
- Sidebar indicators and divider
- Mailboxes depending on their type
- Mailboxes depending on their contents

**Key bindings**
- Hide/Unhide the Sidebar
- Select previous/next mailbox
- Select previous/next mailbox with new mail
- Page up/down through a list of mailboxes

**Misc**
- Formatting string for mailbox
- Wraparound searching
- Flexible mailbox abbreviations
- Support for Unicode mailbox names (UTF-8)

#### Display

Everything about the Sidebar can be configured.

For a quick reference:
- Sidebar variables to set
- Sidebar colors to apply
- Sidebar sort methods

##### Sidebar Basics

The most important variable is `$sidebar_visible`. You can set this in your "neomuttrc", or
bind a key to the function `<sidebar-toggle-visible>`.

```neomuttrc
set sidebar_visible                         # Make the Sidebar visible by default
bind index,pager B sidebar-toggle-visible   # Use 'B' to switch the Sidebar on and off
```

Next, decide how wide you want the Sidebar to be. 25 characters might be enough for the
mailbox name and some numbers. Remember, you can hide/show the Sidebar at the press of
button.

Finally, you might want to change the divider character. By default, Sidebar draws an ASCII
line between it and the Index panel. If your terminal supports it, you can use a Unicode
line-drawing character.

```neomuttrc
set sidebar_width = 25                  # Plenty of space
set sidebar_divider_char = '│'          # Pretty line-drawing character
```

##### Sidebar Format String

`$sidebar_format` allows you to customize the Sidebar display. For an introduction, read
about format strings including the section about conditionals.

The default value is: `%D%* %n`

A more detailed value is: `%B%<F? [%F]>%* %<N?%N/>%S`

Which breaks down as:
- `%B` – Mailbox name
- `%<F? [%F]>` – If flagged emails `[%F]`, otherwise nothing
- `%*` – Pad with spaces
- `%<N?%N/>` – If new emails `%N/`, otherwise nothing
- `%S` – Total number of emails

| Format | Notes | Description |
|--------|-------|-------------|
| `%B` | | Name of the mailbox |
| `%d` | * ‡ | Number of deleted messages |
| `%D` | | Descriptive name of the mailbox |
| `%F` | * † | Number of flagged messages in the mailbox |
| `%L` | * ‡ | Number of messages after limiting |
| `%n` | * | If there's new mail, display "N", otherwise " " (space) |
| `%N` | * † | Number of unread messages in the mailbox (seen or unseen) |
| `%o` | * † | Number of old messages in the mailbox (unread, but seen) |
| `%r` | * † | Number of read messages in the mailbox |
| `%S` | * † | Size of mailbox (total number of messages) |
| `%t` | * ‡ | Number of tagged messages in the mailbox |
| `%Z` | * † | Number of new messages in the mailbox (unread, unseen) |
| `%!` | | "!": one flagged message; "!!": two flagged messages; "n!": n flagged messages (for n > 2). Otherwise prints nothing. |
| `%>X` | | Right justify the rest of the string and pad with "X" |
| `%\|X` | | Pad to the end of the line with "X" |
| `%*X` | | Soft-fill with character "X" as pad |

\* = Can be optionally printed if nonzero

† = To use these expandos, you must first:

```neomuttrc
set mail_check_stats
```

‡ = Only applicable to the current folder

Here are some examples. They show the number of (F)lagged, (N)ew and (S)ize.

| Format | Example |
|--------|---------|
| `%B%<F? [%F]>%* %<N?%N/>%S` | `mailbox [F]            N/S` |
| `%B%* %F:%N:%S` | `mailbox              F:N:S` |
| `%B %<N?(%N)>%* %S` | `mailbox (N)              S` |
| `%B%* %<F?%F/>%N` | `mailbox                F/S` |

##### Abbreviating Mailbox Names

`$sidebar_delim_chars` tells Sidebar how to split up mailbox paths. For local directories use
"/"; for IMAP folders use "."

**Example 1**

This example works well if your mailboxes have unique names after the last separator.

Add some mailboxes of different depths.

```neomuttrc
set folder="~/mail"
mailboxes =fruit/apple          =fruit/banana          =fruit/cherry
mailboxes =water/sea/sicily     =water/sea/archipelago =water/sea/sibuyan
mailboxes =water/ocean/atlantic =water/ocean/pacific   =water/ocean/arctic
```

Shorten the names:

```neomuttrc
set sidebar_short_path                  # Shorten mailbox names (truncate all subdirs)
set sidebar_component_depth=1           # Shorten mailbox names (truncate 1 subdirs)
set sidebar_delim_chars="/"             # Delete everything up to the last or Nth / character
```

The screenshot below shows what the Sidebar would look like before and after shortening using
`sidebar_short_path`.

```
|fruit/apple                            |apple
|fruit/banana                           |banana
|fruit/cherry                           |cherry
|water/sea/sicily                       |sicily
|water/sea/archipelago                  |archipelago
|water/sea/sibuyan                      |sibuyan
|water/ocean/atlantic                   |atlantic
|water/ocean/pacific                    |pacific
|water/ocean/arctic                     |arctic
```

The screenshot below shows what the Sidebar would look like before and after shortening using
`sidebar_component_depth=1`.

```
|fruit/apple                            |apple
|fruit/banana                           |banana
|fruit/cherry                           |cherry
|water/sea/sicily                       |sea/sicily
|water/sea/archipelago                  |sea/archipelago
|water/sea/sibuyan                      |sea/sibuyan
|water/ocean/atlantic                   |ocean/atlantic
|water/ocean/pacific                    |ocean/pacific
|water/ocean/arctic                     |ocean/arctic
```

**Example 2**

This example works well if you have lots of mailboxes which are arranged in a tree.

Add some mailboxes of different depths.

```neomuttrc
set folder="~/mail"
mailboxes =fruit
mailboxes =fruit/apple =fruit/banana =fruit/cherry
mailboxes =water
mailboxes =water/sea
mailboxes =water/sea/sicily =water/sea/archipelago =water/sea/sibuyan
mailboxes =water/ocean
mailboxes =water/ocean/atlantic =water/ocean/pacific =water/ocean/arctic
```

Shorten the names:

```neomuttrc
set sidebar_short_path                  # Shorten mailbox names
set sidebar_delim_chars="/"             # Delete everything up to the last / character
set sidebar_folder_indent               # Indent folders whose names we've shortened
set sidebar_indent_string="  "          # Indent with two spaces
```

The screenshot below shows what the Sidebar would look like before and after shortening.

```
|fruit                                  |fruit
|fruit/apple                            |  apple
|fruit/banana                           |  banana
|fruit/cherry                           |  cherry
|water                                  |water
|water/sea                              |  sea
|water/sea/sicily                       |    sicily
|water/sea/archipelago                  |    archipelago
|water/sea/sibuyan                      |    sibuyan
|water/ocean                            |  ocean
|water/ocean/atlantic                   |    atlantic
|water/ocean/pacific                    |    pacific
|water/ocean/arctic                     |    arctic
```

Sometimes, it will be necessary to add mailboxes, that you don't use, to fill in part of the
tree. This will trade vertical space for horizontal space (but it looks good).

##### Limiting the Number of Mailboxes

If you have a lot of mailboxes, sometimes it can be useful to hide the ones you aren't using.
`$sidebar_new_mail_only` tells Sidebar to only show mailboxes that contain new, or flagged,
email.

Sometimes it is useful to only show mailboxes that have mails in them, while hiding the rest.
`$sidebar_non_empty_mailbox_only` tells the Sidebar to only show mailboxes with a non-zero
number of mails.

If you want some mailboxes to be always visible, then use the `sidebar-pin` command. It takes
a list of mailboxes as parameters.

```neomuttrc
set sidebar_new_mail_only         # Only mailboxes with new/flagged email
sidebar-pin +fruit +fruit/apple   # Always display these two mailboxes
```

#### Colors

Here is a sample color scheme:

```neomuttrc
color sidebar_background default black       # Black background
color sidebar_indicator  default color17     # Dark blue background
color sidebar_highlight  white   color238    # Grey background
color sidebar_spool_file yellow  default     # Yellow
color sidebar_unread     cyan    default     # Light blue
color sidebar_new        green   default     # Green
color sidebar_ordinary   default default     # Default colors
color sidebar_flagged    red     default     # Red
color sidebar_divider    color8  default     # Dark grey
```

There is a priority order when coloring Sidebar mailboxes. e.g. If a mailbox has new mail it
will have the `sidebar_new` color, even if it also contains flagged mails.

| Priority | Color | Description |
|----------|-------|-------------|
| Highest | `sidebar_indicator` | Mailbox is open |
| | `sidebar_highlight` | Mailbox is highlighted |
| | `sidebar_new` | Mailbox contains new mail |
| | `sidebar_unread` | Mailbox contains unread mail |
| | `sidebar_flagged` | Mailbox contains flagged mail |
| | `sidebar_spool_file` | Mailbox is the spool_file (receives incoming mail) |
| Lowest | `sidebar_ordinary` | Mailbox does not match above |

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Sidebar with color theme applied

**Description:** The NeoMutt Sidebar panel with the color scheme from the example above applied, showing mailboxes in different colors — green for new mail, cyan for unread, red for flagged, and the dark blue indicator on the currently open mailbox.

**Highlights:** How color-coding makes it easy to spot mailboxes with new, unread, or flagged messages at a glance, and how the indicator and highlight colors differ.
:::

### Help

The help screen is meant to offer a quick help to the user. It lists the current
configuration of key bindings and their associated commands including a short description, and
currently unbound functions that still need to be associated with a key binding (or
alternatively, they can be called via the NeoMutt command prompt).

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** The Help screen

**Description:** The NeoMutt Help screen showing a list of key bindings and their associated functions with short descriptions, as displayed when pressing `?` from the Index.

**Highlights:** The two-column layout of key bindings paired with function names and descriptions, and the section showing unbound functions at the bottom.
:::

### Compose Menu

The compose menu features a split screen containing the information which really matters
before actually sending a message by mail: who gets the message as what (recipients and who
gets what kind of copy). Additionally, users may set security options like deciding whether to
sign, encrypt or sign and encrypt a message with/for what keys. Also, it's used to attach
messages, to re-edit any attachment including the message itself.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** The Compose Menu screen

**Description:** The NeoMutt Compose Menu showing the split-screen layout with header fields at the top (From, To, Cc, Bcc, Subject, Reply-To, Fcc), security settings (PGP/S/MIME options), and the list of attachments at the bottom.

**Highlights:** The editable header fields, the security option indicators, and how attachments are listed with their MIME types and sizes.
:::

### Alias Menu

The alias menu is used to help users finding the recipients of messages. For users who need to
contact many people, there's no need to remember addresses or names completely because it
allows for searching, too. The alias mechanism and thus the alias menu also features grouping
several addresses by a shorter nickname, the actual alias, so that users don't have to select
each single recipient manually. The alias menu is also used to display the result of external
address queries.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** The Alias Menu screen

**Description:** The NeoMutt Alias Menu showing a list of defined aliases with nicknames, real names, and email addresses, as displayed when selecting recipients for a message.

**Highlights:** How aliases group multiple addresses under short nicknames, the search capability for finding contacts, and how selected aliases are highlighted.
:::

### Attachment Menu

As will be later discussed in detail, NeoMutt features a good and stable MIME implementation,
that is, it supports sending and receiving messages of arbitrary MIME types. The attachment
menu displays a message's structure in detail: what content parts are attached to which parent
part (which gives a true tree structure), which part is of what type and what size. Single
parts may saved, deleted or modified to offer great and easy access to message's internals.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** The Attachment Menu screen

**Description:** The NeoMutt Attachment Menu displaying a message with multiple attachments in a tree structure, showing parent/child MIME parts with their content types (e.g., text/plain, image/jpeg, application/pdf), sizes, and descriptions.

**Highlights:** The tree structure showing how MIME parts are nested, the content type and size columns, and the menu options for saving or viewing individual attachments.
:::

## Moving Around in Menus

The most important navigation keys common to line- or entry-based menus are shown below, as
well as keys for page-based menus.

### Navigation Keys in Entry-Based Menus

| Key | Function | Description |
|-----|----------|-------------|
| j or \<Down\> | `<next-entry>` | Move to the next entry |
| k or \<Up\> | `<previous-entry>` | Move to the previous entry |
| z or \<PageDn\> | `<next-page>` | go to the next page |
| Z or \<PageUp\> | `<previous-page>` | go to the previous page |
| = or \<Home\> | `<first-entry>` | jump to the first entry |
| \* or \<End\> | `<last-entry>` | jump to the last entry |
| q | `<quit>` | exit the current menu |
| ? | `<help>` | list all keybindings for the current menu |

### Navigation Keys in Page-Based Menus

| Key | Function | Description |
|-----|----------|-------------|
| J or \<Return\> | `<next-line>` | Scroll down one line |
| \<Backspace\> | `<previous-line>` | Scroll up one line |
| K, \<Space\> or \<PageDn\> | `<next-page>` | Move to the next page |
| \- or \<PageUp\> | `<previous-page>` | move the previous page |
| \<Home\> | `<top>` | move to the top |
| \<End\> | `<bottom>` | move to the bottom |

## Next Steps

- "I want to connect my account." Go to [Writing Your First Configuration](first-config), or choose your provider in [Start Here](../start-here).
- "I want to read and send mail." Continue with [Reading Your First Email](first-email) and [Sending Email](sending-email).
- "I want a shortcut list of keys." See the [Shortcuts Reference](../reference/shortcuts).
