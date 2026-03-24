---
title: General Options
description: Reference for NeoMutt general configuration variables
keywords: neomutt, configuration, variables, general, settings
---

# General Options

General configuration variables control NeoMutt's core behaviour. These variables
do not belong to a specific feature domain (such as IMAP, PGP, or Sidebar).

--------------------------------------------------------------------------------

(abort-backspace)=
## `$abort_backspace`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set abort_backspace = yes
    ```

If _set_, hitting backspace against an empty prompt aborts the prompt.

--------------------------------------------------------------------------------

(abort-key)=
## `$abort_key`

- **Type:** [String](string)
- **Notes:** {ref}`Not Empty <general>`, {ref}`On Startup <general>`
- **Default:**
    ```neomuttrc
    set abort_key = "\007"
    ```

Specifies the key that can be used to abort prompts.
The format is the same as used in "bind" commands.
The default is equivalent to "Ctrl-G".
Note that the specified key should not be used in other bindings, as the abort operation has higher precedence and the binding will not have the desired effect.

Example:
```neomuttrc
set abort_key = "<Esc>"
```

Please note that when using <Esc> as the abort key, you may also want to set the environment variable ESCDELAY to a low value or even 0 which will reduce the time that ncurses waits to distinguish singular <Esc> key presses from the start of a terminal escape sequence.
The default time is 1000 milliseconds and thus quite noticeable.

--------------------------------------------------------------------------------

(ascii-chars)=
## `$ascii_chars`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set ascii_chars = no
    ```

If _set_, NeoMutt will use plain ASCII characters when displaying thread and attachment trees, instead of the default _ACS_ characters.

--------------------------------------------------------------------------------

(assumed-charset)=
## `$assumed_charset`

- **Type:** [String List](slist)
- **Notes:** [Colon-separated](slist), [Allow Empty](slist)
- **Default:** (empty)
    ```neomuttrc
    set assumed_charset = ""
    ```

This variable is a colon-separated list of character encoding schemes for messages without character encoding indication.
Header field values and message body content without character encoding indication would be assumed that they are written in one of this list.
By default, all the header fields and message body without any charset indication are assumed to be in "us-ascii".

For example, Japanese users might prefer this:
```neomuttrc
set assumed_charset = "iso-2022-jp:euc-jp:shift_jis:utf-8"
```

However, only the first content is valid for the message body.

--------------------------------------------------------------------------------

(attach-format)=
## `$attach_format`

- **Type:** [Expando](expando)
- **Notes:** {ref}`Not Empty <general>`
- **Default:**
    ```neomuttrc
    set attach_format = "%u%D%I %t%4n %T%d %> [%.7m/%.10M, %.6e%<C?, %C>, %s] "
    ```

This variable describes the format of the "attachment" menu.
The following `printf(3)`-style sequences are understood:

| Short  | Long Name             | Description                                                                                       |
|--------|-----------------------|---------------------------------------------------------------------------------------------------|
| `%C`   | `%{charset}`          | Charset                                                                                           |
| `%c`   | `%{charset-convert}`  | Requires charset conversion (`n` or `c`)                                                          |
| `%D`   | `%{deleted}`          | Deleted flag                                                                                      |
| `%d`   | `%{description}`      | Description (if none, falls back to `%F`)                                                         |
| `%e`   | `%{mime-encoding}`    | MIME content-transfer-encoding                                                                    |
| `%F`   | `%{file-disposition}` | Filename in content-disposition header (if none, falls back to `%f`)                              |
| `%f`   | `%{file}`             | Filename                                                                                          |
| `%I`   | `%{disposition}`      | Disposition (`I` for inline, `A` for attachment)                                                  |
| `%M`   | `%{mime-minor}`       | MIME subtype                                                                                      |
| `%m`   | `%{mime-major}`       | Major MIME type                                                                                   |
| `%n`   | `%{number}`           | Attachment number                                                                                 |
| `%Q`   | `%{attach-qualifies}` | `Q`, if MIME part qualifies for attachment counting                                               |
| `%s`   | `%{file-size}`        | Size (see **Size Format**)                                                                        |
| `%T`   | `%{tree}`             | Graphic tree characters                                                                           |
| `%t`   | `%{tagged}`           | Tagged flag                                                                                       |
| `%u`   | `%{unlink}`           | Unlink (=to delete) flag                                                                          |
| `%X`   | `%{attach-count}`     | Number of qualifying MIME parts in this part and its children                                     |
|        |                       | (see the [`$attachments`](#attachment-searching-and-counting) section for possible speed effects) |
| `%*X`  | `%{padding-soft:X}`   | Soft-fill with character `X` as pad                                                               |
| `%>X`  | `%{padding-hard:X}`   | Right justify the rest of the string and pad with character `X`                                   |
| `%\|X` | `%{padding-eol:X}`    | Pad to the end of the line with character `X`                                                     |

For an explanation of "soft-fill", see the [$index_format](index-format) documentation.

--------------------------------------------------------------------------------

(auto-edit)=
## `$auto_edit`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set auto_edit = no
    ```

When _set_ along with [$edit_headers](edit-headers), NeoMutt will skip the initial send-menu (prompting for subject and recipients) and allow you to immediately begin editing the body of your message.
The send-menu may still be accessed once you have finished editing the body of your message.

**Note:** when this option is _set_, you can't use send-hooks that depend on the recipients when composing a new (non-reply) message, as the initial list of recipients is empty.

Also see [$fast_reply](fast-reply).

--------------------------------------------------------------------------------

(auto-tag)=
## `$auto_tag`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set auto_tag = no
    ```

When _set_, functions in the _index_ menu which affect a message will be applied to all tagged messages (if there are any).
When unset, you must first use the `<tag-prefix>` function (bound to ";" by default) to make the next function apply to all tagged messages.

--------------------------------------------------------------------------------

(braille-friendly)=
## `$braille_friendly`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set braille_friendly = no
    ```

When this variable is _set_, NeoMutt will place the cursor at the beginning of the current line in menus, even when the [$arrow_cursor](arrow-cursor) variable is _unset_, making it easier for blind persons using Braille displays to follow these menus.
The option is _unset_ by default because many visual terminals don't permit making the cursor invisible.

--------------------------------------------------------------------------------

(charset)=
## `$charset`

- **Type:** [String](string)
- **Notes:** {ref}`Not Empty <general>`, {ref}`Charset Single <general>`
- **Default:** (empty)
    ```neomuttrc
    set charset = ""
    ```

Character set your terminal uses to display and enter textual data.
It is also the fallback for [$send_charset](send-charset).

Upon startup NeoMutt tries to derive this value from environment variables such as `$$$LC_CTYPE` or `$$$LANG`.

**Note:** It should only be set in case NeoMutt isn't able to determine the character set used correctly.

--------------------------------------------------------------------------------

(color-directcolor)=
## `$color_directcolor`

- **Type:** [Boolean](bool)
- **Notes:** {ref}`On Startup <general>`
- **Default:**
    ```neomuttrc
    set color_directcolor = no
    ```

When _set_, NeoMutt will use and allow 24-bit colours (aka truecolor aka directcolor).
For colours to work properly support from the terminal is required as well as a properly set TERM environment variable advertising the terminals directcolor capability, e.g.
"TERM=xterm-direct".

NeoMutt tries to detect whether the terminal supports 24-bit colours and enables this variable if it does.
If this fails for some reason, you can force 24-bit colours by setting this variable manually.
You may also try to force a certain TERM environment variable by starting NeoMutt from a terminal as follows (this results in wrong colours if the terminal does not implement directcolors):

```sh
TERM=xterm-direct neomutt
```

Note: This variable must be set before using any `color` commands.

--------------------------------------------------------------------------------

(config-charset)=
## `$config_charset`

- **Type:** [String](string)
- **Default:** (empty)
    ```neomuttrc
    set config_charset = ""
    ```

When defined, NeoMutt will recode commands in rc files from this encoding to the current character set as specified by [$charset](charset) and aliases written to [$alias_file](alias-file) from the current character set.

Please note that if setting [$charset](charset) it must be done before setting [$config_charset](config-charset).

Recoding should be avoided as it may render unconvertible characters as question marks which can lead to undesired side effects (for example in regular expressions).

--------------------------------------------------------------------------------

(confirm-append)=
## `$confirm_append`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set confirm_append = yes
    ```

When _set_, NeoMutt will prompt for confirmation when appending messages to an existing mailbox.

--------------------------------------------------------------------------------

(confirm-create)=
## `$confirm_create`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set confirm_create = yes
    ```

When _set_, NeoMutt will prompt for confirmation when saving messages to a mailbox which does not yet exist before creating it.

--------------------------------------------------------------------------------

(copy-decode-weed)=
## `$copy_decode_weed`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set copy_decode_weed = no
    ```

Controls whether NeoMutt will weed headers when invoking the `<decode-copy>` or `<decode-save>` functions.

--------------------------------------------------------------------------------

(date-format)=
## `$date_format`

- **Type:** [String](string)
- **Notes:** {ref}`Not Empty <general>`
- **Default:**
    ```neomuttrc
    set date_format = "!%a, %b %d, %Y at %I:%M:%S%p %Z"
    ```

Instead of using [$date_format](date-format) it is encouraged to use "%[fmt]" directly in the corresponding format strings, where "fmt" is the value of [$date_format](date-format).
This allows for a more fine grained control of the different menu needs.

This variable controls the format of the date printed by the "%d" sequence in [$index_format](index-format).
This is passed to the `strftime(3)`
function to process the date, see the man page for the proper syntax.

Unless the first character in the string is a bang ("!"), the month and week day names are expanded according to the locale.
If the first character in the string is a bang, the bang is discarded, and the month and week day names in the rest of the string are expanded in the _C_ locale (that is in US English).

Format strings using this variable are:

UI: [$folder_format](folder-format), [$index_format](index-format), [$mailbox_folder_format](mailbox-folder-format), [$message_format](message-format).

Composing: [$attribution_intro](attribution-intro), [$forward_attribution_intro](forward-attribution-intro), [$forward_attribution_trailer](forward-attribution-trailer), [$forward_format](forward-format), [$indent_string](indent-string).

--------------------------------------------------------------------------------

(debug-file)=
## `$debug_file`

- **Type:** [Path (String)](path)
- **Notes:** [File only](path)
- **Default:**
    ```neomuttrc
    set debug_file = "~/.neomuttdebug"
    ```

Debug logging is controlled by the variables `[$debug_file](debug-file)` and `[$debug_level](debug-level)`.
`[$debug_file](debug-file)` specifies the root of the filename.
NeoMutt will add "0" to the end.
Each time NeoMutt is run with logging enabled, the log files are rotated.
A maximum of five log files are kept, numbered 0 (most recent) to 4 (oldest).

This option can be enabled on the command line, `neomutt -l mylog`

See also: `[$debug_level](debug-level)`

--------------------------------------------------------------------------------

(debug-level)=
## `$debug_level`

- **Type:** [Number](number)
- **Default:**
    ```neomuttrc
    set debug_level = 0
    ```

Debug logging is controlled by the variables `[$debug_file](debug-file)` and `[$debug_level](debug-level)`.

The debug level controls how much information is saved to the log file.
If you have a problem with NeoMutt, then enabling logging may help find the cause.
Levels 1-3 will usually provide enough information for writing a bug report.
Levels 4,5 will be extremely verbose.

Warning: Logging at high levels may save private information to the file.

This option can be enabled on the command line, `neomutt -d 2`

See also: `[$debug_file](debug-file)`

--------------------------------------------------------------------------------

(delete)=
## `$delete`

- **Type:** [Quad-Option](quad)
- **Default:**
    ```neomuttrc
    set delete = ask-yes
    ```

Controls whether or not messages are really deleted when closing or synchronizing a mailbox.
If set to _yes_, messages marked for deleting will automatically be purged without prompting.
If set to _no_, messages marked for deletion will be kept in the mailbox.

--------------------------------------------------------------------------------

(delete-untag)=
## `$delete_untag`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set delete_untag = yes
    ```

If this option is _set_, NeoMutt will untag messages when marking them for deletion.
This applies when you either explicitly delete a message, or when you save it to another folder.

--------------------------------------------------------------------------------

(devel-security)=
## `$devel_security`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set devel_security = no
    ```

If this option is _set_, NeoMutt will enable the **Security** development features.
See: https://github.com/neomutt/neomutt/discussions/4251

--------------------------------------------------------------------------------

(editor)=
## `$editor`

- **Type:** [Command (String)](string)
- **Notes:** {ref}`Not Empty <general>`
- **Default:** (empty)
    ```neomuttrc
    set editor = ""
    ```

This variable specifies which editor is used by NeoMutt.
It defaults to the value of the `$$$VISUAL`, or `$$$EDITOR`, environment variable, or to the string "vi" if neither of those are set.

The `[$editor](editor)` string may contain a _%s_ escape, which will be replaced by the name of the file to be edited.
If the _%s_ escape does not appear in `[$editor](editor)`, a space and the name to be edited are appended.

The resulting string is then executed by running:

```sh
sh -c 'string'
```

where _string_ is the expansion of `[$editor](editor)` described above.

--------------------------------------------------------------------------------

(flag-safe)=
## `$flag_safe`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set flag_safe = no
    ```

If set, flagged messages can't be deleted.

--------------------------------------------------------------------------------

(folder)=
## `$folder`

- **Type:** [Mailbox (String)](string)
- **Default:**
    ```neomuttrc
    set folder = "~/Mail"
    ```

Specifies the default location of your mailboxes.
A "+" or "=" at the beginning of a pathname will be expanded to the value of this variable.
Note that if you change this variable (from the default)
value you need to make sure that the assignment occurs _before_ you use "+" or "=" for any other variables since expansion takes place when handling the "$mailboxes" command.

--------------------------------------------------------------------------------

(forward-decode)=
## `$forward_decode`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set forward_decode = yes
    ```

Controls the decoding of complex MIME messages into `text/plain` when forwarding a message.
The message header is also [RFC2047](https://www.rfc-editor.org/rfc/rfc2047.html) decoded.
This variable is only used, if [$mime_forward](mime-forward) is _unset_, otherwise [$mime_forward_decode](mime-forward-decode) is used instead.

--------------------------------------------------------------------------------

(forward-quote)=
## `$forward_quote`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set forward_quote = no
    ```

When _set_, forwarded messages included in the main body of the message (when [$mime_forward](mime-forward) is _unset_) will be quoted using [$indent_string](indent-string).

--------------------------------------------------------------------------------

(from)=
## `$from`

- **Type:** {ref}`Address <address>`
- **Default:** (empty)
    ```neomuttrc
    set from = ""
    ```

When _set_, this variable contains a default "from" address.
It can be overridden using "$my-header" (including from a "$send-hook") and [$reverse_name](reverse-name).
This variable is ignored if [$use_from](use-from) is _unset_.

If not specified, then it may be read from the environment variable `$$$EMAIL`.

--------------------------------------------------------------------------------

(gecos-mask)=
## `$gecos_mask`

- **Type:** [Regular Expression](regex)
- **Default:**
    ```neomuttrc
    set gecos_mask = "^[^,]*"
    ```

A regular expression used by NeoMutt to parse the GECOS field of a password entry when expanding the alias.
The default value will return the string up to the first "," encountered.
If the GECOS field contains a string like "lastname, firstname" then you should set it to "`.*`".

This can be useful if you see the following behavior: you address an e-mail to user ID "stevef" whose full name is "Steve Franklin".
If NeoMutt expands "stevef" to '"Franklin" stevef@foo.bar' then you should set the [$gecos_mask](gecos-mask) to a regular expression that will match the whole name so NeoMutt will expand "Franklin" to "Franklin, Steve".

--------------------------------------------------------------------------------

(header)=
## `$header`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set header = no
    ```

When _set_, this variable causes NeoMutt to include the header of the message you are replying to into the edit buffer.
The [$weed](weed) setting applies.

--------------------------------------------------------------------------------

(hostname)=
## `$hostname`

- **Type:** [String](string)
- **Default:** (empty)
    ```neomuttrc
    set hostname = ""
    ```

Specifies the fully-qualified hostname of the system NeoMutt is running on containing the host's name and the DNS domain it belongs to.
It is used as the domain part (after "@") for local email addresses.

If not specified in a config file, then NeoMutt will try to determine the hostname itself.

Optionally, NeoMutt can be compiled with a fixed domain name.

Also see [$use_domain](use-domain) and [$hidden_host](hidden-host).

--------------------------------------------------------------------------------

(indent-string)=
## `$indent_string`

- **Type:** [Expando](expando)
- **Default:**
    ```neomuttrc
    set indent_string = "> "
    ```

Specifies the string to prepend to each line of text quoted in a message to which you are replying.
You are strongly encouraged not to change this value, as it tends to agitate the more fanatical netizens.

The value of this option is ignored if [$text_flowed](text-flowed) is set, because the quoting mechanism is strictly defined for format=flowed.

This option is a format string, please see the description of [$index_format](index-format) for supported `printf(3)`-style sequences.

--------------------------------------------------------------------------------

(keep-flagged)=
## `$keep_flagged`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set keep_flagged = no
    ```

If _set_, read messages marked as flagged will not be moved from your spool mailbox to your [`$mbox`](#mbox) mailbox or to the "mbox" specified by a $mbox-hook command.

Note that [$keep_flagged](keep-flagged) only has an effect if [$move](move) is set.

--------------------------------------------------------------------------------

(local-date-header)=
## `$local_date_header`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set local_date_header = yes
    ```

If _set_, the date in the Date header of emails that you send will be in your local timezone.
If unset a UTC date will be used instead to avoid leaking information about your current location.

--------------------------------------------------------------------------------

(mail-check)=
## `$mail_check`

- **Type:** [Number](number)
- **Notes:** {ref}`Not Negative <general>`
- **Default:**
    ```neomuttrc
    set mail_check = 5
    ```

This variable configures how often (in seconds) NeoMutt should look for new mail.
Also see the [$timeout](timeout) variable.

--------------------------------------------------------------------------------

(mail-check-recent)=
## `$mail_check_recent`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set mail_check_recent = yes
    ```

When _set_, NeoMutt will only notify you about new mail that has been received since the last time you opened the mailbox.
When _unset_, NeoMutt will notify you if any new mail exists in the mailbox, regardless of whether you have visited it recently.

--------------------------------------------------------------------------------

(mail-check-stats)=
## `$mail_check_stats`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set mail_check_stats = no
    ```

When _set_, NeoMutt will periodically calculate message statistics of a mailbox while polling for new mail.
It will check for unread, flagged, and total message counts.
(Note: IMAP mailboxes only support unread and total counts).

Because this operation is more performance intensive, it defaults to _unset_, and has a separate option, [$mail_check_stats_interval](mail-check-stats-interval), to control how often to update these counts.

Message statistics can also be explicitly calculated by invoking the `<check-stats>` function.

--------------------------------------------------------------------------------

(mail-check-stats-interval)=
## `$mail_check_stats_interval`

- **Type:** [Number](number)
- **Notes:** {ref}`Not Negative <general>`
- **Default:**
    ```neomuttrc
    set mail_check_stats_interval = 60
    ```

When [$mail_check_stats](mail-check-stats) is _set_, this variable configures how often (in seconds) NeoMutt will update message counts.

--------------------------------------------------------------------------------

(mark-old)=
## `$mark_old`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set mark_old = yes
    ```

Controls whether or not NeoMutt marks _new_ **unread** messages as _old_ if you exit a mailbox without reading them.
With this option _set_, the next time you start NeoMutt, the messages will show up with an "O" next to them in the index menu, indicating that they are old.

--------------------------------------------------------------------------------

(mbox)=
## `$mbox`

- **Type:** [Mailbox (String)](string)
- **Default:**
    ```neomuttrc
    set mbox = "~/mbox"
    ```

This specifies the folder into which read mail in your [$spool_file](spool-file) folder will be appended.

Also see the [$move](move) variable.

--------------------------------------------------------------------------------

(mbox-type)=
## `$mbox_type`

- **Type:** [Enumeration](enum)
- **Default:**
    ```neomuttrc
    set mbox_type = "mbox"
    ```

The default mailbox type used when creating new folders.

| Values    |
|-----------|
| `maildir` |
| `mbox`    |
| `mh`      |
| `mmdf`    |

This can also be set using the `-m` command-line option.

--------------------------------------------------------------------------------

(message-cache-clean)=
## `$message_cache_clean`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set message_cache_clean = no
    ```

If _set_, NeoMutt will clean out obsolete entries from the message cache when the mailbox is synchronized.
You probably only want to set it every once in a while, since it can be a little slow (especially for large folders).

--------------------------------------------------------------------------------

(message-cache-dir)=
## `$message_cache_dir`

- **Type:** [Path (String)](path)
- **Notes:** [Directory only](path)
- **Default:** (empty)
    ```neomuttrc
    set message_cache_dir = ""
    ```

Set this to a directory and NeoMutt will cache copies of messages from your IMAP and POP servers here.
You are free to remove entries at any time.

When setting this variable to a directory, NeoMutt needs to fetch every remote message only once and can perform regular expression searches as fast as for local folders.

Also see the [$message_cache_clean](message-cache-clean) variable.

--------------------------------------------------------------------------------

(meta-key)=
## `$meta_key`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set meta_key = no
    ```

If _set_, forces NeoMutt to interpret keystrokes with the high bit (bit 8) set as if the user had pressed the Esc key and whatever key remains after having the high bit removed.
For example, if the key pressed has an ASCII value of `0xf8`, then this is treated as if the user had pressed Esc then "x".
This is because the result of removing the high bit from `0xf8` is `0x78`, which is the ASCII character "x".

--------------------------------------------------------------------------------

(move)=
## `$move`

- **Type:** [Quad-Option](quad)
- **Default:**
    ```neomuttrc
    set move = no
    ```

If this variable is _set_, then NeoMutt will move read messages from your spool mailbox to your [`$mbox`](#mbox) mailbox or to the "mbox" specified by a $mbox-hook command.

See also [$keep_flagged](keep-flagged).

--------------------------------------------------------------------------------

(pipe-decode)=
## `$pipe_decode`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pipe_decode = no
    ```

Used in connection with the `<pipe-message>` function.
When _unset_, NeoMutt will pipe the messages without any preprocessing.
When _set_, NeoMutt will attempt to decode the messages first.

Also see [$pipe_decode_weed](pipe-decode-weed), which controls whether headers will be weeded when this is _set_.

--------------------------------------------------------------------------------

(pipe-decode-weed)=
## `$pipe_decode_weed`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pipe_decode_weed = yes
    ```

For `<pipe-message>`, when [$pipe_decode](pipe-decode) is set, this further controls whether NeoMutt will weed headers.

--------------------------------------------------------------------------------

(pipe-sep)=
## `$pipe_sep`

- **Type:** [String](string)
- **Default:**
    ```neomuttrc
    set pipe_sep = "\n"
    ```

The separator to add between messages when piping a list of tagged messages to an external Unix command.

--------------------------------------------------------------------------------

(pipe-split)=
## `$pipe_split`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set pipe_split = no
    ```

Used in connection with the `<pipe-message>` function following `<tag-prefix>`.  
If this variable is _unset_, when piping a list of tagged messages NeoMutt will concatenate the messages and will pipe them all concatenated.
When _set_, NeoMutt will pipe the messages one by one.
In both cases the messages are piped in the current sorted order, and the [$pipe_sep](pipe-sep) separator is added after each message.

--------------------------------------------------------------------------------

(postponed)=
## `$postponed`

- **Type:** [Mailbox (String)](string)
- **Default:**
    ```neomuttrc
    set postponed = "~/postponed"
    ```

NeoMutt allows you to indefinitely "$postpone sending a message" which you are editing.
When you choose to postpone a message, NeoMutt saves it in the mailbox specified by this variable.

Also see the [$postpone](postpone) variable.

--------------------------------------------------------------------------------

(print)=
## `$print`

- **Type:** [Quad-Option](quad)
- **Default:**
    ```neomuttrc
    set print = ask-no
    ```

Controls whether or not NeoMutt really prints messages.
This is set to "ask-no" by default, because some people accidentally hit "p" often.

--------------------------------------------------------------------------------

(print-command)=
## `$print_command`

- **Type:** [Command (String)](string)
- **Default:**
    ```neomuttrc
    set print_command = "lpr"
    ```

This specifies the command pipe that should be used to print messages.

--------------------------------------------------------------------------------

(print-decode)=
## `$print_decode`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set print_decode = yes
    ```

Used in connection with the `<print-message>` function.
If this option is _set_, the message is decoded before it is passed to the external command specified by [$print_command](print-command).
If this option is _unset_, no processing will be applied to the message when printing it.
The latter setting may be useful if you are using some advanced printer filter which is able to properly format e-mail messages for printing.

Also see [$print_decode_weed](print-decode-weed), which controls whether headers will be weeded when this is _set_.

--------------------------------------------------------------------------------

(print-decode-weed)=
## `$print_decode_weed`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set print_decode_weed = yes
    ```

For `<print-message>`, when [$print_decode](print-decode) is set, this further controls whether NeoMutt will weed headers.

--------------------------------------------------------------------------------

(print-split)=
## `$print_split`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set print_split = no
    ```

Used in connection with the `<print-message>` function.
If this option is _set_, the command specified by [$print_command](print-command) is executed once for each message which is to be printed.
If this option is _unset_, the command specified by [$print_command](print-command) is executed only once, and all the messages are concatenated, with a form feed as the message separator.

Those who use the `enscript(1)` program's mail-printing mode will most likely want to _set_ this option.

--------------------------------------------------------------------------------

(quote-regex)=
## `$quote_regex`

- **Type:** [Regular Expression](regex)
- **Default:**
    ```neomuttrc
    set quote_regex = "^([ \t]*[|>:}#])+"
    ```

A regular expression used in the internal pager to determine quoted sections of text in the body of a message.
Quoted text may be filtered out using the `<toggle-quoted>` command, or colored according to the "color quoted" family of directives.

Higher levels of quoting may be colored differently ("color quoted1", "color quoted2", etc.).
The quoting level is determined by removing the last character from the matched text and recursively reapplying the regular expression until it fails to produce a match.

Match detection may be overridden by the [$smileys](smileys) regular expression.

--------------------------------------------------------------------------------

(real-name)=
## `$real_name`

- **Type:** [String](string)
- **Default:** (empty)
    ```neomuttrc
    set real_name = ""
    ```

This variable specifies what "real" or "personal" name should be used when sending messages.

If not specified, then the user's "real name" will be read from `/etc/passwd`.
This option will not be used, if "[$from](from)" is set.

--------------------------------------------------------------------------------

(record)=
## `$record`

- **Type:** [Mailbox (String)](string)
- **Default:**
    ```neomuttrc
    set record = "~/sent"
    ```

This specifies the file into which your outgoing messages should be appended.
(This is meant as the primary method for saving a copy of your messages, but another way to do this is using the "$my-header" command to create a "Bcc:" field with your email address in it.)

The value of [$record](record) is overridden by the [$force_name](force-name) and [$save_name](save-name) variables, and the "$fcc-hook" command.
Also see [$copy](copy) and [$write_bcc](write-bcc).

--------------------------------------------------------------------------------

(resolve)=
## `$resolve`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set resolve = yes
    ```

When _set_, the cursor in a list will be automatically advanced to the next (possibly undeleted) message/attachment/entry whenever a command that modifies the current message/attachment/entry is executed.

Examples of such commands are tagging a message, deleting an entry, or saving an attachment.

--------------------------------------------------------------------------------

(resume-edited-draft-files)=
## `$resume_edited_draft_files`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set resume_edited_draft_files = yes
    ```

If _set_, draft files previously edited (via `-E -H` on the command line) will have [$resume_draft_files](resume-draft-files) automatically set when they are used as a draft file again.

The first time a draft file is saved, NeoMutt will add a header, X-Mutt-Resume-Draft to the saved file.
The next time the draft file is read in, if NeoMutt sees the header, it will set [$resume_draft_files](resume-draft-files).

This option is designed to prevent multiple signatures, user-defined headers, and other processing effects from being made multiple times to the draft file.

--------------------------------------------------------------------------------

(save-address)=
## `$save_address`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set save_address = no
    ```

If _set_, NeoMutt will take the sender's full address when choosing a default folder for saving a mail.
If [$save_name](save-name) or [$force_name](force-name) is _set_ too, the selection of the Fcc folder will be changed as well.

--------------------------------------------------------------------------------

(save-empty)=
## `$save_empty`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set save_empty = yes
    ```

When _unset_, mailboxes which contain no saved messages will be removed when closed (the exception is [$spool_file](spool-file) which is never removed).
If _set_, mailboxes are never removed.

**Note:** This only applies to mbox and MMDF folders, NeoMutt does not delete MH and Maildir directories.

--------------------------------------------------------------------------------

(send-charset)=
## `$send_charset`

- **Type:** [String List](slist)
- **Notes:** [Colon-separated](slist), [Allow Empty](slist), {ref}`Charset Strict <general>`
- **Default:**
    ```neomuttrc
    set send_charset = "us-ascii:iso-8859-1:utf-8"
    ```

A colon-delimited list of character sets for outgoing messages.
NeoMutt will use the first character set into which the text can be converted exactly.
If your [$charset](charset) is not "iso-8859-1" and recipients may not understand "UTF-8", it is advisable to include in the list an appropriate widely used standard character set (such as "iso-8859-2", "koi8-r" or "iso-2022-jp") either instead of or after "iso-8859-1".

In case the text can't be converted into one of these exactly, NeoMutt uses [$charset](charset) as a fallback.

--------------------------------------------------------------------------------

(shell)=
## `$shell`

- **Type:** [Command (String)](string)
- **Default:**
    ```neomuttrc
    set shell = "/bin/sh"
    ```

Command to use when spawning a subshell.
If not specified, then the user's login shell from `/etc/passwd` is used.

--------------------------------------------------------------------------------

(size-show-bytes)=
## `$size_show_bytes`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set size_show_bytes = no
    ```

If _set_, message sizes will display bytes for values less than 1 kilobyte.
See $formatstrings-size.

--------------------------------------------------------------------------------

(size-show-fractions)=
## `$size_show_fractions`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set size_show_fractions = yes
    ```

If _set_, message sizes will be displayed with a single decimal value for sizes from 0 to 10 kilobytes and 1 to 10 megabytes.
See $formatstrings-size.

--------------------------------------------------------------------------------

(size-show-mb)=
## `$size_show_mb`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set size_show_mb = yes
    ```

If _set_, message sizes will display megabytes for values greater than or equal to 1 megabyte.
See $formatstrings-size.

--------------------------------------------------------------------------------

(size-units-on-left)=
## `$size_units_on_left`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set size_units_on_left = no
    ```

If _set_, message sizes units will be displayed to the left of the number.
See $formatstrings-size.

--------------------------------------------------------------------------------

(sleep-time)=
## `$sleep_time`

- **Type:** [Number](number)
- **Notes:** {ref}`Not Negative <general>`
- **Default:**
    ```neomuttrc
    set sleep_time = 1
    ```

Specifies time, in seconds, to pause while displaying certain informational messages, while moving from folder to folder and after expunging messages from the current folder.
The default is to pause one second, so a value of zero for this option suppresses the pause.

--------------------------------------------------------------------------------

(sort)=
## `$sort`

- **Type:** [Sort Order](sort-order)
- **Notes:** [Reverse](sort-order), [Last](sort-order)
- **Default:**
    ```neomuttrc
    set sort = "date"
    ```

Specifies how to sort messages in the "index" menu.

| Value           | Sort by                                      |
|-----------------|----------------------------------------------|
| `date`          | The date the email was sent                  |
| `date-received` | When the message was delivered locally       |
| `from`          | The email's From field                       |
| `label`         | The emails label                             |
| `score`         | The email's score                            |
| `size`          | The size of the email                        |
| `spam`          | The email's spam score                       |
| `subject`       | The email's subject                          |
| `threads`       | Email threads                                |
| `to`            | The email's To field                         |
| `unsorted`      | The order the messages appear in the mailbox |

| Deprecated Value | Use this instead |
|------------------|------------------|
| `date-sent`      | `date`           |
| `mailbox-order`  | `unsorted`       |

You may optionally use the "reverse-" prefix to specify reverse sorting order, or the "last-" prefix to sort threads based on the corresponding attribute of the last descendant rather than the thread root.
If both prefixes are in use, "reverse-" must come before "last-".  The "last-" prefix has no effect on a flat view.

Any ties in the primary sort are broken by [$sort_aux](sort-aux).
When [$use_threads](use-threads) is "threads" or "reverse", [$sort](sort) controls the sorting between threads, and [$sort_aux](sort-aux) controls the sorting within a thread.

The values of "threads" and "reverse-threads" are legacy options, which cause the value of `[$sort_aux](sort-aux)` to also control sorting between threads, and they may not be used with the "last-" prefix.
The preferred way to enable a threaded view is via `[$use_threads](use-threads)`.  
This variable can also be set via the `<sort-mailbox>` and `<sort-reverse>` functions.

Note: When [$use_threads](use-threads) is "threads", the last thread sorts to the bottom; when it is "reversed", the last thread sorts to the top.
The use of "reverse-" in [$sort](sort) swaps which end the last thread will sort to.

See the "Use Threads Feature" section for further explanation and examples, https://neomutt.org/feature/use-threads

--------------------------------------------------------------------------------

(sort-aux)=
## `$sort_aux`

- **Type:** [Sort Order](sort-order)
- **Notes:** [Reverse](sort-order), [Last](sort-order)
- **Default:**
    ```neomuttrc
    set sort_aux = "date"
    ```

This provides a secondary sort for messages in the "index" menu, used when the [$sort](sort) value is equal for two messages.

When sorting by threads, this variable controls how subthreads are sorted within a single thread (for the order between threads, see [$sort](sort)).
This can be set to any value that [$sort](sort) can, including with the use of "reverse-" and "last-" prefixes, except for variations using "threads" (in that case, NeoMutt will just use "date").

For instance,
```neomuttrc
set sort_aux = last-date-received
```

would mean that if a new message is received in a thread, that subthread becomes the last one displayed (or the first, if you have "`set use_threads = reverse`".)  When using [$use_threads](use-threads), it is more common to use "last-" with [$sort](sort) and not with [$sort_aux](sort-aux).

See the "Use Threads Feature" section for further explanation and examples, https://neomutt.org/feature/use-threads

--------------------------------------------------------------------------------

(spool-file)=
## `$spool_file`

- **Type:** [Mailbox (String)](string)
- **Default:** (empty)
    ```neomuttrc
    set spool_file = ""
    ```

If your spool mailbox is in a non-default place where NeoMutt can't find it, you can specify its location with this variable.
The description from "named-mailboxes" may be used for the spool_file.

If not specified, then the environment variables `$$$MAIL` and `$$$MAILDIR` will be checked.

--------------------------------------------------------------------------------

(status-on-top)=
## `$status_on_top`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set status_on_top = no
    ```

Setting this variable causes the "status bar" to be displayed on the first line of the screen rather than near the bottom.
If [`$help`](#help) is _set_ too, it'll be placed at the bottom.

--------------------------------------------------------------------------------

(suspend)=
## `$suspend`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set suspend = yes
    ```

When _unset_, NeoMutt won't stop when the user presses the terminal's _susp_ key, usually "^Z".
This is useful if you run NeoMutt inside an xterm using a command like "`xterm -e neomutt`".

On startup NeoMutt tries to detect if it is the process session leader.
If so, the default of $suspend is "no" otherwise "yes".  This default covers the above mentioned use case of "`xterm -e neomutt`".

--------------------------------------------------------------------------------

(text-flowed)=
## `$text_flowed`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set text_flowed = no
    ```

When _set_, NeoMutt will generate "format=flowed" bodies with a content type of "`text/plain; format=flowed`".
This format is easier to handle for some mailing software, and generally just looks like ordinary text.
To actually make use of this format's features, you'll need support in your editor.

The option only controls newly composed messages.
Postponed messages, resent messages, and draft messages (via -H on the command line) will use the content-type of the source message.

Note that [$indent_string](indent-string) is ignored when this option is _set_.

--------------------------------------------------------------------------------

(timeout)=
## `$timeout`

- **Type:** [Number](number)
- **Notes:** {ref}`Not Negative <general>`
- **Default:**
    ```neomuttrc
    set timeout = 600
    ```

This variable sets the time interval in seconds in which _timeout-hook_ commands get executed while waiting for user input either idling in menus or in an interactive prompt.

A value of zero disables timeout hooks.

--------------------------------------------------------------------------------

(tmp-dir)=
## `$tmp_dir`

- **Type:** [Path (String)](path)
- **Notes:** [Directory only](path), {ref}`Not Empty <general>`
- **Default:**
    ```neomuttrc
    set tmp_dir = "/tmp"
    ```

This variable allows you to specify where NeoMutt will place its temporary files needed for displaying messages.

If this variable is not set, the environment variable `$$$TMPDIR` is used.
Failing that, then "`/tmp`" is used.

--------------------------------------------------------------------------------

(tmp-draft-dir)=
## `$tmp_draft_dir`

- **Type:** [Path (String)](path)
- **Notes:** [Directory only](path), {ref}`Not Empty <general>`
- **Default:**
    ```neomuttrc
    set tmp_draft_dir = "/var/tmp"
    ```

This variable allows you to specify where NeoMutt will place its temporary files when composing messages.

If this variable is not set, the environment variable `$$$TMPDIR` is used.
Failing that, then "`/var/tmp`" is used.

It is recommended that this be set to a directory whose contents won't be removed during an unanticipated reboot, so that draft files will survive a crash or other unplanned computer shutdown.

--------------------------------------------------------------------------------

(trash)=
## `$trash`

- **Type:** [Mailbox (String)](string)
- **Default:** (empty)
    ```neomuttrc
    set trash = ""
    ```

If set, this variable specifies the path of the trash folder where the mails marked for deletion will be moved, instead of being irremediably purged.

NOTE: When you delete a message in the trash folder, it is really deleted, so that you have a way to clean the trash.

--------------------------------------------------------------------------------

(use-domain)=
## `$use_domain`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set use_domain = yes
    ```

When _set_, NeoMutt will qualify all local addresses (ones without the "@host" portion) with the value of [$hostname](hostname).
If _unset_, no addresses will be qualified.

--------------------------------------------------------------------------------

(use-threads)=
## `$use_threads`

- **Type:** [Enumeration](enum)
- **Default:**
    ```neomuttrc
    set use_threads = "unset"
    ```

The style of threading used in the index.

| Value     | Meaning                                      |
|-----------|----------------------------------------------|
| `flat`    | No threading                                 |
| `threads` | Threaded, with subthreads below root message |
| `reverse` | Threaded, with subthreads above root message |
| `yes`     | Synonym for `threads`                        |
| `no`      | Synonym for `flat`                           |

If this variable is never set, then `[$sort](sort)` controls whether threading is used, `[$sort_aux](sort-aux)` controls both the sorting of threads and subthreads, and using `<sort-mailbox>` to select threads affects only `[$sort](sort)`.
Once this variable is set, attempting to set `[$sort](sort)` to a value using "threads" will warn, the value of `[$sort](sort)` controls the sorting between threads while `[$sort_aux](sort-aux)` controls sorting within a thread, and `<sort-mailbox>` toggles `[$use_threads](use-threads)`.

Example:
```neomuttrc
set use_threads = yes
```

See the "Use Threads Feature" section for further explanation and examples.

--------------------------------------------------------------------------------

(wait-key)=
## `$wait_key`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set wait_key = yes
    ```

Controls whether NeoMutt will ask you to press a key after an external command has been invoked by these functions: `<shell-escape>`, `<pipe-message>`, `<pipe-entry>`, `<print-message>`, and `<print-entry>` commands.

It is also used when viewing attachments with "$auto-view", provided that the corresponding mailcap entry has a _needsterminal_ flag, and the external program is interactive.

When _set_, NeoMutt will always ask for a key.
When _unset_, NeoMutt will wait for a key only if the external command returned a non-zero status.

--------------------------------------------------------------------------------

(weed)=
## `$weed`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set weed = yes
    ```

When _set_, NeoMutt will weed headers when displaying, forwarding, or replying to messages.

Also see [$copy_decode_weed](copy-decode-weed), [$pipe_decode_weed](pipe-decode-weed), [$print_decode_weed](print-decode-weed).

--------------------------------------------------------------------------------

(wrap)=
## `$wrap`

- **Type:** [Number](number)
- **Default:**
    ```neomuttrc
    set wrap = 0
    ```

When set to a positive value, NeoMutt will wrap text at [$wrap](wrap) characters.
When set to a negative value, NeoMutt will wrap text so that there are [$wrap](wrap) characters of empty space on the right side of the terminal.
Setting it to zero makes NeoMutt wrap at the terminal width.

Also see [$reflow_wrap](reflow-wrap).

--------------------------------------------------------------------------------

(wrap-search)=
## `$wrap_search`

- **Type:** [Boolean](bool)
- **Default:**
    ```neomuttrc
    set wrap_search = yes
    ```

Controls whether searches wrap around the end.

When _set_, searches will wrap around the first (or last) item.
When _unset_, incremental searches will not wrap.

