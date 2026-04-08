---
title: Glossary
description: Definitions of email and NeoMutt terms from aliases and MIME to threads, hooks, and encryption
keywords: neomutt, glossary, definitions, terminology, email, imap, smtp, pop3, mime, alias, thread, hook, pattern, encryption, gpg, sidebar
---

(ref-glossary)=
# Glossary

This glossary explains terms you may come across in the NeoMutt documentation,
in email-related discussions, or while using NeoMutt day-to-day.
It is written for people who are new to NeoMutt or to email technology in general.

---

## A

**Account**
:  A set of settings that tell NeoMutt how to connect to one email service.
   An account holds the server address, your username, and a collection of mailboxes.
   You can set up several accounts (for example, one for work and one for personal mail) and switch between them.

**Address (Email Address)**
:  The unique name used to send and receive email, written as `user@example.com`.
   The part before the `@` identifies the person; the part after the `@` identifies the mail server.

**Alias**
:  A short nickname that stands for one or more email addresses.
   Instead of typing a long address every time, you can type the alias.
   Aliases are stored in a file you choose (see *Alias File*).

**Alias File**
:  The file where NeoMutt saves your aliases.
   Set with [`$alias_file`](cfg-alias-file).

**Alternates**
:  A list of your own email addresses.
   NeoMutt uses this list to recognise messages that were sent *by you*, so it can handle replies correctly and avoid sending duplicates to yourself.

**Attachment**
:  A file that is sent along with an email message — for example a photo, a document, or a spreadsheet.
   Attachments are encoded using MIME so they can travel safely through the email system.

**Autocrypt**
:  A standard that tries to make email encryption easy and automatic.
   When enabled, NeoMutt exchanges encryption keys in the background so that future messages between you and your contacts can be encrypted without extra steps.

**Auto-view**
:  A feature that tells NeoMutt to automatically convert certain attachment types (for example HTML) into plain text so you can read them directly in the pager.
   Controlled by the [`:auto-view`](cmd-auto-view) command and the *mailcap* file.

---

## B

**Base64**
:  An encoding method used to convert binary data (images, documents) into plain text characters so it can be safely included in an email.
   You rarely need to think about it — NeoMutt handles it for you.

**BCC (Blind Carbon Copy)**
:  A way to send a copy of a message to someone without the other recipients knowing.
   The BCC addresses are hidden from everyone else.

**Body**
:  The main content of an email — the actual message text you read.
   An email can have more than one body part (for example plain text *and* HTML), plus attachments.

**Bounce**
:  Resending a message exactly as it is to a different address, as though the new recipient had been one of the original recipients.
   Unlike forwarding, bouncing does not let you add your own comments.

**Browser**
:  A screen inside NeoMutt that lets you navigate the file system or a list of mailboxes.
   You use it when choosing a folder to open, when attaching files, or when browsing IMAP folders.

---

## C

**CC (Carbon Copy)**
:  A copy of a message sent to additional recipients.
   Unlike BCC, every recipient can see who was CC'd.

**Character Set (Charset)**
:  A mapping that assigns numbers to letters, digits, and symbols so computers can store and display text.
   Common character sets include ASCII, ISO-8859-1, and UTF-8.
   NeoMutt converts between character sets when displaying or sending messages.

**Collapse (Thread)**
:  Hiding all messages in a conversation thread except the first one.
   This saves screen space when a thread has many replies.
   You can expand (open) the thread again at any time.

**Color Rule**
:  A line in your configuration that changes the colour of part of the screen.
   For example, you can make unread messages appear in bold white or highlight important senders in red.

**Compose Menu**
:  The screen you see when you are writing a new message (or a reply or a forward).
   From here you can edit the `To:`, `Cc:`, `Bcc:` and `Subject:` fields, add or remove attachments, choose encryption, and send or postpone the message.

**Config File (neomuttrc)**
:  A text file that contains your personal NeoMutt settings — colours, key bindings, account details, and so on.
   NeoMutt looks for this file when it starts.
   The most common locations are `~/.neomuttrc` or `~/.config/neomutt/neomuttrc`.

**Config Option (Variable)**
:  A named setting that controls some part of NeoMutt's behaviour.
   Options are set with the `set` command (for example `set sort=threads`).
   NeoMutt has hundreds of options, covering everything from display formatting to network timeouts.

**Content-Type**
:  A label on an email part that says what kind of data it contains — for example `text/plain` (ordinary text), `text/html` (a web page), or `image/png` (a picture).
   NeoMutt reads the content-type to decide how to display each part.

---

## D

**Delete**
:  Marking a message for removal.
   In NeoMutt the message is not actually removed until you *sync* or leave the mailbox, so you can undelete it if you change your mind.

**Draft**
:  A message you have started writing but have not sent yet.
   See *Postpone*.

**DSN (Delivery Status Notification)**
:  An automatic report from the mail system telling you whether your message was delivered successfully or if there was an error (a "bounce").

---

## E

**Editor**
:  The external text-editing program (for example `vim`, `nano`, or `emacs`) that NeoMutt opens when you compose a message.
   Set with the [`$editor`](cfg-editor) variable.

**Envelope**
:  The set of header fields that describe a message — From, To, Subject, Date, CC, BCC, and others.
   Think of it as the "outside of the envelope" that the mail system reads to know where to deliver the message.

**Expando (Format String)**
:  A short code starting with `%` that NeoMutt replaces with a piece of information.
   For example, `%s` might stand for the subject and `%f` for the sender.
   Expandos are used in options such as [`$index_format`](cfg-index-format) and [`$sidebar_format`](cfg-sidebar-format) to control what you see on screen.

**Expunge**
:  Permanently removing messages that have been marked for deletion.
   This usually happens when you leave the mailbox or run a sync.

---

## F

**Fcc (File Carbon Copy)**
:  A copy of a sent message saved to a local mailbox.
   By default NeoMutt stores these in the folder set by [`$record`](cfg-record).

**Flag**
:  A marker on a message that records its state.
   Common flags include *new*, *read*, *replied*, *flagged* (important), and *deleted*.
   Some flags are synchronised with the server (IMAP), others are local only.

**Folder**
:  Another word for a *mailbox* — a place where email messages are stored.
   Folders can be local directories or remote IMAP folders.

**Format=Flowed (f=f)**
:  A special way of sending plain-text email that allows the receiver's mail program to re-wrap lines to fit their screen width.
   Enabled with [`$text_flowed`](cfg-text-flowed).

**Forward**
:  Sending a copy of a received message to someone else.
   Unlike *bouncing*, forwarding lets you add your own comments or modify the message.

**Function**
:  A named action that NeoMutt can perform — for example [`<next-entry>`](menu-index), [`<delete-message>`](menu-index), or [`<sync-mailbox>`](menu-index).
   Functions can be bound to keys or used inside macros.

---

## G

**GnuPG (GPG)**
:  A free program for encrypting and signing data, including email.
   NeoMutt can use GnuPG (usually through the GPGME library) to send and receive encrypted or signed messages.
   See also *OpenPGP*, *S/MIME*.

**GPGME (GnuPG Made Easy)**
:  A helper library that makes it simpler for programs like NeoMutt to use GnuPG.
   When [`$crypt_use_gpgme`](cfg-crypt-use-gpgme) is set, NeoMutt uses GPGME for all encryption and signing operations.

---

## H

**Header**
:  A line at the top of an email that carries information about the message — for example `From:`, `To:`, `Subject:`, `Date:`, or `Message-ID:`.
   NeoMutt shows selected headers in the index and the pager.

**Header Cache (hcache)**
:  A local file where NeoMutt stores parsed email headers so that opening a mailbox is faster next time, especially for IMAP and Maildir mailboxes.

**Hook**
:  A rule that tells NeoMutt to run one or more commands when a certain event happens.
   For example, a *folder-hook* runs when you open a specific mailbox, and a *send-hook* runs before you send a message.
   Hooks are a powerful way to change settings automatically.

   Common hook types:

   - **account-hook** — runs when connecting to an account
   - **folder-hook** — runs when entering a mailbox
   - **send-hook** — runs before sending, based on recipients
   - **send2-hook** — runs whenever the compose menu is updated
   - **reply-hook** — runs when replying, based on the original message
   - **message-hook** — runs when viewing a specific message
   - **crypt-hook** — maps recipient addresses to encryption keys
   - **charset-hook** — defines an alias for a character set name

---

## I

**IMAP (Internet Message Access Protocol)**
:  A protocol that lets you read and manage email on a remote server.
   Your messages stay on the server, so you can access the same mailbox from multiple devices.

**Index**
:  The main list of messages inside a mailbox.
   Each line shows information about one message (sender, subject, date, flags, and so on).
   The layout is controlled by [`$index_format`](cfg-index-format).

**In-Reply-To**
:  A header field that contains the Message-ID of the message being replied to.
   NeoMutt uses this, together with *References*, to build conversation threads.

---

## K

**Key Binding**
:  A mapping between a key (or key sequence) and a NeoMutt function.
   Almost every key can be rebound to suit your workflow using the [`:bind`](cmd-bind) command.

---

## L

**Limit**
:  A temporary filter that hides messages in the index so that only messages matching a pattern are shown.
   For example, you can limit the view to unread messages only.
   Removing the limit shows all messages again.

**List Reply**
:  Replying to a mailing list address (rather than to the original sender alone).
   NeoMutt detects list addresses from your configuration or from the message headers.

---

## M

**Macro**
:  A shortcut that runs a sequence of commands when you press a key.
   Macros are defined with the [`:macro`](cmd-macro) command and are very useful for automating repetitive tasks.

**Mailbox**
:  A place where email messages are stored.
   A mailbox can be a local file (mbox), a local directory (Maildir), or a remote folder (IMAP).
   NeoMutt lets you open, switch between, and monitor many mailboxes.

**Mailcap**
:  A file (usually `~/.mailcap`) that tells NeoMutt which external program to use when opening an attachment of a given type.
   For example, you might configure it to open PDF files with a PDF viewer.

**Maildir**
:  A mailbox format that stores each message as a separate file inside a directory structure (`cur/`, `new/`, `tmp/`).
   Maildir is reliable, fast, and well suited to use with IMAP synchronisation tools.

**Mailing List**
:  An email address that redistributes messages to a group of subscribers.
   NeoMutt has special support for mailing lists, including list-reply and automatic detection of list headers.

**mbox**
:  A mailbox format that stores all messages together in a single file.
   It is the oldest and simplest format; each message starts with a line beginning with `From `.

**Message**
:  A single email.
   In the index it appears as one line; in the pager you see its full contents.

**Message-ID**
:  A unique identifier assigned to every email (for example `<abc123@example.com>`).
   It is used to link replies into threads and to avoid duplicates.

**MH**
:  A mailbox format similar to Maildir, where each message is a separate file inside a directory.
   The files are named with numbers.

**MIME (Multipurpose Internet Mail Extensions)**
:  A standard that defines how email messages can include things beyond plain text — attachments, images, formatted text, and so on.
   MIME describes how these parts are encoded and labelled.

**mime.types**
:  A system file that maps file extensions (like `.pdf`, `.jpg`) to MIME content types (like `application/pdf`, `image/jpeg`).
   NeoMutt uses it when you attach a file and need to decide what content-type label to give it.

**Multipart**
:  A MIME message that is made up of more than one part — for example, a plain-text version of the message *and* an HTML version, or a message body plus one or more attachments.

---

## N

**NeoMutt**
:  A modern, feature-rich fork of the Mutt email client.
   It adds new features (sidebar, notmuch support, and many more), improved configuration, and better mailbox handling while remaining compatible with Mutt's configuration.

**NNTP (Network News Transfer Protocol)**
:  A protocol for reading and posting messages on Usenet newsgroups.
   NeoMutt includes optional NNTP support.

**Notmuch**
:  An optional email indexing and tagging system.
   When NeoMutt is built with Notmuch support, you can create *virtual mailboxes* whose contents are defined by search queries rather than by a single folder.

---

## O

**OpenPGP (PGP)**
:  A standard for encrypting and digitally signing email.
   NeoMutt supports OpenPGP through GnuPG (GPG) or GPGME.
   See also *S/MIME*.

---

## P

**Pager**
:  The screen inside NeoMutt that shows the full contents of a single message — its headers and body.
   You can scroll, search, reply, or perform other actions while reading.

**Pattern**
:  A small expression used to search for, select, or filter messages.
   For example:

   - `~N` — new (unread) messages
   - `~s vacation` — subject contains "vacation"
   - `~f alice` — from someone named "alice"

   Patterns are used with the search command, the [`<limit>`](menu-index) function,
   hooks, colour rules, and more.

**POP3 (Post Office Protocol)**
:  A protocol that downloads email from a server to your computer.
   Unlike IMAP, POP3 typically removes messages from the server after downloading, so your mail is available on only one device.

**Postpone (Draft)**
:  Saving an unfinished message so you can return to it later.
   Postponed messages are stored in the mailbox set by [`$postponed`](cfg-postponed).
   When you start a new message, NeoMutt will ask if you want to resume a postponed message.

---

## Q

**Quoted Text**
:  Lines in an email body that come from an earlier message in the conversation.
   They are usually prefixed with `> `.
   NeoMutt can colour quoted text differently and let you skip past it when reading.

**Query Command**
:  An external program that NeoMutt calls to look up email addresses.
   For example, you might use an address-book tool so that when you type part of a name, NeoMutt can suggest matches.
   Set with [`$query_command`](cfg-query-command).

---

## R

**References**
:  A header field listing the `Message-ID:`s of all earlier messages in a conversation.
   Together with `In-Reply-To:`, it lets NeoMutt build threads.

**Regex (Regular Expression)**
:  A text pattern used for searching and matching.
   NeoMutt uses regular expressions in many places — search commands, colour rules, hooks, and more.
   For example, `.*@example\.com` matches any address at `example.com`.

**Reply**
:  Sending an answer to a message you received.
   NeoMutt supports several reply styles:

   - **Simple reply** — reply only to the sender.
   - **Group reply** — reply to the sender and CC all other recipients.
   - **List reply** — reply to the mailing list address.

---

## S

**S/MIME**
:  A standard for signing and encrypting email using X.509 certificates (the same kind of certificates used by websites).
   NeoMutt supports S/MIME through GPGME or through its own "classic" mode.
   See also *OpenPGP*.

**SASL (Simple Authentication and Security Layer)**
:  A framework that allows different authentication methods (`LOGIN`, `PLAIN`, `CRAM-MD5`, and others) to be used when connecting to IMAP, POP, or SMTP servers.

**Score**
:  A number that NeoMutt assigns to each message based on rules you define.
   You can use scores to sort or highlight important messages.
   For example, you could give messages from your boss a high score.

**Sidebar**
:  A vertical panel on the side of the screen that shows a list of your mailboxes with message counts (total, new, flagged).
   It can be toggled on and off and its appearance is highly configurable.

**Signature**
:  A block of text automatically added to the end of every outgoing message.
   Typically it contains your name, title, or contact information.
   Set with [`$signature`](cfg-signature).

**SMTP (Simple Mail Transfer Protocol)**
:  The protocol used to send outgoing email.
   NeoMutt can send mail directly via an SMTP server (set with [`$smtp_url`](cfg-smtp-url)) or hand it off to a local program like `sendmail` or `msmtp`.

**Sort Order**
:  The rule that controls the order of messages in the index.
   Messages can be sorted by date, sender, subject, size, score, or by threads.
   Set with [`$sort`](cfg-sort).

**Source**
:  A configuration command that reads and runs another config file.
   This lets you split your settings into multiple files for easier management — for example, one file for colours and another for key bindings.

**STARTTLS**
:  A command that upgrades an existing plain-text connection to an encrypted one using TLS.
   Used with IMAP, POP, and SMTP.

**Status Bar**
:  The line at the bottom of the index (or top, depending on configuration) that shows information about the current mailbox — its name, the number of messages, your position in the list, and more.
   Controlled by [`$status_format`](cfg-status-format).

**Sync**
:  Writing your changes (deleted messages, flag changes, new mail) back to the mailbox file or remote server.
   This happens automatically when you leave a mailbox, or you can trigger it manually.

---

## T

**Tag**
:  Marking one or more messages so you can perform an action on all of them at once — for example, deleting, moving, or saving a group of tagged messages.

**Thread (Threading)**
:  A group of related messages linked together as a conversation.
   NeoMutt builds threads using the *In-Reply-To* and *References* header fields, and displays them as a tree in the index.

**TLS / SSL (Transport Layer Security / Secure Sockets Layer)**
:  Protocols that encrypt the connection between NeoMutt and a mail server, protecting your username, password, and messages from being read in transit.
   TLS is the modern successor to SSL.

---

## U

**URL**
:  An address used to describe a server connection, for example `imaps://user@mail.example.com/INBOX` or `smtp://user@mail.example.com:587`.

**UTF-8**
:  The most common character encoding for email and the web.
   It can represent virtually every character in every language.

---

## V

**Virtual Mailbox**
:  A mailbox whose contents are generated dynamically by a search query rather than by reading a single folder.
   Used with *Notmuch* to show messages matching specific tags or search terms.

---

## W

**Weed (Weeding)**
:  Filtering out header lines you do not want to see.
   NeoMutt's [`:ignore`](cmd-ignore) command hides headers, and [`:unignore`](cmd-unignore) lets specific ones through.
   For example, the default configuration hides most headers and only shows `From:`, `To:`, `Cc:`, `Subject:` and `Date:`.

---

## Synonyms and Variant Names

Some terms have more than one name.
This table helps you find the right glossary entry.

| You may see              | See glossary entry       |
|--------------------------|--------------------------|
| Config variable, Setting | Config Option            |
| Draft                    | Postpone                 |
| Email                    | Message                  |
| Format string            | Expando                  |
| Folder                   | Mailbox                  |
| GPG                      | GnuPG                    |
| muttrc, neomuttrc        | Config File              |
| PGP                      | OpenPGP                  |
| Regexp                   | Regex                    |
| SMIME                    | S/MIME                   |
| SSL                      | TLS / SSL                |

