---
title: Tour of NeoMutt
description: A guided hub for NeoMutt's dialogs, panels, prompts, and short-lived support screens.
keywords: tour, dialogs, pager, index, compose, browser, sidebar, message window, navigation
---

(tut-tour)=
# Tour of NeoMutt

## Introduction -- Where am I?

This is the tour hub for NeoMutt's user interface.
Each page below is a jump point into one dialog, panel, or support screen, with links out to the deeper reference material for functions, configuration, commands, and colours.
Use it when you want either a quick orientation or a map into the full manual.

::::{grid} 3
:gutter: 3

:::{grid-item-card} Index - List of Emails
:link: index2
:link-type: doc
<div class="thumbnail">

```{include} ../../_includes/_screenshot-index.html
```

</div>
:::

:::{grid-item-card} Pager - Read an Email
:link: pager
:link-type: doc
<div class="thumbnail">

```{include} ../../_includes/_screenshot-pager.html
```

</div>
:::

:::{grid-item-card} Compose - Write an Email
:link: compose
:link-type: doc
<div class="thumbnail">

```{include} ../../_includes/_screenshot-compose.html
```

</div>
:::

::::

## Complex Dialogs

```{toctree}
---
maxdepth: 1
---
browser.md
compose.md
index2.md
pager.md
message.md
sidebar.md
```

% Compose Dialog
%     compose
%     - Compose/Compose-Message dialog
%       - Screen for composing new messages or replies. Provides header-entry prompts (To, Cc, Subject), editor invocation, and send/cancel prompts.
% 
% Index Dialog
%     index
%     - Index (index menu)
%       - Lists messages in the current folder (one-line per message). Used for selecting, tagging, sorting, limiting, and opening messages. Shows flags, number, date, sender, subject.
% 
% Pager Dialog
%     pager
%     - Pager (pager/menu)
%       - Shows a single message's headers and body (page-based). Used to read messages, follow threads, view attachments, and invoke message-level commands (reply, forward, save).
% 
% Browser Dialog
%     browser
% 
% Message window
%     message
%     - Command-line prompt (command prompt)
%       - Single-line prompt at bottom used to type NeoMutt commands, functions, or to show status/errors.
%     - Status line / Status dialog
%       - Context-sensitive single-line area showing mode, mailbox status, message counts; sometimes expanded into a status screen for details (e.g., pager status).
%   - Progress/Transfer dialogs
%     - Small progress displays when performing long operations (fetching messages, sending large attachments).

## Simple Dialogs

```{toctree}
---
maxdepth: 1
---
alias.md
attach.md
autocrypt.md
browser.md
certificate.md
gpgme.md
history.md
pattern.md
pgp.md
postpone.md
query.md
smime.md
```

% Alias Dialog
%     alias
%     - Alias menu
%       - Line-based menu to select addresses from configured aliases when composing recipients.
%     - Address-book (from third-party/addressbook integrations)
%       - If configured, a menu to browse/address entries (NeoMutt itself provides alias menu; GUI addressbooks come from helpers).
% 
% Attach Dialog
%     attach
%     - Attachment menu / View Attachment dialog
%       - Lists attachments for the current message and lets you view, save, pipe, or open them with external programs.
% 
% Autocrypt Dialog
%     autocrypt
% 
% Certificate Dialog
%     certificate
%     - Certificate/SSL prompt
%       - Prompt to accept/reject TLS/SSL certificates when fetching or sending via misconfigured/unknown certs.
% 
% Gpgme Dialog
%     gpgme
% 
% History Dialog
%     history
%     - History / Command history menu
%       - Presents past commands/addresses for selection (invoked in prompts with history support).
% 
% Pattern Dialog
%     pattern
% 
% Pgp Dialog
%     pgp
% 
% Postpone Dialog
%     postpone
% 
% Query Dialog
%     query
% 
% Smime Dialog
%     smime

## Simple Pager

```{toctree}
---
maxdepth: 1
---
simple.md
```

## What am I looking at?

- The cards at the top show the biggest day-to-day screens: the index, pager, and compose views.
- The toctrees below group the rest of the tour into complex dialogs, simple dialogs, panels, prompts, and simple pagers.
- Together, these pages mirror NeoMutt's high-level dialog navigation.

## What can I do?

- Start with the [Index Dialog](index2.md) if you want the main workflow hub.
- Jump to [Pager Dialog](pager.md) and [Compose Dialog](compose.md) for the two other screens most users spend time in.
- Explore specialist screens such as [Attach Dialog](attach.md), [Browser Dialog](browser.md), [Alias Dialog](alias.md), and [Query Dialog](query.md).
- Use [Message Window](message.md) and [Simple Pagers](simple.md) to understand the short-lived support UI that appears everywhere.

## Where can I go next?

- The [Index Dialog](index2.md) page is the best starting point for understanding overall navigation.
- The [Browser Dialog](browser.md), [Compose Dialog](compose.md), and [Pager Dialog](pager.md) pages cover the major branch points in normal use.
- The [Sidebar Panel](sidebar.md) and [Message Window](message.md) pages explain the embedded UI components that appear in many screenshots.

## Where did I come from?

- If you arrived from the rest of the documentation, this page is the high-level bridge between tutorials and the detailed reference chapters.
- If you arrived from a specific dialog page, this hub is the place to branch out to neighbouring screens.

## How do I configure this?

- The tour itself is explanatory, but each dialog page links directly to the relevant [Config Reference](../../reference/config/index.md), [Functions Reference](../../reference/functions/index.md), [Commands Reference](ref-commands), and [Colour Objects](ref-colors).
- For global UI customisation, start with [General Config](ref-cfg-general), [Index Config](ref-cfg-index), [Pager Config](ref-cfg-pager), [Compose Config](ref-cfg-compose), and [Sidebar Config](ref-cfg-sidebar).

% color_dump
%     :color
% dump_bind_macro
%     :bind
%     :macro
%     - Key binding help (help menu)
%       - Page-based listing of current key bindings and functions for the current menu/context.
% mutt_help
%     <help>
% mutt_invoke_sendmail
%     sendmail
% mutt_view_attachment
% op_show_log_messages
%     <show-log-messages>
% parse_setenv
%     :setenv
% parse_version
%     :version
% set_dump
%     :set
% verify_key
