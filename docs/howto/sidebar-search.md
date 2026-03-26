---
title: Sidebar Search
description: Filter and jump to any sidebar mailbox by typing a few characters using real-time fuzzy matching
keywords: sidebar, search, fuzzy, sidebar-start-search, sidebar-abort-search, mailbox, filter, smart case, ranking, navigation panel, folder list, sidebar_format, fuzzy-score
since: 2026-03-01
---

# Sidebar Search

## Support

**Since:** NeoMutt 2026-03-01

:::{note}
This feature is under active development. Its behaviour and
keybindings may change in future releases.
:::

## Introduction

Sidebar Search lets you jump to any mailbox in the Sidebar by
typing a few characters of its name. As you type, the Sidebar
filters itself in real time, hiding entries that don't match and
highlighting the best match. Pressing {kbd}`Enter`
opens the highlighted mailbox; pressing {kbd}`Ctrl-G`
cancels and restores the original view.

If the Sidebar is currently hidden, it will be shown temporarily
during the search and hidden again afterwards.

The search uses the [Fuzzy Search](fuzzy-search) engine,
so you don't need to type the exact name. For example, typing
"mlnd" is enough to reach "mailinglists/neomutt-dev".

## Functions

| Menus   | Default Key | Function                 | Description              |
|---------|-------------|--------------------------|--------------------------|
| sidebar |             | `<sidebar-start-search>` | Fuzzy search the sidebar |
| sidebar |             | `<sidebar-abort-search>` | Close the sidebar search |

The search is started with the `sidebar-start-search`
function. It has no default keybinding, so you must add one yourself.
A natural choice is `Ctrl-S`.

```neomuttrc
bind sidebar \CS sidebar-start-search
```

A prompt reading "Sidebar search:" will appear at the
bottom of the screen. Type your search pattern and the Sidebar will
filter as you type.

## Keybindings During Search

While the search prompt is active, two sets of keybindings are
available simultaneously:

**Navigation**

{kbd}`Up` and {kbd}`Down` move the
highlight through the filtered Sidebar so you can pick a
different match without leaving the prompt.

`<sidebar-abort-search>` (bound to {kbd}`Escape` by default)
closes the search prompt without making a selection.

**Editor functions**

The full set of line-editor keybindings is available for
editing the search pattern. Examples include:

- `<backward-char>`/`<forward-char>` — move the cursor left or right
- `<bol>`/`<eol>` — jump to the start or end of the pattern
- `<backward-word>`/`<forward-word>` — skip a word at a time
- `<backspace>`/`<delete-char>` — delete a character
- `<kill-word>`/`<kill-eol>` — delete to end of word or line

Any binding defined in the `editor` map can be used; use `:bind editor` to customise them.

## Case Sensitivity

Sidebar Search uses *smart case* matching:

- If every letter in your pattern is lowercase, the search is
  *case-insensitive*. Typing "inbox" matches "INBOX", "Inbox", and "inbox".
- If your pattern contains even one uppercase letter, the search
  becomes *case-sensitive*. Typing "Inbox" will only match mailboxes
  whose name contains a capital "I".

This lets you search without caring about case in everyday use,
while still being able to narrow down precisely when you need to.

## UTF-8 Support

Mailbox names are matched as byte sequences, so UTF-8 mailbox names
work correctly: multi-byte characters are never split, and
non-ASCII characters are matched exactly as typed.

Case folding applies only to the ASCII letters A–Z. Accented
characters, CJK characters, and other non-ASCII text are always
matched byte-for-byte. Smart case detection also considers only
ASCII letters, so a pattern consisting entirely of non-ASCII
characters is treated as case-insensitive.

## How Matches Are Ranked

Every mailbox that contains all the letters of your pattern (in
order) is shown; the rest are hidden. Visible mailboxes are sorted
so that the best match is highlighted automatically. The ranking
rewards intuitive matches:

- **Word boundaries score highest.**
  Matching the first letter of a path component (after `/`, `.`,
  `-`, or `_`) or the very start of the name is rewarded more than
  a match buried in the middle of a word.

- **Consecutive letters score higher than scattered ones.**
  Typing "box" will rank "mail**box**" above a mailbox where the
  three letters appear far apart.

- **Compact matches beat spread-out ones.**
  The closer together the matched letters are, the better the score.

- **Shorter names are preferred.**
  When two mailboxes match equally well, the shorter name ranks higher.

- **New and unread mail boost the score.**
  Mailboxes with unread messages are ranked higher so that relevant
  mailboxes rise to the top when you're looking for something to read.
  Each *new* (unseen) message adds 2 points; each *unread* (seen but
  not read) message adds 1 point.

## Debug Expando: Fuzzy Score

:::{note}
This expando is a *temporary development aid* and will be removed in a future release.
:::

During development it can be useful to see the raw fuzzy score
assigned to each sidebar entry. Add the `%f` (or `%{fuzzy-score}`)
expando to your `$sidebar_format` string:

```neomuttrc
set sidebar_format = "%D%*  %n  [%f]"
```

The score is `-1` when no search is active (all mailboxes are shown).
Once a search pattern is entered, each visible entry shows its numeric
score; hidden entries show `-1`.

## Credits

Lucian Langa, Richard Russon
