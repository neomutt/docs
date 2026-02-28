---
title: Understanding Character Sets
description: How NeoMutt handles character sets, encodings, and locale configuration
keywords: [charset, encoding, utf-8, unicode, locale, character set]
diataxis_type: explanation
---

# Understanding Character Sets

:::{admonition} Diátaxis: Explanation
:class: note

Write as **discursive discussion**. Explain WHY things are the way they are. Provide context,
background, and history. Connect concepts together. Use "about" framing. It's OK to include
opinion and perspective. Don't include step-by-step instructions — link to tutorials and
how-to guides instead. The reader should come away with deeper understanding.
:::

A "character set" is basically a mapping between bytes and glyphs and implies a certain
character encoding scheme. For example, for the ISO 8859 family of character sets, an
encoding of 8bit per character is used. For the Unicode character set, different character
encodings may be used, UTF-8 being the most popular. In UTF-8, a character is represented
using a variable number of bytes ranging from 1 to 4.

Since NeoMutt is a command-line tool run from a shell, and delegates certain tasks to
external tools (such as an editor for composing/editing messages), all of these tools need
to agree on a character set and encoding. There exists no way to reliably deduce the
character set a plain text file has. Interoperability is gained by the use of well-defined
environment variables. The full set can be printed by issuing `locale` on the command line.

Upon startup, NeoMutt determines the character set on its own using routines that inspect
locale-specific environment variables. Therefore, it is generally not necessary to set the
`$charset` variable in NeoMutt. It may even be counter-productive as NeoMutt uses system
and library functions that derive the character set themselves and on which NeoMutt has no
influence. It's safest to let NeoMutt work out the locale setup itself.

If you happen to work with several character sets on a regular basis, it's highly advisable
to use Unicode and a UTF-8 locale. Unicode can represent nearly all characters in a message
at the same time. When not using a Unicode locale, it may happen that you receive messages
with characters not representable in your locale. When displaying such a message, or
replying to or forwarding it, information may get lost possibly rendering the message
unusable (not only for you but also for the recipient, this breakage is not reversible as
lost information cannot be guessed).

A Unicode locale makes all conversions superfluous which eliminates the risk of conversion
errors. It also eliminates potentially wrong expectations about the character set between
NeoMutt and external programs.

The terminal emulator used also must be properly configured for the current locale.
Terminal emulators usually do *not* derive the locale from environment variables, they need
to be configured separately. If the terminal is incorrectly configured, NeoMutt may display
random and unexpected characters (question marks, octal codes, or just random glyphs),
format strings may not work as expected, you may not be able to enter non-ascii characters,
and possibly more. Data is always represented using bytes and so a correct setup is very
important as to the machine, all character sets "look" the same.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Garbled vs correct charset display

**Description:** A side-by-side comparison (or two sequential screenshots) of the NeoMutt pager showing the same email message: one with a mismatched charset/locale displaying garbled text (mojibake — question marks, octal codes, or wrong glyphs), and one with the correct UTF-8 locale displaying the message properly with international characters (e.g. accented Latin, CJK, or Cyrillic text).

**Highlights:** The reader should notice the dramatic difference a correct charset configuration makes — the garbled version is unreadable while the correct version renders all characters properly, reinforcing why locale setup matters.
:::

:::{warning}
A mismatch between what system and library functions think the locale is and what NeoMutt
was told the locale is may make it behave badly with non-ascii input: it will fail at
seemingly random places. This warning is to be taken seriously since not only local mail
handling may suffer: sent messages may carry wrong character set information the *receiver*
has to deal with. The need to set `$charset` directly in most cases points at terminal and
environment variable setup problems, not NeoMutt problems.
:::

A list of officially assigned and known character sets can be found at
[IANA](http://www.iana.org/assignments/character-sets), a list of locally supported locales
can be obtained by running `locale -a`.

## Charset Hooks

NeoMutt provides two commands for dealing with non-standard or system-specific charset
names that appear in emails or are required by your iconv library.

### `charset-hook` — Aliasing Unknown Charset Names

```
charset-hook alias charset
```

The `charset-hook` command defines an alias for a character set. This is useful to
properly display messages which are tagged with a charset name not known to NeoMutt. For
example, some mailers send messages labelled with the non-standard name `x-unknown` instead
of a real IANA charset name. You can map it to a sane default:

```
charset-hook x-unknown us-ascii
```

Other common uses include mapping Windows-specific or application-specific names to their
standard equivalents:

```
charset-hook cp1252 windows-1252
charset-hook latin-1 iso-8859-1
```

### `iconv-hook` — System-Specific iconv Names

```
iconv-hook charset local-charset
```

The `iconv-hook` command defines a system-specific name for a character set. This is
helpful when your system's character conversion library (iconv) insists on using unusual,
system-specific names for character sets. For example, some platforms name UTF-8 as
`UTF8` (without the hyphen):

```
iconv-hook utf-8 UTF8
```

### When to Use Charset Hooks

- **`charset-hook`**: Use when you receive messages with non-standard or misspelled charset
  declarations (e.g., `x-unknown`, `cp1252`, or other vendor-specific names). NeoMutt will
  treat the alias as the real charset when decoding the message.

- **`iconv-hook`**: Use when NeoMutt fails to convert a charset because your iconv library
  uses a different internal name for it. This is a workaround for platform quirks rather
  than broken email; it tells NeoMutt which local iconv name to use for a given IANA
  charset name.
