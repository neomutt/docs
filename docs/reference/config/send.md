---
title: Send Options
description: Configuration variables for composing and sending email, SMTP settings, signatures, encoding, and reply attribution.
keywords: neomutt, send, smtp, sendmail, smtp_url, signature, attribution_intro, forward_format, abort_noattach, allow_8bit, encoding, outgoing mail, reply, compose
---

(ref-cfg-send)=
# Send Options

(cfg-abort-noattach)=
## `$abort_noattach`

:Description: Abort sending the email if attachments are missing
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set abort_noattach = no
    ```

If set to _yes_, when composing messages containing the regular expression specified by [`$abort_noattach_regex`](cfg-abort-noattach-regex) and no attachments are given, composition will be aborted.
If set to _no_, composing messages as such will never be aborted.

Example:

```neomuttrc
set abort_noattach_regex = "\\<attach(|ed|ments?)\\>"
```

--------------------------------------------------------------------------------

(cfg-abort-noattach-regex)=
## `$abort_noattach_regex`

:Description: Regex to match text indicating attachments are expected
:Type: [Regular Expression](type-regex)
:Notes: [Localised String](type-general), [Smart Case](type-general)
:Default:
    ```neomuttrc
    set abort_noattach_regex = "\\<(attach|attached|attachments?)\\>"
    ```

Specifies a regular expression to match against the body of the message, to determine if an attachment was mentioned but mistakenly forgotten.
If it matches, [`$abort_noattach`](cfg-abort-noattach) will be consulted to determine if message sending will be aborted.

--------------------------------------------------------------------------------

(cfg-abort-nosubject)=
## `$abort_nosubject`

:Description: Abort creating the email if subject is missing
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set abort_nosubject = ask-yes
    ```

If set to _yes_, when composing messages and no subject is given at the subject prompt, composition will be aborted.
If set to _no_, composing messages with no subject given at the subject prompt will never be aborted.

--------------------------------------------------------------------------------

(cfg-abort-unmodified)=
## `$abort_unmodified`

:Description: Abort the sending if the message hasn't been edited
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set abort_unmodified = yes
    ```

If set to _yes_, composition will automatically abort after editing the message body if no changes are made to the file (this check only happens after the _first_ edit of the file).
When set to _no_, composition will never be aborted.

--------------------------------------------------------------------------------

(cfg-allow-8bit)=
## `$allow_8bit`

:Description: Allow 8-bit messages, don't use quoted-printable or base64
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set allow_8bit = yes
    ```

Controls whether 8-bit data is converted to 7-bit using either **Quoted-Printable** or **Base64** encoding when sending mail.

--------------------------------------------------------------------------------

(cfg-ask-bcc)=
## `$ask_bcc`

:Description: Ask the user for the blind-carbon-copy recipients
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set ask_bcc = no
    ```

If _set_, NeoMutt will prompt you for blind-carbon-copy, `Bcc:`, recipients before editing an outgoing message.

--------------------------------------------------------------------------------

(cfg-ask-cc)=
## `$ask_cc`

:Description: Ask the user for the carbon-copy recipients
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set ask_cc = no
    ```

If _set_, NeoMutt will prompt you for carbon-copy, `Cc:`, recipients before editing the body of an outgoing message.

--------------------------------------------------------------------------------

(cfg-ask-followup-to)=
## `$ask_followup_to`

:Description: Ask the user for follow-up groups before editing
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set ask_followup_to = no
    ```

If set, NeoMutt will prompt you for follow-up groups before editing the body of an outgoing message.

--------------------------------------------------------------------------------

(cfg-ask-x-comment-to)=
## `$ask_x_comment_to`

:Description: Ask the user for the `X-Comment-To` field before editing
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set ask_x_comment_to = no
    ```

If set, NeoMutt will prompt you for `X-Comment-To:` field before editing the body of an outgoing message.

--------------------------------------------------------------------------------

(cfg-attach-charset)=
## `$attach_charset`

:Description: When attaching files, use one of these character sets
:Type: [String List](type-slist)
:Notes: [Colon-separated](type-slist), [Allow Empty](type-slist)
:Default: (empty)
    ```neomuttrc
    set attach_charset = ""
    ```

This variable is a colon-separated list of character encoding schemes for text file attachments.
NeoMutt uses this setting to guess which encoding files being attached are encoded in to convert them to a proper character set given in [`$send_charset`](cfg-send-charset).

If _unset_, the value of [`$charset`](cfg-charset) will be used instead.

For example, the following configuration would work for Japanese text handling:
```neomuttrc
set attach_charset = "iso-2022-jp:euc-jp:shift_jis:utf-8"
```

:::{note}
for Japanese users, "iso-2022-*" must be put at the head of the value as shown above if included.
:::

--------------------------------------------------------------------------------

(cfg-attribution-intro)=
## `$attribution_intro`

:Description: Message to start a reply, "On DATE, PERSON wrote:"
:Type: [Expando](type-expando)
:Notes: [Localised String](type-general), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set attribution_intro = "On %d, %n wrote:"
    ```
:Alternative:
    ```neomuttrc
    set attribution_intro = "On %{date-format}, %{name} wrote:"
    ```

This string will precede a replied-to message which is quoted in the main body of the reply (this is the case when [`$include`](cfg-include) is set).

:::{seealso}
- {doc}`/howto/email-template`
- [`$index_format`](cfg-index-format) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
- [`$attribution_locale`](cfg-attribution-locale)
:::

--------------------------------------------------------------------------------

(cfg-attribution-locale)=
## `$attribution_locale`

:Description: Locale for dates in the `$attribution` message
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set attribution_locale = ""
    ```

The locale used by [`strftime(3)`](exp-strftime) to format dates in the attribution strings.
Valid values are the strings your system accepts for the locale environment variable [`$LC_TIME`](ref-env).

This variable is to allow the attribution date format to be customized by recipient or folder using hooks.
By default, NeoMutt will use your locale environment, so there is no need to set this except to override that default.


:::{seealso}
- {doc}`/howto/email-template`
- Affected variables: [`$attribution_intro`](cfg-attribution-intro), [`$attribution_trailer`](cfg-attribution-trailer), [`$forward_attribution_intro`](cfg-forward-attribution-intro), [`$forward_attribution_trailer`](cfg-forward-attribution-trailer), [`$indent_string`](cfg-indent-string).
:::

--------------------------------------------------------------------------------

(cfg-attribution-trailer)=
## `$attribution_trailer`

:Description: Suffix message to add after reply text
:Type: [Expando](type-expando)
:Notes: [Pipe Support](type-pipe)
:Default: (empty)
    ```neomuttrc
    set attribution_trailer = ""
    ```

Similar to the [`$attribution_intro`](cfg-attribution-intro) variable, this is the string that will come after a replied-to message which is quoted in the main body of the reply (this is the case when [`$include`](cfg-include) is set).

:::{seealso}
- {doc}`/howto/email-template`
- [`$index_format`](cfg-index-format) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
- [`$attribution_locale`](cfg-attribution-locale)
:::

--------------------------------------------------------------------------------

(cfg-bounce-delivered)=
## `$bounce_delivered`

:Description: Add `Delivered-To` to bounced messages
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set bounce_delivered = yes
    ```

When this variable is _set_, NeoMutt will include `Delivered-To:` headers when bouncing messages.
Postfix users may wish to _unset_ this variable.

--------------------------------------------------------------------------------

(cfg-confirm-empty-to)=
## `$confirm_empty_to`

:Description: Ask for a confirmation before sending an email with an empty `To:` recipients list
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set confirm_empty_to = no
    ```

When _set_, NeoMutt will prompt for confirmation when sending an e-mail with an empty `To:` recipients list.

--------------------------------------------------------------------------------

(cfg-content-type)=
## `$content_type`

:Description: Default `Content-Type` for newly composed messages
:Type: [String](type-string)
:Default:
    ```neomuttrc
    set content_type = "text/plain"
    ```

Sets the default `Content-Type:` for the body of newly composed messages.

--------------------------------------------------------------------------------

(cfg-crypt-auto-encrypt)=
## `$crypt_auto_encrypt`

:Description: Automatically PGP encrypt all outgoing mail
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_auto_encrypt = no
    ```

Setting this variable will cause NeoMutt to always attempt to PGP encrypt outgoing messages.
This is probably only useful in connection to the [`:send-hook`](cmd-send-hook) command.
It can be overridden by use of the pgp menu, when encryption is not required or signing is requested as well.
If [`$smime_is_default`](cfg-smime-is-default) is _set_, then OpenSSL is used instead to create S/MIME messages and settings can be overridden by use of the smime menu instead.

--------------------------------------------------------------------------------

(cfg-crypt-auto-pgp)=
## `$crypt_auto_pgp`

:Description: Allow automatic PGP functions
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set crypt_auto_pgp = yes
    ```

This variable controls whether or not NeoMutt may automatically enable PGP encryption/signing for messages.

:::{seealso}
[`$crypt_auto_encrypt`](cfg-crypt-auto-encrypt), [`$crypt_reply_encrypt`](cfg-crypt-reply-encrypt), [`$crypt_auto_sign`](cfg-crypt-auto-sign), [`$crypt_reply_sign`](cfg-crypt-reply-sign), attribution_locale [`$smime_is_default`](cfg-smime-is-default)
:::

--------------------------------------------------------------------------------

(cfg-crypt-auto-sign)=
## `$crypt_auto_sign`

:Description: Automatically PGP sign all outgoing mail
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_auto_sign = no
    ```

Setting this variable will cause NeoMutt to always attempt to cryptographically sign outgoing messages.
This can be overridden by use of the pgp menu, when signing is not required or encryption is requested as well.
If [`$smime_is_default`](cfg-smime-is-default) is _set_, then OpenSSL is used instead to create S/MIME messages and settings can be overridden by use of the smime menu instead of the pgp menu.

--------------------------------------------------------------------------------

(cfg-crypt-auto-smime)=
## `$crypt_auto_smime`

:Description: Allow automatic SMIME functions
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set crypt_auto_smime = yes
    ```

This variable controls whether or not NeoMutt may automatically enable S/MIME encryption/signing for messages.

:::{seealso}
[`$crypt_auto_encrypt`](cfg-crypt-auto-encrypt), [`$crypt_reply_encrypt`](cfg-crypt-reply-encrypt), [`$crypt_auto_sign`](cfg-crypt-auto-sign), [`$crypt_reply_sign`](cfg-crypt-reply-sign), [`$smime_is_default`](cfg-smime-is-default)
:::

--------------------------------------------------------------------------------

(cfg-crypt-reply-encrypt)=
## `$crypt_reply_encrypt`

:Description: Encrypt replies to encrypted messages
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_reply_encrypt = yes
    ```

If _set_, automatically PGP or OpenSSL encrypt replies to messages which are encrypted.

--------------------------------------------------------------------------------

(cfg-crypt-reply-sign)=
## `$crypt_reply_sign`

:Description: Sign replies to signed messages
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_reply_sign = no
    ```

If _set_, automatically PGP or OpenSSL sign replies to messages which are signed.

:::{note}
this does not work on messages that are encrypted _and_ signed!
:::

--------------------------------------------------------------------------------

(cfg-crypt-reply-sign-encrypted)=
## `$crypt_reply_sign_encrypted`

:Description: Sign replies to encrypted messages
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set crypt_reply_sign_encrypted = no
    ```

If _set_, automatically PGP or OpenSSL sign replies to messages which are encrypted.
This makes sense in combination with [`$crypt_reply_encrypt`](cfg-crypt-reply-encrypt), because it allows you to sign all messages which are automatically encrypted.
This works around the problem noted in [`$crypt_reply_sign`](cfg-crypt-reply-sign), that NeoMutt is not able to find out whether an encrypted message is also signed.

--------------------------------------------------------------------------------

(cfg-dsn-notify)=
## `$dsn_notify`

:Description: Request notification for message delivery or delay
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set dsn_notify = ""
    ```

This variable sets the request for when notification is returned.
The string consists of a comma separated list (no spaces!) of one or more of the following: _never_, to never request notification, _failure_, to request notification on transmission failure, _delay_, to be notified of message delays, _success_, to be notified of successful transmission.

Example:
```neomuttrc
set dsn_notify = "failure,delay"
```

:::{note}
When using [`$sendmail`](cfg-sendmail) for delivery, you should not enable this unless you are either using Sendmail 8.8.x or greater or a MTA providing a `sendmail(1)`-compatible interface supporting the `-N` option for DSN.
For SMTP delivery, DSN support is auto-detected so that it depends on the server whether DSN will be used or not.
:::

--------------------------------------------------------------------------------

(cfg-dsn-return)=
## `$dsn_return`

:Description: What to send as a notification of message delivery or delay
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set dsn_return = ""
    ```

This variable controls how much of your message is returned in DSN messages.
It may be set to either _hdrs_ to return just the message header, or _full_ to return the full message.

Example:
```neomuttrc
set dsn_return = "hdrs"
```

:::{note}
When using [`$sendmail`](cfg-sendmail) for delivery, you should not enable this unless you are either using Sendmail 8.8.x or greater or a MTA providing a `sendmail(1)`-compatible interface supporting the `-R` option for DSN.
For SMTP delivery, DSN support is auto-detected so that it depends on the server whether DSN will be used or not.
:::

--------------------------------------------------------------------------------

(cfg-empty-subject)=
## `$empty_subject`

:Description: Subject to use when replying to an email with none
:Type: [String](type-string)
:Default:
    ```neomuttrc
    set empty_subject = "Re: your mail"
    ```

This variable specifies the subject to be used when replying to an email with an empty `Subject:`.
It defaults to "Re: your mail".

--------------------------------------------------------------------------------

(cfg-encode-from)=
## `$encode_from`

:Description: Encode `From ` as "quote-printable" at the beginning of lines
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set encode_from = no
    ```

When _set_, NeoMutt will quoted-printable encode messages when they contain the string "From " (note the trailing space) in the beginning of a line.
This is useful to avoid the tampering certain mail delivery and transport agents tend to do with messages (in order to prevent tools from misinterpreting the line as a mbox message separator).

--------------------------------------------------------------------------------

(cfg-fast-reply)=
## `$fast_reply`

:Description: Don't prompt for the recipients and subject when replying/forwarding
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set fast_reply = no
    ```

When _set_, the initial prompt for recipients (`To:`, `Cc:`, `Bcc:`) and subject are skipped when the relevant information is already provided.
These cases include replying to messages and passing the relevant command line arguments.
The initial prompt for recipients is also skipped when composing a new message to the current message sender, while the initial prompt for subject is also skipped when forwarding messages.

:::{note}
this variable has no effect when the [`$auto_edit`](cfg-auto-edit) variable is _set_.
:::

:::{seealso}
[`$auto_edit`](cfg-auto-edit), [`$edit_headers`](cfg-edit-headers), [`$ask_cc`](cfg-ask-cc), [`$ask_bcc`](cfg-ask-bcc)
:::

--------------------------------------------------------------------------------

(cfg-fcc-attach)=
## `$fcc_attach`

:Description: Save sent message with all their attachments
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set fcc_attach = yes
    ```

This variable controls whether or not attachments on outgoing messages are saved along with the main body of your message.

:::{note}
[`$fcc_before_send`](cfg-fcc-before-send) forces the default (set) behavior of this option.
:::

--------------------------------------------------------------------------------

(cfg-fcc-before-send)=
## `$fcc_before_send`

:Description: Save FCCs before sending the message
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set fcc_before_send = no
    ```

When this variable is _set_, FCCs will occur before sending the message.
Before sending, the message cannot be manipulated, so it will be stored the exact same as sent:
[`$fcc_attach`](cfg-fcc-attach) and [`$fcc_clear`](cfg-fcc-clear) will be ignored (using their default values).

When _unset_, the default, FCCs will occur after sending.
Variables [`$fcc_attach`](cfg-fcc-attach) and [`$fcc_clear`](cfg-fcc-clear) will be respected, allowing it to be stored without attachments or encryption/signing if desired.

--------------------------------------------------------------------------------

(cfg-fcc-clear)=
## `$fcc_clear`

:Description: Save sent messages unencrypted and unsigned
:Type: [Boolean](type-bool)
:Scope: PGP only
:Default:
    ```neomuttrc
    set fcc_clear = no
    ```

When this variable is _set_, FCCs will be stored unencrypted and unsigned, even when the actual message is encrypted and/or signed.

:::{note}
[`$fcc_before_send`](cfg-fcc-before-send) forces the default (unset) behavior of this option.
:::

:::{seealso}
[`$pgp_self_encrypt`](cfg-pgp-self-encrypt), [`$smime_self_encrypt`](cfg-smime-self-encrypt)
:::

--------------------------------------------------------------------------------

(cfg-followup-to)=
## `$followup_to`

:Description: Add the `Mail-Followup-To` header is generated when sending mail
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set followup_to = yes
    ```

Controls whether or not the `Mail-Followup-To:` header field is generated when sending mail.
When _set_, NeoMutt will generate this field when you are replying to a known mailing list, specified with the [`:subscribe`](cmd-subscribe) or [`:lists`](cmd-lists) commands.

This field has two purposes.
First, preventing you from receiving duplicate copies of replies to messages which you send to mailing lists, and second, ensuring that you do get a reply separately for any messages sent to known lists to which you are not subscribed.

The header will contain only the list's address for subscribed lists, and both the list address and your own email address for unsubscribed lists.
Without this header, a group reply to your message sent to a subscribed list will be sent to both the list and your address, resulting in two copies of the same email for you.

--------------------------------------------------------------------------------

(cfg-forward-attachments)=
## `$forward_attachments`

:Description: Forward attachments when forwarding a message
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set forward_attachments = ask-yes
    ```

When forwarding inline (i.e.
[`$mime_forward`](cfg-mime-forward) _unset_ or answered with "no" and [`$forward_decode`](cfg-forward-decode) _set_), attachments which cannot be decoded in a reasonable manner will be attached to the newly composed message if this quadoption is _set_ or answered with "yes".

--------------------------------------------------------------------------------

(cfg-forward-attribution-intro)=
## `$forward_attribution_intro`

:Description: Prefix message for forwarded messages
:Type: [Expando](type-expando)
:Notes: [Localised String](type-general), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set forward_attribution_intro = "----- Forwarded message from %f -----"
    ```
:Alternative:
    ```neomuttrc
    set forward_attribution_intro = "----- Forwarded message from %{from-full} -----"
    ```

This is the string that will precede a message which has been forwarded in the main body of a message (when [`$mime_forward`](cfg-mime-forward) is unset).

:::{seealso}
- {doc}`/howto/email-template`
- [`$index_format`](cfg-index-format) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
- [`$attribution_locale`](cfg-attribution-locale)
:::

--------------------------------------------------------------------------------

(cfg-forward-attribution-trailer)=
## `$forward_attribution_trailer`

:Description: Suffix message for forwarded messages
:Type: [Expando](type-expando)
:Notes: [Localised String](type-general), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set forward_attribution_trailer = "----- End forwarded message -----"
    ```

This is the string that will follow a message which has been forwarded in the main body of a message (when [`$mime_forward`](cfg-mime-forward) is unset).

:::{seealso}
- {doc}`/howto/email-template`
- [`$index_format`](cfg-index-format) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
- [`$attribution_locale`](cfg-attribution-locale)
:::

--------------------------------------------------------------------------------

(cfg-forward-decrypt)=
## `$forward_decrypt`

:Description: Decrypt the message when forwarding it
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set forward_decrypt = yes
    ```

Controls the handling of encrypted messages when forwarding a message.
When _set_, the outer layer of encryption is stripped off.
This variable is only used if [`$mime_forward`](cfg-mime-forward) is _set_ and [`$mime_forward_decode`](cfg-mime-forward-decode) is _unset_.

--------------------------------------------------------------------------------

(cfg-forward-edit)=
## `$forward_edit`

:Description: Automatically start the editor when forwarding a message
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set forward_edit = yes
    ```

This quadoption controls whether or not the user is automatically placed in the editor when forwarding messages.
For those who always want to forward with no modification, use a setting of "no".

--------------------------------------------------------------------------------

(cfg-forward-format)=
## `$forward_format`

:Description: Format string to control the subject when forwarding a message
:Type: [Expando](type-expando)
:Notes: [Not Empty](type-general), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set forward_format = "[%a: %s]"
    ```
:Alternative:
    ```neomuttrc
    set forward_format = "[%{from}: %{subject}]"
    ```

This variable controls the default subject when forwarding a message.

:::{seealso}
- {doc}`/howto/email-template`
- [`$index_format`](cfg-index-format) for a full list of expandos
- **Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-forward-references)=
## `$forward_references`

:Description: Set the `In-Reply-To` and `References` headers when forwarding a message
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set forward_references = no
    ```

When _set_, forwarded messages set the `In-Reply-To:` and `References:` headers in the same way as normal replies would.
Hence the forwarded message becomes part of the original thread instead of starting a new one.

--------------------------------------------------------------------------------

(cfg-greeting)=
## `$greeting`

:Description: Greeting string added to the top of all messages
:Type: [Expando](type-expando)
:Notes: [Pipe Support](type-pipe)
:Default: (empty)
    ```neomuttrc
    set greeting = ""
    ```

Specify the format of the greeting string.
This string is added to the top of every outgoing message.

**Format Sequences**

| Short | Long Name       | Description                    |
|-------|-----------------|--------------------------------|
| `%n`  | `%{real-name}`  | Recipient's real name          |
| `%u`  | `%{user-name}`  | User (login) name of recipient |
| `%v`  | `%{first-name}` | First name of recipient        |

:::{seealso}
- {doc}`/howto/email-template`
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-hdrs)=
## `$hdrs`

:Description: Add custom headers to outgoing mail
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set hdrs = yes
    ```

When _unset_, the header fields normally added by the [`:my-header`](cmd-my-header) command are not created.
This variable _must_ be unset before composing a new message or replying in order to take effect.
If _set_, the user defined header fields are added to every new message.

--------------------------------------------------------------------------------

(cfg-hidden-host)=
## `$hidden_host`

:Description: Don't use the hostname, just the domain, when generating the message id
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set hidden_host = no
    ```

When _set_, NeoMutt will skip the host name part of [`$hostname`](cfg-hostname) variable when adding the domain part to addresses.

--------------------------------------------------------------------------------

(cfg-honor-followup-to)=
## `$honor_followup_to`

:Description: Honour the `Mail-Followup-To` header when group replying
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set honor_followup_to = yes
    ```

This variable controls whether or not a `Mail-Followup-To:` header is honored when group-replying to a message.

--------------------------------------------------------------------------------

(cfg-ignore-list-reply-to)=
## `$ignore_list_reply_to`

:Description: Ignore the `Reply-To` header when using `<reply>` on a mailing list
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set ignore_list_reply_to = no
    ```

Affects the behavior of the [`<reply>`](ref-fn-attach) function when replying to messages from mailing lists (as defined by the [`:subscribe`](cmd-subscribe) or [`:lists`](cmd-lists) commands).  
When _set_, if the `Reply-To:` field is set to the same value as the `To:` field, NeoMutt assumes that the `Reply-To:` field was set by the mailing list to automate responses to the list, and will ignore this field.
To direct a response to the mailing list when this option is _set_, use the [`<list-reply>`](ref-fn-attach) function; [`<group-reply>`](ref-fn-attach) will reply to both the sender and the list.

--------------------------------------------------------------------------------

(cfg-include)=
## `$include`

:Description: Include a copy of the email that's being replied to
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set include = ask-yes
    ```

Controls whether or not a copy of the message(s) you are replying to is included in your reply.

--------------------------------------------------------------------------------

(cfg-inews-command)=
## `$inews_command`

:Description: External command to post news articles
:Type: [Expando (Command String)](type-expando)
:Notes: [Pipe Support](type-pipe)
:Default: (empty)
    ```neomuttrc
    set inews_command = ""
    ```

Specify the format of a command used to deliver news posts.
If _unset_, NeoMutt posts article using current connection to news server.

**Format Sequences**

| Short | Description       |
|-------|-------------------|
| `%a`  | account url       |
| `%p`  | port              |
| `%P`  | port if specified |
| `%s`  | news server name  |
| `%S`  | url schema        |
| `%u`  | username          |

Example:
```neomuttrc
set inews_command = "/usr/local/bin/inews -hS"
```

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)
:::

--------------------------------------------------------------------------------

(cfg-message-id-format)=
## `$message_id_format`

:Description: Format string for customising the `Message-ID`
:Type: [Expando](type-expando)
:Notes: [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set message_id_format = "<%z@%f>"
    ```
:Alternative:
    ```neomuttrc
    set message_id_format = "<%{random_12}@%{hostname}>"
    ```

Specify the format of the `Message-ID:` email header.

Please note that the Message-ID value follows a strict syntax, and you are responsible for ensuring correctness if you change this from the default.
In particular, the value must follow the syntax in RFC 5322: `"<" id-left "@" id-right ">"`.
No spaces are allowed, and `id-left` should follow the dot-atom-text syntax in the RFC.
The `id-right` should generally be left as `%f`.

If unset, NeoMutt will use a long random format.

If the format doesn't begin/end with `<`, `>` they will be added.

The old Message-ID format can be used by setting this to: `<%Y%02m%02d%02H%02M%02S.G%c%p@%f>`

**Format Sequences**

| Short | Long Name      | Description                                                        |
|-------|----------------|--------------------------------------------------------------------|
| %c    | `%{counter}`   | Step counter looping from `A` to `Z`                               |
| %d    | `%{day}`       | Current day of the month (GMT)                                     |
| %f    | `%{hostname}`  | [`$hostname`](cfg-hostname)                                        |
| %H    | `%{hour}`      | Current hour using a 24-hour clock (GMT)                           |
| %m    | `%{minute}`    | Current month number (GMT)                                         |
| %M    | `%{month}`     | Current minute of the hour (GMT)                                   |
| %p    | `%{pid}`       | Pid of the running neomutt process                                 |
| %r    | `%{random_3}`  | 3 bytes of pseudo-random data encoded in Base64                    |
| %S    | `%{second}`    | Current second of the minute (GMT)                                 |
| %x    | `%{random_1}`  | 1 byte of pseudo-random data hex encoded (example: `1b`)           |
| %Y    | `%{year}`      | Current year using 4 digits (GMT)                                  |
| %z    | `%{random_12}` | 4 byte timestamp + 8 bytes of pseudo-random data encoded in Base64 |

:::{seealso}
**Expandos:** [Tutorial Conditional](tut-cond-expando), [Howto Conditional](how-cond-expando), [Formatting](how-format-expando), [Reference](ref-expandos)

Base64Url: <https://datatracker.ietf.org/doc/html/rfc4648#section-5>
:::

--------------------------------------------------------------------------------

(cfg-me-too)=
## `$me_too`

:Description: Remove the user's address from the list of recipients
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set me_too = no
    ```

If _unset_, NeoMutt will remove your address (see the [`:alternates`](cmd-alternates) command) from the list of recipients when replying to a message.

--------------------------------------------------------------------------------

(cfg-mime-forward-decode)=
## `$mime_forward_decode`

:Description: Decode the forwarded message before attaching it
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set mime_forward_decode = no
    ```

Controls the decoding of complex MIME messages into `text/plain` when forwarding a message while [`$mime_forward`](cfg-mime-forward) is _set_.
Otherwise [`$forward_decode`](cfg-forward-decode) is used instead.

--------------------------------------------------------------------------------

(cfg-mime-type-query-command)=
## `$mime_type_query_command`

:Description: External command to determine the MIME type of an attachment
:Type: [Command (String)](type-string)
:Default: (empty)
    ```neomuttrc
    set mime_type_query_command = ""
    ```

This specifies a command to run, to determine the mime type of a new attachment when composing a message.
Unless [`$mime_type_query_first`](cfg-mime-type-query-first) is set, this will only be run if the attachment's extension is not found in the mime.types file.

The string may contain a `%s`, which will be substituted with the attachment filename.
NeoMutt will add quotes around the string substituted for `%s` automatically according to shell quoting rules, so you should avoid adding your own.
If no `%s` is found in the string, NeoMutt will append the attachment filename to the end of the string.

The command should output a single line containing the attachment's mime type.

Suggested values are `xdg-mime query filetype` or `file -bi`.

--------------------------------------------------------------------------------

(cfg-mime-type-query-first)=
## `$mime_type_query_first`

:Description: Run the [`$mime_type_query_command`](cfg-mime-type-query-command) before the mime.types lookup
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set mime_type_query_first = no
    ```

When _set_, the [`$mime_type_query_command`](cfg-mime-type-query-command) will be run before the mime.types lookup.

--------------------------------------------------------------------------------

(cfg-nm-record)=
## `$nm_record`

:Description: If the [`$record`](cfg-record) mailbox (sent mail) should be indexed
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set nm_record = no
    ```

This variable specifies whether, when writing a just-sent message to the [`$record`](cfg-record), the message should also be added to the notmuch DB.
Replies inherit the notmuch tags from the original message.
See [`$nm_record_tags`](cfg-nm-record-tags) for how to modify the set of notmuch tags assigned to sent messages written to the record.

--------------------------------------------------------------------------------

(cfg-pgp-reply-inline)=
## `$pgp_reply_inline`

:Description: Reply using old-style inline PGP messages (not recommended)
:Type: [Boolean](type-bool)
:Scope: PGP only
:Default:
    ```neomuttrc
    set pgp_reply_inline = no
    ```

Setting this variable will cause NeoMutt to always attempt to create an inline (traditional) message when replying to a message which is PGP encrypted/signed inline.
This can be overridden by use of the pgp menu, when inline is not required.
This option does not automatically detect if the (replied-to) message is inline; instead it relies on NeoMutt internals for previously checked/flagged messages.

Note that NeoMutt might automatically use PGP/MIME for messages which consist of more than a single MIME part.
NeoMutt can be configured to ask before sending PGP/MIME messages when inline (traditional) would not work.

Also see the [`$pgp_mime_auto`](cfg-pgp-mime-auto) variable.

Also note that using the old-style PGP message format is **strongly** **deprecated**.

--------------------------------------------------------------------------------

(cfg-postpone-encrypt)=
## `$postpone_encrypt`

:Description: Self-encrypt postponed messages
:Type: [Boolean](type-bool)
:Scope: Crypto only
:Default:
    ```neomuttrc
    set postpone_encrypt = no
    ```

When _set_, postponed messages that are marked for encryption will be self-encrypted.
NeoMutt will first try to encrypt using the value specified in [`$pgp_default_key`](cfg-pgp-default-key) or [`$smime_default_key`](cfg-smime-default-key).

--------------------------------------------------------------------------------

(cfg-postpone-encrypt-as)=
## `$postpone_encrypt_as`

:Description: Fallback encryption key for postponed messages
:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set postpone_encrypt_as = ""
    ```

When _set_, NeoMutt will use this as a fallback encryption key for postponed messages.

--------------------------------------------------------------------------------

(cfg-recall)=
## `$recall`

:Description: Recall postponed mesaages when asked to compose a message
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set recall = ask-yes
    ```

Controls whether or not NeoMutt recalls postponed messages when composing a new message.

Setting this variable to _yes_ is not generally useful, and thus not recommended.
Note that the [`<recall-message>`](ref-fn-index) function can be used to manually recall postponed messages.

Also see [`$postponed`](cfg-postponed) variable.

--------------------------------------------------------------------------------

(cfg-reply-self)=
## `$reply_self`

:Description: Really reply to yourself, when replying to your own email
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set reply_self = no
    ```

If _unset_ and you are replying to a message sent by you, NeoMutt will assume that you want to reply to the recipients of that message rather than to yourself.

Also see the [`:alternates`](cmd-alternates) command.

--------------------------------------------------------------------------------

(cfg-reply-to)=
## `$reply_to`

:Description: Address to use as a `Reply-To` header
:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set reply_to = ask-yes
    ```

If _set_, when replying to a message, NeoMutt will use the address listed in the Reply-to: header as the recipient of the reply.
If _unset_, it will use the address in the From: header field instead.
This option is useful for reading a mailing list that sets the Reply-To:
header field to the list address and you want to send a private message to the author of a message.

--------------------------------------------------------------------------------

(cfg-reply-with-xorig)=
## `$reply_with_xorig`

:Description: Create `From` header from `X-Original-To` header
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set reply_with_xorig = no
    ```

This variable provides a toggle.
When active, the From: header will be extracted from the current mail's 'X-Original-To:' header.
This setting does not have precedence over [`$reverse_real_name`](cfg-reverse-real-name).

Assuming [`$fast_reply`](cfg-fast-reply) is disabled, this option will prompt the user with a prefilled From: header.

--------------------------------------------------------------------------------

(cfg-resume-draft-files)=
## `$resume_draft_files`

:Description: Process draft files like postponed messages
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set resume_draft_files = no
    ```

If _set_, draft files (specified by `-H` on the command line) are processed similarly to when resuming a postponed message.
Recipients are not prompted for; send-hooks are not evaluated; no alias expansion takes place; user-defined headers and signatures are not added to the message.

--------------------------------------------------------------------------------

(cfg-reverse-name)=
## `$reverse_name`

:Description: Set the `From` from the address the email was sent to
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set reverse_name = no
    ```

It may sometimes arrive that you receive mail to a certain machine, move the messages to another machine, and reply to some the messages from there.
If this variable is _set_, the default `From:` line of the reply messages is built using the address where you received the messages you are replying to **if** that address matches your [`:alternates`](cmd-alternates).  
If the variable is _unset_, or the address that would be used doesn't match your [`:alternates`](cmd-alternates), the `From:` line will use your address on the current machine.

Also see the [`:alternates`](cmd-alternates) command and [`$reverse_real_name`](cfg-reverse-real-name).

--------------------------------------------------------------------------------

(cfg-reverse-real-name)=
## `$reverse_real_name`

:Description: Set the `From` from the full `To` address the email was sent to
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set reverse_real_name = yes
    ```

This variable fine-tunes the behavior of the [`$reverse_name`](cfg-reverse-name) feature.

When it is _unset_, NeoMutt will remove the real name part of a matching address.
This allows the use of the email address without having to also use what the sender put in the real name field.

When it is _set_, NeoMutt will use the matching address as-is.

In either case, a missing real name will be filled in afterwards using the value of [`$real_name`](cfg-real-name).

--------------------------------------------------------------------------------

(cfg-sendmail)=
## `$sendmail`

:Description: External command to send email
:Type: [Command (String)](type-string)
:Default:
    ```neomuttrc
    set sendmail = SENDMAIL " -oem -oi"
    ```

Specifies the program and arguments used to deliver mail sent by NeoMutt.
NeoMutt expects that the specified program interprets additional arguments as recipient addresses.
NeoMutt appends all recipients after adding a `--` delimiter (if not already present).  
Additional flags, such as for [`$use_8bit_mime`](cfg-use-8bit-mime), [`$use_envelope_from`](cfg-use-envelope-from), [`$dsn_notify`](cfg-dsn-notify), or [`$dsn_return`](cfg-dsn-return) will be added before the delimiter.

:::{note}
This command is invoked differently from most other commands in NeoMutt.
It is tokenized by space, and invoked directly via `execvp(3)` with an array of arguments - so commands or arguments with spaces in them are not supported.
The shell is not used to run the command, so shell quoting is also not supported.
:::

:::{seealso}
[`$write_bcc`](cfg-write-bcc)
:::

--------------------------------------------------------------------------------

(cfg-sendmail-wait)=
## `$sendmail_wait`

:Description: Time to wait for sendmail to finish
:Type: [Number](type-number)
:Default:
    ```neomuttrc
    set sendmail_wait = 0
    ```

Specifies the number of seconds to wait for the [`$sendmail`](cfg-sendmail) process to finish before giving up and putting delivery in the background.

NeoMutt interprets the value of this variable as follows:

| Value | Description                                                        |
|-------|--------------------------------------------------------------------|
| >0    | number of seconds to wait for sendmail to finish before continuing |
| 0     | wait forever for sendmail to finish                                |
| <0    | always put sendmail in the background without waiting              |

Note that if you specify a value other than 0, the output of the child process will be put in a temporary file.
If there is some error, you will be informed as to where to find the output.

--------------------------------------------------------------------------------

(cfg-signature)=
## `$signature`

:Description: File containing a signature to append to all mail
:Type: [Path (String)](type-path)
:Notes: [File only](type-path), [Pipe Support](type-pipe)
:Default:
    ```neomuttrc
    set signature = "~/.signature"
    ```

Specifies the filename of your signature, which is appended to all outgoing messages.

:::{seealso}
- {doc}`/howto/email-template`
:::

--------------------------------------------------------------------------------

(cfg-sig-dashes)=
## `$sig_dashes`

:Description: Insert `-- ` before the signature
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set sig_dashes = yes
    ```

If _set_, a line containing `-- ` (note the trailing space) will be inserted before your [`$signature`](cfg-signature).
It is **strongly** recommended that you not _unset_ this variable unless your signature contains just your name.
The reason for this is because many software packages use `-- \n` to detect your signature.
For example, NeoMutt has the ability to highlight the signature in a different color in the built-in pager.

:::{seealso}
- {doc}`/howto/email-template`
:::

--------------------------------------------------------------------------------

(cfg-sig-on-top)=
## `$sig_on_top`

:Description: Insert the signature before the quoted text
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set sig_on_top = no
    ```

If _set_, the signature will be included before any quoted or forwarded text.

:::{warning}
Do not set this variable unless you really know what you are doing, and are prepared to take some heat from netiquette guardians.
:::

:::{seealso}
- {doc}`/howto/email-template`
:::

--------------------------------------------------------------------------------

(cfg-smtp-authenticators)=
## `$smtp_authenticators`

:Description: List of allowed authentication methods (colon-separated)
:Type: [String List](type-slist)
:Notes: [Colon-separated](type-slist)
:Default: (empty)
    ```neomuttrc
    set smtp_authenticators = ""
    ```

This is a colon-separated list of authentication methods NeoMutt may attempt to use to log in to an SMTP server, in the order NeoMutt should try them.
Authentication methods are any SASL mechanism, e.g. `plain`, `digest-md5`, `gssapi` or `cram-md5`.
This option is case-insensitive.
If it is unset (the default) NeoMutt will try all available methods, in order from most-secure to least-secure.
Support for the `plain` mechanism is bundled; other mechanisms are provided by an external SASL library (look for '+sasl' in the output of `neomutt -v`).

Example:

```neomuttrc
set smtp_authenticators = "digest-md5:cram-md5"
```

--------------------------------------------------------------------------------

(cfg-smtp-oauth-refresh-command)=
## `$smtp_oauth_refresh_command`

:Description: External command to generate OAUTH refresh token
:Type: [Command (String)](type-string)
:Notes: [Sensitive](type-general)
:Default: (empty)
    ```neomuttrc
    set smtp_oauth_refresh_command = ""
    ```

The command to run to generate an OAUTH refresh token for authorizing your connection to your SMTP server.
This command will be run on every connection attempt that uses the OAUTHBEARER or XOAUTH2 authentication mechanisms.
See "$oauth" for details.

--------------------------------------------------------------------------------

(cfg-smtp-pass)=
## `$smtp_pass`

:Description: Password for the SMTP server
:Type: [String](type-string)
:Notes: [Sensitive](type-general)
:Default: (empty)
    ```neomuttrc
    set smtp_pass = ""
    ```

Specifies the password for your SMTP account.
If _unset_, NeoMutt will prompt you for your password when you first send mail via SMTP.
See [`$smtp_url`](cfg-smtp-url) to configure NeoMutt to send mail via SMTP.

:::{warning}
Only use this option when you are on a fairly secure machine, because the superuser can read your neomuttrc even if you are the only one who can read the file.
:::

--------------------------------------------------------------------------------

(cfg-smtp-url)=
## `$smtp_url`

:Description: URL of the SMTP server
:Type: [String](type-string)
:Notes: [Sensitive](type-general)
:Default: (empty)
    ```neomuttrc
    set smtp_url = ""
    ```

Defines the SMTP smarthost where sent messages should relayed for delivery.
This should take the form of an SMTP URL, e.g.:

```
smtp[s]://[user[:pass]@]host[:port]
```

where "[...]" denotes an optional part.
Setting this variable overrides the value of the [`$sendmail`](cfg-sendmail) variable.

Also see [`$write_bcc`](cfg-write-bcc).

--------------------------------------------------------------------------------

(cfg-smtp-user)=
## `$smtp_user`

:Description: Username for the SMTP server
:Type: [String](type-string)
:Notes: [Sensitive](type-general)
:Default: (empty)
    ```neomuttrc
    set smtp_user = ""
    ```

The username for the SMTP server.

This variable defaults to your user name on the local machine.

--------------------------------------------------------------------------------

(cfg-user-agent)=
## `$user_agent`

:Description: Add a `User-Agent` header to outgoing mail
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set user_agent = no
    ```

When _set_, NeoMutt will add a `User-Agent:` header to outgoing messages, indicating which version of NeoMutt was used for composing them.

--------------------------------------------------------------------------------

(cfg-use-8bit-mime)=
## `$use_8bit_mime`

:Description: Use 8-bit messages and ESMTP to send messages
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set use_8bit_mime = no
    ```

:::{warning}
Do not set this variable unless you are using a version of sendmail which supports the `-B8BITMIME` flag (such as sendmail 8.8.x) or you may not be able to send mail.
:::

When _set_, NeoMutt will invoke [`$sendmail`](cfg-sendmail) with the `-B8BITMIME`
flag when sending 8-bit messages to enable ESMTP negotiation.

--------------------------------------------------------------------------------

(cfg-use-envelope-from)=
## `$use_envelope_from`

:Description: Set the envelope sender of the message
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set use_envelope_from = no
    ```

When _set_, NeoMutt will set the _envelope_ sender of the message.
If [`$envelope_from_address`](cfg-envelope-from-address) is _set_, it will be used as the sender address.
If _unset_, NeoMutt will attempt to derive the sender from the `From:` header.

Note that this information is passed to sendmail command using the `-f` command line switch.
Therefore setting this option is not useful if the [`$sendmail`](cfg-sendmail) variable already contains `-f` or if the executable pointed to by [`$sendmail`](cfg-sendmail) doesn't support the `-f` switch.

--------------------------------------------------------------------------------

(cfg-use-from)=
## `$use_from`

:Description: Set the `From` header for outgoing mail
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set use_from = yes
    ```

When _set_, NeoMutt will generate the `From:` header field when sending messages.
If _unset_, no `From:` header field will be generated unless the user explicitly sets one using the [`:my-header`](cmd-my-header) command.

--------------------------------------------------------------------------------

(cfg-wrap-headers)=
## `$wrap_headers`

:Description: Width to wrap headers in outgoing messages
:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set wrap_headers = 78
    ```

This option specifies the number of characters to use for wrapping an outgoing message's headers.
Allowed values are between 78 and 998 inclusive.

:::{warning}
This option usually shouldn't be changed.
[RFC5233](https://www.rfc-editor.org/rfc/rfc5233.html) recommends a line length of 78 (the default), so **please only change this setting when you know what you're doing**.
:::

--------------------------------------------------------------------------------

(cfg-write-bcc)=
## `$write_bcc`

:Description: Write out the `Bcc:` field when preparing to send a mail
:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set write_bcc = no
    ```

Controls whether NeoMutt writes out the `Bcc:` header when preparing messages to be sent.
Some MTAs, such as Exim and Courier, do not strip the `Bcc:` header; so it is advisable to leave this unset unless you have a particular need for the header to be in the sent message.

If NeoMutt is set to deliver directly via SMTP(see [`$smtp_url`](cfg-smtp-url)), this option does nothing: NeoMutt will never write out the `Bcc:` header in this case.

Note this option only affects the sending of messages.
Fcc'ed copies of a message will always contain the `Bcc:` header if one exists.

