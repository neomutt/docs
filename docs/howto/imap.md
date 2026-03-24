---
title: How to Set Up IMAP
description: Configure NeoMutt to work with remote IMAP mailboxes
keywords: imap, remote mailbox, imap_user, imap_pass, imap_authenticators, folder browser, subscriptions
---

# How to Set Up IMAP

NeoMutt has IMAP support and has the ability to work with folders located on a remote IMAP server.

You can access the remote inbox by selecting the folder by its URL (see **URL syntax** for details) using the `imap` or `imaps` protocol. Alternatively, a pine-compatible notation is also supported, i.e. `{[username@]imapserver[:port][/ssl]}path/to/folder`

Note that not all servers use `/` as the hierarchy separator. NeoMutt should correctly notice which separator is being used by the server and convert paths accordingly.

## Managing Subscriptions

The IMAP protocol has a subscription feature where the server manages a list of subscribed folders. To add or remove a folder to the list of subscribed folders use the commands:

```neomuttrc
subscribe-to <imap-folder-uri>
unsubscribe-from <imap-folder-uri>
```

*imap-folder-uri* must be an IMAP URI, from which the server and the folder is derived, e.g.

```neomuttrc
subscribe-to imaps://mail.example.org/inbox
```

Instead of the above commands you can also use the `<subscribe>` and `<unsubscribe>` functions of the browser (default keys `s` and `u`) to subscribe to or unsubscribe from a folder while browsing the folders on the IMAP server. The browser can be instructed to only display the folders you are subscribed to with the `<toggle-subscribed>` function. See also the `$imap_list_subscribed` variable.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** IMAP folder browser with subscription toggle

**Description:** The NeoMutt folder browser connected to an IMAP server, with `<toggle-subscribed>` active so only subscribed folders are shown. Several folders are listed with the `s`/`u` subscribe/unsubscribe key bindings available in the help bar.

**Highlights:** The subscribed-only filter in effect, and the `s`/`u` key bindings for managing folder subscriptions directly from the browser.
:::

Because the list of subscribed folders is managed by the IMAP server, NeoMutt can also ask the server for that list. If `$imap_check_subscribed` is set, NeoMutt will do that and add those folders to its mailboxes list just as if you had used the `mailboxes` command on each of them, so that these folders get checked periodically for new mail.

## Tuning Mail Polling

Polling for new mail on an IMAP server can cause noticeable delays. So, you'll want to carefully tune the `$mail_check` and `$timeout` variables. Reasonable values are:

```neomuttrc
set mail_check=90
set timeout=15
```

with relatively good results even over slow modem lines.

:::{note}
If you are using mbox as the mail store on UW servers prior to v12.250, the server has been reported to disconnect a client if another client selects the same folder.
:::

## The IMAP Folder Browser

As of version 1.2, NeoMutt supports browsing mailboxes on an IMAP server. This is mostly the same as the local file browser, with the following differences:

- In lieu of file permissions, NeoMutt displays the string "IMAP", possibly followed by the symbol "+", indicating that the entry contains both messages and subfolders. On Cyrus-like servers folders will often contain both messages and subfolders. A mailbox name with a trailing delimiter (usually `/` or `.`) indicates subfolders.

- For the case where an entry can contain both messages and subfolders, the selection key (bound to `enter` by default) will choose to descend into the subfolder view. If you wish to view the messages in that folder, you must use `view-file` instead (bound to `space` by default).

- You can create, delete and rename mailboxes with the `<create-mailbox>`, `<delete-mailbox>`, and `<rename-mailbox>` commands (default bindings: `C`, `d` and `r`, respectively). You may also `<subscribe>` and `<unsubscribe>` to mailboxes (normally these are bound to `s` and `u`, respectively).

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** IMAP folder browser display

**Description:** The NeoMutt IMAP folder browser showing a list of remote mailboxes. Entries display "IMAP" in the permissions column, some with a "+" indicator showing they contain both messages and subfolders. At least one folder name has a trailing hierarchy separator (e.g., `/` or `.`).

**Highlights:** The "IMAP+" indicator for folders containing both messages and subfolders, the hierarchy separator on folder names, and the key bindings for `<create-mailbox>` (C), `<delete-mailbox>` (d), and `<rename-mailbox>` (r) shown in the help bar.
:::

## Authentication

NeoMutt supports four authentication methods with IMAP servers: SASL, GSSAPI, CRAM-MD5, and LOGIN. There is also support for the pseudo-protocol ANONYMOUS, which allows you to log in to a public IMAP server without having an account. To use ANONYMOUS, simply make your username blank or "anonymous".

SASL is a special super-authenticator, which selects among several protocols (including GSSAPI, CRAM-MD5, ANONYMOUS, and DIGEST-MD5) the most secure method available on your host and the server. Using some of these methods (including DIGEST-MD5 and possibly GSSAPI), your entire session will be encrypted and invisible to those teeming network snoops. It is the best option if you have it. To use it, you must have the Cyrus SASL library installed on your system and compile NeoMutt with the *--with-sasl* flag.

NeoMutt will try whichever methods are compiled in and available on the server, in the following order: SASL, ANONYMOUS, GSSAPI, CRAM-MD5, LOGIN.

There are a few variables which control authentication:

- `$imap_user` – controls the username under which you request authentication on the IMAP server, for all authenticators. This is overridden by an explicit username in the mailbox path (i.e. by using a mailbox name of the form `{user@host}`).

- `$imap_pass` – a password which you may preset, used by all authentication methods where a password is needed.

- `$imap_authenticators` – a colon-delimited list of IMAP authentication methods to try, in the order you wish to try them. If specified, this overrides NeoMutt's default (attempt everything, in the order listed above).
