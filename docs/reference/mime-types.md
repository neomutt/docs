---
title: MIME Types
description: Reference for NeoMutt MIME type configuration, mime.types file format, and MIME lookup
keywords: neomutt, MIME, mime.types, mime-lookup, content-type, attachment
---

# MIME Types

## MIME Type Configuration with `mime.types`

To get most out of MIME, it's important that a MIME part's content type matches the content as closely as possible so that the recipient's client can automatically select the right viewer for the content. NeoMutt uses a simple plain text mapping file that specifies what file extension corresponds to what MIME type. This file is called `mime.types`.

### Search Locations

When you add an attachment to your mail message, NeoMutt searches for `mime.types` in the following locations (in order):

1. `/etc/mime.types`
2. `$SYSCONFDIR/mime.types`
3. `$PKGDATADIR/mime.types`
4. `$HOME/.mime.types`

Where `$HOME` is your home directory. The `$PKGDATADIR` and the `$SYSCONFDIR` directories depend on where NeoMutt is installed: the former is the default for shared data, the latter for system configuration files.

### File Format

Each line starts with the full MIME type, followed by a space and space-separated list of file extensions:

```
application/postscript          ps eps
application/pgp                 pgp
audio/x-aiff                    aif aifc aiff
```

A sample `mime.types` file comes with the NeoMutt distribution, and should contain most of the MIME types you are likely to use.

### Fallback Behavior

If NeoMutt can not determine the MIME type by the extension of the file you attach, it will run the command specified in `$mime_type_query_command`. If that command is not specified, NeoMutt will look at the file. If the file is free of binary information, NeoMutt will assume that the file is plain text, and mark it as `text/plain`. If the file contains binary information, then NeoMutt will mark it as `application/octet-stream`. You can change the MIME type that NeoMutt assigns to an attachment by using the `<edit-type>` command from the compose menu (default: ^T).

## Supported MIME Major Types

| MIME major type | Standard | Description                               |
|-----------------|----------|-------------------------------------------|
| `application`   | yes      | General application data                  |
| `audio`         | yes      | Audio data                                |
| `image`         | yes      | Image data                                |
| `message`       | yes      | Mail messages, message status information |
| `model`         | yes      | VRML and other modeling data              |
| `multipart`     | yes      | Container for other MIME parts            |
| `text`          | yes      | Text data                                 |
| `video`         | yes      | Video data                                |
| `chemical`      | no       | Mostly molecular data                     |

NeoMutt recognizes all of these if the appropriate entry is found in the `mime.types` file. Non-recognized MIME types should only be used if the recipient of the message is likely to be expecting such attachments.

MIME types are not arbitrary, they need to be assigned by [IANA](http://www.iana.org/assignments/media-types/).

## MIME Lookup

```
mime-lookup mime-type[/mime-subtype] [...]
unmime-lookup {* | mime-type[/mime-subtype] [...]}
```

:::{note}
Before 2026-01-13, these commands were called `mime_lookup` and `unmime_lookup`.
:::

NeoMutt's `mime-lookup` list specifies a list of MIME types that should *not* be treated according to their mailcap entry. This option is designed to deal with binary types such as `application/octet-stream`. When an attachment's MIME type is listed in `mime-lookup`, then the extension of the filename will be compared to the list of extensions in the `mime.types` file. The MIME type associated with this extension will then be used to process the attachment according to the rules in the mailcap file and according to any other configuration options (such as `auto-view`) specified. Common usage would be:

```
mime-lookup application/octet-stream application/X-Lotus-Manuscript
```

The `unmime-lookup` command may be used to disable this feature for any particular MIME type if it had been set, for example, in a global `.neomuttrc`.
