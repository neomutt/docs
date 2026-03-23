---
title: Email Display & Headers
description: XXX
keywords: XXX
---

# Email Display & Headers

Commands that control how message headers and subjects are displayed.

## `ignore`

Hide headers when displaying messages.  By default, all headers are hidden.

- `ignore *` — hide all headers
- `ignore <header>` — hide a specific header

```neomuttrc
ignore *
ignore X-Mailer X-Priority
```

## `unignore`

Show headers that were previously hidden by `ignore`.

- `unignore *` — show all headers
- `unignore <header>` — show a specific header

```neomuttrc
ignore *
unignore from to cc subject date
unignore message-id reply-to
```

## `header-order`

Set the order in which visible headers are displayed.

- `header-order <header> [<header> ...]` — set display order

```neomuttrc
header-order from date subject to cc
```

## `unheader-order`

Remove headers from the custom display order.

- `unheader-order *` — reset to default order
- `unheader-order <header>` — remove a specific header from the order

```neomuttrc
unheader-order *
```

## `subject-regex`

Rewrite message subjects for display using a regex substitution.

- `subject-regex <regex> <replacement>` — define a substitution

```neomuttrc
subject-regex "^Re: (neomutt-devel|neomutt-users): " "Re: "
subject-regex "\\[PATCH\\] "                           ""
subject-regex "^(Re: )?Bug#([0-9]+): "                "\\1Bug:\\2 "
```

## `unsubject-regex`

Remove subject-rewriting rules.

- `unsubject-regex *` — remove all rules
- `unsubject-regex <regex>` — remove a specific rule

```neomuttrc
unsubject-regex *
```

