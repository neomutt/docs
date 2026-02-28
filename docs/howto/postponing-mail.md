---
title: How to Postpone Mail
description: Delay sending a message and resume it later in NeoMutt
keywords: postpone, draft, resume, recall, compose
---

# How to Postpone Mail

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

At times it is desirable to delay sending a message that you have already begun to compose.
When the `<postpone-message>` function is used in the *compose* menu, the body of your message
and attachments are stored in the mailbox specified by the {ref}`$postponed <postponed>`
variable. This means that you can recall the message even if you exit NeoMutt and then restart
it at a later time.

## Resuming a Postponed Message

Once a message is postponed, there are several ways to resume it:

- From the command line you can use the `-p` option.
- If you compose a new message from the *index* or *pager* you will be prompted if postponed
  messages exist.
- If multiple messages are currently postponed, the *postponed* menu will pop up and you can
  select which message you would like to resume.

:::{note}
If you postpone a reply to a message, the reply setting of the message is only updated when
you actually finish the message and send it. Also, you must be in the same folder with the
message you replied to for the status of the message to be updated.
:::

See also the {ref}`$postpone <postpone>` quad-option.
