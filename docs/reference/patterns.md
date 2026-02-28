---
title: Pattern Matching
description: Complete reference for NeoMutt pattern modifiers, operators, date ranges, and search syntax
keywords: neomutt, patterns, search, limit, tag, filter, matching
---

# Pattern Matching

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

Many of NeoMutt's commands allow you to specify a pattern to match (`limit`, `tag-pattern`, `delete-pattern`, etc.).

## Pattern Modifiers

| Pattern modifier | Notes | Description |
|------------------|-------|-------------|
| `~A` | | all messages |
| `~b` *REGEX* | d) | messages whose body matches *REGEX* |
| `=b` *STRING* | | IMAP: messages whose body contains *STRING* (searches on the server) |
| `~B` *REGEX* | d) | messages whose body or headers match *REGEX* |
| `=B` *STRING* | | IMAP: messages whose body or headers contain *STRING* (searches on the server) |
| `~c` *REGEX* | | messages whose "Cc:" header matches *REGEX* |
| `%c` *GROUP* | | messages whose "Cc:" is a member of *GROUP* |
| `~C` *REGEX* | | messages whose "To:", "Cc:" or "Bcc:" header matches *REGEX* |
| `%C` *GROUP* | | messages whose "To:", "Cc:" or "Bcc:" is a member of *GROUP* |
| `~d` *DATERANGE* | | messages sent in *DATERANGE* |
| `~D` | | deleted messages |
| `~e` *REGEX* | | messages whose "Sender:" header matches *REGEX* |
| `%e` *GROUP* | | messages whose "Sender:" is a member of *GROUP* |
| `~E` | | expired messages |
| `~f` *REGEX* | | messages whose "From:" header matches *REGEX* |
| `%f` *GROUP* | | messages whose "From:" is a member of *GROUP* |
| `~F` | | flagged messages |
| `~g` | | cryptographically signed messages |
| `~G` | | cryptographically encrypted messages |
| `~h` *REGEX* | d) | messages whose header matches *REGEX* |
| `=h` *STRING* | | IMAP: messages whose header contains *STRING* (searches on the server) |
| `~H` *REGEX* | | messages whose spam header matches *REGEX* |
| `~i` *REGEX* | | messages whose "Message-Id:" header matches *REGEX* |
| `~I` *QUERY* | | messages whose "Message-Id:" is included in results from `$external_search_command` |
| `~k` | | messages which contain a PGP key |
| `~K` *REGEX* | | messages whose "Bcc:" header matches *REGEX* |
| `~l` | | messages addressed to known mailing lists |
| `~L` *REGEX* | | messages whose "From:", "Sender:", "To:" or "Cc:" header matches *REGEX* |
| `%L` *GROUP* | | messages whose "From:", "Sender:", "To:" or "Cc:" is a member of *GROUP* |
| `~m` *RANGE* | c) | messages whose number is in *RANGE* |
| `~M` *REGEX* | d) | messages with a Content-Type matching *REGEX* |
| `~n` *RANGE* | a) | messages whose score is in *RANGE* |
| `~N` | | new messages |
| `~O` | | old messages |
| `~p` | | messages addressed to you (consults `$from`, `alternates`, and local account/hostname information) |
| `~P` | | messages from you (consults `$from`, `alternates`, and local account/hostname information) |
| `~Q` | | messages which have been replied to |
| `~r` *DATERANGE* | | messages received in *DATERANGE* |
| `~R` | | read messages |
| `~s` *REGEX* | | messages whose "Subject:" header matches *REGEX* |
| `~S` | | superseded messages |
| `~t` *REGEX* | | messages whose "To:" header matches *REGEX* |
| `~T` | | tagged messages |
| `~u` | | messages addressed to subscribed mailing lists |
| `~U` | | unread messages |
| `~v` | | messages in collapsed threads |
| `~V` | | cryptographically verified messages |
| `~w` *REGEX* | | newsgroups matching *REGEX* |
| `~x` *REGEX* | | messages whose "References:" or "In-Reply-To" headers matches *REGEX* |
| `~X` *RANGE* | a), d) | messages with *RANGE* attachments |
| `~y` *REGEX* | | messages whose "X-Label:" header matches *REGEX* |
| `~Y` *REGEX* | | messages whose tags match *REGEX* |
| `~z` *RANGE* | a), b) | messages whose size is in *RANGE* |
| `~#` | | broken threads (see `$strict_threads`) |
| `~$` | | unreferenced messages (requires threaded view) |
| `=/` *STRING* | | GMail: custom server-side search for *STRING* |
| `~=` | | duplicated messages (see `$duplicate_threads`) |
| `~(`*PATTERN*`)` | | messages in threads containing messages matching *PATTERN*, e.g. all threads containing messages from you: `~(~P)` |
| `~<(`*PATTERN*`)` | | messages whose immediate parent matches *PATTERN*, e.g. replies to your messages: `~<(~P)` |
| `~>(`*PATTERN*`)` | | messages having an immediate child matching *PATTERN*, e.g. messages you replied to: `~>(~P)` |

## Alias Pattern Modifiers

| Pattern modifier | Notes | Description |
|------------------|-------|-------------|
| `~c` *REGEX* | | aliases which contain *REGEX* in the alias comment |
| `~f` *REGEX* | | aliases which contain *REGEX* in the alias name (From part of alias) |
| `~t` *REGEX* | | aliases which contain *REGEX* in the alias address (To part of alias) |
| `~Y` *REGEX* | | aliases whose tags match *REGEX* |

## Argument Types

| Type | Description |
|------|-------------|
| REGEX | Regular expression, see [Regular Expressions](regex.md) |
| STRING | Plain text string (for IMAP server-side search) |
| GROUP | Address group name (defined via `group` command) |
| DATERANGE | Date or date range (see [Searching by Date](#searching-by-date)) |
| RANGE | Numeric range: `N`, `N-M`, `<N`, `>N`, `N,M` (relative) (see [Message Ranges](#message-ranges)) |
| QUERY | Query string for external search command |

### Notes

a) The forms `<[MAX]`, `>[MIN]`, `[MIN]-` and `-[MAX]` are allowed, too.

b) The suffixes `K` and `M` are allowed to specify kilobyte and megabyte respectively.

c) The message number ranges (introduced by `~m`) are even more general and powerful than the other types of ranges. See [Message Ranges](#message-ranges) below.

d) These patterns read each message in, and can therefore be much slower. Over IMAP this will entail downloading each message. They can not be used for message scoring, and it is recommended to avoid using them for index coloring.

## Backslash Handling in Patterns

Special attention has to be paid when using regular expressions inside of patterns. Specifically, NeoMutt's parser for these patterns will strip one level of backslash (`\`), which is normally used for quoting. If it is your intention to use a backslash in the regular expression, you will need to use two backslashes instead (`\\`).

```
# no quotes
save-hook ~h\ list-id:\\s*<only\\.dot>    '=archive'
save-hook ~hlist-id:\\s*<only\\.dot-here> '=archive'

# single quotes
save-hook '~h list-id:\\s<only\.dot>'        '=archive'
save-hook ~h'list-id:\\s*<only\.dot-here>'   '=archive'

# Double quotes
save-hook "~h list-id:\\\\s<only\\\\.dot>"    '=archive'
save-hook ~h"list-id:\\\\s*<only\\\\.dot>"    '=archive'
```

## String Matching vs Regular Expressions

You can force NeoMutt to treat *REGEX* as a simple substring instead of a regular expression by using `=` instead of `~` in the pattern name. For example, `=b *.*` will find all messages that contain the literal string `*.*`. Simple string matches are less powerful than regular expressions but can be considerably faster.

For IMAP folders, string matches `=b`, `=B`, and `=h` will be performed on the server instead of by fetching every message. IMAP treats `=h` specially: it must be of the form "header: substring" and will not partially match header names. The substring part may be omitted if you simply wish to find messages containing a particular header without regard to its value.

## Address List Matching

Patterns matching lists of addresses (notably c, C, p, P and t) match if there is at least one match in the whole list. If you want to make sure that all elements of that list match, you need to prefix your pattern with `^`. This example matches all mails which only has recipients from Germany:

```
^~C \.de$
```

You can restrict address pattern matching to aliases that you have defined with the `@` modifier. This example matches messages whose recipients are all from Germany, and who are known to your alias list:

```
^@~C \.de$
```

To match any defined alias, use a regular expression that matches any string. This example matches messages whose senders are known aliases:

```
@~f .
```

## Message Ranges

If a message number range (MNR) contains a comma (`,`), it is a *relative* MNR. That means the numbers denote *offsets* from the highlighted message.

### Relative Message Number Ranges

| Pattern | Explanation |
|---------|-------------|
| `~m -2,2` | Previous 2, highlighted and next 2 emails |
| `~m 0,1` | Highlighted and next email |

In addition to numbers, either side of the range can also contain one of the special characters (shortcuts) `.^$`:

### Message Number Shortcuts

| Shortcut | Explanation | Example | Meaning |
|----------|-------------|---------|---------|
| `.` | Current / Highlighted | `~m -3,.` | Previous 3 emails plus the highlighted one |
| `$` | Last | `~m .,$` | Highlighted email and all the later ones |
| `^` | First | `~m ^,1` | Highlighted, next and all preceding ones |

You can also leave either side of the range blank, to make it extend as far as possible. For example, `~m ,1` has the same meaning as the last example above.

### Absolute Message Number Ranges

If a MNR *doesn't* contain a comma, the meaning is similar to other ranges, except that the shortcuts are still available:

| Pattern | Explanation |
|---------|-------------|
| `~m 3-10` | Emails 3 to 10 |
| `~m -10` | Emails 1 to 10 |
| `~m 10-` | Emails 10 to last |
| `~m <3` | First and second email |
| `~m ^-2` | First and second email |
| `~m >1` | Everything but first email |
| `~m 2-$` | Everything but first email |
| `~m 2` | Just the second email |

## Simple Searches

NeoMutt supports two versions of "simple searches". These are issued if the query entered for searching, limiting and similar operations does not seem to contain a valid pattern modifier (i.e. it does not contain one of these characters: `~`, `=` or `%`). If the query is supposed to contain one of these special characters, they must be escaped by prepending a backslash (`\`).

### Simple Search Keywords

The first type is by checking whether the query string equals a keyword case-insensitively. If that is the case, NeoMutt will use the shown pattern modifier instead. If a keyword would conflict with your search keyword, you need to turn it into a regular expression to avoid matching the keyword table. For example, if you want to find all messages matching "flag" (using `$simple_search`) but don't want to match flagged messages, simply search for `[f]lag`.

| Keyword | Pattern modifier |
|---------|------------------|
| `all` | `~A` |
| `.` | `~A` |
| `^` | `~A` |
| `del` | `~D` |
| `flag` | `~F` |
| `new` | `~N` |
| `old` | `~O` |
| `repl` | `~Q` |
| `read` | `~R` |
| `tag` | `~T` |
| `unread` | `~U` |

The second type of simple search is to build a complex search pattern using `$simple_search` as a template. NeoMutt will insert your query properly quoted and search for the composed complex query.

## Nesting and Boolean Operators

Logical AND is performed by specifying more than one criterion. For example:

```
~t work ~f smith
```

would select messages which contain the word "work" in the list of recipients *and* that have the word "smith" in the "From" header field.

NeoMutt also recognizes the following operators to create more complex search patterns:

- `!` — logical NOT operator
- `|` — logical OR operator
- `()` — logical grouping operator

Example: This pattern will select all messages which do not contain "work" in the "To" or "Cc" field and which are from "smith":

```
!(~t work|~c work) ~f smith
```

:::{note}
If a regular expression contains parenthesis, or a vertical bar (`|`), you *must* enclose the expression in double or single quotes since those characters are also used to separate different parts of NeoMutt's pattern language. For example: `~f "user@(home\.org|work\.com)"`
:::

## Searching by Date

NeoMutt supports two types of dates, *absolute* and *relative*.

### Absolute Dates

Dates *must* be in DD/MM/YY format (month and year are optional, defaulting to the current month and year) or YYYYMMDD. An example of a valid range of dates is:

```
Limit to messages matching: ~d 20/1/95-31/10
Limit to messages matching: ~d 19950120-19951031
```

If you omit the minimum (first) date, and just specify `-DD/MM/YY` or `-YYYYMMDD`, all messages *before* the given date will be selected. If you omit the maximum (second) date, and specify `DD/MM/YY-`, all messages *after* the given date will be selected. If you specify a single date with no dash (`-`), only messages sent on the given date will be selected.

You can add error margins to absolute dates. An error margin is a sign (`+` or `-`), followed by a digit, followed by one of the date units. As a special case, you can replace the sign by a `*` character, which is equivalent to giving identical plus and minus error margins.

#### Date Units

| Unit | Description |
|------|-------------|
| `y` | Years |
| `m` | Months |
| `w` | Weeks |
| `d` | Days |

Example: To select any messages two weeks around January 15, 2001:

```
Limit to messages matching: ~d 15/1/2001*2w
```

### Relative Dates

This type of date is relative to the current date, and may be specified as:

- `>` *offset* for messages older than *offset* units
- `<` *offset* for messages newer than *offset* units
- `=` *offset* for messages exactly *offset* units old

*offset* is specified as a positive number with one of the following units:

#### Relative Date Units

| Unit | Description |
|------|-------------|
| `y` | Years |
| `m` | Months |
| `w` | Weeks |
| `d` | Days |
| `H` | Hours |
| `M` | Minutes |
| `S` | Seconds |

Example: to select messages less than 1 month old:

```
Limit to messages matching: ~d <1m
```

:::{note}
All dates used when searching are relative to the *local* time zone, so unless you change the setting of your `$index_format` to include a `%[...]` format, these are *not* the dates shown in the main index.
:::

## Gmail Patterns

`=/ "search terms"` invokes server-side search, passing along the search terms provided. Search results are constrained by IMAP to be within the current folder. At present this only supports Gmail's search API IMAP extension. The search language is entirely up to the mail provider and changes at their discretion. Using `~/` will silently fail.

For up-to-date information about searching, see: [Gmail's Support Page](https://support.google.com/mail/answer/7190?hl=en). You will need to (once) use a web-browser to visit Settings/Labels and enable "Show in IMAP" for "All Mail". When searching, visit that folder in NeoMutt to most closely match Gmail search semantics.
