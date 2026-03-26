---
title: Filter Spam
description: Configure NeoMutt to detect, tag, sort, and filter spam using external scoring filters and the spam/nospam commands
keywords: spam, nospam, spam filtering, spam detection, spam tag, header matching, spam_separator, x-spam-status, junk mail, scoring, %H, ~H, index_format, imap_headers, sort by spam
---

# Filter Spam

## Syntax

```neomuttrc
spam regex [format]
nospam {* | regex}
```

## Overview

NeoMutt has generalized support for external spam-scoring filters.
By defining your spam regular expressions with the `spam` and `nospam` commands, you can *limit*, *search*, and *sort* your mail based on its spam attributes, as determined by the external filter.
You also can display the spam attributes in your index display using the `%H` selector in the `$index_format` variable. (Tip: try `%<H?[%H] >` to display spam tags only when they are defined for a given message.)

:::{note}
The value displayed by `%H` and searched by `~H` is stored in the header cache.
NeoMutt isn't smart enough to invalidate a header cache entry based on changing `spam` rules, so if you aren't seeing correct `%H` values, try temporarily turning off the header cache.
If that fixes the problem, then once your spam rules are set to your liking, remove your stale header cache files and turn the header cache back on.
:::

## Defining Spam Rules

1. Define your external filter's spam headers using the `spam` command.
   *regex* should be a regular expression that matches a header in a mail message.
   If any message in the mailbox matches this regular expression, it will receive a "spam tag" or "spam attribute" (unless it also matches a `nospam` regular expression — see below.)

2. The appearance of this attribute is governed by the *format* parameter.
   *format* can be any static text, but it also can include back-references from the *regex* expression.
   (A regular expression "back-reference" refers to a sub-expression contained within parentheses.) `%1` is replaced with the first back-reference in the regex, `%2` with the second, etc.

3. To match spam tags, NeoMutt needs the corresponding header information which is always the case for local and POP folders but not for IMAP in the default configuration.
   Depending on the spam header to be analysed, `$imap_headers` may need to be adjusted.

## Using Multiple Spam Filters

If you're using multiple spam filters, a message can have more than one spam-related header.
You can define `spam` rules for each filter you use.
If a message matches two or more of these regular expressions, and the `$spam_separator` variable is set to a string, then the message's spam tag will consist of all the *format* strings joined together, with the value of `$spam_separator` separating them.

### Example Configuration

```neomuttrc
spam "X-DCC-.*-Metrics:.*(....)=many"         "90+/DCC-%1"
spam "X-Spam-Status: Yes"                     "90+/SA"
spam "X-PerlMX-Spam: .*Probability=([0-9]+)%" "%1/PM"
set spam_separator=", "
```

If then a message is received that DCC registered with "many" hits under the "Fuz2" checksum, and that PureMessage registered with a 97% probability of being spam, that message's spam tag would read `90+/DCC-Fuz2, 97/PM`. (The four characters before "=many" in a DCC report indicate the checksum used — in this case, "Fuz2".)

If the `$spam_separator` variable is unset, then each spam rule match supersedes the previous one.
Instead of getting joined *format* strings, you'll get only the last one to match.

## Spam Tag Usage

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Spam-tagged messages in the index

**Description:** The NeoMutt index view with `%H` included in `$index_format`, showing messages with visible spam tags (e.g. `90+/DCC-Fuz2`, `97/PM`) next to messages with no spam tag, demonstrating how external spam filter scores appear inline.

**Highlights:** The spam tag column rendered by `%H`, how different spam filters produce different tag formats, and how untagged (non-spam) messages show a blank in that column.
:::

The spam tag is what will be displayed in the index when you use `%H` in the `$index_format` variable.
It's also the string that the `~H` pattern-matching expression matches against for `<search>` and `<limit>` functions.
And it's what sorting by spam attribute will use as a sort key.

## Sorting by Spam Tag

Generally, when you sort by spam tag, NeoMutt will sort *lexically* — that is, by ordering strings alphanumerically.
However, if a spam tag begins with a number, NeoMutt will sort numerically first, and lexically only when two numbers are equal in value. (This is like UNIX's `sort -n`.) A message with no spam attributes at all — that is, one that didn't match *any* of your `spam` rules — is sorted at lowest priority.
Numbers are sorted next, beginning with 0 and ranging upward.
Finally, non-numeric strings are sorted, with "a" taking lower priority than "z".
Clearly, in general, sorting by spam tags is most effective when you can coerce your filter to give you a raw number.
But in case you can't, NeoMutt can still do something useful.

## Defining Exceptions with nospam

The `nospam` command can be used to write exceptions to `spam` rules.
If a header field matches something in a `spam` command, but you nonetheless do not want it to receive a spam tag, you can list a more precise regular expression under a `nospam` command.

If the *regex* given to `nospam` is exactly the same as the *regex* on an existing `spam` rule entry, the effect will be to remove the entry from the spam rules list, instead of adding an exception.
Likewise, if the *regex* for a `spam` command matches an entry on the `nospam` rule list, that nospam entry will be removed.
If the *regex* for `nospam` is `*`, *all entries on both lists* will be removed.
This might be the default action if you use `spam` and `nospam` in conjunction with a `folder-hook`.

You can have as many `spam` or `nospam` commands as you like.
You can even do your own primitive `spam` detection within NeoMutt — for example, if you consider all mail from `MAILER-DAEMON` to be spam, you can use a `spam` command like this:

```neomuttrc
spam "^From: .*MAILER-DAEMON"       "999"
```
