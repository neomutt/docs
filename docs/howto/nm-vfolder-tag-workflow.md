---
title: Use Tags as a Workflow
description: Turn Notmuch tags and virtual mailboxes into a triage workflow — inbox, action, done
keywords: notmuch, tags, workflow, triage, virtual mailbox, modify-tags, todo, done, inbox, action, vfolder
---

# Use Tags as a Workflow

## Prerequisites

1. Notmuch virtual mailboxes configured in NeoMutt (see [Getting Started with Notmuch Virtual Mailboxes](../tutorials/notmuch-virtual-mailboxes)).
2. A key bound for tagging (see below).

## Set Up Workflow Mailboxes

1. Add virtual mailboxes that map to workflow stages:

```neomuttrc
virtual-mailboxes "Inbox"  "notmuch://?query=tag:inbox"
virtual-mailboxes "Action" "notmuch://?query=tag:todo"
virtual-mailboxes "Done"   "notmuch://?query=tag:done"
```

2. Bind a key for modifying tags if you haven't already:

```neomuttrc
bind index,pager \eT modify-tags
```

## Triage Messages

1. Open the **Inbox** mailbox.
2. Select a message and press {kbd}`Alt-T`.
3. Add a workflow tag and remove the inbox tag:

```
+todo -inbox
```

Expected result: the message disappears from Inbox and appears in Action.

## Mark Messages as Done

1. Open the **Action** mailbox.
2. Select a completed item and press {kbd}`Alt-T`:

```
+done -todo
```

Expected result: the message moves from Action to Done.

## The Workflow in Practice

| Stage    | Tag change         | Message appears in |
|----------|--------------------|--------------------|
| Triage   | `+todo -inbox`     | Action             |
| Complete | `+done -todo`      | Done               |
| Defer    | leave in inbox     | Inbox              |

Messages move between virtual mailboxes automatically as their tags change — no manual filing required.

## Speed Up Tagging with Macros

1. Create macros for common tag operations:

```neomuttrc
macro index ,t "<modify-tags>+todo -inbox<Enter>"  "Move to Action"
macro index ,d "<modify-tags>+done -todo<Enter>"    "Mark as Done"
macro index ,i "<modify-tags>+inbox -todo -done<Enter>" "Return to Inbox"
```

Expected result: pressing {kbd}`,t`, {kbd}`,d`, or {kbd}`,i` applies the tag change in one step.

See [Organising Email with Tags](../tutorials/tags-workflow) for the full tagging tutorial and [Organise Multiple Virtual Mailboxes](nm-vfolder-organise) for keeping the mailbox list tidy.
