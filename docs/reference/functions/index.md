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

## A

| Function                | Used By                   |
|-------------------------|---------------------------|
| `<alias-dialog>`        | [Index](ref-fn-index)     |
| `<attach-file>`         | [Compose](ref-fn-compose) |
| `<attach-key>`          | [Compose](ref-fn-compose) |
| `<attach-message>`      | [Compose](ref-fn-compose) |
| `<attach-news-message>` | [Compose](ref-fn-compose) |
| `<autocrypt-acct-menu>` | [Index](ref-fn-index)     |
| `<autocrypt-menu>`      | [Compose](ref-fn-compose) |

## B

| Function           | Used By                                                               |
|--------------------|-----------------------------------------------------------------------|
| `<backspace>`      | [Editor](ref-fn-editor)                                               |
| `<backward-char>`  | [Editor](ref-fn-editor)                                               |
| `<backward-word>`  | [Editor](ref-fn-editor)                                               |
| `<bol>`            | [Editor](ref-fn-editor)                                               |
| `<bottom-page>`    | [Generic](ref-fn-generic)                                             |
| `<bottom>`         | [Pager](ref-fn-pager)                                                 |
| `<bounce-message>` | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<break-thread>`   | [Index](ref-fn-index), [Pager](ref-fn-pager)                          |
| `<buffy-cycle>`    | {bdg-warning-line}`Renamed to:` [`<mailbox-cycle>`](#m)               |
| `<buffy-list>`     | {bdg-warning-line}`Renamed to:` [`<mailbox-list>`](#m)                |

## C

| Function                      | Used By                                                               |
|-------------------------------|-----------------------------------------------------------------------|
| `<capitalize-word>`           | [Editor](ref-fn-editor)                                               |
| `<catchup>`                   | [Browser](ref-fn-browser), [Index](ref-fn-index)                      |
| `<change-dir>`                | [Browser](ref-fn-browser)                                             |
| `<change-folder-readonly>`    | [Index](ref-fn-index), [Pager](ref-fn-pager)                          |
| `<change-folder>`             | [Index](ref-fn-index), [Pager](ref-fn-pager)                          |
| `<change-newsgroup-readonly>` | [Index](ref-fn-index), [Pager](ref-fn-pager)                          |
| `<change-newsgroup>`          | [Index](ref-fn-index), [Pager](ref-fn-pager)                          |
| `<change-vfolder>`            | [Index](ref-fn-index), [Pager](ref-fn-pager)                          |
| `<check-new>`                 | [Browser](ref-fn-browser)                                             |
| `<check-stats>`               | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                      |
| `<check-traditional-pgp>`     | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<clear-flag>`                | [Index](ref-fn-index), [Pager](ref-fn-pager)                          |
| `<close-all-threads>`         | [Index](ref-fn-index)                                                 |
| `<close-thread>`              | [Index](ref-fn-index)                                                 |
| `<collapse-all>`              | [Index](ref-fn-index)                                                 |
| `<collapse-parts>`            | [Attach](ref-fn-attach)                                               |
| `<collapse-thread>`           | [Index](ref-fn-index)                                                 |
| `<complete-query>`            | [Editor](ref-fn-editor)                                               |
| `<complete>`                  | [Editor](ref-fn-editor)                                               |
| `<compose-to-sender>`         | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<copy-file>`                 | [Compose](ref-fn-compose)                                             |
| `<copy-message>`              | [Index](ref-fn-index), [Pager](ref-fn-pager)                          |
| `<create-account>`            | [Autocrypt](ref-fn-autocrypt)                                         |
| `<create-alias>`              | [Index](ref-fn-index), [Pager](ref-fn-pager), [Query](ref-fn-query)   |
| `<create-mailbox>`            | [Browser](ref-fn-browser)                                             |
| `<current-bottom>`            | [Generic](ref-fn-generic)                                             |
| `<current-middle>`            | [Generic](ref-fn-generic)                                             |
| `<current-top>`               | [Generic](ref-fn-generic)                                             |

## D

| Function                | Used By                                                                                          |
|-------------------------|--------------------------------------------------------------------------------------------------|
| `<decode-copy>`         | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<decode-save>`         | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<decrypt-copy>`        | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<decrypt-save>`        | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<delete-account>`      | [Autocrypt](ref-fn-autocrypt)                                                                    |
| `<delete-char>`         | [Editor](ref-fn-editor)                                                                          |
| `<delete-entry>`        | [Alias](ref-fn-alias), [Attach](ref-fn-attach), [Postpone](ref-fn-postpone)                      |
| `<delete-mailbox>`      | [Browser](ref-fn-browser)                                                                        |
| `<delete-message>`      | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<delete-pattern>`      | [Index](ref-fn-index)                                                                            |
| `<delete-subthread>`    | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<delete-thread>`       | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<descend-directory>`   | [Browser](ref-fn-browser)                                                                        |
| `<detach-file>`         | [Compose](ref-fn-compose)                                                                        |
| `<display-address>`     | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<display-filename>`    | [Browser](ref-fn-browser)                                                                        |
| `<display-message>`     | [Index](ref-fn-index)                                                                            |
| `<display-toggle-weed>` | [Attach](ref-fn-attach), [Compose](ref-fn-compose), [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<downcase-word>`       | [Editor](ref-fn-editor)                                                                          |

## E

| Function                     | Used By                                                                                                                                                               |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<edit-bcc>`                 | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-cc>`                  | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-content-id>`          | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-description>`         | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-encoding>`            | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-fcc>`                 | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-file>`                | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-followup-to>`         | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-from>`                | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-headers>`             | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-label>`               | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                                                                                          |
| `<edit-language>`            | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-message>`             | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-mime>`                | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-newsgroups>`          | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-or-view-raw-message>` | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                                                                                          |
| `<edit-raw-message>`         | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                                                                                          |
| `<edit-reply-to>`            | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-subject>`             | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-to>`                  | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit-type>`                | [Attach](ref-fn-attach), [Compose](ref-fn-compose), [Index](ref-fn-index), [Pager](ref-fn-pager)                                                                      |
| `<edit-x-comment-to>`        | [Compose](ref-fn-compose)                                                                                                                                             |
| `<edit>`                     | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                                                                                          |
| `<end-cond>`                 | [Generic](ref-fn-generic)                                                                                                                                             |
| `<enter-command>`            | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                                                                                                                      |
| `<enter-mask>`               | [Browser](ref-fn-browser)                                                                                                                                             |
| `<entire-thread>`            | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                                                                                          |
| `<eol>`                      | [Editor](ref-fn-editor)                                                                                                                                               |
| `<error-history>`            | {bdg-warning-line}`Renamed to:` [`<show-log-messages>`](#s)                                                                                                           |
| `<exit>`                     | [Alias](ref-fn-alias), [Attach](ref-fn-attach), [Autocrypt](ref-fn-autocrypt), [Browser](ref-fn-browser), [Compose](ref-fn-compose), [Dialog](ref-fn-dialog),         |
|                              | [Generic](ref-fn-generic), [Index](ref-fn-index), [Pager](ref-fn-pager), [Pgp](ref-fn-pgp), [Postpone](ref-fn-postpone), [Query](ref-fn-query), [Smime](ref-fn-smime) |
| `<extract-keys>`             | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager)                                                                                                 |

## F

| Function              | Used By                                                                                          |
|-----------------------|--------------------------------------------------------------------------------------------------|
| `<fetch-mail>`        | [Index](ref-fn-index)                                                                            |
| `<filter-entry>`      | [Compose](ref-fn-compose)                                                                        |
| `<first-entry>`       | [Generic](ref-fn-generic)                                                                        |
| `<flag-message>`      | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<followup-message>`  | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager)                            |
| `<forget-passphrase>` | [Attach](ref-fn-attach), [Compose](ref-fn-compose), [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<forward-char>`      | [Editor](ref-fn-editor)                                                                          |
| `<forward-message>`   | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager)                            |
| `<forward-to-group>`  | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager)                            |
| `<forward-word>`      | [Editor](ref-fn-editor)                                                                          |

## G

| Function               | Used By                                                               |
|------------------------|-----------------------------------------------------------------------|
| `<get-attachment>`     | [Compose](ref-fn-compose)                                             |
| `<get-children>`       | [Index](ref-fn-index)                                                 |
| `<get-message>`        | [Index](ref-fn-index)                                                 |
| `<get-parent>`         | [Index](ref-fn-index)                                                 |
| `<goto-folder>`        | [Browser](ref-fn-browser)                                             |
| `<goto-parent>`        | [Browser](ref-fn-browser)                                             |
| `<group-alternatives>` | [Compose](ref-fn-compose)                                             |
| `<group-chat-reply>`   | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<group-multilingual>` | [Compose](ref-fn-compose)                                             |
| `<group-related>`      | [Compose](ref-fn-compose)                                             |
| `<group-reply>`        | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager) |

## H

| Function           | Used By                                                                   |
|--------------------|---------------------------------------------------------------------------|
| `<half-down>`      | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                          |
| `<half-up>`        | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                          |
| `<help>`           | [Editor](ref-fn-editor), [Generic](ref-fn-generic), [Pager](ref-fn-pager) |
| `<history-down>`   | [Editor](ref-fn-editor)                                                   |
| `<history-search>` | [Editor](ref-fn-editor)                                                   |
| `<history-up>`     | [Editor](ref-fn-editor)                                                   |

## I

| Function            | Used By                                      |
|---------------------|----------------------------------------------|
| `<imap-fetch-mail>` | [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<imap-logout-all>` | [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<ispell>`          | [Compose](ref-fn-compose)                    |

## J

| Function | Used By                                          |
|----------|--------------------------------------------------|
| `<jump>` | [Generic](ref-fn-generic), [Pager](ref-fn-pager) |

## K

| Function            | Used By                 |
|---------------------|-------------------------|
| `<kill-eol>`        | [Editor](ref-fn-editor) |
| `<kill-eow>`        | [Editor](ref-fn-editor) |
| `<kill-line>`       | [Editor](ref-fn-editor) |
| `<kill-whole-line>` | [Editor](ref-fn-editor) |
| `<kill-word>`       | [Editor](ref-fn-editor) |

## L

| Function                 | Used By                                                               |
|--------------------------|-----------------------------------------------------------------------|
| `<last-entry>`           | [Generic](ref-fn-generic)                                             |
| `<limit-current-thread>` | [Index](ref-fn-index)                                                 |
| `<limit>`                | [Alias](ref-fn-alias), [Index](ref-fn-index), [Query](ref-fn-query)   |
| `<link-threads>`         | [Index](ref-fn-index), [Pager](ref-fn-pager)                          |
| `<list-reply>`           | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<list-subscribe>`       | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<list-unsubscribe>`     | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager) |

## M

| Function                    | Used By                                                                                    |
|-----------------------------|--------------------------------------------------------------------------------------------|
| `<mail-key>`                | [Index](ref-fn-index), [Pager](ref-fn-pager)                                               |
| `<mail>`                    | [Alias](ref-fn-alias), [Index](ref-fn-index), [Pager](ref-fn-pager), [Query](ref-fn-query) |
| `<mailbox-cycle>`           | [Editor](ref-fn-editor)                                                                    |
| `<mailbox-list>`            | [Browser](ref-fn-browser), [Index](ref-fn-index), [Pager](ref-fn-pager)                    |
| `<mark-as-new>`             | [Pager](ref-fn-pager)                                                                      |
| `<mark-message>`            | [Index](ref-fn-index)                                                                      |
| `<middle-page>`             | [Generic](ref-fn-generic)                                                                  |
| `<modify-labels-then-hide>` | [Index](ref-fn-index), [Pager](ref-fn-pager)                                               |
| `<modify-labels>`           | [Index](ref-fn-index), [Pager](ref-fn-pager)                                               |
| `<modify-tags-then-hide>`   | [Index](ref-fn-index), [Pager](ref-fn-pager)                                               |
| `<modify-tags>`             | [Index](ref-fn-index), [Pager](ref-fn-pager)                                               |
| `<move-down>`               | [Compose](ref-fn-compose)                                                                  |
| `<move-up>`                 | [Compose](ref-fn-compose)                                                                  |

## N

| Function                 | Used By                                          |
|--------------------------|--------------------------------------------------|
| `<new-mime>`             | [Compose](ref-fn-compose)                        |
| `<next-entry>`           | [Generic](ref-fn-generic), [Pager](ref-fn-pager) |
| `<next-line>`            | [Generic](ref-fn-generic), [Pager](ref-fn-pager) |
| `<next-new-then-unread>` | [Index](ref-fn-index), [Pager](ref-fn-pager)     |
| `<next-new>`             | [Index](ref-fn-index), [Pager](ref-fn-pager)     |
| `<next-page>`            | [Generic](ref-fn-generic), [Pager](ref-fn-pager) |
| `<next-subthread>`       | [Index](ref-fn-index), [Pager](ref-fn-pager)     |
| `<next-thread>`          | [Index](ref-fn-index), [Pager](ref-fn-pager)     |
| `<next-undeleted>`       | [Index](ref-fn-index), [Pager](ref-fn-pager)     |
| `<next-unread-mailbox>`  | [Index](ref-fn-index), [Pager](ref-fn-pager)     |
| `<next-unread>`          | [Index](ref-fn-index), [Pager](ref-fn-pager)     |

## O

| Function             | Used By               |
|----------------------|-----------------------|
| `<open-all-threads>` | [Index](ref-fn-index) |
| `<open-thread>`      | [Index](ref-fn-index) |

## P

| Function                     | Used By                                                                                          |
|------------------------------|--------------------------------------------------------------------------------------------------|
| `<parent-message>`           | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<pgp-menu>`                 | [Compose](ref-fn-compose)                                                                        |
| `<pipe-entry>`               | [Attach](ref-fn-attach), [Compose](ref-fn-compose), [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<pipe-message>`             | [Attach](ref-fn-attach), [Compose](ref-fn-compose), [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<post-message>`             | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<postpone-message>`         | [Compose](ref-fn-compose)                                                                        |
| `<preview-page-down>`        | [Compose](ref-fn-compose)                                                                        |
| `<preview-page-up>`          | [Compose](ref-fn-compose)                                                                        |
| `<previous-entry>`           | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                                                 |
| `<previous-line>`            | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                                                 |
| `<previous-new-then-unread>` | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<previous-new>`             | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<previous-page>`            | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                                                 |
| `<previous-subthread>`       | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<previous-thread>`          | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<previous-undeleted>`       | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<previous-unread>`          | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<print-entry>`              | [Attach](ref-fn-attach), [Compose](ref-fn-compose), [Pager](ref-fn-pager)                        |
| `<print-message>`            | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<purge-message>`            | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |
| `<purge-thread>`             | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                     |

## Q

| Function         | Used By                                                               |
|------------------|-----------------------------------------------------------------------|
| `<quasi-delete>` | [Index](ref-fn-index), [Pager](ref-fn-pager)                          |
| `<query-append>` | [Query](ref-fn-query)                                                 |
| `<query>`        | [Index](ref-fn-index), [Query](ref-fn-query)                          |
| `<quit>`         | [Dialog](ref-fn-dialog), [Index](ref-fn-index), [Pager](ref-fn-pager) |
| `<quote-char>`   | [Editor](ref-fn-editor)                                               |

## R

| Function               | Used By                                                                   |
|------------------------|---------------------------------------------------------------------------|
| `<read-subthread>`     | [Index](ref-fn-index), [Pager](ref-fn-pager)                              |
| `<read-thread>`        | [Index](ref-fn-index), [Pager](ref-fn-pager)                              |
| `<recall-message>`     | [Index](ref-fn-index), [Pager](ref-fn-pager)                              |
| `<reconstruct-thread>` | [Index](ref-fn-index), [Pager](ref-fn-pager)                              |
| `<redraw-screen>`      | [Editor](ref-fn-editor), [Generic](ref-fn-generic), [Pager](ref-fn-pager) |
| `<refresh>`            | {bdg-warning-line}`Renamed to:` [`<redraw-screen>`](#r)                   |
| `<reload-active>`      | [Browser](ref-fn-browser)                                                 |
| `<rename-attachment>`  | [Compose](ref-fn-compose)                                                 |
| `<rename-file>`        | [Compose](ref-fn-compose)                                                 |
| `<rename-mailbox>`     | [Browser](ref-fn-browser)                                                 |
| `<reply>`              | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager)     |
| `<resend-message>`     | [Attach](ref-fn-attach), [Index](ref-fn-index), [Pager](ref-fn-pager)     |
| `<root-message>`       | [Index](ref-fn-index), [Pager](ref-fn-pager)                              |

## S

| Function                   | Used By                                                                                        |
|----------------------------|------------------------------------------------------------------------------------------------|
| `<save-entry>`             | [Attach](ref-fn-attach), [Pager](ref-fn-pager)                                                 |
| `<save-message>`           | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                   |
| `<search-next>`            | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                                               |
| `<search-opposite>`        | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                                               |
| `<search-reverse>`         | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                                               |
| `<search-toggle>`          | [Pager](ref-fn-pager)                                                                          |
| `<search>`                 | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                                               |
| `<select-entry>`           | [Generic](ref-fn-generic)                                                                      |
| `<select-new>`             | [Browser](ref-fn-browser)                                                                      |
| `<send-message>`           | [Compose](ref-fn-compose)                                                                      |
| `<set-flag>`               | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                   |
| `<shell-escape>`           | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                                               |
| `<show-limit>`             | [Index](ref-fn-index)                                                                          |
| `<show-log-messages>`      | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                                               |
| `<show-version>`           | [Generic](ref-fn-generic), [Pager](ref-fn-pager)                                               |
| `<sidebar-abort-search>`   | [Sidebar](ref-fn-sidebar)                                                                      |
| `<sidebar-first>`          | [Sidebar](ref-fn-sidebar)                                                                      |
| `<sidebar-last>`           | [Sidebar](ref-fn-sidebar)                                                                      |
| `<sidebar-next-new>`       | [Sidebar](ref-fn-sidebar)                                                                      |
| `<sidebar-next>`           | [Sidebar](ref-fn-sidebar)                                                                      |
| `<sidebar-open>`           | [Sidebar](ref-fn-sidebar)                                                                      |
| `<sidebar-page-down>`      | [Sidebar](ref-fn-sidebar)                                                                      |
| `<sidebar-page-up>`        | [Sidebar](ref-fn-sidebar)                                                                      |
| `<sidebar-prev-new>`       | [Sidebar](ref-fn-sidebar)                                                                      |
| `<sidebar-prev>`           | [Sidebar](ref-fn-sidebar)                                                                      |
| `<sidebar-start-search>`   | [Sidebar](ref-fn-sidebar)                                                                      |
| `<sidebar-toggle-virtual>` | [Sidebar](ref-fn-sidebar)                                                                      |
| `<sidebar-toggle-visible>` | [Sidebar](ref-fn-sidebar)                                                                      |
| `<skip-headers>`           | [Pager](ref-fn-pager)                                                                          |
| `<skip-quoted>`            | [Pager](ref-fn-pager)                                                                          |
| `<smime-menu>`             | [Compose](ref-fn-compose)                                                                      |
| `<sort-alias-reverse>`     | [Alias](ref-fn-alias)                                                                          |
| `<sort-alias>`             | [Alias](ref-fn-alias)                                                                          |
| `<sort-mailbox>`           | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                   |
| `<sort-reverse>`           | [Browser](ref-fn-browser), [Index](ref-fn-index), [Pager](ref-fn-pager), [Query](ref-fn-query) |
| `<sort>`                   | [Browser](ref-fn-browser), [Query](ref-fn-query)                                               |
| `<subscribe-pattern>`      | [Browser](ref-fn-browser)                                                                      |
| `<subscribe>`              | [Browser](ref-fn-browser)                                                                      |
| `<sync-mailbox>`           | [Index](ref-fn-index), [Pager](ref-fn-pager)                                                   |

## T

| Function                  | Used By                                                             |
|---------------------------|---------------------------------------------------------------------|
| `<tag-entry>`             | [Generic](ref-fn-generic)                                           |
| `<tag-message>`           | [Pager](ref-fn-pager)                                               |
| `<tag-pattern>`           | [Alias](ref-fn-alias), [Index](ref-fn-index), [Query](ref-fn-query) |
| `<tag-prefix-cond>`       | [Generic](ref-fn-generic)                                           |
| `<tag-prefix>`            | [Generic](ref-fn-generic)                                           |
| `<tag-subthread>`         | [Index](ref-fn-index)                                               |
| `<tag-thread>`            | [Index](ref-fn-index)                                               |
| `<toggle-active>`         | [Autocrypt](ref-fn-autocrypt)                                       |
| `<toggle-disposition>`    | [Compose](ref-fn-compose)                                           |
| `<toggle-mailboxes>`      | [Browser](ref-fn-browser)                                           |
| `<toggle-new>`            | [Index](ref-fn-index)                                               |
| `<toggle-prefer-encrypt>` | [Autocrypt](ref-fn-autocrypt)                                       |
| `<toggle-quoted>`         | [Pager](ref-fn-pager)                                               |
| `<toggle-read>`           | [Index](ref-fn-index)                                               |
| `<toggle-recode>`         | [Compose](ref-fn-compose)                                           |
| `<toggle-subscribed>`     | [Browser](ref-fn-browser)                                           |
| `<toggle-unlink>`         | [Compose](ref-fn-compose)                                           |
| `<toggle-write>`          | [Index](ref-fn-index), [Pager](ref-fn-pager)                        |
| `<top-page>`              | [Generic](ref-fn-generic)                                           |
| `<top>`                   | [Pager](ref-fn-pager)                                               |
| `<transpose-chars>`       | [Editor](ref-fn-editor)                                             |

## U

| Function                | Used By                                                                     |
|-------------------------|-----------------------------------------------------------------------------|
| `<uncatchup>`           | [Browser](ref-fn-browser)                                                   |
| `<undelete-entry>`      | [Alias](ref-fn-alias), [Attach](ref-fn-attach), [Postpone](ref-fn-postpone) |
| `<undelete-message>`    | [Index](ref-fn-index), [Pager](ref-fn-pager)                                |
| `<undelete-pattern>`    | [Index](ref-fn-index)                                                       |
| `<undelete-subthread>`  | [Index](ref-fn-index), [Pager](ref-fn-pager)                                |
| `<undelete-thread>`     | [Index](ref-fn-index), [Pager](ref-fn-pager)                                |
| `<ungroup-attachment>`  | [Compose](ref-fn-compose)                                                   |
| `<unsubscribe-pattern>` | [Browser](ref-fn-browser)                                                   |
| `<unsubscribe>`         | [Browser](ref-fn-browser)                                                   |
| `<untag-pattern>`       | [Alias](ref-fn-alias), [Index](ref-fn-index), [Query](ref-fn-query)         |
| `<upcase-word>`         | [Editor](ref-fn-editor)                                                     |
| `<update-encoding>`     | [Compose](ref-fn-compose)                                                   |

## V

| Function                        | Used By                                            |
|---------------------------------|----------------------------------------------------|
| `<verify-key>`                  | [Pgp](ref-fn-pgp), [Smime](ref-fn-smime)           |
| `<vfolder-from-query-readonly>` | [Index](ref-fn-index), [Pager](ref-fn-pager)       |
| `<vfolder-from-query>`          | [Index](ref-fn-index), [Pager](ref-fn-pager)       |
| `<vfolder-window-backward>`     | [Index](ref-fn-index)                              |
| `<vfolder-window-forward>`      | [Index](ref-fn-index)                              |
| `<vfolder-window-reset>`        | [Index](ref-fn-index)                              |
| `<view-attach>`                 | [Attach](ref-fn-attach), [Compose](ref-fn-compose) |
| `<view-attachments>`            | [Index](ref-fn-index), [Pager](ref-fn-pager)       |
| `<view-file>`                   | [Browser](ref-fn-browser)                          |
| `<view-mailcap>`                | [Attach](ref-fn-attach), [Compose](ref-fn-compose) |
| `<view-name>`                   | [Pgp](ref-fn-pgp), [Smime](ref-fn-smime)           |
| `<view-pager>`                  | [Attach](ref-fn-attach), [Compose](ref-fn-compose) |
| `<view-raw-message>`            | [Index](ref-fn-index), [Pager](ref-fn-pager)       |
| `<view-text>`                   | [Attach](ref-fn-attach), [Compose](ref-fn-compose) |

## W

| Function      | Used By                                          |
|---------------|--------------------------------------------------|
| `<what-key>`  | [Generic](ref-fn-generic), [Pager](ref-fn-pager) |
| `<write-fcc>` | [Compose](ref-fn-compose)                        |

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

