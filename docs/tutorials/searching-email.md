---
title: Searching and Filtering Email
description: Step-by-step guide to finding messages using NeoMutt's search and pattern matching
keywords: [neomutt, search, filter, patterns, limit, notmuch, tutorial]
---

# Searching and Filtering Email

This tutorial teaches the basic search and limit workflow in the index.
If you're new to reading mail in NeoMutt, start with [Reading Your First Email](first-email).

## Basic Search

1. Open a mailbox in the index.
2. Press `/` and type a word from a message subject, then press `Enter`.
3. Press `n` to jump to the next match.

Expected result: the cursor moves to messages that match the search string.

## Filter the Message List with Limit

1. Press `l` in the index to limit the view.
2. Enter a pattern like `~f alice@example.com`.
3. Press `Enter` to apply the limit.
4. Press `l` again and enter `*` to clear the limit.

Expected result: the index shows only matching messages while the limit is active.

## NeoMutt's Pattern Matching Language

Try these common patterns:

```text
~f alice@example.com     (from)
~s "build report"        (subject)
~d <1w                  (date within 1 week)
~b "error code"          (body)
```

Expected result: you can target specific message fields using patterns.

## Search by Sender, Subject, Date, and Body

1. Limit to a sender with `~f`.
2. Limit to last week with `~d <1w`.
3. Limit to a keyword in the body with `~b`.

Expected result: you can filter messages by common criteria.

## Combine Patterns

1. Combine with AND by listing patterns:

```
~f alice@example.com ~s report
```

2. Use OR with `|`:

```
(~f alice@example.com | ~f bob@example.com)
```

3. Exclude with `!`:

```
~s report !~b draft
```

Expected result: you can build precise queries.

## Save and Reuse Search Patterns

1. Create a macro for a frequent search:

```neomuttrc
macro index ,r "<limit>~f alice@example.com ~s report<Enter>" "Limit to reports from Alice"
```

2. Use `,r` in the index.

Expected result: you can repeat complex searches quickly.

## Full-Text Search with Notmuch

Notmuch adds full-text search and tag-based queries. If you need whole-mailbox searching, set up Notmuch and use `notmuch://` virtual mailboxes.

See [How to Use Notmuch](../howto/notmuch).

## Next Steps

- "I want to organize with tags." Continue with [Organising Email with Tags](tags-workflow).
- "I want to build saved searches." See [Macros](../howto/macros) and [Patterns](../reference/patterns).
