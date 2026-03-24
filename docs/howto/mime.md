---
title: How to Configure MIME Handling
description: Configure MIME types, mailcap viewers, auto-view, alternative ordering, and attachment searching in NeoMutt
keywords: MIME, mailcap, auto-view, alternative-order, attachments, mime.types, content-type, multipart
---

# How to Configure MIME Handling

## MIME Overview

MIME is short for "Multipurpose Internet Mail Extension" and describes
mechanisms to internationalize and structure mail messages. Before the
introduction of MIME, messages had a single text part and were limited to
us-ascii header and content. With MIME, messages can have attachments (and even
attachments which themselves have attachments and thus form a tree structure),
nearly arbitrary characters can be used for sender names, recipients and
subjects.

Besides the handling of non-ascii characters in message headers, to NeoMutt the
most important aspect of MIME are so-called MIME types. These are constructed
using a *major* and *minor* type separated by a forward slash. These specify
details about the content that follows. Based upon these, NeoMutt decides how
to handle this part. The most popular major type is `text` with minor types for
plain text, HTML and various other formats. Major types also exist for images,
audio, video and of course general application data (e.g. to separate
cryptographically signed data with a signature, send office documents, and in
general arbitrary binary data). There's also the `multipart` major type which
represents the root of a subtree of MIME parts.

MIME also defines a set of encoding schemes for transporting MIME content over
the network: `7bit`, `8bit`, `quoted-printable`, `base64` and `binary`. There
are some rules when to choose what for encoding headers and/or body (if
needed), and NeoMutt will in general make a good choice.

NeoMutt does most of MIME encoding/decoding behind the scenes to form messages
conforming to MIME on the sending side. On reception, it can be flexibly
configured as to how what MIME structure is displayed (and if it's displayed):
these decisions are based on the content's MIME type. There are three
areas/menus in dealing with MIME: the pager (while viewing a message), the
attachment menu and the compose menu.

## Viewing MIME Messages in the Pager

When you select a message from the index and view it in the pager, NeoMutt
decodes as much of a message as possible to a text representation. NeoMutt
internally supports a number of MIME types, including the `text/plain` type,
the `message/rfc822` (mail messages) type and some `multipart` types. In
addition, it recognizes a variety of PGP MIME and S/MIME types, including
PGP/MIME and `application/pgp`, and `application/pkcs7-mime`.

NeoMutt will denote attachments with a couple lines describing them. These
lines are of the form:

```
[-- Attachment #1: Description --]
[-- Type: text/plain, Encoding: 7bit, Size: 10000 --]
```

Where the *Description* is the description or filename given for the
attachment, and the *Encoding* is one of the already mentioned content
encodings.

If NeoMutt cannot deal with a MIME type, it will display a message like:

```
[-- image/gif is unsupported (use 'v' to view this part) --]
```

## The Attachment Menu

The default binding for `<view-attachments>` is "v", which displays the
attachment menu for a message. The attachment menu displays a list of the
attachments in a message. From the attachment menu, you can save, print, pipe,
delete, and view attachments. You can apply these operations to a group of
attachments at once, by tagging the attachments and by using the
`<tag-prefix>` operator. You can also reply to the current message from this
menu, and only the current attachment (or the attachments tagged) will be
quoted in your reply. You can view attachments as text, or view them using the
mailcap viewer definition (the mailcap mechanism is explained later in detail).

Finally, you can apply the usual message-related functions (like
**\<resend-message\>**, and the `<reply>` and
`<forward-message>` functions) to attachments of type `message/rfc822`.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** The attachment menu

**Description:** NeoMutt attachment menu (`v` key) showing a multipart message with several attachments listed — a text/plain body, an HTML alternative, an inline image, and a PDF attachment. Each line shows the MIME type, encoding, size, and filename.

**Highlights:** The tree structure for nested multipart containers, the MIME type and size columns, and the attachment numbering that lets users navigate and act on individual parts.
:::

### Viewing Attachments

There are four ways of viewing attachments:

- **`<view-mailcap>` (default keybinding: m)** — This will use the first
  matching mailcap entry. If no matching mailcap entries are found, it will
  abort with an error message.

- **`<view-attach>` (default keybinding: Enter)** — NeoMutt will display
  internally supported MIME types in the pager. This will respect
  **auto-view** settings, to determine whether to use a
  `copiousoutput` mailcap entry or just directly display the attachment. Other
  MIME types will use the first matching mailcap entry. If no matching mailcap
  entries are found, the attachment will be displayed in the pager as raw text.

- **`<view-pager>`** — NeoMutt will use the first matching `copiousoutput`
  mailcap entry to display the attachment in the pager (regardless of
  **auto-view** settings). If no matching mailcap entries are
  found, the attachment will be displayed in the pager as raw text.

- **`<view-text>` (default keybinding: T)** — The attachment will always be
  displayed in the pager as raw text.

### Saving Attachments

- **`<save-entry>` (default keybinding: s)** — This will save the attachment
  to disk. The permissions of the saved file will depend on the user's `umask`.
  e.g. `umask 022` will create a file with permissions `rw-r--r--`.

  See also: `$attach_save_dir`,
  `$attach_save_without_prompting`,
  `$attach_sep`,
  `$attach_split`

## The Compose Menu

The compose menu is the menu you see before you send a message. It allows you
to edit the recipient list, the subject, and other aspects of your message. It
also contains a list of the attachments of your message, including the main
body. From this menu, you can print, copy, filter, pipe, edit, compose, review,
and rename an attachment or a list of tagged attachments. You can also modify
the attachment information, notably the type, encoding and description.

Attachments appear as follows by default:

```
- 1 [text/plain, 7bit, 1K]           /tmp/neomutt-euler-8082-0 <no description>
  2 [applica/x-gunzip, base64, 422K] ~/src/neomutt-0.85.tar.gz <no description>
```

The "-" denotes that NeoMutt will delete the file after sending (or
postponing, or canceling) the message. It can be toggled with the
`<toggle-unlink>` command (default: u). The next field is the MIME
content-type, and can be changed with the `<edit-type>` command (default: ^T).
The next field is the encoding for the attachment, which allows a binary message
to be encoded for transmission on 7bit links. It can be changed with the
`<edit-encoding>` command (default: ^E). The next field is the size of the
attachment, rounded to kilobytes or megabytes. The next field is the filename,
which can be changed with the `<rename-file>` command (default: R). The final
field is the description of the attachment, and can be changed with the
`<edit-description>` command (default: d). See
`$attach_format` for a full list of available expandos to
format this display to your needs.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** The compose menu with attachments

**Description:** NeoMutt compose menu showing the message header fields (To, Cc, Subject, etc.) at the top and the attachment list at the bottom — including a text/plain body marked with "-" (will be deleted after sending) and one or two attached files with their MIME types, encodings, sizes, and filenames.

**Highlights:** The layout of the compose screen — header fields above, attachment list below — and the "-" unlink indicator, MIME type, encoding, and size columns for each attachment.
:::

:::{note}
The `<edit-type>` function (default: `^T`) is available in the index, pager,
compose, and attachment menus. It temporarily changes the MIME content-type of
an attachment — for example, to correct a bogus charset parameter set by the
sender's mailer (e.g., changing `text/plain; charset=us-ascii` to
`text/plain; charset=utf-8`). These changes are **not persistent**: they apply
only for the current session or send operation and do not modify the stored
message.
:::

## MIME Type Configuration with `mime.types`

To get the most out of MIME, it's important that a MIME part's content type
matches the content as closely as possible so that the recipient's client can
automatically select the right viewer for the content. However, there's no
reliable way for NeoMutt to know how to detect every possible file type.
Instead, it uses a simple plain text mapping file that specifies what file
extension corresponds to what MIME type. This file is called `mime.types`.

When you add an attachment to your mail message, NeoMutt searches the system
`mime.types` file at `/etc/mime.types`, `$SYSCONFDIR/mime.types` or
`$PKGDATADIR/mime.types` and then your personal `mime.types` file at
`$HOME/.mime.types`.

Where `$HOME` is your home directory. The `$PKGDATADIR` and the `$SYSCONFDIR`
directories depend on where NeoMutt is installed: the former is the default for
shared data, the latter for system configuration files.

Each line starts with the full MIME type, followed by a space and
space-separated list of file extensions. For example:

```
application/postscript          ps eps
application/pgp                 pgp
audio/x-aiff                    aif aifc aiff
```

A sample `mime.types` file comes with the NeoMutt distribution, and should
contain most of the MIME types you are likely to use.

If NeoMutt can not determine the MIME type by the extension of the file you
attach, it will run the command specified in
`$mime_type_query_command`. If that command is
not specified, NeoMutt will look at the file. If the file is free of binary
information, NeoMutt will assume that the file is plain text, and mark it as
`text/plain`. If the file contains binary information, then NeoMutt will mark
it as `application/octet-stream`. You can change the MIME type that NeoMutt
assigns to an attachment by using the `<edit-type>` command from the compose
menu (default: ^T). NeoMutt recognizes all of these if the appropriate entry is
found in the `mime.types` file. Non-recognized MIME types should only be used if
the recipient of the message is likely to be expecting such attachments.

### Supported MIME Types

| MIME major type | Standard | Description |
|-----------------|----------|-------------|
| `application` | yes | General application data |
| `audio` | yes | Audio data |
| `image` | yes | Image data |
| `message` | yes | Mail messages, message status information |
| `model` | yes | VRML and other modeling data |
| `multipart` | yes | Container for other MIME parts |
| `text` | yes | Text data |
| `video` | yes | Video data |
| `chemical` | no | Mostly molecular data |

MIME types are not arbitrary, they need to be assigned by
[IANA](http://www.iana.org/assignments/media-types/).

## MIME Viewer Configuration with Mailcap

NeoMutt supports [RFC1524](https://www.rfc-editor.org/rfc/rfc1524.html) MIME Configuration, in particular the Unix specific
format specified in Appendix A of [RFC1524](https://www.rfc-editor.org/rfc/rfc1524.html). This file format is commonly referred
to as the "mailcap" format. Many MIME compliant programs utilize the mailcap
format, allowing you to specify handling for all MIME types in one place for all
programs. Programs known to use this format include Firefox, lynx and metamail.

In order to handle various MIME types that NeoMutt doesn't have built-in
support for, it parses a series of external configuration files to find an
external handler. The default search string for these files is a colon
delimited list containing the following files:

1. `$HOME/.mailcap`
2. `$PKGDATADIR/mailcap`
3. `$SYSCONFDIR/mailcap`
4. `/etc/mailcap`
5. `/usr/etc/mailcap`
6. `/usr/local/etc/mailcap`

Where `$HOME` is your home directory. The `$PKGDATADIR` and the `$SYSCONFDIR`
directories depend on where NeoMutt is installed: the former is the default for
shared data, the latter for system configuration files.

The default search path can be obtained by running the following command:

```sh
neomutt -nF /dev/null -Q mailcap_path
```

In particular, the metamail distribution will install a mailcap file, usually
as `/usr/local/etc/mailcap`, which contains some baseline entries.

### The Basics of the Mailcap File

A mailcap file consists of a series of lines which are comments, blank, or
definitions.

A comment line consists of a `#` character followed by anything you want.

A blank line is blank.

A definition line consists of a content type, a view command, and any number of
optional fields. Each field of a definition line is divided by a semicolon ";"
character.

The content type is specified in the MIME standard "type/subtype" notation. For
example, `text/plain`, `text/html`, `image/gif`, etc. In addition, the mailcap
format includes two formats for wildcards, one using the special `*` subtype,
the other is the implicit wild, where you only include the major type. For
example, `image/*`, or `video` will match all image types and video types,
respectively.

The view command is a Unix command for viewing the type specified. There are two
different types of commands supported. The default is to send the body of the
MIME message to the command on stdin. You can change this behavior by using `%s`
as a parameter to your view command. This will cause NeoMutt to save the body
of the MIME message to a temporary file, and then call the view command with the
`%s` replaced by the name of the temporary file. In both cases, NeoMutt will
turn over the terminal to the view program until the program quits, at which
time NeoMutt will remove the temporary file if it exists. This means that
mailcap does *not* work out of the box with programs which detach themselves
from the terminal right after starting, like `open` on Mac OS X. In order to
nevertheless use these programs with mailcap, you probably need custom shell
scripts.

So, in the simplest form, you can send a `text/plain` message to the external
pager more on standard input:

```
text/plain; more
```

Or, you could send the message as a file:

```
text/plain; more %s
```

Perhaps you would like to use lynx to interactively view a `text/html` message:

```
text/html; lynx %s
```

In this case, lynx does not support viewing a file from standard input, so you
must use the `%s` syntax.

:::{note}
*Some older versions of lynx contain a bug where they will check the mailcap
file for a viewer for `text/html`. They will find the line which calls lynx,
and run it. This causes lynx to continuously spawn itself to view the object.*
:::

On the other hand, maybe you don't want to use lynx interactively, you just
want to have it convert the `text/html` to `text/plain`, then you can use:

```
text/html; lynx -dump %s | more
```

Perhaps you wish to use lynx to view `text/html` files, and a pager on all
other text formats, then you would use the following:

```
text/html; lynx %s
text/*; more
```

### Secure Use of Mailcap

The interpretation of shell meta-characters embedded in MIME parameters can lead
to security problems in general. NeoMutt tries to quote parameters in expansion
of `%s` syntaxes properly, and avoids risky characters by substituting them, see
the {ref}`$mailcap_sanitize <mailcap-sanitize>` variable.

Although NeoMutt's procedures to invoke programs with mailcap seem to be safe,
there are other applications parsing mailcap, maybe taking less care of it.
Therefore you should pay attention to the following rules:

*Keep the %-expandos away from shell quoting.* Don't quote them with single or
double quotes. NeoMutt does this for you, the right way, as should any other
program which interprets mailcap. Don't put them into backtick expansions. Be
highly careful with eval statements, and avoid them if possible at all. Trying
to fix broken behavior with quotes introduces new leaks — there is no
alternative to correct quoting in the first place.

If you have to use the %-expandos' values in context where you need quoting or
backtick expansions, put that value into a shell variable and reference the
shell variable where necessary, as in the following example (using `$charset`
inside the backtick expansion is safe, since it is not itself subject to any
further expansion):

```
text/test-mailcap-bug; cat %s; copiousoutput; test=charset=%{charset} \
        && test "`echo $charset | tr '[A-Z]' '[a-z]'`" != iso-8859-1
```

### Advanced Mailcap Usage

#### Optional Fields

In addition to the required content-type and view command fields, you can add
semi-colon ";" separated fields to set flags and other options. NeoMutt
recognizes the following optional fields:

- **copiousoutput** — This flag tells NeoMutt that the command passes possibly
  large amounts of text on standard output. This causes NeoMutt to invoke a
  pager (either the internal pager or the external pager defined by the pager
  variable) on the output of the view command. Without this flag, NeoMutt
  assumes that the command is interactive. One could use this to replace the
  pipe to `more` in the `lynx -dump` example in the Basic section:

  ```
  text/html; lynx -dump %s ; copiousoutput
  ```

  This will cause lynx to format the `text/html` output as `text/plain` and
  NeoMutt will use your standard pager to display the results.

  NeoMutt will set the `COLUMNS` environment variable to the width of the
  pager. Some programs make use of this environment variable automatically.
  Others provide a command line argument that can use this to set the output
  width:

  ```
  text/html; lynx -dump -width ${COLUMNS:-80} %s; copiousoutput
  ```

  Note that when using the built-in pager, *only* entries with this flag will
  be considered a handler for a MIME type — all other entries will be ignored.

- **needsterminal** — NeoMutt uses this flag when viewing attachments with
  **auto-view**, in order to decide whether it should honor the
  setting of the {ref}`$wait_key <wait-key>` variable or not. When an
  attachment is viewed using an interactive program, and the corresponding
  mailcap entry has a *needsterminal* flag, NeoMutt will use
  {ref}`$wait_key <wait-key>` and the exit status of the program to decide if
  it will ask you to press a key after the external program has exited. In all
  other situations it will not prompt you for a key.

- **compose=\<command\>** — This flag specifies the command to use to create a
  new attachment of a specific MIME type. NeoMutt supports this from the
  compose menu.

- **composetyped=\<command\>** — This flag specifies the command to use to
  create a new attachment of a specific MIME type. This command differs from
  the compose command in that NeoMutt will expect standard MIME headers on the
  data. This can be used to specify parameters, filename, description, etc.
  for a new attachment. NeoMutt supports this from the compose menu.

- **print=\<command\>** — This flag specifies the command to use to print a
  specific MIME type. NeoMutt supports this from the attachment and compose
  menus.

- **edit=\<command\>** — This flag specifies the command to use to edit a
  specific MIME type. NeoMutt supports this from the compose menu, and also
  uses it to compose new attachments. NeoMutt will default to the defined
  {ref}`$editor <editor>` for text attachments.

- **nametemplate=\<template\>** — This field specifies the format for the file
  denoted by `%s` in the command fields. Certain programs will require a
  certain file extension, for instance, to correctly view a file. For instance,
  lynx will only interpret a file as `text/html` if the file ends in `.html`.
  So, you would specify lynx as a `text/html` viewer with a line in the
  mailcap file like:

  ```
  text/html; lynx %s; nametemplate=%s.html
  ```

- **test=\<command\>** — This field specifies a command to run to test whether
  this mailcap entry should be used. The command is defined with the command
  expansion rules defined in the next section. If the command returns 0, then
  the test passed, and NeoMutt uses this entry. If the command returns
  non-zero, then the test failed, and NeoMutt continues searching for the
  right entry. Note that the content-type must match before NeoMutt performs
  the test. For example:

  ```
  text/html; firefox -remote 'openURL(%s)' ; test=RunningX
  text/html; lynx %s
  ```

  In this example, NeoMutt will run the program `RunningX` which will return 0
  if the X Window manager is running, and non-zero if it isn't. If `RunningX`
  returns 0, then NeoMutt will run firefox to display the `text/html` object.
  If RunningX doesn't return 0, then NeoMutt will go on to the next entry and
  use lynx to display the `text/html` object.

- **x-neomutt-keep** — `x-neomutt-keep` tells NeoMutt to *not* delete the
  temporary file after the program has been run. Using it allows you to control
  the lifespan of the temporary file. Without this option, the file will be
  deleted after {ref}`$timeout <timeout>` seconds.

  ```
  text/html; firefox %s & x-neomutt-keep
  ```

- **x-neomutt-nowrap** — `x-neomutt-nowrap` tells the NeoMutt pager to ignore
  the {ref}`$wrap <wrap>` parameter and to assume the output from the mailcap
  command to already be correctly wrapped.

  ```
  text/html; /usr/local/bin/w3m -s -T text/html -o display_link_number=1 %s; nametemplate=%s.html; copiousoutput; x-neomutt-nowrap;
  ```

#### Search Order

When searching for an entry in the mailcap file, NeoMutt will search for the
most useful entry for its purpose. For instance, if you are attempting to print
an `image/gif`, and you have the following entries in your mailcap file, NeoMutt
will search for an entry with the print command:

```
image/*;        xv %s
image/gif;      ; print=anytopnm %s | pnmtops | lpr; \
                nametemplate=%s.gif
```

NeoMutt will skip the `image/*` entry and use the `image/gif` entry with the
print command.

In addition, you can use this with **auto-view** to denote two
commands for viewing an attachment, one to be viewed automatically, the other to
be viewed interactively from the attachment menu using the `<view-mailcap>`
function (bound to "m" by default). In addition, you can then use the test
feature to determine which viewer to use interactively depending on your
environment.

```
text/html;      firefox -remote 'openURL(%s)' ; test=RunningX
text/html;      lynx %s; nametemplate=%s.html
text/html;      lynx -dump %s; nametemplate=%s.html; copiousoutput
```

For **auto-view**, NeoMutt will choose the third entry because
of the `copiousoutput` tag. For interactive viewing, NeoMutt will run the
program `RunningX` to determine if it should use the first entry. If the
program returns non-zero, NeoMutt will use the second entry for interactive
viewing. The last entry is for inline display in the pager and the
`<view-attach>` function in the attachment menu.

Entries with the `copiousoutput` tag should always be specified as the last one
per type. For non-interactive use, the last entry will then actually be the
first matching one with the tag set. For non-interactive use, only
`copiousoutput`-tagged entries are considered. For interactive use, NeoMutt
ignores this tag and treats all entries equally. Therefore, if not specified
last, all following entries without this tag would never be considered for
`<view-attach>` because the `copiousoutput` before them matched already.

#### Command Expansion

The various commands defined in the mailcap files are passed to the `/bin/sh`
shell using the `system(3)` function. Before the command is passed to
`/bin/sh -c`, it is parsed to expand various special parameters with
information from NeoMutt. The keywords NeoMutt expands are:

- **%s** — As seen in the basic mailcap section, this variable is expanded to a
  filename specified by the calling program. This file contains the body of the
  message to view/print/edit or where the composing program should place the
  results of composition. In addition, the use of this keyword causes NeoMutt
  to not pass the body of the message to the view/print/edit program on stdin.

- **%t** — NeoMutt will expand `%t` to the text representation of the content
  type of the message in the same form as the first parameter of the mailcap
  definition line, i.e. `text/html` or `image/gif`.

- **%{<parameter\>}** — NeoMutt will expand this to the value of the specified
  parameter from the Content-Type: line of the mail message. For instance, if
  your mail message contains:

  ```
  Content-Type: text/plain; charset=iso-8859-1
  ```

  then NeoMutt will expand `%{charset}` to "iso-8859-1". The default metamail
  mailcap file uses this feature to test the charset to spawn an xterm using
  the right charset to view the message.

- **\\%** — This will be replaced by a literal `%`.

NeoMutt does not currently support the `%F` and `%n` keywords specified in
[RFC1524](https://www.rfc-editor.org/rfc/rfc1524.html). The main purpose of these parameters is for multipart messages, which
is handled internally by NeoMutt.

### Example Mailcap Files

This mailcap file is fairly simple and standard:

```bash
# I'm always running X :)
video/*;        xanim %s > /dev/null
image/*;        xv %s > /dev/null
# I'm always running firefox (if my computer had more memory, maybe)
text/html;      firefox -remote 'openURL(%s)'
```

These mailcap files show how to control the lifespan of the temporary file:

```bash
# The `display` program shows an image and doesn't return until the user quits.

# Display an image, but wait for the user to quit the display program.
# When the user quits control will return to NeoMutt.
image/png; display %s;

# Display an image and return to NeoMutt immediately.
image/png; display %s &;

# The file will be automatically deleted after $timeout seconds.
```

```bash
# Some graphical programs return immediately if they're already running.
# We'll add an ampersand (&), just in case they're not.

# View the contents of a 'tar' file.
# The file will be automatically deleted after $timeout seconds.
application/x-tar; file-roller %s &;

# View the contents of a 'tar' file.
# The file will *not* be deleted.
application/x-tar; file-roller %s &; x-neomutt-keep
```

```bash
# Some programs watch any files they have open.
# If NeoMutt deleted the file, the program would close prematurely.

# Use a custom script to manage the file's lifespan.
application/pdf; my-pdf-script.sh %s; x-neomutt-keep
```

This mailcap file shows quite a number of examples:

```bash
# Use xanim to view all videos Xanim produces a header on startup,
# send that to /dev/null so I don't see it
video/*;        xanim %s > /dev/null
# Send html to a running firefox by remote
text/html;      firefox -remote 'openURL(%s)'; test=RunningFirefox
# If I'm not running firefox but I am running X, start firefox on the
# object
text/html;      firefox %s; test=RunningX
# Else use lynx to view it as text
text/html;      lynx %s
# This version would convert the text/html to text/plain
text/html;      lynx -dump %s; copiousoutput
# I use enscript to print text in two columns to a page
text/*;         more %s; print=enscript -2Gr %s
# Firefox adds a flag to tell itself to view jpegs internally
image/jpeg;     xv %s; x-mozilla-flags=internal
# Use xv to view images if I'm running X
# In addition, this uses the \ to extend the line and set my editor
# for images
image/*;        xv %s; test=RunningX; edit=xpaint %s
# Convert images to text using the netpbm tools
image/*;        (anytopnm %s | pnmscale -xysize 80 46 | ppmtopgm | pgmtopbm | \
                pbmtoascii -1x2) 2>&1 ; copiousoutput
# Send excel spreadsheets to my NT box
application/ms-excel;   open.pl %s
```

## MIME Autoview

**Usage:**

```neomuttrc
auto-view mime-type[/mime-subtype] [mime-type[/mime-subtype] ...]
unauto-view { * | mime-type[/mime-subtype] ... }
```

:::{note}
Before 2026-01-13, these commands were called `auto_view` and `unauto_view`.
:::

In addition to explicitly telling NeoMutt to view an attachment with the MIME
viewer defined in the mailcap file from the attachments menu, NeoMutt has
support for automatically viewing MIME attachments while in the pager.

For this to work, you must define a viewer in the mailcap file which uses the
`copiousoutput` option to denote that it is non-interactive. Usually, you also
use the entry to convert the attachment to a text representation which you can
view in the pager.

You then use the `auto-view` configuration command to list the content-types
that you wish to view automatically. For instance, if you set it to:

```neomuttrc
auto-view text/html application/x-gunzip \
  application/postscript image/gif application/x-tar-gz
```

...NeoMutt would try to find corresponding entries for rendering attachments of
these types as text. A corresponding mailcap could look like:

```
text/html;              lynx -dump %s; copiousoutput; nametemplate=%s.html
image/*;                anytopnm %s | pnmscale -xsize 80 -ysize 50 | ppmtopgm | \
                        pgmtopbm | pbmtoascii ; copiousoutput
application/x-gunzip;   gzcat; copiousoutput
application/x-tar-gz;   gunzip -c %s | tar -tf - ; copiousoutput
application/postscript; ps2ascii %s; copiousoutput
```

`unauto-view` can be used to remove previous entries from the `auto-view`
list. This can be used with **message-hook** to autoview
messages based on size, etc. `unauto-view *` will remove all previous entries.

## MIME Multipart/Alternative

**Usage:**

```neomuttrc
alternative-order mime-type[/mime-subtype] [mime-type[/mime-subtype] ...]
unalternative-order { * | mime-type[/mime-subtype] ... }
```

:::{note}
Before 2026-01-13, these commands were called `alternative_order` and
`unalternative_order`.
:::

A `multipart/alternative` email has several parts that represent the same
content in different formats, such as `text/plain` and `text/html`. This kind
of email is heavily used by many modern mail user agents to send HTML messages
which contain an alternative plain text representation. You can read and write
`multipart/alternative` emails in NeoMutt.

### Reading Multipart/Alternative Emails

NeoMutt has some heuristics for determining which attachment of a
`multipart/alternative` type to display:

1. First, NeoMutt will check the `alternative-order` list to determine if one
   of the available types is preferred. It consists of a number of MIME types in
   order, including support for implicit and explicit wildcards. For example:

   ```neomuttrc
   alternative-order text/enriched text/plain text application/postscript image/*
   ```

2. Next, NeoMutt will check if any of the types have a defined
   **auto-view**, and use that.

3. Failing that, NeoMutt will look first for `text/enriched`, followed by
   `text/plain`, and finally `text/html`.

4. As a last attempt, NeoMutt will look for any type it knows how to handle.

To remove a MIME type from the `alternative-order` list, use the
`unalternative-order` command.

### Composing Multipart/Alternative Emails

NeoMutt includes some primitive ability to compose multipart/alternative
emails:

1. In the Compose menu, attach the two (or more) alternatives as usual. For
   example, attach "invitation.html" and then "invitation.txt". (You can
   reorder them using the `<move-up>` (-) and `<move-down>` (+) bindings, and
   edit the descriptions).

2. Tag the attachments that are alternatives, and press the
   `<group-alternatives>` (&) binding to group them together. After this, the
   separate parts will be displayed in a tree structure. Attachments can still
   be edited separately and reordered within the group, but must be ungrouped
   using the `<ungroup-attachment>` (#) binding for more advanced editing
   before tagging and grouping together again as described above.

3. Send the email as usual.

If all the attachments have been grouped and form a single
`multipart/alternative` part then this message will be sent as a
`multipart/alternative` email, otherwise it will be sent as a
`multipart/mixed` email.

Be aware that when sending a `multipart/alternative` email, you have to
manually prepare the alternative parts and attach them. However, you can use
NeoMutt's macro to perform all the operations needed, such that you can compose
a plain text email as usual and turn that into a `multipart/alternative` email
in one single command, with one part being `text/plain` and the other
`text/html`. An example macro which adds an HTML part to the main body of an
email and sends it could be the following:

```neomuttrc
macro compose Y "<first-entry><enter-command>set wait_key=no<enter>\
<pipe-entry>pandoc -o /tmp/neomutt-alternative.html<enter>\
<attach-file>/tmp/neomutt-alternative.html<enter>\
<toggle-unlink><toggle-disposition>\
<tag-entry><first-entry><tag-entry><group-alternatives>\
<enter-command>set wait_key=yes<enter><send-message>" \
"send the message as 'multipart/alternative'"
```

(attachment-searching-and-counting)=
## Attachment Searching and Counting

If you ever lose track of attachments in your mailboxes, NeoMutt's
attachment-counting and -searching support might be for you. You can make your
message index display the number of qualifying attachments in each message, or
search for messages by attachment count. You also can configure what kinds of
attachments qualify for this feature with the `attachments` and `unattachments`
commands.

In order to provide this information, NeoMutt needs to fully MIME-parse all
messages affected first. This can slow down operation especially for remote mail
folders such as IMAP because all messages have to be downloaded first regardless
whether the user really wants to view them or not though using body caching
usually means to download the message just once.

By default, NeoMutt will not search inside `multipart/alternative` containers.
This can be changed via the
{ref}`$count_alternatives <count-alternatives>` configuration variable.

**Usage:**

```neomuttrc
attachments { + | - } disposition mime-type [mime-type ...]
unattachments { + | - } disposition mime-type [mime-type ...]
attachments ?
unattachments *
```

*disposition* is the attachment's Content-Disposition type — either `inline` or
`attachment`. You can abbreviate this to `I` or `A`.

Disposition is prefixed by either a "+" symbol or a "-" symbol. If it's a "+",
you're saying that you want to allow this disposition and MIME type to qualify.
If it's a "-", you're saying that this disposition and MIME type is an exception
to previous "+" rules. There are examples below of how this is useful.

*mime-type* is the MIME type of the attachment you want the command to affect. A
MIME type is always of the format `major/minor`, where `major` describes the
broad category of document you're looking at, and `minor` describes the
specific type within that category. The major part of mime-type must be literal
text (or the special token `*`), but the minor part may be a regular
expression. (Therefore, `*/.*` matches any MIME type.)

The MIME types you give to the `attachments` directive are a kind of pattern.
When you use the `attachments` directive, the patterns you specify are added to
a list. When you use `unattachments`, the pattern is removed from the list. The
patterns are not expanded and matched to specific MIME types at this time —
they're just text in a list. They're only matched when actually evaluating a
message.

Note that the first MIME part is treated slightly differently: It is almost
always the message text. Thus, it is not counted as an attachment if its
disposition is `inline` and it is not a `multipart/*` or `message/*` MIME-type.

:::{admonition} Example: Attachment counting
:class: tip

```neomuttrc
# Removing a pattern from a list removes that pattern literally. It
# does not remove any type matching the pattern.
#
#  attachments   +A */.*
#  attachments   +A image/jpeg
#  unattachments +A */.*
#
# This leaves "attached" image/jpeg files on the allowed attachments
# list. It does not remove all items, as you might expect, because the
# second */.* is not a matching expression at this time.
#
# Remember: "unattachments" only undoes what "attachments" has done!
# It does not trigger any matching on actual messages.
#
# Qualify any MIME part with an "attachment" disposition, EXCEPT for
# text/vcard, text/x-vcard, application/pgp.*, application/pkcs7-.* and
# application/x-pkcs7-.* parts. (PGP and S/MIME parts are already known
# to NeoMutt, and can be searched for with ~g, ~G, and ~k.)
#
# I've added pkcs7/x-pkcs7 to this, since it functions (for S/MIME)
# analogously to PGP signature attachments. S/MIME isn't supported
# in a stock NeoMutt build, but we can still treat it specially here.
#
attachments  +A */.*
attachments  -A text/vcard text/x-vcard
attachments  -A application/pgp.*
attachments  -A application/pkcs7-.* application/x-pkcs7-.*
# Discount all MIME parts with an "inline" disposition, unless they're
# text/plain. (Why inline a text/plain part unless it's external to the
# message flow?)
attachments  +I text/plain
# These two lines make NeoMutt qualify MIME containers. (So, for example,
# a message/rfc822 forward will count as an attachment.) The first
# line is unnecessary if you already have "attach-allow */.*", of
# course. These are off by default! The MIME elements contained
# within a message/* or multipart/* are still examined, even if the
# containers themselves don't qualify.
# Recursion into multipart/alternatives containers is controlled by the
# $count_alternatives setting.

#attachments  +A message/.* multipart/.*
#attachments  +I message/.* multipart/.*
## You probably don't really care to know about deleted attachments.
attachments  -A message/external-body
attachments  -I message/external-body
```
:::

Entering the command `attachments ?` as a command will list your current
settings in neomuttrc format, so that it can be pasted elsewhere.

Entering the command `unattachments *` as a command will clear all attachment
settings.
