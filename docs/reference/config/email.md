---
title: Email Options
description: Configuration variables for email display, MIME handling, mailcap, scoring, text reflow, and reply threading.
keywords: email, mime, mailcap, scoring, reflow_text, reply_regex, reverse_alias, rfc2047, spam, auto_subscribe, multipart, format flowed
---

(cfg-email)=
# Conn Options

(auto-subscribe)=
## `$auto_subscribe`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set auto_subscribe = no
    ```

When _set_, NeoMutt assumes the presence of a List-Post header means the recipient is subscribed to the list.
Unless the mailing list is in the "unsubscribe" or "unlist" lists, it will be added to the [`subscribe`](cmd-subscribe) list.
Parsing and checking these things slows header reading down, so this option is disabled by default.

--------------------------------------------------------------------------------

(honor-disposition)=
## `$honor_disposition`

:Type: [Boolean](bool)
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

(hidden-tags)=
## `$hidden_tags`

:Type: [String List](slist)
:Notes: [Comma-separated](slist)
:Default:
    ```neomuttrc
    set hidden_tags = "unread,draft,flagged,passed,replied,attachment,signed,encrypted"
    ```

This variable specifies a list of comma-separated private notmuch/imap tags which should not be printed on screen.

--------------------------------------------------------------------------------

(implicit-auto-view)=
## `$implicit_auto_view`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set implicit_auto_view = no
    ```

If set to "yes", NeoMutt will look for a mailcap entry with the `copiousoutput` flag set for _every_ MIME attachment it doesn't have an internal viewer defined for.
If such an entry is found, NeoMutt will use the viewer defined in that entry to convert the body part to text form.

--------------------------------------------------------------------------------

(include-encrypted)=
## `$include_encrypted`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set include_encrypted = no
    ```

Controls whether or not NeoMutt includes separately encrypted attachment contents when replying.

This variable was added to prevent accidental exposure of encrypted contents when replying to an attacker.
If a previously encrypted message were attached by the attacker, they could trick an unwary recipient into decrypting and including the message in their reply.

--------------------------------------------------------------------------------

(include-only-first)=
## `$include_only_first`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set include_only_first = no
    ```

Controls whether or not NeoMutt includes only the first attachment of the message you are replying.

--------------------------------------------------------------------------------

(mailcap-path)=
## `$mailcap_path`

:Type: [String List](slist)
:Notes: [Colon-separated](slist)
:Default:
    ```neomuttrc
    set mailcap_path = "~/.mailcap:" PKGDATADIR "/mailcap:" SYSCONFDIR "/mailcap:/etc/mailcap:/usr/etc/mailcap:/usr/local/etc/mailcap"
    ```

This variable specifies a list of colon-separated files to consult when attempting to display MIME bodies not directly supported by NeoMutt.
The default value is generated during startup: see the "$mailcap" section of the manual.

[`$mailcap_path`](mailcap-path) is overridden by the environment variable `$MAILCAPS`.

The default search path is from [RFC1524](https://www.rfc-editor.org/rfc/rfc1524.html).

--------------------------------------------------------------------------------

(mailcap-sanitize)=
## `$mailcap_sanitize`

:Type: [Boolean](bool)
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

(preferred-languages)=
## `$preferred_languages`

:Type: [String List](slist)
:Notes: [Comma-separated](slist)
:Default: (empty)
    ```neomuttrc
    set preferred_languages = ""
    ```

This variable specifies a list of comma-separated languages.
[RFC8255](https://www.rfc-editor.org/rfc/rfc8255.html) : user preferred languages to be searched in parts and display.

Example:
```neomuttrc
set preferred_languages = "en,fr,de"
```

--------------------------------------------------------------------------------

(reflow-space-quotes)=
## `$reflow_space_quotes`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set reflow_space_quotes = yes
    ```

This option controls how quotes from format=flowed messages are displayed in the pager and when replying (with [`$text_flowed`](text-flowed) _unset_).
When set, this option adds spaces after each level of quote marks, turning ">>>foo" into "> > > foo".

:::{note}
If [`$reflow_text`](reflow-text) is _unset_, this option has no effect.
:::

Also, this option does not affect replies when [`$text_flowed`](text-flowed) is _set_.

--------------------------------------------------------------------------------

(reflow-text)=
## `$reflow_text`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set reflow_text = yes
    ```

When _set_, NeoMutt will reformat paragraphs in text/plain parts marked format=flowed.
If _unset_, NeoMutt will display paragraphs unaltered from how they appear in the message body.
See [RFC3676](https://www.rfc-editor.org/rfc/rfc3676.html) for details on the _format=flowed_ format.

Also see [`$reflow_wrap`](reflow-wrap), and [`$wrap`](wrap).

--------------------------------------------------------------------------------

(reflow-wrap)=
## `$reflow_wrap`

:Type: [Number](number)
:Default:
    ```neomuttrc
    set reflow_wrap = 78
    ```

This variable controls the maximum paragraph width when reformatting text/plain parts when [`$reflow_text`](reflow-text) is _set_.
When the value is 0, paragraphs will be wrapped at the terminal's right margin.
A positive value sets the paragraph width relative to the left margin.
A negative value set the paragraph width relative to the right margin.

Be aware that the reformatted lines of a paragraph are still subject to [`$wrap`](wrap).
This means if [`$reflow_wrap`](reflow-wrap) is 40 and [`$wrap`](wrap) is 30, then the paragraph gets reformatted to 40 characters a line (due to [`$reflow_wrap`](reflow-wrap)) and afterwards each 40-character-line is split at 30 characters (due to [`$wrap`](wrap)), resulting in alternating line lengths of 30 and 10 characters.

Also see [`$wrap`](wrap).

--------------------------------------------------------------------------------

(reply-regex)=
## `$reply_regex`

:Type: [Regular Expression](regex)
:Notes: {ref}`Localised String <general>`
:Default:
    ```neomuttrc
    set reply_regex = "^((re)(\\[[0-9]+\\])*:[ \t]*)*"
    ```

A regular expression used to recognize reply messages when threading and replying.
The default value corresponds to the standard Latin "Re:" prefix.

This value may have been localized by the translator for your locale, adding other prefixes that are common in the locale.
You can add your own prefixes by appending inside `"^(re)"`.  For example: `"^(re|sv)"` or `"^(re|aw|sv)"`.

The second parenthesized expression matches zero or more bracketed numbers following the prefix, such as `"Re[1]: "`.
The initial `"\\["` means a literal left-bracket character.
Note the backslash must be doubled when used inside a double quoted string in the neomuttrc.
`"[0-9]+"` means one or more numbers.
`"\\]"` means a literal right-bracket.
Finally the whole parenthesized expression has a `"*"` suffix, meaning it can occur zero or more times.

The last part matches a colon followed by an optional space or tab.
Note `"\t"` is converted to a literal tab inside a double quoted string.
If you use a single quoted string, you would have to type an actual tab character, and would need to convert the double-backslashes to single backslashes.

:::{note}
the result of this regex match against the subject is stored in the header cache.
:::
Mutt isn't smart enough to invalidate a header cache entry based on changing [`$reply_regex`](reply-regex), so if you aren't seeing correct values in the index, try temporarily turning off the header cache.
If that fixes the problem, then once the variable is set to your liking, remove your stale header cache files and turn the header cache back on.

--------------------------------------------------------------------------------

(reverse-alias)=
## `$reverse_alias`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set reverse_alias = no
    ```

This variable controls whether or not NeoMutt will display the "personal" name from your aliases in the index menu if it finds an alias that matches the message's sender.
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

(rfc2047-parameters)=
## `$rfc2047_parameters`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set rfc2047_parameters = yes
    ```

When this variable is _set_, NeoMutt will decode [RFC2047](https://www.rfc-editor.org/rfc/rfc2047.html)-encoded MIME parameters.
You want to set this variable when NeoMutt suggests you to save attachments to files named like:

```
=?iso-8859-1?Q?file=5F=E4=5F991116=2Ezip?=
=?utf-8?Q?z=C4=99ta.png?=
```

When this variable is _set_ interactively, the change won't be active until you change folders.

Note that this use of [RFC2047](https://www.rfc-editor.org/rfc/rfc2047.html)'s encoding is explicitly prohibited by the standard, but nevertheless encountered in the wild and produced by, e.g., Outlook.

Also note that setting this parameter will _not_ have the effect that NeoMutt _generates_ this kind of encoding.
Instead, NeoMutt will unconditionally use the encoding specified in [RFC2231](https://www.rfc-editor.org/rfc/rfc2231.html).

--------------------------------------------------------------------------------

(score)=
## `$score`

:Type: [Boolean](bool)
:Default:
    ```neomuttrc
    set score = yes
    ```

When this variable is _unset_, scoring is turned off.
This can be useful to selectively disable scoring for certain folders when the [`$score_threshold_delete`](score-threshold-delete) variable and related are used.

--------------------------------------------------------------------------------

(score-threshold-delete)=
## `$score_threshold_delete`

:Type: [Number](number)
:Default:
    ```neomuttrc
    set score_threshold_delete = -1
    ```

Messages which have been assigned a score equal to or lower than the value of this variable are automatically marked for deletion by NeoMutt.
Since NeoMutt scores are always greater than or equal to zero, the default setting of this variable will never mark a message for deletion.

--------------------------------------------------------------------------------

(score-threshold-flag)=
## `$score_threshold_flag`

:Type: [Number](number)
:Default:
    ```neomuttrc
    set score_threshold_flag = 9999
    ```

Messages which have been assigned a score greater than or equal to this variable's value are automatically marked "flagged".

--------------------------------------------------------------------------------

(score-threshold-read)=
## `$score_threshold_read`

:Type: [Number](number)
:Default:
    ```neomuttrc
    set score_threshold_read = -1
    ```

Messages which have been assigned a score equal to or lower than the value of this variable are automatically marked as read by NeoMutt.
Since NeoMutt scores are always greater than or equal to zero, the default setting of this variable will never mark a message read.

--------------------------------------------------------------------------------

(show-multipart-alternative)=
## `$show_multipart_alternative`

:Type: [String](string)
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

(spam-separator)=
## `$spam_separator`

:Type: [String](string)
:Default:
    ```neomuttrc
    set spam_separator = ","
    ```

This variable controls what happens when multiple spam headers are matched: if _unset_, each successive header will overwrite any previous matches value for the spam label.
If _set_, each successive match will append to the previous, using this variable's value as a separator.

