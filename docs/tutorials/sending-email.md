---
title: Sending Your First Email
description: Learn to compose, reply to, and send emails with NeoMutt, including the compose menu, header editing, and cryptographic signing
keywords: [neomutt, sending, email, compose, reply, forward, pgp, smime, tutorial]
diataxis_type: tutorial
---

# Sending Your First Email

:::{admonition} Diátaxis: Tutorial
:class: note

Write as a **lesson**. Guide the learner through a meaningful exercise step by step.
Use second person ("you"). Show concrete actions and their expected results.
Don't explain concepts — demonstrate them through doing. Start with the simplest case
and build complexity gradually. The reader should feel a sense of accomplishment at the end.
:::

## Introduction

The following bindings are available in the *index* and *pager* to start a new message.

### Mail Sending Keys

| Key | Function | Description |
|-----|----------|-------------|
| m | `<mail>` | compose a new message |
| r | `<reply>` | reply to sender |
| g | `<group-reply>` | reply to all recipients |
| | `<group-chat-reply>` | reply to all recipients preserving To/Cc |
| L | `<list-reply>` | reply to a mailing list |
| L | `<list-subscribe>` | send a subscription email to a mailing list |
| L | `<list-unsubscribe>` | send an unsubscription email to a mailing list |
| f | `<forward-message>` | forward message |
| b | `<bounce-message>` | bounce (remail) message |
| Esc k | `<mail-key>` | mail a PGP public key to someone |

*Bouncing* a message sends the message as-is to the recipient you specify. *Forwarding*
a message allows you to add comments or modify the message you are forwarding. These items
are discussed in greater detail in the section "Forwarding and Bouncing Mail".

NeoMutt will then enter the *compose* menu and prompt you for the recipients to place on the
"To:" header field when you hit `m` to start a new message. Next, it will ask you for the
"Subject:" field for the message, providing a default if you are replying to or forwarding
a message. You again have the chance to adjust recipients, subject, and security settings
right before actually sending the message. See also `$ask_cc`, `$ask_bcc`, `$auto_edit`,
`$bounce`, `$fast_reply`, and `$include` for changing how and if NeoMutt asks these
questions.

When replying, NeoMutt fills these fields with proper values depending on the reply type. The
types of replying supported are:

Simple reply
: Reply to the author directly.

Group reply
: Reply to the author; cc all other recipients; consults `alternates` and excludes you.

Group Chat reply
: Reply to the author and other recipients in the To list; cc other recipients in the Cc
  list; consults `alternates` and excludes you.

List reply
: Reply to all mailing list addresses found, either specified via configuration or
  auto-detected.

After getting recipients for new messages, forwards or replies, NeoMutt will then
automatically start your `$editor` on the message body. If the `$edit_headers` variable is
set, the headers will be at the top of the message in your editor; the message body should
start on a new line after the existing blank line at the end of headers. Any messages you are
replying to will be added in sort order to the message, with appropriate
`$attribution_intro`, `$indent_string` and `$attribution_trailer`. When forwarding a message,
if the `$mime_forward` variable is unset, a copy of the forwarded message will be included. If
you have specified a `$signature`, it will be appended to the message.

Once you have finished editing the body of your mail message, you are returned to the
*compose* menu providing the functions shown below to modify, send or postpone the message.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Compose flow — editor with headers

**Description:** A terminal showing NeoMutt's editor view when composing a new message with `$edit_headers` enabled, displaying editable headers (From, To, Cc, Subject) at the top of the editor, followed by a blank line and the message body area with the signature appended.

**Highlights:** How headers appear as editable text at the top of the editor, the blank separator line between headers and body, and the signature placement at the end.
:::

## The Compose Menu

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** The Compose Menu screen

**Description:** The NeoMutt Compose Menu after returning from the editor, showing the split-screen layout: header fields (From, To, Cc, Bcc, Subject, Reply-To, Fcc) in the upper section, security options (PGP/S/MIME off/on), and the attachment list in the lower section showing at least one text/plain attachment (the message body).

**Highlights:** The editable fields in the upper pane, the security status indicators, and the attachment list showing the message body as the first attachment with its MIME type and size.
:::

### Compose Menu Keys

| Key | Function | Description |
|-----|----------|-------------|
| a | `<attach-file>` | attach a file |
| A | `<attach-message>` | attach message(s) to the message |
| Esc k | `<attach-key>` | attach a PGP public key |
| d | `<edit-description>` | edit description on attachment |
| D | `<detach-file>` | detach a file |
| t | `<edit-to>` | edit the To field |
| Esc f | `<edit-from>` | edit the From field |
| r | `<edit-reply-to>` | edit the Reply-To field |
| c | `<edit-cc>` | edit the Cc field |
| b | `<edit-bcc>` | edit the Bcc field |
| y | `<send-message>` | send the message |
| s | `<edit-subject>` | edit the Subject |
| S | `<smime-menu>` | select S/MIME options |
| f | `<edit-fcc>` | specify an "Fcc" mailbox |
| p | `<pgp-menu>` | select PGP options |
| P | `<postpone-message>` | postpone this message until later |
| q | `<quit>` | quit (abort) sending the message |
| w | `<write-fcc>` | write the message to a folder |
| i | `<ispell>` | check spelling (if available on your system) |
| ^F | `<forget-passphrase>` | wipe passphrase(s) from memory |

The compose menu is also used to edit the attachments for a message which can be either files
or other messages. The `<attach-message>` function will prompt you for a folder to attach
messages from. You can now tag messages in that folder and they will be attached to the
message you are sending.

:::{note}
Note that certain operations like composing a new mail, replying, forwarding, etc. are not
permitted when you are in that folder. The %r in `$status_format` will change to a "A" to
indicate that you are in attach-message mode.
:::

After exiting the compose menu via `<send-message>`, the message will be sent. This happens
via `$smtp_url`. Otherwise `$sendmail` will be invoked. Prior to version 2019-11-29, NeoMutt
enabled `$write_bcc` by default, assuming the MTA would automatically remove a `Bcc:` header
as part of delivery. Starting with 2019-11-29, the option is unset by default, but no longer
affects the fcc copy of the message.

## Editing the Message Header

When editing the header because of `$edit_headers` being set, there are several pseudo
headers available which will not be included in sent messages but trigger special NeoMutt
behavior.

### Fcc: Pseudo Header

If you specify either of

`Mutt-Fcc:` *filename*

`Fcc:` *filename*

as a header, NeoMutt will pick up *filename* just as if you had used the `<edit-fcc>`
function in the *compose* menu. It can later be changed from the compose menu.

### Attach: Pseudo Header

You can also attach files to your message by specifying either of

`Mutt-Attach:` *filename* [*description*]

`Attach:` *filename* [*description*]

where *filename* is the file to attach and *description* is an optional string to use as the
description of the attached file. Spaces in filenames have to be escaped using backslash
("\\"). The file can be removed as well as more added from the compose menu.

### Pgp: Pseudo Header

If you want to use PGP, you can specify either of

`Mutt-PGP:` [ `E` | `S` | `S` *\<id\>* ]

`Pgp:` [ `E` | `S` | `S` *\<id\>* ]

"E" selects encryption, "S" selects signing and "S\<id\>" selects signing with the given key,
setting `$pgp_sign_as` for the duration of the message composition session. The selection can
later be changed in the compose menu.

### Smime: Pseudo Header

If you want to use S/MIME, you can specify either of

`Mutt-SMIME:` [ `E` | `S` | `S` *\<id\>* ]

`Smime:` [ `E` | `S` | `S` *\<id\>* ]

"E" selects encryption, "S" selects signing and "S\<id\>" selects signing with the given key,
setting `$smime_sign_as` for the duration of the message composition session. The selection
can later be changed in the compose menu.

### In-Reply-To: Header

When replying to messages, the *In-Reply-To:* header contains the Message-Id of the
message(s) you reply to. If you remove or modify its value, NeoMutt will not generate
a *References:* field, which allows you to create a new message thread, for example to create
a new message to a mailing list without having to enter the mailing list's address.

If you intend to start a new thread by replying, please make really sure you remove the
*In-Reply-To:* header in your editor. Otherwise, though you'll produce a technically valid
reply, some netiquette guardians will be annoyed by this so-called "thread hijacking".

## Sending Cryptographically Signed/Encrypted Messages

If you have told NeoMutt to PGP or S/MIME encrypt a message, it will guide you through a key
selection process when you try to send the message. NeoMutt will not ask you any questions
about keys which have a certified user ID matching one of the message recipients' mail
addresses. However, there may be situations in which there are several keys, weakly certified
user ID fields, or where no matching keys can be found.

In these cases, you are dropped into a menu with a list of keys from which you can select one.
When you quit this menu, or NeoMutt can't find any matching keys, you are prompted for a user
ID. You can, as usually, abort this prompt using `^G`. When you do so, NeoMutt will return to
the compose screen.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** PGP key selection menu

**Description:** The NeoMutt PGP key selection menu showing a list of available public keys with columns for key ID, capabilities (encryption/signing), validity flags, creation date, and associated user IDs/email addresses.

**Highlights:** The key capability indicators (e/s for encrypt/sign), the validity column showing trust level, and how multiple keys for the same recipient are listed for selection.
:::

Once you have successfully finished the key selection, the message will be encrypted using the
selected public keys when sent out.

To ensure you can view encrypted messages you have sent, you may wish to set
`$pgp_self_encrypt` and `$pgp_default_key` for PGP, or `$smime_self_encrypt` and
`$smime_default_key` for S/MIME.

Most fields of the entries in the key selection menu (see also `$pgp_entry_format`) have
obvious meanings. But some explanations on the capabilities, flags, and validity fields are in
order.

The flags sequence ("%f") will expand to one of the following flags:

### PGP Key Menu Flags

| Flag | Description |
|------|-------------|
| R | The key has been revoked and can't be used. |
| X | The key is expired and can't be used. |
| d | You have marked the key as disabled. |
| c | There are unknown critical self-signature packets. |

The capabilities field ("%c") expands to a two-character sequence representing a key's
capabilities. The first character gives the key's encryption capabilities: A minus sign ("-")
means that the key cannot be used for encryption. A dot (".") means that it's marked as
a signature key in one of the user IDs, but may also be used for encryption. The letter "e"
indicates that this key can be used for encryption.

The second character indicates the key's signing capabilities. Once again, a "-" implies "not
for signing", "." implies that the key is marked as an encryption key in one of the user-ids,
and "s" denotes a key which can be used for signing.

Finally, the validity field ("%t") indicates how well-certified a user-id is. Its values
depend on the backend used. Note that S/MIME (which uses X509 certificates) has no concept of
validity, so this field simply shows `x`.

### PGP Key Menu Validity

| Flag (classic PGP) | Flag (GPGME) | Description |
|---------------------|--------------|-------------|
| N/A | ? | indicates unknown validity |
| ? | q | indicates undefined validity |
| \- | n | indicates a never valid key (untrusted association) |
| space | m | indicates marginal validity (partially trusted) |
| + | f | indicates full validity (fully trusted) |
| N/A | u | indicates ultimate validity |
| N/A | x | the entry is an X509 certificate (S/MIME) |

## Sending Format=Flowed Messages

### Concept

`format=flowed`-style messages (or `f=f` for short) are `text/plain` messages that consist of
paragraphs which a receiver's mail client may reformat to its own needs, which mostly means to
customize line lengths regardless of what the sender sent. Technically this is achieved by
letting lines of a "flowable" paragraph end in spaces except for the last line.

While for text-mode clients like NeoMutt it's best to assume only a standard 80x24 character
cell terminal, it may be desired to let the receiver decide completely how to view a message.

### NeoMutt Support

NeoMutt only supports setting the required `format=flowed` MIME parameter on outgoing messages
if the `$text_flowed` variable is set, specifically it does not add the trailing spaces.

After editing, NeoMutt properly space-stuffs the message. *Space-stuffing* is required by
RFC3676, defining `format=flowed`, and means to prepend a space to:

- all lines starting with a space
- lines starting with the word "`From`" followed by space
- all lines starting with "`>`", which is not intended to be a quote character

:::{note}
NeoMutt only supports space-stuffing for the first two types of lines but not for the third:
It is impossible to safely detect whether a leading `>` character starts a quote or not.
:::

All leading spaces are to be removed by receiving clients to restore the original message
prior to further processing.

### Editor Considerations

As NeoMutt provides no additional features to compose `f=f` messages, it's completely up to
the user and his editor to produce proper messages. Please consider your editor's
documentation if you intend to send `f=f` messages.

For example, *vim* provides the `w` flag for its `formatoptions` setting to assist in creating
`f=f` messages, see `:help fo-table` for details.

### Reformatting

NeoMutt has some support for reformatting when viewing and replying to `format=flowed`
messages. In order to take advantage of these, `$reflow_text` must be set.

- Paragraphs are automatically reflowed and wrapped at a width specified by `$reflow_wrap`.
- In its original format, the quoting style of `format=flowed` messages can be difficult to
  read, and doesn't intermix well with non-flowed replies. Setting `$reflow_space_quotes`
  adds spaces after each level of quoting when in the pager and replying in a non-flowed
  format (i.e. with `$text_flowed` unset).
- If `$reflow_space_quotes` is unset, NeoMutt will still add one trailing space after all the
  quotes in the pager (but not when replying).
