---
title: Index Menu Functions
description: Default key bindings and functions for the NeoMutt Index Menu.
keywords: neomutt, functions, index, menu, bindings, keys, mail
---

# Index Menu Functions

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

| Function | Default Key | Description |
|----------|-------------|-------------|
| `<alias-dialog>` |  | open the aliases dialog |
| `<autocrypt-acct-menu>` | A | manage autocrypt accounts |
| `<bounce-message>` | b | remail a message to another user |
| `<break-thread>` | # | break the thread in two |
| `<catchup>` |  | mark all articles in newsgroup as read |
| `<change-folder>` | c | open a different folder |
| `<change-folder-readonly>` | Esc c | open a different folder in read only mode |
| `<change-newsgroup>` | i | open a different newsgroup |
| `<change-newsgroup-readonly>` | Esc i | open a different newsgroup in read only mode |
| `<change-vfolder>` |  | open a different virtual folder |
| `<check-traditional-pgp>` | Esc P | check for classic PGP |
| `<clear-flag>` | W | clear a status flag from a message |
| `<collapse-all>` | Esc V | collapse/uncollapse all threads |
| `<collapse-thread>` | Esc v | collapse/uncollapse current thread |
| `<compose-to-sender>` |  | compose new message to the current message sender |
| `<copy-message>` | C | copy a message to a file/mailbox |
| `<create-alias>` | a | create an alias from a message sender |
| `<decode-copy>` | Esc C | make decoded (text/plain) copy |
| `<decode-save>` | Esc s | make decoded copy (text/plain) and delete |
| `<decrypt-copy>` |  | make decrypted copy |
| `<decrypt-save>` |  | make decrypted copy and delete |
| `<delete-message>` | d | delete the current entry |
| `<delete-pattern>` | D | delete non-hidden messages matching a pattern |
| `<delete-subthread>` | Esc d | delete all messages in subthread |
| `<delete-thread>` | ^D | delete all messages in thread |
| `<display-address>` | @ | display full address of sender |
| `<display-message>` | <Enter> | display a message |
| `<display-message>` | <Keypadenter> | display a message |
| `<display-message>` | <Return> | display a message |
| `<display-message>` | <Space> | display a message |
| `<display-toggle-weed>` | h | display message and toggle header weeding |
| `<edit>` |  | edit the raw message (edit and edit-raw-message are synonyms) |
| `<edit-label>` | Y | add, change, or delete a message's label |
| `<edit-or-view-raw-message>` | e | edit the raw message if the mailbox is not read-only, otherwise view it |
| `<edit-raw-message>` |  | edit the raw message (edit and edit-raw-message are synonyms) |
| `<edit-type>` | ^E | edit attachment content type |
| `<entire-thread>` |  | read entire thread of the current message |
| `<exit>` | x | exit this menu |
| `<extract-keys>` | ^K | extract supported public keys |
| `<fetch-mail>` | G | retrieve mail from POP server |
| `<flag-message>` | F | toggle a message's 'important' flag |
| `<followup-message>` |  | followup to newsgroup |
| `<forget-passphrase>` | ^F | wipe passphrases from memory |
| `<forward-message>` | f | forward a message with comments |
| `<forward-to-group>` |  | forward to newsgroup |
| `<get-children>` |  | get all children of the current message |
| `<get-message>` |  | get message with Message-Id |
| `<get-parent>` |  | get parent of the current message |
| `<group-chat-reply>` |  | reply to all recipients preserving To/Cc |
| `<group-reply>` | g | reply to all recipients |
| `<imap-fetch-mail>` |  | force retrieval of mail from IMAP server |
| `<imap-logout-all>` |  | logout from all IMAP servers |
| `<limit>` | l | show only messages matching a pattern |
| `<limit-current-thread>` |  | limit view to current thread |
| `<link-threads>` | & | link tagged message to the current one |
| `<list-reply>` | L | reply to specified mailing list |
| `<list-subscribe>` |  | subscribe to a mailing list |
| `<list-unsubscribe>` |  | unsubscribe from a mailing list |
| `<mail>` | m | compose a new mail message |
| `<mail-key>` | Esc k | mail a PGP public key |
| `<mailbox-list>` | . | list mailboxes with new mail |
| `<mark-message>` | ~ | create a hotkey macro for the current message |
| `<modify-labels>` |  | modify (notmuch/imap) tags |
| `<modify-labels-then-hide>` |  | modify (notmuch/imap) tags and then hide message |
| `<modify-tags>` |  | modify (notmuch/imap) tags |
| `<modify-tags-then-hide>` |  | modify (notmuch/imap) tags and then hide message |
| `<next-entry>` | J | move to the next entry |
| `<next-new>` |  | jump to the next new message |
| `<next-new-then-unread>` | <Tab> | jump to the next new or unread message |
| `<next-subthread>` | Esc n | jump to the next subthread |
| `<next-thread>` | ^N | jump to the next thread |
| `<next-undeleted>` | <Down> | move to the next undeleted message |
| `<next-undeleted>` | j | move to the next undeleted message |
| `<next-unread>` |  | jump to the next unread message |
| `<next-unread-mailbox>` |  | open next mailbox with new mail |
| `<parent-message>` | P | jump to parent message in thread |
| `<pipe-entry>` | \| | pipe message/attachment to a shell command |
| `<pipe-message>` | \| | pipe message/attachment to a shell command |
| `<post-message>` |  | post message to newsgroup |
| `<previous-entry>` | K | move to the previous entry |
| `<previous-new>` |  | jump to the previous new message |
| `<previous-new-then-unread>` | Esc <Tab> | jump to the previous new or unread message |
| `<previous-subthread>` | Esc p | jump to previous subthread |
| `<previous-thread>` | ^P | jump to previous thread |
| `<previous-undeleted>` | <Up> | move to the previous undeleted message |
| `<previous-undeleted>` | k | move to the previous undeleted message |
| `<previous-unread>` |  | jump to the previous unread message |
| `<print-message>` | p | print the current entry |
| `<purge-message>` |  | delete the current entry, bypassing the trash folder |
| `<purge-thread>` |  | delete the current thread, bypassing the trash folder |
| `<quasi-delete>` |  | delete from NeoMutt, don't touch on disk |
| `<query>` | Q | query external program for addresses |
| `<quit>` | q | save changes to mailbox and quit |
| `<read-subthread>` | Esc r | mark the current subthread as read |
| `<read-thread>` | ^R | mark the current thread as read |
| `<recall-message>` | R | recall a postponed message |
| `<reconstruct-thread>` |  | reconstruct thread containing current message |
| `<reply>` | r | reply to a message |
| `<resend-message>` | Esc e | use the current message as a template for a new one |
| `<root-message>` |  | jump to root message in thread |
| `<save-message>` | s | save message/attachment to a mailbox/file |
| `<set-flag>` | w | set a status flag on a message |
| `<show-limit>` | Esc l | show currently active limit pattern |
| `<show-log-messages>` | M | show log (and debug) messages |
| `<sort-mailbox>` | o | sort messages |
| `<sort-reverse>` | O | sort messages in reverse order |
| `<sync-mailbox>` | $ | save changes to mailbox |
| `<tag-pattern>` | T | tag non-hidden messages matching a pattern |
| `<tag-subthread>` |  | tag the current subthread |
| `<tag-thread>` | Esc t | tag the current thread |
| `<toggle-new>` | N | toggle a message's 'new' flag |
| `<toggle-read>` |  | toggle view of read messages |
| `<toggle-write>` | % | toggle whether the mailbox will be rewritten |
| `<undelete-message>` | u | undelete the current entry |
| `<undelete-pattern>` | U | undelete non-hidden messages matching a pattern |
| `<undelete-subthread>` | Esc u | undelete all messages in subthread |
| `<undelete-thread>` | ^U | undelete all messages in thread |
| `<untag-pattern>` | ^T | untag non-hidden messages matching a pattern |
| `<vfolder-from-query>` |  | generate virtual folder from query |
| `<vfolder-from-query-readonly>` |  | generate a read-only virtual folder from query |
| `<vfolder-window-backward>` |  | shifts virtual folder time window backwards |
| `<vfolder-window-forward>` |  | shifts virtual folder time window forwards |
| `<vfolder-window-reset>` |  | resets virtual folder time window to the present |
| `<view-attachments>` | v | show MIME attachments |
| `<view-raw-message>` |  | show the raw message |
