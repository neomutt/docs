---
title: Email Options
description: Configuration option for email display, MIME handling, mailcap, scoring, text reflow, and reply threading.
keywords: email, mime, mailcap, scoring, reflow_text, reply_regex, reverse_alias, rfc2047, spam, auto_subscribe, multipart, format flowed
---

(ref-cfg-email)=
# Email Options

(cfg-auto-subscribe)=
## `$auto_subscribe`

:Description: Automatically check if the user is subscribed to a mailing list
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set auto_subscribe = no
    ```

When _set_, NeoMutt assumes the presence of a List-Post header means the recipient is subscribed to the list.
Unless the mailing list is in the "unsubscribe" or "unlist" lists, it will be added to the [`:subscribe`](cmd-subscribe) list.
Parsing and checking these things slows header reading down, so this option is disabled by default.

--------------------------------------------------------------------------------

(cfg-honor-disposition)=
## `$honor_disposition`

:Description: Don't display MIME parts inline if they have a disposition of "attachment"
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set honor_disposition = no
    ```

**Set**

NeoMutt will not display attachments with a disposition of "attachment" inline even if it could render the part to plain text.
These MIME parts can only be viewed from the attachment menu.

**Unset**

NeoMutt will render all MIME parts it can properly transform to plain text.

--------------------------------------------------------------------------------

(cfg-hidden-tags)=
## `$hidden_tags`

:Description: List of tags that shouldn't be displayed on screen (comma-separated)
:Type: [String List](type-slist)
:Notes: [Comma-separated](type-slist)
:Default:
    ```neomuttrc
    set hidden_tags = "unread,draft,flagged,passed,replied,attachment,signed,encrypted"
    ```

Specify a list of comma-separated private notmuch/imap tags which should not be printed on screen.

--------------------------------------------------------------------------------

(cfg-implicit-auto-view)=
## `$implicit_auto_view`

:Description: Display MIME attachments inline if a `copiousoutput` mailcap entry exists
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set implicit_auto_view = no
    ```

If set to `yes`, NeoMutt will look for a mailcap entry with the `copiousoutput` flag set for _every_ MIME attachment it doesn't have an internal viewer defined for.
If such an entry is found, NeoMutt will use the viewer defined in that entry to convert the body part to text form.

--------------------------------------------------------------------------------

(cfg-include-encrypted)=
## `$include_encrypted`

:Description: Whether to include encrypted content when replying
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set include_encrypted = no
    ```

Controls whether or not NeoMutt includes separately encrypted attachment contents when replying.

Prevent accidental exposure of encrypted contents when replying to an attacker.
If a previously encrypted message were attached by the attacker, they could trick an unwary recipient into decrypting and including the message in their reply.

--------------------------------------------------------------------------------

(cfg-include-only-first)=
## `$include_only_first`

:Description: Only include the first attachment when replying
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set include_only_first = no
    ```

Controls whether or not NeoMutt includes only the first attachment of the message you are replying.

--------------------------------------------------------------------------------

(cfg-mailcap-path)=
## `$mailcap_path`

:Description: List of mailcap files (colon-separated)
:Type: [String List](type-slist)
:Notes: [Colon-separated](type-slist)
:Default:
    ```neomuttrc
    set mailcap_path = "~/.mailcap:/usr/share/neomutt/mailcap:/etc/mailcap:/usr/etc/mailcap:/usr/local/etc/mailcap"
    ```

Specify a list of files to consult when attempting to display MIME bodies not directly supported by NeoMutt.
The default value is generated during startup: see the "$mailcap" section of the manual.

It is overridden by the environment variable [`$MAILCAPS`](ref-env).

The default search path is from [RFC1524](https://www.rfc-editor.org/rfc/rfc1524.html).

--------------------------------------------------------------------------------

(cfg-mailcap-sanitize)=
## `$mailcap_sanitize`

:Description: Restrict the possible characters in mailcap expandos
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set mailcap_sanitize = yes
    ```

If _set_, NeoMutt will restrict possible characters in mailcap % expandos to a well-defined set of safe characters.
This is the safe setting, but we are not sure it doesn't break some more advanced MIME stuff.

:::{danger}
Don't change this setting unless you are really sure what you are doing!
:::

--------------------------------------------------------------------------------

(cfg-preferred-languages)=
## `$preferred_languages`

:Description: List of Preferred Languages for multilingual MIME (comma-separated)
:Type: [String List](type-slist)
:Notes: [Comma-separated](type-slist)
:Default: (empty)
    ```neomuttrc
    set preferred_languages = ""
    ```

Specify a list of comma-separated languages.
[RFC8255](https://www.rfc-editor.org/rfc/rfc8255.html) : user preferred languages to be searched in parts and display.

Example:
```neomuttrc
set preferred_languages = "en,fr,de"
```

--------------------------------------------------------------------------------

(cfg-reflow-space-quotes)=
## `$reflow_space_quotes`

:Description: Insert spaces into reply quotes for `format=flowed` messages
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set reflow_space_quotes = yes
    ```

Control how quotes from format=flowed messages are displayed in the pager and when replying (with [`$text_flowed`](cfg-text-flowed) _unset_).
When set, this option adds spaces after each level of quote marks, turning ">>>foo" into "> > > foo".

:::{note}
- If [`$reflow_text`](cfg-reflow-text) is _unset_, this option has no effect.
- This option does not affect replies when [`$text_flowed`](cfg-text-flowed) is _set_.
:::

--------------------------------------------------------------------------------

(cfg-reflow-text)=
## `$reflow_text`

:Description: Reformat paragraphs of `format=flowed` text
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set reflow_text = yes
    ```

When _set_, NeoMutt will reformat paragraphs in text/plain parts marked format=flowed.
If _unset_, NeoMutt will display paragraphs unaltered from how they appear in the message body.
See [RFC3676](https://www.rfc-editor.org/rfc/rfc3676.html) for details on the _format=flowed_ format.

:::{seealso}
{ref}`how-text-wrapping`, [`$reflow_wrap`](cfg-reflow-wrap), [`$wrap`](cfg-wrap)
:::

--------------------------------------------------------------------------------

(cfg-reflow-wrap)=
## `$reflow_wrap`

:Description: Maximum paragraph width for reformatting `format=flowed` text
:Type: [Number](type-number)
:Default:
    ```neomuttrc
    set reflow_wrap = 78
    ```

Control the maximum paragraph width when reformatting text/plain parts when [`$reflow_text`](cfg-reflow-text) is _set_.
When the value is 0, paragraphs will be wrapped at the terminal's right margin.
A positive value sets the paragraph width relative to the left margin.
A negative value set the paragraph width relative to the right margin.

Be aware that the reformatted lines of a paragraph are still subject to [`$wrap`](cfg-wrap).
This means if [`$reflow_wrap`](cfg-reflow-wrap) is 40 and [`$wrap`](cfg-wrap) is 30, then the paragraph gets reformatted to 40 characters a line (due to [`$reflow_wrap`](cfg-reflow-wrap)) and afterwards each 40-character-line is split at 30 characters (due to [`$wrap`](cfg-wrap)), resulting in alternating line lengths of 30 and 10 characters.

:::{seealso}
{ref}`how-text-wrapping`, [`$wrap`](cfg-wrap)
:::

--------------------------------------------------------------------------------

(cfg-reply-regex)=
## `$reply_regex`

:Description: Regex to match message reply subjects like `re: `
:Type: [Regular Expression](type-regex)
:Notes: [Localised String](type-general), [Smart Case](type-general)
:Default:
    ```neomuttrc
    set reply_regex = "^((re)(\\[[0-9]+\\])*:[ \t]*)*"
    ```

A regular expression used to recognize reply messages when threading and replying.
The default value corresponds to the standard Latin `Re:` prefix.

This value may have been localized by the translator for your locale, adding other prefixes that are common in the locale.
You can add your own prefixes by appending inside `^(re)`.  For example: `^(re|sv)` or `^(re|aw|sv)`.

The second parenthesized expression matches zero or more bracketed numbers following the prefix, such as `Re[1]: `.
The initial `\\[` means a literal left-bracket character.
Note the backslash must be doubled when used inside a double quoted string in the neomuttrc.
`[0-9]+` means one or more numbers.
`\\]` means a literal right-bracket.
Finally the whole parenthesized expression has a `*` suffix, meaning it can occur zero or more times.

The last part matches a colon followed by an optional space or tab.
Note `\t` is converted to a literal tab inside a double quoted string.
If you use a single quoted string, you would have to type an actual tab character, and would need to convert the double-backslashes to single backslashes.

:::{note}
the result of this regex match against the subject is stored in the header cache.
NeoMutt isn't smart enough to invalidate a header cache entry based on changing [`$reply_regex`](cfg-reply-regex), so if you aren't seeing correct values in the index, try temporarily turning off the header cache.
If that fixes the problem, then once the option is set to your liking, remove your stale header cache files and turn the header cache back on.
:::

--------------------------------------------------------------------------------

(cfg-reverse-alias)=
## `$reverse_alias`

:Description: Display the alias in the index, rather than the message's sender
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set reverse_alias = no
    ```

Control whether NeoMutt displays the "personal" name from your aliases in the index menu if it finds an alias that matches the message's sender.
For example, if you have the following alias:

```neomuttrc
alias juser abd30425@somewhere.net (Joe User)
```

and then you receive mail which contains the following header:

```email
From: abd30425@somewhere.net
```

It would be displayed in the index menu as "Joe User" instead of "abd30425@somewhere.net."  This is useful when the person's e-mail address is not human friendly.

--------------------------------------------------------------------------------

(cfg-rfc2047-parameters)=
## `$rfc2047_parameters`

:Description: Decode [RFC2047](https://www.rfc-editor.org/rfc/rfc2047.html)-encoded MIME parameters
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set rfc2047_parameters = yes
    ```

When this option is _set_, NeoMutt will decode [RFC2047](https://www.rfc-editor.org/rfc/rfc2047.html)-encoded MIME parameters.
You want to set this option when NeoMutt suggests you to save attachments to files named like:

```
=?iso-8859-1?Q?file=5F=E4=5F991116=2Ezip?=
=?utf-8?Q?z=C4=99ta.png?=
```

When this option is _set_ interactively, the change won't be active until you change folders.

:::{note}
This use of [RFC2047](https://www.rfc-editor.org/rfc/rfc2047.html)'s encoding is explicitly prohibited by the standard,
but nevertheless encountered in the wild and produced by, e.g., Outlook.
:::

:::{note}
Setting this parameter will _not_ have the effect that NeoMutt _generates_ this kind of encoding.
Instead, NeoMutt will unconditionally use the encoding specified in [RFC2231](https://www.rfc-editor.org/rfc/rfc2231.html).
:::

--------------------------------------------------------------------------------

(cfg-score)=
## `$score`

:Description: Use message scoring
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set score = yes
    ```

When this option is _unset_, scoring is turned off.
This can be useful to selectively disable scoring for certain folders when [`$score_threshold_delete`](cfg-score-threshold-delete) and related are used.

--------------------------------------------------------------------------------

(cfg-score-threshold-delete)=
## `$score_threshold_delete`

:Description: Messages with a lower score will be automatically deleted
:Type: [Number](type-number)
:Default:
    ```neomuttrc
    set score_threshold_delete = -1
    ```

Messages which have been assigned a score equal to or lower than the value of this option are automatically marked for deletion by NeoMutt.
Since NeoMutt scores are always greater than or equal to zero, the default setting of this option will never mark a message for deletion.

--------------------------------------------------------------------------------

(cfg-score-threshold-flag)=
## `$score_threshold_flag`

:Description: Messages with a greater score will be automatically flagged
:Type: [Number](type-number)
:Default:
    ```neomuttrc
    set score_threshold_flag = 9999
    ```

Messages which have been assigned a score greater than or equal to this option's value are automatically marked "flagged".

--------------------------------------------------------------------------------

(cfg-score-threshold-read)=
## `$score_threshold_read`

:Description: Messages with a lower score will be automatically marked read
:Type: [Number](type-number)
:Default:
    ```neomuttrc
    set score_threshold_read = -1
    ```

Messages which have been assigned a score equal to or lower than the value of this option are automatically marked as read by NeoMutt.
Since NeoMutt scores are always greater than or equal to zero, the default setting of this option will never mark a message read.

--------------------------------------------------------------------------------

(cfg-show-multipart-alternative)=
## `$show_multipart_alternative`

:Description: How to display `multipart/alternative` MIME parts
:Type: [String](type-string)
:Notes: [Case Sensitive](type-general)
:Default: (empty)
    ```neomuttrc
    set show_multipart_alternative = ""
    ```

| Setting  | Action                                     |
|----------|--------------------------------------------|
| unset    | Only show the chosen alternative           |
| `info`   | Show the multipart/alternative information |
| `inline` | All of the alternatives are displayed      |

--------------------------------------------------------------------------------

(cfg-spam-separator)=
## `$spam_separator`

:Description: Separator for multiple spam headers
:Type: [String](type-string)
:Default:
    ```neomuttrc
    set spam_separator = ","
    ```

Control what happens when multiple spam headers are matched: if _unset_, each successive header will overwrite any previous matches value for the spam label.
If _set_, each successive match will append to the previous, using this option's value as a separator.

