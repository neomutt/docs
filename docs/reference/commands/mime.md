---
title: MIME & Attachments
description: Commands for MIME type handling, auto-view, attachment counting, alternative order, and mailto URL header control.
keywords: alternative-order, auto-view, attachments, unattachments, mime-lookup, mailto-allow, mime types, mailcap, multipart, inline display, attachment rules, content type
---

(ref-cmd-mime)=
# MIME & Attachments

Commands for MIME type handling, auto-view, attachment counting, and content preferences.

(cmd-alternative-order)=
## `alternative-order`

Set the preference order for viewing multipart/alternative messages.

- `alternative-order <type> [<type> ...]` — list types in order of preference

```neomuttrc
alternative-order text/plain text/enriched text/html
```

(cmd-unalternative-order)=
## `unalternative-order`

Remove types from the preference order.

- `unalternative-order *` — reset to default
- `unalternative-order <type>` — remove a specific type

```neomuttrc
unalternative-order *
```

(cmd-auto-view)=
## `auto-view`

Automatically display MIME types inline using a mailcap entry.

- `auto-view <type> [<type> ...]` — add types for inline display

```neomuttrc
auto-view text/html
auto-view text/html application/pdf text/calendar
auto-view application/pgp-encrypted
```

(cmd-unauto-view)=
## `unauto-view`

Remove types from the auto-view list.

- `unauto-view *` — remove all
- `unauto-view <type>` — remove a specific type

```neomuttrc
unauto-view *
unauto-view text/html
```

(cmd-attachments)=
## `attachments`

Define rules for how NeoMutt counts attachments (affects `%X`, `%Q`, `%q` expandos).

- `attachments +<disposition> <type>` — count a type as an attachment
- `attachments -<disposition> <type>` — don't count a type
- `attachments ?` — show current rules

Dispositions: `I` (inline) or `A` (attached).

```neomuttrc
attachments +A */.*
attachments +I text/plain
attachments -A text/x-vcard
attachments -A message/external-body
attachments -I message/external-body
attachments ?
```

(cmd-unattachments)=
## `unattachments`

Remove attachment counting rules.

- `unattachments *` — remove all rules
- `unattachments +A <type>` — remove a specific rule

```neomuttrc
unattachments *
unattachments +A text/x-vcard
```

(cmd-mime-lookup)=
## `mime-lookup`

Tell NeoMutt to look up mailcap handlers for specific MIME types via the mailcap file.

- `mime-lookup <type> [<type> ...]`

```neomuttrc
mime-lookup application/octet-stream
```

(cmd-unmime-lookup)=
## `unmime-lookup`

Remove custom MIME-lookup rules.

- `unmime-lookup *` — remove all
- `unmime-lookup <type>` — remove a specific type

```neomuttrc
unmime-lookup *
```

(cmd-mailto-allow)=
## `mailto-allow`

Permit specific header fields to be set by `mailto:` URLs.

- `mailto-allow *` — allow all headers
- `mailto-allow <field> [<field> ...]` — allow specific headers

```neomuttrc
mailto-allow subject body cc
mailto-allow in-reply-to
```

(cmd-unmailto-allow)=
## `unmailto-allow`

Disallow headers in `mailto:` URL processing.

- `unmailto-allow *` — disallow all headers
- `unmailto-allow <field>` — disallow a specific header

```neomuttrc
unmailto-allow *
unmailto-allow body
```

