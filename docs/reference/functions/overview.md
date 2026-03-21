---
title:
description: Default key bindings and functions for the NeoMutt Index Menu.
keywords: neomutt, functions, index, menu, bindings, keys, mail
---

(functions)=

# Functions

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

Functions are named actions that NeoMutt can perform.
Each function belongs to one or more menus and may have a default key binding. Bindings can be changed with the `bind` command.

The tables below list every function grouped by menu.
Where a function has multiple default bindings, each binding appears as a separate row.

```{toctree}
---
maxdepth: 1
hidden:
---
alias
attach
autocrypt
browser
compose
dialog
editor
generic
index
pager
pgp
postpone
query
sidebar
smime
```

## [Alias Menu](menu-alias)

Browse and select from your saved email address aliases.
You can sort, search, delete, and compose messages to your contacts.

| Function               | Description                                  |
|------------------------|----------------------------------------------|
| `<delete-entry>`       | Delete the current entry                     |
| `<exit>`               | Exit this menu                               |
| `<limit>`              | Show only messages matching a pattern        |
| `<mail>`               | Compose a new mail message                   |
| `<sort-alias-reverse>` | Sort messages in reverse order               |
| `<sort-alias>`         | Sort messages                                |
| `<tag-pattern>`        | Tag non-hidden messages matching a pattern   |
| `<undelete-entry>`     | Undelete the current entry                   |
| `<untag-pattern>`      | Untag non-hidden messages matching a pattern |

## [Attach Menu](menu-attach)

View and manage the attachments of a received email.
You can save, print, pipe, delete, or open attachments, and reply or forward from this view.

| Function                  | Description                                          |
|---------------------------|------------------------------------------------------|
| `<bounce-message>`        | Remail a message to another user                     |
| `<check-traditional-pgp>` | Check for classic PGP                                |
| `<collapse-parts>`        | Toggle display of subparts                           |
| `<compose-to-sender>`     | Compose new message to the current message sender    |
| `<delete-entry>`          | Delete the current entry                             |
| `<display-toggle-weed>`   | Display message and toggle header weeding            |
| `<edit-type>`             | Edit attachment content type                         |
| `<exit>`                  | Exit this menu                                       |
| `<extract-keys>`          | Extract supported public keys                        |
| `<followup-message>`      | Followup to newsgroup                                |
| `<forget-passphrase>`     | Wipe passphrases from memory                         |
| `<forward-message>`       | Forward a message with comments                      |
| `<forward-to-group>`      | Forward to newsgroup                                 |
| `<group-chat-reply>`      | Reply to all recipients preserving To/Cc             |
| `<group-reply>`           | Reply to all recipients                              |
| `<list-reply>`            | Reply to specified mailing list                      |
| `<list-subscribe>`        | Subscribe to a mailing list                          |
| `<list-unsubscribe>`      | Unsubscribe from a mailing list                      |
| `<pipe-entry>`            | Pipe message/attachment to a shell command           |
| `<pipe-message>`          | Pipe message/attachment to a shell command           |
| `<print-entry>`           | Print the current entry                              |
| `<reply>`                 | Reply to a message                                   |
| `<resend-message>`        | Use the current message as a template for a new one  |
| `<save-entry>`            | Save message/attachment to a mailbox/file            |
| `<undelete-entry>`        | Undelete the current entry                           |
| `<view-attach>`           | View attachment using mailcap entry if necessary     |
| `<view-mailcap>`          | Force viewing of attachment using mailcap            |
| `<view-pager>`            | View attachment in pager using copiousoutput mailcap |
| `<view-text>`             | View attachment as text                              |

## [Autocrypt Menu](menu-autocrypt)

Manage your Autocrypt encryption accounts.
You can create, delete, toggle, and set preferences for automatic email encryption keys.

| Function                  | Description                                    |
|---------------------------|------------------------------------------------|
| `<create-account>`        | Create a new autocrypt account                 |
| `<delete-account>`        | Delete the current account                     |
| `<exit>`                  | Exit this menu                                 |
| `<toggle-active>`         | Toggle the current account active/inactive     |
| `<toggle-prefer-encrypt>` | Toggle the current account prefer-encrypt flag |

## [Browser Menu](menu-browser)

Browse files on disk or mailboxes on a server.
You can navigate directories, sort listings, subscribe to mailboxes, and select a mailbox to open.

| Function                | Description                                                |
|-------------------------|------------------------------------------------------------|
| `<buffy-list>`          | {bdg-danger}`Deprecated` use `<mailbox-list>`              |
| `<catchup>`             | Mark all articles in newsgroup as read                     |
| `<change-dir>`          | Change directories                                         |
| `<check-new>`           | Check mailboxes for new mail                               |
| `<create-mailbox>`      | Create a new mailbox (IMAP only)                           |
| `<delete-mailbox>`      | Delete the current mailbox (IMAP only)                     |
| `<descend-directory>`   | Descend into a directory                                   |
| `<display-filename>`    | Display the currently selected file's name                 |
| `<enter-mask>`          | Enter a file mask                                          |
| `<exit>`                | Exit this menu                                             |
| `<goto-folder>`         | Swap the current folder position with $folder if it exists |
| `<goto-parent>`         | Go to parent directory                                     |
| `<mailbox-list>`        | List mailboxes with new mail                               |
| `<reload-active>`       | Load list of all newsgroups from NNTP server               |
| `<rename-mailbox>`      | Rename the current mailbox (IMAP only)                     |
| `<select-new>`          | Select a new file in this directory                        |
| `<sort-reverse>`        | Sort messages in reverse order                             |
| `<sort>`                | Sort messages                                              |
| `<subscribe-pattern>`   | Subscribe to newsgroups matching a pattern                 |
| `<subscribe>`           | Subscribe to current mbox (IMAP/NNTP only)                 |
| `<toggle-mailboxes>`    | Toggle whether to browse mailboxes or all files            |
| `<toggle-subscribed>`   | Toggle view all/subscribed mailboxes (IMAP only)           |
| `<uncatchup>`           | Mark all articles in newsgroup as unread                   |
| `<unsubscribe-pattern>` | Unsubscribe from newsgroups matching a pattern             |
| `<unsubscribe>`         | Unsubscribe from current mbox (IMAP/NNTP only)             |
| `<view-file>`           | View file                                                  |

## [Compose Menu](menu-compose)

Prepare an email before sending it.
You can edit recipients, subject, and headers, attach files, configure encryption, and send or postpone the message.

| Function                | Description                                          |
|-------------------------|------------------------------------------------------|
| `<attach-file>`         | Attach files to this message                         |
| `<attach-key>`          | Attach a PGP public key                              |
| `<attach-message>`      | Attach messages to this message                      |
| `<attach-news-message>` | Attach news articles to this message                 |
| `<autocrypt-menu>`      | Show autocrypt compose menu options                  |
| `<copy-file>`           | Save message/attachment to a mailbox/file            |
| `<detach-file>`         | Delete the current entry                             |
| `<display-toggle-weed>` | Display message and toggle header weeding            |
| `<edit-bcc>`            | Edit the BCC list                                    |
| `<edit-cc>`             | Edit the CC list                                     |
| `<edit-content-id>`     | Edit the 'Content-ID' of the attachment              |
| `<edit-description>`    | Edit attachment description                          |
| `<edit-encoding>`       | Edit attachment transfer-encoding                    |
| `<edit-fcc>`            | Enter a file to save a copy of this message in       |
| `<edit-file>`           | Edit the file to be attached                         |
| `<edit-followup-to>`    | Edit the Followup-To field                           |
| `<edit-from>`           | Edit the from field                                  |
| `<edit-headers>`        | Edit the message with headers                        |
| `<edit-language>`       | Edit the 'Content-Language' of the attachment        |
| `<edit-message>`        | Edit the message                                     |
| `<edit-mime>`           | Edit attachment using mailcap entry                  |
| `<edit-newsgroups>`     | Edit the newsgroups list                             |
| `<edit-reply-to>`       | Edit the Reply-To field                              |
| `<edit-subject>`        | Edit the subject of this message                     |
| `<edit-to>`             | Edit the TO list                                     |
| `<edit-type>`           | Edit attachment content type                         |
| `<edit-x-comment-to>`   | Edit the X-Comment-To field                          |
| `<exit>`                | Exit this menu                                       |
| `<filter-entry>`        | Filter attachment through a shell command            |
| `<forget-passphrase>`   | Wipe passphrases from memory                         |
| `<get-attachment>`      | Get a temporary copy of an attachment                |
| `<group-alternatives>`  | Group tagged attachments as 'multipart/alternative'  |
| `<group-multilingual>`  | Group tagged attachments as 'multipart/multilingual' |
| `<group-related>`       | Group tagged attachments as 'multipart/related'      |
| `<ispell>`              | Run ispell on the message                            |
| `<move-down>`           | Move an attachment down in the attachment list       |
| `<move-up>`             | Move an attachment up in the attachment list         |
| `<new-mime>`            | Compose new attachment using mailcap entry           |
| `<pgp-menu>`            | Show PGP options                                     |
| `<pipe-entry>`          | Pipe message/attachment to a shell command           |
| `<pipe-message>`        | Pipe message/attachment to a shell command           |
| `<postpone-message>`    | Save this message to send later                      |
| `<preview-page-down>`   | Show the next page of the message                    |
| `<preview-page-up>`     | Show the previous page of the message                |
| `<print-entry>`         | Print the current entry                              |
| `<rename-attachment>`   | Send attachment with a different name                |
| `<rename-file>`         | Rename/move an attached file                         |
| `<send-message>`        | Send the message                                     |
| `<smime-menu>`          | Show S/MIME options                                  |
| `<toggle-disposition>`  | Toggle disposition between inline/attachment         |
| `<toggle-recode>`       | Toggle recoding of this attachment                   |
| `<toggle-unlink>`       | Toggle whether to delete file after sending it       |
| `<ungroup-attachment>`  | Ungroup 'multipart' attachment                       |
| `<update-encoding>`     | Update an attachment's encoding info                 |
| `<view-attach>`         | View attachment using mailcap entry if necessary     |
| `<view-mailcap>`        | Force viewing of attachment using mailcap            |
| `<view-pager>`          | View attachment in pager using copiousoutput mailcap |
| `<view-text>`           | View attachment as text                              |
| `<write-fcc>`           | Write the message to a folder                        |

## [Dialog Menu](menu-dialog)

A simple informational pop-up, such as the help screen or log messages.
It only supports quitting.

| Function | Description                      |
|----------|----------------------------------|
| `<exit>` | Exit this menu                   |
| `<quit>` | Save changes to mailbox and quit |

## [Editor Menu](menu-editor)

The text input line where you type responses to prompts.
It supports cursor movement, word editing, tab-completion, and command history.

| Function            | Description                                         |
|---------------------|-----------------------------------------------------|
| `<backspace>`       | Delete the char in front of the cursor              |
| `<backward-char>`   | Move the cursor one character to the left           |
| `<backward-word>`   | Move the cursor to the beginning of the word        |
| `<bol>`             | Jump to the beginning of the line                   |
| `<buffy-cycle>`     | {bdg-danger}`Deprecated` use `<mailbox-cycle>`      |
| `<capitalize-word>` | Capitalize the word                                 |
| `<complete-query>`  | Complete address with query                         |
| `<complete>`        | Complete filename or alias                          |
| `<delete-char>`     | Delete the char under the cursor                    |
| `<downcase-word>`   | Convert the word to lower case                      |
| `<eol>`             | Jump to the end of the line                         |
| `<forward-char>`    | Move the cursor one character to the right          |
| `<forward-word>`    | Move the cursor to the end of the word              |
| `<help>`            | This screen                                         |
| `<history-down>`    | Scroll down through the history list                |
| `<history-search>`  | Search through the history list                     |
| `<history-up>`      | Scroll up through the history list                  |
| `<kill-eol>`        | Delete chars from cursor to end of line             |
| `<kill-eow>`        | Delete chars from the cursor to the end of the word |
| `<kill-line>`       | Delete chars from cursor to beginning the line      |
| `<kill-whole-line>` | Delete all chars on the line                        |
| `<kill-word>`       | Delete the word in front of the cursor              |
| `<mailbox-cycle>`   | Cycle among incoming mailboxes                      |
| `<quote-char>`      | Quote the next typed key                            |
| `<redraw-screen>`   | Clear and redraw the screen                         |
| `<transpose-chars>` | Transpose character under cursor with previous      |
| `<upcase-word>`     | Convert the word to upper case                      |

## [Generic Menu](menu-generic)

Not a menu itself, but provides common functions — such as scrolling, searching, and tagging — that are inherited by all other menus (except pager and editor).

| Function              | Description                                        |
|-----------------------|----------------------------------------------------|
| `<bottom-page>`       | Move to the bottom of the page                     |
| `<check-stats>`       | Calculate message statistics for all mailboxes     |
| `<current-bottom>`    | Move entry to bottom of screen                     |
| `<current-middle>`    | Move entry to middle of screen                     |
| `<current-top>`       | Move entry to top of screen                        |
| `<end-cond>`          | End of conditional execution (noop)                |
| `<enter-command>`     | Enter a neomuttrc command                          |
| `<error-history>`     | {bdg-danger}`Deprecated` use `<show-log-messages>` |
| `<exit>`              | Exit this menu                                     |
| `<first-entry>`       | Move to the first entry                            |
| `<half-down>`         | Scroll down 1/2 page                               |
| `<half-up>`           | Scroll up 1/2 page                                 |
| `<help>`              | This screen                                        |
| `<jump>`              | Jump to an index number                            |
| `<last-entry>`        | Move to the last entry                             |
| `<middle-page>`       | Move to the middle of the page                     |
| `<next-entry>`        | Move to the next entry                             |
| `<next-line>`         | Scroll down one line                               |
| `<next-page>`         | Move to the next page                              |
| `<previous-entry>`    | Move to the previous entry                         |
| `<previous-line>`     | Scroll up one line                                 |
| `<previous-page>`     | Move to the previous page                          |
| `<redraw-screen>`     | Clear and redraw the screen                        |
| `<refresh>`           | {bdg-danger}`Deprecated` use `<redraw-screen>`     |
| `<search-next>`       | Search for next match                              |
| `<search-opposite>`   | Search for next match in opposite direction        |
| `<search-reverse>`    | Search backwards for a regular expression          |
| `<search>`            | Search for a regular expression                    |
| `<select-entry>`      | Select the current entry                           |
| `<shell-escape>`      | Invoke a command in a subshell                     |
| `<show-log-messages>` | Show log (and debug) messages                      |
| `<show-version>`      | Show the NeoMutt version number and date           |
| `<tag-entry>`         | Tag the current entry                              |
| `<tag-prefix-cond>`   | Apply next function ONLY to tagged messages        |
| `<tag-prefix>`        | Apply next function to tagged messages             |
| `<top-page>`          | Move to the top of the page                        |
| `<what-key>`          | Display the keycode for a key press                |

## [Index Menu](menu-index)

The main screen showing the list of emails in a mailbox.
You can read, reply, forward, delete, tag, sort, search, and manage messages.

| Function                        | Description                                                             |
|---------------------------------|-------------------------------------------------------------------------|
| `<alias-dialog>`                | Open the aliases dialog                                                 |
| `<autocrypt-acct-menu>`         | Manage autocrypt accounts                                               |
| `<bounce-message>`              | Remail a message to another user                                        |
| `<break-thread>`                | Break the thread in two                                                 |
| `<buffy-list>`                  | {bdg-danger}`Deprecated` use `<mailbox-list>`                           |
| `<catchup>`                     | Mark all articles in newsgroup as read                                  |
| `<change-folder-readonly>`      | Open a different folder in read only mode                               |
| `<change-folder>`               | Open a different folder                                                 |
| `<change-newsgroup-readonly>`   | Open a different newsgroup in read only mode                            |
| `<change-newsgroup>`            | Open a different newsgroup                                              |
| `<change-vfolder>`              | Open a different virtual folder                                         |
| `<check-traditional-pgp>`       | Check for classic PGP                                                   |
| `<clear-flag>`                  | Clear a status flag from a message                                      |
| `<close-all-threads>`           | Collapse all threads                                                    |
| `<close-thread>`                | Collapse current thread                                                 |
| `<collapse-all>`                | Collapse/Uncollapse all threads                                         |
| `<collapse-thread>`             | Collapse/Uncollapse current thread                                      |
| `<compose-to-sender>`           | Compose new message to the current message sender                       |
| `<copy-message>`                | Copy a message to a file/mailbox                                        |
| `<create-alias>`                | Create an alias from a message sender                                   |
| `<decode-copy>`                 | Make decoded (text/plain) copy                                          |
| `<decode-save>`                 | Make decoded copy (text/plain) and delete                               |
| `<decrypt-copy>`                | Make decrypted copy                                                     |
| `<decrypt-save>`                | Make decrypted copy and delete                                          |
| `<delete-message>`              | Delete the current entry                                                |
| `<delete-pattern>`              | Delete non-hidden messages matching a pattern                           |
| `<delete-subthread>`            | Delete all messages in subthread                                        |
| `<delete-thread>`               | Delete all messages in thread                                           |
| `<display-address>`             | Display full address of sender                                          |
| `<display-message>`             | Display a message                                                       |
| `<display-toggle-weed>`         | Display message and toggle header weeding                               |
| `<edit-label>`                  | Add, change, or delete a message's label                                |
| `<edit-or-view-raw-message>`    | Edit the raw message if the mailbox is not read-only, otherwise view it |
| `<edit-raw-message>`            | Edit the raw message (edit and edit-raw-message are synonyms)           |
| `<edit-type>`                   | Edit attachment content type                                            |
| `<edit>`                        | Edit the raw message (edit and edit-raw-message are synonyms)           |
| `<entire-thread>`               | Read entire thread of the current message                               |
| `<exit>`                        | Exit this menu                                                          |
| `<extract-keys>`                | Extract supported public keys                                           |
| `<fetch-mail>`                  | Retrieve mail from POP server                                           |
| `<flag-message>`                | Toggle a message's 'important' flag                                     |
| `<followup-message>`            | Followup to newsgroup                                                   |
| `<forget-passphrase>`           | Wipe passphrases from memory                                            |
| `<forward-message>`             | Forward a message with comments                                         |
| `<forward-to-group>`            | Forward to newsgroup                                                    |
| `<get-children>`                | Get all children of the current message                                 |
| `<get-message>`                 | Get message with Message-Id                                             |
| `<get-parent>`                  | Get parent of the current message                                       |
| `<group-chat-reply>`            | Reply to all recipients preserving To/Cc                                |
| `<group-reply>`                 | Reply to all recipients                                                 |
| `<imap-fetch-mail>`             | Force retrieval of mail from IMAP server                                |
| `<imap-logout-all>`             | Logout from all IMAP servers                                            |
| `<limit-current-thread>`        | Limit view to current thread                                            |
| `<limit>`                       | Show only messages matching a pattern                                   |
| `<link-threads>`                | Link tagged message to the current one                                  |
| `<list-reply>`                  | Reply to specified mailing list                                         |
| `<list-subscribe>`              | Subscribe to a mailing list                                             |
| `<list-unsubscribe>`            | Unsubscribe from a mailing list                                         |
| `<mail-key>`                    | Mail a PGP public key                                                   |
| `<mail>`                        | Compose a new mail message                                              |
| `<mailbox-list>`                | List mailboxes with new mail                                            |
| `<mark-message>`                | Create a hotkey macro for the current message                           |
| `<modify-labels-then-hide>`     | Modify (notmuch/imap) tags and then hide message                        |
| `<modify-labels>`               | Modify (notmuch/imap) tags                                              |
| `<modify-tags-then-hide>`       | Modify (notmuch/imap) tags and then hide message                        |
| `<modify-tags>`                 | Modify (notmuch/imap) tags                                              |
| `<next-new-then-unread>`        | Jump to the next new or unread message                                  |
| `<next-new>`                    | Jump to the next new message                                            |
| `<next-subthread>`              | Jump to the next subthread                                              |
| `<next-thread>`                 | Jump to the next thread                                                 |
| `<next-undeleted>`              | Move to the next undeleted message                                      |
| `<next-unread-mailbox>`         | Open next mailbox with new mail                                         |
| `<next-unread>`                 | Jump to the next unread message                                         |
| `<open-all-threads>`            | Uncollapse all threads                                                  |
| `<open-thread>`                 | Uncollapse current thread                                               |
| `<parent-message>`              | Jump to parent message in thread                                        |
| `<pipe-entry>`                  | Pipe message/attachment to a shell command                              |
| `<pipe-message>`                | Pipe message/attachment to a shell command                              |
| `<post-message>`                | Post message to newsgroup                                               |
| `<previous-new-then-unread>`    | Jump to the previous new or unread message                              |
| `<previous-new>`                | Jump to the previous new message                                        |
| `<previous-subthread>`          | Jump to previous subthread                                              |
| `<previous-thread>`             | Jump to previous thread                                                 |
| `<previous-undeleted>`          | Move to the previous undeleted message                                  |
| `<previous-unread>`             | Jump to the previous unread message                                     |
| `<print-message>`               | Print the current entry                                                 |
| `<purge-message>`               | Delete the current entry, bypassing the trash folder                    |
| `<purge-thread>`                | Delete the current thread, bypassing the trash folder                   |
| `<quasi-delete>`                | Delete from NeoMutt, don't touch on disk                                |
| `<query>`                       | Query external program for addresses                                    |
| `<quit>`                        | Save changes to mailbox and quit                                        |
| `<read-subthread>`              | Mark the current subthread as read                                      |
| `<read-thread>`                 | Mark the current thread as read                                         |
| `<recall-message>`              | Recall a postponed message                                              |
| `<reconstruct-thread>`          | Reconstruct thread containing current message                           |
| `<reply>`                       | Reply to a message                                                      |
| `<resend-message>`              | Use the current message as a template for a new one                     |
| `<root-message>`                | Jump to root message in thread                                          |
| `<save-message>`                | Save message/attachment to a mailbox/file                               |
| `<set-flag>`                    | Set a status flag on a message                                          |
| `<show-limit>`                  | Show currently active limit pattern                                     |
| `<sort-mailbox>`                | Sort messages                                                           |
| `<sort-reverse>`                | Sort messages in reverse order                                          |
| `<sync-mailbox>`                | Save changes to mailbox                                                 |
| `<tag-pattern>`                 | Tag non-hidden messages matching a pattern                              |
| `<tag-subthread>`               | Tag the current subthread                                               |
| `<tag-thread>`                  | Tag the current thread                                                  |
| `<toggle-new>`                  | Toggle a message's 'new' flag                                           |
| `<toggle-read>`                 | Toggle view of read messages                                            |
| `<toggle-write>`                | Toggle whether the mailbox will be rewritten                            |
| `<undelete-message>`            | Undelete the current entry                                              |
| `<undelete-pattern>`            | Undelete non-hidden messages matching a pattern                         |
| `<undelete-subthread>`          | Undelete all messages in subthread                                      |
| `<undelete-thread>`             | Undelete all messages in thread                                         |
| `<untag-pattern>`               | Untag non-hidden messages matching a pattern                            |
| `<vfolder-from-query-readonly>` | Generate a read-only virtual folder from query                          |
| `<vfolder-from-query>`          | Generate virtual folder from query                                      |
| `<vfolder-window-backward>`     | Shifts virtual folder time window backwards                             |
| `<vfolder-window-forward>`      | Shifts virtual folder time window forwards                              |
| `<vfolder-window-reset>`        | Resets virtual folder time window to the present                        |
| `<view-attachments>`            | Show MIME attachments                                                   |
| `<view-raw-message>`            | Show the raw message                                                    |

## [Pager Menu](menu-pager)

The email reading view that displays a message's contents.
You can scroll, search within the text, and perform many of the same actions as the index.

| Function                        | Description                                                             |
|---------------------------------|-------------------------------------------------------------------------|
| `<bottom>`                      | Jump to the bottom of the message                                       |
| `<bounce-message>`              | Remail a message to another user                                        |
| `<break-thread>`                | Break the thread in two                                                 |
| `<buffy-list>`                  | {bdg-danger}`Deprecated` use `<mailbox-list>`                           |
| `<change-folder-readonly>`      | Open a different folder in read only mode                               |
| `<change-folder>`               | Open a different folder                                                 |
| `<change-newsgroup-readonly>`   | Open a different newsgroup in read only mode                            |
| `<change-newsgroup>`            | Open a different newsgroup                                              |
| `<change-vfolder>`              | Open a different virtual folder                                         |
| `<check-stats>`                 | Calculate message statistics for all mailboxes                          |
| `<check-traditional-pgp>`       | Check for classic PGP                                                   |
| `<clear-flag>`                  | Clear a status flag from a message                                      |
| `<compose-to-sender>`           | Compose new message to the current message sender                       |
| `<copy-message>`                | Copy a message to a file/mailbox                                        |
| `<create-alias>`                | Create an alias from a message sender                                   |
| `<decode-copy>`                 | Make decoded (text/plain) copy                                          |
| `<decode-save>`                 | Make decoded copy (text/plain) and delete                               |
| `<decrypt-copy>`                | Make decrypted copy                                                     |
| `<decrypt-save>`                | Make decrypted copy and delete                                          |
| `<delete-message>`              | Delete the current entry                                                |
| `<delete-subthread>`            | Delete all messages in subthread                                        |
| `<delete-thread>`               | Delete all messages in thread                                           |
| `<display-address>`             | Display full address of sender                                          |
| `<display-toggle-weed>`         | Display message and toggle header weeding                               |
| `<edit-label>`                  | Add, change, or delete a message's label                                |
| `<edit-or-view-raw-message>`    | Edit the raw message if the mailbox is not read-only, otherwise view it |
| `<edit-raw-message>`            | Edit the raw message (edit and edit-raw-message are synonyms)           |
| `<edit-type>`                   | Edit attachment content type                                            |
| `<edit>`                        | Edit the raw message (edit and edit-raw-message are synonyms)           |
| `<enter-command>`               | Enter a neomuttrc command                                               |
| `<entire-thread>`               | Read entire thread of the current message                               |
| `<error-history>`               | {bdg-danger}`Deprecated` use `<show-log-messages>`                      |
| `<exit>`                        | Exit this menu                                                          |
| `<extract-keys>`                | Extract supported public keys                                           |
| `<flag-message>`                | Toggle a message's 'important' flag                                     |
| `<followup-message>`            | Followup to newsgroup                                                   |
| `<forget-passphrase>`           | Wipe passphrases from memory                                            |
| `<forward-message>`             | Forward a message with comments                                         |
| `<forward-to-group>`            | Forward to newsgroup                                                    |
| `<group-chat-reply>`            | Reply to all recipients preserving To/Cc                                |
| `<group-reply>`                 | Reply to all recipients                                                 |
| `<half-down>`                   | Scroll down 1/2 page                                                    |
| `<half-up>`                     | Scroll up 1/2 page                                                      |
| `<help>`                        | This screen                                                             |
| `<imap-fetch-mail>`             | Force retrieval of mail from IMAP server                                |
| `<imap-logout-all>`             | Logout from all IMAP servers                                            |
| `<jump>`                        | Jump to an index number                                                 |
| `<link-threads>`                | Link tagged message to the current one                                  |
| `<list-reply>`                  | Reply to specified mailing list                                         |
| `<list-subscribe>`              | Subscribe to a mailing list                                             |
| `<list-unsubscribe>`            | Unsubscribe from a mailing list                                         |
| `<mail-key>`                    | Mail a PGP public key                                                   |
| `<mail>`                        | Compose a new mail message                                              |
| `<mailbox-list>`                | List mailboxes with new mail                                            |
| `<mark-as-new>`                 | Toggle a message's 'new' flag                                           |
| `<modify-labels-then-hide>`     | Modify (notmuch/imap) tags and then hide message                        |
| `<modify-labels>`               | Modify (notmuch/imap) tags                                              |
| `<modify-tags-then-hide>`       | Modify (notmuch/imap) tags and then hide message                        |
| `<modify-tags>`                 | Modify (notmuch/imap) tags                                              |
| `<next-entry>`                  | Move to the next entry                                                  |
| `<next-line>`                   | Scroll down one line                                                    |
| `<next-new-then-unread>`        | Jump to the next new or unread message                                  |
| `<next-new>`                    | Jump to the next new message                                            |
| `<next-page>`                   | Move to the next page                                                   |
| `<next-subthread>`              | Jump to the next subthread                                              |
| `<next-thread>`                 | Jump to the next thread                                                 |
| `<next-undeleted>`              | Move to the next undeleted message                                      |
| `<next-unread-mailbox>`         | Open next mailbox with new mail                                         |
| `<next-unread>`                 | Jump to the next unread message                                         |
| `<parent-message>`              | Jump to parent message in thread                                        |
| `<pipe-entry>`                  | Pipe message/attachment to a shell command                              |
| `<pipe-message>`                | Pipe message/attachment to a shell command                              |
| `<post-message>`                | Post message to newsgroup                                               |
| `<previous-entry>`              | Move to the previous entry                                              |
| `<previous-line>`               | Scroll up one line                                                      |
| `<previous-new-then-unread>`    | Jump to the previous new or unread message                              |
| `<previous-new>`                | Jump to the previous new message                                        |
| `<previous-page>`               | Move to the previous page                                               |
| `<previous-subthread>`          | Jump to previous subthread                                              |
| `<previous-thread>`             | Jump to previous thread                                                 |
| `<previous-undeleted>`          | Move to the previous undeleted message                                  |
| `<previous-unread>`             | Jump to the previous unread message                                     |
| `<print-entry>`                 | Print the current entry                                                 |
| `<print-message>`               | Print the current entry                                                 |
| `<purge-message>`               | Delete the current entry, bypassing the trash folder                    |
| `<purge-thread>`                | Delete the current thread, bypassing the trash folder                   |
| `<quasi-delete>`                | Delete from NeoMutt, don't touch on disk                                |
| `<quit>`                        | Save changes to mailbox and quit                                        |
| `<read-subthread>`              | Mark the current subthread as read                                      |
| `<read-thread>`                 | Mark the current thread as read                                         |
| `<recall-message>`              | Recall a postponed message                                              |
| `<reconstruct-thread>`          | Reconstruct thread containing current message                           |
| `<redraw-screen>`               | Clear and redraw the screen                                             |
| `<reply>`                       | Reply to a message                                                      |
| `<resend-message>`              | Use the current message as a template for a new one                     |
| `<root-message>`                | Jump to root message in thread                                          |
| `<save-entry>`                  | Save message/attachment to a mailbox/file                               |
| `<save-message>`                | Save message/attachment to a mailbox/file                               |
| `<search-next>`                 | Search for next match                                                   |
| `<search-opposite>`             | Search for next match in opposite direction                             |
| `<search-reverse>`              | Search backwards for a regular expression                               |
| `<search-toggle>`               | Toggle search pattern coloring                                          |
| `<search>`                      | Search for a regular expression                                         |
| `<set-flag>`                    | Set a status flag on a message                                          |
| `<shell-escape>`                | Invoke a command in a subshell                                          |
| `<show-log-messages>`           | Show log (and debug) messages                                           |
| `<show-version>`                | Show the NeoMutt version number and date                                |
| `<skip-headers>`                | Jump to first line after headers                                        |
| `<skip-quoted>`                 | Skip beyond quoted text                                                 |
| `<sort-mailbox>`                | Sort messages                                                           |
| `<sort-reverse>`                | Sort messages in reverse order                                          |
| `<sync-mailbox>`                | Save changes to mailbox                                                 |
| `<tag-message>`                 | Tag the current entry                                                   |
| `<toggle-quoted>`               | Toggle display of quoted text                                           |
| `<toggle-write>`                | Toggle whether the mailbox will be rewritten                            |
| `<top>`                         | Jump to the top of the message                                          |
| `<undelete-message>`            | Undelete the current entry                                              |
| `<undelete-subthread>`          | Undelete all messages in subthread                                      |
| `<undelete-thread>`             | Undelete all messages in thread                                         |
| `<vfolder-from-query-readonly>` | Generate a read-only virtual folder from query                          |
| `<vfolder-from-query>`          | Generate virtual folder from query                                      |
| `<view-attachments>`            | Show MIME attachments                                                   |
| `<view-raw-message>`            | Show the raw message                                                    |
| `<what-key>`                    | Display the keycode for a key press                                     |

## [PGP Menu](menu-pgp)

Select a PGP key when encrypting or signing an email.
You can verify key details before choosing which key to use.

| Function       | Description            |
|----------------|------------------------|
| `<exit>`       | Exit this menu         |
| `<verify-key>` | Verify a public key    |
| `<view-name>`  | View the key's user id |

## [Postpone Menu](menu-postpone)

Select from your saved draft emails to resume editing.
You can pick a previously postponed message to continue composing it.

| Function           | Description                |
|--------------------|----------------------------|
| `<delete-entry>`   | Delete the current entry   |
| `<exit>`           | Exit this menu             |
| `<undelete-entry>` | Undelete the current entry |

## [Query Menu](menu-query)

Display results from an external address-book query.
You can search for contacts, create aliases from the results, and compose messages to selected addresses.

| Function          | Description                                  |
|-------------------|----------------------------------------------|
| `<create-alias>`  | Create an alias from a message sender        |
| `<exit>`          | Exit this menu                               |
| `<limit>`         | Show only messages matching a pattern        |
| `<mail>`          | Compose a new mail message                   |
| `<query-append>`  | Append new query results to current results  |
| `<query>`         | Query external program for addresses         |
| `<sort-reverse>`  | Sort messages in reverse order               |
| `<sort>`          | Sort messages                                |
| `<tag-pattern>`   | Tag non-hidden messages matching a pattern   |
| `<untag-pattern>` | Untag non-hidden messages matching a pattern |

## [Sidebar Menu](menu-sidebar)

Navigate the sidebar panel that lists your mailboxes.
You can move between mailboxes, open them, and toggle the sidebar's visibility.

| Function                   | Description                                          |
|----------------------------|------------------------------------------------------|
| `<sidebar-abort-search>`   | Close the sidebar search                             |
| `<sidebar-first>`          | Move the highlight to the first mailbox              |
| `<sidebar-last>`           | Move the highlight to the last mailbox               |
| `<sidebar-next-new>`       | Move the highlight to next mailbox with new mail     |
| `<sidebar-next>`           | Move the highlight to next mailbox                   |
| `<sidebar-open>`           | Open highlighted mailbox                             |
| `<sidebar-page-down>`      | Scroll the sidebar down 1 page                       |
| `<sidebar-page-up>`        | Scroll the sidebar up 1 page                         |
| `<sidebar-prev-new>`       | Move the highlight to previous mailbox with new mail |
| `<sidebar-prev>`           | Move the highlight to previous mailbox               |
| `<sidebar-start-search>`   | Fuzzy search the sidebar                             |
| `<sidebar-toggle-virtual>` | Toggle between mailboxes and virtual mailboxes       |
| `<sidebar-toggle-visible>` | Make the sidebar (in)visible                         |

## [S/MIME Menu](menu-smime)

Select an S/MIME certificate when encrypting or signing an email.
You can verify certificate details before choosing which one to use.

| Function       | Description            |
|----------------|------------------------|
| `<exit>`       | Exit this menu         |
| `<verify-key>` | Verify a public key    |
| `<view-name>`  | View the key's user id |

