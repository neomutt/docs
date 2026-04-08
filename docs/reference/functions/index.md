---
title: Functions
description: Overview of all NeoMutt functions grouped by menu, with default key bindings and descriptions
keywords: neomutt, functions, overview, menus, bindings, keys, bind command, reference, alias, attach, compose, pager, index, sidebar, editor, generic
---

(ref-functions)=
# Functions

Functions are named actions that NeoMutt can perform.
Each function belongs to one or more menus and may have a default key binding.
Bindings can be changed with [`:bind`](cmd-bind).

(fn-alias-dialog)=
(fn-attach-file)=
(fn-attach-key)=
(fn-attach-message)=
(fn-attach-news-message)=
(fn-autocrypt-acct-menu)=
(fn-autocrypt-menu)=
## A

| Function                | Used By               |
|-------------------------|-----------------------|
| `<alias-dialog>`        | [Index](fn-index)     |
| `<attach-file>`         | [Compose](fn-compose) |
| `<attach-key>`          | [Compose](fn-compose) |
| `<attach-message>`      | [Compose](fn-compose) |
| `<attach-news-message>` | [Compose](fn-compose) |
| `<autocrypt-acct-menu>` | [Index](fn-index)     |
| `<autocrypt-menu>`      | [Compose](fn-compose) |

(fn-backspace)=
(fn-backward-char)=
(fn-backward-word)=
(fn-bol)=
(fn-bottom-page)=
(fn-bottom)=
(fn-bounce-message)=
(fn-break-thread)=
## B

| Function           | Used By                                                               |
|--------------------|-----------------------------------------------------------------------|
| `<backspace>`      | [Editor](fn-editor)                                                   |
| `<backward-char>`  | [Editor](fn-editor)                                                   |
| `<backward-word>`  | [Editor](fn-editor)                                                   |
| `<bol>`            | [Editor](fn-editor)                                                   |
| `<bottom-page>`    | [Generic](fn-generic)                                                 |
| `<bottom>`         | [Pager](fn-pager)                                                     |
| `<bounce-message>` | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager)             |
| `<break-thread>`   | [Index](fn-index), [Pager](fn-pager)                                  |
| `<buffy-cycle>`    | {bdg-warning-line}`Renamed to:` [`<mailbox-cycle>`](fn-mailbox-cycle) |
| `<buffy-list>`     | {bdg-warning-line}`Renamed to:` [`<mailbox-list>`](fn-mailbox-list)   |

(fn-capitalize-word)=
(fn-catchup)=
(fn-change-dir)=
(fn-change-folder-readonly)=
(fn-change-folder)=
(fn-change-newsgroup-readonly)=
(fn-change-newsgroup)=
(fn-change-vfolder)=
(fn-check-new)=
(fn-check-stats)=
(fn-check-traditional-pgp)=
(fn-clear-flag)=
(fn-close-all-threads)=
(fn-close-thread)=
(fn-collapse-all)=
(fn-collapse-parts)=
(fn-collapse-thread)=
(fn-complete-query)=
(fn-complete)=
(fn-compose-to-sender)=
(fn-copy-file)=
(fn-copy-message)=
(fn-create-account)=
(fn-create-alias)=
(fn-create-mailbox)=
(fn-current-bottom)=
(fn-current-middle)=
(fn-current-top)=
## C

| Function                      | Used By                                                   |
|-------------------------------|-----------------------------------------------------------|
| `<capitalize-word>`           | [Editor](fn-editor)                                       |
| `<catchup>`                   | [Browser](fn-browser), [Index](fn-index)                  |
| `<change-dir>`                | [Browser](fn-browser)                                     |
| `<change-folder-readonly>`    | [Index](fn-index), [Pager](fn-pager)                      |
| `<change-folder>`             | [Index](fn-index), [Pager](fn-pager)                      |
| `<change-newsgroup-readonly>` | [Index](fn-index), [Pager](fn-pager)                      |
| `<change-newsgroup>`          | [Index](fn-index), [Pager](fn-pager)                      |
| `<change-vfolder>`            | [Index](fn-index), [Pager](fn-pager)                      |
| `<check-new>`                 | [Browser](fn-browser)                                     |
| `<check-stats>`               | [Generic](fn-generic), [Pager](fn-pager)                  |
| `<check-traditional-pgp>`     | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager) |
| `<clear-flag>`                | [Index](fn-index), [Pager](fn-pager)                      |
| `<close-all-threads>`         | [Index](fn-index)                                         |
| `<close-thread>`              | [Index](fn-index)                                         |
| `<collapse-all>`              | [Index](fn-index)                                         |
| `<collapse-parts>`            | [Attach](fn-attach)                                       |
| `<collapse-thread>`           | [Index](fn-index)                                         |
| `<complete-query>`            | [Editor](fn-editor)                                       |
| `<complete>`                  | [Editor](fn-editor)                                       |
| `<compose-to-sender>`         | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager) |
| `<copy-file>`                 | [Compose](fn-compose)                                     |
| `<copy-message>`              | [Index](fn-index), [Pager](fn-pager)                      |
| `<create-account>`            | [Autocrypt](fn-autocrypt)                                 |
| `<create-alias>`              | [Index](fn-index), [Pager](fn-pager), [Query](fn-query)   |
| `<create-mailbox>`            | [Browser](fn-browser)                                     |
| `<current-bottom>`            | [Generic](fn-generic)                                     |
| `<current-middle>`            | [Generic](fn-generic)                                     |
| `<current-top>`               | [Generic](fn-generic)                                     |

(fn-decode-copy)=
(fn-decode-save)=
(fn-decrypt-copy)=
(fn-decrypt-save)=
(fn-delete-account)=
(fn-delete-char)=
(fn-delete-entry)=
(fn-delete-mailbox)=
(fn-delete-message)=
(fn-delete-pattern)=
(fn-delete-subthread)=
(fn-delete-thread)=
(fn-descend-directory)=
(fn-detach-file)=
(fn-display-address)=
(fn-display-filename)=
(fn-display-message)=
(fn-display-toggle-weed)=
(fn-downcase-word)=
## D

| Function                | Used By                                                                          |
|-------------------------|----------------------------------------------------------------------------------|
| `<decode-copy>`         | [Index](fn-index), [Pager](fn-pager)                                             |
| `<decode-save>`         | [Index](fn-index), [Pager](fn-pager)                                             |
| `<decrypt-copy>`        | [Index](fn-index), [Pager](fn-pager)                                             |
| `<decrypt-save>`        | [Index](fn-index), [Pager](fn-pager)                                             |
| `<delete-account>`      | [Autocrypt](fn-autocrypt)                                                        |
| `<delete-char>`         | [Editor](fn-editor)                                                              |
| `<delete-entry>`        | [Alias](fn-alias), [Attach](fn-attach), [Postpone](fn-postpone)                  |
| `<delete-mailbox>`      | [Browser](fn-browser)                                                            |
| `<delete-message>`      | [Index](fn-index), [Pager](fn-pager)                                             |
| `<delete-pattern>`      | [Index](fn-index)                                                                |
| `<delete-subthread>`    | [Index](fn-index), [Pager](fn-pager)                                             |
| `<delete-thread>`       | [Index](fn-index), [Pager](fn-pager)                                             |
| `<descend-directory>`   | [Browser](fn-browser)                                                            |
| `<detach-file>`         | [Compose](fn-compose)                                                            |
| `<display-address>`     | [Index](fn-index), [Pager](fn-pager)                                             |
| `<display-filename>`    | [Browser](fn-browser)                                                            |
| `<display-message>`     | [Index](fn-index)                                                                |
| `<display-toggle-weed>` | [Attach](fn-attach), [Compose](fn-compose), [Index](fn-index), [Pager](fn-pager) |
| `<downcase-word>`       | [Editor](fn-editor)                                                              |

(fn-edit-bcc)=
(fn-edit-cc)=
(fn-edit-content-id)=
(fn-edit-description)=
(fn-edit-encoding)=
(fn-edit-fcc)=
(fn-edit-file)=
(fn-edit-followup-to)=
(fn-edit-from)=
(fn-edit-headers)=
(fn-edit-label)=
(fn-edit-language)=
(fn-edit-message)=
(fn-edit-mime)=
(fn-edit-newsgroups)=
(fn-edit-or-view-raw-message)=
(fn-edit-raw-message)=
(fn-edit-reply-to)=
(fn-edit-subject)=
(fn-edit-to)=
(fn-edit-type)=
(fn-edit-x-comment-to)=
(fn-edit)=
(fn-end-cond)=
(fn-enter-command)=
(fn-enter-mask)=
(fn-entire-thread)=
(fn-eol)=
(fn-exit)=
(fn-extract-keys)=
## E

| Function                     | Used By                                                                                                                                   |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `<edit-bcc>`                 | [Compose](fn-compose)                                                                                                                     |
| `<edit-cc>`                  | [Compose](fn-compose)                                                                                                                     |
| `<edit-content-id>`          | [Compose](fn-compose)                                                                                                                     |
| `<edit-description>`         | [Compose](fn-compose)                                                                                                                     |
| `<edit-encoding>`            | [Compose](fn-compose)                                                                                                                     |
| `<edit-fcc>`                 | [Compose](fn-compose)                                                                                                                     |
| `<edit-file>`                | [Compose](fn-compose)                                                                                                                     |
| `<edit-followup-to>`         | [Compose](fn-compose)                                                                                                                     |
| `<edit-from>`                | [Compose](fn-compose)                                                                                                                     |
| `<edit-headers>`             | [Compose](fn-compose)                                                                                                                     |
| `<edit-label>`               | [Index](fn-index), [Pager](fn-pager)                                                                                                      |
| `<edit-language>`            | [Compose](fn-compose)                                                                                                                     |
| `<edit-message>`             | [Compose](fn-compose)                                                                                                                     |
| `<edit-mime>`                | [Compose](fn-compose)                                                                                                                     |
| `<edit-newsgroups>`          | [Compose](fn-compose)                                                                                                                     |
| `<edit-or-view-raw-message>` | [Index](fn-index), [Pager](fn-pager)                                                                                                      |
| `<edit-raw-message>`         | [Index](fn-index), [Pager](fn-pager)                                                                                                      |
| `<edit-reply-to>`            | [Compose](fn-compose)                                                                                                                     |
| `<edit-subject>`             | [Compose](fn-compose)                                                                                                                     |
| `<edit-to>`                  | [Compose](fn-compose)                                                                                                                     |
| `<edit-type>`                | [Attach](fn-attach), [Compose](fn-compose), [Index](fn-index), [Pager](fn-pager)                                                          |
| `<edit-x-comment-to>`        | [Compose](fn-compose)                                                                                                                     |
| `<edit>`                     | [Index](fn-index), [Pager](fn-pager)                                                                                                      |
| `<end-cond>`                 | [Generic](fn-generic)                                                                                                                     |
| `<enter-command>`            | [Generic](fn-generic), [Pager](fn-pager)                                                                                                  |
| `<enter-mask>`               | [Browser](fn-browser)                                                                                                                     |
| `<entire-thread>`            | [Index](fn-index), [Pager](fn-pager)                                                                                                      |
| `<eol>`                      | [Editor](fn-editor)                                                                                                                       |
| `<error-history>`            | {bdg-warning-line}`Renamed to:` [`<show-log-messages>`](fn-show-log-messages)                                                             |
| `<exit>`                     | [Alias](fn-alias), [Attach](fn-attach), [Autocrypt](fn-autocrypt), [Browser](fn-browser), [Compose](fn-compose), [Dialog](fn-dialog),     |
|                              | [Generic](fn-generic), [Index](fn-index), [Pager](fn-pager), [Pgp](fn-pgp), [Postpone](fn-postpone), [Query](fn-query), [Smime](fn-smime) |
| `<extract-keys>`             | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager)                                                                                 |

(fn-fetch-mail)=
(fn-filter-entry)=
(fn-first-entry)=
(fn-flag-message)=
(fn-followup-message)=
(fn-forget-passphrase)=
(fn-forward-char)=
(fn-forward-message)=
(fn-forward-to-group)=
(fn-forward-word)=
## F

| Function              | Used By                                                                          |
|-----------------------|----------------------------------------------------------------------------------|
| `<fetch-mail>`        | [Index](fn-index)                                                                |
| `<filter-entry>`      | [Compose](fn-compose)                                                            |
| `<first-entry>`       | [Generic](fn-generic)                                                            |
| `<flag-message>`      | [Index](fn-index), [Pager](fn-pager)                                             |
| `<followup-message>`  | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager)                        |
| `<forget-passphrase>` | [Attach](fn-attach), [Compose](fn-compose), [Index](fn-index), [Pager](fn-pager) |
| `<forward-char>`      | [Editor](fn-editor)                                                              |
| `<forward-message>`   | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager)                        |
| `<forward-to-group>`  | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager)                        |
| `<forward-word>`      | [Editor](fn-editor)                                                              |

(fn-get-attachment)=
(fn-get-children)=
(fn-get-message)=
(fn-get-parent)=
(fn-goto-folder)=
(fn-goto-parent)=
(fn-group-alternatives)=
(fn-group-chat-reply)=
(fn-group-multilingual)=
(fn-group-related)=
(fn-group-reply)=
## G

| Function               | Used By                                                   |
|------------------------|-----------------------------------------------------------|
| `<get-attachment>`     | [Compose](fn-compose)                                     |
| `<get-children>`       | [Index](fn-index)                                         |
| `<get-message>`        | [Index](fn-index)                                         |
| `<get-parent>`         | [Index](fn-index)                                         |
| `<goto-folder>`        | [Browser](fn-browser)                                     |
| `<goto-parent>`        | [Browser](fn-browser)                                     |
| `<group-alternatives>` | [Compose](fn-compose)                                     |
| `<group-chat-reply>`   | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager) |
| `<group-multilingual>` | [Compose](fn-compose)                                     |
| `<group-related>`      | [Compose](fn-compose)                                     |
| `<group-reply>`        | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager) |

(fn-half-down)=
(fn-half-up)=
(fn-help)=
(fn-history-down)=
(fn-history-search)=
(fn-history-up)=
## H

| Function           | Used By                                                       |
|--------------------|---------------------------------------------------------------|
| `<half-down>`      | [Generic](fn-generic), [Pager](fn-pager)                      |
| `<half-up>`        | [Generic](fn-generic), [Pager](fn-pager)                      |
| `<help>`           | [Editor](fn-editor), [Generic](fn-generic), [Pager](fn-pager) |
| `<history-down>`   | [Editor](fn-editor)                                           |
| `<history-search>` | [Editor](fn-editor)                                           |
| `<history-up>`     | [Editor](fn-editor)                                           |

(fn-imap-fetch-mail)=
(fn-imap-logout-all)=
(fn-ispell)=
## I

| Function            | Used By                              |
|---------------------|--------------------------------------|
| `<imap-fetch-mail>` | [Index](fn-index), [Pager](fn-pager) |
| `<imap-logout-all>` | [Index](fn-index), [Pager](fn-pager) |
| `<ispell>`          | [Compose](fn-compose)                |

(fn-jump)=
## J

| Function | Used By                                  |
|----------|------------------------------------------|
| `<jump>` | [Generic](fn-generic), [Pager](fn-pager) |

(fn-kill-eol)=
(fn-kill-eow)=
(fn-kill-line)=
(fn-kill-whole-line)=
(fn-kill-word)=
## K

| Function            | Used By             |
|---------------------|---------------------|
| `<kill-eol>`        | [Editor](fn-editor) |
| `<kill-eow>`        | [Editor](fn-editor) |
| `<kill-line>`       | [Editor](fn-editor) |
| `<kill-whole-line>` | [Editor](fn-editor) |
| `<kill-word>`       | [Editor](fn-editor) |

(fn-last-entry)=
(fn-limit-current-thread)=
(fn-limit)=
(fn-link-threads)=
(fn-list-reply)=
(fn-list-subscribe)=
(fn-list-unsubscribe)=
## L

| Function                 | Used By                                                   |
|--------------------------|-----------------------------------------------------------|
| `<last-entry>`           | [Generic](fn-generic)                                     |
| `<limit-current-thread>` | [Index](fn-index)                                         |
| `<limit>`                | [Alias](fn-alias), [Index](fn-index), [Query](fn-query)   |
| `<link-threads>`         | [Index](fn-index), [Pager](fn-pager)                      |
| `<list-reply>`           | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager) |
| `<list-subscribe>`       | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager) |
| `<list-unsubscribe>`     | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager) |

(fn-mail-key)=
(fn-mail)=
(fn-mailbox-cycle)=
(fn-mailbox-list)=
(fn-mark-as-new)=
(fn-mark-message)=
(fn-middle-page)=
(fn-modify-labels-then-hide)=
(fn-modify-labels)=
(fn-modify-tags-then-hide)=
(fn-modify-tags)=
(fn-move-down)=
(fn-move-up)=
## M

| Function                    | Used By                                                                    |
|-----------------------------|----------------------------------------------------------------------------|
| `<mail-key>`                | [Index](fn-index), [Pager](fn-pager)                                       |
| `<mail>`                    | [Alias](fn-alias), [Index](fn-index), [Pager](fn-pager), [Query](fn-query) |
| `<mailbox-cycle>`           | [Editor](fn-editor)                                                        |
| `<mailbox-list>`            | [Browser](fn-browser), [Index](fn-index), [Pager](fn-pager)                |
| `<mark-as-new>`             | [Pager](fn-pager)                                                          |
| `<mark-message>`            | [Index](fn-index)                                                          |
| `<middle-page>`             | [Generic](fn-generic)                                                      |
| `<modify-labels-then-hide>` | [Index](fn-index), [Pager](fn-pager)                                       |
| `<modify-labels>`           | [Index](fn-index), [Pager](fn-pager)                                       |
| `<modify-tags-then-hide>`   | [Index](fn-index), [Pager](fn-pager)                                       |
| `<modify-tags>`             | [Index](fn-index), [Pager](fn-pager)                                       |
| `<move-down>`               | [Compose](fn-compose)                                                      |
| `<move-up>`                 | [Compose](fn-compose)                                                      |

(fn-new-mime)=
(fn-next-entry)=
(fn-next-line)=
(fn-next-new-then-unread)=
(fn-next-new)=
(fn-next-page)=
(fn-next-subthread)=
(fn-next-thread)=
(fn-next-undeleted)=
(fn-next-unread-mailbox)=
(fn-next-unread)=
## N

| Function                 | Used By                                  |
|--------------------------|------------------------------------------|
| `<new-mime>`             | [Compose](fn-compose)                    |
| `<next-entry>`           | [Generic](fn-generic), [Pager](fn-pager) |
| `<next-line>`            | [Generic](fn-generic), [Pager](fn-pager) |
| `<next-new-then-unread>` | [Index](fn-index), [Pager](fn-pager)     |
| `<next-new>`             | [Index](fn-index), [Pager](fn-pager)     |
| `<next-page>`            | [Generic](fn-generic), [Pager](fn-pager) |
| `<next-subthread>`       | [Index](fn-index), [Pager](fn-pager)     |
| `<next-thread>`          | [Index](fn-index), [Pager](fn-pager)     |
| `<next-undeleted>`       | [Index](fn-index), [Pager](fn-pager)     |
| `<next-unread-mailbox>`  | [Index](fn-index), [Pager](fn-pager)     |
| `<next-unread>`          | [Index](fn-index), [Pager](fn-pager)     |

(fn-open-all-threads)=
(fn-open-thread)=
## O

| Function             | Used By           |
|----------------------|-------------------|
| `<open-all-threads>` | [Index](fn-index) |
| `<open-thread>`      | [Index](fn-index) |

(fn-parent-message)=
(fn-pgp-menu)=
(fn-pipe-entry)=
(fn-pipe-message)=
(fn-post-message)=
(fn-postpone-message)=
(fn-preview-page-down)=
(fn-preview-page-up)=
(fn-previous-entry)=
(fn-previous-line)=
(fn-previous-new-then-unread)=
(fn-previous-new)=
(fn-previous-page)=
(fn-previous-subthread)=
(fn-previous-thread)=
(fn-previous-undeleted)=
(fn-previous-unread)=
(fn-print-entry)=
(fn-print-message)=
(fn-purge-message)=
(fn-purge-thread)=
## P

| Function                     | Used By                                                                          |
|------------------------------|----------------------------------------------------------------------------------|
| `<parent-message>`           | [Index](fn-index), [Pager](fn-pager)                                             |
| `<pgp-menu>`                 | [Compose](fn-compose)                                                            |
| `<pipe-entry>`               | [Attach](fn-attach), [Compose](fn-compose), [Index](fn-index), [Pager](fn-pager) |
| `<pipe-message>`             | [Attach](fn-attach), [Compose](fn-compose), [Index](fn-index), [Pager](fn-pager) |
| `<post-message>`             | [Index](fn-index), [Pager](fn-pager)                                             |
| `<postpone-message>`         | [Compose](fn-compose)                                                            |
| `<preview-page-down>`        | [Compose](fn-compose)                                                            |
| `<preview-page-up>`          | [Compose](fn-compose)                                                            |
| `<previous-entry>`           | [Generic](fn-generic), [Pager](fn-pager)                                         |
| `<previous-line>`            | [Generic](fn-generic), [Pager](fn-pager)                                         |
| `<previous-new-then-unread>` | [Index](fn-index), [Pager](fn-pager)                                             |
| `<previous-new>`             | [Index](fn-index), [Pager](fn-pager)                                             |
| `<previous-page>`            | [Generic](fn-generic), [Pager](fn-pager)                                         |
| `<previous-subthread>`       | [Index](fn-index), [Pager](fn-pager)                                             |
| `<previous-thread>`          | [Index](fn-index), [Pager](fn-pager)                                             |
| `<previous-undeleted>`       | [Index](fn-index), [Pager](fn-pager)                                             |
| `<previous-unread>`          | [Index](fn-index), [Pager](fn-pager)                                             |
| `<print-entry>`              | [Attach](fn-attach), [Compose](fn-compose), [Pager](fn-pager)                    |
| `<print-message>`            | [Index](fn-index), [Pager](fn-pager)                                             |
| `<purge-message>`            | [Index](fn-index), [Pager](fn-pager)                                             |
| `<purge-thread>`             | [Index](fn-index), [Pager](fn-pager)                                             |

(fn-quasi-delete)=
(fn-query-append)=
(fn-query)=
(fn-quit)=
(fn-quote-char)=
## Q

| Function         | Used By                                                   |
|------------------|-----------------------------------------------------------|
| `<quasi-delete>` | [Index](fn-index), [Pager](fn-pager)                      |
| `<query-append>` | [Query](fn-query)                                         |
| `<query>`        | [Index](fn-index), [Query](fn-query)                      |
| `<quit>`         | [Dialog](fn-dialog), [Index](fn-index), [Pager](fn-pager) |
| `<quote-char>`   | [Editor](fn-editor)                                       |

(fn-read-subthread)=
(fn-read-thread)=
(fn-recall-message)=
(fn-reconstruct-thread)=
(fn-redraw-screen)=
(fn-reload-active)=
(fn-rename-attachment)=
(fn-rename-file)=
(fn-rename-mailbox)=
(fn-reply)=
(fn-resend-message)=
(fn-root-message)=
## R

| Function               | Used By                                                               |
|------------------------|-----------------------------------------------------------------------|
| `<read-subthread>`     | [Index](fn-index), [Pager](fn-pager)                                  |
| `<read-thread>`        | [Index](fn-index), [Pager](fn-pager)                                  |
| `<recall-message>`     | [Index](fn-index), [Pager](fn-pager)                                  |
| `<reconstruct-thread>` | [Index](fn-index), [Pager](fn-pager)                                  |
| `<redraw-screen>`      | [Editor](fn-editor), [Generic](fn-generic), [Pager](fn-pager)         |
| `<refresh>`            | {bdg-warning-line}`Renamed to:` [`<redraw-screen>`](fn-redraw-screen) |
| `<reload-active>`      | [Browser](fn-browser)                                                 |
| `<rename-attachment>`  | [Compose](fn-compose)                                                 |
| `<rename-file>`        | [Compose](fn-compose)                                                 |
| `<rename-mailbox>`     | [Browser](fn-browser)                                                 |
| `<reply>`              | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager)             |
| `<resend-message>`     | [Attach](fn-attach), [Index](fn-index), [Pager](fn-pager)             |
| `<root-message>`       | [Index](fn-index), [Pager](fn-pager)                                  |

(fn-save-entry)=
(fn-save-message)=
(fn-search-next)=
(fn-search-opposite)=
(fn-search-reverse)=
(fn-search-toggle)=
(fn-search)=
(fn-select-entry)=
(fn-select-new)=
(fn-send-message)=
(fn-set-flag)=
(fn-shell-escape)=
(fn-show-limit)=
(fn-show-log-messages)=
(fn-show-version)=
(fn-sidebar-abort-search)=
(fn-sidebar-first)=
(fn-sidebar-last)=
(fn-sidebar-next-new)=
(fn-sidebar-next)=
(fn-sidebar-open)=
(fn-sidebar-page-down)=
(fn-sidebar-page-up)=
(fn-sidebar-prev-new)=
(fn-sidebar-prev)=
(fn-sidebar-start-search)=
(fn-sidebar-toggle-virtual)=
(fn-sidebar-toggle-visible)=
(fn-skip-headers)=
(fn-skip-quoted)=
(fn-smime-menu)=
(fn-sort-alias-reverse)=
(fn-sort-alias)=
(fn-sort-mailbox)=
(fn-sort-reverse)=
(fn-sort)=
(fn-subscribe-pattern)=
(fn-subscribe)=
(fn-sync-mailbox)=
## S

| Function                   | Used By                                                                        |
|----------------------------|--------------------------------------------------------------------------------|
| `<save-entry>`             | [Attach](fn-attach), [Pager](fn-pager)                                         |
| `<save-message>`           | [Index](fn-index), [Pager](fn-pager)                                           |
| `<search-next>`            | [Generic](fn-generic), [Pager](fn-pager)                                       |
| `<search-opposite>`        | [Generic](fn-generic), [Pager](fn-pager)                                       |
| `<search-reverse>`         | [Generic](fn-generic), [Pager](fn-pager)                                       |
| `<search-toggle>`          | [Pager](fn-pager)                                                              |
| `<search>`                 | [Generic](fn-generic), [Pager](fn-pager)                                       |
| `<select-entry>`           | [Generic](fn-generic)                                                          |
| `<select-new>`             | [Browser](fn-browser)                                                          |
| `<send-message>`           | [Compose](fn-compose)                                                          |
| `<set-flag>`               | [Index](fn-index), [Pager](fn-pager)                                           |
| `<shell-escape>`           | [Generic](fn-generic), [Pager](fn-pager)                                       |
| `<show-limit>`             | [Index](fn-index)                                                              |
| `<show-log-messages>`      | [Generic](fn-generic), [Pager](fn-pager)                                       |
| `<show-version>`           | [Generic](fn-generic), [Pager](fn-pager)                                       |
| `<sidebar-abort-search>`   | [Sidebar](fn-sidebar)                                                          |
| `<sidebar-first>`          | [Sidebar](fn-sidebar)                                                          |
| `<sidebar-last>`           | [Sidebar](fn-sidebar)                                                          |
| `<sidebar-next-new>`       | [Sidebar](fn-sidebar)                                                          |
| `<sidebar-next>`           | [Sidebar](fn-sidebar)                                                          |
| `<sidebar-open>`           | [Sidebar](fn-sidebar)                                                          |
| `<sidebar-page-down>`      | [Sidebar](fn-sidebar)                                                          |
| `<sidebar-page-up>`        | [Sidebar](fn-sidebar)                                                          |
| `<sidebar-prev-new>`       | [Sidebar](fn-sidebar)                                                          |
| `<sidebar-prev>`           | [Sidebar](fn-sidebar)                                                          |
| `<sidebar-start-search>`   | [Sidebar](fn-sidebar)                                                          |
| `<sidebar-toggle-virtual>` | [Sidebar](fn-sidebar)                                                          |
| `<sidebar-toggle-visible>` | [Sidebar](fn-sidebar)                                                          |
| `<skip-headers>`           | [Pager](fn-pager)                                                              |
| `<skip-quoted>`            | [Pager](fn-pager)                                                              |
| `<smime-menu>`             | [Compose](fn-compose)                                                          |
| `<sort-alias-reverse>`     | [Alias](fn-alias)                                                              |
| `<sort-alias>`             | [Alias](fn-alias)                                                              |
| `<sort-mailbox>`           | [Index](fn-index), [Pager](fn-pager)                                           |
| `<sort-reverse>`           | [Browser](fn-browser), [Index](fn-index), [Pager](fn-pager), [Query](fn-query) |
| `<sort>`                   | [Browser](fn-browser), [Query](fn-query)                                       |
| `<subscribe-pattern>`      | [Browser](fn-browser)                                                          |
| `<subscribe>`              | [Browser](fn-browser)                                                          |
| `<sync-mailbox>`           | [Index](fn-index), [Pager](fn-pager)                                           |

(fn-tag-entry)=
(fn-tag-message)=
(fn-tag-pattern)=
(fn-tag-prefix-cond)=
(fn-tag-prefix)=
(fn-tag-subthread)=
(fn-tag-thread)=
(fn-toggle-active)=
(fn-toggle-disposition)=
(fn-toggle-mailboxes)=
(fn-toggle-new)=
(fn-toggle-prefer-encrypt)=
(fn-toggle-quoted)=
(fn-toggle-read)=
(fn-toggle-recode)=
(fn-toggle-subscribed)=
(fn-toggle-unlink)=
(fn-toggle-write)=
(fn-top-page)=
(fn-top)=
(fn-transpose-chars)=
## T

| Function                  | Used By                                                 |
|---------------------------|---------------------------------------------------------|
| `<tag-entry>`             | [Generic](fn-generic)                                   |
| `<tag-message>`           | [Pager](fn-pager)                                       |
| `<tag-pattern>`           | [Alias](fn-alias), [Index](fn-index), [Query](fn-query) |
| `<tag-prefix-cond>`       | [Generic](fn-generic)                                   |
| `<tag-prefix>`            | [Generic](fn-generic)                                   |
| `<tag-subthread>`         | [Index](fn-index)                                       |
| `<tag-thread>`            | [Index](fn-index)                                       |
| `<toggle-active>`         | [Autocrypt](fn-autocrypt)                               |
| `<toggle-disposition>`    | [Compose](fn-compose)                                   |
| `<toggle-mailboxes>`      | [Browser](fn-browser)                                   |
| `<toggle-new>`            | [Index](fn-index)                                       |
| `<toggle-prefer-encrypt>` | [Autocrypt](fn-autocrypt)                               |
| `<toggle-quoted>`         | [Pager](fn-pager)                                       |
| `<toggle-read>`           | [Index](fn-index)                                       |
| `<toggle-recode>`         | [Compose](fn-compose)                                   |
| `<toggle-subscribed>`     | [Browser](fn-browser)                                   |
| `<toggle-unlink>`         | [Compose](fn-compose)                                   |
| `<toggle-write>`          | [Index](fn-index), [Pager](fn-pager)                    |
| `<top-page>`              | [Generic](fn-generic)                                   |
| `<top>`                   | [Pager](fn-pager)                                       |
| `<transpose-chars>`       | [Editor](fn-editor)                                     |

(fn-uncatchup)=
(fn-undelete-entry)=
(fn-undelete-message)=
(fn-undelete-pattern)=
(fn-undelete-subthread)=
(fn-undelete-thread)=
(fn-ungroup-attachment)=
(fn-unsubscribe-pattern)=
(fn-unsubscribe)=
(fn-untag-pattern)=
(fn-upcase-word)=
(fn-update-encoding)=
## U

| Function                | Used By                                                         |
|-------------------------|-----------------------------------------------------------------|
| `<uncatchup>`           | [Browser](fn-browser)                                           |
| `<undelete-entry>`      | [Alias](fn-alias), [Attach](fn-attach), [Postpone](fn-postpone) |
| `<undelete-message>`    | [Index](fn-index), [Pager](fn-pager)                            |
| `<undelete-pattern>`    | [Index](fn-index)                                               |
| `<undelete-subthread>`  | [Index](fn-index), [Pager](fn-pager)                            |
| `<undelete-thread>`     | [Index](fn-index), [Pager](fn-pager)                            |
| `<ungroup-attachment>`  | [Compose](fn-compose)                                           |
| `<unsubscribe-pattern>` | [Browser](fn-browser)                                           |
| `<unsubscribe>`         | [Browser](fn-browser)                                           |
| `<untag-pattern>`       | [Alias](fn-alias), [Index](fn-index), [Query](fn-query)         |
| `<upcase-word>`         | [Editor](fn-editor)                                             |
| `<update-encoding>`     | [Compose](fn-compose)                                           |

(fn-verify-key)=
(fn-vfolder-from-query-readonly)=
(fn-vfolder-from-query)=
(fn-vfolder-window-backward)=
(fn-vfolder-window-forward)=
(fn-vfolder-window-reset)=
(fn-view-attach)=
(fn-view-attachments)=
(fn-view-file)=
(fn-view-mailcap)=
(fn-view-name)=
(fn-view-pager)=
(fn-view-raw-message)=
(fn-view-text)=
## V

| Function                        | Used By                                    |
|---------------------------------|--------------------------------------------|
| `<verify-key>`                  | [Pgp](fn-pgp), [Smime](fn-smime)           |
| `<vfolder-from-query-readonly>` | [Index](fn-index), [Pager](fn-pager)       |
| `<vfolder-from-query>`          | [Index](fn-index), [Pager](fn-pager)       |
| `<vfolder-window-backward>`     | [Index](fn-index)                          |
| `<vfolder-window-forward>`      | [Index](fn-index)                          |
| `<vfolder-window-reset>`        | [Index](fn-index)                          |
| `<view-attach>`                 | [Attach](fn-attach), [Compose](fn-compose) |
| `<view-attachments>`            | [Index](fn-index), [Pager](fn-pager)       |
| `<view-file>`                   | [Browser](fn-browser)                      |
| `<view-mailcap>`                | [Attach](fn-attach), [Compose](fn-compose) |
| `<view-name>`                   | [Pgp](fn-pgp), [Smime](fn-smime)           |
| `<view-pager>`                  | [Attach](fn-attach), [Compose](fn-compose) |
| `<view-raw-message>`            | [Index](fn-index), [Pager](fn-pager)       |
| `<view-text>`                   | [Attach](fn-attach), [Compose](fn-compose) |

(fn-what-key)=
(fn-write-fcc)=
## W

| Function      | Used By                                  |
|---------------|------------------------------------------|
| `<what-key>`  | [Generic](fn-generic), [Pager](fn-pager) |
| `<write-fcc>` | [Compose](fn-compose)                    |

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
index2
pager
pgp
postpone
query
sidebar
smime
```

