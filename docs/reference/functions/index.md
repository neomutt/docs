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

---

[Alias](menu-alias)
[Attach](menu-attach)
[Autocrypt](menu-autocrypt)
[Browser](menu-browser)
[Compose](menu-compose)
[Dialog](menu-dialog)
[Editor](menu-editor)
[Generic](menu-generic)
[Index](menu-index)
[Pager](menu-pager)
[Pgp](menu-pgp)
[Postpone](menu-postpone)
[Query](menu-query)
[Sidebar](menu-sidebar)
[Smime](menu-smime)

---

(fn-alias-dialog)=
(fn-attach-file)=
(fn-attach-key)=
(fn-attach-message)=
(fn-attach-news-message)=
(fn-autocrypt-acct-menu)=
(fn-autocrypt-menu)=
## A

| Function                | Used By                 |
|-------------------------|-------------------------|
| `<alias-dialog>`        | [Index](menu-index)     |
| `<attach-file>`         | [Compose](menu-compose) |
| `<attach-key>`          | [Compose](menu-compose) |
| `<attach-message>`      | [Compose](menu-compose) |
| `<attach-news-message>` | [Compose](menu-compose) |
| `<autocrypt-acct-menu>` | [Index](menu-index)     |
| `<autocrypt-menu>`      | [Compose](menu-compose) |

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
| `<backspace>`      | [Editor](menu-editor)                                                 |
| `<backward-char>`  | [Editor](menu-editor)                                                 |
| `<backward-word>`  | [Editor](menu-editor)                                                 |
| `<bol>`            | [Editor](menu-editor)                                                 |
| `<bottom>`         | [Pager](menu-pager)                                                   |
| `<bottom-page>`    | [Generic](menu-generic)                                               |
| `<bounce-message>` | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager)       |
| `<break-thread>`   | [Index](menu-index), [Pager](menu-pager)                              |
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

| Function                      | Used By                                                         |
|-------------------------------|-----------------------------------------------------------------|
| `<capitalize-word>`           | [Editor](menu-editor)                                           |
| `<catchup>`                   | [Browser](menu-browser), [Index](menu-index)                    |
| `<change-dir>`                | [Browser](menu-browser)                                         |
| `<change-folder>`             | [Index](menu-index), [Pager](menu-pager)                        |
| `<change-folder-readonly>`    | [Index](menu-index), [Pager](menu-pager)                        |
| `<change-newsgroup>`          | [Index](menu-index), [Pager](menu-pager)                        |
| `<change-newsgroup-readonly>` | [Index](menu-index), [Pager](menu-pager)                        |
| `<change-vfolder>`            | [Index](menu-index), [Pager](menu-pager)                        |
| `<check-new>`                 | [Browser](menu-browser)                                         |
| `<check-stats>`               | [Generic](menu-generic), [Pager](menu-pager)                    |
| `<check-traditional-pgp>`     | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager) |
| `<clear-flag>`                | [Index](menu-index), [Pager](menu-pager)                        |
| `<close-all-threads>`         | [Index](menu-index)                                             |
| `<close-thread>`              | [Index](menu-index)                                             |
| `<collapse-all>`              | [Index](menu-index)                                             |
| `<collapse-parts>`            | [Attach](menu-attach)                                           |
| `<collapse-thread>`           | [Index](menu-index)                                             |
| `<complete>`                  | [Editor](menu-editor)                                           |
| `<complete-query>`            | [Editor](menu-editor)                                           |
| `<compose-to-sender>`         | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager) |
| `<copy-file>`                 | [Compose](menu-compose)                                         |
| `<copy-message>`              | [Index](menu-index), [Pager](menu-pager)                        |
| `<create-account>`            | [Autocrypt](menu-autocrypt)                                     |
| `<create-alias>`              | [Index](menu-index), [Pager](menu-pager), [Query](menu-query)   |
| `<create-mailbox>`            | [Browser](menu-browser)                                         |
| `<current-bottom>`            | [Generic](menu-generic)                                         |
| `<current-middle>`            | [Generic](menu-generic)                                         |
| `<current-top>`               | [Generic](menu-generic)                                         |

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

| Function                | Used By                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------|
| `<decode-copy>`         | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<decode-save>`         | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<decrypt-copy>`        | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<decrypt-save>`        | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<delete-account>`      | [Autocrypt](menu-autocrypt)                                                              |
| `<delete-char>`         | [Editor](menu-editor)                                                                    |
| `<delete-entry>`        | [Alias](menu-alias), [Attach](menu-attach), [Postpone](menu-postpone)                    |
| `<delete-mailbox>`      | [Browser](menu-browser)                                                                  |
| `<delete-message>`      | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<delete-pattern>`      | [Index](menu-index)                                                                      |
| `<delete-subthread>`    | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<delete-thread>`       | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<descend-directory>`   | [Browser](menu-browser)                                                                  |
| `<detach-file>`         | [Compose](menu-compose)                                                                  |
| `<display-address>`     | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<display-filename>`    | [Browser](menu-browser)                                                                  |
| `<display-message>`     | [Index](menu-index)                                                                      |
| `<display-toggle-weed>` | [Attach](menu-attach), [Compose](menu-compose), [Index](menu-index), [Pager](menu-pager) |
| `<downcase-word>`       | [Editor](menu-editor)                                                                    |

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

| Function                     | Used By                                                                                                                                                 |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<edit>`                     | [Index](menu-index), [Pager](menu-pager)                                                                                                                |
| `<edit-bcc>`                 | [Compose](menu-compose)                                                                                                                                 |
| `<edit-cc>`                  | [Compose](menu-compose)                                                                                                                                 |
| `<edit-content-id>`          | [Compose](menu-compose)                                                                                                                                 |
| `<edit-description>`         | [Compose](menu-compose)                                                                                                                                 |
| `<edit-encoding>`            | [Compose](menu-compose)                                                                                                                                 |
| `<edit-fcc>`                 | [Compose](menu-compose)                                                                                                                                 |
| `<edit-file>`                | [Compose](menu-compose)                                                                                                                                 |
| `<edit-followup-to>`         | [Compose](menu-compose)                                                                                                                                 |
| `<edit-from>`                | [Compose](menu-compose)                                                                                                                                 |
| `<edit-headers>`             | [Compose](menu-compose)                                                                                                                                 |
| `<edit-label>`               | [Index](menu-index), [Pager](menu-pager)                                                                                                                |
| `<edit-language>`            | [Compose](menu-compose)                                                                                                                                 |
| `<edit-message>`             | [Compose](menu-compose)                                                                                                                                 |
| `<edit-mime>`                | [Compose](menu-compose)                                                                                                                                 |
| `<edit-newsgroups>`          | [Compose](menu-compose)                                                                                                                                 |
| `<edit-or-view-raw-message>` | [Index](menu-index), [Pager](menu-pager)                                                                                                                |
| `<edit-raw-message>`         | [Index](menu-index), [Pager](menu-pager)                                                                                                                |
| `<edit-reply-to>`            | [Compose](menu-compose)                                                                                                                                 |
| `<edit-subject>`             | [Compose](menu-compose)                                                                                                                                 |
| `<edit-to>`                  | [Compose](menu-compose)                                                                                                                                 |
| `<edit-type>`                | [Attach](menu-attach), [Compose](menu-compose), [Index](menu-index), [Pager](menu-pager)                                                                |
| `<edit-x-comment-to>`        | [Compose](menu-compose)                                                                                                                                 |
| `<end-cond>`                 | [Generic](menu-generic)                                                                                                                                 |
| `<enter-command>`            | [Generic](menu-generic), [Pager](menu-pager)                                                                                                            |
| `<enter-mask>`               | [Browser](menu-browser)                                                                                                                                 |
| `<entire-thread>`            | [Index](menu-index), [Pager](menu-pager)                                                                                                                |
| `<eol>`                      | [Editor](menu-editor)                                                                                                                                   |
| `<error-history>`            | {bdg-warning-line}`Renamed to:` [`<show-log-messages>`](fn-show-log-messages)                                                                           |
| `<exit>`                     | [Alias](menu-alias), [Attach](menu-attach), [Autocrypt](menu-autocrypt), [Browser](menu-browser), [Compose](menu-compose), [Dialog](menu-dialog),       |
|                              | [Generic](menu-generic), [Index](menu-index), [Pager](menu-pager), [Pgp](menu-pgp), [Postpone](menu-postpone), [Query](menu-query), [Smime](menu-smime) |
| `<extract-keys>`             | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager)                                                                                         |

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

| Function              | Used By                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------|
| `<fetch-mail>`        | [Index](menu-index)                                                                      |
| `<filter-entry>`      | [Compose](menu-compose)                                                                  |
| `<first-entry>`       | [Generic](menu-generic)                                                                  |
| `<flag-message>`      | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<followup-message>`  | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager)                          |
| `<forget-passphrase>` | [Attach](menu-attach), [Compose](menu-compose), [Index](menu-index), [Pager](menu-pager) |
| `<forward-char>`      | [Editor](menu-editor)                                                                    |
| `<forward-message>`   | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager)                          |
| `<forward-to-group>`  | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager)                          |
| `<forward-word>`      | [Editor](menu-editor)                                                                    |

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

| Function               | Used By                                                         |
|------------------------|-----------------------------------------------------------------|
| `<get-attachment>`     | [Compose](menu-compose)                                         |
| `<get-children>`       | [Index](menu-index)                                             |
| `<get-message>`        | [Index](menu-index)                                             |
| `<get-parent>`         | [Index](menu-index)                                             |
| `<goto-folder>`        | [Browser](menu-browser)                                         |
| `<goto-parent>`        | [Browser](menu-browser)                                         |
| `<group-alternatives>` | [Compose](menu-compose)                                         |
| `<group-chat-reply>`   | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager) |
| `<group-multilingual>` | [Compose](menu-compose)                                         |
| `<group-related>`      | [Compose](menu-compose)                                         |
| `<group-reply>`        | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager) |

(fn-half-down)=
(fn-half-up)=
(fn-help)=
(fn-history-down)=
(fn-history-search)=
(fn-history-up)=
## H

| Function           | Used By                                                             |
|--------------------|---------------------------------------------------------------------|
| `<half-down>`      | [Generic](menu-generic), [Pager](menu-pager)                        |
| `<half-up>`        | [Generic](menu-generic), [Pager](menu-pager)                        |
| `<help>`           | [Editor](menu-editor), [Generic](menu-generic), [Pager](menu-pager) |
| `<history-down>`   | [Editor](menu-editor)                                               |
| `<history-search>` | [Editor](menu-editor)                                               |
| `<history-up>`     | [Editor](menu-editor)                                               |

(fn-imap-fetch-mail)=
(fn-imap-logout-all)=
(fn-ispell)=
## I

| Function            | Used By                                  |
|---------------------|------------------------------------------|
| `<imap-fetch-mail>` | [Index](menu-index), [Pager](menu-pager) |
| `<imap-logout-all>` | [Index](menu-index), [Pager](menu-pager) |
| `<ispell>`          | [Compose](menu-compose)                  |

(fn-jump)=
## J

| Function | Used By                                      |
|----------|----------------------------------------------|
| `<jump>` | [Generic](menu-generic), [Pager](menu-pager) |

(fn-kill-eol)=
(fn-kill-eow)=
(fn-kill-line)=
(fn-kill-whole-line)=
(fn-kill-word)=
## K

| Function            | Used By               |
|---------------------|-----------------------|
| `<kill-eol>`        | [Editor](menu-editor) |
| `<kill-eow>`        | [Editor](menu-editor) |
| `<kill-line>`       | [Editor](menu-editor) |
| `<kill-whole-line>` | [Editor](menu-editor) |
| `<kill-word>`       | [Editor](menu-editor) |

(fn-last-entry)=
(fn-limit-current-thread)=
(fn-limit)=
(fn-link-threads)=
(fn-list-reply)=
(fn-list-subscribe)=
(fn-list-unsubscribe)=
## L

| Function                 | Used By                                                         |
|--------------------------|-----------------------------------------------------------------|
| `<last-entry>`           | [Generic](menu-generic)                                         |
| `<limit>`                | [Alias](menu-alias), [Index](menu-index), [Query](menu-query)   |
| `<limit-current-thread>` | [Index](menu-index)                                             |
| `<link-threads>`         | [Index](menu-index), [Pager](menu-pager)                        |
| `<list-reply>`           | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager) |
| `<list-subscribe>`       | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager) |
| `<list-unsubscribe>`     | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager) |

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

| Function                    | Used By                                                                            |
|-----------------------------|------------------------------------------------------------------------------------|
| `<mail>`                    | [Alias](menu-alias), [Index](menu-index), [Pager](menu-pager), [Query](menu-query) |
| `<mail-key>`                | [Index](menu-index), [Pager](menu-pager)                                           |
| `<mailbox-cycle>`           | [Editor](menu-editor)                                                              |
| `<mailbox-list>`            | [Browser](menu-browser), [Index](menu-index), [Pager](menu-pager)                  |
| `<mark-as-new>`             | [Pager](menu-pager)                                                                |
| `<mark-message>`            | [Index](menu-index)                                                                |
| `<middle-page>`             | [Generic](menu-generic)                                                            |
| `<modify-labels>`           | [Index](menu-index), [Pager](menu-pager)                                           |
| `<modify-labels-then-hide>` | [Index](menu-index), [Pager](menu-pager)                                           |
| `<modify-tags>`             | [Index](menu-index), [Pager](menu-pager)                                           |
| `<modify-tags-then-hide>`   | [Index](menu-index), [Pager](menu-pager)                                           |
| `<move-down>`               | [Compose](menu-compose)                                                            |
| `<move-up>`                 | [Compose](menu-compose)                                                            |

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

| Function                 | Used By                                      |
|--------------------------|----------------------------------------------|
| `<new-mime>`             | [Compose](menu-compose)                      |
| `<next-entry>`           | [Generic](menu-generic), [Pager](menu-pager) |
| `<next-line>`            | [Generic](menu-generic), [Pager](menu-pager) |
| `<next-new>`             | [Index](menu-index), [Pager](menu-pager)     |
| `<next-new-then-unread>` | [Index](menu-index), [Pager](menu-pager)     |
| `<next-page>`            | [Generic](menu-generic), [Pager](menu-pager) |
| `<next-subthread>`       | [Index](menu-index), [Pager](menu-pager)     |
| `<next-thread>`          | [Index](menu-index), [Pager](menu-pager)     |
| `<next-undeleted>`       | [Index](menu-index), [Pager](menu-pager)     |
| `<next-unread>`          | [Index](menu-index), [Pager](menu-pager)     |
| `<next-unread-mailbox>`  | [Index](menu-index), [Pager](menu-pager)     |

(fn-open-all-threads)=
(fn-open-thread)=
## O

| Function             | Used By             |
|----------------------|---------------------|
| `<open-all-threads>` | [Index](menu-index) |
| `<open-thread>`      | [Index](menu-index) |

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

| Function                     | Used By                                                                                  |
|------------------------------|------------------------------------------------------------------------------------------|
| `<parent-message>`           | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<pgp-menu>`                 | [Compose](menu-compose)                                                                  |
| `<pipe-entry>`               | [Attach](menu-attach), [Compose](menu-compose), [Index](menu-index), [Pager](menu-pager) |
| `<pipe-message>`             | [Attach](menu-attach), [Compose](menu-compose), [Index](menu-index), [Pager](menu-pager) |
| `<post-message>`             | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<postpone-message>`         | [Compose](menu-compose)                                                                  |
| `<preview-page-down>`        | [Compose](menu-compose)                                                                  |
| `<preview-page-up>`          | [Compose](menu-compose)                                                                  |
| `<previous-entry>`           | [Generic](menu-generic), [Pager](menu-pager)                                             |
| `<previous-line>`            | [Generic](menu-generic), [Pager](menu-pager)                                             |
| `<previous-new>`             | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<previous-new-then-unread>` | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<previous-page>`            | [Generic](menu-generic), [Pager](menu-pager)                                             |
| `<previous-subthread>`       | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<previous-thread>`          | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<previous-undeleted>`       | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<previous-unread>`          | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<print-entry>`              | [Attach](menu-attach), [Compose](menu-compose), [Pager](menu-pager)                      |
| `<print-message>`            | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<purge-message>`            | [Index](menu-index), [Pager](menu-pager)                                                 |
| `<purge-thread>`             | [Index](menu-index), [Pager](menu-pager)                                                 |

(fn-quasi-delete)=
(fn-query-append)=
(fn-query)=
(fn-quit)=
(fn-quote-char)=
## Q

| Function         | Used By                                                         |
|------------------|-----------------------------------------------------------------|
| `<quasi-delete>` | [Index](menu-index), [Pager](menu-pager)                        |
| `<query>`        | [Index](menu-index), [Query](menu-query)                        |
| `<query-append>` | [Query](menu-query)                                             |
| `<quit>`         | [Dialog](menu-dialog), [Index](menu-index), [Pager](menu-pager) |
| `<quote-char>`   | [Editor](menu-editor)                                           |

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
| `<read-subthread>`     | [Index](menu-index), [Pager](menu-pager)                              |
| `<read-thread>`        | [Index](menu-index), [Pager](menu-pager)                              |
| `<recall-message>`     | [Index](menu-index), [Pager](menu-pager)                              |
| `<reconstruct-thread>` | [Index](menu-index), [Pager](menu-pager)                              |
| `<redraw-screen>`      | [Editor](menu-editor), [Generic](menu-generic), [Pager](menu-pager)   |
| `<refresh>`            | {bdg-warning-line}`Renamed to:` [`<redraw-screen>`](fn-redraw-screen) |
| `<reload-active>`      | [Browser](menu-browser)                                               |
| `<rename-attachment>`  | [Compose](menu-compose)                                               |
| `<rename-file>`        | [Compose](menu-compose)                                               |
| `<rename-mailbox>`     | [Browser](menu-browser)                                               |
| `<reply>`              | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager)       |
| `<resend-message>`     | [Attach](menu-attach), [Index](menu-index), [Pager](menu-pager)       |
| `<root-message>`       | [Index](menu-index), [Pager](menu-pager)                              |

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

| Function                   | Used By                                                                                |
|----------------------------|----------------------------------------------------------------------------------------|
| `<save-entry>`             | [Attach](menu-attach), [Pager](menu-pager)                                             |
| `<save-message>`           | [Index](menu-index), [Pager](menu-pager)                                               |
| `<search>`                 | [Generic](menu-generic), [Pager](menu-pager)                                           |
| `<search-next>`            | [Generic](menu-generic), [Pager](menu-pager)                                           |
| `<search-opposite>`        | [Generic](menu-generic), [Pager](menu-pager)                                           |
| `<search-reverse>`         | [Generic](menu-generic), [Pager](menu-pager)                                           |
| `<search-toggle>`          | [Pager](menu-pager)                                                                    |
| `<select-entry>`           | [Generic](menu-generic)                                                                |
| `<select-new>`             | [Browser](menu-browser)                                                                |
| `<send-message>`           | [Compose](menu-compose)                                                                |
| `<set-flag>`               | [Index](menu-index), [Pager](menu-pager)                                               |
| `<shell-escape>`           | [Generic](menu-generic), [Pager](menu-pager)                                           |
| `<show-limit>`             | [Index](menu-index)                                                                    |
| `<show-log-messages>`      | [Generic](menu-generic), [Pager](menu-pager)                                           |
| `<show-version>`           | [Generic](menu-generic), [Pager](menu-pager)                                           |
| `<sidebar-abort-search>`   | [Sidebar](menu-sidebar)                                                                |
| `<sidebar-first>`          | [Sidebar](menu-sidebar)                                                                |
| `<sidebar-last>`           | [Sidebar](menu-sidebar)                                                                |
| `<sidebar-next>`           | [Sidebar](menu-sidebar)                                                                |
| `<sidebar-next-new>`       | [Sidebar](menu-sidebar)                                                                |
| `<sidebar-open>`           | [Sidebar](menu-sidebar)                                                                |
| `<sidebar-page-down>`      | [Sidebar](menu-sidebar)                                                                |
| `<sidebar-page-up>`        | [Sidebar](menu-sidebar)                                                                |
| `<sidebar-prev>`           | [Sidebar](menu-sidebar)                                                                |
| `<sidebar-prev-new>`       | [Sidebar](menu-sidebar)                                                                |
| `<sidebar-start-search>`   | [Sidebar](menu-sidebar)                                                                |
| `<sidebar-toggle-virtual>` | [Sidebar](menu-sidebar)                                                                |
| `<sidebar-toggle-visible>` | [Sidebar](menu-sidebar)                                                                |
| `<skip-headers>`           | [Pager](menu-pager)                                                                    |
| `<skip-quoted>`            | [Pager](menu-pager)                                                                    |
| `<smime-menu>`             | [Compose](menu-compose)                                                                |
| `<sort>`                   | [Browser](menu-browser), [Query](menu-query)                                           |
| `<sort-alias>`             | [Alias](menu-alias)                                                                    |
| `<sort-alias-reverse>`     | [Alias](menu-alias)                                                                    |
| `<sort-mailbox>`           | [Index](menu-index), [Pager](menu-pager)                                               |
| `<sort-reverse>`           | [Browser](menu-browser), [Index](menu-index), [Pager](menu-pager), [Query](menu-query) |
| `<subscribe>`              | [Browser](menu-browser)                                                                |
| `<subscribe-pattern>`      | [Browser](menu-browser)                                                                |
| `<sync-mailbox>`           | [Index](menu-index), [Pager](menu-pager)                                               |

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

| Function                  | Used By                                                       |
|---------------------------|---------------------------------------------------------------|
| `<tag-entry>`             | [Generic](menu-generic)                                       |
| `<tag-message>`           | [Pager](menu-pager)                                           |
| `<tag-pattern>`           | [Alias](menu-alias), [Index](menu-index), [Query](menu-query) |
| `<tag-prefix>`            | [Generic](menu-generic)                                       |
| `<tag-prefix-cond>`       | [Generic](menu-generic)                                       |
| `<tag-subthread>`         | [Index](menu-index)                                           |
| `<tag-thread>`            | [Index](menu-index)                                           |
| `<toggle-active>`         | [Autocrypt](menu-autocrypt)                                   |
| `<toggle-disposition>`    | [Compose](menu-compose)                                       |
| `<toggle-mailboxes>`      | [Browser](menu-browser)                                       |
| `<toggle-new>`            | [Index](menu-index)                                           |
| `<toggle-prefer-encrypt>` | [Autocrypt](menu-autocrypt)                                   |
| `<toggle-quoted>`         | [Pager](menu-pager)                                           |
| `<toggle-read>`           | [Index](menu-index)                                           |
| `<toggle-recode>`         | [Compose](menu-compose)                                       |
| `<toggle-subscribed>`     | [Browser](menu-browser)                                       |
| `<toggle-unlink>`         | [Compose](menu-compose)                                       |
| `<toggle-write>`          | [Index](menu-index), [Pager](menu-pager)                      |
| `<top>`                   | [Pager](menu-pager)                                           |
| `<top-page>`              | [Generic](menu-generic)                                       |
| `<transpose-chars>`       | [Editor](menu-editor)                                         |

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

| Function                | Used By                                                               |
|-------------------------|-----------------------------------------------------------------------|
| `<uncatchup>`           | [Browser](menu-browser)                                               |
| `<undelete-entry>`      | [Alias](menu-alias), [Attach](menu-attach), [Postpone](menu-postpone) |
| `<undelete-message>`    | [Index](menu-index), [Pager](menu-pager)                              |
| `<undelete-pattern>`    | [Index](menu-index)                                                   |
| `<undelete-subthread>`  | [Index](menu-index), [Pager](menu-pager)                              |
| `<undelete-thread>`     | [Index](menu-index), [Pager](menu-pager)                              |
| `<ungroup-attachment>`  | [Compose](menu-compose)                                               |
| `<unsubscribe>`         | [Browser](menu-browser)                                               |
| `<unsubscribe-pattern>` | [Browser](menu-browser)                                               |
| `<untag-pattern>`       | [Alias](menu-alias), [Index](menu-index), [Query](menu-query)         |
| `<upcase-word>`         | [Editor](menu-editor)                                                 |
| `<update-encoding>`     | [Compose](menu-compose)                                               |

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

| Function                        | Used By                                        |
|---------------------------------|------------------------------------------------|
| `<verify-key>`                  | [Pgp](menu-pgp), [Smime](menu-smime)           |
| `<vfolder-from-query>`          | [Index](menu-index), [Pager](menu-pager)       |
| `<vfolder-from-query-readonly>` | [Index](menu-index), [Pager](menu-pager)       |
| `<vfolder-window-backward>`     | [Index](menu-index)                            |
| `<vfolder-window-forward>`      | [Index](menu-index)                            |
| `<vfolder-window-reset>`        | [Index](menu-index)                            |
| `<view-attach>`                 | [Attach](menu-attach), [Compose](menu-compose) |
| `<view-attachments>`            | [Index](menu-index), [Pager](menu-pager)       |
| `<view-file>`                   | [Browser](menu-browser)                        |
| `<view-mailcap>`                | [Attach](menu-attach), [Compose](menu-compose) |
| `<view-name>`                   | [Pgp](menu-pgp), [Smime](menu-smime)           |
| `<view-pager>`                  | [Attach](menu-attach), [Compose](menu-compose) |
| `<view-raw-message>`            | [Index](menu-index), [Pager](menu-pager)       |
| `<view-text>`                   | [Attach](menu-attach), [Compose](menu-compose) |

(fn-what-key)=
(fn-write-fcc)=
## W

| Function      | Used By                                      |
|---------------|----------------------------------------------|
| `<what-key>`  | [Generic](menu-generic), [Pager](menu-pager) |
| `<write-fcc>` | [Compose](menu-compose)                      |

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

