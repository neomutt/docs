---
title: Functions
description: Complete listing of NeoMutt functions organised by menu, with default key bindings
keywords: functions, key bindings, menus, actions, shortcuts
---

# Functions

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

Functions are named actions that NeoMutt can perform. Each function belongs to
one or more menus and may have a default key binding. Bindings can be changed
with the [`bind`](commands) command.

The tables below list every function grouped by menu. Where a function has
multiple default bindings, each binding appears as a separate row.

## Generic Menu {#generic-map}

The *generic* menu is not a real menu. It defines common functions (such as
movement) available in all menus except *pager* and *editor*. Changing bindings
here affects the defaults for all other menus (except as noted).

**Detail page:** [functions/generic](functions/generic)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<bottom-page>` | `L` | move to the bottom of the page |
| `<check-stats>` | | calculate message statistics for all mailboxes |
| `<current-bottom>` | | move entry to bottom of screen |
| `<current-middle>` | | move entry to middle of screen |
| `<current-top>` | | move entry to top of screen |
| `<end-cond>` | | end of conditional execution (noop) |
| `<enter-command>` | `:` | enter a neomuttrc command |
| `<exit>` | | exit this menu |
| `<first-entry>` | `<Home>` | move to the first entry |
| `<first-entry>` | `=` | move to the first entry |
| `<half-down>` | `]` | scroll down 1/2 page |
| `<half-up>` | `[` | scroll up 1/2 page |
| `<help>` | `?` | this screen |
| `<jump>` | | jump to an index number |
| `<last-entry>` | `<End>` | move to the last entry |
| `<last-entry>` | `*` | move to the last entry |
| `<middle-page>` | `M` | move to the middle of the page |
| `<next-entry>` | `<Down>` | move to the next entry |
| `<next-entry>` | `j` | move to the next entry |
| `<next-line>` | `>` | scroll down one line |
| `<next-page>` | `<Pagedown>` | move to the next page |
| `<next-page>` | `<Right>` | move to the next page |
| `<next-page>` | `z` | move to the next page |
| `<previous-entry>` | `<Up>` | move to the previous entry |
| `<previous-entry>` | `k` | move to the previous entry |
| `<previous-line>` | `<` | scroll up one line |
| `<previous-page>` | `<Left>` | move to the previous page |
| `<previous-page>` | `<Pageup>` | move to the previous page |
| `<previous-page>` | `Z` | move to the previous page |
| `<redraw-screen>` | `^L` | clear and redraw the screen |
| `<search>` | `/` | search for a regular expression |
| `<search-next>` | `n` | search for next match |
| `<search-opposite>` | | search for next match in opposite direction |
| `<search-reverse>` | `Esc /` | search backwards for a regular expression |
| `<select-entry>` | `<Enter>` | select the current entry |
| `<select-entry>` | `<Keypadenter>` | select the current entry |
| `<select-entry>` | `<Return>` | select the current entry |
| `<shell-escape>` | `!` | invoke a command in a subshell |
| `<show-log-messages>` | | show log (and debug) messages |
| `<show-version>` | `V` | show the NeoMutt version number and date |
| `<tag-entry>` | `t` | tag the current entry |
| `<tag-prefix>` | `;` | apply next function to tagged messages |
| `<tag-prefix-cond>` | | apply next function ONLY to tagged messages |
| `<top-page>` | `H` | move to the top of the page |
| `<what-key>` | | display the keycode for a key press |

## Index Menu {#index-map}

**Detail page:** [functions/index-menu](functions/index-menu)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<alias-dialog>` | | open the aliases dialog |
| `<autocrypt-acct-menu>` | `A` | manage autocrypt accounts |
| `<bounce-message>` | `b` | remail a message to another user |
| `<break-thread>` | `#` | break the thread in two |
| `<catchup>` | | mark all articles in newsgroup as read |
| `<change-folder>` | `c` | open a different folder |
| `<change-folder-readonly>` | `Esc c` | open a different folder in read only mode |
| `<change-newsgroup>` | `i` | open a different newsgroup |
| `<change-newsgroup-readonly>` | `Esc i` | open a different newsgroup in read only mode |
| `<change-vfolder>` | | open a different virtual folder |
| `<check-traditional-pgp>` | `Esc P` | check for classic PGP |
| `<clear-flag>` | `W` | clear a status flag from a message |
| `<collapse-all>` | `Esc V` | collapse/uncollapse all threads |
| `<collapse-thread>` | `Esc v` | collapse/uncollapse current thread |
| `<compose-to-sender>` | | compose new message to the current message sender |
| `<copy-message>` | `C` | copy a message to a file/mailbox |
| `<create-alias>` | `a` | create an alias from a message sender |
| `<decode-copy>` | `Esc C` | make decoded (text/plain) copy |
| `<decode-save>` | `Esc s` | make decoded copy (text/plain) and delete |
| `<decrypt-copy>` | | make decrypted copy |
| `<decrypt-save>` | | make decrypted copy and delete |
| `<delete-message>` | `d` | delete the current entry |
| `<delete-pattern>` | `D` | delete non-hidden messages matching a pattern |
| `<delete-subthread>` | `Esc d` | delete all messages in subthread |
| `<delete-thread>` | `^D` | delete all messages in thread |
| `<display-address>` | `@` | display full address of sender |
| `<display-message>` | `<Enter>` | display a message |
| `<display-message>` | `<Keypadenter>` | display a message |
| `<display-message>` | `<Return>` | display a message |
| `<display-message>` | `<Space>` | display a message |
| `<display-toggle-weed>` | `h` | display message and toggle header weeding |
| `<edit>` | | edit the raw message (edit and edit-raw-message are synonyms) |
| `<edit-label>` | `Y` | add, change, or delete a message's label |
| `<edit-or-view-raw-message>` | `e` | edit the raw message if the mailbox is not read-only, otherwise view it |
| `<edit-raw-message>` | | edit the raw message (edit and edit-raw-message are synonyms) |
| `<edit-type>` | `^E` | edit attachment content type |
| `<entire-thread>` | | read entire thread of the current message |
| `<exit>` | `x` | exit this menu |
| `<extract-keys>` | `^K` | extract supported public keys |
| `<fetch-mail>` | `G` | retrieve mail from POP server |
| `<flag-message>` | `F` | toggle a message's 'important' flag |
| `<followup-message>` | | followup to newsgroup |
| `<forget-passphrase>` | `^F` | wipe passphrases from memory |
| `<forward-message>` | `f` | forward a message with comments |
| `<forward-to-group>` | | forward to newsgroup |
| `<get-children>` | | get all children of the current message |
| `<get-message>` | | get message with Message-Id |
| `<get-parent>` | | get parent of the current message |
| `<group-chat-reply>` | | reply to all recipients preserving To/Cc |
| `<group-reply>` | `g` | reply to all recipients |
| `<imap-fetch-mail>` | | force retrieval of mail from IMAP server |
| `<imap-logout-all>` | | logout from all IMAP servers |
| `<limit>` | `l` | show only messages matching a pattern |
| `<limit-current-thread>` | | limit view to current thread |
| `<link-threads>` | `&` | link tagged message to the current one |
| `<list-reply>` | `L` | reply to specified mailing list |
| `<list-subscribe>` | | subscribe to a mailing list |
| `<list-unsubscribe>` | | unsubscribe from a mailing list |
| `<mail>` | `m` | compose a new mail message |
| `<mail-key>` | `Esc k` | mail a PGP public key |
| `<mailbox-list>` | `.` | list mailboxes with new mail |
| `<mark-message>` | `~` | create a hotkey macro for the current message |
| `<modify-labels>` | | modify (notmuch/imap) tags |
| `<modify-labels-then-hide>` | | modify (notmuch/imap) tags and then hide message |
| `<modify-tags>` | | modify (notmuch/imap) tags |
| `<modify-tags-then-hide>` | | modify (notmuch/imap) tags and then hide message |
| `<next-entry>` | `J` | move to the next entry |
| `<next-new>` | | jump to the next new message |
| `<next-new-then-unread>` | `<Tab>` | jump to the next new or unread message |
| `<next-subthread>` | `Esc n` | jump to the next subthread |
| `<next-thread>` | `^N` | jump to the next thread |
| `<next-undeleted>` | `<Down>` | move to the next undeleted message |
| `<next-undeleted>` | `j` | move to the next undeleted message |
| `<next-unread>` | | jump to the next unread message |
| `<next-unread-mailbox>` | | open next mailbox with new mail |
| `<parent-message>` | `P` | jump to parent message in thread |
| `<pipe-entry>` | `\|` | pipe message/attachment to a shell command |
| `<pipe-message>` | `\|` | pipe message/attachment to a shell command |
| `<post-message>` | | post message to newsgroup |
| `<previous-entry>` | `K` | move to the previous entry |
| `<previous-new>` | | jump to the previous new message |
| `<previous-new-then-unread>` | `Esc <Tab>` | jump to the previous new or unread message |
| `<previous-subthread>` | `Esc p` | jump to previous subthread |
| `<previous-thread>` | `^P` | jump to previous thread |
| `<previous-undeleted>` | `<Up>` | move to the previous undeleted message |
| `<previous-undeleted>` | `k` | move to the previous undeleted message |
| `<previous-unread>` | | jump to the previous unread message |
| `<print-message>` | `p` | print the current entry |
| `<purge-message>` | | delete the current entry, bypassing the trash folder |
| `<purge-thread>` | | delete the current thread, bypassing the trash folder |
| `<quasi-delete>` | | delete from NeoMutt, don't touch on disk |
| `<query>` | `Q` | query external program for addresses |
| `<quit>` | `q` | save changes to mailbox and quit |
| `<read-subthread>` | `Esc r` | mark the current subthread as read |
| `<read-thread>` | `^R` | mark the current thread as read |
| `<recall-message>` | `R` | recall a postponed message |
| `<reconstruct-thread>` | | reconstruct thread containing current message |
| `<reply>` | `r` | reply to a message |
| `<resend-message>` | `Esc e` | use the current message as a template for a new one |
| `<root-message>` | | jump to root message in thread |
| `<save-message>` | `s` | save message/attachment to a mailbox/file |
| `<set-flag>` | `w` | set a status flag on a message |
| `<show-limit>` | `Esc l` | show currently active limit pattern |
| `<show-log-messages>` | `M` | show log (and debug) messages |
| `<sort-mailbox>` | `o` | sort messages |
| `<sort-reverse>` | `O` | sort messages in reverse order |
| `<sync-mailbox>` | `$` | save changes to mailbox |
| `<tag-pattern>` | `T` | tag non-hidden messages matching a pattern |
| `<tag-subthread>` | | tag the current subthread |
| `<tag-thread>` | `Esc t` | tag the current thread |
| `<toggle-new>` | `N` | toggle a message's 'new' flag |
| `<toggle-read>` | | toggle view of read messages |
| `<toggle-write>` | `%` | toggle whether the mailbox will be rewritten |
| `<undelete-message>` | `u` | undelete the current entry |
| `<undelete-pattern>` | `U` | undelete non-hidden messages matching a pattern |
| `<undelete-subthread>` | `Esc u` | undelete all messages in subthread |
| `<undelete-thread>` | `^U` | undelete all messages in thread |
| `<untag-pattern>` | `^T` | untag non-hidden messages matching a pattern |
| `<vfolder-from-query>` | | generate virtual folder from query |
| `<vfolder-from-query-readonly>` | | generate a read-only virtual folder from query |
| `<vfolder-window-backward>` | | shifts virtual folder time window backwards |
| `<vfolder-window-forward>` | | shifts virtual folder time window forwards |
| `<vfolder-window-reset>` | | resets virtual folder time window to the present |
| `<view-attachments>` | `v` | show MIME attachments |
| `<view-raw-message>` | | show the raw message |

## Pager Menu {#pager-map}

**Detail page:** [functions/pager](functions/pager)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<bottom>` | `<End>` | jump to the bottom of the message |
| `<bounce-message>` | `b` | remail a message to another user |
| `<break-thread>` | `#` | break the thread in two |
| `<change-folder>` | `c` | open a different folder |
| `<change-folder-readonly>` | `Esc c` | open a different folder in read only mode |
| `<change-newsgroup>` | | open a different newsgroup |
| `<change-newsgroup-readonly>` | | open a different newsgroup in read only mode |
| `<change-vfolder>` | | open a different virtual folder |
| `<check-stats>` | | calculate message statistics for all mailboxes |
| `<check-traditional-pgp>` | `Esc P` | check for classic PGP |
| `<clear-flag>` | `W` | clear a status flag from a message |
| `<compose-to-sender>` | | compose new message to the current message sender |
| `<copy-message>` | `C` | copy a message to a file/mailbox |
| `<create-alias>` | `a` | create an alias from a message sender |
| `<decode-copy>` | `Esc C` | make decoded (text/plain) copy |
| `<decode-save>` | `Esc s` | make decoded copy (text/plain) and delete |
| `<decrypt-copy>` | | make decrypted copy |
| `<decrypt-save>` | | make decrypted copy and delete |
| `<delete-message>` | `d` | delete the current entry |
| `<delete-subthread>` | `Esc d` | delete all messages in subthread |
| `<delete-thread>` | `^D` | delete all messages in thread |
| `<display-address>` | `@` | display full address of sender |
| `<display-toggle-weed>` | `h` | display message and toggle header weeding |
| `<edit>` | | edit the raw message (edit and edit-raw-message are synonyms) |
| `<edit-label>` | `Y` | add, change, or delete a message's label |
| `<edit-or-view-raw-message>` | `e` | edit the raw message if the mailbox is not read-only, otherwise view it |
| `<edit-raw-message>` | | edit the raw message (edit and edit-raw-message are synonyms) |
| `<edit-type>` | `^E` | edit attachment content type |
| `<enter-command>` | `:` | enter a neomuttrc command |
| `<entire-thread>` | | read entire thread of the current message |
| `<exit>` | `q` | exit this menu |
| `<exit>` | `x` | exit this menu |
| `<extract-keys>` | `^K` | extract supported public keys |
| `<flag-message>` | `F` | toggle a message's 'important' flag |
| `<followup-message>` | | followup to newsgroup |
| `<forget-passphrase>` | `^F` | wipe passphrases from memory |
| `<forward-message>` | `f` | forward a message with comments |
| `<forward-to-group>` | | forward to newsgroup |
| `<group-chat-reply>` | | reply to all recipients preserving To/Cc |
| `<group-reply>` | `g` | reply to all recipients |
| `<half-down>` | | scroll down 1/2 page |
| `<half-up>` | | scroll up 1/2 page |
| `<help>` | `?` | this screen |
| `<imap-fetch-mail>` | | force retrieval of mail from IMAP server |
| `<imap-logout-all>` | | logout from all IMAP servers |
| `<jump>` | | jump to an index number |
| `<link-threads>` | `&` | link tagged message to the current one |
| `<list-reply>` | `L` | reply to specified mailing list |
| `<list-subscribe>` | | subscribe to a mailing list |
| `<list-unsubscribe>` | | unsubscribe from a mailing list |
| `<mail>` | `m` | compose a new mail message |
| `<mail-key>` | `Esc k` | mail a PGP public key |
| `<mailbox-list>` | `.` | list mailboxes with new mail |
| `<mark-as-new>` | `N` | toggle a message's 'new' flag |
| `<modify-labels>` | | modify (notmuch/imap) tags |
| `<modify-labels-then-hide>` | | modify (notmuch/imap) tags and then hide message |
| `<modify-tags>` | | modify (notmuch/imap) tags |
| `<modify-tags-then-hide>` | | modify (notmuch/imap) tags and then hide message |
| `<next-entry>` | `J` | move to the next entry |
| `<next-line>` | `<Enter>` | scroll down one line |
| `<next-line>` | `<Keypadenter>` | scroll down one line |
| `<next-line>` | `<Return>` | scroll down one line |
| `<next-new>` | | jump to the next new message |
| `<next-new-then-unread>` | `<Tab>` | jump to the next new or unread message |
| `<next-page>` | `<Pagedown>` | move to the next page |
| `<next-page>` | `<Space>` | move to the next page |
| `<next-subthread>` | `Esc n` | jump to the next subthread |
| `<next-thread>` | `^N` | jump to the next thread |
| `<next-undeleted>` | `<Down>` | move to the next undeleted message |
| `<next-undeleted>` | `<Right>` | move to the next undeleted message |
| `<next-undeleted>` | `j` | move to the next undeleted message |
| `<next-unread>` | | jump to the next unread message |
| `<next-unread-mailbox>` | | open next mailbox with new mail |
| `<parent-message>` | `P` | jump to parent message in thread |
| `<pipe-entry>` | `\|` | pipe message/attachment to a shell command |
| `<pipe-message>` | `\|` | pipe message/attachment to a shell command |
| `<post-message>` | | post message to newsgroup |
| `<previous-entry>` | `K` | move to the previous entry |
| `<previous-line>` | `<Backspace>` | scroll up one line |
| `<previous-new>` | | jump to the previous new message |
| `<previous-new-then-unread>` | | jump to the previous new or unread message |
| `<previous-page>` | `<Pageup>` | move to the previous page |
| `<previous-page>` | `-` | move to the previous page |
| `<previous-subthread>` | `Esc p` | jump to previous subthread |
| `<previous-thread>` | `^P` | jump to previous thread |
| `<previous-undeleted>` | `<Left>` | move to the previous undeleted message |
| `<previous-undeleted>` | `<Up>` | move to the previous undeleted message |
| `<previous-undeleted>` | `k` | move to the previous undeleted message |
| `<previous-unread>` | | jump to the previous unread message |
| `<print-entry>` | | print the current entry |
| `<print-message>` | `p` | print the current entry |
| `<purge-message>` | | delete the current entry, bypassing the trash folder |
| `<purge-thread>` | | delete the current thread, bypassing the trash folder |
| `<quasi-delete>` | | delete from NeoMutt, don't touch on disk |
| `<quit>` | `Q` | save changes to mailbox and quit |
| `<read-subthread>` | `Esc r` | mark the current subthread as read |
| `<read-thread>` | `^R` | mark the current thread as read |
| `<recall-message>` | `R` | recall a postponed message |
| `<reconstruct-thread>` | | reconstruct thread containing current message |
| `<redraw-screen>` | `^L` | clear and redraw the screen |
| `<reply>` | `r` | reply to a message |
| `<resend-message>` | `Esc e` | use the current message as a template for a new one |
| `<root-message>` | | jump to root message in thread |
| `<save-entry>` | | save message/attachment to a mailbox/file |
| `<save-message>` | `s` | save message/attachment to a mailbox/file |
| `<search>` | `/` | search for a regular expression |
| `<search-next>` | `n` | search for next match |
| `<search-opposite>` | | search for next match in opposite direction |
| `<search-reverse>` | `Esc /` | search backwards for a regular expression |
| `<search-toggle>` | `\\` | toggle search pattern coloring |
| `<set-flag>` | `w` | set a status flag on a message |
| `<shell-escape>` | `!` | invoke a command in a subshell |
| `<show-log-messages>` | | show log (and debug) messages |
| `<show-version>` | `V` | show the NeoMutt version number and date |
| `<skip-headers>` | `H` | jump to first line after headers |
| `<skip-quoted>` | `S` | skip beyond quoted text |
| `<sort-mailbox>` | `o` | sort messages |
| `<sort-reverse>` | `O` | sort messages in reverse order |
| `<sync-mailbox>` | `$` | save changes to mailbox |
| `<tag-message>` | `t` | tag the current entry |
| `<toggle-quoted>` | `T` | toggle display of quoted text |
| `<toggle-write>` | `%` | toggle whether the mailbox will be rewritten |
| `<top>` | `<Home>` | jump to the top of the message |
| `<top>` | `^` | jump to the top of the message |
| `<undelete-message>` | `u` | undelete the current entry |
| `<undelete-subthread>` | `Esc u` | undelete all messages in subthread |
| `<undelete-thread>` | `^U` | undelete all messages in thread |
| `<vfolder-from-query>` | | generate virtual folder from query |
| `<vfolder-from-query-readonly>` | | generate a read-only virtual folder from query |
| `<view-attachments>` | `v` | show MIME attachments |
| `<view-raw-message>` | | show the raw message |
| `<what-key>` | | display the keycode for a key press |

## Alias Menu {#alias-map}

**Detail page:** [functions/alias](functions/alias)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<delete-entry>` | `d` | delete the current entry |
| `<exit>` | `q` | exit this menu |
| `<limit>` | `l` | show only messages matching a pattern |
| `<mail>` | `m` | compose a new mail message |
| `<sort-alias>` | `o` | sort messages |
| `<sort-alias-reverse>` | `O` | sort messages in reverse order |
| `<tag-entry>` | `<Space>` | tag the current entry |
| `<tag-pattern>` | `T` | tag non-hidden messages matching a pattern |
| `<undelete-entry>` | `u` | undelete the current entry |
| `<untag-pattern>` | `^T` | untag non-hidden messages matching a pattern |

## Query Menu {#query-map}

**Detail page:** [functions/query](functions/query)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<create-alias>` | `a` | create an alias from a message sender |
| `<exit>` | `q` | exit this menu |
| `<limit>` | `l` | show only messages matching a pattern |
| `<mail>` | `m` | compose a new mail message |
| `<query>` | `Q` | query external program for addresses |
| `<query-append>` | `A` | append new query results to current results |
| `<sort>` | `o` | sort messages |
| `<sort-reverse>` | `O` | sort messages in reverse order |
| `<tag-entry>` | `<Space>` | tag the current entry |
| `<tag-pattern>` | `T` | tag non-hidden messages matching a pattern |
| `<untag-pattern>` | `^T` | untag non-hidden messages matching a pattern |

## Attachment Menu {#attachment-map}

**Detail page:** [functions/attachment](functions/attachment)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<bounce-message>` | `b` | remail a message to another user |
| `<check-traditional-pgp>` | `Esc P` | check for classic PGP |
| `<collapse-parts>` | `v` | toggle display of subparts |
| `<compose-to-sender>` | | compose new message to the current message sender |
| `<delete-entry>` | `d` | delete the current entry |
| `<display-toggle-weed>` | `h` | display message and toggle header weeding |
| `<edit-type>` | `^E` | edit attachment content type |
| `<exit>` | `q` | exit this menu |
| `<extract-keys>` | `^K` | extract supported public keys |
| `<followup-message>` | | followup to newsgroup |
| `<forget-passphrase>` | `^F` | wipe passphrases from memory |
| `<forward-message>` | `f` | forward a message with comments |
| `<forward-to-group>` | | forward to newsgroup |
| `<group-chat-reply>` | | reply to all recipients preserving To/Cc |
| `<group-reply>` | `g` | reply to all recipients |
| `<list-reply>` | `L` | reply to specified mailing list |
| `<list-subscribe>` | | subscribe to a mailing list |
| `<list-unsubscribe>` | | unsubscribe from a mailing list |
| `<pipe-entry>` | `\|` | pipe message/attachment to a shell command |
| `<pipe-message>` | `\|` | pipe message/attachment to a shell command |
| `<print-entry>` | `p` | print the current entry |
| `<reply>` | `r` | reply to a message |
| `<resend-message>` | `Esc e` | use the current message as a template for a new one |
| `<save-entry>` | `s` | save message/attachment to a mailbox/file |
| `<undelete-entry>` | `u` | undelete the current entry |
| `<view-attach>` | `<Enter>` | view attachment using mailcap entry if necessary |
| `<view-attach>` | `<Keypadenter>` | view attachment using mailcap entry if necessary |
| `<view-attach>` | `<Return>` | view attachment using mailcap entry if necessary |
| `<view-mailcap>` | `m` | force viewing of attachment using mailcap |
| `<view-pager>` | | view attachment in pager using copiousoutput mailcap |
| `<view-text>` | `T` | view attachment as text |

## Compose Menu {#compose-map}

**Detail page:** [functions/compose](functions/compose)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<attach-file>` | `a` | attach files to this message |
| `<attach-key>` | `Esc k` | attach a PGP public key |
| `<attach-message>` | `A` | attach messages to this message |
| `<attach-news-message>` | | attach news articles to this message |
| `<autocrypt-menu>` | `o` | show autocrypt compose menu options |
| `<copy-file>` | `C` | save message/attachment to a mailbox/file |
| `<detach-file>` | `D` | delete the current entry |
| `<display-toggle-weed>` | `h` | display message and toggle header weeding |
| `<edit-bcc>` | `b` | edit the BCC list |
| `<edit-cc>` | `c` | edit the CC list |
| `<edit-content-id>` | `Esc i` | edit the 'Content-ID' of the attachment |
| `<edit-description>` | `d` | edit attachment description |
| `<edit-encoding>` | `^E` | edit attachment transfer-encoding |
| `<edit-fcc>` | `f` | enter a file to save a copy of this message in |
| `<edit-file>` | `Esc e` | edit the file to be attached |
| `<edit-followup-to>` | | edit the Followup-To field |
| `<edit-from>` | `Esc f` | edit the from field |
| `<edit-headers>` | `E` | edit the message with headers |
| `<edit-language>` | `^L` | edit the 'Content-Language' of the attachment |
| `<edit-message>` | `e` | edit the message |
| `<edit-mime>` | `m` | edit attachment using mailcap entry |
| `<edit-newsgroups>` | | edit the newsgroups list |
| `<edit-reply-to>` | `r` | edit the Reply-To field |
| `<edit-subject>` | `s` | edit the subject of this message |
| `<edit-to>` | `t` | edit the TO list |
| `<edit-type>` | `^T` | edit attachment content type |
| `<edit-x-comment-to>` | | edit the X-Comment-To field |
| `<exit>` | `q` | exit this menu |
| `<filter-entry>` | `F` | filter attachment through a shell command |
| `<forget-passphrase>` | `^F` | wipe passphrases from memory |
| `<get-attachment>` | `G` | get a temporary copy of an attachment |
| `<group-alternatives>` | `&` | group tagged attachments as 'multipart/alternative' |
| `<group-multilingual>` | `^` | group tagged attachments as 'multipart/multilingual' |
| `<group-related>` | `%` | group tagged attachments as 'multipart/related' |
| `<ispell>` | `i` | run ispell on the message |
| `<move-down>` | `+` | move an attachment down in the attachment list |
| `<move-up>` | `-` | move an attachment up in the attachment list |
| `<new-mime>` | `n` | compose new attachment using mailcap entry |
| `<pgp-menu>` | `p` | show PGP options |
| `<pipe-entry>` | `\|` | pipe message/attachment to a shell command |
| `<pipe-message>` | `\|` | pipe message/attachment to a shell command |
| `<postpone-message>` | `P` | save this message to send later |
| `<preview-page-down>` | `<Pagedown>` | show the next page of the message |
| `<preview-page-up>` | `<Pageup>` | show the previous page of the message |
| `<print-entry>` | `l` | print the current entry |
| `<rename-attachment>` | `^O` | send attachment with a different name |
| `<rename-file>` | `R` | rename/move an attached file |
| `<send-message>` | `y` | send the message |
| `<smime-menu>` | `S` | show S/MIME options |
| `<tag-entry>` | `T` | tag the current entry |
| `<toggle-disposition>` | `^D` | toggle disposition between inline/attachment |
| `<toggle-recode>` | | toggle recoding of this attachment |
| `<toggle-unlink>` | `u` | toggle whether to delete file after sending it |
| `<ungroup-attachment>` | `#` | ungroup 'multipart' attachment |
| `<update-encoding>` | `U` | update an attachment's encoding info |
| `<view-attach>` | `<Enter>` | view attachment using mailcap entry if necessary |
| `<view-attach>` | `<Keypadenter>` | view attachment using mailcap entry if necessary |
| `<view-attach>` | `<Return>` | view attachment using mailcap entry if necessary |
| `<view-mailcap>` | | force viewing of attachment using mailcap |
| `<view-pager>` | | view attachment in pager using copiousoutput mailcap |
| `<view-text>` | | view attachment as text |
| `<write-fcc>` | `w` | write the message to a folder |

## Postpone Menu {#postpone-map}

**Detail page:** [functions/postpone](functions/postpone)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<delete-entry>` | `d` | delete the current entry |
| `<exit>` | `q` | exit this menu |
| `<undelete-entry>` | `u` | undelete the current entry |

## Browser Menu {#browser-map}

**Detail page:** [functions/browser](functions/browser)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<catchup>` | | mark all articles in newsgroup as read |
| `<change-dir>` | `c` | change directories |
| `<check-new>` | | check mailboxes for new mail |
| `<create-mailbox>` | `C` | create a new mailbox (IMAP only) |
| `<delete-mailbox>` | `d` | delete the current mailbox (IMAP only) |
| `<descend-directory>` | | descend into a directory |
| `<display-filename>` | `@` | display the currently selected file's name |
| `<enter-mask>` | `m` | enter a file mask |
| `<exit>` | `q` | exit this menu |
| `<goto-folder>` | `=` | swap the current folder position with $folder if it exists |
| `<goto-parent>` | `p` | go to parent directory |
| `<mailbox-list>` | `.` | list mailboxes with new mail |
| `<reload-active>` | | load list of all newsgroups from NNTP server |
| `<rename-mailbox>` | `r` | rename the current mailbox (IMAP only) |
| `<select-new>` | `N` | select a new file in this directory |
| `<sort>` | `o` | sort messages |
| `<sort-reverse>` | `O` | sort messages in reverse order |
| `<subscribe>` | `s` | subscribe to current mbox (IMAP/NNTP only) |
| `<subscribe-pattern>` | | subscribe to newsgroups matching a pattern |
| `<toggle-mailboxes>` | `<Tab>` | toggle whether to browse mailboxes or all files |
| `<toggle-subscribed>` | `T` | toggle view all/subscribed mailboxes (IMAP only) |
| `<uncatchup>` | | mark all articles in newsgroup as unread |
| `<unsubscribe>` | `u` | unsubscribe from current mbox (IMAP/NNTP only) |
| `<unsubscribe-pattern>` | | unsubscribe from newsgroups matching a pattern |
| `<view-file>` | `<Space>` | view file |

## PGP Menu {#pgp-map}

**Detail page:** [functions/pgp](functions/pgp)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<exit>` | `q` | exit this menu |
| `<verify-key>` | `c` | verify a public key |
| `<view-name>` | `%` | view the key's user id |

## S/MIME Menu {#smime-map}

**Detail page:** [functions/smime](functions/smime)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<exit>` | `q` | exit this menu |
| `<verify-key>` | `c` | verify a public key |
| `<view-name>` | `%` | view the key's user id |

## Editor Menu {#editor-map}

**Detail page:** [functions/editor](functions/editor)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<backspace>` | `<Backspace>` | delete the char in front of the cursor |
| `<backspace>` | `<Delete>` | delete the char in front of the cursor |
| `<backward-char>` | `<Left>` | move the cursor one character to the left |
| `<backward-char>` | `^B` | move the cursor one character to the left |
| `<backward-word>` | `Esc b` | move the cursor to the beginning of the word |
| `<bol>` | `<Home>` | jump to the beginning of the line |
| `<bol>` | `^A` | jump to the beginning of the line |
| `<capitalize-word>` | `Esc c` | capitalize the word |
| `<complete>` | `<Tab>` | complete filename or alias |
| `<complete-query>` | `^T` | complete address with query |
| `<delete-char>` | `<Delete>` | delete the char under the cursor |
| `<delete-char>` | `^D` | delete the char under the cursor |
| `<downcase-word>` | `Esc l` | convert the word to lower case |
| `<eol>` | `<End>` | jump to the end of the line |
| `<eol>` | `^E` | jump to the end of the line |
| `<forward-char>` | `<Right>` | move the cursor one character to the right |
| `<forward-char>` | `^F` | move the cursor one character to the right |
| `<forward-word>` | `Esc f` | move the cursor to the end of the word |
| `<help>` | `Esc ?` | this screen |
| `<history-down>` | `<Down>` | scroll down through the history list |
| `<history-down>` | `^N` | scroll down through the history list |
| `<history-search>` | `^R` | search through the history list |
| `<history-up>` | `<Up>` | scroll up through the history list |
| `<history-up>` | `^P` | scroll up through the history list |
| `<kill-eol>` | `^K` | delete chars from cursor to end of line |
| `<kill-eow>` | `Esc d` | delete chars from the cursor to the end of the word |
| `<kill-line>` | `^U` | delete chars from cursor to beginning the line |
| `<kill-whole-line>` | | delete all chars on the line |
| `<kill-word>` | `^W` | delete the word in front of the cursor |
| `<mailbox-cycle>` | `<Space>` | cycle among incoming mailboxes |
| `<quote-char>` | `^V` | quote the next typed key |
| `<redraw-screen>` | `^L` | clear and redraw the screen |
| `<transpose-chars>` | | transpose character under cursor with previous |
| `<upcase-word>` | `Esc u` | convert the word to upper case |

## Sidebar Menu {#sidebar-map}

**Detail page:** [functions/sidebar](functions/sidebar)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<sidebar-abort-search>` | | close the sidebar search |
| `<sidebar-first>` | | move the highlight to the first mailbox |
| `<sidebar-last>` | | move the highlight to the last mailbox |
| `<sidebar-next>` | | move the highlight to next mailbox |
| `<sidebar-next-new>` | | move the highlight to next mailbox with new mail |
| `<sidebar-open>` | | open highlighted mailbox |
| `<sidebar-page-down>` | | scroll the sidebar down 1 page |
| `<sidebar-page-up>` | | scroll the sidebar up 1 page |
| `<sidebar-prev>` | | move the highlight to previous mailbox |
| `<sidebar-prev-new>` | | move the highlight to previous mailbox with new mail |
| `<sidebar-start-search>` | | fuzzy search the sidebar |
| `<sidebar-toggle-virtual>` | | toggle between mailboxes and virtual mailboxes |
| `<sidebar-toggle-visible>` | | make the sidebar (in)visible |

## Autocrypt Menu {#autocrypt-account-map}

**Detail page:** [functions/autocrypt](functions/autocrypt)

| Function | Default key | Description |
|----------|-------------|-------------|
| `<create-account>` | `c` | create a new autocrypt account |
| `<delete-account>` | `D` | delete the current account |
| `<exit>` | `q` | exit this menu |
| `<toggle-active>` | `a` | toggle the current account active/inactive |
| `<toggle-prefer-encrypt>` | `p` | toggle the current account prefer-encrypt flag |
