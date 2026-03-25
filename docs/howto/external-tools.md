---
title: Integrate External Tools
description: Connect NeoMutt with external tools like urlview, msmtp, offlineimap, notmuch, and HTML renderers
keywords: external tools, urlview, urlscan, msmtp, sendmail, offlineimap, mbsync, isync, notmuch, mailcap, w3m, lynx, pipe-message, macro, query_command, calendar, khal, calcurse
---

# Integrate External Tools

## Prerequisites

1. Install the external tool you want to use.
2. Confirm NeoMutt is working with a basic configuration.

## Extracting URLs with urlview / urlscan

1. Install urlview or urlscan.
2. Add a macro to pipe the current message to the tool:

```neomuttrc
macro index \cb "<pipe-message>urlview<Enter>" "Open URLs with urlview"
macro pager \cb "<pipe-message>urlview<Enter>" "Open URLs with urlview"
```

3. Open a message with URLs and press `Ctrl-b`.

Expected result: a list of URLs appears and you can open one in your browser.

References: urlview man page and urlscan documentation.

## Contact Management with abook or khard

1. Configure your address source.
2. Set `query_command` to the external tool:

```neomuttrc
set query_command = "abook --mutt-query %s"
```

3. Use `Q` in the index menu or `^T` at an address prompt to query.

Expected result: the query menu shows matches from your address book.

See [How to Set Up Address Book Integration](address-book).

## Sending Mail with msmtp

1. Install and configure msmtp.
2. Tell NeoMutt to use it as the sendmail backend:

```neomuttrc
set sendmail = "msmtp"
```

3. Send a test message.

Expected result: mail is delivered by msmtp using its own configuration.

References: msmtp documentation.

## Offline IMAP with offlineimap / mbsync

1. Configure offlineimap or mbsync (isync) to sync your IMAP account to a local Maildir.
2. Point NeoMutt at the local folder:

```neomuttrc
set folder = "~/Mail"
set spoolfile = "+INBOX"
```

3. Run your sync tool, then open the mailbox in NeoMutt.

Expected result: NeoMutt reads from the local Maildir while your sync tool keeps it updated.

References: offlineimap and isync documentation.

## Full-Text Search with notmuch

1. Install and configure notmuch.
2. Follow the Notmuch setup steps in NeoMutt.

See [How to Use Notmuch](notmuch).

## Rendering HTML Email with w3m / lynx / elinks

1. Install a text-mode browser.
2. Add a mailcap entry to render HTML:

```
text/html; lynx -dump %s; copiousoutput
```

3. View an HTML message in NeoMutt.

Expected result: HTML is rendered as readable text in the pager.

References: mailcap documentation and the w3m, lynx, and elinks projects.

## Calendar Integration (khal, calcurse)

1. Save a calendar invite (ICS file) from the attachment menu.
2. Open or import it with your calendar tool:

- khal: https://khal.readthedocs.io/
- calcurse: https://calcurse.org/

Expected result: the invite appears in your calendar tool.

## Custom Processing with `pipe-message`

1. Create a script or command to process messages.
2. Bind a key to pipe the current message:

```neomuttrc
macro index,pager ,p "<pipe-message>~/bin/mail-filter<Enter>" "Pipe message to filter"
```

3. Press `,p` while viewing a message.

Expected result: the message is passed to your command for processing.
