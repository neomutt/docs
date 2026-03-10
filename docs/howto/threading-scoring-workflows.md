---
title: How to Build Threading and Scoring Workflows
description: Combine threading and scoring to prioritize conversations in the index
keywords: threads, scoring, use_threads, sort, sort_aux, score
---

# How to Build Threading and Scoring Workflows

## Prerequisites

1. A mailbox with enough traffic to see threads.
2. Basic familiarity with the index view.

## Enable Threaded View

1. Turn on threading explicitly:

```neomuttrc
set use_threads = yes
set sort = date
set sort_aux = reverse-last-date-received
```

2. Open a mailbox with replies.

Expected result: related messages appear grouped in threads.

## Prioritize Important Threads with Scoring

1. Add score rules for key senders or subjects:

```neomuttrc
score ~f boss@example.com +50
score ~s "release" +20
```

2. Sort by score:

```neomuttrc
set sort = score
```

Expected result: important threads float to the top.

## Rescore After Threading (Optional)

If you use thread-dependent patterns in scoring, push the score command after opening the mailbox:

```neomuttrc
folder-hook . 'push "<enter-command>score ~= 10<enter>"'
```

Expected result: score rules that depend on thread state take effect.

See [How to Edit and Navigate Threads](/home/mutt/rtd/docs/docs/howto/threads.md) and [How to Use Scoring](/home/mutt/rtd/docs/docs/howto/scoring.md).
