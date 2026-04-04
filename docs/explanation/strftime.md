---
title: Understanding strftime()
description: How NeoMutt uses the C library strftime() function to format dates and times in format strings
keywords: strftime, date format, time format, date_format, index_format, cond-date, expandos, formatting codes
diataxis_type: explanation
---

(exp-strftime)=
# Understanding strftime()

NeoMutt uses the C library function `strftime()` to format dates and times wherever a date format string is expected — most commonly in `$index_format`, `$date_format`, and conditional date expressions.

## How NeoMutt Uses strftime()

In NeoMutt's format strings, date expandos like `%{...}`, `%[...]`, and `%(...)` pass their contents to `strftime()` for expansion:

| Expando    | Meaning                                              |
|------------|------------------------------------------------------|
| `%{fmt}`   | Message date/time converted to the **sender's** time zone |
| `%[fmt]`   | Message date/time converted to the **local** time zone    |
| `%(fmt)`   | Date/time when the message was **received** locally       |

The `fmt` part inside the braces is a `strftime()` format string.

## Common Format Codes

| Code | Description              | Example    |
|------|--------------------------|------------|
| `%Y` | Year with century        | `2026`     |
| `%y` | Year without century     | `26`       |
| `%m` | Month (01–12)            | `04`       |
| `%b` | Abbreviated month name   | `Apr`      |
| `%B` | Full month name          | `April`    |
| `%d` | Day of month (01–31)     | `04`       |
| `%a` | Abbreviated weekday name | `Sat`      |
| `%A` | Full weekday name        | `Saturday` |
| `%H` | Hour, 24-hour (00–23)    | `15`       |
| `%I` | Hour, 12-hour (01–12)    | `03`       |
| `%M` | Minute (00–59)           | `07`       |
| `%S` | Second (00–60)           | `42`       |
| `%p` | AM or PM                 | `PM`       |
| `%Z` | Time zone abbreviation   | `CET`      |
| `%z` | UTC offset               | `+0100`    |
| `%F` | ISO 8601 date (`%Y-%m-%d`) | `2026-04-04` |
| `%T` | ISO 8601 time (`%H:%M:%S`) | `15:07:42` |
| `%c` | Locale's date and time   | `Sat Apr  4 15:07:42 2026` |
| `%%` | Literal `%`              | `%`        |

## Examples in NeoMutt

### Setting the date format

```neomuttrc
set date_format = "%d/%m/%y %H:%M"
```

This makes the `%d` expando in `$index_format` display dates like `04/04/26 15:07`.

### Using date expandos in index_format

```neomuttrc
set index_format = "%4C %Z %[%b %d %H:%M] %-15.15L %s"
```

Here `%[%b %d %H:%M]` formats the message date in the local time zone as `Apr 04 15:07`.

### Combining with conditional dates

NeoMutt's conditional date feature uses `strftime()` codes inside the true/false branches:

```neomuttrc
set index_format = '%4C %Z %<[d?%[%H:%M]&%[%b %d]> %-15.15L %s'
```

Today's messages show the time (`15:07`), older messages show month and day (`Apr 04`).

## Locale Dependence

The output of codes like `%a`, `%b`, `%B`, and `%c` depends on the current locale.
NeoMutt inherits the locale from your environment — the `LC_TIME` environment variable controls which locale `strftime()` uses.

## Further Reading

- {doc}`/howto/format-strings` — NeoMutt format strings, conditionals, and padding
- [`strftime(3)` — Linux man page](https://man7.org/linux/man-pages/man3/strftime.3.html) — Full list of conversion specifiers
