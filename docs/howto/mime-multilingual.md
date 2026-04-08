---
title: Handle Multilingual Messages
description: Read and compose multipart/multilingual and multipart/related emails with language and content-ID support in NeoMutt
keywords: multipart, multilingual, related, preferred_languages, content-language, content-id, rfc8255, rfc2387, group-multilingual, group-related, language selection, internationalization, compound objects, inline images
---

# Handle Multilingual Messages

## MIME Multipart/Multilingual

NeoMutt includes support for reading and writing `multipart/multilingual` emails.
A `multipart/multilingual` email is like a `multipart/alternative` email, except that it comes with parts of different versions of languages instead of appearances.
Its format is described by [RFC8255](https://www.rfc-editor.org/rfc/rfc8255.html).

### Reading Multipart/Multilingual Emails

NeoMutt uses the [`$preferred_languages`](cfg-preferred-languages) variable to determine which languages to display when displaying a `multipart/multilingual` email.
You can have several preferred languages, separated by `,`:

```neomuttrc
set preferred_languages="fr,en,de"
```

NeoMutt will try to match these strings against the multilingual header in the received emails "by prefix", e.g., `en` will match both `en` and `en_US`.

If [`$preferred_languages`](cfg-preferred-languages) is not set, it defaults to None, and the first part of the received `multipart/multilingual` email will be displayed.

### Composing Multipart/Multilingual Emails

The procedure for composing a `multipart/multilingual` email is similar to those in composing multipart/alternative.
You have to prepare every part manually or using some scripts, and then tag and group them together into a `multipart/multilingual` bundle before sending it:

1. Prepare parts of the multilingual emails.
2. Attach them as attachments.
3. Tag them with [`<tag-entry>`](fn-tag-entry).
4. Edit the `Content-Language` header of every attachment with command [`<edit-language>`](fn-edit-language) (default to `Ctrl-L`).
   This is important, otherwise the recipient of this email will not know the corresponding languages.
   You can set arbitrary string as `Content-Language`, but it is recommended to set it as some common prefixes such as "en", "zh" and "fr".
5. Group all the tagged messages together by [`<group-multilingual>`](fn-group-multilingual) (default to `^`).
6. Send the email as usual.

As in composing multipart/alternative, you can also use NeoMutt's macro and some external scripts to combine this procedure into one.

After grouping, the separate parts will be displayed in a tree structure.
Attachments can still be edited separately and reordered within the group, but must be ungrouped using the [`<ungroup-attachment>`](fn-ungroup-attachment) (`#`) binding for more advanced editing before tagging and grouping together again as described above.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Compose menu with multilingual attachment group

**Description:** NeoMutt compose menu showing a `multipart/multilingual` group
after [`<group-multilingual>`](fn-group-multilingual) has been applied — the grouped language parts (e.g.
English, French, German) are displayed in a tree structure under a single
multipart/multilingual container, each with its Content-Language visible.

**Highlights:** The tree-structured grouping of language alternatives in the compose attachment list, showing how the separate language parts become children of the multilingual container.
:::

## MIME Multipart/Related

NeoMutt doesn't include any special support for reading `multipart/related` emails, but it is possible to write a `multipart/related` email.
A `multipart/related` attachment is intended for compound objects consisting of several inter-related body parts which are linked together using the `Content-ID` header.
Its format is described by [RFC2387](https://www.rfc-editor.org/rfc/rfc2387.html).

### Composing Multipart/Related Emails

The procedure for composing a `multipart/related` email is similar to that in composing multipart/alternative.
You have to prepare every part manually or using some scripts, and then tag and group them together into a `multipart/related` bundle before sending it:

1. Prepare parts of the related email.
2. Attach them as attachments.
3. Tag them with [`<tag-entry>`](fn-tag-entry).
4. One part can reference another using its `Content-ID` header.
   For example, an HTML part that includes an embedded image needs to contain: `<img src="cid:content-id">` where an attached image has a `Content-ID` header of `content-id`.
   The `Content-ID` of an attachment can be set using [`<edit-content-id>`](fn-edit-content-id) (default key `Alt-i`).
   [`<edit-content-id>`](fn-edit-content-id) sets a random ID which can then be changed if desired.
   Permitted characters for `Content-ID` are: `-.0-9@A-Z_a-z`.

   If the `multipart/related` group is intended to be inline, members of the group should also have their `Content-Disposition` header set to `inline` which can be toggled using [`<toggle-disposition>`](fn-toggle-disposition) (default key `Ctrl-D`).

   It can also be desirable to give referenced files in the group a `filename` even when the `Content-Disposition` is set to be `inline`.
   To do this use [`<rename-attachment>`](fn-rename-attachment) (default key `Ctrl-O`).
5. Group all the tagged messages together with [`<group-related>`](fn-group-related) (default key `%`).
   Top level attachments (excluding `multipart` ones) in the group are automatically given a random `Content-ID` if they do not already have one.
6. Send the email as usual.

Some care needs to be taken with the construction of a `multipart/related` email to ensure it is correctly displayed by the receiving mail client.
A typical email with a `multipart/alternative` part containing a `text/plain` part and a `text/html` part with an embedded image, along with a separate attachment might end up like this:

```
  I     1 <no description>                                         [multipart/related, 7bit, 0K]
  I     2 ├─><no description>                                  [multipart/alternative, 7bit, 0K]
- I     3 │ ├─>/tmp/neomutt-hostname-XXXX-XXXXXX-XXXXXXXXXX   [text/plain, 7bit, us-ascii, 0.1K]
- I     4 │ └─>/tmp/neomutt-alternative.html                      [text/html, 8bit, utf-8, 0.6K]
  I     5 └─>image.png                                                  [image/png, base64, 19K]
  A     6 attachment.pdf                                         [application/pdf, quoted, 7.1K]
```

In the above email `/tmp/neomutt-alternative.html` would reference `image.png` using `<img src="cid:content-id">` and `image.png` has been given an explicit name of `image.png` using [`<rename-attachment>`](fn-rename-attachment) (regardless of its initial filename). [`<group-related>`](fn-group-related) has set its `Content-ID` header to a random value.
