# Functions

## Alias

| Function               | Description                                  |
| :--------------------- | :------------------------------------------- |
| `<create-alias>`       | Create an alias from a message sender        |
| `<delete-entry>`       | Delete the current entry                     |
| `<exit>`               | Exit this menu                               |
| `<select-entry>`       | Select the current entry                     |
| `<mail>`               | Compose a new mail message                   |
| `<limit>`              | Show only messages matching a pattern        |
| `<tag-pattern>`        | Tag non-hidden messages matching a pattern   |
| `<untag-pattern>`      | Untag non-hidden messages matching a pattern |
| `<query>`              | Query external program for addresses         |
| `<query-append>`       | Append new query results to current results  |
| `<search>`             | Search for a regular expression              |
| `<search-next>`        | Search for next match                        |
| `<search-opposite>`    | Search for next match in opposite direction  |
| `<search-reverse>`     | Search backwards for a regular expression    |
| `<sort-alias>`         | Sort messages                                |
| `<sort-alias-reverse>` | Sort messages in reverse order               |
| `<undelete-entry>`     | Undelete the current entry                   |

## Attach

| Function                  | Description                                          |
| :------------------------ | :--------------------------------------------------- |
| `<collapse-parts>`        | Toggle display of subparts                           |
| `<delete-entry>`          | Delete the current entry                             |
| `<edit-type>`             | Edit attachment content type                         |
| `<pipe-entry>`            | Pipe message/attachment to a shell command           |
| `<print-entry>`           | Print the current entry                              |
| `<save-entry>`            | Save message/attachment to a mailbox/file            |
| `<undelete-entry>`        | Undelete the current entry                           |
| `<view-attach>`           | View attachment using mailcap entry if necessary     |
| `<view-mailcap>`          | Force viewing of attachment using mailcap            |
| `<view-pager>`            | View attachment in pager using copiousoutput mailcap |
| `<view-text>`             | View attachment as text                              |
| `<bounce-message>`        | Remail a message to another user                     |
| `<check-traditional-pgp>` | Check for classic PGP                                |
| `<compose-to-sender>`     | Compose new message to the current message sender    |
| `<display-toggle-weed>`   | Display message and toggle header weeding            |
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
| `<reply>`                 | Reply to a message                                   |
| `<resend-message>`        | Use the current message as a template for a new one  |

## Autocrypt

| Function                  | Description                                    |
| :------------------------ | :--------------------------------------------- |
| `<create-account>`        | Create a new autocrypt account                 |
| `<delete-account>`        | Delete the current account                     |
| `<toggle-active>`         | Toggle the current account active/inactive     |
| `<toggle-prefer-encrypt>` | Toggle the current account prefer-encrypt flag |
| `<exit>`                  | Exit this menu                                 |

## Browser

| Function                | Description                                                |
| :---------------------- | :--------------------------------------------------------- |
| `<goto-folder>`         | Swap the current folder position with $folder if it exists |
| `<select-new>`          | Select a new file in this directory                        |
| `<subscribe>`           | Subscribe to current mbox (IMAP/NNTP only)                 |
| `<display-filename>`    | Display the currently selected file's name                 |
| `<toggle-subscribed>`   | Toggle view all/subscribed mailboxes (IMAP only)           |
| `<unsubscribe>`         | Unsubscribe from current mbox (IMAP/NNTP only)             |
| `<view-file>`           | View file                                                  |
| `<catchup>`             | Mark all articles in newsgroup as read                     |
| `<change-dir>`          | Change directories                                         |
| `<check-new>`           | Check mailboxes for new mail                               |
| `<create-mailbox>`      | Create a new mailbox (IMAP only)                           |
| `<delete-mailbox>`      | Delete the current mailbox (IMAP only)                     |
| `<descend-directory>`   | Descend into a directory                                   |
| `<enter-mask>`          | Enter a file mask                                          |
| `<exit>`                | Exit this menu                                             |
| `<select-entry>`        | Select the current entry                                   |
| `<goto-parent>`         | Go to parent directory                                     |
| `<reload-active>`       | Load list of all newsgroups from NNTP server               |
| `<mailbox-list>`        | List mailboxes with new mail                               |
| `<rename-mailbox>`      | Rename the current mailbox (IMAP only)                     |
| `<sort>`                | Sort messages                                              |
| `<sort-reverse>`        | Sort messages in reverse order                             |
| `<subscribe-pattern>`   | Subscribe to newsgroups matching a pattern                 |
| `<toggle-mailboxes>`    | Toggle whether to browse mailboxes or all files            |
| `<uncatchup>`           | Mark all articles in newsgroup as unread                   |
| `<unsubscribe-pattern>` | Unsubscribe from newsgroups matching a pattern             |

## Compose

| Function                | Description                                          |
| :---------------------- | :--------------------------------------------------- |
| `<attach-file>`         | Attach files to this message                         |
| `<attach-key>`          | Attach a PGP public key                              |
| `<attach-message>`      | Attach messages to this message                      |
| `<attach-news-message>` | Attach news articles to this message                 |
| `<detach-file>`         | Delete the current entry                             |
| `<edit-content-id>`     | Edit the 'Content-ID' of the attachment              |
| `<edit-description>`    | Edit attachment description                          |  |
| `<edit-encoding>`       | Edit attachment transfer-encoding                    |
| `<edit-language>`       | Edit the 'Content-Language' of the attachment        |
| `<edit-mime>`           | Edit attachment using mailcap entry                  |
| `<edit-type>`           | Edit attachment content type                         |
| `<filter-entry>`        | Filter attachment through a shell command            |
| `<get-attachment>`      | Get a temporary copy of an attachment                |
| `<group-alternatives>`  | Group tagged attachments as 'multipart/alternative'  |
| `<group-multilingual>`  | Group tagged attachments as 'multipart/multilingual' |
| `<group-related>`       | Group tagged attachments as 'multipart/related'      |
| `<move-down>`           | Move an attachment down in the attachment list       |
| `<move-up>`             | Move an attachment up in the attachment list         |
| `<new-mime>`            | Compose new attachment using mailcap entry           |
| `<pipe-entry>`          | Pipe message/attachment to a shell command           |
| `<print-entry>`         | Print the current entry                              |
| `<rename-attachment>`   | Send attachment with a different name                |
| `<copy-file>`           | Save message/attachment to a mailbox/file            |
| `<toggle-disposition>`  | Toggle disposition between inline/attachment         |
| `<toggle-recode>`       | Toggle recoding of this attachment                   |
| `<toggle-unlink>`       | Toggle whether to delete file after sending it       |
| `<ungroup-attachment>`  | Ungroup 'multipart' attachment                       |
| `<update-encoding>`     | Update an attachment's encoding info                 |
| `<view-attach>`         | View attachment using mailcap entry if necessary     |
| `<view-mailcap>`        | Force viewing of attachment using mailcap            |
| `<view-pager>`          | View attachment in pager using copiousoutput mailcap |
| `<view-text>`           | View attachment as text                              |
| `<edit-file>`           | Edit the file to be attached                         |
| `<edit-message>`        | Edit the message                                     |
| `<ispell>`              | Run ispell on the message                            |
| `<postpone-message>`    | Save this message to send later                      |
| `<rename-file>`         | Rename/move an attached file                         |
| `<send-message>`        | Send the message                                     |
| `<write-fcc>`           | Write the message to a folder                        |
| `<display-toggle-weed>` | Display message and toggle header weeding            |
| `<edit-headers>`        | Edit the message with headers                        |
| `<exit>`                | Exit this menu                                       |
| `<forget-passphrase>`   | Wipe passphrases from memory                         |

## Enter

| Function            | Description                                         |
| :------------------ | :-------------------------------------------------- |
| `<backspace>`       | Delete the char in front of the cursor              |
| `<backward-char>`   | Move the cursor one character to the left           |
| `<backward-word>`   | Move the cursor to the beginning of the word        |
| `<bol>`             | Jump to the beginning of the line                   |
| `<capitalize-word>` | Capitalize the word                                 |
| `<complete>`        | Complete filename or alias                          |
| `<complete-query>`  | Complete address with query                         |
| `<delete-char>`     | Delete the char under the cursor                    |
| `<downcase-word>`   | Convert the word to lower case                      |
| `<eol>`             | Jump to the end of the line                         |
| `<forward-char>`    | Move the cursor one character to the right          |
| `<forward-word>`    | Move the cursor to the end of the word              |
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
| `<transpose-chars>` | Transpose character under cursor with previous      |
| `<upcase-word>`     | Convert the word to upper case                      |
| `<help>`            | This screen                                         |
| `<redraw-screen>`   | Clear and redraw the screen                         |

## Envelope

| Function              | Description                                    |
| :-------------------- | :--------------------------------------------- |
| `<autocrypt-menu>`    | Show autocrypt compose menu options            |
| `<pgp-menu>`          | Show PGP options                               |
| `<smime-menu>`        | Show S/MIME options                            |
| `<edit-bcc>`          | Edit the BCC list                              |
| `<edit-cc>`           | Edit the CC list                               |
| `<edit-fcc>`          | Enter a file to save a copy of this message in |
| `<edit-followup-to>`  | Edit the Followup-To field                     |
| `<edit-from>`         | Edit the from field                            |
| `<edit-newsgroups>`   | Edit the newsgroups list                       |
| `<edit-reply-to>`     | Edit the Reply-To field                        |
| `<edit-subject>`      | Edit the subject of this message               |
| `<edit-to>`           | Edit the TO list                               |
| `<edit-x-comment-to>` | Edit the X-Comment-To field                    |

## Generic

| Function            | Description                                 |
| :------------------ | :------------------------------------------ |
| `<bottom-page>`     | Move to the bottom of the page              |
| `<current-bottom>`  | Move entry to bottom of screen              |
| `<current-middle>`  | Move entry to middle of screen              |
| `<current-top>`     | Move entry to top of screen                 |
| `<first-entry>`     | Move to the first entry                     |
| `<half-down>`       | Scroll down 1/2 page                        |
| `<half-up>`         | Scroll up 1/2 page                          |
| `<help>`            | This screen                                 |
| `<jump>`            | Jump to an index number                     |
| `<jump>`            | Jump to an index number                     |
| `<jump>`            | Jump to an index number                     |
| `<jump>`            | Jump to an index number                     |
| `<jump>`            | Jump to an index number                     |
| `<jump>`            | Jump to an index number                     |
| `<jump>`            | Jump to an index number                     |
| `<jump>`            | Jump to an index number                     |
| `<jump>`            | Jump to an index number                     |
| `<jump>`            | Jump to an index number                     |
| `<last-entry>`      | Move to the last entry                      |
| `<middle-page>`     | Move to the middle of the page              |
| `<next-entry>`      | Move to the next entry                      |
| `<next-line>`       | Scroll down one line                        |
| `<next-page>`       | Move to the next page                       |
| `<previous-entry>`  | Move to the previous entry                  |
| `<previous-line>`   | Scroll up one line                          |
| `<previous-page>`   | Move to the previous page                   |
| `<search>`          | Search for a regular expression             |
| `<search-next>`     | Search for next match                       |
| `<search-opposite>` | Search for next match in opposite direction |
| `<search-reverse>`  | Search backwards for a regular expression   |
| `<top-page>`        | Move to the top of the page                 |

## Global

| Function              | Description                                    |
| :-------------------- | :--------------------------------------------- |
| `<check-stats>`       | Calculate message statistics for all mailboxes |
| `<enter-command>`     | Enter a neomuttrc command                      |
| `<redraw-screen>`     | Clear and redraw the screen                    |
| `<shell-escape>`      | Invoke a command in a subshell                 |
| `<show-log-messages>` | Show log (and debug) messages                  |
| `<show-version>`      | Show the NeoMutt version number and date       |
| `<what-key>`          | Display the keycode for a key press            |

## Gpgme

| Function         | Description              |
| :--------------- | :----------------------- |
| `<exit>`         | Exit this menu           |
| `<select-entry>` | Select the current entry |
| `<verify-key>`   | Verify a public key      |
| `<view-name>`    | View the key's user id   |

## History

| Function         | Description                      |
| :--------------- | :------------------------------- |
| `<select-entry>` | Select the current entry         |
| `<quit>`         | Save changes to mailbox and quit |

## Index

| Function                        | Description                                                             |
| :------------------------------ | :---------------------------------------------------------------------- |
| `<alias-dialog>`                | Open the aliases dialog                                                 |
| `<edit-type>`                   | Edit attachment content type                                            |
| `<bounce-message>`              | Remail a message to another user                                        |
| `<catchup>`                     | Mark all articles in newsgroup as read                                  |
| `<check-traditional-pgp>`       | Check for classic PGP                                                   |
| `<compose-to-sender>`           | Compose new message to the current message sender                       |
| `<copy-message>`                | Copy a message to a file/mailbox                                        |
| `<create-alias>`                | Create an alias from a message sender                                   |
| `<decode-copy>`                 | Make decoded (text/plain) copy                                          |
| `<decode-save>`                 | Make decoded copy (text/plain) and delete                               |
| `<decrypt-copy>`                | Make decrypted copy                                                     |
| `<decrypt-save>`                | Make decrypted copy and delete                                          |
| `<delete-entry>`                | Delete the current entry                                                |
| `<delete-subthread>`            | Delete all messages in subthread                                        |
| `<delete-thread>`               | Delete all messages in thread                                           |
| `<display-address>`             | Display full address of sender                                          |
| `<display-toggle-weed>`         | Display message and toggle header weeding                               |
| `<display-message>`             | Display a message                                                       |
| `<edit-label>`                  | Add, change, or delete a message's label                                |
| `<edit-or-view-raw-message>`    | Edit the raw message if the mailbox is not read-only, otherwise view it |
| `<edit>`                        | Edit the raw message (edit and edit-raw-message are synonyms)           |
| `<end-cond>`                    | End of conditional execution (noop)                                     |
| `<exit>`                        | Exit this menu                                                          |
| `<extract-keys>`                | Extract supported public keys                                           |
| `<flag-message>`                | Toggle a message's 'important' flag                                     |
| `<followup-message>`            | Followup to newsgroup                                                   |
| `<forget-passphrase>`           | Wipe passphrases from memory                                            |
| `<forward-message>`             | Forward a message with comments                                         |
| `<forward-to-group>`            | Forward to newsgroup                                                    |
| `<get-children>`                | Get all children of the current message                                 |
| `<get-message>`                 | Get message with Message-Id                                             |
| `<get-parent>`                  | Get parent of the current message                                       |
| `<select-entry>`                | Select the current entry                                                |
| `<group-chat-reply>`            | Reply to all recipients preserving To/Cc                                |
| `<group-reply>`                 | Reply to all recipients                                                 |
| `<jump>`                        | Jump to an index number                                                 |
| `<jump>`                        | Jump to an index number                                                 |
| `<jump>`                        | Jump to an index number                                                 |
| `<jump>`                        | Jump to an index number                                                 |
| `<jump>`                        | Jump to an index number                                                 |
| `<jump>`                        | Jump to an index number                                                 |
| `<jump>`                        | Jump to an index number                                                 |
| `<jump>`                        | Jump to an index number                                                 |
| `<jump>`                        | Jump to an index number                                                 |
| `<jump>`                        | Jump to an index number                                                 |
| `<limit-current-thread>`        | Limit view to current thread                                            |
| `<list-reply>`                  | Reply to specified mailing list                                         |
| `<list-subscribe>`              | Subscribe to a mailing list                                             |
| `<list-unsubscribe>`            | Unsubscribe from a mailing list                                         |
| `<mail>`                        | Compose a new mail message                                              |
| `<mailbox-list>`                | List mailboxes with new mail                                            |
| `<mail-key>`                    | Mail a PGP public key                                                   |
| `<break-thread>`                | Break the thread in two                                                 |
| `<change-folder>`               | Open a different folder                                                 |
| `<change-folder-readonly>`      | Open a different folder in read only mode                               |
| `<change-newsgroup>`            | Open a different newsgroup                                              |
| `<change-newsgroup-readonly>`   | Open a different newsgroup in read only mode                            |
| `<clear-flag>`                  | Clear a status flag from a message                                      |
| `<collapse-all>`                | Collapse/uncollapse all threads                                         |
| `<collapse-thread>`             | Collapse/uncollapse current thread                                      |
| `<delete-pattern>`              | Delete non-hidden messages matching a pattern                           |
| `<fetch-mail>`                  | Retrieve mail from POP server                                           |
| `<imap-fetch-mail>`             | Force retrieval of mail from IMAP server                                |
| `<imap-logout-all>`             | Logout from all IMAP servers                                            |
| `<limit>`                       | Show only messages matching a pattern                                   |
| `<link-threads>`                | Link tagged message to the current one                                  |
| `<modify-tags>`                 | Modify (notmuch/imap) tags                                              |
| `<modify-tags-then-hide>`       | Modify (notmuch/imap) tags and then hide message                        |
| `<next-new>`                    | Jump to the next new message                                            |
| `<next-new-then-unread>`        | Jump to the next new or unread message                                  |
| `<next-subthread>`              | Jump to the next subthread                                              |
| `<next-thread>`                 | Jump to the next thread                                                 |
| `<next-undeleted>`              | Move to the next undeleted message                                      |
| `<next-unread>`                 | Jump to the next unread message                                         |
| `<next-unread-mailbox>`         | Open next mailbox with new mail                                         |
| `<parent-message>`              | Jump to parent message in thread                                        |
| `<previous-new>`                | Jump to the previous new message                                        |
| `<previous-new-then-unread>`    | Jump to the previous new or unread message                              |
| `<previous-subthread>`          | Jump to previous subthread                                              |
| `<previous-thread>`             | Jump to previous thread                                                 |
| `<previous-undeleted>`          | Move to the previous undeleted message                                  |
| `<previous-unread>`             | Jump to the previous unread message                                     |
| `<quasi-delete>`                | Delete from NeoMutt, don't touch on disk                                |
| `<read-subthread>`              | Mark the current subthread as read                                      |
| `<read-thread>`                 | Mark the current thread as read                                         |
| `<root-message>`                | Jump to root message in thread                                          |
| `<set-flag>`                    | Set a status flag on a message                                          |
| `<show-limit>`                  | Show currently active limit pattern                                     |
| `<sync-mailbox>`                | Save changes to mailbox                                                 |
| `<tag-pattern>`                 | Tag non-hidden messages matching a pattern                              |
| `<undelete-pattern>`            | Undelete non-hidden messages matching a pattern                         |
| `<untag-pattern>`               | Untag non-hidden messages matching a pattern                            |
| `<mark-message>`                | Create a hotkey macro for the current message                           |
| `<next-entry>`                  | Move to the next entry                                                  |
| `<pipe-message>`                | Pipe message/attachment to a shell command                              |
| `<post-message>`                | Post message to newsgroup                                               |
| `<previous-entry>`              | Move to the previous entry                                              |
| `<print-message>`               | Print the current entry                                                 |
| `<purge-message>`               | Delete the current entry, bypassing the trash folder                    |
| `<purge-thread>`                | Delete the current thread, bypassing the trash folder                   |
| `<query>`                       | Query external program for addresses                                    |
| `<quit>`                        | Save changes to mailbox and quit                                        |
| `<recall-message>`              | Recall a postponed message                                              |
| `<reconstruct-thread>`          | Reconstruct thread containing current message                           |
| `<reply>`                       | Reply to a message                                                      |
| `<resend-message>`              | Use the current message as a template for a new one                     |
| `<save-message>`                | Save message/attachment to a mailbox/file                               |
| `<search>`                      | Search for a regular expression                                         |
| `<search-next>`                 | Search for next match                                                   |
| `<search-opposite>`             | Search for next match in opposite direction                             |
| `<search-reverse>`              | Search backwards for a regular expression                               |
| `<sort-mailbox>`                | Sort messages                                                           |
| `<sort-reverse>`                | Sort messages in reverse order                                          |
| `<tag-entry>`                   | Tag the current entry                                                   |
| `<tag-subthread>`               | Tag the current subthread                                               |
| `<tag-thread>`                  | Tag the current thread                                                  |
| `<toggle-new>`                  | Toggle a message's 'new' flag                                           |
| `<toggle-read>`                 | Toggle view of read messages                                            |
| `<toggle-write>`                | Toggle whether the mailbox will be rewritten                            |
| `<undelete-message>`            | Undelete the current entry                                              |
| `<undelete-subthread>`          | Undelete all messages in subthread                                      |
| `<undelete-thread>`             | Undelete all messages in thread                                         |
| `<view-attachments>`            | Show MIME attachments                                                   |
| `<view-raw-message>`            | Show the raw message                                                    |
| `<autocrypt-acct-menu>`         | Manage autocrypt accounts                                               |
| `<change-vfolder>`              | Open a different virtual folder                                         |
| `<entire-thread>`               | Read entire thread of the current message                               |
| `<vfolder-from-query>`          | Generate virtual folder from query                                      |
| `<vfolder-from-query-readonly>` | Generate a read-only virtual folder from query                          |
| `<vfolder-window-backward>`     | Shifts virtual folder time window backwards                             |
| `<vfolder-window-forward>`      | Shifts virtual folder time window forwards                              |
| `<vfolder-window-reset>`        | Resets virtual folder time window to the present                        |

## Pager

| Function             | Description                                 |
| :------------------- | :------------------------------------------ |
| `<exit>`             | Exit this menu                              |
| `<half-down>`        | Scroll down 1/2 page                        |
| `<half-up>`          | Scroll up 1/2 page                          |
| `<help>`             | This screen                                 |
| `<next-line>`        | Scroll down one line                        |
| `<next-page>`        | Move to the next page                       |
| `<bottom>`           | Jump to the bottom of the message           |
| `<toggle-quoted>`    | Toggle display of quoted text               |
| `<skip-headers>`     | Jump to first line after headers            |
| `<skip-quoted>`      | Skip beyond quoted text                     |
| `<top>`              | Jump to the top of the message              |
| `<previous-line>`    | Scroll up one line                          |
| `<previous-page>`    | Move to the previous page                   |
| `<save-message>`     | Save message/attachment to a mailbox/file   |
| `<search>`           | Search for a regular expression             |
| `<search-reverse>`   | Search backwards for a regular expression   |
| `<search-next>`      | Search for next match                       |
| `<search-opposite>`  | Search for next match in opposite direction |
| `<search-toggle>`    | Toggle search pattern coloring              |
| `<view-attachments>` | Show MIME attachments                       |

## Pattern

| Function         | Description                      |
| :--------------- | :------------------------------- |
| `<select-entry>` | Select the current entry         |
| `<quit>`         | Save changes to mailbox and quit |

## Pgp

| Function         | Description              |
| :--------------- | :----------------------- |
| `<exit>`         | Exit this menu           |
| `<select-entry>` | Select the current entry |
| `<verify-key>`   | Verify a public key      |
| `<view-name>`    | View the key's user id   |

## Postpone

| Function            | Description                                 |
| :------------------ | :------------------------------------------ |
| `<delete-entry>`    | Delete the current entry                    |
| `<exit>`            | Exit this menu                              |
| `<select-entry>`    | Select the current entry                    |
| `<search>`          | Search for a regular expression             |
| `<search-next>`     | Search for next match                       |
| `<search-opposite>` | Search for next match in opposite direction |
| `<search-reverse>`  | Search backwards for a regular expression   |
| `<undelete-entry>`  | Undelete the current entry                  |

## Preview

| Function              | Description                           |
| :-------------------- | :------------------------------------ |
| `<preview-page-down>` | Show the next page of the message     |
| `<preview-page-up>`   | Show the previous page of the message |

## Sidebar

| Function                   | Description                                          |
| :------------------------- | :--------------------------------------------------- |
| `<sidebar-first>`          | Move the highlight to the first mailbox              |
| `<sidebar-last>`           | Move the highlight to the last mailbox               |
| `<sidebar-next>`           | Move the highlight to next mailbox                   |
| `<sidebar-next-new>`       | Move the highlight to next mailbox with new mail     |
| `<sidebar-open>`           | Open highlighted mailbox                             |
| `<sidebar-page-down>`      | Scroll the sidebar down 1 page                       |
| `<sidebar-page-up>`        | Scroll the sidebar up 1 page                         |
| `<sidebar-prev>`           | Move the highlight to previous mailbox               |
| `<sidebar-prev-new>`       | Move the highlight to previous mailbox with new mail |
| `<sidebar-toggle-virtual>` | Toggle between mailboxes and virtual mailboxes       |
| `<sidebar-toggle-visible>` | Make the sidebar (in)visible                         |

## Smime

| Function         | Description              |
| :--------------- | :----------------------- |
| `<exit>`         | Exit this menu           |
| `<select-entry>` | Select the current entry |

