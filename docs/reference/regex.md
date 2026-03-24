---
title: Regular Expressions
description: Reference for regular expression syntax used in NeoMutt pattern matching
keywords: neomutt, regex, regular expressions, POSIX, pattern matching
---

# Regular Expressions

All string patterns in NeoMutt including those in more complex [patterns](patterns.md) must be specified using regular expressions (regex) in the "POSIX extended" syntax (which is more or less the syntax used by egrep and GNU awk).

The search is case sensitive if the regular expression contains at least one upper case letter, and case insensitive otherwise.

:::{note}
`\` must be quoted if used for a regular expression in an initialization command: `\\`.
:::

A regular expression is a pattern that describes a set of strings. Regular expressions are constructed analogously to arithmetic expressions, by using various operators to combine smaller expressions.

:::{note}
The regular expression can be enclosed/delimited by either `"` or `'` which is useful if the regular expression includes a white-space character. See [Configuration File Syntax](config-syntax.md) for more information on `"` and `'` delimiter processing. To match a literal `"` or `'` you must preface it with `\` (backslash).
:::

The fundamental building blocks are the regular expressions that match a single character. Most characters, including all letters and digits, are regular expressions that match themselves. Any metacharacter with special meaning may be quoted by preceding it with a backslash.

## Matching a Literal Dot

```
# no quotes
alternates only\.dot@example\.org

# single quotes
lists 'only\.dot@example\.org'

# Double quotes
subscribe "only\\.dot@example\\.org"
```

The period `.` matches any single character. The caret `^` and the dollar sign `$` are metacharacters that respectively match the empty string at the beginning and end of a line.

A list of characters enclosed by `[` and `]` matches any single character in that list; if the first character of the list is a caret `^` then it matches any character *not* in the list. For example, the regular expression *[0123456789]* matches any single digit. A range of ASCII characters may be specified by giving the first and last characters, separated by a hyphen `-`. Most metacharacters lose their special meaning inside lists. To include a literal `]` place it first in the list. Similarly, to include a literal `^` place it anywhere but first. Finally, to include a literal hyphen `-` place it last.

## POSIX Character Classes

Certain named classes of characters are predefined. Character classes consist of `[:`, a keyword denoting the class, and `:]`. The following classes are defined by the POSIX standard:

| Character class | Description                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------|
| `[:alnum:]`     | Alphanumeric characters                                                                                       |
| `[:alpha:]`     | Alphabetic characters                                                                                         |
| `[:blank:]`     | Space or tab characters                                                                                       |
| `[:cntrl:]`     | Control characters                                                                                            |
| `[:digit:]`     | Numeric characters                                                                                            |
| `[:graph:]`     | Characters that are both printable and visible. (A space is printable, but not visible, while an "a" is both) |
| `[:lower:]`     | Lower-case alphabetic characters                                                                              |
| `[:print:]`     | Printable characters (characters that are not control characters)                                             |
| `[:punct:]`     | Punctuation characters (characters that are not letter, digits, control characters, or space characters)      |
| `[:space:]`     | Space characters (such as space, tab and formfeed, to name a few)                                             |
| `[:upper:]`     | Upper-case alphabetic characters                                                                              |
| `[:xdigit:]`    | Characters that are hexadecimal digits                                                                        |

A character class is only valid in a regular expression inside the brackets of a character list.

:::{note}
The brackets in these class names are part of the symbolic names, and must be included in addition to the brackets delimiting the bracket list. For example, *[[:digit:]]* is equivalent to *[0-9]*.
:::

## Special Sequences

Two additional special sequences can appear in character lists. These apply to non-ASCII character sets, which can have single symbols (called collating elements) that are represented with more than one character, as well as several characters that are equivalent for collating or sorting purposes:

**Collating Symbols**
: A collating symbol is a multi-character collating element enclosed in `[.` and `.]`. For example, if "ch" is a collating element, then *[[.ch.]]* is a regex that matches this collating element, while *[ch]* is a regex that matches either "c" or "h".

**Equivalence Classes**
: An equivalence class is a locale-specific name for a list of characters that are equivalent. The name is enclosed in `[=` and `=]`. For example, the name "e" might be used to represent all of "e" with grave ("è"), "e" with acute ("é") and "e". In this case, *[[=e=]]* is a regex that matches any of: "e" with grave ("è"), "e" with acute ("é") and "e".

## Repetition Operators

A regular expression matching a single character may be followed by one of several repetition operators:

| Operator | Description                                                                  |
|----------|------------------------------------------------------------------------------|
| `?`      | The preceding item is optional and matched at most once                      |
| `*`      | The preceding item will be matched zero or more times                        |
| `+`      | The preceding item will be matched one or more times                         |
| `{n}`    | The preceding item is matched exactly *n* times                              |
| `{n,}`   | The preceding item is matched *n* or more times                              |
| `{,m}`   | The preceding item is matched at most *m* times                              |
| `{n,m}`  | The preceding item is matched at least *n* times, but no more than *m* times |

## Concatenation and Alternation

Two regular expressions may be concatenated; the resulting regular expression matches any string formed by concatenating two substrings that respectively match the concatenated subexpressions.

Two regular expressions may be joined by the infix operator `|`; the resulting regular expression matches any string matching either subexpression.

Repetition takes precedence over concatenation, which in turn takes precedence over alternation. A whole subexpression may be enclosed in parentheses to override these precedence rules.

## GNU Extensions

:::{note}
If you compile NeoMutt with the included regular expression engine, the following operators may also be used in regular expressions. These operators are not defined by POSIX, so they may or may not be available in stock libraries on various systems.
:::

| Expression | Description                                                           |
|------------|-----------------------------------------------------------------------|
| `\y`       | Matches the empty string at either the beginning or the end of a word |
| `\B`       | Matches the empty string within a word                                |
| `\<`       | Matches the empty string at the beginning of a word                   |
| `\>`       | Matches the empty string at the end of a word                         |
| `\w`       | Matches any word-constituent character (letter, digit, or underscore) |
| `\W`       | Matches any character that is not word-constituent                    |
| `` \` ``   | Matches the empty string at the beginning of a buffer (string)        |
| `\'`       | Matches the empty string at the end of a buffer                       |
