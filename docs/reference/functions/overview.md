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
| `<delete-entry>`       | delete the current entry                     |
| `<exit>`               | exit this menu                               |
| `<limit>`              | show only messages matching a pattern        |
| `<mail>`               | compose a new mail message                   |
| `<sort-alias-reverse>` | sort messages in reverse order               |
| `<sort-alias>`         | sort messages                                |
| `<tag-pattern>`        | tag non-hidden messages matching a pattern   |
| `<undelete-entry>`     | undelete the current entry                   |
| `<untag-pattern>`      | untag non-hidden messages matching a pattern |

## [Attach Menu](menu-attach)

View and manage the attachments of a received email.
You can save, print, pipe, delete, or open attachments, and reply or forward from this view.

| Function                  | Description                                          |
|---------------------------|------------------------------------------------------|
| `<bounce-message>`        | remail a message to another user                     |
| `<check-traditional-pgp>` | check for classic PGP                                |
| `<collapse-parts>`        | toggle display of subparts                           |
| `<compose-to-sender>`     | compose new message to the current message sender    |
| `<delete-entry>`          | delete the current entry                             |
| `<display-toggle-weed>`   | display message and toggle header weeding            |
| `<edit-type>`             | edit attachment content type                         |
| `<exit>`                  | exit this menu                                       |
| `<extract-keys>`          | extract supported public keys                        |
| `<followup-message>`      | followup to newsgroup                                |
| `<forget-passphrase>`     | wipe passphrases from memory                         |
| `<forward-message>`       | forward a message with comments                      |
| `<forward-to-group>`      | forward to newsgroup                                 |
| `<group-chat-reply>`      | reply to all recipients preserving To/Cc             |
| `<group-reply>`           | reply to all recipients                              |
| `<list-reply>`            | reply to specified mailing list                      |
| `<list-subscribe>`        | subscribe to a mailing list                          |
| `<list-unsubscribe>`      | unsubscribe from a mailing list                      |
| `<pipe-entry>`            | pipe message/attachment to a shell command           |
| `<pipe-message>`          | pipe message/attachment to a shell command           |
| `<print-entry>`           | print the current entry                              |
| `<reply>`                 | reply to a message                                   |
| `<resend-message>`        | use the current message as a template for a new one  |
| `<save-entry>`            | save message/attachment to a mailbox/file            |
| `<undelete-entry>`        | undelete the current entry                           |
| `<view-attach>`           | view attachment using mailcap entry if necessary     |
| `<view-mailcap>`          | force viewing of attachment using mailcap            |
| `<view-pager>`            | view attachment in pager using copiousoutput mailcap |
| `<view-text>`             | view attachment as text                              |

## [Autocrypt Menu](menu-autocrypt)

Manage your Autocrypt encryption accounts.
You can create, delete, toggle, and set preferences for automatic email encryption keys.

| Function                  | Description                                    |
|---------------------------|------------------------------------------------|
| `<create-account>`        | create a new autocrypt account                 |
| `<delete-account>`        | delete the current account                     |
| `<exit>`                  | exit this menu                                 |
| `<toggle-active>`         | toggle the current account active/inactive     |
| `<toggle-prefer-encrypt>` | toggle the current account prefer-encrypt flag |

## [Browser Menu](menu-browser)

Browse files on disk or mailboxes on a server.
You can navigate directories, sort listings, subscribe to mailboxes, and select a mailbox to open.

| Function                | Description                                                |
|-------------------------|------------------------------------------------------------|
| `<buffy-list>`          | {bdg-danger}`Deprecated` use `<mailbox-list>`              |
| `<catchup>`             | mark all articles in newsgroup as read                     |
| `<change-dir>`          | change directories                                         |
| `<check-new>`           | check mailboxes for new mail                               |
| `<create-mailbox>`      | create a new mailbox (IMAP only)                           |
| `<delete-mailbox>`      | delete the current mailbox (IMAP only)                     |
| `<descend-directory>`   | descend into a directory                                   |
| `<display-filename>`    | display the currently selected file's name                 |
| `<enter-mask>`          | enter a file mask                                          |
| `<exit>`                | exit this menu                                             |
| `<goto-folder>`         | swap the current folder position with $folder if it exists |
| `<goto-parent>`         | go to parent directory                                     |
| `<mailbox-list>`        | list mailboxes with new mail                               |
| `<reload-active>`       | load list of all newsgroups from NNTP server               |
| `<rename-mailbox>`      | rename the current mailbox (IMAP only)                     |
| `<select-new>`          | select a new file in this directory                        |
| `<sort-reverse>`        | sort messages in reverse order                             |
| `<sort>`                | sort messages                                              |
| `<subscribe-pattern>`   | subscribe to newsgroups matching a pattern                 |
| `<subscribe>`           | subscribe to current mbox (IMAP/NNTP only)                 |
| `<toggle-mailboxes>`    | toggle whether to browse mailboxes or all files            |
| `<toggle-subscribed>`   | toggle view all/subscribed mailboxes (IMAP only)           |
| `<uncatchup>`           | mark all articles in newsgroup as unread                   |
| `<unsubscribe-pattern>` | unsubscribe from newsgroups matching a pattern             |
| `<unsubscribe>`         | unsubscribe from current mbox (IMAP/NNTP only)             |
| `<view-file>`           | view file                                                  |

## [Compose Menu](menu-compose)

Prepare an email before sending it.
You can edit recipients, subject, and headers, attach files, configure encryption, and send or postpone the message.

| Function                | Description                                          |
|-------------------------|------------------------------------------------------|
| `<attach-file>`         | attach files to this message                         |
| `<attach-key>`          | attach a PGP public key                              |
| `<attach-message>`      | attach messages to this message                      |
| `<attach-news-message>` | attach news articles to this message                 |
| `<autocrypt-menu>`      | show autocrypt compose menu options                  |
| `<copy-file>`           | save message/attachment to a mailbox/file            |
| `<detach-file>`         | delete the current entry                             |
| `<display-toggle-weed>` | display message and toggle header weeding            |
| `<edit-bcc>`            | edit the BCC list                                    |
| `<edit-cc>`             | edit the CC list                                     |
| `<edit-content-id>`     | edit the 'Content-ID' of the attachment              |
| `<edit-description>`    | edit attachment description                          |
| `<edit-encoding>`       | edit attachment transfer-encoding                    |
| `<edit-fcc>`            | enter a file to save a copy of this message in       |
| `<edit-file>`           | edit the file to be attached                         |
| `<edit-followup-to>`    | edit the Followup-To field                           |
| `<edit-from>`           | edit the from field                                  |
| `<edit-headers>`        | edit the message with headers                        |
| `<edit-language>`       | edit the 'Content-Language' of the attachment        |
| `<edit-message>`        | edit the message                                     |
| `<edit-mime>`           | edit attachment using mailcap entry                  |
| `<edit-newsgroups>`     | edit the newsgroups list                             |
| `<edit-reply-to>`       | edit the Reply-To field                              |
| `<edit-subject>`        | edit the subject of this message                     |
| `<edit-to>`             | edit the TO list                                     |
| `<edit-type>`           | edit attachment content type                         |
| `<edit-x-comment-to>`   | edit the X-Comment-To field                          |
| `<exit>`                | exit this menu                                       |
| `<filter-entry>`        | filter attachment through a shell command            |
| `<forget-passphrase>`   | wipe passphrases from memory                         |
| `<get-attachment>`      | get a temporary copy of an attachment                |
| `<group-alternatives>`  | group tagged attachments as 'multipart/alternative'  |
| `<group-multilingual>`  | group tagged attachments as 'multipart/multilingual' |
| `<group-related>`       | group tagged attachments as 'multipart/related'      |
| `<ispell>`              | run ispell on the message                            |
| `<move-down>`           | move an attachment down in the attachment list       |
| `<move-up>`             | move an attachment up in the attachment list         |
| `<new-mime>`            | compose new attachment using mailcap entry           |
| `<pgp-menu>`            | show PGP options                                     |
| `<pipe-entry>`          | pipe message/attachment to a shell command           |
| `<pipe-message>`        | pipe message/attachment to a shell command           |
| `<postpone-message>`    | save this message to send later                      |
| `<preview-page-down>`   | show the next page of the message                    |
| `<preview-page-up>`     | show the previous page of the message                |
| `<print-entry>`         | print the current entry                              |
| `<rename-attachment>`   | send attachment with a different name                |
| `<rename-file>`         | rename/move an attached file                         |
| `<send-message>`        | send the message                                     |
| `<smime-menu>`          | show S/MIME options                                  |
| `<toggle-disposition>`  | toggle disposition between inline/attachment         |
| `<toggle-recode>`       | toggle recoding of this attachment                   |
| `<toggle-unlink>`       | toggle whether to delete file after sending it       |
| `<ungroup-attachment>`  | ungroup 'multipart' attachment                       |
| `<update-encoding>`     | update an attachment's encoding info                 |
| `<view-attach>`         | view attachment using mailcap entry if necessary     |
| `<view-mailcap>`        | force viewing of attachment using mailcap            |
| `<view-pager>`          | view attachment in pager using copiousoutput mailcap |
| `<view-text>`           | view attachment as text                              |
| `<write-fcc>`           | write the message to a folder                        |

## [Dialog Menu](menu-dialog)

A simple informational pop-up, such as the help screen or log messages.
It only supports quitting.

| Function | Description                      |
|----------|----------------------------------|
| `<exit>` | exit this menu                   |
| `<quit>` | save changes to mailbox and quit |

## [Editor Menu](menu-editor)

The text input line where you type responses to prompts.
It supports cursor movement, word editing, tab-completion, and command history.

| Function            | Description                                         |
|---------------------|-----------------------------------------------------|
| `<backspace>`       | delete the char in front of the cursor              |
| `<backward-char>`   | move the cursor one character to the left           |
| `<backward-word>`   | move the cursor to the beginning of the word        |
| `<bol>`             | jump to the beginning of the line                   |
| `<buffy-cycle>`     | {bdg-danger}`Deprecated` use `<mailbox-cycle>`      |
| `<capitalize-word>` | capitalize the word                                 |
| `<complete-query>`  | complete address with query                         |
| `<complete>`        | complete filename or alias                          |
| `<delete-char>`     | delete the char under the cursor                    |
| `<downcase-word>`   | convert the word to lower case                      |
| `<eol>`             | jump to the end of the line                         |
| `<forward-char>`    | move the cursor one character to the right          |
| `<forward-word>`    | move the cursor to the end of the word              |
| `<help>`            | this screen                                         |
| `<history-down>`    | scroll down through the history list                |
| `<history-search>`  | search through the history list                     |
| `<history-up>`      | scroll up through the history list                  |
| `<kill-eol>`        | delete chars from cursor to end of line             |
| `<kill-eow>`        | delete chars from the cursor to the end of the word |
| `<kill-line>`       | delete chars from cursor to beginning the line      |
| `<kill-whole-line>` | delete all chars on the line                        |
| `<kill-word>`       | delete the word in front of the cursor              |
| `<mailbox-cycle>`   | cycle among incoming mailboxes                      |
| `<quote-char>`      | quote the next typed key                            |
| `<redraw-screen>`   | clear and redraw the screen                         |
| `<transpose-chars>` | transpose character under cursor with previous      |
| `<upcase-word>`     | convert the word to upper case                      |

## [Generic Menu](menu-generic)

Not a menu itself, but provides common functions — such as scrolling, searching, and tagging — that are inherited by all other menus (except pager and editor).

| Function              | Description                                        |
|-----------------------|----------------------------------------------------|
| `<bottom-page>`       | move to the bottom of the page                     |
| `<check-stats>`       | calculate message statistics for all mailboxes     |
| `<current-bottom>`    | move entry to bottom of screen                     |
| `<current-middle>`    | move entry to middle of screen                     |
| `<current-top>`       | move entry to top of screen                        |
| `<end-cond>`          | end of conditional execution (noop)                |
| `<enter-command>`     | enter a neomuttrc command                          |
| `<error-history>`     | {bdg-danger}`Deprecated` use `<show-log-messages>` |
| `<exit>`              | exit this menu                                     |
| `<first-entry>`       | move to the first entry                            |
| `<half-down>`         | scroll down 1/2 page                               |
| `<half-up>`           | scroll up 1/2 page                                 |
| `<help>`              | this screen                                        |
| `<jump>`              | jump to an index number                            |
| `<last-entry>`        | move to the last entry                             |
| `<middle-page>`       | move to the middle of the page                     |
| `<next-entry>`        | move to the next entry                             |
| `<next-line>`         | scroll down one line                               |
| `<next-page>`         | move to the next page                              |
| `<previous-entry>`    | move to the previous entry                         |
| `<previous-line>`     | scroll up one line                                 |
| `<previous-page>`     | move to the previous page                          |
| `<redraw-screen>`     | clear and redraw the screen                        |
| `<refresh>`           | {bdg-danger}`Deprecated` use `<redraw-screen>`     |
| `<search-next>`       | search for next match                              |
| `<search-opposite>`   | search for next match in opposite direction        |
| `<search-reverse>`    | search backwards for a regular expression          |
| `<search>`            | search for a regular expression                    |
| `<select-entry>`      | select the current entry                           |
| `<shell-escape>`      | invoke a command in a subshell                     |
| `<show-log-messages>` | show log (and debug) messages                      |
| `<show-version>`      | show the NeoMutt version number and date           |
| `<tag-entry>`         | tag the current entry                              |
| `<tag-prefix-cond>`   | apply next function ONLY to tagged messages        |
| `<tag-prefix>`        | apply next function to tagged messages             |
| `<top-page>`          | move to the top of the page                        |
| `<what-key>`          | display the keycode for a key press                |

## [Index Menu](menu-index)

The main screen showing the list of emails in a mailbox.
You can read, reply, forward, delete, tag, sort, search, and manage messages.

| Function                        | Description                                                             |
|---------------------------------|-------------------------------------------------------------------------|
| `<alias-dialog>`                | open the aliases dialog                                                 |
| `<autocrypt-acct-menu>`         | manage autocrypt accounts                                               |
| `<bounce-message>`              | remail a message to another user                                        |
| `<break-thread>`                | break the thread in two                                                 |
| `<buffy-list>`                  | {bdg-danger}`Deprecated` use `<mailbox-list>`                           |
| `<catchup>`                     | mark all articles in newsgroup as read                                  |
| `<change-folder-readonly>`      | open a different folder in read only mode                               |
| `<change-folder>`               | open a different folder                                                 |
| `<change-newsgroup-readonly>`   | open a different newsgroup in read only mode                            |
| `<change-newsgroup>`            | open a different newsgroup                                              |
| `<change-vfolder>`              | open a different virtual folder                                         |
| `<check-traditional-pgp>`       | check for classic PGP                                                   |
| `<clear-flag>`                  | clear a status flag from a message                                      |
| `<close-all-threads>`           | collapse all threads                                                    |
| `<close-thread>`                | collapse current thread                                                 |
| `<collapse-all>`                | collapse/uncollapse all threads                                         |
| `<collapse-thread>`             | collapse/uncollapse current thread                                      |
| `<compose-to-sender>`           | compose new message to the current message sender                       |
| `<copy-message>`                | copy a message to a file/mailbox                                        |
| `<create-alias>`                | create an alias from a message sender                                   |
| `<decode-copy>`                 | make decoded (text/plain) copy                                          |
| `<decode-save>`                 | make decoded copy (text/plain) and delete                               |
| `<decrypt-copy>`                | make decrypted copy                                                     |
| `<decrypt-save>`                | make decrypted copy and delete                                          |
| `<delete-message>`              | delete the current entry                                                |
| `<delete-pattern>`              | delete non-hidden messages matching a pattern                           |
| `<delete-subthread>`            | delete all messages in subthread                                        |
| `<delete-thread>`               | delete all messages in thread                                           |
| `<display-address>`             | display full address of sender                                          |
| `<display-message>`             | display a message                                                       |
| `<display-toggle-weed>`         | display message and toggle header weeding                               |
| `<edit-label>`                  | add, change, or delete a message's label                                |
| `<edit-or-view-raw-message>`    | edit the raw message if the mailbox is not read-only, otherwise view it |
| `<edit-raw-message>`            | edit the raw message (edit and edit-raw-message are synonyms)           |
| `<edit-type>`                   | edit attachment content type                                            |
| `<edit>`                        | edit the raw message (edit and edit-raw-message are synonyms)           |
| `<entire-thread>`               | read entire thread of the current message                               |
| `<exit>`                        | exit this menu                                                          |
| `<extract-keys>`                | extract supported public keys                                           |
| `<fetch-mail>`                  | retrieve mail from POP server                                           |
| `<flag-message>`                | toggle a message's 'important' flag                                     |
| `<followup-message>`            | followup to newsgroup                                                   |
| `<forget-passphrase>`           | wipe passphrases from memory                                            |
| `<forward-message>`             | forward a message with comments                                         |
| `<forward-to-group>`            | forward to newsgroup                                                    |
| `<get-children>`                | get all children of the current message                                 |
| `<get-message>`                 | get message with Message-Id                                             |
| `<get-parent>`                  | get parent of the current message                                       |
| `<group-chat-reply>`            | reply to all recipients preserving To/Cc                                |
| `<group-reply>`                 | reply to all recipients                                                 |
| `<imap-fetch-mail>`             | force retrieval of mail from IMAP server                                |
| `<imap-logout-all>`             | logout from all IMAP servers                                            |
| `<limit-current-thread>`        | limit view to current thread                                            |
| `<limit>`                       | show only messages matching a pattern                                   |
| `<link-threads>`                | link tagged message to the current one                                  |
| `<list-reply>`                  | reply to specified mailing list                                         |
| `<list-subscribe>`              | subscribe to a mailing list                                             |
| `<list-unsubscribe>`            | unsubscribe from a mailing list                                         |
| `<mail-key>`                    | mail a PGP public key                                                   |
| `<mail>`                        | compose a new mail message                                              |
| `<mailbox-list>`                | list mailboxes with new mail                                            |
| `<mark-message>`                | create a hotkey macro for the current message                           |
| `<modify-labels-then-hide>`     | modify (notmuch/imap) tags and then hide message                        |
| `<modify-labels>`               | modify (notmuch/imap) tags                                              |
| `<modify-tags-then-hide>`       | modify (notmuch/imap) tags and then hide message                        |
| `<modify-tags>`                 | modify (notmuch/imap) tags                                              |
| `<next-new-then-unread>`        | jump to the next new or unread message                                  |
| `<next-new>`                    | jump to the next new message                                            |
| `<next-subthread>`              | jump to the next subthread                                              |
| `<next-thread>`                 | jump to the next thread                                                 |
| `<next-undeleted>`              | move to the next undeleted message                                      |
| `<next-unread-mailbox>`         | open next mailbox with new mail                                         |
| `<next-unread>`                 | jump to the next unread message                                         |
| `<open-all-threads>`            | uncollapse all threads                                                  |
| `<open-thread>`                 | uncollapse current thread                                               |
| `<parent-message>`              | jump to parent message in thread                                        |
| `<pipe-entry>`                  | pipe message/attachment to a shell command                              |
| `<pipe-message>`                | pipe message/attachment to a shell command                              |
| `<post-message>`                | post message to newsgroup                                               |
| `<previous-new-then-unread>`    | jump to the previous new or unread message                              |
| `<previous-new>`                | jump to the previous new message                                        |
| `<previous-subthread>`          | jump to previous subthread                                              |
| `<previous-thread>`             | jump to previous thread                                                 |
| `<previous-undeleted>`          | move to the previous undeleted message                                  |
| `<previous-unread>`             | jump to the previous unread message                                     |
| `<print-message>`               | print the current entry                                                 |
| `<purge-message>`               | delete the current entry, bypassing the trash folder                    |
| `<purge-thread>`                | delete the current thread, bypassing the trash folder                   |
| `<quasi-delete>`                | delete from NeoMutt, don't touch on disk                                |
| `<query>`                       | query external program for addresses                                    |
| `<quit>`                        | save changes to mailbox and quit                                        |
| `<read-subthread>`              | mark the current subthread as read                                      |
| `<read-thread>`                 | mark the current thread as read                                         |
| `<recall-message>`              | recall a postponed message                                              |
| `<reconstruct-thread>`          | reconstruct thread containing current message                           |
| `<reply>`                       | reply to a message                                                      |
| `<resend-message>`              | use the current message as a template for a new one                     |
| `<root-message>`                | jump to root message in thread                                          |
| `<save-message>`                | save message/attachment to a mailbox/file                               |
| `<set-flag>`                    | set a status flag on a message                                          |
| `<show-limit>`                  | show currently active limit pattern                                     |
| `<sort-mailbox>`                | sort messages                                                           |
| `<sort-reverse>`                | sort messages in reverse order                                          |
| `<sync-mailbox>`                | save changes to mailbox                                                 |
| `<tag-pattern>`                 | tag non-hidden messages matching a pattern                              |
| `<tag-subthread>`               | tag the current subthread                                               |
| `<tag-thread>`                  | tag the current thread                                                  |
| `<toggle-new>`                  | toggle a message's 'new' flag                                           |
| `<toggle-read>`                 | toggle view of read messages                                            |
| `<toggle-write>`                | toggle whether the mailbox will be rewritten                            |
| `<undelete-message>`            | undelete the current entry                                              |
| `<undelete-pattern>`            | undelete non-hidden messages matching a pattern                         |
| `<undelete-subthread>`          | undelete all messages in subthread                                      |
| `<undelete-thread>`             | undelete all messages in thread                                         |
| `<untag-pattern>`               | untag non-hidden messages matching a pattern                            |
| `<vfolder-from-query-readonly>` | generate a read-only virtual folder from query                          |
| `<vfolder-from-query>`          | generate virtual folder from query                                      |
| `<vfolder-window-backward>`     | shifts virtual folder time window backwards                             |
| `<vfolder-window-forward>`      | shifts virtual folder time window forwards                              |
| `<vfolder-window-reset>`        | resets virtual folder time window to the present                        |
| `<view-attachments>`            | show MIME attachments                                                   |
| `<view-raw-message>`            | show the raw message                                                    |

## [Pager Menu](menu-pager)

The email reading view that displays a message's contents.
You can scroll, search within the text, and perform many of the same actions as the index.

| Function                        | Description                                                             |
|---------------------------------|-------------------------------------------------------------------------|
| `<bottom>`                      | jump to the bottom of the message                                       |
| `<bounce-message>`              | remail a message to another user                                        |
| `<break-thread>`                | break the thread in two                                                 |
| `<buffy-list>`                  | {bdg-danger}`Deprecated` use `<mailbox-list>`                           |
| `<change-folder-readonly>`      | open a different folder in read only mode                               |
| `<change-folder>`               | open a different folder                                                 |
| `<change-newsgroup-readonly>`   | open a different newsgroup in read only mode                            |
| `<change-newsgroup>`            | open a different newsgroup                                              |
| `<change-vfolder>`              | open a different virtual folder                                         |
| `<check-stats>`                 | calculate message statistics for all mailboxes                          |
| `<check-traditional-pgp>`       | check for classic PGP                                                   |
| `<clear-flag>`                  | clear a status flag from a message                                      |
| `<compose-to-sender>`           | compose new message to the current message sender                       |
| `<copy-message>`                | copy a message to a file/mailbox                                        |
| `<create-alias>`                | create an alias from a message sender                                   |
| `<decode-copy>`                 | make decoded (text/plain) copy                                          |
| `<decode-save>`                 | make decoded copy (text/plain) and delete                               |
| `<decrypt-copy>`                | make decrypted copy                                                     |
| `<decrypt-save>`                | make decrypted copy and delete                                          |
| `<delete-message>`              | delete the current entry                                                |
| `<delete-subthread>`            | delete all messages in subthread                                        |
| `<delete-thread>`               | delete all messages in thread                                           |
| `<display-address>`             | display full address of sender                                          |
| `<display-toggle-weed>`         | display message and toggle header weeding                               |
| `<edit-label>`                  | add, change, or delete a message's label                                |
| `<edit-or-view-raw-message>`    | edit the raw message if the mailbox is not read-only, otherwise view it |
| `<edit-raw-message>`            | edit the raw message (edit and edit-raw-message are synonyms)           |
| `<edit-type>`                   | edit attachment content type                                            |
| `<edit>`                        | edit the raw message (edit and edit-raw-message are synonyms)           |
| `<enter-command>`               | enter a neomuttrc command                                               |
| `<entire-thread>`               | read entire thread of the current message                               |
| `<error-history>`               | {bdg-danger}`Deprecated` use `<show-log-messages>`                      |
| `<exit>`                        | exit this menu                                                          |
| `<extract-keys>`                | extract supported public keys                                           |
| `<flag-message>`                | toggle a message's 'important' flag                                     |
| `<followup-message>`            | followup to newsgroup                                                   |
| `<forget-passphrase>`           | wipe passphrases from memory                                            |
| `<forward-message>`             | forward a message with comments                                         |
| `<forward-to-group>`            | forward to newsgroup                                                    |
| `<group-chat-reply>`            | reply to all recipients preserving To/Cc                                |
| `<group-reply>`                 | reply to all recipients                                                 |
| `<half-down>`                   | scroll down 1/2 page                                                    |
| `<half-up>`                     | scroll up 1/2 page                                                      |
| `<help>`                        | this screen                                                             |
| `<imap-fetch-mail>`             | force retrieval of mail from IMAP server                                |
| `<imap-logout-all>`             | logout from all IMAP servers                                            |
| `<jump>`                        | jump to an index number                                                 |
| `<link-threads>`                | link tagged message to the current one                                  |
| `<list-reply>`                  | reply to specified mailing list                                         |
| `<list-subscribe>`              | subscribe to a mailing list                                             |
| `<list-unsubscribe>`            | unsubscribe from a mailing list                                         |
| `<mail-key>`                    | mail a PGP public key                                                   |
| `<mail>`                        | compose a new mail message                                              |
| `<mailbox-list>`                | list mailboxes with new mail                                            |
| `<mark-as-new>`                 | toggle a message's 'new' flag                                           |
| `<modify-labels-then-hide>`     | modify (notmuch/imap) tags and then hide message                        |
| `<modify-labels>`               | modify (notmuch/imap) tags                                              |
| `<modify-tags-then-hide>`       | modify (notmuch/imap) tags and then hide message                        |
| `<modify-tags>`                 | modify (notmuch/imap) tags                                              |
| `<next-entry>`                  | move to the next entry                                                  |
| `<next-line>`                   | scroll down one line                                                    |
| `<next-new-then-unread>`        | jump to the next new or unread message                                  |
| `<next-new>`                    | jump to the next new message                                            |
| `<next-page>`                   | move to the next page                                                   |
| `<next-subthread>`              | jump to the next subthread                                              |
| `<next-thread>`                 | jump to the next thread                                                 |
| `<next-undeleted>`              | move to the next undeleted message                                      |
| `<next-unread-mailbox>`         | open next mailbox with new mail                                         |
| `<next-unread>`                 | jump to the next unread message                                         |
| `<parent-message>`              | jump to parent message in thread                                        |
| `<pipe-entry>`                  | pipe message/attachment to a shell command                              |
| `<pipe-message>`                | pipe message/attachment to a shell command                              |
| `<post-message>`                | post message to newsgroup                                               |
| `<previous-entry>`              | move to the previous entry                                              |
| `<previous-line>`               | scroll up one line                                                      |
| `<previous-new-then-unread>`    | jump to the previous new or unread message                              |
| `<previous-new>`                | jump to the previous new message                                        |
| `<previous-page>`               | move to the previous page                                               |
| `<previous-subthread>`          | jump to previous subthread                                              |
| `<previous-thread>`             | jump to previous thread                                                 |
| `<previous-undeleted>`          | move to the previous undeleted message                                  |
| `<previous-unread>`             | jump to the previous unread message                                     |
| `<print-entry>`                 | print the current entry                                                 |
| `<print-message>`               | print the current entry                                                 |
| `<purge-message>`               | delete the current entry, bypassing the trash folder                    |
| `<purge-thread>`                | delete the current thread, bypassing the trash folder                   |
| `<quasi-delete>`                | delete from NeoMutt, don't touch on disk                                |
| `<quit>`                        | save changes to mailbox and quit                                        |
| `<read-subthread>`              | mark the current subthread as read                                      |
| `<read-thread>`                 | mark the current thread as read                                         |
| `<recall-message>`              | recall a postponed message                                              |
| `<reconstruct-thread>`          | reconstruct thread containing current message                           |
| `<redraw-screen>`               | clear and redraw the screen                                             |
| `<reply>`                       | reply to a message                                                      |
| `<resend-message>`              | use the current message as a template for a new one                     |
| `<root-message>`                | jump to root message in thread                                          |
| `<save-entry>`                  | save message/attachment to a mailbox/file                               |
| `<save-message>`                | save message/attachment to a mailbox/file                               |
| `<search-next>`                 | search for next match                                                   |
| `<search-opposite>`             | search for next match in opposite direction                             |
| `<search-reverse>`              | search backwards for a regular expression                               |
| `<search-toggle>`               | toggle search pattern coloring                                          |
| `<search>`                      | search for a regular expression                                         |
| `<set-flag>`                    | set a status flag on a message                                          |
| `<shell-escape>`                | invoke a command in a subshell                                          |
| `<show-log-messages>`           | show log (and debug) messages                                           |
| `<show-version>`                | show the NeoMutt version number and date                                |
| `<skip-headers>`                | jump to first line after headers                                        |
| `<skip-quoted>`                 | skip beyond quoted text                                                 |
| `<sort-mailbox>`                | sort messages                                                           |
| `<sort-reverse>`                | sort messages in reverse order                                          |
| `<sync-mailbox>`                | save changes to mailbox                                                 |
| `<tag-message>`                 | tag the current entry                                                   |
| `<toggle-quoted>`               | toggle display of quoted text                                           |
| `<toggle-write>`                | toggle whether the mailbox will be rewritten                            |
| `<top>`                         | jump to the top of the message                                          |
| `<undelete-message>`            | undelete the current entry                                              |
| `<undelete-subthread>`          | undelete all messages in subthread                                      |
| `<undelete-thread>`             | undelete all messages in thread                                         |
| `<vfolder-from-query-readonly>` | generate a read-only virtual folder from query                          |
| `<vfolder-from-query>`          | generate virtual folder from query                                      |
| `<view-attachments>`            | show MIME attachments                                                   |
| `<view-raw-message>`            | show the raw message                                                    |
| `<what-key>`                    | display the keycode for a key press                                     |

## [PGP Menu](menu-pgp)

Select a PGP key when encrypting or signing an email.
You can verify key details before choosing which key to use.

| Function       | Description            |
|----------------|------------------------|
| `<exit>`       | exit this menu         |
| `<verify-key>` | verify a public key    |
| `<view-name>`  | view the key's user id |

## [Postpone Menu](menu-postpone)

Select from your saved draft emails to resume editing.
You can pick a previously postponed message to continue composing it.

| Function           | Description                |
|--------------------|----------------------------|
| `<delete-entry>`   | delete the current entry   |
| `<exit>`           | exit this menu             |
| `<undelete-entry>` | undelete the current entry |

## [Query Menu](menu-query)

Display results from an external address-book query.
You can search for contacts, create aliases from the results, and compose messages to selected addresses.

| Function          | Description                                  |
|-------------------|----------------------------------------------|
| `<create-alias>`  | create an alias from a message sender        |
| `<exit>`          | exit this menu                               |
| `<limit>`         | show only messages matching a pattern        |
| `<mail>`          | compose a new mail message                   |
| `<query-append>`  | append new query results to current results  |
| `<query>`         | query external program for addresses         |
| `<sort-reverse>`  | sort messages in reverse order               |
| `<sort>`          | sort messages                                |
| `<tag-pattern>`   | tag non-hidden messages matching a pattern   |
| `<untag-pattern>` | untag non-hidden messages matching a pattern |

## [Sidebar Menu](menu-sidebar)

Navigate the sidebar panel that lists your mailboxes.
You can move between mailboxes, open them, and toggle the sidebar's visibility.

| Function                   | Description                                          |
|----------------------------|------------------------------------------------------|
| `<sidebar-abort-search>`   | close the sidebar search                             |
| `<sidebar-first>`          | move the highlight to the first mailbox              |
| `<sidebar-last>`           | move the highlight to the last mailbox               |
| `<sidebar-next-new>`       | move the highlight to next mailbox with new mail     |
| `<sidebar-next>`           | move the highlight to next mailbox                   |
| `<sidebar-open>`           | open highlighted mailbox                             |
| `<sidebar-page-down>`      | scroll the sidebar down 1 page                       |
| `<sidebar-page-up>`        | scroll the sidebar up 1 page                         |
| `<sidebar-prev-new>`       | move the highlight to previous mailbox with new mail |
| `<sidebar-prev>`           | move the highlight to previous mailbox               |
| `<sidebar-start-search>`   | fuzzy search the sidebar                             |
| `<sidebar-toggle-virtual>` | toggle between mailboxes and virtual mailboxes       |
| `<sidebar-toggle-visible>` | make the sidebar (in)visible                         |

## [S/MIME Menu](menu-smime)

Select an S/MIME certificate when encrypting or signing an email.
You can verify certificate details before choosing which one to use.

| Function       | Description            |
|----------------|------------------------|
| `<exit>`       | exit this menu         |
| `<verify-key>` | verify a public key    |
| `<view-name>`  | view the key's user id |

