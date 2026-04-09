---
title: Fix an Empty Virtual Mailbox
description: Diagnose why a Notmuch virtual mailbox shows no messages in NeoMutt
keywords: notmuch, virtual mailbox, empty, troubleshooting, debug, query, tags, notmuch new, vfolder
---

# Fix an Empty Virtual Mailbox

## Prerequisites

1. A Notmuch virtual mailbox configured in NeoMutt that shows no messages.

## Test the Query on the Command Line

1. Copy the query from your config and run it directly:

```sh
notmuch search 'tag:inbox and tag:unread'
```

If this also returns nothing, the problem is in the query or the database, not NeoMutt.

## Check That Tags Exist

1. List the tags in your database:

```sh
notmuch search --output=tags '*'
```

2. Confirm the tags used in your query appear in the list.

Expected result: `inbox`, `unread`, or whichever tags your query uses are present.

If a tag is missing, your initial tagging rules may not have applied.
Run `notmuch tag +inbox -- folder:INBOX` (or an appropriate rule) to add the tag.

## Update the Database

1. Run `notmuch new` to index any recently synced mail:

```sh
notmuch new
```

2. Re-test the query.

Expected result: if new messages were indexed, the query now returns results.

## Verify Query Syntax

Common mistakes:

| Problem                      | Fix                                         |
|------------------------------|---------------------------------------------|
| Missing `and` / `or`         | `tag:inbox tag:unread` → `tag:inbox and tag:unread` |
| Typo in tag name             | Check with `notmuch search --output=tags '*'` |
| Wrong `from:` address        | Test with a known sender address             |
| Unquoted special characters  | Wrap the query in single quotes on the command line |

## Check nm_default_url

1. Confirm [`$nm_default_url`](cfg-nm-default-url) points to the correct database path:

```neomuttrc
set nm_default_url = "notmuch:///home/you/.local/share/mail"
```

The path must match `notmuch config get database.path`.

Expected result: NeoMutt and Notmuch use the same database.

## Check nm_exclude_tags

1. If you have [`$nm_exclude_tags`](cfg-nm-exclude-tags) set, confirm it isn't hiding the messages you expect:

```
:set nm_exclude_tags?
```

Expected result: the tags listed here do not overlap with the tags your query targets.

See [Notmuch](../notmuch) for full variable reference.
