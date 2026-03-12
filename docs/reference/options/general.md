---
title: General Options
description: Reference for NeoMutt general configuration variables
keywords: neomutt, configuration, variables, general, settings
---

# General Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

General configuration variables control NeoMutt's core behaviour. These variables
do not belong to a specific feature domain (such as IMAP, PGP, or Sidebar).

(abort-backspace)=
## `$abort_backspace`

- **Type:** boolean
- **Default:** yes

If *set*, hitting backspace against an empty prompt aborts the
prompt.

(abort-key)=
## `$abort_key`

- **Type:** string
- **Default:** "`007`"

Specifies the key that can be used to abort prompts.  The format is the
same as used in "bind" commands.  The default is equivalent to "Ctrl-G".
Note that the specified key should not be used in other bindings, as the
abort operation has higher precedence and the binding will not have the
desired effect.

Example:

```neomuttrc
set abort_key = "<Esc>"
```

Please note that when using <Esc> as the abort key, you may also want to
set the environment variable ESCDELAY to a low value or even 0 which will
reduce the time that ncurses waits to distinguish singular <Esc> key
presses from the start of a terminal escape sequence. The default time is
1000 milliseconds and thus quite noticeable.

(abort-noattach)=
## `$abort_noattach`

- **Type:** quadoption
- **Default:** no

If set to *yes*, when composing messages containing the regular
expression specified by [$abort_noattach_regex](#abort-noattach-regex) and no attachments are
given, composition will be aborted. If set to *no*, composing messages
as such will never be aborted.

Example:

```neomuttrc
set abort_noattach_regex = "\\<attach(|ed|ments?)\\>"
```

(abort-noattach-regex)=
## `$abort_noattach_regex`

- **Type:** regular expression
- **Default:** "`\<(attach|attached|attachments?)\>`"

Specifies a regular expression to match against the body of the message, to
determine if an attachment was mentioned but mistakenly forgotten.  If it
matches, [$abort_noattach](#abort-noattach) will be consulted to determine if message sending
will be aborted.

Like other regular expressions in NeoMutt, the search is case sensitive
if the pattern contains at least one upper case letter, and case
insensitive otherwise.

(abort-nosubject)=
## `$abort_nosubject`

- **Type:** quadoption
- **Default:** ask-yes

If set to *yes*, when composing messages and no subject is given
at the subject prompt, composition will be aborted.  If set to
*no*, composing messages with no subject given at the subject
prompt will never be aborted.

(abort-unmodified)=
## `$abort_unmodified`

- **Type:** quadoption
- **Default:** yes

If set to *yes*, composition will automatically abort after
editing the message body if no changes are made to the file (this
check only happens after the *first* edit of the file).  When set
to *no*, composition will never be aborted.

(account-command)=
## `$account_command`

- **Type:** command
- **Default:** (empty)

If set, this command is used to retrieve account credentials. The command
is invoked passing a number of *--key value* arguments with the
specifics of the account to lookup. The command writes to standard output a
number of *key: value* lines. Currently supported arguments are
*--hostname*, *--username*, and *--type*, where type can be
any of *imap*, *imaps*, *pop*, *pops*, *smtp*,
*smtps*, *nntp*, and *nntps*. Currently supported output lines
are *login*, *username*, and *password*.

(allow-8bit)=
## `$allow_8bit`

- **Type:** boolean
- **Default:** yes

Controls whether 8-bit data is converted to 7-bit using either Quoted-
Printable or Base64 encoding when sending mail.

(allow-ansi)=
## `$allow_ansi`

- **Type:** boolean
- **Default:** no

Controls whether ANSI color codes in messages (and color tags in
rich text messages) are to be interpreted.
Messages containing these codes are rare, but if this option is *set*,
their text will be colored accordingly. Note that this may override
your color choices, and even present a security problem, since a
message could include a line like

```
[-- PGP output follows ...
```

and give it the same color as your attachment color (see also
[$crypt_timestamp](#crypt-timestamp)).

(arrow-cursor)=
## `$arrow_cursor`

- **Type:** boolean
- **Default:** no

When *set*, an arrow ("->") will be used to indicate the current entry
in menus instead of highlighting the whole line.  On slow network or modem
links this will make response faster because there is less that has to
be redrawn on the screen when moving to the next or previous entries
in the menu.

(arrow-string)=
## `$arrow_string`

- **Type:** string
- **Default:** "`->`"

Specifies the string of arrow_cursor when arrow_cursor enabled.

(ascii-chars)=
## `$ascii_chars`

- **Type:** boolean
- **Default:** no

If *set*, NeoMutt will use plain ASCII characters when displaying thread
and attachment trees, instead of the default *ACS* characters.

(ask-bcc)=
## `$ask_bcc`

- **Type:** boolean
- **Default:** no

If *set*, NeoMutt will prompt you for blind-carbon-copy (Bcc) recipients
before editing an outgoing message.

(ask-cc)=
## `$ask_cc`

- **Type:** boolean
- **Default:** no

If *set*, NeoMutt will prompt you for carbon-copy (Cc) recipients before
editing the body of an outgoing message.

(ask-followup-to)=
## `$ask_followup_to`

- **Type:** boolean
- **Default:** no

If set, NeoMutt will prompt you for follow-up groups before editing
the body of an outgoing message.

(ask-x-comment-to)=
## `$ask_x_comment_to`

- **Type:** boolean
- **Default:** no

If set, NeoMutt will prompt you for x-comment-to field before editing
the body of an outgoing message.

(assumed-charset)=
## `$assumed_charset`

- **Type:** string list
- **Default:** (empty)

This variable is a colon-separated list of character encoding
schemes for messages without character encoding indication.
Header field values and message body content without character encoding
indication would be assumed that they are written in one of this list.
By default, all the header fields and message body without any charset
indication are assumed to be in "us-ascii".

For example, Japanese users might prefer this:

```
set assumed_charset="iso-2022-jp:euc-jp:shift_jis:utf-8"
```

However, only the first content is valid for the message body.

(attribution-intro)=
## `$attribution_intro`

- **Type:** string
- **Default:** "`On %d, %n wrote:`"

This is the string that will precede a replied-to message which is
quoted in the main body of the reply (this is the case when [$include](#include) is
set).

For a full listing of defined `printf(3)`-like sequences see the section
on [$index_format](#index-format).  See also [$attribution_locale](#attribution-locale).

(attribution-locale)=
## `$attribution_locale`

- **Type:** string
- **Default:** (empty)

The locale used by `strftime(3)` to format dates in the
attribution strings.  Valid values are the strings your system
accepts for the locale environment variable `$LC_TIME`.

This variable is to allow the attribution date format to be
customized by recipient or folder using hooks.  By default, NeoMutt
will use your locale environment, so there is no need to set
this except to override that default.

Affected variables are: [$attribution_intro](#attribution-intro), [$attribution_trailer](#attribution-trailer),
[$forward_attribution_intro](#forward-attribution-intro), [$forward_attribution_trailer](#forward-attribution-trailer), [$indent_string](#indent-string).

(attribution-trailer)=
## `$attribution_trailer`

- **Type:** string
- **Default:** (empty)

Similar to the [$attribution_intro](#attribution-intro) variable, this is the string that will
come after a replied-to message which is quoted in the main body of the reply
(this is the case when [$include](#include) is set).

For a full listing of defined `printf(3)`-like sequences see the section
on [$index_format](#index-format).  See also [$attribution_locale](#attribution-locale).

(auto-edit)=
## `$auto_edit`

- **Type:** boolean
- **Default:** no

When *set* along with [$edit_headers](#edit-headers), NeoMutt will skip the initial
send-menu (prompting for subject and recipients) and allow you to
immediately begin editing the body of your
message.  The send-menu may still be accessed once you have finished
editing the body of your message.

**Note:** when this option is *set*, you can't use send-hooks that
depend on the recipients when composing a new (non-reply) message, as the
initial list of recipients is empty.

Also see [$fast_reply](#fast-reply).

(auto-subscribe)=
## `$auto_subscribe`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt assumes the presence of a List-Post header
means the recipient is subscribed to the list.  Unless the mailing list
is in the "unsubscribe" or "unlist" lists, it will be added
to the "`subscribe`" list.  Parsing and checking these things slows
header reading down, so this option is disabled by default.

(auto-tag)=
## `$auto_tag`

- **Type:** boolean
- **Default:** no

When *set*, functions in the *index* menu which affect a message
will be applied to all tagged messages (if there are any).  When
unset, you must first use the `<tag-prefix>` function (bound to ";"
by default) to make the next function apply to all tagged messages.

(general-autocrypt)=
## `$autocrypt`

- **Type:** boolean
- **Default:** no

When *set*, enables autocrypt, which provides
passive encryption protection with keys exchanged via headers.
See "**Autocrypt**" for more details.
(Autocrypt only)

(beep)=
## `$beep`

- **Type:** boolean
- **Default:** yes

When this variable is *set*, NeoMutt will beep when an error occurs.

(beep-new)=
## `$beep_new`

- **Type:** boolean
- **Default:** no

When this variable is *set*, NeoMutt will beep whenever it prints a
message notifying you of new mail. This is independent of the setting of the
[$beep](#beep) variable.

(bounce)=
## `$bounce`

- **Type:** quadoption
- **Default:** ask-yes

Controls whether you will be asked to confirm bouncing messages.
If set to *yes* you don't get asked if you want to bounce a
message. Setting this variable to *no* is not generally useful,
and thus not recommended, because you are unable to bounce messages.

(bounce-delivered)=
## `$bounce_delivered`

- **Type:** boolean
- **Default:** yes

When this variable is *set*, NeoMutt will include Delivered-To headers
when bouncing messages. Postfix users may wish to *unset* this variable.

(braille-friendly)=
## `$braille_friendly`

- **Type:** boolean
- **Default:** no

When this variable is *set*, NeoMutt will place the cursor at the
beginning of the current line in menus, even when the [$arrow_cursor](#arrow-cursor) variable
is *unset*, making it easier for blind persons using Braille displays to
follow these menus. The option is *unset* by default because many visual
terminals don't permit making the cursor invisible.

(catchup-newsgroup)=
## `$catchup_newsgroup`

- **Type:** quadoption
- **Default:** ask-yes

If this variable is *set*, NeoMutt will mark all articles in newsgroup
as read when you quit the newsgroup (catchup newsgroup).

(certificate-file)=
## `$certificate_file`

- **Type:** path
- **Default:** "`~/.mutt_certificates`"

This variable specifies the file where the certificates you trust
are saved. When an unknown certificate is encountered, you are asked
if you accept it or not. If you accept it, the certificate can also
be saved in this file and further connections are automatically
accepted.

You can also manually add CA certificates in this file. Any server
certificate that is signed with one of these CA certificates is
also automatically accepted.

Example:

```
set certificate_file=~/.neomutt/certificates
```

(OpenSSL and GnuTLS only)

(change-folder-next)=
## `$change_folder_next`

- **Type:** boolean
- **Default:** no

When this variable is *set*, the `<change-folder>` function
mailbox suggestion will start at the next folder in your "`mailboxes`"
list, instead of starting at the first folder in the list.

(charset)=
## `$charset`

- **Type:** string
- **Default:** (empty)

Character set your terminal uses to display and enter textual data.
It is also the fallback for [$send_charset](#send-charset).

Upon startup NeoMutt tries to derive this value from environment variables
such as `$LC_CTYPE` or `$LANG`.

**Note:** It should only be set in case NeoMutt isn't able to determine the
character set used correctly.

(check-mbox-size)=
## `$check_mbox_size`

- **Type:** boolean
- **Default:** no

When this variable is *set*, NeoMutt will use file size attribute instead
of access time when checking for new mail in mbox and mmdf folders.

This variable is *unset* by default and should only be enabled when
new mail detection for these folder types is unreliable or doesn't work.

Note that enabling this variable should happen before any "`mailboxes`"
directives occur in configuration files regarding mbox or mmdf folders
because NeoMutt needs to determine the initial new mail status of such a
mailbox by performing a fast mailbox scan when it is defined.
Afterwards the new mail status is tracked by file size changes.

(check-new)=
## `$check_new`

- **Type:** boolean
- **Default:** yes

**Note:** this option only affects *maildir* and *MH* style
mailboxes.

When *set*, NeoMutt will check for new mail delivered while the
mailbox is open.  Especially with MH mailboxes, this operation can
take quite some time since it involves scanning the directory and
checking each file to see if it has already been looked at.  If
this variable is *unset*, no check for new mail is performed
while the mailbox is open.

(collapse-all)=
## `$collapse_all`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will collapse all threads when entering a folder.

(collapse-flagged)=
## `$collapse_flagged`

- **Type:** boolean
- **Default:** yes

When *unset*, NeoMutt will not collapse a thread if it contains any
flagged messages.

(collapse-unread)=
## `$collapse_unread`

- **Type:** boolean
- **Default:** yes

When *unset*, NeoMutt will not collapse a thread if it contains any
unread messages.

(color-directcolor)=
## `$color_directcolor`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will use and allow 24-bit colours (aka truecolor aka
directcolor).  For colours to work properly support from the terminal is
required as well as a properly set TERM environment variable advertising the
terminals directcolor capability, e.g. "TERM=xterm-direct".

NeoMutt tries to detect whether the terminal supports 24-bit colours and
enables this variable if it does.  If this fails for some reason, you can
force 24-bit colours by setting this variable manually.  You may also try to
force a certain TERM environment variable by starting NeoMutt from
a terminal as follows (this results in wrong colours if the terminal does
not implement directcolors):

```
TERM=xterm-direct neomutt
```

Note: This variable must be set before using any `color` commands.

(config-charset)=
## `$config_charset`

- **Type:** string
- **Default:** (empty)

When defined, NeoMutt will recode commands in rc files from this
encoding to the current character set as specified by [$charset](#charset)
and aliases written to [$alias_file](#alias-file) from the current character set.

Please note that if setting [$charset](#charset) it must be done before
setting [$config_charset](#config-charset).

Recoding should be avoided as it may render unconvertible
characters as question marks which can lead to undesired
side effects (for example in regular expressions).

(confirm-append)=
## `$confirm_append`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will prompt for confirmation when appending messages
to an existing mailbox.

(confirm-create)=
## `$confirm_create`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will prompt for confirmation when saving messages to
a mailbox which does not yet exist before creating it.

(confirm-empty-to)=
## `$confirm_empty_to`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will prompt for confirmation when sending an e-mail
with an empty To recipients list.

(content-type)=
## `$content_type`

- **Type:** string
- **Default:** "`text/plain`"

Sets the default Content-Type for the body of newly composed messages.

(copy)=
## `$copy`

- **Type:** quadoption
- **Default:** yes

This variable controls whether or not copies of your outgoing messages
will be saved for later references.  Also see [$record](#record),
[$save_name](#save-name), [$force_name](#force-name) and "`fcc-hook`".

(copy-decode-weed)=
## `$copy_decode_weed`

- **Type:** boolean
- **Default:** no

Controls whether NeoMutt will weed headers when invoking the
`<decode-copy>` or `<decode-save>` functions.

(count-alternatives)=
## `$count_alternatives`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will recurse inside multipart/alternatives while
performing attachment searching and counting(see `attachments`).

Traditionally, multipart/alternative parts have simply represented
different encodings of the main content of the email.  Unfortunately,
some mail clients have started to place email attachments inside
one of alternatives.  Setting this will allow NeoMutt to find
and count matching attachments hidden there, and include them
in the index via %X or through ~X pattern matching.

(date-format)=
## `$date_format`

- **Type:** string
- **Default:** "`!%a, %b %d, %Y at %I:%M:%S%p %Z`"

Instead of using [$date_format](#date-format) it is encouraged to use "%[fmt]"
directly in the corresponding format strings, where "fmt" is the
value of [$date_format](#date-format).  This allows for a more fine grained control
of the different menu needs.

This variable controls the format of the date printed by the "%d"
sequence in [$index_format](#index-format).  This is passed to the `strftime(3)`
function to process the date, see the man page for the proper syntax.

Unless the first character in the string is a bang ("!"), the month
and week day names are expanded according to the locale.
If the first character in the string is a
bang, the bang is discarded, and the month and week day names in the
rest of the string are expanded in the *C* locale (that is in US
English).

Format strings using this variable are:

UI: [$folder_format](#folder-format), [$index_format](#index-format), [$mailbox_folder_format](#mailbox-folder-format),
[$message_format](#message-format)

Composing: [$attribution_intro](#attribution-intro), [$forward_attribution_intro](#forward-attribution-intro),
[$forward_attribution_trailer](#forward-attribution-trailer), [$forward_format](#forward-format), [$indent_string](#indent-string).

(debug-file)=
## `$debug_file`

- **Type:** path
- **Default:** "`~/.neomuttdebug`"

Debug logging is controlled by the variables `[$debug_file](#debug-file)` and
`[$debug_level](#debug-level)`. `[$debug_file](#debug-file)` specifies the root of the filename.
NeoMutt will add "0" to the end. Each time NeoMutt is run with logging
enabled, the log files are rotated. A maximum of five log files are kept,
numbered 0 (most recent) to 4 (oldest).

This option can be enabled on the command line, "neomutt -l mylog"

See also: `[$debug_level](#debug-level)`

(debug-level)=
## `$debug_level`

- **Type:** number
- **Default:** 0

Debug logging is controlled by the variables `[$debug_file](#debug-file)` and
`[$debug_level](#debug-level)`.

The debug level controls how much information is saved to the log file. If
you have a problem with NeoMutt, then enabling logging may help find the
cause. Levels 1-3 will usually provide enough information for writing a bug
report. Levels 4,5 will be extremely verbose.

Warning: Logging at high levels may save private information to the file.

This option can be enabled on the command line, "neomutt -d 2"

See also: `[$debug_file](#debug-file)`

(default-hook)=
## `$default_hook`

- **Type:** string
- **Default:** "`~f %s !~P | (~P ~C %s)`"

This variable controls how some hooks are interpreted if their pattern is a
plain string or a regex. i.e. they don't contain a pattern, like `~f`

The hooks are: `fcc-hook`, `fcc-save-hook`, `index-format-hook`, `message-hook`,
`reply-hook`, `save-hook`, `send-hook` and `send2-hook`.

The hooks are expanded when they are declared, so a hook will be interpreted
according to the value of this variable at the time the hook is declared.

The default value matches if the message is either from a user matching the
regular expression given, or if it is from you (if the from address matches
"`alternates`") and is to or cc'ed to a user matching the given regular
expression.

(delete)=
## `$delete`

- **Type:** quadoption
- **Default:** ask-yes

Controls whether or not messages are really deleted when closing or
synchronizing a mailbox.  If set to *yes*, messages marked for
deleting will automatically be purged without prompting.  If set to
*no*, messages marked for deletion will be kept in the mailbox.

(delete-untag)=
## `$delete_untag`

- **Type:** boolean
- **Default:** yes

If this option is *set*, NeoMutt will untag messages when marking them
for deletion.  This applies when you either explicitly delete a message,
or when you save it to another folder.

(devel-security)=
## `$devel_security`

- **Type:** boolean
- **Default:** no

If this option is *set*, NeoMutt will enable the **Security**
development features. See:
[https://github.com/neomutt/neomutt/discussions/4251](https://github.com/neomutt/neomutt/discussions/4251)

(digest-collapse)=
## `$digest_collapse`

- **Type:** boolean
- **Default:** yes

If this option is *set*, NeoMutt's received-attachments menu will not
show the subparts of individual messages in a multipart/digest. To see these
subparts, press "v" on that menu.

(display-filter)=
## `$display_filter`

- **Type:** command
- **Default:** (empty)

When set, specifies a command used to filter messages.  When a message
is viewed it is passed as standard input to [$display_filter](#display-filter), and the
filtered message is read from the standard output.

When preparing the message, NeoMutt inserts some escape sequences into the
text.  They are of the form: `<esc>]9;XXX<bel>` where "XXX" is a random
64-bit number.

If these escape sequences interfere with your filter, they can be removed
using a tool like `ansifilter` or
`sed 's/^\x1b]9;[0-9]\+\x7//'`

If they are removed, then PGP and MIME headers will no longer be coloured.
This can be fixed by adding this to your config:
`color body magenta default '^\[-- .* --\]$'`.

(dsn-notify)=
## `$dsn_notify`

- **Type:** string
- **Default:** (empty)

This variable sets the request for when notification is returned.  The
string consists of a comma separated list (no spaces!) of one or more
of the following: *never*, to never request notification,
*failure*, to request notification on transmission failure,
*delay*, to be notified of message delays, *success*, to be
notified of successful transmission.

Example:

```
set dsn_notify="failure,delay"
```

**Note:** when using [$sendmail](#sendmail) for delivery, you should not enable this
unless you are either using Sendmail 8.8.x or greater or a MTA providing a
`sendmail(1)`-compatible interface supporting the `-N` option for
DSN. For SMTP delivery, DSN support is auto-detected so that it depends on
the server whether DSN will be used or not.

(dsn-return)=
## `$dsn_return`

- **Type:** string
- **Default:** (empty)

This variable controls how much of your message is returned in DSN
messages.  It may be set to either *hdrs* to return just the
message header, or *full* to return the full message.

Example:

```
set dsn_return=hdrs
```

**Note:** when using [$sendmail](#sendmail) for delivery, you should not enable this
unless you are either using Sendmail 8.8.x or greater or a MTA providing a
`sendmail(1)`-compatible interface supporting the `-R` option for
DSN. For SMTP delivery, DSN support is auto-detected so that it depends on
the server whether DSN will be used or not.

(duplicate-threads)=
## `$duplicate_threads`

- **Type:** boolean
- **Default:** yes

This variable controls whether NeoMutt, when `$sort` is set to *threads*,
threads messages with the same Message-Id together. If it is *set*, it
will indicate that it thinks they are duplicates of each other with an equals
sign in the thread tree.

(edit-headers)=
## `$edit_headers`

- **Type:** boolean
- **Default:** no

This option allows you to edit the header of your outgoing messages
along with the body of your message.

Although the compose menu may have localized header labels, the
labels passed to your editor will be standard [RFC2822](https://www.rfc-editor.org/rfc/rfc2822.html) headers,
(e.g. To:, Cc:, Subject:).  Headers added in your editor must
also be [RFC2822](https://www.rfc-editor.org/rfc/rfc2822.html) headers, or one of the pseudo headers listed in
"`edit-header`".  NeoMutt will not understand localized header
labels, just as it would not when parsing an actual email.

**Note** that changes made to the References: and Date: headers are
ignored for interoperability reasons.

(editor)=
## `$editor`

- **Type:** command
- **Default:** (empty)

This variable specifies which editor is used by NeoMutt. It defaults to the
value of the `$VISUAL`, or `$EDITOR`, environment variable, or to
the string "vi" if neither of those are set.

The `[$editor](#editor)` string may contain a *%s* escape, which will be
replaced by the name of the file to be edited. If the *%s* escape does
not appear in `[$editor](#editor)`, a space and the name to be edited are appended.

The resulting string is then executed by running

```neomuttrc
sh -c 'string'
```

where *string* is the expansion of `[$editor](#editor)` described above.

(empty-subject)=
## `$empty_subject`

- **Type:** string
- **Default:** "`Re: your mail`"

This variable specifies the subject to be used when replying to an email
with an empty subject.  It defaults to "Re: your mail".

(encode-from)=
## `$encode_from`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will quoted-printable encode messages when they
contain the string "From " (note the trailing space) in the beginning of a
line. This is useful to avoid the tampering certain mail delivery and
transport agents tend to do with messages (in order to prevent tools from
misinterpreting the line as a mbox message separator).

(entropy-file)=
## `$entropy_file`

- **Type:** path
- **Default:** (empty)

The file which includes random data that is used to initialize SSL
library functions. (OpenSSL only)

(envelope-from-address)=
## `$envelope_from_address`

- **Type:** e-mail address
- **Default:** (empty)

Manually sets the *envelope* sender for outgoing messages.
This value is ignored if [$use_envelope_from](#use-envelope-from) is *unset*.

(external-search-command)=
## `$external_search_command`

- **Type:** command
- **Default:** (empty)

If set, contains the name of the external program used by "~I" patterns.
This will usually be a wrapper script around mairix, mu, or similar
indexers other than notmuch (for which there is optional special support).

Here is an example how it works.  Let's assume [$external_search_command](#external-search-command)
is set to "mairix_filter", and mairix_filter is a script which
runs the old but well loved mairix indexer with the arguments
given to mairix_filter, in the "raw" mode of mairix, producing
on the standard output a list of Message-IDs, one per line.

If possible, it also filters down the results coming from mairix
such that only messages in the current folder remain.  It can do
this because it gets a hidden first argument which is the path
to the folder.
(This can be the type of clean and simple script called a *one-liner*.)

Now if NeoMutt gets a limit or tag command followed by the pattern
"~I '-t s:bleeping='", mairix_filter runs mairix with the
arguments from inside the quotes (the quotes are needed because
of the space after "-t"), mairix finds all messages with
"bleeping" in the Subject plus all messages sharing threads
with these and outputs their file names, and mairix_filter
translates the file names into Message-IDs.  Finally, NeoMutt
reads the Message-IDs and targets the matching messages with the
command given to it.

You, the user, still have to rewrite the mairix_filter script to
match the behavior of your indexer, but this should help users
of indexers other than notmuch to integrate them cleanly with NeoMutt.

(fast-reply)=
## `$fast_reply`

- **Type:** boolean
- **Default:** no

When *set*, the initial prompt for recipients (to, cc, bcc) and subject
are skipped when the relevant information is already provided. These cases
include replying to messages and passing the relevant command line arguments.
The initial prompt for recipients is also skipped when composing a new
message to the current message sender, while the initial prompt for subject
is also skipped when forwarding messages.

**Note:** this variable has no effect when the [$auto_edit](#auto-edit)
variable is *set*.

See also: [$auto_edit](#auto-edit), [$edit_headers](#edit-headers), [$ask_cc](#ask-cc), [$ask_bcc](#ask-bcc)

(fcc-attach)=
## `$fcc_attach`

- **Type:** quadoption
- **Default:** yes

This variable controls whether or not attachments on outgoing messages
are saved along with the main body of your message.

Note: [$fcc_before_send](#fcc-before-send) forces the default (set) behavior of this option.

(fcc-before-send)=
## `$fcc_before_send`

- **Type:** boolean
- **Default:** no

When this variable is *set*, FCCs will occur before sending
the message.  Before sending, the message cannot be manipulated,
so it will be stored the exact same as sent:
[$fcc_attach](#fcc-attach) and [$fcc_clear](#fcc-clear) will be ignored (using their default
values).

When *unset*, the default, FCCs will occur after sending.
Variables [$fcc_attach](#fcc-attach) and [$fcc_clear](#fcc-clear) will be respected, allowing
it to be stored without attachments or encryption/signing if
desired.

(fcc-clear)=
## `$fcc_clear`

- **Type:** boolean
- **Default:** no

When this variable is *set*, FCCs will be stored unencrypted and
unsigned, even when the actual message is encrypted and/or
signed.

Note: [$fcc_before_send](#fcc-before-send) forces the default (unset) behavior of this option.
(PGP only)

See also [$pgp_self_encrypt](#pgp-self-encrypt), [$smime_self_encrypt](#smime-self-encrypt)

(flag-chars)=
## `$flag_chars`

- **Type:** character string
- **Default:** "`*!DdrONon- `"

Controls the characters used in several flags.

| **Character** | **Default** | **Description** |
| --- | --- | --- |
| 1 | * | The mail is tagged. |
| 2 | ! | The mail is flagged as important. |
| 3 | D | The mail is marked for deletion. |
| 4 | d | The mail has attachments marked for deletion. |
| 5 | r | The mail has been replied to. |
| 6 | O | The mail is Old (Unread but seen). |
| 7 | N | The mail is New (Unread but not seen). |
| 8 | o | The mail thread is Old (Unread but seen). |
| 9 | n | The mail thread is New (Unread but not seen). |
| 10 | - | The mail is read - %S expando. |
| 11 | <space> | The mail is read - %Z expando. |

(flag-safe)=
## `$flag_safe`

- **Type:** boolean
- **Default:** no

If set, flagged messages can't be deleted.

(folder)=
## `$folder`

- **Type:** mailbox
- **Default:** "`~/Mail`"

Specifies the default location of your mailboxes.  A "+" or "=" at the
beginning of a pathname will be expanded to the value of this
variable.  Note that if you change this variable (from the default)
value you need to make sure that the assignment occurs *before*
you use "+" or "=" for any other variables since expansion takes place
when handling the "`mailboxes`" command.

(folder-format)=
## `$folder_format`

- **Type:** string
- **Default:** "`%2C %t %N %F %2l %-8.8u %-8.8g %8s %d %i`"

This variable allows you to customize the file browser display to your
personal taste.  This string is similar to [$index_format](#index-format), but has
its own set of `printf(3)`-like sequences:

| **Short** | **Long Name** | **Description** |
| --- | --- | --- |
| `%a` | `%{notify}` | Alert: 1 if user is notified of new mail |
| `%C` | `%{number}` | Current file number |
| `%D` | `%{date}` | Date/time folder was last modified using [$date_format](#date-format). |
|  |  | It is recommended to use `%[fmt]` instead, where `fmt` is the value of [$date_format](#date-format). |
| `%d` | `%{date-format}` | Date/time folder was last modified |
| `%F` | `%{file-mode}` | File permissions |
| `%f` | `%{filename}` | Filename (`/` is appended to directory names, |
|  |  | `@` to symbolic links and `*` to executable files) |
| `%g` | `%{file-group}` | Group name (or numeric gid, if missing) |
| `%i` | `%{description}` | Description of the folder |
| `%l` | `%{hard-links}` | Number of hard links |
| `%m` | `%{message-count}` | Number of messages in the mailbox |
| `%N` | `%{new-mail}` | `N` if mailbox has new mail, ` ` (space) otherwise |
| `%n` | `%{unread-count}` | Number of unread messages in the mailbox |
| `%p` | `%{poll}` | Poll: 1 if Mailbox is checked for new mail |
| `%s` | `%{file-size}` | Size in bytes (see **Size Format**) |
| `%t` | `%{tagged}` | `*` if the file is tagged, blank otherwise |
| `%u` | `%{file-owner}` | Owner name (or numeric uid, if missing) |
| `%[fmt]` |  | Date/time folder was last modified using an `strftime(3)` expression |
| `%*X` | `%{padding-soft}` | Soft-fill with character `X` as pad |
| `%>X` | `%{padding-hard}` | Right justify the rest of the string and pad with character `X` |
| `%|X` | `%{padding-eol}` | Pad to the end of the line with character `X` |

For an explanation of "soft-fill", see the [$index_format](#index-format) documentation.

* = can be optionally printed if nonzero

%m, %n, and %N only work for monitored mailboxes.
%m requires [$mail_check_stats](#mail-check-stats) to be set.
%n requires [$mail_check_stats](#mail-check-stats) to be set (except for IMAP mailboxes).

(followup-to)=
## `$followup_to`

- **Type:** boolean
- **Default:** yes

Controls whether or not the "Mail-Followup-To:" header field is
generated when sending mail.  When *set*, NeoMutt will generate this
field when you are replying to a known mailing list, specified with
the "`subscribe`" or "`lists`" commands.

This field has two purposes.  First, preventing you from
receiving duplicate copies of replies to messages which you send
to mailing lists, and second, ensuring that you do get a reply
separately for any messages sent to known lists to which you are
not subscribed.

The header will contain only the list's address
for subscribed lists, and both the list address and your own
email address for unsubscribed lists.  Without this header, a
group reply to your message sent to a subscribed list will be
sent to both the list and your address, resulting in two copies
of the same email for you.

(followup-to-poster)=
## `$followup_to_poster`

- **Type:** quadoption
- **Default:** ask-yes

If this variable is *set* and the keyword "poster" is present in
*Followup-To* header, follow-up to newsgroup function is not
permitted.  The message will be mailed to the submitter of the
message via mail.

(force-name)=
## `$force_name`

- **Type:** boolean
- **Default:** no

This variable is similar to [$save_name](#save-name), except that NeoMutt will
store a copy of your outgoing message by the username of the address
you are sending to even if that mailbox does not exist.

Also see the [$record](#record) variable.

(from)=
## `$from`

- **Type:** e-mail address
- **Default:** (empty)

When *set*, this variable contains a default "from" address.  It
can be overridden using "`my-header`" (including from a "`send-hook`") and
[$reverse_name](#reverse-name).  This variable is ignored if [$use_from](#use-from) is *unset*.

If not specified, then it may be read from the environment variable
`$EMAIL`.

(from-chars)=
## `$from_chars`

- **Type:** character string
- **Default:** (empty)

Controls the character used to prefix the %F and %L fields in the
index.

| **Character** | **Description** |
| --- | --- |
| 1 | Mail is written by you and has a To address, or has a known mailing list in the To address. |
| 2 | Mail is written by you and has a Cc address, or has a known mailing list in the Cc address. |
| 3 | Mail is written by you and has a Bcc address. |
| 4 | All remaining cases. |

If this is empty or unset (default), the traditional long "To ",
"Cc " and "Bcc " prefixes are used.  If set but too short to
include a character for a particular case, a single space will be
prepended to the field.  To prevent any prefix at all from being
added in a particular case, use the special value CR (aka ^M)
for the corresponding character.

This slightly odd interface is necessitated by NeoMutt's handling of
string variables; one can't tell a variable that is unset from one
that is set to the empty string.

(gecos-mask)=
## `$gecos_mask`

- **Type:** regular expression
- **Default:** "`^[^,]*`"

A regular expression used by NeoMutt to parse the GECOS field of a password
entry when expanding the alias.  The default value
will return the string up to the first "," encountered.
If the GECOS field contains a string like "lastname, firstname" then you
should set it to "`.*`".

This can be useful if you see the following behavior: you address an e-mail
to user ID "stevef" whose full name is "Steve Franklin". If NeoMutt expands
"stevef" to '"Franklin" stevef@foo.bar' then you should set the [$gecos_mask](#gecos-mask)
to a regular expression that will match the whole name so NeoMutt will expand
"Franklin" to "Franklin, Steve".

(greeting)=
## `$greeting`

- **Type:** string
- **Default:** (empty)

When set, this is the string that will precede every message as a
greeting phrase to the recipients.

"Format strings" are similar to the strings used in the "C"
function printf to format output (see the man page for more detail).
The following sequences are defined in NeoMutt:

| **Short** | **Long Name** | **Description** |
| --- | --- | --- |
| `%n` | `%{real-name}` | Recipient's real name |
| `%u` | `%{user-name}` | User (login) name of recipient |
| `%v` | `%{first-name}` | First name of recipient |

(group-index-format)=
## `$group_index_format`

- **Type:** string
- **Default:** "`%4C %M%N %5s  %-45.45f %d`"

This variable allows you to customize the newsgroup browser display to
your personal taste.  This string is similar to "[index_format](#index-format)", but
has its own set of printf()-like sequences:

| **Short** | **Long Name** | **Description** |
| --- | --- | --- |
| `%a` | `%{notify}` | Alert: 1 if user is notified of new mail |
| `%C` | `%{number}` | Current newsgroup number |
| `%d` | `%{description}` | Description of newsgroup (becomes from server) |
| `%f` | `%{newsgroup}` | Newsgroup name |
| `%M` | `%{flags}` | `-` if newsgroup not allowed for direct post (moderated for example) |
| `%N` | `%{flags2}` | `N` if newsgroup is new, `u` if unsubscribed, ` ` (space) otherwise |
| `%n` | `%{new-count}` | Number of new articles in newsgroup |
| `%p` | `%{poll}` | Poll: 1 if Mailbox is checked for new mail |
| `%s` | `%{unread-count}` | Number of unread articles in newsgroup |
| `%*X` | `%{padding-soft}` | Soft-fill with character `X` as pad |
| `%>X` | `%{padding-hard}` | Right justify the rest of the string and pad with character `X` |
| `%|X` | `%{padding-eol}` | Pad to the end of the line with character `X` |

(hdrs)=
## `$hdrs`

- **Type:** boolean
- **Default:** yes

When *unset*, the header fields normally added by the "`my-header`"
command are not created.  This variable *must* be unset before
composing a new message or replying in order to take effect.  If *set*,
the user defined header fields are added to every new message.

(general-header)=
## `$header`

- **Type:** boolean
- **Default:** no

When *set*, this variable causes NeoMutt to include the header
of the message you are replying to into the edit buffer.
The [$weed](#weed) setting applies.

(help)=
## `$help`

- **Type:** boolean
- **Default:** yes

When *set*, help lines describing the bindings for the major functions
provided by each menu are displayed on the first line of the screen.

**Note:** The binding will not be displayed correctly if the
function is bound to a sequence rather than a single keystroke.  Also,
the help line may not be updated if a binding is changed while NeoMutt is
running.  Since this variable is primarily aimed at new users, neither
of these should present a major problem.

(hidden-host)=
## `$hidden_host`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will skip the host name part of [$hostname](#hostname) variable
when adding the domain part to addresses.

(hidden-tags)=
## `$hidden_tags`

- **Type:** string list
- **Default:** "`unread,draft,flagged,passed,replied,attachment,signed,encrypted`"

This variable specifies a list of comma-separated private notmuch/imap tags
which should not be printed on screen.

(hide-limited)=
## `$hide_limited`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will not show the presence of messages that are
hidden by limiting, in the thread tree.

(hide-missing)=
## `$hide_missing`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will not show the presence of missing messages in the
thread tree.

(hide-thread-subject)=
## `$hide_thread_subject`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will not show the subject of messages in the thread
tree that have the same subject as their parent or closest previously
displayed sibling.

(hide-top-limited)=
## `$hide_top_limited`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will not show the presence of messages that are
hidden by limiting, at the top of threads in the thread tree. Note that when
[$hide_limited](#hide-limited) is *set*, this option will have no effect.

(hide-top-missing)=
## `$hide_top_missing`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will not show the presence of missing messages at the
top of threads in the thread tree.  Note that when [$hide_missing](#hide-missing) is
*set*, this option will have no effect.

(general-history)=
## `$history`

- **Type:** number
- **Default:** 10

This variable controls the size (in number of strings remembered) of
the string history buffer per category. The buffer is cleared each time the
variable is set.

Note that strings (e.g. commands) starting with a space are never recorded
in the history.  This is for example useful to prevent leaking sensitive
information into the history file or for one off tests.

Also note that a string is not added to the history if it exactly matches
its immediate predecessor, e.g. executing the same command twice in a row
results in only one copy being added to the history.  To prevent duplicates
over all entries use [$history_remove_dups](#history-remove-dups).

(honor-disposition)=
## `$honor_disposition`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will not display attachments with a
disposition of "attachment" inline even if it could
render the part to plain text. These MIME parts can only
be viewed from the attachment menu.

If *unset*, NeoMutt will render all MIME parts it can
properly transform to plain text.

(honor-followup-to)=
## `$honor_followup_to`

- **Type:** quadoption
- **Default:** yes

This variable controls whether or not a Mail-Followup-To header is
honored when group-replying to a message.

(hostname)=
## `$hostname`

- **Type:** string
- **Default:** (empty)

Specifies the fully-qualified hostname of the system NeoMutt is running on
containing the host's name and the DNS domain it belongs to. It is used
as the domain part (after "@") for local email addresses.

If not specified in a config file, then NeoMutt will try to determine the
hostname itself.

Optionally, NeoMutt can be compiled with a fixed domain name.

Also see [$use_domain](#use-domain) and [$hidden_host](#hidden-host).

(idn-decode)=
## `$idn_decode`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will show you international domain names decoded.
Note: You can use IDNs for addresses even if this is *unset*.
This variable only affects decoding. (IDN only)

(idn-encode)=
## `$idn_encode`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will encode international domain names using
IDN.  Unset this if your SMTP server can handle newer ([RFC6531](https://www.rfc-editor.org/rfc/rfc6531.html))
UTF-8 encoded domains. (IDN only)

(ignore-list-reply-to)=
## `$ignore_list_reply_to`

- **Type:** boolean
- **Default:** no

Affects the behavior of the `<reply>` function when replying to
messages from mailing lists (as defined by the "`subscribe`" or
"`lists`" commands).  When *set*, if the "Reply-To:" field is
set to the same value as the "To:" field, NeoMutt assumes that the
"Reply-To:" field was set by the mailing list to automate responses
to the list, and will ignore this field.  To direct a response to the
mailing list when this option is *set*, use the `[<list-reply>](#list-reply)`
function; `<group-reply>` will reply to both the sender and the
list.

(implicit-auto-view)=
## `$implicit_auto_view`

- **Type:** boolean
- **Default:** no

If set to "yes", NeoMutt will look for a mailcap entry with the
"`copiousoutput`" flag set for *every* MIME attachment it doesn't
have an internal viewer defined for. If such an entry is found, NeoMutt will
use the viewer defined in that entry to convert the body part to text form.

(include)=
## `$include`

- **Type:** quadoption
- **Default:** ask-yes

Controls whether or not a copy of the message(s) you are replying to
is included in your reply.

(include-encrypted)=
## `$include_encrypted`

- **Type:** boolean
- **Default:** no

Controls whether or not NeoMutt includes separately encrypted attachment
contents when replying.

This variable was added to prevent accidental exposure of encrypted
contents when replying to an attacker.  If a previously encrypted message
were attached by the attacker, they could trick an unwary recipient into
decrypting and including the message in their reply.

(include-only-first)=
## `$include_only_first`

- **Type:** boolean
- **Default:** no

Controls whether or not NeoMutt includes only the first attachment
of the message you are replying.

(indent-string)=
## `$indent_string`

- **Type:** string
- **Default:** "`> `"

Specifies the string to prepend to each line of text quoted in a
message to which you are replying.  You are strongly encouraged not to
change this value, as it tends to agitate the more fanatical netizens.

The value of this option is ignored if [$text_flowed](#text-flowed) is set, because
the quoting mechanism is strictly defined for format=flowed.

This option is a format string, please see the description of
[$index_format](#index-format) for supported `printf(3)`-style sequences.

(index-format)=
## `$index_format`

- **Type:** string
- **Default:** "`%4C %Z %{%b %d} %-15.15L (%<l?%4l&%4c>) %s`"

This variable allows you to customize the message index display to
your personal taste.

"Format strings" are similar to the strings used in the C function
`printf(3)` to format output (see the man page for more details). For an
explanation of the %<...> construct, see the [status_format](#status-format) description. The
following sequences are defined in NeoMutt:

| **Short** | **Long Name** | **Description** |
| --- | --- | --- |
| `%A` | `%{reply-to}` | Reply-to address (if present; otherwise: address of author) |
| `%a` | `%{from}` | Address of the author |
| `%B` | `%{list-address}` | List to which the email was sent (if any; otherwise: Mailbox name) |
| `%b` | `%{mailbox-name}` | Filename of the original message folder (think mailbox) |
| `%C` | `%{number}` | Current message number |
| `%c` | `%{body-characters}` | Number of characters (bytes) in the body of the message (see **Size Format**) |
| `%cr` | `%{size}` | Number of characters (bytes) in the raw message, including the header (see **Size Format**) |
| `%D` | `%{date-format-local}` | Date and time of message using [$date_format](#date-format) and local timezone. |
|  |  | It is recommended to use `%[fmt]` instead, where `fmt` is the value of [$date_format](#date-format). |
| `%d` | `%{date-format}` | Date and time of message using [$date_format](#date-format) and sender's timezone. |
|  |  | It is recommended to use `%{fmt}` instead, where `fmt` is the value of [$date_format](#date-format). |
| `%E` | `%{thread-count}` | Number of messages in current thread |
| `%e` | `%{thread-number}` | Current message number in thread |
| `%F` | `%{sender}` | Author name, or recipient name if the message is from you |
| `%Fp` | `%{sender-plain}` | Like `%F`, but plain. No contextual formatting is applied to recipient name |
| `%f` | `%{from-full}` | Sender (address + real name), either From: or Return-Path: |
| `%Gx` | `%{tags-transformed}` | Individual message tag (e.g. Notmuch tags/imap flags) |
| `%g` | `%{tags}` | Message tags (e.g. Notmuch tags/imap flags) |
| `%H` | `%{spam}` | Spam attribute(s) of this message |
| `%I` | `%{initials}` | Initials of author |
| `%i` | `%{message-id}` | Message-id of the current message |
| `%J` | `%{thread-tags}` | Message tags (if present, tree unfolded, and != parent's tags) |
| `%K` | `%{list-empty}` | List to which the email was sent (if any; otherwise: empty) |
| `%L` | `%{from-list}` | If an address in the `To:` or `Cc:` header field matches an address |
|  |  | defined by the user's `$subscribe` command, this displays. |
| `%l` | `%{lines}` | Number of lines in the unprocessed message (may not work with maildir, mh, and IMAP folders) |
| `%M` | `%{thread-hidden-count}` | Number of hidden messages if the thread is collapsed |
| `%m` | `%{message-count}` | Total number of message in the mailbox |
| `%N` | `%{score}` | Message score |
| `%n` | `%{name}` | Author's real name (or address if missing) |
| `%O` | `%{save-folder}` | Original save folder where NeoMutt would formerly have Stashed the message: |
|  |  | list name or recipient name if not sent to a list |
| `%P` | `%{percentage}` | Progress indicator for the built-in pager (how much of the file has been displayed) |
| `%q` | `%{newsgroup}` | Newsgroup name (if compiled with NNTP support) |
| `%R` | `%{cc-all}` | Comma separated list of `Cc:` recipients |
| `%r` | `%{to-all}` | Comma separated list of `To:` recipients |
| `%S` | `%{flag-chars}` | Single character status of the message (`N`/`O`/`D`/`d`/`!`/`r`/`*`) |
| `%s` | `%{subject}` | Subject of the message |
| `%T` | `%{to-chars}` | Appropriate character from the [$to_chars](#to-chars) string |
| `%t` | `%{to}` | `%{To:}` field (recipients) |
| `%u` | `%{username}` | User (login) name of the author |
| `%v` | `%{first-name}` | First name of the author, or the recipient if the message is from you |
| `%W` | `%{organization}` | Name of organization of author (`Organization:` field) |
| `%X` | `%{attachment-count}` | Number of MIME attachments (see the `$attachments` section for possible speed effects) |
| `%x` | `%{x-comment-to}` | `%{X-Comment-To:}` field (if present) |
| `%Y` | `%{thread-x-label}` | `%{X-Label:}` field, if present, and |
|  |  | 1. not at part of a thread tree |
|  |  | 2. at the top of a thread, or |
|  |  | 3. `X-Label:` is different from Preceding message's `X-Label:` |
| `%y` | `%{x-label}` | `%{X-Label:}` field, if present |
| `%Z` | `%{combined-flags}` | A three character set of message status flags. |
|  |  | The first character is new/read/replied flags (`n`/`o`/`r`/`O`/`N`). |
|  |  | The second is deleted or encryption flags (`D`/`d`/`S`/`P`/`s`/`K`). |
|  |  | The third is either tagged/flagged (`*`/`!`), or one of the characters. |
|  |  | Listed in [$to_chars](#to-chars). |
| `%zc` | `%{crypto-flags}` | Message crypto flags |
| `%zs` | `%{status-flags}` | Message status flags |
| `%zt` | `%{message-flags}` | Message tag flags |
| `%@name@` |  | Insert and evaluate format-string from the matching ``index-format-hook`` command |
| `%{fmt}` |  | Date and time of the message is converted to sender's time zone, and `fmt` is expanded by the library function `strftime(3)`; |
|  |  | if the first character inside the braces is a bang (`!`), the date is formatted ignoring any locale settings. |
|  |  | Note that the sender's time zone might only be available as a numerical offset, so `%Z` behaves like `%z`. |
|  |  | `%{fmt}` behaves like `%[fmt]` on systems where `struct tm` doesn't have a `tm_gmtoff` member. |
| `%[fmt]` |  | Date and time of the message is converted to the local time zone, and `fmt` is expanded by the library function `strftime(3)`; |
|  |  | if the first character inside the brackets is a bang (`!`), the date is formatted ignoring any locale settings. |
| `%(fmt)` |  | Local date and time when the message was received, and `fmt` is expanded by the library function `strftime(3)`; |
|  |  | if the first character inside the parentheses is a bang (`!`), the date is formatted ignoring any locale settings. |
| `%*X` | `%{padding-soft}` | Soft-fill with character `X` as pad |
| `%>X` | `%{padding-hard}` | Right justify the rest of the string and pad with character `X` |
| `%|X` | `%{padding-eol}` | Pad to the end of the line with character `X` |

Date format expressions can be constructed based on relative dates. Using
the date formatting operators along with nested conditionals, the date
format can be modified based on how old a message is.  See the section on
"Conditional Dates" for an explanation and examples

Note that for mbox/mmdf, "%l" applies to the unprocessed message, and
for maildir/mh, the value comes from the "Lines:" header field when
present (the meaning is normally the same). Thus the value depends on
the encodings used in the different parts of the message and has little
meaning in practice.

"Soft-fill" deserves some explanation: Normal right-justification
will print everything to the left of the "%>", displaying padding and
whatever lies to the right only if there's room. By contrast,
soft-fill gives priority to the right-hand side, guaranteeing space
to display it and showing padding only if there's still room. If
necessary, soft-fill will eat text leftwards to make room for
rightward text.

Note that these expandos are supported in
"`save-hook`", "`fcc-hook`" and "`fcc-save-hook`", too.

(inews-command)=
## `$inews_command`

- **Type:** command
- **Default:** (empty)

If set, specifies the program and arguments used to deliver news posted
by NeoMutt.  Otherwise, NeoMutt posts article using current connection to
news server.  The following printf-style sequence is understood:

| %a | account url |
| --- | --- |
| %p | port |
| %P | port if specified |
| %s | news server name |
| %S | url schema |
| %u | username |

Example:

```neomuttrc
set inews_command="/usr/local/bin/inews -hS"
```

(ispell)=
## `$ispell`

- **Type:** command
- **Default:** "`ispell`"

How to invoke ispell (GNU's spell-checking software).

(keep-flagged)=
## `$keep_flagged`

- **Type:** boolean
- **Default:** no

If *set*, read messages marked as flagged will not be moved
from your spool mailbox to your [$mbox](#mbox) mailbox or to the "mbox"
specified by a `mbox-hook` command.

Note that [$keep_flagged](#keep-flagged) only has an effect if [$move](#move) is set.

(local-date-header)=
## `$local_date_header`

- **Type:** boolean
- **Default:** yes

If *set*, the date in the Date header of emails that you send will be in
your local timezone. If unset a UTC date will be used instead to avoid
leaking information about your current location.

(mail-check)=
## `$mail_check`

- **Type:** number
- **Default:** 5

This variable configures how often (in seconds) NeoMutt should look for
new mail. Also see the [$timeout](#timeout) variable.

(mail-check-recent)=
## `$mail_check_recent`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will only notify you about new mail that has been
received since the last time you opened the mailbox. When *unset*,
NeoMutt will notify you if any new mail exists in the mailbox, regardless of
whether you have visited it recently.

(mail-check-stats)=
## `$mail_check_stats`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will periodically calculate message
statistics of a mailbox while polling for new mail.  It will
check for unread, flagged, and total message counts.
(Note: IMAP mailboxes only support unread and total counts).

Because this operation is more performance intensive, it defaults
to *unset*, and has a separate option,
[$mail_check_stats_interval](#mail-check-stats-interval), to control how often to update these
counts.

Message statistics can also be explicitly calculated by invoking the
`<check-stats>` function.

(mail-check-stats-interval)=
## `$mail_check_stats_interval`

- **Type:** number
- **Default:** 60

When [$mail_check_stats](#mail-check-stats) is *set*, this variable configures
how often (in seconds) NeoMutt will update message counts.

(mailbox-folder-format)=
## `$mailbox_folder_format`

- **Type:** string
- **Default:** "`%2C %<n?%6n&      > %6m %i`"

This variable allows you to customize the file browser display to your
personal taste. It's only used to customize network mailboxes (e.g. imap).
This string is identical in formatting to the one used by
"[$folder_format](#folder-format)".

(mailcap-path)=
## `$mailcap_path`

- **Type:** string list
- **Default:** "`~/.mailcap:/usr/share/neomutt/mailcap:/etc/mailcap:/etc/mailcap:/usr/etc/mailcap:/usr/local/etc/mailcap`"

This variable specifies a list of colon-separated files to consult when
attempting to display MIME bodies not directly supported by NeoMutt.  The
default value is generated during startup: see the "`mailcap`" section of the
manual.

[$mailcap_path](#mailcap-path) is overridden by the environment variable `$MAILCAPS`.

The default search path is from [RFC1524](https://www.rfc-editor.org/rfc/rfc1524.html).

(mailcap-sanitize)=
## `$mailcap_sanitize`

- **Type:** boolean
- **Default:** yes

If *set*, NeoMutt will restrict possible characters in mailcap % expandos
to a well-defined set of safe characters.  This is the safe setting,
but we are not sure it doesn't break some more advanced MIME stuff.

**DON'T CHANGE THIS SETTING UNLESS YOU ARE REALLY SURE WHAT YOU ARE
DOING!**

(mark-macro-prefix)=
## `$mark_macro_prefix`

- **Type:** string
- **Default:** "`'`"

Prefix for macros created using mark-message.  A new macro
automatically generated with *<mark-message>a* will be composed
from this prefix and the letter *a*.

(mark-old)=
## `$mark_old`

- **Type:** boolean
- **Default:** yes

Controls whether or not NeoMutt marks *new* **unread**
messages as *old* if you exit a mailbox without reading them.
With this option *set*, the next time you start NeoMutt, the messages
will show up with an "O" next to them in the index menu,
indicating that they are old.

(markers)=
## `$markers`

- **Type:** boolean
- **Default:** yes

Controls the display of wrapped lines in the internal pager. If set, a
"+" marker is displayed at the beginning of wrapped lines.

Also see the [$smart_wrap](#smart-wrap) variable.

(mask)=
## `$mask`

- **Type:** regular expression
- **Default:** "`!^\.[^.]`"

A regular expression used in the file browser, optionally preceded by
the *not* operator "!".  Only files whose names match this mask
will be shown. The match is always case-sensitive.

(mbox)=
## `$mbox`

- **Type:** mailbox
- **Default:** "`~/mbox`"

This specifies the folder into which read mail in your [$spool_file](#spool-file)
folder will be appended.

Also see the [$move](#move) variable.

(mbox-type)=
## `$mbox_type`

- **Type:** enumeration
- **Default:** mbox

The default mailbox type used when creating new folders. May be any of
"mbox", "MMDF", "MH" or "Maildir".

This can also be set using the `-m` command-line option.

(me-too)=
## `$me_too`

- **Type:** boolean
- **Default:** no

If *unset*, NeoMutt will remove your address (see the "`alternates`"
command) from the list of recipients when replying to a message.

(menu-context)=
## `$menu_context`

- **Type:** number
- **Default:** 0

This variable controls the number of lines of context that are given
when scrolling through menus. (Similar to [$pager_context](#pager-context).)

(menu-move-off)=
## `$menu_move_off`

- **Type:** boolean
- **Default:** yes

When *unset*, the bottom entry of menus will never scroll up past
the bottom of the screen, unless there are less entries than lines.
When *set*, the bottom entry may move off the bottom.

(menu-scroll)=
## `$menu_scroll`

- **Type:** boolean
- **Default:** no

When *set*, menus will be scrolled up or down one line when you
attempt to move across a screen boundary.  If *unset*, the screen
is cleared and the next or previous page of the menu is displayed
(useful for slow links to avoid many redraws).

(message-cache-clean)=
## `$message_cache_clean`

- **Type:** boolean
- **Default:** no

If *set*, NeoMutt will clean out obsolete entries from the message cache
when the mailbox is synchronized. You probably only want to set it every once
in a while, since it can be a little slow (especially for large folders).

(message-cache-dir)=
## `$message_cache_dir`

- **Type:** path
- **Default:** (empty)

Set this to a directory and NeoMutt will cache copies of messages from
your IMAP and POP servers here. You are free to remove entries at any
time.

When setting this variable to a directory, NeoMutt needs to fetch every
remote message only once and can perform regular expression searches
as fast as for local folders.

Also see the [$message_cache_clean](#message-cache-clean) variable.

(message-format)=
## `$message_format`

- **Type:** string
- **Default:** "`%s`"

This is the string displayed in the "attachment" menu for
attachments of type `message/rfc822`.  For a full listing of defined
`printf(3)`-like sequences see the section on [$index_format](#index-format).

(message-id-format)=
## `$message_id_format`

- **Type:** string
- **Default:** "`<%z@%f>`"

This variable allows you to choose a custom format for the Message-Id when
sending messages. The value may end in "|" to invoke an external filter.
See **format string filters**.

Please note that the Message-ID value follows a strict syntax, and you are
responsible for ensuring correctness if you change this from the default.
In particular, the value must follow the syntax in [RFC5322](https://www.rfc-editor.org/rfc/rfc5322.html):
"`"<" id-left "@" id-right ">"`".  No spaces are allowed, and
`id-left` should follow the dot-atom-text syntax in the RFC.
The `id-right` should generally be left as "`%f`".

If unset, NeoMutt will use a long random format.

If the format doesn't begin/end with "<", ">" they will be added.

The old Message-ID format can be used by setting this to:
"`<%Y%02m%02d%02H%02M%02S.G%c%p@%f>`"

The following `printf(3)`-style sequences are understood:

| **Short** | **Long Name** | **Description** |
| --- | --- | --- |
| %c | `%{counter}` | Step counter looping from `A` to `Z` |
| %d | `%{day}` | Current day of the month (GMT) |
| %f | `%{hostname}` | [$hostname](#hostname) |
| %H | `%{hour}` | Current hour using a 24-hour clock (GMT) |
| %m | `%{minute}` | Current month number (GMT) |
| %M | `%{month}` | Current minute of the hour (GMT) |
| %p | `%{pid}` | Pid of the running mutt process |
| %r | `%{random_3}` | 3 bytes of pseudo-random data encoded in Base64 |
| %S | `%{second}` | Current second of the minute (GMT) |
| %x | `%{random_1}` | 1 byte of pseudo-random data hex encoded (example: `1b`) |
| %Y | `%{year}` | Current year using 4 digits (GMT) |
| %z | `%{random_12}` | 4 byte timestamp + 8 bytes of pseudo-random data encoded in Base64 |

See also: Base64Url: [https://datatracker.ietf.org/doc/html/rfc4648#section-5](https://datatracker.ietf.org/doc/html/rfc4648#section-5)

(meta-key)=
## `$meta_key`

- **Type:** boolean
- **Default:** no

If *set*, forces NeoMutt to interpret keystrokes with the high bit (bit
8) set as if the user had pressed the Esc key and whatever key remains after
having the high bit removed. For example, if the key pressed has an ASCII
value of `0xf8`, then this is treated as if the user had pressed Esc then
"x". This is because the result of removing the high bit from `0xf8` is
`0x78`, which is the ASCII character "x".

(move)=
## `$move`

- **Type:** quadoption
- **Default:** no

If this variable is *set*, then NeoMutt will move read messages
from your spool mailbox to your [$mbox](#mbox) mailbox or to the "mbox"
specified by a `mbox-hook` command.

See also [$keep_flagged](#keep-flagged).

(narrow-tree)=
## `$narrow_tree`

- **Type:** boolean
- **Default:** no

This variable, when *set*, makes the thread tree narrower, allowing
deeper threads to fit on the screen.

(net-inc)=
## `$net_inc`

- **Type:** number
- **Default:** 10

Operations that expect to transfer a large amount of data over the
network will update their progress every [$net_inc](#net-inc) kilobytes.
If set to 0, no progress messages will be displayed.

See also [$read_inc](#read-inc), [$write_inc](#write-inc) and [$net_inc](#net-inc).

(new-mail-command)=
## `$new_mail_command`

- **Type:** command
- **Default:** (empty)

If *set*, NeoMutt will call this command after a new message is received.
See the [$status_format](#status-format) documentation for the values that can be formatted
into this command.

(news-cache-dir)=
## `$news_cache_dir`

- **Type:** path
- **Default:** "`~/.neomutt`"

This variable pointing to directory where NeoMutt will save cached news
articles and headers in. If *unset*, articles and headers will not be
saved at all and will be reloaded from the server each time.

(news-server)=
## `$news_server`

- **Type:** string
- **Default:** (empty)

This variable specifies domain name or address of NNTP server.

You can also specify username and an alternative port for each news server,
e.g. `[[s]news://][username[:password]@]server[:port]`

This option can also be set using the command line option "-g", the
environment variable `$NNTPSERVER`, or putting the server name in the
file "/etc/nntpserver".

(newsgroups-charset)=
## `$newsgroups_charset`

- **Type:** string
- **Default:** "`utf-8`"

Character set of newsgroups descriptions.

(newsrc)=
## `$newsrc`

- **Type:** path
- **Default:** "`~/.newsrc`"

The file, containing info about subscribed newsgroups - names and
indexes of read articles.  The following printf-style sequence
is understood:

| **Short** | **Long Name** | **Description** |
| --- | --- | --- |
| `%a` | `%{account}` | Account url |
| `%P` | `%{port-if}` | Port if specified |
| `%p` | `%{port}` | Port |
| `%S` | `%{schema}` | Url schema |
| `%s` | `%{server}` | News server name |
| `%u` | `%{username}` | Username |

(general-pager)=
## `$pager`

- **Type:** command
- **Default:** (empty)

This variable specifies which pager you would like to use to view
messages. When empty, NeoMutt will use the built-in pager, otherwise this
variable should specify the pathname of the external pager you would
like to use.

Using an external pager may have some disadvantages: Additional
keystrokes are necessary because you can't call NeoMutt functions
directly from the pager, and screen resizes cause lines longer than
the screen width to be badly formatted in the help menu.

(pattern-format)=
## `$pattern_format`

- **Type:** string
- **Default:** "`%2n %-15e  %d`"

This variable describes the format of the "pattern completion" menu. The
following `printf(3)`-style sequences are understood:

| **Short** | **Long Name** | **Description** |
| --- | --- | --- |
| `%d` | `%{description}` | Pattern description |
| `%e` | `%{expression}` | Pattern expression |
| `%n` | `%{number}` | Index number |
| `%*X` | `%{padding-soft}` | Soft-fill with character `X` as pad |
| `%>X` | `%{padding-hard}` | Right justify the rest of the string and pad with character `X` |
| `%|X` | `%{padding-eol}` | Pad to the end of the line with character `X` |

(post-moderated)=
## `$post_moderated`

- **Type:** quadoption
- **Default:** ask-yes

If set to *yes*, NeoMutt will post article to newsgroup that have
not permissions to posting (e.g. moderated).  **Note:** if news server
does not support posting to that newsgroup or totally read-only, that
posting will not have an effect.

(postpone)=
## `$postpone`

- **Type:** quadoption
- **Default:** ask-yes

Controls whether or not messages are saved in the [$postponed](#postponed)
mailbox when you elect not to send immediately. If set to
*ask-yes* or *ask-no*, you will be prompted with "Save
(postpone) draft message?" when quitting from the "compose"
screen.

Also see the [$recall](#recall) variable.

(postpone-encrypt)=
## `$postpone_encrypt`

- **Type:** boolean
- **Default:** no

When *set*, postponed messages that are marked for encryption will be
self-encrypted.  NeoMutt will first try to encrypt using the value specified
in [$pgp_default_key](#pgp-default-key) or [$smime_default_key](#smime-default-key).
(Crypto only)

(postpone-encrypt-as)=
## `$postpone_encrypt_as`

- **Type:** string
- **Default:** (empty)

When *set*, NeoMutt will use this as a fallback encryption key for
postponed messages.

(postponed)=
## `$postponed`

- **Type:** mailbox
- **Default:** "`~/postponed`"

NeoMutt allows you to indefinitely "[postpone](#postpone) sending a message" which
you are editing.  When you choose to postpone a message, NeoMutt saves it
in the mailbox specified by this variable.

Also see the [$postpone](#postpone) variable.

(preconnect)=
## `$preconnect`

- **Type:** string
- **Default:** (empty)

If *set*, a shell command to be executed if NeoMutt fails to establish
a connection to the server. This is useful for setting up secure
connections, e.g. with `ssh(1)`. If the command returns a  nonzero
status, NeoMutt gives up opening the server. Example:

```neomuttrc
set preconnect="ssh -f -q -L 1234:mailhost.net:143 mailhost.net \
sleep 20 < /dev/null > /dev/null"
```

Mailbox "foo" on "mailhost.net" can now be reached
as "{localhost:1234}foo".

Note: For this example to work, you must be able to log in to the
remote machine without having to enter a password.

(preferred-languages)=
## `$preferred_languages`

- **Type:** string list
- **Default:** (empty)

This variable specifies a list of comma-separated languages.
[RFC8255](https://www.rfc-editor.org/rfc/rfc8255.html) : user preferred languages to be searched in parts and display.
Example:

```neomuttrc
set preferred_languages="en,fr,de"
```

(general-print)=
## `$print`

- **Type:** quadoption
- **Default:** ask-no

Controls whether or not NeoMutt really prints messages.
This is set to "ask-no" by default, because some people
accidentally hit "p" often.

(prompt-after)=
## `$prompt_after`

- **Type:** boolean
- **Default:** yes

If you use an *external* `$pager`, setting this variable will
cause NeoMutt to prompt you for a command when the pager exits rather
than returning to the index menu.  If *unset*, NeoMutt will return to the
index menu when the external pager exits.

(query-command)=
## `$query_command`

- **Type:** command
- **Default:** (empty)

This specifies the command NeoMutt will use to make external address
queries.  The string may contain a "%s", which will be substituted
with the query string the user types.  NeoMutt will add quotes around the
string substituted for "%s" automatically according to shell quoting
rules, so you should avoid adding your own.  If no "%s" is found in
the string, NeoMutt will append the user's query to the end of the string.
See [Address Queries](../../howto/address-query).

(query-format)=
## `$query_format`

- **Type:** string
- **Default:** "`%3i %t %-25N %-25E | %C%> %Y`"

This variable describes the format of the "query" menu. The
following `printf(3)`-style sequences are understood:

| **Short** | **Long Name** | **Description** |
| --- | --- | --- |
| `%A` | `%{address}` | Full Address (Name and Email) |
| `%C` | `%{comment}` | Comment |
| `%E` | `%{email}` | Email Address |
| `%i` | `%{number}` | Index number |
| `%N` | `%{name}` | Real name |
| `%t` | `%{tagged}` | Alias is tagged (selected) |
| `%Y` | `%{tags}` | User-defined tags (labels) |
| `%*X` | `%{padding-soft}` | Soft-fill with character `X` as pad |
| `%>X` | `%{padding-hard}` | Right justify the rest of the string and pad with character `X` |
| `%|X` | `%{padding-eol}` | Pad to the end of the line with character `X` |

For an explanation of "soft-fill", see the [$index_format](#index-format) documentation.

The following sequences are deprecated; they will be removed in the future.

| %a | Use %E instead |
| --- | --- |
| %c | Use %i instead |
| %e | Use %C instead |
| %n | Use %N instead |

(quit)=
## `$quit`

- **Type:** quadoption
- **Default:** yes

This variable controls whether "quit" and "exit" actually quit from NeoMutt.
If this option is *set*, they do quit, if it is *unset*, they have no
effect, and if it is set to *ask-yes* or *ask-no*, you are prompted
for confirmation when you try to quit.

In order to quit from NeoMutt if this variable is *unset*, you must send
the signal SIGINT to NeoMutt.  This can usually be achieved by pressing
CTRL-C in the terminal.

(quote-regex)=
## `$quote_regex`

- **Type:** regular expression
- **Default:** "`^([ \t]*[|>:}#])+`"

A regular expression used in the internal pager to determine quoted
sections of text in the body of a message. Quoted text may be filtered
out using the `<toggle-quoted>` command, or colored according to the
"color quoted" family of directives.

Higher levels of quoting may be colored differently ("color quoted1",
"color quoted2", etc.). The quoting level is determined by removing
the last character from the matched text and recursively reapplying
the regular expression until it fails to produce a match.

Match detection may be overridden by the [$smileys](#smileys) regular expression.

(read-inc)=
## `$read_inc`

- **Type:** number
- **Default:** 10

If set to a value greater than 0, NeoMutt will display which message it is
currently on when reading a mailbox or when performing search actions such as
search and limit. The message is printed after this many messages have been
read or searched (e.g., if set to 25, NeoMutt will print a message when it is
at message 25, and then again when it gets to message 50). This variable is
meant to indicate progress when reading or searching large mailboxes which
may take some time. When set to 0, only a single message will appear before
the reading the mailbox.

Also see the [$write_inc](#write-inc), [$net_inc](#net-inc) and [$time_inc](#time-inc) variables and the
"**tuning**" section of the manual for performance considerations.

(read-only)=
## `$read_only`

- **Type:** boolean
- **Default:** no

If *set*, all folders are opened in read-only mode.

(real-name)=
## `$real_name`

- **Type:** string
- **Default:** (empty)

This variable specifies what "real" or "personal" name should be used
when sending messages.

If not specified, then the user's "real name" will be read from
`/etc/passwd`. This option will not be used, if "[$from](#from)" is set.

(recall)=
## `$recall`

- **Type:** quadoption
- **Default:** ask-yes

Controls whether or not NeoMutt recalls postponed messages
when composing a new message.

Setting this variable to *yes* is not generally useful, and thus not
recommended.  Note that the `<recall-message>` function can be used
to manually recall postponed messages.

Also see [$postponed](#postponed) variable.

(record)=
## `$record`

- **Type:** mailbox
- **Default:** "`~/sent`"

This specifies the file into which your outgoing messages should be
appended.  (This is meant as the primary method for saving a copy of
your messages, but another way to do this is using the "`my-header`"
command to create a "Bcc:" field with your email address in it.)

The value of *[$record](#record)* is overridden by the [$force_name](#force-name) and
[$save_name](#save-name) variables, and the "`fcc-hook`" command.  Also see [$copy](#copy)
and [$write_bcc](#write-bcc).

(reflow-space-quotes)=
## `$reflow_space_quotes`

- **Type:** boolean
- **Default:** yes

This option controls how quotes from format=flowed messages are displayed
in the pager and when replying (with [$text_flowed](#text-flowed) *unset*).
When set, this option adds spaces after each level of quote marks, turning
">>>foo" into "> > > foo".

**Note:** If [$reflow_text](#reflow-text) is *unset*, this option has no effect.
Also, this option does not affect replies when [$text_flowed](#text-flowed) is *set*.

(reflow-text)=
## `$reflow_text`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will reformat paragraphs in text/plain
parts marked format=flowed.  If *unset*, NeoMutt will display paragraphs
unaltered from how they appear in the message body.  See [RFC3676](https://www.rfc-editor.org/rfc/rfc3676.html) for
details on the *format=flowed* format.

Also see [$reflow_wrap](#reflow-wrap), and [$wrap](#wrap).

(reflow-wrap)=
## `$reflow_wrap`

- **Type:** number
- **Default:** 78

This variable controls the maximum paragraph width when reformatting
text/plain parts when [$reflow_text](#reflow-text) is *set*. When the value is 0,
paragraphs will be wrapped at the terminal's right margin. A positive value
sets the paragraph width relative to the left margin. A negative value set
the paragraph width relative to the right margin.

Be aware that the reformatted lines of a paragraph are still subject to
[$wrap](#wrap). This means if [$reflow_wrap](#reflow-wrap) is 40 and [$wrap](#wrap) is 30, then the
paragraph gets reformatted to 40 characters a line (due to [$reflow_wrap](#reflow-wrap)) and
afterwards each 40-character-line is split at 30 characters (due to [$wrap](#wrap)),
resulting in alternating line lengths of 30 and 10 characters.

Also see [$wrap](#wrap).

(reply-regex)=
## `$reply_regex`

- **Type:** regular expression
- **Default:** "`^((re)(\[[0-9]+\])*:[ \t]*)*`"

A regular expression used to recognize reply messages when
threading and replying. The default value corresponds to the
standard Latin "Re:" prefix.

This value may have been localized by the translator for your
locale, adding other prefixes that are common in the locale. You
can add your own prefixes by appending inside `"^(re)"`.  For
example: `"^(re|sv)"` or `"^(re|aw|sv)"`.

The second parenthesized expression matches zero or more
bracketed numbers following the prefix, such as `"Re[1]: "`.
The initial `"\\["` means a literal left-bracket character.
Note the backslash must be doubled when used inside a double
quoted string in the neomuttrc.  `"[0-9]+"` means one or more
numbers.  `"\\]"` means a literal right-bracket.  Finally the
whole parenthesized expression has a `"*"` suffix, meaning it
can occur zero or more times.

The last part matches a colon followed by an optional space or
tab.  Note `"\t"` is converted to a literal tab inside a
double quoted string.  If you use a single quoted string, you
would have to type an actual tab character, and would need to
convert the double-backslashes to single backslashes.

Note: the result of this regex match against the subject is
stored in the header cache.  Mutt isn't smart enough to
invalidate a header cache entry based on changing [$reply_regex](#reply-regex),
so if you aren't seeing correct values in the index, try
temporarily turning off the header cache.  If that fixes the
problem, then once the variable is set to your liking, remove
your stale header cache files and turn the header cache back on.

(reply-self)=
## `$reply_self`

- **Type:** boolean
- **Default:** no

If *unset* and you are replying to a message sent by you, NeoMutt will
assume that you want to reply to the recipients of that message rather
than to yourself.

Also see the "`alternates`" command.

(reply-to)=
## `$reply_to`

- **Type:** quadoption
- **Default:** ask-yes

If *set*, when replying to a message, NeoMutt will use the address listed
in the Reply-to: header as the recipient of the reply.  If *unset*,
it will use the address in the From: header field instead.  This
option is useful for reading a mailing list that sets the Reply-To:
header field to the list address and you want to send a private
message to the author of a message.

(reply-with-xorig)=
## `$reply_with_xorig`

- **Type:** boolean
- **Default:** no

This variable provides a toggle. When active, the From: header will be
extracted from the current mail's 'X-Original-To:' header. This setting
does not have precedence over "[reverse_real_name](#reverse-real-name)".

Assuming 'fast_reply' is disabled, this option will prompt the user with a
prefilled From: header.

(resolve)=
## `$resolve`

- **Type:** boolean
- **Default:** yes

When *set*, the cursor in a list will be automatically advanced to the
next (possibly undeleted) message/attachment/entry whenever a command that
modifies the current message/attachment/entry is executed.

Examples of such commands are tagging a message, deleting an entry, or
saving an attachment.

(resume-draft-files)=
## `$resume_draft_files`

- **Type:** boolean
- **Default:** no

If *set*, draft files (specified by `-H` on the command
line) are processed similarly to when resuming a postponed
message.  Recipients are not prompted for; send-hooks are not
evaluated; no alias expansion takes place; user-defined headers
and signatures are not added to the message.

(resume-edited-draft-files)=
## `$resume_edited_draft_files`

- **Type:** boolean
- **Default:** yes

If *set*, draft files previously edited (via `-E -H` on
the command line) will have [$resume_draft_files](#resume-draft-files) automatically
set when they are used as a draft file again.

The first time a draft file is saved, NeoMutt will add a header,
X-Mutt-Resume-Draft to the saved file.  The next time the draft
file is read in, if NeoMutt sees the header, it will set
[$resume_draft_files](#resume-draft-files).

This option is designed to prevent multiple signatures,
user-defined headers, and other processing effects from being
made multiple times to the draft file.

(reverse-alias)=
## `$reverse_alias`

- **Type:** boolean
- **Default:** no

This variable controls whether or not NeoMutt will display the "personal"
name from your aliases in the index menu if it finds an alias that
matches the message's sender.  For example, if you have the following
alias:

```neomuttrc
alias juser abd30425@somewhere.net (Joe User)
```

and then you receive mail which contains the following header:

```
From: abd30425@somewhere.net
```

It would be displayed in the index menu as "Joe User" instead of
"abd30425@somewhere.net."  This is useful when the person's e-mail
address is not human friendly.

(reverse-name)=
## `$reverse_name`

- **Type:** boolean
- **Default:** no

It may sometimes arrive that you receive mail to a certain machine,
move the messages to another machine, and reply to some the messages
from there.  If this variable is *set*, the default *From:* line of
the reply messages is built using the address where you received the
messages you are replying to **if** that address matches your
"`alternates`".  If the variable is *unset*, or the address that would be
used doesn't match your "`alternates`", the *From:* line will use
your address on the current machine.

Also see the "`alternates`" command and [$reverse_real_name](#reverse-real-name).

(reverse-real-name)=
## `$reverse_real_name`

- **Type:** boolean
- **Default:** yes

This variable fine-tunes the behavior of the [$reverse_name](#reverse-name) feature.

When it is *unset*, NeoMutt will remove the real name part of a
matching address.  This allows the use of the email address
without having to also use what the sender put in the real name
field.

When it is *set*, NeoMutt will use the matching address as-is.

In either case, a missing real name will be filled in afterwards
using the value of [$real_name](#real-name).

(rfc2047-parameters)=
## `$rfc2047_parameters`

- **Type:** boolean
- **Default:** yes

When this variable is *set*, NeoMutt will decode [RFC2047](https://www.rfc-editor.org/rfc/rfc2047.html)-encoded MIME
parameters. You want to set this variable when NeoMutt suggests you
to save attachments to files named like:

```
=?iso-8859-1?Q?file=5F=E4=5F991116=2Ezip?=
=?utf-8?Q?z=C4=99ta.png?=
```

When this variable is *set* interactively, the change won't be
active until you change folders.

Note that this use of [RFC2047](https://www.rfc-editor.org/rfc/rfc2047.html)'s encoding is explicitly
prohibited by the standard, but nevertheless encountered in the
wild and produced by, e.g., Outlook.

Also note that setting this parameter will *not* have the effect
that NeoMutt *generates* this kind of encoding.  Instead, NeoMutt will
unconditionally use the encoding specified in [RFC2231](https://www.rfc-editor.org/rfc/rfc2231.html).

(save-address)=
## `$save_address`

- **Type:** boolean
- **Default:** no

If *set*, NeoMutt will take the sender's full address when choosing a
default folder for saving a mail. If [$save_name](#save-name) or [$force_name](#force-name)
is *set* too, the selection of the Fcc folder will be changed as well.

(save-empty)=
## `$save_empty`

- **Type:** boolean
- **Default:** yes

When *unset*, mailboxes which contain no saved messages will be removed
when closed (the exception is [$spool_file](#spool-file) which is never removed).
If *set*, mailboxes are never removed.

**Note:** This only applies to mbox and MMDF folders, NeoMutt does not
delete MH and Maildir directories.

(save-history)=
## `$save_history`

- **Type:** number
- **Default:** 0

This variable controls the size of the history (per category) saved in the
[$history_file](#history-file) file.

Setting this to a value greater than `$history` is possible.  However, there
will never be more than `$history` entries to select from even if more are
recorded in the history file.

(save-name)=
## `$save_name`

- **Type:** boolean
- **Default:** no

This variable controls how copies of outgoing messages are saved.
When *set*, a check is made to see if a mailbox specified by the
recipient address exists (this is done by searching for a mailbox in
the [$folder](#folder) directory with the *username* part of the
recipient address).  If the mailbox exists, the outgoing message will
be saved to that mailbox, otherwise the message is saved to the
[$record](#record) mailbox.

Also see the [$force_name](#force-name) variable.

(save-unsubscribed)=
## `$save_unsubscribed`

- **Type:** boolean
- **Default:** no

When *set*, info about unsubscribed newsgroups will be saved into
"newsrc" file and into cache.

(general-score)=
## `$score`

- **Type:** boolean
- **Default:** yes

When this variable is *unset*, scoring is turned off.  This can
be useful to selectively disable scoring for certain folders when the
[$score_threshold_delete](#score-threshold-delete) variable and related are used.

(search-context)=
## `$search_context`

- **Type:** number
- **Default:** 0

For the pager, this variable specifies the number of lines shown
before search results. By default, search results will be top-aligned.

(send-charset)=
## `$send_charset`

- **Type:** string list
- **Default:** "`us-ascii:iso-8859-1:utf-8`"

A colon-delimited list of character sets for outgoing messages. NeoMutt will
use the first character set into which the text can be converted exactly. If
your [$charset](#charset) is not "iso-8859-1" and recipients may not understand "UTF-8",
it is advisable to include in the list an appropriate widely used standard
character set (such as "iso-8859-2", "koi8-r" or "iso-2022-jp") either
instead of or after "iso-8859-1".

In case the text can't be converted into one of these exactly,
NeoMutt uses [$charset](#charset) as a fallback.

(sendmail)=
## `$sendmail`

- **Type:** command
- **Default:** "`/usr/sbin/sendmail -oem -oi`"

Specifies the program and arguments used to deliver mail sent by NeoMutt.
NeoMutt expects that the specified program interprets additional
arguments as recipient addresses.  NeoMutt appends all recipients after
adding a `--` delimiter (if not already present).  Additional
flags, such as for [$use_8bit_mime](#use-8bit-mime), [$use_envelope_from](#use-envelope-from),
[$dsn_notify](#dsn-notify), or [$dsn_return](#dsn-return) will be added before the delimiter.

**Note:** This command is invoked differently from most other
commands in NeoMutt.  It is tokenized by space, and invoked directly
via `execvp(3)` with an array of arguments - so commands or
arguments with spaces in them are not supported.  The shell is
not used to run the command, so shell quoting is also not
supported.

**See also:** [$write_bcc](#write-bcc).

(sendmail-wait)=
## `$sendmail_wait`

- **Type:** number
- **Default:** 0

Specifies the number of seconds to wait for the [$sendmail](#sendmail) process
to finish before giving up and putting delivery in the background.

NeoMutt interprets the value of this variable as follows:

| >0 | number of seconds to wait for sendmail to finish before continuing |
| --- | --- |
| 0 | wait forever for sendmail to finish |
| <0 | always put sendmail in the background without waiting |

Note that if you specify a value other than 0, the output of the child
process will be put in a temporary file.  If there is some error, you
will be informed as to where to find the output.

(shell)=
## `$shell`

- **Type:** command
- **Default:** "`/bin/sh`"

Command to use when spawning a subshell.
If not specified, then the user's login shell from `/etc/passwd` is used.

(show-multipart-alternative)=
## `$show_multipart_alternative`

- **Type:** string
- **Default:** (empty)

When *set* to `info`, the multipart/alternative information is shown.
When *set* to `inline`, all of the alternatives are displayed.
When not set, the default behavior is to show only the chosen alternative.

(show-new-news)=
## `$show_new_news`

- **Type:** boolean
- **Default:** yes

If *set*, news server will be asked for new newsgroups on entering
the browser.  Otherwise, it will be done only once for a news server.
Also controls whether or not number of new articles of subscribed
newsgroups will be then checked.

(show-only-unread)=
## `$show_only_unread`

- **Type:** boolean
- **Default:** no

If *set*, only subscribed newsgroups that contain unread articles
will be displayed in browser.

(sig-dashes)=
## `$sig_dashes`

- **Type:** boolean
- **Default:** yes

If *set*, a line containing "-- " (note the trailing space) will be
inserted before your [$signature](#signature). It is **strongly** recommended that you
not *unset* this variable unless your signature contains just your name.
The reason for this is because many software packages use "-- \n" to detect
your signature. For example, NeoMutt has the ability to highlight the
signature in a different color in the built-in pager.

(sig-on-top)=
## `$sig_on_top`

- **Type:** boolean
- **Default:** no

If *set*, the signature will be included before any quoted or forwarded
text.  It is **strongly** recommended that you do not set this variable
unless you really know what you are doing, and are prepared to take
some heat from netiquette guardians.

(signature)=
## `$signature`

- **Type:** path
- **Default:** "`~/.signature`"

Specifies the filename of your signature, which is appended to all
outgoing messages.  If the filename ends with a pipe ("|"), it is
assumed that filename is a shell command and input should be read from
its standard output.

(simple-search)=
## `$simple_search`

- **Type:** string
- **Default:** "`~f %s | ~s %s`"

Specifies how NeoMutt should expand a simple search into a real search
pattern.  A simple search is one that does not contain any of the "~" pattern
operators.  See "[patterns](../patterns.md)" for more information on search patterns.

simple_search applies to several functions, e.g. `<delete-pattern>`,
`<limit>`, searching in the index, and all of the index colors.

For example, if you simply type "joe" at a search or limit prompt, NeoMutt
will automatically expand it to the value specified by this variable by
replacing "%s" with the supplied string.
For the default value, "joe" would be expanded to: "~f joe | ~s joe".

(size-show-bytes)=
## `$size_show_bytes`

- **Type:** boolean
- **Default:** no

If *set*, message sizes will display bytes for values less than
1 kilobyte.  See **Size Format**.

(size-show-fractions)=
## `$size_show_fractions`

- **Type:** boolean
- **Default:** yes

If *set*, message sizes will be displayed with a single decimal value
for sizes from 0 to 10 kilobytes and 1 to 10 megabytes.
See **Size Format**.

(size-show-mb)=
## `$size_show_mb`

- **Type:** boolean
- **Default:** yes

If *set*, message sizes will display megabytes for values greater than
or equal to 1 megabyte.  See **Size Format**.

(size-units-on-left)=
## `$size_units_on_left`

- **Type:** boolean
- **Default:** no

If *set*, message sizes units will be displayed to the left of the
number. See **Size Format**.

(sleep-time)=
## `$sleep_time`

- **Type:** number
- **Default:** 1

Specifies time, in seconds, to pause while displaying certain informational
messages, while moving from folder to folder and after expunging
messages from the current folder.  The default is to pause one second, so
a value of zero for this option suppresses the pause.

(smart-wrap)=
## `$smart_wrap`

- **Type:** boolean
- **Default:** yes

Controls the display of lines longer than the screen width in the
internal pager. If *set*, long lines are wrapped at a word boundary.  If
*unset*, lines are simply wrapped at the screen edge. Also see the
[$markers](#markers) variable.

(smileys)=
## `$smileys`

- **Type:** regular expression
- **Default:** "`(>From )|(:[-^]?[][)(><}{|/DP])`"

The *pager* uses this variable to catch some common false
positives of [$quote_regex](#quote-regex), most notably smileys and not consider
a line quoted text if it also matches [$smileys](#smileys). This mostly
happens at the beginning of a line.

(socket-timeout)=
## `$socket_timeout`

- **Type:** number
- **Default:** 30

Causes NeoMutt to timeout any socket connect/read/write operation (for IMAP,
POP or SMTP) after this many seconds.  A negative value causes NeoMutt to
wait indefinitely.

(general-sort)=
## `$sort`

- **Type:** sort order
- **Default:** date

Specifies how to sort messages in the "index" menu.

| **Value** | **Sort by** |
| --- | --- |
| `date` | The date the email was sent |
| `date-received` | When the message was delivered locally |
| `from` | The email's From field |
| `label` | The emails label |
| `score` | The email's score |
| `size` | The size of the email |
| `spam` | The email's spam score |
| `subject` | The email's subject |
| `threads` | Email threads |
| `to` | The email's To field |
| `unsorted` | The order the messages appear in the mailbox |

| **Deprecated Value** | **Use this instead** |
| --- | --- |
| `date-sent` | `date` |
| `mailbox-order` | `unsorted` |

You may optionally use the "reverse-" prefix to specify reverse
sorting order, or the "last-" prefix to sort threads based on the
corresponding attribute of the last descendant rather than the
thread root.  If both prefixes are in use, "reverse-" must come
before "last-".  The "last-" prefix has no effect on a flat view.

Any ties in the primary sort are broken by [$sort_aux](#sort-aux).  When
[$use_threads](#use-threads) is "threads" or "reverse", `$sort` controls the
sorting between threads, and [$sort_aux](#sort-aux) controls the sorting within
a thread.

The values of "threads" and "reverse-threads" are legacy options,
which cause the value of `[$sort_aux](#sort-aux)` to also control sorting
between threads, and they may not be used with the "last-" prefix.
The preferred way to enable a threaded view is via
`[$use_threads](#use-threads)`.  This variable can also be set via the
`<sort-mailbox>` and `<sort-reverse>` functions.

Note: When [$use_threads](#use-threads) is "threads", the last thread sorts to the
bottom; when it is "reversed", the last thread sorts to the top.
The use of "reverse-" in `$sort` swaps which end the last thread
will sort to.

See the "Use Threads Feature" section for further explanation and
examples, see [Use Threads](../../howto/threads).

(spam-separator)=
## `$spam_separator`

- **Type:** string
- **Default:** "`,`"

This variable controls what happens when multiple spam headers
are matched: if *unset*, each successive header will overwrite any
previous matches value for the spam label. If *set*, each successive
match will append to the previous, using this variable's value as a
separator.

(spool-file)=
## `$spool_file`

- **Type:** mailbox
- **Default:** (empty)

If your spool mailbox is in a non-default place where NeoMutt can't find
it, you can specify its location with this variable. The description from
"named-mailboxes" may be used for the spool_file.

If not specified, then the environment variables `$MAIL` and
`$MAILDIR` will be checked.

(strict-threads)=
## `$strict_threads`

- **Type:** boolean
- **Default:** no

If *set*, threading will only make use of the "In-Reply-To" and
"References:" fields when you `$sort` by message threads.  By
default, messages with the same subject are grouped together in
"pseudo threads.". This may not always be desirable, such as in a
personal mailbox where you might have several unrelated messages with
the subjects like "hi" which will get grouped together. See also
[$sort_re](#sort-re) for a less drastic way of controlling this
behavior.

(suspend)=
## `$suspend`

- **Type:** boolean
- **Default:** yes

When *unset*, NeoMutt won't stop when the user presses the terminal's
*susp* key, usually "^Z". This is useful if you run NeoMutt
inside an xterm using a command like "`xterm -e neomutt`".

On startup NeoMutt tries to detect if it is the process session leader.
If so, the default of [suspend](#suspend) is "no" otherwise "yes".  This default covers
the above mentioned use case of "`xterm -e neomutt`".

(text-flowed)=
## `$text_flowed`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will generate "format=flowed" bodies with a content
type of "`text/plain; format=flowed`". This format is easier to handle
for some mailing software, and generally just looks like ordinary text. To
actually make use of this format's features, you'll need support in your
editor.

The option only controls newly composed messages.  Postponed messages,
resent messages, and draft messages (via -H on the command line) will
use the content-type of the source message.

Note that [$indent_string](#indent-string) is ignored when this option is *set*.

(thorough-search)=
## `$thorough_search`

- **Type:** boolean
- **Default:** yes

Affects the `~b`, `~B`, and `~h` search operations
described in section "[patterns](../patterns.md)".  If *set*, the headers and
body/attachments of messages to be searched are decoded before searching.
If *unset*, messages are searched as they appear in the folder.

Users searching attachments or for non-ASCII characters should *set* this
value because decoding also includes MIME parsing/decoding and possible
character set conversions. Otherwise NeoMutt will attempt to match against
the raw message received (for example quoted-printable encoded or with
encoded headers) which may lead to incorrect search results.

(thread-received)=
## `$thread_received`

- **Type:** boolean
- **Default:** no

If [$strict_threads](#strict-threads) is *unset*, then messages may also be grouped by
subject.  Unlike threading by "In-Reply-To:" and "References:" header,
grouping by subject does not imply a parent-child relation between two
messages.

To determine the ancestry between messages grouped by subject, NeoMutt uses
their date: only newer messages can be descendants of older ones.

When [$thread_received](#thread-received) is *set*, NeoMutt uses the date received rather
than the date sent when comparing messages for the date.

See also [$strict_threads](#strict-threads), and [$sort_re](#sort-re).

(tilde)=
## `$tilde`

- **Type:** boolean
- **Default:** no

When *set*, the internal-pager will pad blank lines to the bottom of the
screen with a tilde ("~").

(time-inc)=
## `$time_inc`

- **Type:** number
- **Default:** 0

Along with [$read_inc](#read-inc), [$write_inc](#write-inc), and [$net_inc](#net-inc), this
variable controls the frequency with which progress updates are
displayed. It suppresses updates less than [$time_inc](#time-inc) milliseconds
apart. This can improve throughput on systems with slow terminals,
or when running NeoMutt on a remote system.

Also see the "**tuning**" section of the manual for performance considerations.

(timeout)=
## `$timeout`

- **Type:** number
- **Default:** 600

This variable sets the time interval in seconds in which *timeout-hook*
commands get executed while waiting for user input either idling in menus
or in an interactive prompt.

A value of zero disables timeout hooks.

(tmp-dir)=
## `$tmp_dir`

- **Type:** path
- **Default:** "`/tmp`"

This variable allows you to specify where NeoMutt will place its
temporary files needed for displaying and composing messages.

If this variable is not set, the environment variable `$TMPDIR` is
used.  Failing that, then "`/tmp`" is used.

(to-chars)=
## `$to_chars`

- **Type:** character string
- **Default:** "` +TCFLR`"

Controls the character used to indicate mail addressed to you.

| **Character** | **Default** | **Description** |
| --- | --- | --- |
| 1 | <space> | The mail is *not* addressed to your address. |
| 2 | + | You are the only recipient of the message. |
| 3 | T | Your address appears in the "To:" header field, but you are not the only recipient of the message. |
| 4 | C | Your address is specified in the "Cc:" header field, but you are not the only recipient. |
| 5 | F | Indicates the mail that was sent by *you*. |
| 6 | L | Indicates the mail was sent to a mailing-list you subscribe to. |
| 7 | R | Your address appears in the "Reply-To:" header field but none of the above applies. |

(toggle-quoted-show-levels)=
## `$toggle_quoted_show_levels`

- **Type:** number
- **Default:** 0

Quoted text may be filtered out using the `<toggle-quoted>` command.
If set to a number greater than 0, then the `<toggle-quoted>`
command will only filter out quote levels above this number.

(trash)=
## `$trash`

- **Type:** mailbox
- **Default:** (empty)

If set, this variable specifies the path of the trash folder where the
mails marked for deletion will be moved, instead of being irremediably
purged.

NOTE: When you delete a message in the trash folder, it is really
deleted, so that you have a way to clean the trash.

(ts-enabled)=
## `$ts_enabled`

- **Type:** boolean
- **Default:** no

Controls whether NeoMutt tries to set the terminal status line and icon name.
Most terminal emulators emulate the status line in the window title.

(ts-icon-format)=
## `$ts_icon_format`

- **Type:** string
- **Default:** "`M%<n?AIL&ail>`"

Controls the format of the icon title, as long as "[$ts_enabled](#ts-enabled)" is set.
This string is identical in formatting to the one used by
"[$status_format](#status-format)".

(ts-status-format)=
## `$ts_status_format`

- **Type:** string
- **Default:** "`NeoMutt with %<m?%m messages&no messages>%<n? [%n NEW]>`"

Controls the format of the terminal status line (or window title),
provided that "[$ts_enabled](#ts-enabled)" has been set. This string is identical in
formatting to the one used by "[$status_format](#status-format)".

(tunnel)=
## `$tunnel`

- **Type:** command
- **Default:** (empty)

Setting this variable will cause NeoMutt to open a pipe to a command
instead of a raw socket. You may be able to use this to set up
preauthenticated connections to your IMAP/POP3/SMTP server. Example:

```
set tunnel="ssh -q mailhost.net /usr/local/libexec/imapd"
```

Note: For this example to work you must be able to log in to the remote
machine without having to enter a password.

When set, NeoMutt uses the tunnel for all remote connections.
Please see "`account-hook`" in the manual for how to use different
tunnel commands per connection.

(tunnel-is-secure)=
## `$tunnel_is_secure`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will assume the [$tunnel](#tunnel) connection does not need
STARTTLS to be enabled.  It will also allow IMAP PREAUTH server
responses inside a [tunnel](#tunnel) to proceed.  This is appropriate if [$tunnel](#tunnel)
uses ssh or directly invokes the server locally.

When *unset*, NeoMutt will negotiate STARTTLS according to the
[ssl_starttls](#ssl-starttls) and [ssl_force_tls](#ssl-force-tls) variables.  If [ssl_force_tls](#ssl-force-tls) is
set, NeoMutt will abort connecting if an IMAP server responds with PREAUTH.
This setting is appropriate if [$tunnel](#tunnel) does not provide security and
could be tampered with by attackers.

(uncollapse-jump)=
## `$uncollapse_jump`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will jump to the next unread message, if any,
when the current thread is *un*collapsed.

(uncollapse-new)=
## `$uncollapse_new`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will automatically uncollapse any collapsed
thread that receives a newly delivered message.  When
*unset*, collapsed threads will remain collapsed. The
presence of the newly delivered message will still affect index
sorting, though.

(use-8bit-mime)=
## `$use_8bit_mime`

- **Type:** boolean
- **Default:** no

**Warning:** do not set this variable unless you are using a version
of sendmail which supports the `-B8BITMIME` flag (such as sendmail
8.8.x) or you may not be able to send mail.

When *set*, NeoMutt will invoke [$sendmail](#sendmail) with the `-B8BITMIME`
flag when sending 8-bit messages to enable ESMTP negotiation.

(use-domain)=
## `$use_domain`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will qualify all local addresses (ones without the
"@host" portion) with the value of [$hostname](#hostname).  If *unset*, no
addresses will be qualified.

(use-envelope-from)=
## `$use_envelope_from`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will set the *envelope* sender of the message.
If [$envelope_from_address](#envelope-from-address) is *set*, it will be used as the sender
address. If *unset*, NeoMutt will attempt to derive the sender from the
"From:" header.

Note that this information is passed to sendmail command using the
`-f` command line switch. Therefore setting this option is not useful
if the [$sendmail](#sendmail) variable already contains `-f` or if the
executable pointed to by [$sendmail](#sendmail) doesn't support the `-f` switch.

(use-from)=
## `$use_from`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will generate the "From:" header field when
sending messages.  If *unset*, no "From:" header field will be
generated unless the user explicitly sets one using the "`my-header`"
command.

(use-ipv6)=
## `$use_ipv6`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will look for IPv6 addresses of hosts it tries to
contact. If this option is *unset*, NeoMutt will restrict itself to IPv4
addresses. Normally, the default should work.

(use-threads)=
## `$use_threads`

- **Type:** enumeration
- **Default:** unset

The style of threading used in the index. May be one of "flat" (no
threading), "threads" (threaded, with subthreads below root
message) or "reverse" (threaded, with subthreads above root
message). For convenience, the value "yes" is a synonym for
"threads", and "no" is a synonym for "flat".

If this variable is never set, then ``$sort`` controls whether
threading is used, `[$sort_aux](#sort-aux)` controls both the sorting of
threads and subthreads, and using `<sort-mailbox>` to select
threads affects only ``$sort``.  Once this variable is set,
attempting to set ``$sort`` to a value using "threads" will
warn, the value of ``$sort`` controls the sorting between
threads while `[$sort_aux](#sort-aux)` controls sorting within a thread,
and `<sort-mailbox>` toggles `[$use_threads](#use-threads)`.

Example:

```
set use_threads=yes
```

See the "Use Threads Feature" section for further explanation and
examples.

(user-agent)=
## `$user_agent`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will add a "User-Agent:" header to outgoing
messages, indicating which version of NeoMutt was used for composing
them.

(virtual-spool-file)=
## `$virtual_spool_file`

- **Type:** boolean
- **Default:** no

When *set*, NeoMutt will use the first Notmuch virtual mailbox as a
spool file.

(wait-key)=
## `$wait_key`

- **Type:** boolean
- **Default:** yes

Controls whether NeoMutt will ask you to press a key after an external
command has been invoked by these functions: `<shell-escape>`,
`<pipe-message>`, `<pipe-entry>`, `<print-message>`, and
`<print-entry>` commands.

It is also used when viewing attachments with "`auto-view`", provided
that the corresponding mailcap entry has a *needsterminal* flag,
and the external program is interactive.

When *set*, NeoMutt will always ask for a key. When *unset*, NeoMutt
will wait for a key only if the external command returned a non-zero status.

(weed)=
## `$weed`

- **Type:** boolean
- **Default:** yes

When *set*, NeoMutt will weed headers when displaying, forwarding,
or replying to messages.

Also see [$copy_decode_weed](#copy-decode-weed), [$pipe_decode_weed](#pipe-decode-weed), [$print_decode_weed](#print-decode-weed).

(wrap)=
## `$wrap`

- **Type:** number
- **Default:** 0

When set to a positive value, NeoMutt will wrap text at [$wrap](#wrap) characters.
When set to a negative value, NeoMutt will wrap text so that there are [$wrap](#wrap)
characters of empty space on the right side of the terminal. Setting it
to zero makes NeoMutt wrap at the terminal width.

Also see [$reflow_wrap](#reflow-wrap).

(wrap-headers)=
## `$wrap_headers`

- **Type:** number
- **Default:** 78

This option specifies the number of characters to use for wrapping
an outgoing message's headers. Allowed values are between 78 and 998
inclusive.

**Note:** This option usually shouldn't be changed. [RFC5233](https://www.rfc-editor.org/rfc/rfc5233.html)
recommends a line length of 78 (the default), so **please only change
this setting when you know what you're doing**.

(wrap-search)=
## `$wrap_search`

- **Type:** boolean
- **Default:** yes

Controls whether searches wrap around the end.

When *set*, searches will wrap around the first (or last) item. When
*unset*, incremental searches will not wrap.

(write-bcc)=
## `$write_bcc`

- **Type:** boolean
- **Default:** no

Controls whether NeoMutt writes out the "Bcc:" header when
preparing messages to be sent.  Some MTAs, such as Exim and
Courier, do not strip the "Bcc:" header; so it is advisable to
leave this unset unless you have a particular need for the header
to be in the sent message.

If NeoMutt is set to deliver directly via SMTP(see [$smtp_url](#smtp-url)),
this option does nothing: NeoMutt will never write out the "Bcc:"
header in this case.

Note this option only affects the sending of messages.  Fcc'ed
copies of a message will always contain the "Bcc:" header if
one exists.

(write-inc)=
## `$write_inc`

- **Type:** number
- **Default:** 10

When writing a mailbox, a message will be printed every
[$write_inc](#write-inc) messages to indicate progress.  If set to 0, only a
single message will be displayed before writing a mailbox.

Also see the [$read_inc](#read-inc), [$net_inc](#net-inc) and [$time_inc](#time-inc) variables and the
"**tuning**" section of the manual for performance considerations.

(x-comment-to)=
## `$x_comment_to`

- **Type:** boolean
- **Default:** no

If *set*, NeoMutt will add "X-Comment-To:" field (that contains full
name of original article author) to article that followuped to newsgroup.
