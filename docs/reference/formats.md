---
title: Format Strings
description: XXX
sidebar: docs/reference/index
difficulty: Advanced
diataxis: Reference
last_updated: 2025-12-01
---

# Format Strings

## alias\_format

| Short   | Long Name      | Description                                                     |
| :------ | :------------- | :-------------------------------------------------------------- |
| `%A`    | `address`      | Full Address (Name and Email)                                   |
| `%a`    | `alias`        | Alias name                                                      |
| `%C`    | `comment`      | Comment                                                         |
| `%E`    | `email`        | Email Address                                                   |
| `%f`    | `flags`        | Flags - currently, a `d` for an alias marked for deletion       |
| `%i`    | `number`       | Index number                                                    |
| `%N`    | `name`         | Real name                                                       |
| `%t`    | `tagged`       | Alias is tagged (selected)                                      |
| `%Y`    | `tags`         | User-defined tags (labels)                                      |
| `%*X`   | `padding-soft` | Soft-fill with character `X` as pad                             |
| `%>X`   | `padding-hard` | Right justify the rest of the string and pad with character `X` |
| `%\|X`  | `padding-eol`  | Pad to the end of the line with character `X`                   |
| `%c`    |                | **Deprecated:** Use `%C` instead                                  |
| `%n`    |                | **Deprecated:** Use `%i` instead                                  |
| `%r`    |                | **Deprecated:** Use `%A` instead                                  |

## attach\_format

| Short   | Long Name          | Description                                                        |
| :------ | :----------------- | :----------------------------------------------------------------- |
| `%C`    | `charset`          | Charset                                                            |
| `%c`    | `charset-convert`  | Requires charset conversion (`n` or `c`)                           |
| `%D`    | `deleted`          | Deleted flag                                                       |
| `%d`    | `description`      | Description (if none, falls back to `%F`)                            |
| `%e`    | `mime-encoding`    | MIME content-transfer-encoding                                     |
| `%F`    | `file-disposition` | Filename in content-disposition header (if none, falls back to `%f`) |
| `%f`    | `file`             | Filename                                                           |
| `%I`    | `disposition`      | Disposition (`I` for inline, `A` for attachment)                   |
| `%M`    | `mime-minor`       | MIME subtype                                                       |
| `%m`    | `mime-major`       | Major MIME type                                                    |
| `%n`    | `number`           | Attachment number                                                  |
| `%Q`    | `attach-qualifies` | `Q`, if MIME part qualifies for attachment counting                |
| `%s`    | `file-size`        | Size (see $formatstrings-size)                                     |
| `%T`    | `tree`             | Graphic tree characters                                            |
| `%t`    | `tagged`           | Tagged flag                                                        |
| `%u`    | `unlink`           | Unlink (=to delete) flag                                           |
| `%X`    | `attach-count`     | Number of qualifying MIME parts in this part and its children<br>(see the `$attachments` section for possible speed effects) |
| `%*X`   | `padding-soft`     | Soft-fill with character `X` as pad                                |
| `%>X`   | `padding-hard`     | Right justify the rest of the string and pad with character `X`    |
| `%\|X`  | `padding-eol`      | Pad to the end of the line with character `X`                      |

## autocrypt\_acct\_format

| Short   | Long Name        | Description                                                     |
| :------ | :--------------- | :-------------------------------------------------------------- |
| `%a`    | `address`        | Email address                                                   |
| `%k`    | `keyid`          | GPG keyid                                                       |
| `%n`    | `number`         | Current entry number                                            |
| `%p`    | `prefer-encrypt` | Prefer-encrypt flag                                             |
| `%s`    | `enabled`        | Status flag (active/inactive)                                   |
| `%*X`   | `padding-soft`   | Soft-fill with character `X` as pad                             |
| `%>X`   | `padding-hard`   | Right justify the rest of the string and pad with character `X` |
| `%\|X`  | `padding-eol`    | Pad to the end of the line with character `X`                   |

## compose\_format

| Short   | Long Name      | Description                                                                  | 
| :------ | :------------- | :--------------------------------------------------------------------------- |
| `%a`    | `attach-count` | Total number of attachments                                                  |
| `%h`    | `hostname`     | Local hostname                                                               |
| `%l`    | `attach-size`  | Approximate size (in bytes) of the current message (see $formatstrings-size) |
| `%v`    | `version`      | NeoMutt version string                                                       |
| `%*X`   | `padding-soft` | Soft-fill with character `X` as pad                                          |
| `%>X`   | `padding-hard` | Right justify the rest of the string and pad with character `X`              |
| `%\|X`  | `padding-eol`  | Pad to the end of the line with character `X`                                |

## folder\_format

| Short    | Long Name       | Description                                                              |
| :------- | :-------------- | :----------------------------------------------------------------------- |
| `%a`     | `notify`        | Alert: 1 if user is notified of new mail                                 |
| `%C`     | `number`        | Current file number                                                      |
| `%D`     | `date`          | Date/time folder was last modified using `$date_format`.<br>It is recommended to use `%[fmt]` instead, where `fmt` is the value of `$date_format`. |
| `%d`     | `date-format`   | Date/time folder was last modified                                       |
| `%F`     | `file-mode`     | File permissions                                                         |
| `%f`     | `filename`      | Filename (`/` is appended to directory names,<br>`@` to symbolic links and `*` to executable files) |
| `%g`     | `file-group`    | Group name (or numeric gid, if missing)                                  |
| `%i`     | `description`   | Description of the folder                                                |
| `%l`     | `hard-links`    | Number of hard links                                                     |
| `%m`     | `message-count` | Number of messages in the mailbox                                        |
| `%N`     | `new-mail`      | `N` if mailbox has new mail, ` ` (space) otherwise                       |
| `%n`     | `unread-count`  | Number of unread messages in the mailbox                                 |
| `%p`     | `poll`          | Poll: 1 if Mailbox is checked for new mail                               |
| `%s`     | `file-size`     | Size in bytes (see $formatstrings-size)                                  |
| `%t`     | `tagged`        | `\*` if the file is tagged, blank otherwise                              |
| `%u`     | `file-owner`    | Owner name (or numeric uid, if missing)                                  |
| `%[fmt]` |                 | Date/time folder was last modified using an `strftime(3)` expression     |
| `%*X`    | `padding-soft`  | Soft-fill with character `X` as pad                                      |
| `%>X`    | `padding-hard`  | Right justify the rest of the string and pad with character `X`          |
| `%\|X`   | `padding-eol`   | Pad to the end of the line with character `X`                            |

## greeting

| Short   | Long Name    | Description                    |
| :------ | :----------- | :----------------------------- |
| `%n`    | `real-name`  | Recipient's real name          |
| `%u`    | `user-name`  | User (login) name of recipient |
| `%v`    | `first-name` | First name of recipient        |

## group\_index\_format

| Short   | Long Name      | Description                                                        |
| :------ | :------------- | :----------------------------------------------------------------- |
| `%a`    | `notify`       | Alert: 1 if user is notified of new mail                           |
| `%C`    | `number`       | Current newsgroup number                                           |
| `%d`    | `description`  | Description of newsgroup (becomes from server)                     |
| `%f`    | `newsgroup`    | Newsgroup name                                                     |
| `%M`    | `flags`        | `-` if newsgroup not allowed for direct post (moderated for example) |
| `%N`    | `flags2`       | `N` if newsgroup is new, `u` if unsubscribed, ` ` (space) otherwise |
| `%n`    | `new-count`    | Number of new articles in newsgroup                                |
| `%p`    | `poll`         | Poll: 1 if Mailbox is checked for new mail                         |
| `%s`    | `unread-count` | Number of unread articles in newsgroup                             |
| `%*X`   | `padding-soft` | Soft-fill with character `X` as pad                                |
| `%>X`   | `padding-hard` | Right justify the rest of the string and pad with character `X`    |
| `%\|X`  | `padding-eol`  | Pad to the end of the line with character `X`                      |

## history\_format

| Short   | Long Name      | Description                                                     |
| :------ | :------------- | :-------------------------------------------------------------- |
| `%C`    | `number`       | Line number                                                     |
| `%s`    | `match`        | History match                                                   |
| `%*X`   | `padding-soft` | Soft-fill with character `X` as pad                             |
| `%>X`   | `padding-hard` | Right justify the rest of the string and pad with character `X` |
| `%\|X`  | `padding-eol`  | Pad to the end of the line with character `X`                   |

## index\_format

| Short     | Long Name             | Description                                                                                     |
| :-------- | :-------------------- | :---------------------------------------------------------------------------------------------- |
| `%A`      | `reply-to`            | Reply-to address (if present; otherwise: address of author)                                     |
| `%a`      | `from`                | Address of the author                                                                           |
| `%B`      | `list-address`        | Same as `%K`                                                                                      |
| `%b`      | `mailbox-name`        | Filename of the original message folder (think mailbox)                                         |
| `%C`      | `number`              | Current message number                                                                          |
| `%c`      | `body-characters`     | Number of characters (bytes) in the body of the message (see $formatstrings-size)               |
| `%cr`     | `size`                | Number of characters (bytes) in the raw message, including the header (see $formatstrings-size) |
| `%D`      | `date-format-local`   | Date and time of message using `$date_format` and local timezone.<br>It is recommended to use `%[fmt]` instead, where `fmt` is the value of `$date_format`. |
| `%d`      | `date-format`         | Date and time of message using `$date_format` and sender's timezone.<br>It is recommended to use `%{fmt}` instead, where `fmt` is the value of `$date_format`. |
| `%E`      | `thread-count`        | Number of messages in current thread                                                            |
| `%e`      | `thread-number`       | Current message number in thread                                                                |
| `%F`      | `sender`              | Author name, or recipient name if the message is from you                                       |
| `%Fp`     | `sender-plain`        | Like `%F`, but plain. No contextual formatting is applied to recipient name                       |
| `%f`      | `from-full`           | Sender (address + real name), either From: or Return-Path:                                      |
| `%Gx`     | `tags-transformed`    | Individual message tag (e.g. Notmuch tags/imap flags)                                           |
| `%g`      | `tags`                | Message tags (e.g. Notmuch tags/imap flags)                                                     |
| `%H`      | `spam`                | Spam attribute(s) of this message                                                               |
| `%I`      | `initials`            | Initials of author                                                                              |
| `%i`      | `message-id`          | Message-id of the current message                                                               |
| `%J`      | `thread-tags`         | Message tags (if present, tree unfolded, and != parent's tags)                                  |
| `%K`      | `list-empty`          | List to which the letter was sent (if any; otherwise: empty)                                |
| `%L`      | `from-list`           | If an address in the `To:` or `Cc:` header field matches an address<br>defined by the user's `$subscribe` command, this displays. |
| `%l`      | `lines`               | Number of lines in the unprocessed message (may not work with maildir, mh, and IMAP folders) |
| `%M`      | `thread-hidden-count` | Number of hidden messages if the thread is collapsed                                            |
| `%m`      | `message-count`       | Total number of message in the mailbox                                                          |
| `%N`      | `score`               | Message score                                                                                   |
| `%n`      | `name`                | Author's real name (or address if missing)                                                      |
| `%O`      | `save-folder`         | Original save folder where NeoMutt would formerly have Stashed the message:<br>list name or recipient name if not sent to a list |
| `%P`      | `percentage`          | Progress indicator for the built-in pager (how much of the file has been displayed)             |
| `%q`      | `newsgroup`           | Newsgroup name (if compiled with NNTP support)                                                  |
| `%R`      | `cc-all`              | Comma separated list of `Cc:` recipients                                                        |
| `%r`      | `to-all`              | Comma separated list of `To:` recipients                                                        |
| `%S`      | `flag-chars`          | Single character status of the message (`N`/`O`/`D`/`d`/`!`/`r`/`*`)                            |
| `%s`      | `subject`             | Subject of the message                                                                          |
| `%T`      | `to-chars`            | Appropriate character from the `$to_chars` string                                           |
| `%t`      | `to`                  | `To:` field (recipients)                                                                        |
| `%u`      | `username`            | User (login) name of the author                                                                 |
| `%v`      | `first-name`          | First name of the author, or the recipient if the message is from you                           |
| `%W`      | `organization`        | Name of organization of author (`Organization:` field)                                          |
| `%X`      | `attachment-count`    | Number of MIME attachments (see the `$attachments` section for possible speed effects)   |
| `%x`      | `x-comment-to`        | `X-Comment-To:` field (if present)                               |
| `%Y`      | `thread-x-label`      | `X-Label:` field, if present, and<br>1. not at part of a thread tree<br>2. at the top of a thread, or<br>3. `X-Label:` is different from Preceding message's `X-Label:` |
| `%y`      | `x-label`             | `X-Label:` field, if present                                                                    |
| `%Z`      | `combined-flags`      | A three character set of message status flags.<br>The first character is new/read/replied flags (`n`/`o`/`r`/`O`/`N`).<br>The second is deleted or encryption flags (`D`/`d`/`S`/`P`/`s`/`K`).<br>The third is either tagged/flagged (`*`/`!`), or one of the characters.<br>Listed in `$to_chars`. |
| `%zc`     | `crypto-flags`        | Message crypto flags                                                                            |
| `%zs`     | `status-flags`        | Message status flags                                                                            |
| `%zt`     | `message-flags`       | Message tag flags                                                                               |
| `%@name@` |                       | Insert and evaluate format-string from the matching `$index-format-hook` command                |
| `%{fmt}`  |                       | Date and time of the message is converted to sender's time zone, and `fmt` is expanded by the library function `strftime(3)`;<br>if the first character inside the braces is a bang (`!`), the date is formatted ignoring any locale settings.<br>Note that the sender's time zone might only be available as a numerical offset, so `%Z` behaves like `%z`.<br>`%{fmt}` behaves like `%[fmt]` on systems where `struct tm` doesn't have a `tm_gmtoff` member. |
| `%[fmt]`  |                       | Date and time of the message is converted to the local time zone, and `fmt` is expanded by the library function `strftime(3)`;<br>if the first character inside the brackets is a bang (`!`), the date is formatted ignoring any locale settings. |
| `%(fmt)`  |                       | Local date and time when the message was received, and `fmt` is expanded by the library function `strftime(3)`;<br>if the first character inside the parentheses is a bang (`!`), the date is formatted ignoring any locale settings. |
| `%*X`     | `padding-soft`        | Soft-fill with character `X` as pad                                                             |
| `%>X`     | `padding-hard`        | Right justify the rest of the string and pad with character `X`                                 |
| `%\|X`    | `padding-eol`         | Pad to the end of the line with character `X`                                                   |

## newsrc

| Short   | Long Name  | Description       |
| :------ | :--------- | :---------------- |
| `%a`    | `account`  | Account url       |
| `%P`    | `port-if`  | Port if specified |
| `%p`    | `port`     | Port              |
| `%S`    | `schema`   | Url schema        |
| `%s`    | `server`   | News server name  |
| `%u`    | `username` | Username          |

## pattern\_format

| Short   | Long Name      | Description                                                     | 
| :------ | :------------- | :-------------------------------------------------------------- |
| `%d`    | `description`  | Pattern description                                             |
| `%e`    | `expression`   | Pattern expression                                              |
| `%n`    | `number`       | Index number                                                    |
| `%*X`   | `padding-soft` | Soft-fill with character `X` as pad                             |
| `%>X`   | `padding-hard` | Right justify the rest of the string and pad with character `X` |
| `%\|X`  | `padding-eol`  | Pad to the end of the line with character `X`                   |

## pgp\_decode\_command

| Short   | Long Name        | Description                                                      |
| :------ | :--------------- | :--------------------------------------------------------------- |
| `%a`    | `sign-as`        | Value of `$pgp_sign_as` if set, otherwise the value of `$pgp_default_key` |
| `%f`    | `file-message`   | Expands to the name of a file containing a message               |
| `%p`    | `need-pass`      | Expands to `PGPPASSFD=0` when a pass phrase is needed, to an empty string otherwise.<br>Note: This may be used with a `%<...>` construct. |
| `%r`    | `key-ids`        | One or more key IDs (or fingerprints if available)               |
| `%s`    | `file-signature` | Expands to the name of a file containing the signature part<br>of a `multipart/signed` attachment when verifying it |

## pgp\_entry\_format

| Short    | Long Name           | Description                                                     |
| :------- | :------------------ | :-------------------------------------------------------------- |
| `%a`     | `key-algorithm`     | Algorithm                                                       |
| `%c`     | `key-capabilities`  | Capabilities                                                    |
| `%f`     | `key-flags`         | Flags                                                           |
| `%i`     | `key-fingerprint`   | Key fingerprint (or long key id if non-existent)                |
| `%k`     | `key-id`            | Key id                                                          |
| `%l`     | `key-length`        | Key length                                                      |
| `%n`     | `number`            | Number                                                          |
| `%p`     | `protocol`          | Protocol                                                        |
| `%t`     | `trust`             | Trust/validity of the key-uid association                       |
| `%u`     | `user-id`           | User id                                                         |
| `%A`     | `pkey-algorithm`    | Primary Key Algorithm                                           |
| `%C`     | `pkey-capabilities` | Primary Key Capabilities                                        |
| `%F`     | `pkey-flags`        | Primary Key Flags                                               |
| `%I`     | `pkey-fingerprint`  | Primary Key fingerprint (or long key id if non-existent)        |
| `%K`     | `pkey-id`           | Primary Key id                                                  |
| `%L`     | `pkey-length`       | Primary Key length                                              |
| `%[<s>]` | `date`              | Date of the key where `<s>` is an `strftime(3)` expression  |
| `%*X`    | `padding-soft`      | Soft-fill with character `X` as pad                             |
| `%>X`    | `padding-hard`      | Right justify the rest of the string and pad with character `X` |
| `%\|X`   | `padding-eol`       | Pad to the end of the line with character `X`                   |

## query\_format

| Short   | Long Name      | Description                                                     |
| :------ | :------------- | :-------------------------------------------------------------- |
| `%A`    | `address`      | Full Address (Name and Email)                                   |
| `%C`    | `comment`      | Comment                                                         |
| `%E`    | `email`        | Email Address                                                   |
| `%i`    | `number`       | Index number                                                    |
| `%N`    | `name`         | Real name                                                       |
| `%t`    | `tagged`       | Alias is tagged (selected)                                      |
| `%Y`    | `tags`         | User-defined tags (labels)                                      |
| `%*X`   | `padding-soft` | Soft-fill with character `X` as pad                             |
| `%>X`   | `padding-hard` | Right justify the rest of the string and pad with character `X` |
| `%\|X`  | `padding-eol`  | Pad to the end of the line with character `X`                   |
| `%a`    |                | **Deprecated:** Use `%E` instead                                  |
| `%c`    |                | **Deprecated:** Use `%i` instead                                  |
| `%e`    |                | **Deprecated:** Use `%C` instead                                  |
| `%n`    |                | **Deprecated:** Use `%N` instead                                  |

## sidebar\_format

| Short   | Long Name       | Cur  | Description                                                     |
| :------ | :-------------- | :--- | :-------------------------------------------------------------- |
| `%a`    | `notify`        |      | Alert: 1 if user is notified of new mail                        |
| `%B`    | `name`          |      | Name of the mailbox                                             |
| `%D`    | `description`   |      | Descriptive name of the mailbox                                 |
| `%d`    | `deleted-count` | Cur  | Number of deleted messages in the mailbox                       |
| `%F`    | `flagged-count` |      | Number of flagged messages in the mailbox                       |
| `%L`    | `limited-count` | Cur  | Number of messages after limiting                               |
| `%N`    | `new-mail`      |      | Number of unread messages in the mailbox (seen or unseen)       |
| `%n`    | `unread-count`  |      | `N` if mailbox has new mail, ` ` (space) otherwise              |
| `%o`    | `old-count`     |      | Number of old messages in the mailbox (unread, seen)            |
| `%p`    | `poll`          |      | Poll: 1 if Mailbox is checked for new mail                      |
| `%r`    | `read-count`    |      | Number of read messages in the mailbox (read, seen)             |
| `%S`    | `message-count` |      | Size of mailbox (total number of messages)                      |
| `%t`    | `tagged-count`  | Cur  | Number of tagged messages in the mailbox                        |
| `%Z`    | `unseen-count`  |      | Number of new messages in the mailbox (unread, unseen)          |
| `%!`    | `flagged`       |      | `!` : one flagged message<br>`!!` : two flagged messages<br>`n!` : n flagged messages (for n > 2) |
| `%*X`   | `padding-soft`  |      | Soft-fill with character `X` as pad                             |
| `%>X`   | `padding-hard`  |      | Right justify the rest of the string and pad with character `X` |
| `%\|X`  | `padding-eol`   |      | Pad to the end of the line with character `X`                   |

Cur = Only applicable to the current folder

## smime\_decrypt\_command

| Short   | Long Name          | Description                                                          |
| :------ | :----------------- | :------------------------------------------------------------------- |
| `%a`    | `algorithm`        | Algorithm used for encryption                                    |
| `%C`    | `certificate-path` | CA location:  Depending on whether `$smime_ca_location` points to a directory or file,<br>this expands to "-CApath `$smime_ca_location`" or "-CAfile `$smime_ca_location`" |
| `%c`    | `certificate-ids`  | One or more certificate IDs                                          |
| `%d`    | `digest-algorithm` | Message digest algorithm specified with `$smime_sign_digest_alg` |
| `%f`    | `message-file`     | Expands to the name of a file containing a message                   |
| `%i`    | `intermediate-ids` | Intermediate certificates                                            |
| `%k`    | `key`              | Key-pair specified with `$smime_default_key`                     |
| `%s`    | `signature-file`   | Expands to the name of a file containing the signature part<br>of a `multipart/signed` attachment when verifying it |

## status\_format

| Short   | Long Name          | Description                                                        |
| :------ | :----------------- | :----------------------------------------------------------------- |
| `%b`    | `unread-mailboxes` | Number of mailboxes with new mail                                  |
| `%D`    | `description`      | Description of the mailbox                                         |
| `%d`    | `deleted-count`    | Number of deleted messages                                         |
| `%f`    | `flagged-count`    | Full pathname of the current mailbox                           |
| `%F`    | `mailbox-path`     | Number of flagged messages                                         |
| `%h`    | `hostname`         | Local hostname                                                     |
| `%l`    | `limit-size`       | Size (in bytes) of the current mailbox (see $formatstrings-size)   |
| `%L`    | `mailbox-size`     | Size (in bytes) of the messages shown (i.e., which match the current limit) (see $formatstrings-size) |
| `%m`    | `limit-count`      | Number of messages in the mailbox                              |
| `%M`    | `message-count`    | Number of messages shown (i.e., which match the current limit) |
| `%n`    | `new-count`        | Number of new messages in the mailbox (unread, unseen)             |
| `%o`    | `old-count`        | Number of old messages in the mailbox (unread, seen)               |
| `%P`    | `percentage`       | Percentage of the way through the index                            |
| `%p`    | `postponed-count`  | Number of postponed messages                                       |
| `%r`    | `read-count`       | Modified/read-only/won't-write/attach-message indicator, According to `$status_chars` |
| `%R`    | `readonly`         | Number of read messages in the mailbox (read, seen)                |
| `%S`    | `sort-aux`         | Current aux sorting method (`$sort_aux`)                           |
| `%s`    | `sort`             | Current sorting mode (`$sort`)                                     |
| `%T`    | `use-threads`      | Current threading mode (`$use_threads`)                            |
| `%t`    | `tagged-count`     | Number of tagged messages in the mailbox                           |
| `%u`    | `unread-count`     | Number of unread messages in the mailbox (seen or unseen)          |
| `%v`    | `limit-pattern`    | NeoMutt version string                                             |
| `%V`    | `version`          | Currently active limit pattern, if any                             |
| `%*X`   | `padding-soft`     | Soft-fill with character `X` as pad                                |
| `%>X`   | `padding-hard`     | Right justify the rest of the string and pad with character `X`    |
| `%\|X`  | `padding-eol`      | Pad to the end of the line with character `X`                      |

