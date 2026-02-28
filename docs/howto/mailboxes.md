---
title: How to Configure Mailboxes
description: Set up mailbox monitoring, multiple spool mailboxes, and the mbox-hook command in NeoMutt
keywords: mailboxes, named-mailboxes, unmailboxes, mbox-hook, spool, new mail, monitoring, label, notify, poll
---

# How to Configure Mailboxes

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

## Using Multiple Spool Mailboxes

```
mbox-hook [-noregex] regex mailbox
```

This command is used to move read messages from a specified mailbox to a different mailbox automatically when you quit or change folders. *regex* is used to specify the mailbox to treat as a "spool" mailbox and *mailbox* specifies where mail should be saved when read. The *-noregex* switch controls whether *regex* is matched using a simple string comparison or a full regex match.

The regex parameter has **mailbox shortcut** expansion performed on the first character. See **mailbox-hook** for more details.

Note that execution of mbox-hooks is dependent on the `$move` configuration variable. If set to "no" (the default), mbox-hooks will not be executed.

Unlike some of the other *hook* commands, only the *first* matching regex is used (it is not possible to save read mail in more than a single mailbox).

## Monitoring Incoming Mail

```
mailboxes [-label label] [-nolabel] [-notify] [-nonotify] [-poll] [-nopoll] mailbox [...]
named-mailboxes [-notify] [-nonotify] [-poll] [-nopoll] label mailbox [label mailbox ...]
unmailboxes { * | mailbox [...] }
```

This command specifies folders which can receive mail and which will be checked for new messages periodically.

The `-label` argument can be used to specify an alternative label to print in the sidebar or mailbox browser instead of the mailbox path. A label may be removed via the `-nolabel` argument. If unspecified, an existing mailbox label will be unchanged.

Use `-nonotify` to disable notifying when new mail arrives. The `-notify` argument can be used to re-enable notifying for an existing mailbox. If unspecified: a new mailbox will notify by default, while an existing mailbox will be unchanged.

To disable polling, specify `-nopoll` before the mailbox name. The `-poll` argument can be used to re-enable polling for an existing mailbox. If unspecified: a new mailbox will poll by default, while an existing mailbox will be unchanged.

*folder* can either be a local file or directory (Mbox/Mmdf or Maildir/Mh). If NeoMutt was built with POP and/or IMAP support, *folder* can also be a POP/IMAP folder URL. The URL syntax is described in **URL syntax**, POP and IMAP are described in [POP](pop.md) and [IMAP](imap.md) respectively.

NeoMutt provides a number of advanced features for handling (possibly many) folders and new mail within them, please refer to **new mail** for details (including in what situations and how often NeoMutt checks for new mail). Additionally, `$new_mail_command` can be used to run a command when new mail is detected.

The `unmailboxes` command is used to remove a token from the list of folders which receive mail. `unmailboxes` can be used on the mailbox path, `$folder`-abbreviated path, or description. Use `unmailboxes *` to remove all tokens.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Mailbox browser with named mailboxes

**Description:** The NeoMutt mailbox browser (opened with `c?` or the `<browser>` function) showing a list of monitored mailboxes configured via `named-mailboxes`, displaying the custom label names (e.g. "My INBOX", "Work Mail") instead of raw folder paths, along with message counts and new mail indicators.

**Highlights:** How `-label` / `named-mailboxes` labels replace raw paths in the browser, the new mail flag column, and the folder size or message count columns.
:::

:::{note}
The folders in the `mailboxes` command are resolved when the command is executed, so if these names contain **shortcut characters** (such as `=` and `!`), any variable definition that affects these characters (like `$folder` and `$spool_file`) should be set before the `mailboxes` command. If none of these shortcuts are used, a local path should be absolute as otherwise NeoMutt tries to find it relative to the directory from where NeoMutt was started which may not always be desired.
:::
