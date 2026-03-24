---
title: Fuzzy Search
description: Find items quickly by typing approximate or abbreviated text using FZF-style subsequence matching
keywords: fuzzy, fuzzy search, fzf, subsequence, matching, scoring, smart case, sidebar search
since: 2026-02-11
---

# Fuzzy Search

## Support

**Since:** NeoMutt 2026-02-11

:::{note}
This feature is under active development. Its API and behaviour
may change in future releases.
:::

## Introduction

The Fuzzy Search feature lets you find items — such as mailboxes,
aliases, or commands — by typing just a few characters from anywhere
in the name. You don't need to remember the exact spelling or the
full path. For example, typing "mlnd" is enough to
match "mailinglists/neomutt-dev".

The matcher works through the whole list of candidates in a single
pass and ranks every match by quality. Matches at the start of a
word, at a path separator, or in consecutive characters score higher
than scattered matches, so the best result naturally rises to the
top.

Searching is case-insensitive by default. When *smart case* is enabled,
typing an all-lowercase pattern still matches regardless of case, but
including even one uppercase letter makes the whole search case-sensitive.
This means you can find "INBOX" with "inbox", but typing "Inbox" will only
match strings that contain a capital "I".

Fuzzy search quality depends on ranking, not just yes/no matching.
If multiple candidates match, the one with the best score is shown
first. This usually favors short, compact, boundary-aligned matches.

## Used By

The following NeoMutt features use Fuzzy Search internally:

- [Sidebar Search](sidebar-search) — dynamically filter the Sidebar mailbox list as you type

Developers can benchmark the matcher using
`fuzzy/fuzzy-benchmark`. See `fuzzy/BENCHMARK.md` for usage details.

## Technical Details

The library currently provides one algorithm:
**subsequence matching** (`FUZZY_ALGO_SUBSEQ`), an FZF-style approach in
which every character of the pattern must appear in the candidate
string in order, but not necessarily consecutively. The
architecture is pluggable, so additional algorithms (edit distance,
token-based) can be added without changing the public API.

### Scoring Rules

Every match is given a numeric score. A higher score means a
better match. A score of `-1` means no match at all.

**Base Score**

| Rule | Points |
|------|--------|
| Each matched character | +10 per character |

**Bonuses**

| Condition | Points |
|-----------|--------|
| Match at position 0 (start of string) | +30 |
| Match after a separator (`/` `.` `-` `_`) | +15 |
| Each consecutive matched character | +15 |
| CamelCase boundary (lowercase then uppercase ASCII) | +10 |
| Match at position 0 with `prefer_prefix` enabled | +40 |

**Penalties**

| Condition | Points |
|-----------|--------|
| Gap between two matched characters | −2 per skipped character |
| Total match span (last position − first position + 1) | −1 per character |
| Candidate string length | −(length / 4) |

After all bonuses and penalties are applied, the final score is
clamped to a minimum of `0` for any valid match.

### Smart Case Matching

By default, matching ignores case for ASCII letters (A–Z).
When `smart_case` is enabled in `FuzzyOptions`:

- An all-lowercase pattern → case-insensitive matching (ASCII)
- A pattern containing any uppercase ASCII letter → case-sensitive matching

Non-ASCII characters (e.g. accented letters, CJK) are always
matched as-is, byte-for-byte, since only ASCII A–Z are
case-folded.

### UTF-8 Handling

Matching is hybrid:

- ASCII pattern characters are matched with ASCII case folding (A–Z only).
- Non-ASCII pattern characters are matched as complete UTF-8
  codepoints (their byte sequences must stay contiguous).

This avoids false positives where bytes from one UTF-8 character
are accidentally matched across different characters. Boundary
bonuses (separator and CamelCase) are still ASCII-only.

### Performance

The algorithm is designed for interactive use with thousands of
candidates:

- O(n) time — single forward pass through the candidate
- O(m) stack space — fixed 256-byte array for match positions; no heap allocation
- No backtracking, no recursion

Throughput depends on CPU, compiler flags, input shape and
iteration count. Use the bundled benchmark tool to measure your
environment rather than relying on a fixed ops/sec number.

## Known Bugs

None

## Credits

Richard Russon
