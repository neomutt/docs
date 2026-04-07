---
title: Color Objects
description: Complete list of every colorable UI object in NeoMutt including index, sidebar, compose, and pager elements
keywords: color, colour, theme, style, object, index, sidebar, compose, pager, quoted, status, indicator, attachment
---

(ref-colors)=
# Color Objects

```{toctree}
---
maxdepth: 2
hidden:
---
names.md
syntax.md
```

| Colour                             | Description                                                             |
|------------------------------------|-------------------------------------------------------------------------|
| `attachment`                       | MIME attachments text (entire line)                                     |
| `attach_headers`                   | MIME attachment test (takes a pattern)                                  |
| `body`                             | Pager: highlight body of message (takes a pattern)                      |
| `bold`                             | Bold text                                                               |
| `compose header`           (space) | {bdg-warning-line}`Renamed to:` `compose_header`           (underscore) |
| `compose security_both`    (space) | {bdg-warning-line}`Renamed to:` `compose_security_both`    (underscore) |
| `compose security_encrypt` (space) | {bdg-warning-line}`Renamed to:` `compose_security_encrypt` (underscore) |
| `compose security_none`    (space) | {bdg-warning-line}`Renamed to:` `compose_security_none`    (underscore) |
| `compose security_sign`    (space) | {bdg-warning-line}`Renamed to:` `compose_security_sign`    (underscore) |
| `compose_header`                   | Header labels, e.g. From:                                               |
| `compose_security_both`            | Mail will be encrypted and signed                                       |
| `compose_security_encrypt`         | Mail will be encrypted                                                  |
| `compose_security_none`            | Mail will not be encrypted or signed                                    |
| `compose_security_sign`            | Mail will be signed                                                     |
| `error`                            | Error message                                                           |
| `hdrdefault`                       | Header default colour                                                   |
| `header`                           | Message headers (takes a pattern)                                       |
| `index_author`                     | Index: author field                                                     |
| `index_collapsed`                  | Index: number of messages in collapsed thread                           |
| `index_date`                       | Index: date field                                                       |
| `index_flags`                      | Index: flags field                                                      |
| `index_label`                      | Index: label field                                                      |
| `index_number`                     | Index: index number                                                     |
| `index_size`                       | Index: size field                                                       |
| `index_subject`                    | Index: subject field                                                    |
| `index_tags`                       | Index: tags field (`%g`, `%J`)                                          |
| `index_tag`                        | Index: tag field (`%G`)                                                 |
| `index`                            | Index: default colour                                                   |
| `indicator`                        | Selected item in list                                                   |
| `italic`                           | Italic text                                                             |
| `markers`                          | Pager: markers, line continuation                                       |
| `message`                          | Informational message                                                   |
| `normal`                           | Plain text                                                              |
| `options`                          | Options in prompt                                                       |
| `progress`                         | Progress bar                                                            |
| `prompt`                           | Question/user input                                                     |
| `quoted`                           | {bdg-warning-line}`Renamed to:` `quoted0`                               |
| `quoted0`                          | Pager: quoted text, level 0                                             |
| `quoted1`                          | Pager: quoted text, level 1                                             |
| `quoted2`                          | Pager: quoted text, level 2                                             |
| `quoted3`                          | Pager: quoted text, level 3                                             |
| `quoted4`                          | Pager: quoted text, level 4                                             |
| `quoted5`                          | Pager: quoted text, level 5                                             |
| `quoted6`                          | Pager: quoted text, level 6                                             |
| `quoted7`                          | Pager: quoted text, level 7                                             |
| `quoted8`                          | Pager: quoted text, level 8                                             |
| `quoted9`                          | Pager: quoted text, level 9                                             |
| `search`                           | Pager: search matches                                                   |
| `sidebar_background`               | Background colour for the Sidebar                                       |
| `sidebar_divider`                  | Line dividing sidebar from the index/pager                              |
| `sidebar_flagged`                  | Mailbox with flagged messages                                           |
| `sidebar_highlight`                | Select cursor                                                           |
| `sidebar_indicator`                | Current open mailbox                                                    |
| `sidebar_new`                      | Mailbox with new mail                                                   |
| `sidebar_ordinary`                 | Mailbox with no new or flagged messages                                 |
| `sidebar_spoolfile`                | {bdg-warning-line}`Renamed to:` `sidebar_spool_file`                    |
| `sidebar_spool_file`               | `$spool_file` (Spool mailbox)                                           |
| `sidebar_unread`                   | Mailbox with unread mail                                                |
| `signature`                        | Pager: signature lines                                                  |
| `status`                           | Status bar (takes a pattern)                                            |
| `stripe_even`                      | Stripes: even lines of the Help Page                                    |
| `stripe_odd`                       | Stripes: odd lines of the Help Page                                     |
| `tilde`                            | Pager: empty lines after message                                        |
| `tree`                             | Index: tree-drawing characters                                          |
| `underline`                        | Underlined text                                                         |
| `warning`                          | Warning messages                                                        |

