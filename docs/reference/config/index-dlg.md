---
title: Index Options
description: Configuration variables for the index menu display, status bar formatting, flags, and terminal title.
keywords: neomutt, index, index_format, status_format, flag_chars, crypt_chars, from_chars, to_chars, ts_enabled, new_mail_command, status bar, message list
---

(cfg-index-dlg)=
# Index Options

(cfg-beep-new)=
## `$beep_new`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set beep_new = no
    ```

When this variable is _set_, NeoMutt will beep whenever it prints a message notifying you of new mail.
This is independent of the setting of the [`$beep`](cfg-beep) variable.

--------------------------------------------------------------------------------

(cfg-change-folder-next)=
## `$change_folder_next`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set change_folder_next = no
    ```

When this variable is _set_, the [`<change-folder>`](fn-index) function mailbox suggestion will start at the next folder in your [`mailboxes`](cmd-mailboxes) list, instead of starting at the first folder in the list.

--------------------------------------------------------------------------------

(cfg-collapse-all)=
## `$collapse_all`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set collapse_all = no
    ```

When _set_, NeoMutt will collapse all threads when entering a folder.

--------------------------------------------------------------------------------

(cfg-crypt-chars)=
## `$crypt_chars`

:Type: [Character String](type-mbtable)
:Default:
    ```neomuttrc
    set crypt_chars = "SPsK "
    ```

Controls the characters used in cryptography flags.

| Character | Default     | Description                                                    |
|-----------|-------------|----------------------------------------------------------------|
| 1         | `S`         | The mail is signed, and the signature is successfully verified |
| 2         | `P`         | The mail is PGP encrypted                                      |
| 3         | `s`         | The mail is signed                                             |
| 4         | `K`         | The mail contains a PGP public key                             |
| 5         | ` ` (space) | The mail has no crypto info                                    |

--------------------------------------------------------------------------------

(cfg-flag-chars)=
## `$flag_chars`

:Type: [Character String](type-mbtable)
:Default:
    ```neomuttrc
    set flag_chars = "*!DdrONon- "
    ```

Controls the characters used in several flags.

| Character | Default     | Description                              |
|-----------|-------------|------------------------------------------|
| 1         | `*`         | Mail is tagged                           |
| 2         | `!`         | Mail is flagged as important             |
| 3         | `D`         | Mail is marked for deletion              |
| 4         | `d`         | Mail has attachments marked for deletion |
| 5         | `r`         | Mail has been replied to                 |
| 6         | `O`         | Mail is Old (Unread but seen)            |
| 7         | `N`         | Mail is New (Unread but not seen)        |
| 8         | `o`         | Mail thread is Old (Unread but seen)     |
| 9         | `n`         | Mail thread is New (Unread but not seen) |
| 10        | `-`         | Mail is read - %S expando                |
| 11        | ` ` (space) | Mail is read - %Z expando                |

--------------------------------------------------------------------------------

(cfg-from-chars)=
## `$from_chars`

:Type: [Character String](type-mbtable)
:Default: (empty)
    ```neomuttrc
    set from_chars = ""
    ```

Controls the character used to prefix the %F and %L fields in the index.

| Character | Description                                                                                 |
|-----------|---------------------------------------------------------------------------------------------|
| 1         | Mail is written by you and has a To address, or has a known mailing list in the To address. |
| 2         | Mail is written by you and has a Cc address, or has a known mailing list in the Cc address. |
| 3         | Mail is written by you and has a Bcc address.                                               |
| 4         | All remaining cases.                                                                        |

If this is empty or unset (default), the traditional long "To ", "Cc " and "Bcc " prefixes are used.
If set but too short to include a character for a particular case, a single space will be prepended to the field.
To prevent any prefix at all from being added in a particular case, use the special value CR (aka ^M)
for the corresponding character.

This slightly odd interface is necessitated by NeoMutt's handling of string variables; one can't tell a variable that is unset from one that is set to the empty string.

--------------------------------------------------------------------------------

(cfg-index-format)=
## `$index_format`

:Type: [Expando](type-expando)
:Notes: {ref}`Not Empty <type-general>`
:Default:
    ```neomuttrc
    set index_format = "%4C %Z %{%b %d} %-15.15L (%<l?%4l&%4c>) %s"
    ```
:Alternative:
    ```neomuttrc
    set index_format = "%4{number} %{combined-flags} %{%b %d} %-15.15{from-list} (%<l?%4{lines}&%4{size}>) %{subject}"
    ```

This variable allows you to customize the message index display to your personal taste.

"Format strings" are similar to the strings used in the C function `printf(3)` to format output (see the man page for more details).
For an explanation of the %<...> construct, see the [`$status_format`](cfg-status-format) description.
The following sequences are defined in NeoMutt:

| Short     | Long Name                | Description                                                                                                                    |
|-----------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `%A`      | `%{reply-to}`            | Reply-to address (if present; otherwise: address of author)                                                                    |
| `%a`      | `%{from}`                | Address of the author                                                                                                          |
| `%B`      | `%{list-address}`        | List to which the email was sent (if any; otherwise: Mailbox name)                                                             |
| `%b`      | `%{mailbox-name}`        | Filename of the original message folder (think mailbox)                                                                        |
| `%C`      | `%{number}`              | Current message number                                                                                                         |
| `%c`      | `%{body-characters}`     | Number of characters (bytes) in the body of the message (see **Size Format**)                                                  |
| `%cr`     | `%{size}`                | Number of characters (bytes) in the raw message, including the header (see **Size Format**)                                    |
| `%D`      | `%{date-format-local}`   | Date and time of message using [`$date_format`](cfg-date-format) and local timezone.                                                |
|           |                          | It is recommended to use `%[fmt]` instead, where `fmt` is the value of [`$date_format`](cfg-date-format).                           |
| `%d`      | `%{date-format}`         | Date and time of message using [`$date_format`](cfg-date-format) and sender's timezone.                                             |
|           |                          | It is recommended to use `%{fmt}` instead, where `fmt` is the value of [`$date_format`](cfg-date-format).                           |
| `%E`      | `%{thread-count}`        | Number of messages in current thread                                                                                           |
| `%e`      | `%{thread-number}`       | Current message number in thread                                                                                               |
| `%F`      | `%{sender}`              | Author name, or recipient name if the message is from you                                                                      |
| `%Fp`     | `%{sender-plain}`        | Like `%F`, but plain. No contextual formatting is applied to recipient name                                                    |
| `%f`      | `%{from-full}`           | Sender (address + real name), either From: or Return-Path:                                                                     |
| `%Gx`     | `%{tags-transformed}`    | Individual message tag (e.g. Notmuch tags/imap flags)                                                                          |
| `%g`      | `%{tags}`                | Message tags (e.g. Notmuch tags/imap flags)                                                                                    |
| `%H`      | `%{spam}`                | Spam attribute(s) of this message                                                                                              |
| `%I`      | `%{initials}`            | Initials of author                                                                                                             |
| `%i`      | `%{message-id}`          | Message-id of the current message                                                                                              |
| `%J`      | `%{thread-tags}`         | Message tags (if present, tree unfolded, and != parent's tags)                                                                 |
| `%K`      | `%{list-empty}`          | List to which the email was sent (if any; otherwise: empty)                                                                    |
| `%L`      | `%{from-list}`           | If an address in the `To:` or `Cc:` header field matches an address                                                            |
|           |                          | defined by the user's `$subscribe` command, this displays.                                                                     |
| `%l`      | `%{lines}`               | Number of lines in the unprocessed message (may not work with maildir, mh, and IMAP folders)                                   |
| `%M`      | `%{thread-hidden-count}` | Number of hidden messages if the thread is collapsed                                                                           |
| `%m`      | `%{message-count}`       | Total number of message in the mailbox                                                                                         |
| `%N`      | `%{score}`               | Message score                                                                                                                  |
| `%n`      | `%{name}`                | Author's real name (or address if missing)                                                                                     |
| `%O`      | `%{save-folder}`         | Original save folder where NeoMutt would formerly have Stashed the message:                                                    |
|           |                          | list name or recipient name if not sent to a list                                                                              |
| `%P`      | `%{percentage}`          | Progress indicator for the built-in pager (how much of the file has been displayed)                                            |
| `%q`      | `%{newsgroup}`           | Newsgroup name (if compiled with NNTP support)                                                                                 |
| `%R`      | `%{cc-all}`              | Comma separated list of `Cc:` recipients                                                                                       |
| `%r`      | `%{to-all}`              | Comma separated list of `To:` recipients                                                                                       |
| `%S`      | `%{flag-chars}`          | Single character status of the message (`N`/`O`/`D`/`d`/`!`/`r`/`*`)                                                           |
| `%s`      | `%{subject}`             | Subject of the message                                                                                                         |
| `%T`      | `%{to-chars}`            | Appropriate character from the [`$to_chars`](cfg-to-chars) string                                                                   |
| `%t`      | `%{to}`                  | `%{To:}` field (recipients)                                                                                                    |
| `%u`      | `%{username}`            | User (login) name of the author                                                                                                |
| `%v`      | `%{first-name}`          | First name of the author, or the recipient if the message is from you                                                          |
| `%W`      | `%{organization}`        | Name of organization of author (`Organization:` field)                                                                         |
| `%X`      | `%{attachment-count}`    | Number of MIME attachments (see the `$attachments` section for possible speed effects)                                         |
| `%x`      | `%{x-comment-to}`        | `%{X-Comment-To:}` field (if present)                                                                                          |
| `%Y`      | `%{thread-x-label}`      | `%{X-Label:}` field, if present, and                                                                                           |
|           |                          | 1. not at part of a thread tree                                                                                                |
|           |                          | 2. at the top of a thread, or                                                                                                  |
|           |                          | 3. `X-Label:` is different from Preceding message's `X-Label:`                                                                 |
| `%y`      | `%{x-label}`             | `%{X-Label:}` field, if present                                                                                                |
| `%Z`      | `%{combined-flags}`      | A three character set of message status flags.                                                                                 |
|           |                          | The first character is new/read/replied flags (`n`/`o`/`r`/`O`/`N`).                                                           |
|           |                          | The second is deleted or encryption flags (`D`/`d`/`S`/`P`/`s`/`K`).                                                           |
|           |                          | The third is either tagged/flagged (`*`/`!`), or one of the characters.                                                        |
|           |                          | Listed in [`$to_chars`](cfg-to-chars).                                                                                              |
| `%zc`     | `%{crypto-flags}`        | Message crypto flags                                                                                                           |
| `%zs`     | `%{status-flags}`        | Message status flags                                                                                                           |
| `%zt`     | `%{message-flags}`       | Message tag flags                                                                                                              |
| `%@name@` |                          | Insert and evaluate format-string from the matching ``index-format-hook`` command                                              |
| `%{fmt}`  |                          | Date and time of the message is converted to sender's time zone, and `fmt` is expanded by the library function `strftime(3)`;  |
|           |                          | if the first character inside the braces is a bang (`!`), the date is formatted ignoring any locale settings.                  |
|           |                          | Note that the sender's time zone might only be available as a numerical offset, so `%Z` behaves like `%z`.                     |
|           |                          | `%{fmt}` behaves like `%[fmt]` on systems where `struct tm` doesn't have a `tm_gmtoff` member.                                 |
| `%[fmt]`  |                          | Date and time of the message is converted to the local time zone, and `fmt` is expanded by the library function `strftime(3)`; |
|           |                          | if the first character inside the brackets is a bang (`!`), the date is formatted ignoring any locale settings.                |
| `%(fmt)`  |                          | Local date and time when the message was received, and `fmt` is expanded by the library function `strftime(3)`;                |
|           |                          | if the first character inside the parentheses is a bang (`!`), the date is formatted ignoring any locale settings.             |
| `%*X`     | `%{padding-soft:X}`      | Soft-fill with character `X` as pad                                                                                            |
| `%>X`     | `%{padding-hard:X}`      | Right justify the rest of the string and pad with character `X`                                                                |
| `%\|X`    | `%{padding-eol:X}`       | Pad to the end of the line with character `X`                                                                                  |

Date format expressions can be constructed based on relative dates.
Using the date formatting operators along with nested conditionals, the date format can be modified based on how old a message is.
See the section on "Conditional Dates" for an explanation and examples.

Note that for mbox/mmdf, "%l" applies to the unprocessed message, and for maildir/mh, the value comes from the "Lines:" header field when present (the meaning is normally the same).
Thus the value depends on the encodings used in the different parts of the message and has little meaning in practice.

"Soft-fill" deserves some explanation: Normal right-justification will print everything to the left of the "%>", displaying padding and whatever lies to the right only if there's room.
By contrast, soft-fill gives priority to the right-hand side, guaranteeing space to display it and showing padding only if there's still room.
If necessary, soft-fill will eat text leftwards to make room for rightward text.

Note that these expandos are supported in [`save-hook`](cmd-save-hook), [`fcc-hook`](cmd-fcc-hook) and [`fcc-save-hook`](cmd-fcc-save-hook), too.

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-mark-macro-prefix)=
## `$mark_macro_prefix`

:Type: [String](type-string)
:Default:
    ```neomuttrc
    set mark_macro_prefix = "'"
    ```

Prefix for macros created using mark-message.
A new macro automatically generated with _<mark-message>a_ will be composed from this prefix and the letter _a_.

--------------------------------------------------------------------------------

(cfg-new-mail-command)=
## `$new_mail_command`

:Type: [Expando (Command String)](type-expando)
:Default: (empty)
    ```neomuttrc
    set new_mail_command = ""
    ```

If _set_, NeoMutt will call this command after a new message is received.
See the [`$status_format`](cfg-status-format) documentation for the values that can be formatted into this command.

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-quit)=
## `$quit`

:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set quit = yes
    ```

This variable controls whether "quit" and "exit" actually quit from NeoMutt.
If this option is _set_, they do quit, if it is _unset_, they have no effect, and if it is set to _ask-yes_ or _ask-no_, you are prompted for confirmation when you try to quit.

In order to quit from NeoMutt if this variable is _unset_, you must send the signal SIGINT to NeoMutt.
This can usually be achieved by pressing CTRL-C in the terminal.

--------------------------------------------------------------------------------

(cfg-read-only)=
## `$read_only`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set read_only = no
    ```

If _set_, all folders are opened in read-only mode.

--------------------------------------------------------------------------------

(cfg-status-chars)=
## `$status_chars`

:Type: [Character String](type-mbtable)
:Default:
    ```neomuttrc
    set status_chars = "-*%A"
    ```

Controls the characters used by the "%r" indicator in [`$status_format`](cfg-status-format).

| Character | Default | Description                                                                                                       |
|-----------|---------|-------------------------------------------------------------------------------------------------------------------|
| 1         | `-`     | Mailbox is unchanged                                                                                              |
| 2         | `*`     | Mailbox has been changed and needs to be resynchronized                                                           |
| 3         | `%`     | Mailbox is read-only, or will not be written when exiting.                                                        |
|           |         | You can toggle whether to write changes to a mailbox with the [`<toggle-write>`](fn-index) operation, bound by default to "%" |
| 4         | `A`     | Folder opened in attach-message mode.                                                                             |
|           |         | Certain operations like composing a new mail, replying, forwarding, etc. are not permitted in this mode           |

--------------------------------------------------------------------------------

(cfg-status-format)=
## `$status_format`

:Type: [Expando](type-expando)
:Notes: {ref}`Localised String <type-general>`
:Default:
    ```neomuttrc
    set status_format = "-%r-NeoMutt: %D [Msgs:%<M?%M/>%m%<n? New:%n>%<o? Old:%o> %<d? Del:%d>%<F? Flag:%F> %<t? Tag:%t>%<p? Post:%p>%<b? Inc:%b> %<l? %l>]---(%<T?%T/>%s/%S)-%>-(%P)---"
    ```
:Alternative:
    ```neomuttrc
    set status_format = "-%{readonly}-NeoMutt: %{description} \
    [Msgs:%<M?%{limit-count}/>%{message-count}\
    %<n? New:%{new-count}>\
    %<o? Old:%{old-count}>\
    %<d? Del:%{deleted-count}>\
    %<F? Flag:%{flagged-count}>\
    %<t? Tag:%{tagged-count}>\
    %<p? Post:%{postponed-count}>\
    %<n? Inc:%{unread-mailboxes}>\
    %<l? %{mailbox-size}>]---\
    (%<T?%{use-threads}/>%{sort}/%{sort-aux})-\
    %{padding-hard:-}(%{percentage})---"
    ```

Controls the format of the status line displayed in the "index" menu.
This string is similar to [`$index_format`](cfg-index-format), but has its own set of `printf(3)`-like sequences:

| Short  | Long Name             | Description                                                                                            |
|--------|-----------------------|--------------------------------------------------------------------------------------------------------|
| `%b`   | `%{unread-mailboxes}` | Number of mailboxes with new mail                                                                      |
| `%D`   | `%{description}`      | Description of the mailbox                                                                             |
| `%d`   | `%{deleted-count}`    | Number of deleted messages                                                                             |
| `%f`   | `%{flagged-count}`    | Number of flagged messages                                                                             |
| `%F`   | `%{mailbox-path}`     | Full pathname of the current mailbox                                                                   |
| `%h`   | `%{hostname}`         | Local hostname                                                                                         |
| `%l`   | `%{limit-size}`       | Size (in bytes) of the messages shown (i.e., which match the current limit) (see formatstrings-size)   |
| `%L`   | `%{mailbox-size}`     | Size (in bytes) of the current mailbox (see formatstrings-size)                                        |
| `%m`   | `%{limit-count}`      | Number of messages shown (i.e., which match the current limit)                                         |
| `%M`   | `%{message-count}`    | Number of messages in the mailbox                                                                      |
| `%n`   | `%{new-count}`        | Number of new messages in the mailbox (unread, unseen)                                                 |
| `%o`   | `%{old-count}`        | Number of old messages in the mailbox (unread, seen)                                                   |
| `%p`   | `%{postponed-count}`  | Number of postponed messages                                                                           |
| `%P`   | `%{percentage}`       | Percentage of the way through the index                                                                |
| `%r`   | `%{read-count}`       | Number of read messages in the mailbox (read, seen)                                                    |
| `%R`   | `%{readonly}`         | Modified/read-only/won't-write/attach-message indicator, according to [`$status_chars`](cfg-status-chars)  |
| `%s`   | `%{sort}`             | Current sorting mode (`$sort`)                                                                         |
| `%S`   | `%{sort-aux}`         | Current aux sorting method (`$sort_aux`)                                                               |
| `%t`   | `%{tagged-count}`     | Number of tagged messages in the mailbox                                                               |
| `%T`   | `%{use-threads}`      | Current threading mode (`$use_threads`)                                                                |
| `%u`   | `%{unread-count}`     | Number of unread messages in the mailbox (seen or unseen)                                              |
| `%v`   | `%{limit-pattern}`    | Currently active limit pattern, if any                                                                 |
| `%V`   | `%{version}`          | NeoMutt version string                                                                                 |
| `%*X`  | `%{padding-soft:X}`   | Soft-fill with character `X` as pad                                                                    |
| `%>X`  | `%{padding-hard:X}`   | Right justify the rest of the string and pad with character `X`                                        |
| `%\|X` | `%{padding-eol:X}`    | Pad to the end of the line with character `X`                                                          |

Some of the above sequences can be used to optionally print a string if their value is nonzero.
For example, you may only want to see the number of flagged messages if such messages exist, since zero is not particularly meaningful.
To optionally print a string based upon one of the above sequences, the following construct is used:

`%<sequence_char?optional_string>`

where _sequence_char_ is a character from the table above, and _optional_string_ is the string you would like printed if _sequence_char_ is nonzero.
_optional_string_ **may** contain other sequences as well as normal text.

Here is an example illustrating how to optionally print the number of new messages in a mailbox:

`%<n?%n new messages>`

You can also switch between two strings using the following construct:

`%<sequence_char?if_string&else_string>`

If the value of _sequence_char_ is non-zero, _if_string_ will be expanded, otherwise _else_string_ will be expanded.

As another example, here is how to show either [`$sort`](cfg-sort) and [`$sort_aux`](cfg-sort-aux) or [`$use_threads`](cfg-use-threads) and [`$sort`](cfg-sort), based on whether threads are enabled with [`$use_threads`](cfg-use-threads):

`%<T?%s/%S&%T/%s>`

You can force the result of any `printf(3)`-like sequence to be lowercase by prefixing the sequence character with an underscore ("_")
sign.
For example, if you want to display the local hostname in lowercase, you would use: "`%_h`".

If you prefix the sequence character with a colon (":") character, NeoMutt will replace any dots in the expansion by underscores.
This might be helpful with IMAP folders that don't like dots in folder names.

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

(cfg-to-chars)=
## `$to_chars`

:Type: [Character String](type-mbtable)
:Default:
    ```neomuttrc
    set to_chars = " +TCFLR"
    ```

Controls the character used to indicate mail addressed to you.

| Character | Default     | Description                                                                                       |
|-----------|-------------|---------------------------------------------------------------------------------------------------|
| 1         | ` ` (space) | The mail is *not* addressed to your address                                                       |
| 2         | `+`         | You are the only recipient of the message                                                         |
| 3         | `T`         | Your address appears in the "To:" header field, but you are not the only recipient of the message |
| 4         | `C`         | Your address is specified in the "Cc:" header field, but you are not the only recipient           |
| 5         | `F`         | Indicates the mail that was sent by *you*                                                         |
| 6         | `L`         | Indicates the mail was sent to a mailing-list you subscribe to                                    |
| 7         | `R`         | Your address appears in the "Reply-To:" header field but none of the above applies                |

--------------------------------------------------------------------------------

(cfg-ts-enabled)=
## `$ts_enabled`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set ts_enabled = no
    ```

Controls whether NeoMutt tries to set the terminal status line and icon name.
Most terminal emulators emulate the status line in the window title.

--------------------------------------------------------------------------------

(cfg-ts-icon-format)=
## `$ts_icon_format`

:Type: [Expando](type-expando)
:Notes: {ref}`Localised String <type-general>`
:Default:
    ```neomuttrc
    set ts_icon_format = "M%<n?AIL&ail>"
    ```
:Alternative:
    ```neomuttrc
    set ts_icon_format = "M%<{new-count}?AIL&ail>"
    ```

Controls the format of the icon title, as long as "[`$ts_enabled`](cfg-ts-enabled)" is set.
This string is identical in formatting to the one used by "[`$status_format`](cfg-status-format)".

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-ts-status-format)=
## `$ts_status_format`

:Type: [Expando](type-expando)
:Notes: {ref}`Localised String <type-general>`
:Default:
    ```neomuttrc
    set ts_status_format = "NeoMutt with %<m?%m messages&no messages>%<n? [%n NEW]>"
    ```
:Alternative:
    ```neomuttrc
    set ts_status_format = "NeoMutt with %<m?%{message-count} messages&no messages>%<n? [%{new-count} NEW]>"
    ```

Controls the format of the terminal status line (or window title), provided that "[`$ts_enabled`](cfg-ts-enabled)" has been set.
This string is identical in formatting to the one used by "[`$status_format`](cfg-status-format)".

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-uncollapse-jump)=
## `$uncollapse_jump`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set uncollapse_jump = no
    ```

When _set_, NeoMutt will jump to the next unread message, if any, when the current thread is _un_collapsed.

--------------------------------------------------------------------------------

(cfg-uncollapse-new)=
## `$uncollapse_new`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set uncollapse_new = yes
    ```

When _set_, NeoMutt will automatically uncollapse any collapsed thread that receives a newly delivered message.
When _unset_, collapsed threads will remain collapsed.
The presence of the newly delivered message will still affect index sorting, though.

