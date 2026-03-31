---
title: Tour of NeoMutt
description: XXX
keywords: XXX
---

(tut-tour)=
# Tour of NeoMutt

## Complex Dialogs

```{toctree}
---
maxdepth: 1
---
tour/browser
tour/compose
tour/index
tour/pager
tour/message
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
tour/alias
tour/attach
tour/autocrypt
tour/browser
tour/certificate
tour/gpgme
tour/history
tour/pattern
tour/pgp
tour/postpone
tour/query
tour/smime
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
tour/simple
```

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

