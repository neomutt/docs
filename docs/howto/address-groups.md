---
title: How to Use Address Groups
description: Group addresses logically for use in patterns and hooks
keywords: address groups, group, ungroup, patterns, hooks
---

# How to Use Address Groups

## Syntax

```neomuttrc
group [-group name ...] {-rx regex ... | -addr address ...}
ungroup [-group name ...] {* | -rx regex ... | -addr address ...}
```

## Creating Address Groups

NeoMutt supports grouping addresses logically into named groups.
An address or regular expression can appear in several groups at the same time.
These groups can be used in patterns (for searching, limiting and tagging) and in hooks by using group patterns.

The `group` command is used to directly add either addresses or regular expressions to the specified group or groups.
The different categories of arguments to the `group` command can be in any order.
The flags `-rx` and `-addr` specify what the following strings (that cannot begin with a hyphen) should be interpreted as: either a regular expression or an email address, respectively.

## Implicit Group Creation

Address groups can also be created implicitly by the `alias`, `lists`, `subscribe` and `alternates` commands by specifying the optional `-group` option.
For example:

```neomuttrc
alternates -group me address1 address2
alternates -group me -group work address3
```

This would create a group named "me" which contains all three addresses and a group named "work" which contains only your work address *address3*.
Besides many other possibilities, this could be used to automatically mark your own messages in a mailing list folder as read or use a special signature for work-related messages.

## Removing Addresses from Groups

The `ungroup` command is used to remove addresses or regular expressions from the specified group or groups.
The syntax is similar to the `group` command, however the special character `*` can be used to empty a group of all of its contents.
As soon as a group gets empty because all addresses and regular expressions have been removed, it will internally be removed, too (i.e. there cannot be an empty group).
When removing regular expressions from a group, the *regex* must be specified exactly as given to the `group` command or `-group` argument.
