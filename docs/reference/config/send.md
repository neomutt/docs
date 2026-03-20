---
title: Send Options
description: Send protocol configuration variables for NeoMutt
keywords: pop_auth_try_all, pop_authenticators, pop_check_interval, pop_delete, pop_host, pop_last, pop_oauth_refresh_command, pop_pass, pop_reconnect, pop_user
---

# Send Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

--------------------------------------------------------------------------------

(abort-noattach)=
## `$abort_noattach`

- **Type:** quad-option
- **Default:**
    ```
    set abort_noattach = no
    ```

If set to _yes_, when composing messages containing the regular expression specified by $$abort_noattach_regex and no attachments are given, composition will be aborted.
If set to _no_, composing messages as such will never be aborted.

Example:

```neomuttrc
set abort_noattach_regex = "\\<attach(|ed|ments?)\\>"
```

--------------------------------------------------------------------------------

(abort-noattach-regex)=
## `$abort_noattach_regex`

- **Type:** regular expression
- **Default:**
    ```
    set abort_noattach_regex = "\\<(attach|attached|attachments?)\\>"
    ```

Specifies a regular expression to match against the body of the message, to determine if an attachment was mentioned but mistakenly forgotten.
If it matches, $$abort_noattach will be consulted to determine if message sending will be aborted.

Like other regular expressions in NeoMutt, the search is case sensitive if the pattern contains at least one upper case letter, and case insensitive otherwise.

--------------------------------------------------------------------------------

(abort-nosubject)=
## `$abort_nosubject`

- **Type:** quad-option
- **Default:**
    ```
    set abort_nosubject = ask-yes
    ```

If set to _yes_, when composing messages and no subject is given at the subject prompt, composition will be aborted.
If set to _no_, composing messages with no subject given at the subject prompt will never be aborted.

--------------------------------------------------------------------------------

(abort-unmodified)=
## `$abort_unmodified`

- **Type:** quad-option
- **Default:**
    ```
    set abort_unmodified = yes
    ```

If set to _yes_, composition will automatically abort after editing the message body if no changes are made to the file (this check only happens after the _first_ edit of the file).
When set to _no_, composition will never be aborted.

--------------------------------------------------------------------------------

(allow-8bit)=
## `$allow_8bit`

- **Type:** boolean
- **Default:**
    ```
    set allow_8bit = yes
    ```

Controls whether 8-bit data is converted to 7-bit using either Quoted-Printable or Base64 encoding when sending mail.

--------------------------------------------------------------------------------

(ask-bcc)=
## `$ask_bcc`

- **Type:** boolean
- **Default:**
    ```
    set ask_bcc = no
    ```

If _set_, NeoMutt will prompt you for blind-carbon-copy (Bcc) recipients before editing an outgoing message.

--------------------------------------------------------------------------------

(ask-cc)=
## `$ask_cc`

- **Type:** boolean
- **Default:**
    ```
    set ask_cc = no
    ```

If _set_, NeoMutt will prompt you for carbon-copy (Cc) recipients before editing the body of an outgoing message.

--------------------------------------------------------------------------------

(ask-followup-to)=
## `$ask_followup_to`

- **Type:** boolean
- **Default:**
    ```
    set ask_followup_to = no
    ```

If set, NeoMutt will prompt you for follow-up groups before editing the body of an outgoing message.

--------------------------------------------------------------------------------

(ask-x-comment-to)=
## `$ask_x_comment_to`

- **Type:** boolean
- **Default:**
    ```
    set ask_x_comment_to = no
    ```

If set, NeoMutt will prompt you for x-comment-to field before editing the body of an outgoing message.

--------------------------------------------------------------------------------

(attach-charset)=
## `$attach_charset`

- **Type:** string list
- **Default:** (empty)
    ```
    set attach_charset = ""
    ```

This variable is a colon-separated list of character encoding schemes for text file attachments.
NeoMutt uses this setting to guess which encoding files being attached are encoded in to convert them to a proper character set given in $$send_charset.

If _unset_, the value of $$charset will be used instead.

For example, the following configuration would work for Japanese text handling:
```
set attach_charset="iso-2022-jp:euc-jp:shift_jis:utf-8" 
```

Note: for Japanese users, "iso-2022-*" must be put at the head of the value as shown above if included.

--------------------------------------------------------------------------------

(attribution-intro)=
## `$attribution_intro`

- **Type:** expando
- **Default:**
    ```
    set attribution_intro = "On %d, %n wrote:"
    ```

This is the string that will precede a replied-to message which is quoted in the main body of the reply (this is the case when $$include is set).

For a full listing of defined `printf(3)`-like sequences see the section on $$index_format.
See also $$attribution_locale.

--------------------------------------------------------------------------------

(attribution-locale)=
## `$attribution_locale`

- **Type:** string
- **Default:** (empty)
    ```
    set attribution_locale = ""
    ```

The locale used by `strftime(3)` to format dates in the attribution strings.
Valid values are the strings your system accepts for the locale environment variable `$$$LC_TIME`.

This variable is to allow the attribution date format to be customized by recipient or folder using hooks.
By default, NeoMutt will use your locale environment, so there is no need to set this except to override that default.

Affected variables are: $$attribution_intro, $$attribution_trailer, $$forward_attribution_intro, $$forward_attribution_trailer, $$indent_string.

--------------------------------------------------------------------------------

(attribution-trailer)=
## `$attribution_trailer`

- **Type:** expando
- **Default:** (empty)
    ```
    set attribution_trailer = ""
    ```

Similar to the $$attribution_intro variable, this is the string that will come after a replied-to message which is quoted in the main body of the reply (this is the case when $$include is set).

For a full listing of defined `printf(3)`-like sequences see the section on $$index_format.
See also $$attribution_locale.

--------------------------------------------------------------------------------

(bounce-delivered)=
## `$bounce_delivered`

- **Type:** boolean
- **Default:**
    ```
    set bounce_delivered = yes
    ```

When this variable is _set_, NeoMutt will include Delivered-To headers when bouncing messages.
Postfix users may wish to _unset_ this variable.

--------------------------------------------------------------------------------

(confirm-empty-to)=
## `$confirm_empty_to`

- **Type:** boolean
- **Default:**
    ```
    set confirm_empty_to = no
    ```

When _set_, NeoMutt will prompt for confirmation when sending an e-mail with an empty To recipients list.

--------------------------------------------------------------------------------

(content-type)=
## `$content_type`

- **Type:** string
- **Default:**
    ```
    set content_type = "text/plain"
    ```

Sets the default Content-Type for the body of newly composed messages.

--------------------------------------------------------------------------------

(crypt-auto-encrypt)=
## `$crypt_auto_encrypt`

- **Type:** boolean
- **Default:**
    ```
    set crypt_auto_encrypt = no
    ```
- **Scope:** Crypto only

Setting this variable will cause NeoMutt to always attempt to PGP encrypt outgoing messages.
This is probably only useful in connection to the "$send-hook" command.
It can be overridden by use of the pgp menu, when encryption is not required or signing is requested as well.
If $$smime_is_default is _set_, then OpenSSL is used instead to create S/MIME messages and settings can be overridden by use of the smime menu instead.

--------------------------------------------------------------------------------

(crypt-auto-pgp)=
## `$crypt_auto_pgp`

- **Type:** boolean
- **Default:**
    ```
    set crypt_auto_pgp = yes
    ```

This variable controls whether or not NeoMutt may automatically enable PGP encryption/signing for messages.
See also $$crypt_auto_encrypt, $$crypt_reply_encrypt, $$crypt_auto_sign, $$crypt_reply_sign and $$smime_is_default.

--------------------------------------------------------------------------------

(crypt-auto-sign)=
## `$crypt_auto_sign`

- **Type:** boolean
- **Default:**
    ```
    set crypt_auto_sign = no
    ```
- **Scope:** Crypto only

Setting this variable will cause NeoMutt to always attempt to cryptographically sign outgoing messages.
This can be overridden by use of the pgp menu, when signing is not required or encryption is requested as well.
If $$smime_is_default is _set_, then OpenSSL is used instead to create S/MIME messages and settings can be overridden by use of the smime menu instead of the pgp menu.

--------------------------------------------------------------------------------

(crypt-auto-smime)=
## `$crypt_auto_smime`

- **Type:** boolean
- **Default:**
    ```
    set crypt_auto_smime = yes
    ```

This variable controls whether or not NeoMutt may automatically enable S/MIME encryption/signing for messages.
See also $$crypt_auto_encrypt, $$crypt_reply_encrypt, $$crypt_auto_sign, $$crypt_reply_sign and $$smime_is_default.

--------------------------------------------------------------------------------

(crypt-reply-encrypt)=
## `$crypt_reply_encrypt`

- **Type:** boolean
- **Default:**
    ```
    set crypt_reply_encrypt = yes
    ```
- **Scope:** Crypto only

If _set_, automatically PGP or OpenSSL encrypt replies to messages which are encrypted.

--------------------------------------------------------------------------------

(crypt-reply-sign)=
## `$crypt_reply_sign`

- **Type:** boolean
- **Default:**
    ```
    set crypt_reply_sign = no
    ```
- **Scope:** Crypto only

If _set_, automatically PGP or OpenSSL sign replies to messages which are signed.

**Note:** this does not work on messages that are encrypted _and_ signed!

--------------------------------------------------------------------------------

(crypt-reply-sign-encrypted)=
## `$crypt_reply_sign_encrypted`

- **Type:** boolean
- **Default:**
    ```
    set crypt_reply_sign_encrypted = no
    ```
- **Scope:** Crypto only

If _set_, automatically PGP or OpenSSL sign replies to messages which are encrypted.
This makes sense in combination with $$crypt_reply_encrypt, because it allows you to sign all messages which are automatically encrypted.
This works around the problem noted in $$crypt_reply_sign, that NeoMutt is not able to find out whether an encrypted message is also signed.

--------------------------------------------------------------------------------

(dsn-notify)=
## `$dsn_notify`

- **Type:** string
- **Default:** (empty)
    ```
    set dsn_notify = ""
    ```

This variable sets the request for when notification is returned.
The string consists of a comma separated list (no spaces!) of one or more of the following: _never_, to never request notification, _failure_, to request notification on transmission failure, _delay_, to be notified of message delays, _success_, to be notified of successful transmission.

Example:
```
set dsn_notify="failure,delay" 
```

**Note:** when using $$sendmail for delivery, you should not enable this unless you are either using Sendmail 8.8.x or greater or a MTA providing a `sendmail(1)`-compatible interface supporting the `-N` option for DSN.
For SMTP delivery, DSN support is auto-detected so that it depends on the server whether DSN will be used or not.

--------------------------------------------------------------------------------

(dsn-return)=
## `$dsn_return`

- **Type:** string
- **Default:** (empty)
    ```
    set dsn_return = ""
    ```

This variable controls how much of your message is returned in DSN messages.
It may be set to either _hdrs_ to return just the message header, or _full_ to return the full message.

Example:
```
set dsn_return=hdrs 
```

**Note:** when using $$sendmail for delivery, you should not enable this unless you are either using Sendmail 8.8.x or greater or a MTA providing a `sendmail(1)`-compatible interface supporting the `-R` option for DSN.
For SMTP delivery, DSN support is auto-detected so that it depends on the server whether DSN will be used or not.

--------------------------------------------------------------------------------

(empty-subject)=
## `$empty_subject`

- **Type:** string
- **Default:**
    ```
    set empty_subject = "Re: your mail"
    ```

This variable specifies the subject to be used when replying to an email with an empty subject.
It defaults to "Re: your mail".

--------------------------------------------------------------------------------

(encode-from)=
## `$encode_from`

- **Type:** boolean
- **Default:**
    ```
    set encode_from = no
    ```

When _set_, NeoMutt will quoted-printable encode messages when they contain the string "From " (note the trailing space) in the beginning of a line.
This is useful to avoid the tampering certain mail delivery and transport agents tend to do with messages (in order to prevent tools from misinterpreting the line as a mbox message separator).

--------------------------------------------------------------------------------

(fast-reply)=
## `$fast_reply`

- **Type:** boolean
- **Default:**
    ```
    set fast_reply = no
    ```

When _set_, the initial prompt for recipients (to, cc, bcc) and subject are skipped when the relevant information is already provided.
These cases include replying to messages and passing the relevant command line arguments.
The initial prompt for recipients is also skipped when composing a new message to the current message sender, while the initial prompt for subject is also skipped when forwarding messages.

**Note:** this variable has no effect when the $$auto_edit variable is _set_.

See also: $$auto_edit, $$edit_headers, $$ask_cc, $$ask_bcc.

--------------------------------------------------------------------------------

(fcc-attach)=
## `$fcc_attach`

- **Type:** quad-option
- **Default:**
    ```
    set fcc_attach = yes
    ```

This variable controls whether or not attachments on outgoing messages are saved along with the main body of your message.

Note: $$fcc_before_send forces the default (set) behavior of this option.

--------------------------------------------------------------------------------

(fcc-before-send)=
## `$fcc_before_send`

- **Type:** boolean
- **Default:**
    ```
    set fcc_before_send = no
    ```

When this variable is _set_, FCCs will occur before sending the message.
Before sending, the message cannot be manipulated, so it will be stored the exact same as sent:
$$fcc_attach and $$fcc_clear will be ignored (using their default values).

When _unset_, the default, FCCs will occur after sending.
Variables $$fcc_attach and $$fcc_clear will be respected, allowing it to be stored without attachments or encryption/signing if desired.

--------------------------------------------------------------------------------

(fcc-clear)=
## `$fcc_clear`

- **Type:** boolean
- **Default:**
    ```
    set fcc_clear = no
    ```
- **Scope:** PGP only

When this variable is _set_, FCCs will be stored unencrypted and unsigned, even when the actual message is encrypted and/or signed.

Note: $$fcc_before_send forces the default (unset) behavior of this option.

See also $$pgp_self_encrypt, $$smime_self_encrypt.

--------------------------------------------------------------------------------

(followup-to)=
## `$followup_to`

- **Type:** boolean
- **Default:**
    ```
    set followup_to = yes
    ```

Controls whether or not the "Mail-Followup-To:" header field is generated when sending mail.
When _set_, NeoMutt will generate this field when you are replying to a known mailing list, specified with the "$subscribe" or "$lists" commands.

This field has two purposes.
First, preventing you from receiving duplicate copies of replies to messages which you send to mailing lists, and second, ensuring that you do get a reply separately for any messages sent to known lists to which you are not subscribed.

The header will contain only the list's address for subscribed lists, and both the list address and your own email address for unsubscribed lists.
Without this header, a group reply to your message sent to a subscribed list will be sent to both the list and your address, resulting in two copies of the same email for you.

--------------------------------------------------------------------------------

(forward-attachments)=
## `$forward_attachments`

- **Type:** quad-option
- **Default:**
    ```
    set forward_attachments = ask-yes
    ```

When forwarding inline (i.e.
$$mime_forward _unset_ or answered with "no" and $$forward_decode _set_), attachments which cannot be decoded in a reasonable manner will be attached to the newly composed message if this quadoption is _set_ or answered with "yes".

--------------------------------------------------------------------------------

(forward-attribution-intro)=
## `$forward_attribution_intro`

- **Type:** expando
- **Default:**
    ```
    set forward_attribution_intro = "----- Forwarded message from %f -----"
    ```

This is the string that will precede a message which has been forwarded in the main body of a message (when $$mime_forward is unset).
For a full listing of defined `printf(3)`-like sequences see the section on $$index_format.
See also $$attribution_locale.

--------------------------------------------------------------------------------

(forward-attribution-trailer)=
## `$forward_attribution_trailer`

- **Type:** expando
- **Default:**
    ```
    set forward_attribution_trailer = "----- End forwarded message -----"
    ```

This is the string that will follow a message which has been forwarded in the main body of a message (when $$mime_forward is unset).
For a full listing of defined `printf(3)`-like sequences see the section on $$index_format.
See also $$attribution_locale.

--------------------------------------------------------------------------------

(forward-decrypt)=
## `$forward_decrypt`

- **Type:** boolean
- **Default:**
    ```
    set forward_decrypt = yes
    ```

Controls the handling of encrypted messages when forwarding a message.
When _set_, the outer layer of encryption is stripped off.
This variable is only used if $$mime_forward is _set_ and $$mime_forward_decode is _unset_.

--------------------------------------------------------------------------------

(forward-edit)=
## `$forward_edit`

- **Type:** quad-option
- **Default:**
    ```
    set forward_edit = yes
    ```

This quadoption controls whether or not the user is automatically placed in the editor when forwarding messages.
For those who always want to forward with no modification, use a setting of "no".

--------------------------------------------------------------------------------

(forward-format)=
## `$forward_format`

- **Type:** expando
- **Default:**
    ```
    set forward_format = "[%a: %s]"
    ```

This variable controls the default subject when forwarding a message.
It uses the same format sequences as the $$index_format variable.

--------------------------------------------------------------------------------

(forward-references)=
## `$forward_references`

- **Type:** boolean
- **Default:**
    ```
    set forward_references = no
    ```

When _set_, forwarded messages set the "In-Reply-To:" and "References:" headers in the same way as normal replies would.
Hence the forwarded message becomes part of the original thread instead of starting a new one.

--------------------------------------------------------------------------------

(greeting)=
## `$greeting`

- **Type:** expando
- **Default:** (empty)
    ```
    set greeting = ""
    ```

When set, this is the string that will precede every message as a greeting phrase to the recipients.

"Format strings" are similar to the strings used in the "C" function printf to format output (see the man page for more detail).
The following sequences are defined in NeoMutt:

| Short | Long Name       | Description                    |
|-------|-----------------|--------------------------------|
| `%n` | `%{real-name}`  | Recipient's real name          |
| `%u` | `%{user-name}`  | User (login) name of recipient |
| `%v` | `%{first-name}` | First name of recipient        |

--------------------------------------------------------------------------------

(hdrs)=
## `$hdrs`

- **Type:** boolean
- **Default:**
    ```
    set hdrs = yes
    ```

When _unset_, the header fields normally added by the "$my-header" command are not created.
This variable _must_ be unset before composing a new message or replying in order to take effect.
If _set_, the user defined header fields are added to every new message.

--------------------------------------------------------------------------------

(hidden-host)=
## `$hidden_host`

- **Type:** boolean
- **Default:**
    ```
    set hidden_host = no
    ```

When _set_, NeoMutt will skip the host name part of $$hostname variable when adding the domain part to addresses.

--------------------------------------------------------------------------------

(honor-followup-to)=
## `$honor_followup_to`

- **Type:** quad-option
- **Default:**
    ```
    set honor_followup_to = yes
    ```

This variable controls whether or not a Mail-Followup-To header is honored when group-replying to a message.

--------------------------------------------------------------------------------

(ignore-list-reply-to)=
## `$ignore_list_reply_to`

- **Type:** boolean
- **Default:**
    ```
    set ignore_list_reply_to = no
    ```

Affects the behavior of the `<reply>` function when replying to messages from mailing lists (as defined by the "$subscribe" or "$lists" commands).  When _set_, if the "Reply-To:" field is set to the same value as the "To:" field, NeoMutt assumes that the "Reply-To:" field was set by the mailing list to automate responses to the list, and will ignore this field.
To direct a response to the mailing list when this option is _set_, use the `$<list-reply>` function; `<group-reply>` will reply to both the sender and the list.

--------------------------------------------------------------------------------

(include)=
## `$include`

- **Type:** quad-option
- **Default:**
    ```
    set include = ask-yes
    ```

Controls whether or not a copy of the message(s) you are replying to is included in your reply.

--------------------------------------------------------------------------------

(inews-command)=
## `$inews_command`

- **Type:** expando (command string)
- **Default:** (empty)
    ```
    set inews_command = ""
    ```

If set, specifies the program and arguments used to deliver news posted by NeoMutt.
Otherwise, NeoMutt posts article using current connection to news server.
The following printf-style sequence is understood:

| Short | Description       |
|-------|-------------------|
| `%a`  | account url       |
| `%p`  | port              |
| `%P`  | port if specified |
| `%s`  | news server name  |
| `%S`  | url schema        |
| `%u`  | username          |

Example:

Example:
```
set inews_command="/usr/local/bin/inews -hS" 
```

--------------------------------------------------------------------------------

(message-id-format)=
## `$message_id_format`

- **Type:** expando
- **Default:**
    ```
    set message_id_format = "<%z@%f>"
    ```

This variable allows you to choose a custom format for the Message-Id when sending messages.
The value may end in ``|'' to invoke an external filter.
See $formatstrings-filters.

Please note that the Message-ID value follows a strict syntax, and you are responsible for ensuring correctness if you change this from the default.
In particular, the value must follow the syntax in RFC 5322:
```"<" id-left "@" id-right ">"`''.  No spaces are allowed, and `id-left` should follow the dot-atom-text syntax in the RFC.
The `id-right` should generally be left as ```%f`''.

If unset, NeoMutt will use a long random format.

If the format doesn't begin/end with ``<'', ``>'' they will be added.

The old Message-ID format can be used by setting this to: ```<%Y%02m%02d%02H%02M%02S.G%c%p@%f>`'' 

The following `printf(3)`-style sequences are understood:

| Short | Long Name      | Description                                                        |
|-------|----------------|--------------------------------------------------------------------|
| %c    | `%{counter}`   | Step counter looping from `A` to `Z`                               |
| %d    | `%{day}`       | Current day of the month (GMT)                                     |
| %f    | `%{hostname}`  | [$hostname](#hostname)                                             |
| %H    | `%{hour}`      | Current hour using a 24-hour clock (GMT)                           |
| %m    | `%{minute}`    | Current month number (GMT)                                         |
| %M    | `%{month}`     | Current minute of the hour (GMT)                                   |
| %p    | `%{pid}`       | Pid of the running mutt process                                    |
| %r    | `%{random_3}`  | 3 bytes of pseudo-random data encoded in Base64                    |
| %S    | `%{second}`    | Current second of the minute (GMT)                                 |
| %x    | `%{random_1}`  | 1 byte of pseudo-random data hex encoded (example: `1b`)           |
| %Y    | `%{year}`      | Current year using 4 digits (GMT)                                  |
| %z    | `%{random_12}` | 4 byte timestamp + 8 bytes of pseudo-random data encoded in Base64 |

See also: Base64Url: https://datatracker.ietf.org/doc/html/rfc4648#section-5 

--------------------------------------------------------------------------------

(me-too)=
## `$me_too`

- **Type:** boolean
- **Default:**
    ```
    set me_too = no
    ```

If _unset_, NeoMutt will remove your address (see the "$alternates" command) from the list of recipients when replying to a message.

--------------------------------------------------------------------------------

(mime-forward-decode)=
## `$mime_forward_decode`

- **Type:** boolean
- **Default:**
    ```
    set mime_forward_decode = no
    ```

Controls the decoding of complex MIME messages into `text/plain` when forwarding a message while $$mime_forward is _set_.
Otherwise $$forward_decode is used instead.

--------------------------------------------------------------------------------

(mime-type-query-command)=
## `$mime_type_query_command`

- **Type:** command (string)
- **Default:** (empty)
    ```
    set mime_type_query_command = ""
    ```

This specifies a command to run, to determine the mime type of a new attachment when composing a message.
Unless $$mime_type_query_first is set, this will only be run if the attachment's extension is not found in the mime.types file.

The string may contain a "%s", which will be substituted with the attachment filename.
NeoMutt will add quotes around the string substituted for "%s" automatically according to shell quoting rules, so you should avoid adding your own.
If no "%s" is found in the string, NeoMutt will append the attachment filename to the end of the string.

The command should output a single line containing the attachment's mime type.

Suggested values are "xdg-mime query filetype" or "file -bi".

--------------------------------------------------------------------------------

(mime-type-query-first)=
## `$mime_type_query_first`

- **Type:** boolean
- **Default:**
    ```
    set mime_type_query_first = no
    ```

When _set_, the $$mime_type_query_command will be run before the mime.types lookup.

--------------------------------------------------------------------------------

(nm-record)=
## `$nm_record`

- **Type:** boolean
- **Default:**
    ```
    set nm_record = no
    ```

This variable specifies whether, when writing a just-sent message to the $$record, the message should also be added to the notmuch DB.
Replies inherit the notmuch tags from the original message.
See $$nm_record_tags for how to modify the set of notmuch tags assigned to sent messages written to the record.

--------------------------------------------------------------------------------

(pgp-reply-inline)=
## `$pgp_reply_inline`

- **Type:** boolean
- **Default:**
    ```
    set pgp_reply_inline = no
    ```
- **Scope:** PGP only

Setting this variable will cause NeoMutt to always attempt to create an inline (traditional) message when replying to a message which is PGP encrypted/signed inline.
This can be overridden by use of the pgp menu, when inline is not required.
This option does not automatically detect if the (replied-to) message is inline; instead it relies on NeoMutt internals for previously checked/flagged messages.

Note that NeoMutt might automatically use PGP/MIME for messages which consist of more than a single MIME part.
NeoMutt can be configured to ask before sending PGP/MIME messages when inline (traditional) would not work.

Also see the $$pgp_mime_auto variable.

Also note that using the old-style PGP message format is **strongly** **deprecated**.

--------------------------------------------------------------------------------

(postpone-encrypt)=
## `$postpone_encrypt`

- **Type:** boolean
- **Default:**
    ```
    set postpone_encrypt = no
    ```
- **Scope:** Crypto only

When _set_, postponed messages that are marked for encryption will be self-encrypted.
NeoMutt will first try to encrypt using the value specified in $$pgp_default_key or $$smime_default_key.

--------------------------------------------------------------------------------

(postpone-encrypt-as)=
## `$postpone_encrypt_as`

- **Type:** string
- **Default:** (empty)
    ```
    set postpone_encrypt_as = ""
    ```

When _set_, NeoMutt will use this as a fallback encryption key for postponed messages.

--------------------------------------------------------------------------------

(recall)=
## `$recall`

- **Type:** quad-option
- **Default:**
    ```
    set recall = ask-yes
    ```

Controls whether or not NeoMutt recalls postponed messages when composing a new message.

Setting this variable to _yes_ is not generally useful, and thus not recommended.
Note that the `<recall-message>` function can be used to manually recall postponed messages.

Also see $$postponed variable.

--------------------------------------------------------------------------------

(reply-self)=
## `$reply_self`

- **Type:** boolean
- **Default:**
    ```
    set reply_self = no
    ```

If _unset_ and you are replying to a message sent by you, NeoMutt will assume that you want to reply to the recipients of that message rather than to yourself.

Also see the "$alternates" command.

--------------------------------------------------------------------------------

(reply-to)=
## `$reply_to`

- **Type:** quad-option
- **Default:**
    ```
    set reply_to = ask-yes
    ```

If _set_, when replying to a message, NeoMutt will use the address listed in the Reply-to: header as the recipient of the reply.
If _unset_, it will use the address in the From: header field instead.
This option is useful for reading a mailing list that sets the Reply-To:
header field to the list address and you want to send a private message to the author of a message.

--------------------------------------------------------------------------------

(reply-with-xorig)=
## `$reply_with_xorig`

- **Type:** boolean
- **Default:**
    ```
    set reply_with_xorig = no
    ```

This variable provides a toggle.
When active, the From: header will be extracted from the current mail's 'X-Original-To:' header.
This setting does not have precedence over "$reverse_real_name".

Assuming 'fast_reply' is disabled, this option will prompt the user with a prefilled From: header.

--------------------------------------------------------------------------------

(resume-draft-files)=
## `$resume_draft_files`

- **Type:** boolean
- **Default:**
    ```
    set resume_draft_files = no
    ```

If _set_, draft files (specified by `-H` on the command line) are processed similarly to when resuming a postponed message.
Recipients are not prompted for; send-hooks are not evaluated; no alias expansion takes place; user-defined headers and signatures are not added to the message.

--------------------------------------------------------------------------------

(reverse-name)=
## `$reverse_name`

- **Type:** boolean
- **Default:**
    ```
    set reverse_name = no
    ```

It may sometimes arrive that you receive mail to a certain machine, move the messages to another machine, and reply to some the messages from there.
If this variable is _set_, the default _From:_ line of the reply messages is built using the address where you received the messages you are replying to **if** that address matches your "$alternates".  If the variable is _unset_, or the address that would be used doesn't match your "$alternates", the _From:_ line will use your address on the current machine.

Also see the "$alternates" command and $$reverse_real_name.

--------------------------------------------------------------------------------

(reverse-real-name)=
## `$reverse_real_name`

- **Type:** boolean
- **Default:**
    ```
    set reverse_real_name = yes
    ```

This variable fine-tunes the behavior of the $$reverse_name feature.

When it is _unset_, NeoMutt will remove the real name part of a matching address.
This allows the use of the email address without having to also use what the sender put in the real name field.

When it is _set_, NeoMutt will use the matching address as-is.

In either case, a missing real name will be filled in afterwards using the value of $$real_name.

--------------------------------------------------------------------------------

(sendmail)=
## `$sendmail`

- **Type:** command (string)
- **Default:**
    ```
    set sendmail = SENDMAIL " -oem -oi"
    ```

Specifies the program and arguments used to deliver mail sent by NeoMutt.
NeoMutt expects that the specified program interprets additional arguments as recipient addresses.
NeoMutt appends all recipients after adding a `--` delimiter (if not already present).  Additional flags, such as for $$use_8bit_mime, $$use_envelope_from, $$dsn_notify, or $$dsn_return will be added before the delimiter.

**Note:** This command is invoked differently from most other commands in NeoMutt.
It is tokenized by space, and invoked directly via `execvp(3)` with an array of arguments - so commands or arguments with spaces in them are not supported.
The shell is not used to run the command, so shell quoting is also not supported.

**See also:** $$write_bcc.

--------------------------------------------------------------------------------

(sendmail-wait)=
## `$sendmail_wait`

- **Type:** number
- **Default:**
    ```
    set sendmail_wait = 0
    ```

Specifies the number of seconds to wait for the $$sendmail process to finish before giving up and putting delivery in the background.

NeoMutt interprets the value of this variable as follows:

| Value | Description                                                        |
|-------|--------------------------------------------------------------------|
| >0 | number of seconds to wait for sendmail to finish before continuing |
| 0  | wait forever for sendmail to finish                                |
| <0 | always put sendmail in the background without waiting              |

Note that if you specify a value other than 0, the output of the child process will be put in a temporary file.
If there is some error, you will be informed as to where to find the output.

--------------------------------------------------------------------------------

(signature)=
## `$signature`

- **Type:** path (string)
- **Default:**
    ```
    set signature = "~/.signature"
    ```

Specifies the filename of your signature, which is appended to all outgoing messages.
If the filename ends with a pipe ("|"), it is assumed that filename is a shell command and input should be read from its standard output.

--------------------------------------------------------------------------------

(sig-dashes)=
## `$sig_dashes`

- **Type:** boolean
- **Default:**
    ```
    set sig_dashes = yes
    ```

If _set_, a line containing "-- " (note the trailing space) will be inserted before your $$signature.
It is **strongly** recommended that you not _unset_ this variable unless your signature contains just your name.
The reason for this is because many software packages use "-- \n" to detect your signature.
For example, NeoMutt has the ability to highlight the signature in a different color in the built-in pager.

--------------------------------------------------------------------------------

(sig-on-top)=
## `$sig_on_top`

- **Type:** boolean
- **Default:**
    ```
    set sig_on_top = no
    ```

If _set_, the signature will be included before any quoted or forwarded text.
It is **strongly** recommended that you do not set this variable unless you really know what you are doing, and are prepared to take some heat from netiquette guardians.

--------------------------------------------------------------------------------

(smtp-authenticators)=
## `$smtp_authenticators`

- **Type:** string list
- **Default:** (empty)
    ```
    set smtp_authenticators = ""
    ```

This is a colon-separated list of authentication methods NeoMutt may attempt to use to log in to an SMTP server, in the order NeoMutt should try them.
Authentication methods are any SASL mechanism, e.g.
"plain", "digest-md5", "gssapi" or "cram-md5".
This option is case-insensitive.
If it is "unset" (the default) NeoMutt will try all available methods, in order from most-secure to least-secure.
Support for the "plain" mechanism is bundled; other mechanisms are provided by an external SASL library (look for '+sasl' in the output of neomutt -v).

Example:

```neomuttrc
set smtp_authenticators="digest-md5:cram-md5"
```

--------------------------------------------------------------------------------

(smtp-oauth-refresh-command)=
## `$smtp_oauth_refresh_command`

- **Type:** command (string)
- **Default:** (empty)
    ```
    set smtp_oauth_refresh_command = ""
    ```

The command to run to generate an OAUTH refresh token for authorizing your connection to your SMTP server.
This command will be run on every connection attempt that uses the OAUTHBEARER or XOAUTH2 authentication mechanisms.
See "$oauth" for details.

--------------------------------------------------------------------------------

(smtp-pass)=
## `$smtp_pass`

- **Type:** string
- **Default:** (empty)
    ```
    set smtp_pass = ""
    ```

Specifies the password for your SMTP account.
If _unset_, NeoMutt will prompt you for your password when you first send mail via SMTP.
See $$smtp_url to configure NeoMutt to send mail via SMTP.

**Warning**: you should only use this option when you are on a fairly secure machine, because the superuser can read your neomuttrc even if you are the only one who can read the file.

--------------------------------------------------------------------------------

(smtp-url)=
## `$smtp_url`

- **Type:** string
- **Default:** (empty)
    ```
    set smtp_url = ""
    ```

Defines the SMTP smarthost where sent messages should relayed for delivery.
This should take the form of an SMTP URL, e.g.:

```
smtp[s]://[user[:pass]@]host[:port]
```

where "[...]" denotes an optional part.
Setting this variable overrides the value of the $$sendmail variable.

Also see $$write_bcc.

--------------------------------------------------------------------------------

(smtp-user)=
## `$smtp_user`

- **Type:** string
- **Default:** (empty)
    ```
    set smtp_user = ""
    ```

The username for the SMTP server.

This variable defaults to your user name on the local machine.

--------------------------------------------------------------------------------

(user-agent)=
## `$user_agent`

- **Type:** boolean
- **Default:**
    ```
    set user_agent = no
    ```

When _set_, NeoMutt will add a "User-Agent:" header to outgoing messages, indicating which version of NeoMutt was used for composing them.

--------------------------------------------------------------------------------

(use-8bit-mime)=
## `$use_8bit_mime`

- **Type:** boolean
- **Default:**
    ```
    set use_8bit_mime = no
    ```

**Warning:** do not set this variable unless you are using a version of sendmail which supports the `-B8BITMIME` flag (such as sendmail 8.8.x) or you may not be able to send mail.

When _set_, NeoMutt will invoke $$sendmail with the `-B8BITMIME`
flag when sending 8-bit messages to enable ESMTP negotiation.

--------------------------------------------------------------------------------

(use-envelope-from)=
## `$use_envelope_from`

- **Type:** boolean
- **Default:**
    ```
    set use_envelope_from = no
    ```

When _set_, NeoMutt will set the _envelope_ sender of the message.
If $$envelope_from_address is _set_, it will be used as the sender address.
If _unset_, NeoMutt will attempt to derive the sender from the "From:" header.

Note that this information is passed to sendmail command using the `-f` command line switch.
Therefore setting this option is not useful if the $$sendmail variable already contains `-f` or if the executable pointed to by $$sendmail doesn't support the `-f` switch.

--------------------------------------------------------------------------------

(use-from)=
## `$use_from`

- **Type:** boolean
- **Default:**
    ```
    set use_from = yes
    ```

When _set_, NeoMutt will generate the "From:" header field when sending messages.
If _unset_, no "From:" header field will be generated unless the user explicitly sets one using the "$my-header" command.

--------------------------------------------------------------------------------

(wrap-headers)=
## `$wrap_headers`

- **Type:** number
- **Default:**
    ```
    set wrap_headers = 78
    ```

This option specifies the number of characters to use for wrapping an outgoing message's headers.
Allowed values are between 78 and 998 inclusive.

**Note:** This option usually shouldn't be changed.
RFC5233 recommends a line length of 78 (the default), so **please only change this setting when you know what you're doing**.

--------------------------------------------------------------------------------

(write-bcc)=
## `$write_bcc`

- **Type:** boolean
- **Default:**
    ```
    set write_bcc = no
    ```

Controls whether NeoMutt writes out the "Bcc:" header when preparing messages to be sent.
Some MTAs, such as Exim and Courier, do not strip the "Bcc:" header; so it is advisable to leave this unset unless you have a particular need for the header to be in the sent message.

If NeoMutt is set to deliver directly via SMTP(see $$smtp_url), this option does nothing: NeoMutt will never write out the "Bcc:" header in this case.

Note this option only affects the sending of messages.
Fcc'ed copies of a message will always contain the "Bcc:" header if one exists.

