---
title: "Attachment Options"
description: "Reference for NeoMutt attachment configuration variables."
keywords: "attachment, mime, variables, neomutt"
---

# Attachment Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

(attach-charset)=
## `$attach_charset`

- **Type:** string list
- **Default:** (empty)

This variable is a colon-separated list of character encoding
schemes for text file attachments. NeoMutt uses this setting to guess
which encoding files being attached are encoded in to convert them to
a proper character set given in [`$send_charset`](#send-charset).

If *unset*, the value of [`$charset`](#charset) will be used instead.
For example, the following configuration would work for Japanese
text handling:

```neomuttrc
set attach_charset="iso-2022-jp:euc-jp:shift_jis:utf-8"
```

Note: for Japanese users, "iso-2022-*" must be put at the head
of the value as shown above if included.

(attach-format)=
## `$attach_format`

- **Type:** string
- **Default:** "`%u%D%I %t%4n %T%d %> [%.7m/%.10M, %.6e%<C?, %C>, %s] `"

This variable describes the format of the "attachment" menu.  The
following `printf(3)`-style sequences are understood:

*Short* *Long Name*           *Description*

`%C`    `%{charset}`          Charset

`%c`    `%{charset-convert}`  Requires charset conversion (`n` or `c`)

`%D`    `%{deleted}`          Deleted flag

`%d`    `%{description}`      Description (if none, falls back to `%F`)

`%e`    `%{mime-encoding}`    MIME content-transfer-encoding

`%F`    `%{file-disposition}` Filename in content-disposition header (if none, falls back to `%f`)

`%f`    `%{file}`             Filename

`%I`    `%{disposition}`      Disposition (`I` for inline, `A` for attachment)

`%M`    `%{mime-minor}`       MIME subtype

`%m`    `%{mime-major}`       Major MIME type

`%n`    `%{number}`           Attachment number

`%Q`    `%{attach-qualifies}` `Q`, if MIME part qualifies for attachment counting

`%s`    `%{file-size}`        Size (see **Size Format**)

`%T`    `%{tree}`             Graphic tree characters

`%t`    `%{tagged}`           Tagged flag

`%u`    `%{unlink}`           Unlink (=to delete) flag

`%X`    `%{attach-count}`     Number of qualifying MIME parts in this part and its children

                                      (see the [`$attachments`](#attachments) section for possible speed effects)

`%*X`   `%{padding-soft}`     Soft-fill with character `X` as pad

`%>X`   `%{padding-hard}`     Right justify the rest of the string and pad with character `X`

`%|X`   `%{padding-eol}`      Pad to the end of the line with character `X`

For an explanation of "soft-fill", see the [`$index_format`](#index-format) documentation.

(attach-save-dir)=
## `$attach_save_dir`

- **Type:** path
- **Default:** "`./`"

The directory where attachments are saved.

(attach-save-without-prompting)=
## `$attach_save_without_prompting`

- **Type:** boolean
- **Default:** no

This variable, when set to true, will cause attachments to be saved to
the 'attach_save_dir' location without prompting the user for the filename.

(attach-sep)=
## `$attach_sep`

- **Type:** string
- **Default:** "`\n`"

The separator to add between attachments when operating (saving,
printing, piping, etc) on a list of tagged attachments.

(attach-split)=
## `$attach_split`

- **Type:** boolean
- **Default:** yes

If this variable is *unset*, when operating (saving, printing, piping,
etc) on a list of tagged attachments, NeoMutt will concatenate the
attachments and will operate on them as a single attachment. The
[`$attach_sep`](#attach-sep) separator is added after each attachment. When *set*,
NeoMutt will operate on the attachments one by one.
