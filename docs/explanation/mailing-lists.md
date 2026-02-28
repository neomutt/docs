---
title: Understanding Mailing Lists
description: How NeoMutt handles mailing lists, alternative addresses, and list subscriptions
keywords: [mailing lists, lists, subscribe, alternates, mail-followup-to, list-reply]
diataxis_type: explanation
---

# Understanding Mailing Lists

:::{admonition} Diátaxis: Explanation
:class: note

Write as **discursive discussion**. Explain WHY things are the way they are. Provide context,
background, and history. Connect concepts together. Use "about" framing. It's OK to include
opinion and perspective. Don't include step-by-step instructions — link to tutorials and
how-to guides instead. The reader should come away with deeper understanding.
:::

## Handling Mailing Lists

NeoMutt has a few configuration options that make dealing with large amounts of mail easier.
The first thing you must do is to let NeoMutt know what addresses you consider to be
mailing lists (technically this does not have to be a mailing list, but that is what it is
most often used for), and what lists you are subscribed to. This is accomplished through the
use of the `lists` and `subscribe` commands in your `.neomuttrc`. Alternatively or
additionally, you can set `$auto_subscribe` to automatically subscribe addresses found in a
`List-Post` header.

Now that NeoMutt knows what your mailing lists are, it can do several things, the first of
which is the ability to show the name of a list through which you received a message (i.e.,
of a subscribed list) in the *index* menu display. This is useful to distinguish between
personal and list mail in the same mailbox. In the `$index_format` variable, the expando
"%L" will print the string "To \<list\>" when "list" appears in the "To" field, and
"Cc \<list\>" when it appears in the "Cc" field (otherwise it prints the name of the
author).

Often times the "To" and "Cc" fields in mailing list messages tend to get quite large. Most
people do not bother to remove the author of the message they reply to from the list,
resulting in two or more copies being sent to that person. The `<list-reply>` function,
which by default is bound to "L" in the *index* menu and *pager*, helps reduce the clutter
by only replying to the known mailing list addresses instead of all recipients (except as
specified by `Mail-Followup-To`, see below).

NeoMutt also supports the `Mail-Followup-To` header. When you send a message to a list of
recipients which includes one or several known mailing lists, and if the `$followup_to`
option is set, NeoMutt will generate a Mail-Followup-To header. If any of the recipients
are subscribed mailing lists, this header will contain all the recipients to whom you send
this message, but not your address. This indicates that group-replies or list-replies (also
known as "followups") to this message should only be sent to the original recipients of the
message, and not separately to you — you'll receive your copy through one of the mailing
lists you are subscribed to. If none of the recipients are subscribed mailing lists, the
header will also contain your address, ensuring you receive a copy of replies.

Conversely, when group-replying or list-replying to a message which has a
`Mail-Followup-To` header, NeoMutt will respect this header if the `$honor_followup_to`
configuration variable is set. Using list-reply will in this case also make sure that the
reply goes to the mailing list, even if it's not specified in the list of recipients in the
`Mail-Followup-To`.

:::{note}
When header editing is enabled, you can create a `Mail-Followup-To` header manually.
NeoMutt will only auto-generate this header if it doesn't exist when you send the message.
:::

The other method some mailing list admins use is to generate a "Reply-To" field which
points back to the mailing list address rather than the author of the message. This can
create problems when trying to reply directly to the author in private, since most mail
clients will automatically reply to the address given in the "Reply-To" field. NeoMutt uses
the `$reply_to` variable to help decide which address to use. If set to *ask-yes* or
*ask-no*, you will be prompted as to whether or not you would like to use the address given
in the "Reply-To" field, or reply directly to the address given in the "From" field. When
set to *yes*, the "Reply-To" field will be used when present.

You can change or delete the "X-Label:" field within NeoMutt using the "edit-label"
command, bound to the "y" key by default. This works for tagged messages, too. While in the
edit-label function, pressing the \<complete\> binding (TAB, by default) will perform
completion against all labels currently in use.

Lastly, NeoMutt has the ability to sort the mailbox into threads. A thread is a group of
messages which all relate to the same subject. This is usually organized into a tree-like
structure where a message and all of its replies are represented graphically. If you've ever
used a threaded news client, this is the same concept. It makes dealing with large volume
mailing lists easier because you can easily delete uninteresting threads and quickly find
topics of value.

## Alternative Addresses

With various functions, NeoMutt will treat messages differently, depending on whether you
sent them or whether you received them from someone else. For instance, when replying to a
message that you sent to a different party, NeoMutt will automatically suggest to send the
response to the original message's recipients — responding to yourself won't make much
sense in many cases. (See `$reply_to`.)

Many users receive e-mail under a number of different addresses. To fully use NeoMutt's
features here, the program must be able to recognize what e-mail addresses you receive mail
under. That's the purpose of the `alternates` command: It takes a list of regular
expressions, each of which can identify an address under which you receive e-mail.

As addresses are matched using regular expressions and not exact strict comparisons, you
should make sure you specify your addresses as precisely as possible to avoid mismatches.
For example, if you specify:

```
alternates user@example
```

NeoMutt will consider `some-user@example` as being your address, too which may not be
desired. As a solution, in such cases addresses should be specified as:

```
alternates '^user@example$'
```

The `-group` flag causes all of the subsequent regular expressions to be added to the named
group.

The `unalternates` command can be used to write exceptions to `alternates` regex. If an
address matches something in an `alternates` command, but you nonetheless do not think it is
from you, you can list a more precise regex under an `unalternates` command.

To remove a regular expression from the `alternates` list, use the `unalternates` command
with exactly the same *regex*. Likewise, if the *regex* for an `alternates` command matches
an entry on the `unalternates` list, that `unalternates` entry will be removed. If the
*regex* for `unalternates` is "\*", *all entries* on `alternates` will be removed.

## Mailing List Commands

NeoMutt has a few nice features for handling mailing lists. In order to take advantage of
them, you must specify which addresses belong to mailing lists, and which mailing lists you
are subscribed to. NeoMutt also has limited support for auto-detecting mailing lists: it
supports parsing `mailto:` links in the common `List-Post:` header which has the same
effect as specifying the list address via the `lists` command (except the group feature).
Once you have done this, the `<list-reply>` function will work for all known lists.
Additionally, when you send a message to a known list and `$followup_to` is set, NeoMutt
will add a Mail-Followup-To header. For unsubscribed lists, this will include your personal
address, ensuring you receive a copy of replies. For subscribed mailing lists, the header
will not, telling other users' mail user agents not to send copies of replies to your
personal address.

:::{note}
The Mail-Followup-To header is a non-standard extension which is not supported by all mail
user agents. Adding it is not bullet-proof against receiving personal CCs of list messages.
Also note that the generation of the Mail-Followup-To header is controlled by the
`$followup_to` configuration variable since it's common practice on some mailing lists to
send Cc upon replies (which is more a group- than a list-reply).
:::

More precisely, NeoMutt maintains lists of regular expressions for the addresses of known
and subscribed mailing lists. Every subscribed mailing list is known. To mark a mailing
list as known, use the `lists` command. To mark it as subscribed, use `subscribe`.

You can use regular expressions with both commands. To mark all messages sent to a specific
bug report's address on Debian's bug tracking system as list mail, for instance, you could
say

```
subscribe [0-9]+.*@bugs.debian.org
```

as it's often sufficient to just give a portion of the list's e-mail address.

Specify as much of the address as you need to remove ambiguity. For example, if you've
subscribed to the NeoMutt mailing list, you will receive mail addressed to
`neomutt-users@neomutt.org`. So, to tell NeoMutt that this is a mailing list, you could add
`lists neomutt-users@` to your initialization file. To tell NeoMutt that you are subscribed
to it, add `subscribe neomutt-users` to your initialization file instead. If you also
happen to get mail from someone whose address is `neomutt-users@example.com`, you could use
`lists ^neomutt-users@neomutt\.org$` or `subscribe ^neomutt-users@neomutt\.org$` to match
only mail from the actual list.

The `-group` flag adds all of the subsequent regular expressions to the named address group
in addition to adding to the specified address list.

The `unlists` command is used to remove a token from the list of known and subscribed
mailing-lists. Use `unlists *` to remove all tokens.

To remove a mailing list from the list of subscribed mailing lists, but keep it on the list
of known mailing lists, use `unsubscribe`.
