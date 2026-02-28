---
title: Pager Menu Functions
description: Default key bindings and functions for the NeoMutt Pager Menu.
keywords: neomutt, functions, pager, menu, bindings, keys, reading
---

# Pager Menu Functions

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

| Function | Default Key | Description |
|----------|-------------|-------------|
| `<bottom>` | <End> | jump to the bottom of the message |
| `<bounce-message>` | b | remail a message to another user |
| `<break-thread>` | # | break the thread in two |
| `<change-folder>` | c | open a different folder |
| `<change-folder-readonly>` | Esc c | open a different folder in read only mode |
| `<change-newsgroup>` |  | open a different newsgroup |
| `<change-newsgroup-readonly>` |  | open a different newsgroup in read only mode |
| `<change-vfolder>` |  | open a different virtual folder |
| `<check-stats>` |  | calculate message statistics for all mailboxes |
| `<check-traditional-pgp>` | Esc P | check for classic PGP |
| `<clear-flag>` | W | clear a status flag from a message |
| `<compose-to-sender>` |  | compose new message to the current message sender |
| `<copy-message>` | C | copy a message to a file/mailbox |
| `<create-alias>` | a | create an alias from a message sender |
| `<decode-copy>` | Esc C | make decoded (text/plain) copy |
| `<decode-save>` | Esc s | make decoded copy (text/plain) and delete |
| `<decrypt-copy>` |  | make decrypted copy |
| `<decrypt-save>` |  | make decrypted copy and delete |
| `<delete-message>` | d | delete the current entry |
| `<delete-subthread>` | Esc d | delete all messages in subthread |
| `<delete-thread>` | ^D | delete all messages in thread |
| `<display-address>` | @ | display full address of sender |
| `<display-toggle-weed>` | h | display message and toggle header weeding |
| `<edit>` |  | edit the raw message (edit and edit-raw-message are synonyms) |
| `<edit-label>` | Y | add, change, or delete a message's label |
| `<edit-or-view-raw-message>` | e | edit the raw message if the mailbox is not read-only, otherwise view it |
| `<edit-raw-message>` |  | edit the raw message (edit and edit-raw-message are synonyms) |
| `<edit-type>` | ^E | edit attachment content type |
| `<enter-command>` | : | enter a neomuttrc command |
| `<entire-thread>` |  | read entire thread of the current message |
| `<exit>` | q | exit this menu |
| `<exit>` | x | exit this menu |
| `<extract-keys>` | ^K | extract supported public keys |
| `<flag-message>` | F | toggle a message's 'important' flag |
| `<followup-message>` |  | followup to newsgroup |
| `<forget-passphrase>` | ^F | wipe passphrases from memory |
| `<forward-message>` | f | forward a message with comments |
| `<forward-to-group>` |  | forward to newsgroup |
| `<group-chat-reply>` |  | reply to all recipients preserving To/Cc |
| `<group-reply>` | g | reply to all recipients |
| `<half-down>` |  | scroll down 1/2 page |
| `<half-up>` |  | scroll up 1/2 page |
| `<help>` | ? | this screen |
| `<imap-fetch-mail>` |  | force retrieval of mail from IMAP server |
| `<imap-logout-all>` |  | logout from all IMAP servers |
| `<jump>` |  | jump to an index number |
| `<link-threads>` | & | link tagged message to the current one |
| `<list-reply>` | L | reply to specified mailing list |
| `<list-subscribe>` |  | subscribe to a mailing list |
| `<list-unsubscribe>` |  | unsubscribe from a mailing list |
| `<mail>` | m | compose a new mail message |
| `<mail-key>` | Esc k | mail a PGP public key |
| `<mailbox-list>` | . | list mailboxes with new mail |
| `<mark-as-new>` | N | toggle a message's 'new' flag |
| `<modify-labels>` |  | modify (notmuch/imap) tags |
| `<modify-labels-then-hide>` |  | modify (notmuch/imap) tags and then hide message |
| `<modify-tags>` |  | modify (notmuch/imap) tags |
| `<modify-tags-then-hide>` |  | modify (notmuch/imap) tags and then hide message |
| `<next-entry>` | J | move to the next entry |
| `<next-line>` | <Enter> | scroll down one line |
| `<next-line>` | <Keypadenter> | scroll down one line |
| `<next-line>` | <Return> | scroll down one line |
| `<next-new>` |  | jump to the next new message |
| `<next-new-then-unread>` | <Tab> | jump to the next new or unread message |
| `<next-page>` | <Pagedown> | move to the next page |
| `<next-page>` | <Space> | move to the next page |
| `<next-subthread>` | Esc n | jump to the next subthread |
| `<next-thread>` | ^N | jump to the next thread |
| `<next-undeleted>` | <Down> | move to the next undeleted message |
| `<next-undeleted>` | <Right> | move to the next undeleted message |
| `<next-undeleted>` | j | move to the next undeleted message |
| `<next-unread>` |  | jump to the next unread message |
| `<next-unread-mailbox>` |  | open next mailbox with new mail |
| `<parent-message>` | P | jump to parent message in thread |
| `<pipe-entry>` | \| | pipe message/attachment to a shell command |
| `<pipe-message>` | \| | pipe message/attachment to a shell command |
| `<post-message>` |  | post message to newsgroup |
| `<previous-entry>` | K | move to the previous entry |
| `<previous-line>` | <Backspace> | scroll up one line |
| `<previous-new>` |  | jump to the previous new message |
| `<previous-new-then-unread>` |  | jump to the previous new or unread message |
| `<previous-page>` | <Pageup> | move to the previous page |
| `<previous-page>` | - | move to the previous page |
| `<previous-subthread>` | Esc p | jump to previous subthread |
| `<previous-thread>` | ^P | jump to previous thread |
| `<previous-undeleted>` | <Left> | move to the previous undeleted message |
| `<previous-undeleted>` | <Up> | move to the previous undeleted message |
| `<previous-undeleted>` | k | move to the previous undeleted message |
| `<previous-unread>` |  | jump to the previous unread message |
| `<print-entry>` |  | print the current entry |
| `<print-message>` | p | print the current entry |
| `<purge-message>` |  | delete the current entry, bypassing the trash folder |
| `<purge-thread>` |  | delete the current thread, bypassing the trash folder |
| `<quasi-delete>` |  | delete from NeoMutt, don't touch on disk |
| `<quit>` | Q | save changes to mailbox and quit |
| `<read-subthread>` | Esc r | mark the current subthread as read |
| `<read-thread>` | ^R | mark the current thread as read |
| `<recall-message>` | R | recall a postponed message |
| `<reconstruct-thread>` |  | reconstruct thread containing current message |
| `<redraw-screen>` | ^L | clear and redraw the screen |
| `<reply>` | r | reply to a message |
| `<resend-message>` | Esc e | use the current message as a template for a new one |
| `<root-message>` |  | jump to root message in thread |
| `<save-entry>` |  | save message/attachment to a mailbox/file |
| `<save-message>` | s | save message/attachment to a mailbox/file |
| `<search>` | / | search for a regular expression |
| `<search-next>` | n | search for next match |
| `<search-opposite>` |  | search for next match in opposite direction |
| `<search-reverse>` | Esc / | search backwards for a regular expression |
| `<search-toggle>` | \\ | toggle search pattern coloring |
| `<set-flag>` | w | set a status flag on a message |
| `<shell-escape>` | ! | invoke a command in a subshell |
| `<show-log-messages>` |  | show log (and debug) messages |
| `<show-version>` | V | show the NeoMutt version number and date |
| `<skip-headers>` | H | jump to first line after headers |
| `<skip-quoted>` | S | skip beyond quoted text |
| `<sort-mailbox>` | o | sort messages |
| `<sort-reverse>` | O | sort messages in reverse order |
| `<sync-mailbox>` | $ | save changes to mailbox |
| `<tag-message>` | t | tag the current entry |
| `<toggle-quoted>` | T | toggle display of quoted text |
| `<toggle-write>` | % | toggle whether the mailbox will be rewritten |
| `<top>` | <Home> | jump to the top of the message |
| `<top>` | ^ | jump to the top of the message |
| `<undelete-message>` | u | undelete the current entry |
| `<undelete-subthread>` | Esc u | undelete all messages in subthread |
| `<undelete-thread>` | ^U | undelete all messages in thread |
| `<vfolder-from-query>` |  | generate virtual folder from query |
| `<vfolder-from-query-readonly>` |  | generate a read-only virtual folder from query |
| `<view-attachments>` | v | show MIME attachments |
| `<view-raw-message>` |  | show the raw message |
| `<what-key>` |  | display the keycode for a key press |
