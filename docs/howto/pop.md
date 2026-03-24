---
title: How to Set Up POP3
description: Configure NeoMutt to access remote POP3 mailboxes and fetch mail
keywords: pop3, remote mailbox, fetch mail, pop_host, pop_check_interval
---

# How to Set Up POP3

NeoMutt has POP3 support and has the ability to work with mailboxes located on a remote POP3 server and fetch mail for local browsing.

Remote POP3 servers can be accessed using URLs with the `pop` protocol for unencrypted and `pops` for encrypted communication. 
See **URL syntax** for details.

## Remote POP3 Mailboxes

Polling for new mail is more expensive over POP3 than locally. 
For this reason the frequency at which NeoMutt will check for mail remotely can be controlled by the `$pop_check_interval` variable, which defaults to every 60 seconds.

Due to limitations in POP3, this method doesn't allow for some features such as editing messages, changing their flags or even deleting them. 
However, using **header caching** and **body caching**, NeoMutt simulates the new/old/read flags as well as flagged and replied. 
NeoMutt applies some logic on top of remote messages but cannot change them so that modifications of flags are lost when messages are downloaded from the POP3 server (either by NeoMutt or other tools).

1. Set the POP3 password (optionally reuse the SMTP password):

   ```neomuttrc
   # If an SMTP password has been set, use this to set the same password for POP3.
   set pop_pass=$smtp_pass
   ```

2. Set the POP3 server and user:

   ```neomuttrc
   set pop_host="pops://user@example.com"
   ```

3. Use the remote server as the mailbox:

   ```neomuttrc
   set folder=$pop_host
   set spool_file=+
   ```

## Fetching Mail from a POP3 Server

Another way to access your POP3 mail is the `<fetch-mail>` function (default: G). 
It allows you to connect to `$pop_host`, fetch all your new mail and place it in the local `$spool_file`. 
After this point, NeoMutt runs exactly as if the mail had always been local. 
The `<fetch-mail>` function will ask whether you want to delete the messages on the remote server, leaving only your local copies.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** POP3 fetch-mail prompt

**Description:** The NeoMutt index after pressing `G` to fetch mail from a POP3 server. 
The prompt at the bottom of the screen asks the user whether to delete messages from the remote server, with newly fetched messages visible in the index.

**Highlights:** The delete confirmation prompt at the bottom of the screen and the newly fetched messages appearing in the message index.
:::

:::{note}
If you only need to fetch all messages to a local mailbox, you should consider using a specialized program, such as `fetchmail(1)`, `getmail(1)` or similar.
:::

1. Set the local spool file (initialize it as an empty file if it doesn't exist):

   ```neomuttrc
   set spool_file="/home/user/.mailspool"
   ```

2. Set the POP3 server and user from which to fetch messages:

   ```neomuttrc
   set pop_host="pops://user@example.com"
   ```

3. Press `G` in the index to fetch mail.
