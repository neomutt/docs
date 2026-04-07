---
title: General Options
description: Core configuration variables for NeoMutt behavior, character sets, colors, sorting, threading, and folders.
keywords: neomutt, general, abort_key, charset, color_directcolor, date_format, folder, hostname, mail_check, mbox_type, sort, use_threads, trash, timeout, wrap
---

(ref-cfg-general)=
# General Options

General configuration variables control NeoMutt's core behaviour. These variables
do not belong to a specific feature domain (such as IMAP, PGP, or Sidebar).

--------------------------------------------------------------------------------

(cfg-abort-backspace)=
## `$abort_backspace`

:Description: Hitting backspace against an empty prompt aborts the prompt
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set abort_backspace = yes
    ```

If _set_, hitting backspace against an empty prompt aborts the prompt.

--------------------------------------------------------------------------------

(cfg-abort-key)=
## `$abort_key`

:Description: String representation of key to abort prompts
:Type: [String](type-string)
:Notes: [Not Empty](type-general), [On Startup](type-general)
:Default:
    ```neomuttrc
    set abort_key = "\007"
    ```

Specifies the key that can be used to abort prompts.
The format is the same as used in "bind" commands.
The default is equivalent to {kbd}`Ctrl-G`.
Note that the specified key should not be used in other bindings, as the abort operation has higher precedence and the binding will not have the desired effect.

Example:
```neomuttrc
set abort_key = "<Esc>"
```

Please note that when using {kbd}`<Esc>` as the abort key, you may also want to set the environment variable ESCDELAY to a low value or even 0 which will reduce the time that ncurses waits to distinguish singular {kbd}`<Esc>` key presses from the start of a terminal escape sequence.
The default time is 1000 milliseconds and thus quite noticeable.

--------------------------------------------------------------------------------

(cfg-ascii-chars)=
## `$ascii_chars`

:Description: Use plain ASCII characters, when drawing email threads
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set ascii_chars = no
    ```

If _set_, NeoMutt will use plain ASCII characters when displaying thread and attachment trees, instead of the default _ACS_ characters.

--------------------------------------------------------------------------------

(cfg-assumed-charset)=
## `$assumed_charset`

:Description: If a message is missing a character set, assume this character set
:Type: [String List](type-slist)
:Notes: [Colon-separated](type-slist), [Allow Empty](type-slist)
:Default: (empty)
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

(cfg-attach-format)=
## `$attach_format`

:Description: Format string for the [Attach Dialog](tour-attach)
:Type: [Expando](type-expando)
:Notes: [Not Empty](type-general), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set attach_format = "%u%D%I %t%4n %T%d %> [%.7m/%.10M, %.6e%<C?, %C>, %s] "
    ```
:Alternative:
    ```neomuttrc
    set attach_format = "%{unlink}%{deleted}%{disposition} %{tagged}%4{number} %{tree}%{description} %{padding-hard: }[%.7{mime-major}/%.10{mime-minor}, %.6{mime-encoding}%<C?, %{charset}>, %{file-size}] "
    ```

Specify the format of the data displayed in the [`Attach Dialog`](tour-attach).

**Format Sequences**

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
| `%s`   | `%{file-size}`        | Size (see {ref}`how-bytes-size`)                                                                  |
| `%T`   | `%{tree}`             | Graphic tree characters                                                                           |
| `%t`   | `%{tagged}`           | Tagged flag                                                                                       |
| `%u`   | `%{unlink}`           | Unlink (=to delete) flag                                                                          |
| `%X`   | `%{attach-count}`     | Number of qualifying MIME parts in this part and its children                                     |
|        |                       | (see the [`$attachments`](#attachment-searching-and-counting) section for possible speed effects) |
| `%*X`  | `%{padding-soft:X}`   | Soft-fill with character `X` as pad                                                               |
| `%>X`  | `%{padding-hard:X}`   | Right justify the rest of the string and pad with character `X`                                   |
| `%\|X` | `%{padding-eol:X}`    | Pad to the end of the line with character `X`                                                     |

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-auto-edit)=
## `$auto_edit`

:Description: Skip the initial compose menu and edit the email
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set auto_edit = no
    ```

When _set_ along with [`$edit_headers`](cfg-edit-headers), NeoMutt will skip the initial send-menu (prompting for subject and recipients) and allow you to immediately begin editing the body of your message.
The send-menu may still be accessed once you have finished editing the body of your message.

:::{note}
When this option is _set_, you can't use send-hooks that depend on the recipients when composing a new (non-reply) message, as the initial list of recipients is empty.
:::

Also see [`$fast_reply`](cfg-fast-reply).

--------------------------------------------------------------------------------

(cfg-auto-tag)=
## `$auto_tag`

:Description: Automatically apply actions to all tagged messages
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set auto_tag = no
    ```

When _set_, functions in the _index_ menu which affect a message will be applied to all tagged messages (if there are any).
When unset, you must first use the [`<tag-prefix>`](ref-fn-generic) function (bound to {kbd}`;` by default) to make the next function apply to all tagged messages.

--------------------------------------------------------------------------------

(cfg-braille-friendly)=
## `$braille_friendly`

:Description: Move the cursor to the beginning of the line
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set braille_friendly = no
    ```

When this variable is _set_, NeoMutt will place the cursor at the beginning of the current line in menus, even when the [`$arrow_cursor`](cfg-arrow-cursor) variable is _unset_, making it easier for blind persons using Braille displays to follow these menus.
The option is _unset_ by default because many visual terminals don't permit making the cursor invisible.

--------------------------------------------------------------------------------

(cfg-charset)=
## `$charset`

:Description: Default character set for displaying text on screen
:Type: [String](type-string)
:Notes: [Not Empty](type-general), [Charset Single](type-general)
:Default: (empty)
    ```neomuttrc
    set charset = ""
    ```

Character set your terminal uses to display and enter textual data.
It is also the fallback for [`$send_charset`](cfg-send-charset).

Upon startup NeoMutt tries to derive this value from environment variables such as [`$LC_CTYPE`](ref-env) or [`$LANG`](ref-env).

:::{note}
It should only be set in case NeoMutt isn't able to determine the character set used correctly.
:::

--------------------------------------------------------------------------------

(cfg-color-directcolor)=
## `$color_directcolor`

:Description: Use 24bit colors (aka truecolor or directcolor)
:Type: [Boolean](type-bool)
:Notes: [On Startup](type-general)
:Default:
    ```neomuttrc
    set color_directcolor = no
    ```

When _set_, NeoMutt will use and allow 24-bit colours (aka truecolor aka directcolor).
For colours to work properly support from the terminal is required as well as a properly set TERM environment variable advertising the terminals directcolor capability, e.g.
`TERM=xterm-direct`.

NeoMutt tries to detect whether the terminal supports 24-bit colours and enables this variable if it does.
If this fails for some reason, you can force 24-bit colours by setting this variable manually.
You may also try to force a certain TERM environment variable by starting NeoMutt from a terminal as follows (this results in wrong colours if the terminal does not implement directcolors):

```sh
TERM=xterm-direct neomutt
```

:::{note}
This variable must be set before using any `color` commands.
:::

--------------------------------------------------------------------------------

(cfg-config-charset)=
## `$config_charset`

:Description: Character set that the config files are in
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set config_charset = ""
    ```

When defined, NeoMutt will recode commands in rc files from this encoding to the current character set as specified by [`$charset`](cfg-charset) and aliases written to [`$alias_file`](cfg-alias-file) from the current character set.

Please note that if setting [`$charset`](cfg-charset) it must be done before setting [`$config_charset`](cfg-config-charset).

Recoding should be avoided as it may render unconvertible characters as question marks which can lead to undesired side effects (for example in regular expressions).

--------------------------------------------------------------------------------

(cfg-confirm-append)=
## `$confirm_append`

:Description: Confirm before appending emails to a mailbox
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set confirm_append = yes
    ```

When _set_, NeoMutt will prompt for confirmation when appending messages to an existing mailbox.

--------------------------------------------------------------------------------

(cfg-confirm-create)=
## `$confirm_create`

:Description: Confirm before creating a new mailbox
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set confirm_create = yes
    ```

When _set_, NeoMutt will prompt for confirmation when saving messages to a mailbox which does not yet exist before creating it.

--------------------------------------------------------------------------------

(cfg-copy-decode-weed)=
## `$copy_decode_weed`

:Description: Controls whether to weed headers when copying or saving emails
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set copy_decode_weed = no
    ```

Controls whether NeoMutt will weed headers when invoking the [`<decode-copy>`](ref-fn-index) or [`<decode-save>`](ref-fn-index) functions.

--------------------------------------------------------------------------------

(cfg-date-format)=
## `$date_format`

:Description: [`strftime(3)`](exp-strftime) format string for the `%d` expando
:Type: [String](type-string)
:Notes: [Not Empty](type-general)
:Default:
    ```neomuttrc
    set date_format = "!%a, %b %d, %Y at %I:%M:%S%p %Z"
    ```

Instead of using [`$date_format`](cfg-date-format) it is encouraged to use "%[fmt]" directly in the corresponding format strings, where "fmt" is the value of [`$date_format`](cfg-date-format).
This allows for a more fine grained control of the different menu needs.

This variable controls the format of the date printed by the `%d` sequence in [`$index_format`](cfg-index-format).
This is passed to the [`strftime(3)`](exp-strftime) function to process the date, see the man page for the proper syntax.

Unless the first character in the string is a bang (`!`), the month and week day names are expanded according to the locale.
If the first character in the string is a bang, the bang is discarded, and the month and week day names in the rest of the string are expanded in the _C_ locale (that is in US English).

Format strings using this variable are:

UI: [`$folder_format`](cfg-folder-format), [`$index_format`](cfg-index-format), [`$mailbox_folder_format`](cfg-mailbox-folder-format), [`$message_format`](cfg-message-format).

Composing: [`$attribution_intro`](cfg-attribution-intro), [`$forward_attribution_intro`](cfg-forward-attribution-intro), [`$forward_attribution_trailer`](cfg-forward-attribution-trailer), [`$forward_format`](cfg-forward-format), [`$indent_string`](cfg-indent-string).

--------------------------------------------------------------------------------

(cfg-debug-file)=
## `$debug_file`

:Description: File to save debug logs
:Type: [Path (String)](type-path)
:Notes: [File only](type-path)
:Default:
    ```neomuttrc
    set debug_file = "~/.neomuttdebug"
    ```

Debug logging is controlled by the variables [`$debug_file`](cfg-debug-file) and [`$debug_level`](cfg-debug-level).
[`$debug_file`](cfg-debug-file) specifies the root of the filename.
NeoMutt will add `0` to the end.
Each time NeoMutt is run with logging enabled, the log files are rotated.
A maximum of five log files are kept, numbered 0 (most recent) to 4 (oldest).

This option can be enabled on the command line,
```sh
neomutt -l mylog
```

:::{seealso}
[`$debug_level`](cfg-debug-level)
:::

--------------------------------------------------------------------------------

(cfg-debug-level)=
## `$debug_level`

:Description: Logging level for debug logs
:Type: [Number](type-number)
:Default:
    ```neomuttrc
    set debug_level = 0
    ```

Debug logging is controlled by the variables [`$debug_file`](cfg-debug-file) and [`$debug_level`](cfg-debug-level).

The debug level controls how much information is saved to the log file.
If you have a problem with NeoMutt, then enabling logging may help find the cause.
Levels 1-3 will usually provide enough information for writing a bug report.
Levels 4,5 will be extremely verbose.

:::{warning}
Logging at high levels may save private information to the file.
:::

This option can be enabled on the command line,
```sh
neomutt -d 2
```

:::{seealso}
[`$debug_file`](cfg-debug-file)
:::

--------------------------------------------------------------------------------

(cfg-delete)=
## `$delete`

:Description: Really delete messages, when the mailbox is closed
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set delete = ask-yes
    ```

Controls whether or not messages are really deleted when closing or synchronizing a mailbox.
If set to _yes_, messages marked for deleting will automatically be purged without prompting.
If set to _no_, messages marked for deletion will be kept in the mailbox.

--------------------------------------------------------------------------------

(cfg-delete-untag)=
## `$delete_untag`

:Description: Untag messages when they are marked for deletion
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set delete_untag = yes
    ```

If this option is _set_, NeoMutt will untag messages when marking them for deletion.
This applies when you either explicitly delete a message, or when you save it to another folder.

--------------------------------------------------------------------------------

(cfg-devel-security)=
## `$devel_security`

:Description: Devel feature: Security -- [Issue #4251](https://github.com/neomutt/neomutt/discussions/4251)
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set devel_security = no
    ```

If this option is _set_, NeoMutt will enable the **Security** development features.

:::{seealso}
<https://github.com/neomutt/neomutt/discussions/4251>
:::

--------------------------------------------------------------------------------

(cfg-editor)=
## `$editor`

:Description: External command to use as an email editor
:Type: [Command (String)](type-string)
:Notes: [Not Empty](type-general)
:Default: (empty)
    ```neomuttrc
    set editor = ""
    ```

This variable specifies which editor is used by NeoMutt.
It defaults to the value of the [`$VISUAL`](ref-env), or [`$EDITOR`](ref-env), environment variable, or to the string `vi` if neither of those are set.

The [`$editor`](cfg-editor) string may contain a _%s_ escape, which will be replaced by the name of the file to be edited.
If the `%s` escape does not appear in [`$editor`](cfg-editor), a space and the name to be edited are appended.

The resulting string is then executed by running:

```sh
sh -c 'string'
```

where _string_ is the expansion of [`$editor`](cfg-editor) described above.

--------------------------------------------------------------------------------

(cfg-flag-safe)=
## `$flag_safe`

:Description: Protect flagged messages from deletion
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set flag_safe = no
    ```

If set, flagged messages can't be deleted.

--------------------------------------------------------------------------------

(cfg-folder)=
## `$folder`

:Description: Base folder for a set of mailboxes
:Type: [Mailbox (String)](type-string)
:Default:
    ```neomuttrc
    set folder = "~/Mail"
    ```

Specifies the default location of your mailboxes.
A `+` or `=` at the beginning of a pathname will be expanded to the value of this variable.
Note that if you change this variable (from the default)
value you need to make sure that the assignment occurs _before_ you use `+` or `=` for any other variables since expansion takes place when handling the [`:mailboxes`](cmd-mailboxes) command.

--------------------------------------------------------------------------------

(cfg-forward-decode)=
## `$forward_decode`

:Description: Decode the message when forwarding it
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set forward_decode = yes
    ```

Controls the decoding of complex MIME messages into `text/plain` when forwarding a message.
The message header is also [RFC2047](https://www.rfc-editor.org/rfc/rfc2047.html) decoded.
This variable is only used, if [`$mime_forward`](cfg-mime-forward) is _unset_, otherwise [`$mime_forward_decode`](cfg-mime-forward-decode) is used instead.

--------------------------------------------------------------------------------

(cfg-forward-quote)=
## `$forward_quote`

:Description: Automatically quote a forwarded message using [`$indent_string`](cfg-indent-string)
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set forward_quote = no
    ```

When _set_, forwarded messages included in the main body of the message (when [`$mime_forward`](cfg-mime-forward) is _unset_) will be quoted using [`$indent_string`](cfg-indent-string).

:::{seealso}
- {doc}`/howto/email-template`
:::

--------------------------------------------------------------------------------

(cfg-from)=
## `$from`

:Description: Default `From` address to use, if isn't otherwise set
:Type: [Address](type-address)
:Default: (empty)
    ```neomuttrc
    set from = ""
    ```

When _set_, this variable contains a default "from" address.
It can be overridden using [`:my-header`](cmd-my-header) (including from a [`:send-hook`](cmd-send-hook)) and [`$reverse_name`](cfg-reverse-name).
This variable is ignored if [`$use_from`](cfg-use-from) is _unset_.

If not specified, then it may be read from the environment variable [`$EMAIL`](ref-env).

--------------------------------------------------------------------------------

(cfg-gecos-mask)=
## `$gecos_mask`

:Description: Regex for parsing GECOS field of `/etc/passwd`
:Type: [Regular Expression](type-regex)
:Notes: [Smart Case](type-general)
:Default:
    ```neomuttrc
    set gecos_mask = "^[^,]*"
    ```

A regular expression used by NeoMutt to parse the GECOS field of a password entry when expanding the alias.
The default value will return the string up to the first `,` encountered.
If the GECOS field contains a string like "lastname, firstname" then you should set it to `.*`.

This can be useful if you see the following behavior: you address an e-mail to user ID "stevef" whose full name is "Steve Franklin".
If NeoMutt expands "stevef" to '"Franklin" stevef@foo.bar' then you should set the [`$gecos_mask`](cfg-gecos-mask) to a regular expression that will match the whole name so NeoMutt will expand "Franklin" to "Franklin, Steve".

--------------------------------------------------------------------------------

(cfg-header)=
## `$header`

:Description: Include the message headers in the reply email (Weed applies)
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set header = no
    ```

When _set_, this variable causes NeoMutt to include the header of the message you are replying to into the edit buffer.
The [`$weed`](cfg-weed) setting applies.

--------------------------------------------------------------------------------

(cfg-help)=
## `$help`

:Description: Display a help line with common key bindings
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set help = yes
    ```

When _set_, help lines describing the bindings for the major functions provided by each menu are displayed on the first line of the screen.

:::{note}
The binding will not be displayed correctly if the function is bound to a sequence rather than a single keystroke.
Also, the help line may not be updated if a binding is changed while NeoMutt is running.
Since this variable is primarily aimed at new users, neither of these should present a major problem.
:::

--------------------------------------------------------------------------------

(cfg-hostname)=
## `$hostname`

:Description: Fully-qualified domain name of this machine
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set hostname = ""
    ```

Specifies the fully-qualified hostname of the system NeoMutt is running on containing the host's name and the DNS domain it belongs to.
It is used as the domain part (after `@`) for local email addresses.

If not specified in a config file, then NeoMutt will try to determine the hostname itself.

Optionally, NeoMutt can be compiled with a fixed domain name.

Also see [`$use_domain`](cfg-use-domain) and [`$hidden_host`](cfg-hidden-host).

--------------------------------------------------------------------------------

(cfg-indent-string)=
## `$indent_string`

:Description: String used to indent "reply" text
:Type: [Expando](type-expando)
:Default:
    ```neomuttrc
    set indent_string = "> "
    ```

Specifies the string to prepend to each line of text quoted in a message to which you are replying.
You are strongly encouraged not to change this value, as it tends to agitate the more fanatical netizens.

The value of this option is ignored if [`$text_flowed`](cfg-text-flowed) is set, because the quoting mechanism is strictly defined for `format=flowed`.

:::{seealso}
- {doc}`/howto/email-template`
- [`$index_format`](cfg-index-format) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-keep-flagged)=
## `$keep_flagged`

:Description: Don't move flagged messages from [`$spool_file`](cfg-spool-file) to [`$mbox`](cfg-mbox)
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set keep_flagged = no
    ```

If _set_, read messages marked as flagged will not be moved from your spool mailbox to your [`$mbox`](cfg-mbox) mailbox or to the "mbox" specified by a [`:mbox-hook`](cmd-mbox-hook) command.

Note that [`$keep_flagged`](cfg-keep-flagged) only has an effect if [`$move`](cfg-move) is set.

--------------------------------------------------------------------------------

(cfg-local-date-header)=
## `$local_date_header`

:Description: Convert the date in the Date header of sent emails into local timezone, UTC otherwise
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set local_date_header = yes
    ```

If _set_, the date in the Date header of emails that you send will be in your local timezone.
If unset a UTC date will be used instead to avoid leaking information about your current location.

--------------------------------------------------------------------------------

(cfg-mail-check)=
## `$mail_check`

:Description: Number of seconds before NeoMutt checks for new mail
:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set mail_check = 5
    ```

This variable configures how often (in seconds) NeoMutt should look for new mail.
Also see the [`$timeout`](cfg-timeout) variable.

--------------------------------------------------------------------------------

(cfg-mail-check-recent)=
## `$mail_check_recent`

:Description: Notify the user about new mail since the last time the mailbox was opened
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set mail_check_recent = yes
    ```

When _set_, NeoMutt will only notify you about new mail that has been received since the last time you opened the mailbox.
When _unset_, NeoMutt will notify you if any new mail exists in the mailbox, regardless of whether you have visited it recently.

--------------------------------------------------------------------------------

(cfg-mail-check-stats)=
## `$mail_check_stats`

:Description: Periodically check for new mail
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set mail_check_stats = no
    ```

When _set_, NeoMutt will periodically calculate message statistics of a mailbox while polling for new mail.
It will check for unread, flagged, and total message counts.
(Note: IMAP mailboxes only support unread and total counts).

Because this operation is more performance intensive, it defaults to _unset_, and has a separate option, [`$mail_check_stats_interval`](cfg-mail-check-stats-interval), to control how often to update these counts.

Message statistics can also be explicitly calculated by invoking the [`<check-stats>`](ref-fn-generic) function.

--------------------------------------------------------------------------------

(cfg-mail-check-stats-interval)=
## `$mail_check_stats_interval`

:Description: How often to check for new mail
:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set mail_check_stats_interval = 60
    ```

When [`$mail_check_stats`](cfg-mail-check-stats) is _set_, this variable configures how often (in seconds) NeoMutt will update message counts.

--------------------------------------------------------------------------------

(cfg-mark-old)=
## `$mark_old`

:Description: Mark new emails as old when leaving the mailbox
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set mark_old = yes
    ```

Controls whether or not NeoMutt marks _new_ **unread** messages as _old_ if you exit a mailbox without reading them.
With this option _set_, the next time you start NeoMutt, the messages will show up with an `O` next to them in the index menu, indicating that they are old.

--------------------------------------------------------------------------------

(cfg-mbox)=
## `$mbox`

:Description: Folder that receives read emails
:Type: [Mailbox (String)](type-string)
:Default:
    ```neomuttrc
    set mbox = "~/mbox"
    ```

This specifies the folder into which read mail in your [`$spool_file`](cfg-spool-file) folder will be appended.

Also see the [`$move`](cfg-move) variable.

--------------------------------------------------------------------------------

(cfg-mbox-type)=
## `$mbox_type`

:Description: Default type for creating new mailboxes
:Type: [Enumeration](type-enum)
:Default:
    ```neomuttrc
    set mbox_type = mbox
    ```

The default mailbox type used when creating new folders.

| Values    |
|-----------|
| `maildir` |
| `mbox`    |
| `mh`      |
| `mmdf`    |

This can also be set using the `neomutt -m` command-line option.

--------------------------------------------------------------------------------

(cfg-message-cache-clean)=
## `$message_cache_clean`

:Description: Clean out obsolete entries from the message cache
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set message_cache_clean = no
    ```

If _set_, NeoMutt will clean out obsolete entries from the message cache when the mailbox is synchronized.
You probably only want to set it every once in a while, since it can be a little slow (especially for large folders).

--------------------------------------------------------------------------------

(cfg-message-cache-dir)=
## `$message_cache_dir`

:Description: Directory for the message cache
:Type: [Path (String)](type-path)
:Notes: [Directory only](type-path)
:Default: (empty)
    ```neomuttrc
    set message_cache_dir = ""
    ```

Set this to a directory and NeoMutt will cache copies of messages from your IMAP and POP servers here.
You are free to remove entries at any time.

When setting this variable to a directory, NeoMutt needs to fetch every remote message only once and can perform regular expression searches as fast as for local folders.

Also see the [`$message_cache_clean`](cfg-message-cache-clean) variable.

--------------------------------------------------------------------------------

(cfg-meta-key)=
## `$meta_key`

:Description: Interpret 'ALT-x' as 'ESC-x'
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set meta_key = no
    ```

If _set_, forces NeoMutt to interpret keystrokes with the high bit (bit 8) set as if the user had pressed the Esc key and whatever key remains after having the high bit removed.
For example, if the key pressed has an ASCII value of `0xf8`, then this is treated as if the user had pressed Esc then `x`.
This is because the result of removing the high bit from `0xf8` is `0x78`, which is the ASCII character `x`.

--------------------------------------------------------------------------------

(cfg-move)=
## `$move`

:Description: Move emails from [`$spool_file`](cfg-spool-file) to [`$mbox`](cfg-mbox) when read
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set move = no
    ```

If this variable is _set_, then NeoMutt will move read messages from your spool mailbox to your [`$mbox`](cfg-mbox) mailbox or to the "mbox" specified by a [`:mbox-hook`](cmd-mbox-hook) command.

:::{seealso}
[`$keep_flagged`](cfg-keep-flagged)
:::

--------------------------------------------------------------------------------

(cfg-pipe-decode)=
## `$pipe_decode`

:Description: Decode the message when piping it
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set pipe_decode = no
    ```

Used in connection with the [`<pipe-message>`](ref-fn-attach) function.
When _unset_, NeoMutt will pipe the messages without any preprocessing.
When _set_, NeoMutt will attempt to decode the messages first.

Also see [`$pipe_decode_weed`](cfg-pipe-decode-weed), which controls whether headers will be weeded when this is _set_.

--------------------------------------------------------------------------------

(cfg-pipe-decode-weed)=
## `$pipe_decode_weed`

:Description: Control whether to weed headers when piping an email
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set pipe_decode_weed = yes
    ```

For [`<pipe-message>`](ref-fn-attach), when [`$pipe_decode`](cfg-pipe-decode) is set, this further controls whether NeoMutt will weed headers.

--------------------------------------------------------------------------------

(cfg-pipe-sep)=
## `$pipe_sep`

:Description: Separator to add between multiple piped messages
:Type: [String](type-string)
:Default:
    ```neomuttrc
    set pipe_sep = "\n"
    ```

The separator to add between messages when piping a list of tagged messages to an external Unix command.

--------------------------------------------------------------------------------

(cfg-pipe-split)=
## `$pipe_split`

:Description: Run the pipe command on each message separately
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set pipe_split = no
    ```

Used in connection with the [`<pipe-message>`](ref-fn-attach) function following [`<tag-prefix>`](ref-fn-generic).

If this variable is _unset_, when piping a list of tagged messages NeoMutt will concatenate the messages and will pipe them all concatenated.
When _set_, NeoMutt will pipe the messages one by one.
In both cases the messages are piped in the current sorted order, and the [`$pipe_sep`](cfg-pipe-sep) separator is added after each message.

--------------------------------------------------------------------------------

(cfg-postponed)=
## `$postponed`

:Description: Folder to store postponed messages
:Type: [Mailbox (String)](type-string)
:Default:
    ```neomuttrc
    set postponed = "~/postponed"
    ```

NeoMutt allows you to indefinitely "$postpone sending a message" which you are editing.
When you choose to postpone a message, NeoMutt saves it in the mailbox specified by this variable.

Also see the [`$postpone`](cfg-postpone) variable.

--------------------------------------------------------------------------------

(cfg-print)=
## `$print`

:Description: Confirm before printing a message
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set print = ask-no
    ```

Controls whether or not NeoMutt really prints messages.
This is set to `ask-no` by default, because some people accidentally hit {kbd}`p` often.

--------------------------------------------------------------------------------

(cfg-print-command)=
## `$print_command`

:Description: External command to print a message
:Type: [Command (String)](type-string)
:Default:
    ```neomuttrc
    set print_command = "lpr"
    ```

This specifies the command pipe that should be used to print messages.

--------------------------------------------------------------------------------

(cfg-print-decode)=
## `$print_decode`

:Description: Decode message before printing it
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set print_decode = yes
    ```

Used in connection with the [`<print-message>`](ref-fn-index) function.
If this option is _set_, the message is decoded before it is passed to the external command specified by [`$print_command`](cfg-print-command).
If this option is _unset_, no processing will be applied to the message when printing it.
The latter setting may be useful if you are using some advanced printer filter which is able to properly format e-mail messages for printing.

Also see [`$print_decode_weed`](cfg-print-decode-weed), which controls whether headers will be weeded when this is _set_.

--------------------------------------------------------------------------------

(cfg-print-decode-weed)=
## `$print_decode_weed`

:Description: Control whether to weed headers when printing an email
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set print_decode_weed = yes
    ```

For [`<print-message>`](ref-fn-index), when [`$print_decode`](cfg-print-decode) is set, this further controls whether NeoMutt will weed headers.

--------------------------------------------------------------------------------

(cfg-print-split)=
## `$print_split`

:Description: Print multiple messages separately
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set print_split = no
    ```

Used in connection with the [`<print-message>`](ref-fn-index) function.
If this option is _set_, the command specified by [`$print_command`](cfg-print-command) is executed once for each message which is to be printed.
If this option is _unset_, the command specified by [`$print_command`](cfg-print-command) is executed only once, and all the messages are concatenated, with a form feed as the message separator.

Those who use the `enscript(1)` program's mail-printing mode will most likely want to _set_ this option.

--------------------------------------------------------------------------------

(cfg-quote-regex)=
## `$quote_regex`

:Description: Regex to match quoted text in a reply
:Type: [Regular Expression](type-regex)
:Notes: [Smart Case](type-general)
:Default:
    ```neomuttrc
    set quote_regex = "^([ \t]*[|>:}#])+"
    ```

A regular expression used in the internal pager to determine quoted sections of text in the body of a message.
Quoted text may be filtered out using the [`<toggle-quoted>`](ref-fn-pager) command, or colored according to the `color quotedN` family of directives.

Higher levels of quoting may be colored differently (`color quoted1`, `color quoted2`, etc.).
The quoting level is determined by removing the last character from the matched text and recursively reapplying the regular expression until it fails to produce a match.

Match detection may be overridden by the [`$smileys`](cfg-smileys) regular expression.

--------------------------------------------------------------------------------

(cfg-real-name)=
## `$real_name`

:Description: Real name of the user
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set real_name = ""
    ```

This variable specifies what "real" or "personal" name should be used when sending messages.

If not specified, then the user's "real name" will be read from `/etc/passwd`.
This option will not be used, if [`$from`](cfg-from) is set.

--------------------------------------------------------------------------------

(cfg-record)=
## `$record`

:Description: Folder to save 'sent' messages
:Type: [Mailbox (String)](type-string)
:Default:
    ```neomuttrc
    set record = "~/sent"
    ```

This specifies the file into which your outgoing messages should be appended.
(This is meant as the primary method for saving a copy of your messages, but another way to do this is using the [`:my-header`](cmd-my-header) command to create a `Bcc:` field with your email address in it.)

The value of [`$record`](cfg-record) is overridden by the [`$force_name`](cfg-force-name) and [`$save_name`](cfg-save-name) variables, and the [`:fcc-hook`](cmd-fcc-hook) command.
Also see [`$copy`](cfg-copy) and [`$write_bcc`](cfg-write-bcc).

--------------------------------------------------------------------------------

(cfg-resolve)=
## `$resolve`

:Description: Move to the next email whenever a command modifies an email
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set resolve = yes
    ```

When _set_, the cursor in a list will be automatically advanced to the next (possibly undeleted) message/attachment/entry whenever a command that modifies the current message/attachment/entry is executed.

Examples of such commands are tagging a message, deleting an entry, or saving an attachment.

--------------------------------------------------------------------------------

(cfg-resume-edited-draft-files)=
## `$resume_edited_draft_files`

:Description: Resume editing previously saved draft files
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set resume_edited_draft_files = yes
    ```

If _set_, draft files previously edited (via `-E -H` on the command line) will have [`$resume_draft_files`](cfg-resume-draft-files) automatically set when they are used as a draft file again.

The first time a draft file is saved, NeoMutt will add a header, `X-Mutt-Resume-Draft` to the saved file.
The next time the draft file is read in, if NeoMutt sees the header, it will set [`$resume_draft_files`](cfg-resume-draft-files).

This option is designed to prevent multiple signatures, user-defined headers, and other processing effects from being made multiple times to the draft file.

--------------------------------------------------------------------------------

(cfg-save-address)=
## `$save_address`

:Description: Use sender's full address as a default save folder
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set save_address = no
    ```

If _set_, NeoMutt will take the sender's full address when choosing a default folder for saving a mail.
If [`$save_name`](cfg-save-name) or [`$force_name`](cfg-force-name) is _set_ too, the selection of the Fcc folder will be changed as well.

--------------------------------------------------------------------------------

(cfg-save-empty)=
## `$save_empty`

:Description: Preserve empty mailboxes
:Type: [Boolean](type-bool)
:Scope: Only mbox and mmdf mailboxes
:Default:
    ```neomuttrc
    set save_empty = yes
    ```

When _unset_, mailboxes which contain no saved messages will be removed when closed (the exception is [`$spool_file`](cfg-spool-file) which is never removed).
If _set_, mailboxes are never removed.

:::{note}
NeoMutt does not delete MH and Maildir directories.
:::

--------------------------------------------------------------------------------

(cfg-send-charset)=
## `$send_charset`

:Description: Character sets for outgoing mail
:Type: [String List](type-slist)
:Notes: [Colon-separated](type-slist), [Allow Empty](type-slist), [Charset Strict](type-general)
:Default:
    ```neomuttrc
    set send_charset = "us-ascii:iso-8859-1:utf-8"
    ```

A colon-delimited list of character sets for outgoing messages.
NeoMutt will use the first character set into which the text can be converted exactly.
If your [`$charset`](cfg-charset) is not "iso-8859-1" and recipients may not understand "UTF-8", it is advisable to include in the list an appropriate widely used standard character set (such as "iso-8859-2", "koi8-r" or "iso-2022-jp") either instead of or after "iso-8859-1".

In case the text can't be converted into one of these exactly, NeoMutt uses [`$charset`](cfg-charset) as a fallback.

--------------------------------------------------------------------------------

(cfg-shell)=
## `$shell`

:Description: External command to run subshells in
:Type: [Command (String)](type-string)
:Default:
    ```neomuttrc
    set shell = "/bin/sh"
    ```

Command to use when spawning a subshell.
If not specified, then the user's login shell from `/etc/passwd` is used.

--------------------------------------------------------------------------------

(cfg-size-show-bytes)=
## `$size_show_bytes`

:Description: Show smaller sizes in bytes
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set size_show_bytes = no
    ```

If _set_, message sizes will display bytes for values less than 1 kilobyte.

:::{seealso}
{ref}`how-bytes-size`
:::

--------------------------------------------------------------------------------

(cfg-size-show-fractions)=
## `$size_show_fractions`

:Description: Show size fractions with a single decimal place
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set size_show_fractions = yes
    ```

If _set_, message sizes will be displayed with a single decimal value for sizes from 0 to 10 kilobytes and 1 to 10 megabytes.

:::{seealso}
{ref}`how-bytes-size`
:::

--------------------------------------------------------------------------------

(cfg-size-show-mb)=
## `$size_show_mb`

:Description: Show sizes in megabytes for sizes greater than 1 megabyte
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set size_show_mb = yes
    ```

If _set_, message sizes will display megabytes for values greater than or equal to 1 megabyte.

:::{seealso}
{ref}`how-bytes-size`
:::

--------------------------------------------------------------------------------

(cfg-size-units-on-left)=
## `$size_units_on_left`

:Description: Show the units as a prefix to the size
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set size_units_on_left = no
    ```

If _set_, message sizes units will be displayed to the left of the number.

:::{seealso}
{ref}`how-bytes-size`
:::

--------------------------------------------------------------------------------

(cfg-sleep-time)=
## `$sleep_time`

:Description: Time to pause after certain info messages
:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set sleep_time = 1
    ```

Specifies time, in seconds, to pause while displaying certain informational messages, while moving from folder to folder and after expunging messages from the current folder.
The default is to pause one second, so a value of zero for this option suppresses the pause.

--------------------------------------------------------------------------------

(cfg-sort)=
## `$sort`

:Description: Sort method for the [Index Dialog](tour-index)
:Type: [Sort Order](type-sort-order)
:Notes: [Reverse](type-sort-order), [Last](type-sort-order)
:Default:
    ```neomuttrc
    set sort = date
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

Any ties in the primary sort are broken by [`$sort_aux`](cfg-sort-aux).
When [`$use_threads`](cfg-use-threads) is "threads" or "reverse", [`$sort`](cfg-sort) controls the sorting between threads, and [`$sort_aux`](cfg-sort-aux) controls the sorting within a thread.

The values of "threads" and "reverse-threads" are legacy options, which cause the value of [`$sort_aux`](cfg-sort-aux) to also control sorting between threads, and they may not be used with the "last-" prefix.
The preferred way to enable a threaded view is via [`$use_threads`](cfg-use-threads).  
This variable can also be set via the [`<sort-mailbox>`](ref-fn-index) and [`<sort-reverse>`](ref-fn-browser) functions.

:::{note}
When [`$use_threads`](cfg-use-threads) is "threads", the last thread sorts to the bottom; when it is "reversed", the last thread sorts to the top.
The use of "reverse-" in [`$sort`](cfg-sort) swaps which end the last thread will sort to.
:::

See the "Use Threads Feature" section for further explanation and examples, <https://neomutt.org/feature/use-threads>

--------------------------------------------------------------------------------

(cfg-sort-aux)=
## `$sort_aux`

:Description: Secondary sort method for the Index
:Type: [Sort Order](type-sort-order)
:Notes: [Reverse](type-sort-order), [Last](type-sort-order)
:Default:
    ```neomuttrc
    set sort_aux = date
    ```

This provides a secondary sort for messages in the "index" menu, used when the [`$sort`](cfg-sort) value is equal for two messages.

When sorting by threads, this variable controls how subthreads are sorted within a single thread (for the order between threads, see [`$sort`](cfg-sort)).
This can be set to any value that [`$sort`](cfg-sort) can, including with the use of "reverse-" and "last-" prefixes, except for variations using "threads" (in that case, NeoMutt will just use "date").

For instance,
```neomuttrc
set sort_aux = last-date-received
```

would mean that if a new message is received in a thread, that subthread becomes the last one displayed (or the first, if you have `set use_threads = reverse`)  When using [`$use_threads`](cfg-use-threads), it is more common to use "last-" with [`$sort`](cfg-sort) and not with [`$sort_aux`](cfg-sort-aux).

See the "Use Threads Feature" section for further explanation and examples, <https://neomutt.org/feature/use-threads>

--------------------------------------------------------------------------------

(cfg-spool-file)=
## `$spool_file`

:Description: Inbox
:Type: [Mailbox (String)](type-string)
:Default: (empty)
    ```neomuttrc
    set spool_file = ""
    ```

If your spool mailbox is in a non-default place where NeoMutt can't find it, you can specify its location with this variable.
The description from "named-mailboxes" may be used for the spool_file.

If not specified, then the environment variables [`$MAIL`](ref-env) and [`$MAILDIR`](ref-env) will be checked.

--------------------------------------------------------------------------------

(cfg-status-on-top)=
## `$status_on_top`

:Description: Display the status bar at the top
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set status_on_top = no
    ```

Setting this variable causes the "status bar" to be displayed on the first line of the screen rather than near the bottom.
If [`$help`](cfg-help) is _set_ too, it'll be placed at the bottom.

--------------------------------------------------------------------------------

(cfg-suspend)=
## `$suspend`

:Description: Allow the user to suspend NeoMutt using `^Z`
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set suspend = yes
    ```

When _unset_, NeoMutt won't stop when the user presses the terminal's _susp_ key, usually {kbd}`^Z`.
This is useful if you run NeoMutt inside an xterm using a command like `xterm -e neomutt`

On startup NeoMutt tries to detect if it is the process session leader.
If so, the default of [`$suspend`](cfg-suspend) is `no` otherwise `yes`.  This default covers the above mentioned use case of `xterm -e neomutt`

--------------------------------------------------------------------------------

(cfg-text-flowed)=
## `$text_flowed`

:Description: Generate `format=flowed` messages
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set text_flowed = no
    ```

When _set_, NeoMutt will generate "format=flowed" bodies with a content type of `text/plain; format=flowed`

This format is easier to handle for some mailing software, and generally just looks like ordinary text.
To actually make use of this format's features, you'll need support in your editor.

The option only controls newly composed messages.
Postponed messages, resent messages, and draft messages (via `-H` on the command line) will use the content-type of the source message.

Note that [`$indent_string`](cfg-indent-string) is ignored when this option is _set_.

--------------------------------------------------------------------------------

(cfg-timeout)=
## `$timeout`

:Description: Time to wait for user input in menus
:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set timeout = 600
    ```

This variable sets the time interval in seconds in which [`:timeout-hook`](cmd-timeout-hook) commands get executed while waiting for user input either idling in menus or in an interactive prompt.

A value of zero disables timeout hooks.

--------------------------------------------------------------------------------

(cfg-tmp-dir)=
## `$tmp_dir`

:Description: Directory for temporary files
:Type: [Path (String)](type-path)
:Notes: [Directory only](type-path), [Not Empty](type-general)
:Default:
    ```neomuttrc
    set tmp_dir = "/tmp"
    ```

This variable allows you to specify where NeoMutt will place its temporary files needed for displaying messages.

If this variable is not set, the environment variable [`$TMPDIR`](ref-env) is used.
Failing that, then `/tmp` is used.

--------------------------------------------------------------------------------

(cfg-tmp-draft-dir)=
## `$tmp_draft_dir`

:Description: Directory for Compose temporary files
:Type: [Path (String)](type-path)
:Notes: [Directory only](type-path), [Not Empty](type-general)
:Default:
    ```neomuttrc
    set tmp_draft_dir = "/var/tmp"
    ```

This variable allows you to specify where NeoMutt will place its temporary files when composing messages.

If this variable is not set, the environment variable [`$TMPDIR`](ref-env) is used.
Failing that, then `/var/tmp` is used.

It is recommended that this be set to a directory whose contents won't be removed during an unanticipated reboot, so that draft files will survive a crash or other unplanned computer shutdown.

--------------------------------------------------------------------------------

(cfg-trash)=
## `$trash`

:Description: Folder to put deleted emails
:Type: [Mailbox (String)](type-string)
:Default: (empty)
    ```neomuttrc
    set trash = ""
    ```

If set, this variable specifies the path of the trash folder where the mails marked for deletion will be moved, instead of being irremediably purged.

:::{note}
When you delete a message in the trash folder, it is really deleted, so that you have a way to clean the trash.
:::

--------------------------------------------------------------------------------

(cfg-use-domain)=
## `$use_domain`

:Description: Qualify local addresses using this domain
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set use_domain = yes
    ```

When _set_, NeoMutt will qualify all local addresses (ones without the "@host" portion) with the value of [`$hostname`](cfg-hostname).
If _unset_, no addresses will be qualified.

--------------------------------------------------------------------------------

(cfg-use-threads)=
## `$use_threads`

:Description: Whether to use threads for the index
:Type: [Enumeration](type-enum)
:Default:
    ```neomuttrc
    set use_threads = unset
    ```

The style of threading used in the index.

| Value     | Meaning                                      |
|-----------|----------------------------------------------|
| `unset`   | Not set (no threading)
| `flat`    | No threading                                 |
| `threads` | Threaded, with subthreads below root message |
| `reverse` | Threaded, with subthreads above root message |
| `yes`     | Synonym for `threads`                        |
| `no`      | Synonym for `flat`                           |

If this variable is never set, then [`$sort`](cfg-sort) controls whether threading is used, [`$sort_aux`](cfg-sort-aux) controls both the sorting of threads and subthreads, and using [`<sort-mailbox>`](ref-fn-index) to select threads affects only [`$sort`](cfg-sort).
Once this variable is set, attempting to set [`$sort`](cfg-sort) to a value using "threads" will warn, the value of [`$sort`](cfg-sort) controls the sorting between threads while [`$sort_aux`](cfg-sort-aux) controls sorting within a thread, and [`<sort-mailbox>`](ref-fn-index) toggles [`$use_threads`](cfg-use-threads).

Example:
```neomuttrc
set use_threads = yes
```

See the "Use Threads Feature" section for further explanation and examples.

--------------------------------------------------------------------------------

(cfg-wait-key)=
## `$wait_key`

:Description: Prompt to press a key after running external commands
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set wait_key = yes
    ```

Controls whether NeoMutt will ask you to press a key after an external command has been invoked by these functions: [`<shell-escape>`](ref-fn-generic), [`<pipe-message>`](ref-fn-attach), [`<pipe-entry>`](ref-fn-attach), [`<print-message>`](ref-fn-index), and [`<print-entry>`](ref-fn-attach) commands.

It is also used when viewing attachments with [`:auto-view`](cmd-auto-view), provided that the corresponding mailcap entry has a `needsterminal` flag, and the external program is interactive.

When _set_, NeoMutt will always ask for a key.
When _unset_, NeoMutt will wait for a key only if the external command returned a non-zero status.

--------------------------------------------------------------------------------

(cfg-weed)=
## `$weed`

:Description: Filter headers when displaying/forwarding/printing/replying
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set weed = yes
    ```

When _set_, NeoMutt will weed headers when displaying, forwarding, or replying to messages.

Also see [`$copy_decode_weed`](cfg-copy-decode-weed), [`$pipe_decode_weed`](cfg-pipe-decode-weed), [`$print_decode_weed`](cfg-print-decode-weed).

--------------------------------------------------------------------------------

(cfg-wrap)=
## `$wrap`

:Description: Width to wrap text in the pager
:Type: [Number](type-number)
:Default:
    ```neomuttrc
    set wrap = 0
    ```

When set to a positive value, NeoMutt will wrap text at [`$wrap`](cfg-wrap) characters.
When set to a negative value, NeoMutt will wrap text so that there are [`$wrap`](cfg-wrap) characters of empty space on the right side of the terminal.
Setting it to zero makes NeoMutt wrap at the terminal width.

Also see [`$reflow_wrap`](cfg-reflow-wrap).

--------------------------------------------------------------------------------

(cfg-wrap-search)=
## `$wrap_search`

:Description: Wrap around when the search hits the end
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set wrap_search = yes
    ```

Controls whether searches wrap around the end.

When _set_, searches will wrap around the first (or last) item.
When _unset_, incremental searches will not wrap.

