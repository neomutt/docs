---
title: IMAP Options
description: IMAP protocol configuration variables for NeoMutt
keywords: imap_authenticators, imap_check_subscribed, imap_condstore, imap_deflate, imap_delim_chars, imap_fetch_chunk_size, imap_headers, imap_idle, imap_keep_alive, imap_list_subscribed, imap_login, imap_oauth_refresh_command, imap_pass, imap_passive, imap_peek, imap_pipeline_depth, imap_poll_timeout, imap_qresync, imap_rfc5161, imap_send_id, imap_server_noise, imap_user
---

# IMAP Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

--------------------------------------------------------------------------------

(imap-authenticators)=
## `$imap_authenticators`

- **Type:** string list
- **Notes:** Colon-separated
- **Default:** (empty)
    ```
    set imap_authenticators = ""
    ```

This is a colon-separated list of authentication methods NeoMutt may attempt to use to log in to an IMAP server, in the order NeoMutt should try them.
Authentication methods are either "login" or the right side of an IMAP "AUTH=xxx" capability string, e.g.
"digest-md5", "gssapi" or "cram-md5".
This option is case-insensitive.
If it's _unset_ (the default) NeoMutt will try all available methods, in order from most-secure to least-secure.

Example:
```
set imap_authenticators="gssapi:cram-md5:login" 
```

**Note:** NeoMutt will only fall back to other authentication methods if the previous methods are unavailable.
If a method is available but authentication fails, NeoMutt will not connect to the IMAP server.

--------------------------------------------------------------------------------

(imap-check-subscribed)=
## `$imap_check_subscribed`

- **Type:** boolean
- **Default:**
    ```
    set imap_check_subscribed = no
    ```

When _set_, NeoMutt will fetch the set of subscribed folders from your server whenever a mailbox is **selected**, and add them to the set of mailboxes it polls for new mail just as if you had issued individual "$mailboxes" commands.

--------------------------------------------------------------------------------

(imap-condstore)=
## `$imap_condstore`

- **Type:** boolean
- **Default:**
    ```
    set imap_condstore = no
    ```

When _set_, NeoMutt will use the CONDSTORE extension (RFC7162)
if advertised by the server.
NeoMutt's current implementation is basic, used only for initial message fetching and flag updates.

For some IMAP servers, enabling this will slightly speed up downloading initial messages.
Unfortunately, Gmail is not one those, and displays worse performance when enabled.
Your mileage may vary.

--------------------------------------------------------------------------------

(imap-deflate)=
## `$imap_deflate`

- **Type:** boolean
- **Default:**
    ```
    set imap_deflate = yes
    ```

When _set_, NeoMutt will use the COMPRESS=DEFLATE extension (RFC4978)
if advertised by the server.

In general a good compression efficiency can be achieved, which speeds up reading large mailboxes also on fairly good connections.

--------------------------------------------------------------------------------

(imap-delim-chars)=
## `$imap_delim_chars`

- **Type:** string
- **Default:**
    ```
    set imap_delim_chars = "/."
    ```

This contains the list of characters that NeoMutt will use as folder separators for IMAP paths, when no separator is provided on the IMAP connection.

--------------------------------------------------------------------------------

(imap-fetch-chunk-size)=
## `$imap_fetch_chunk_size`

- **Type:** number (long)
- **Notes:** Not negative
- **Default:**
    ```
    set imap_fetch_chunk_size = 0
    ```

When set to a value greater than 0, new headers will be downloaded in groups of this many headers per request.
If you have a very large mailbox, this might prevent a timeout and disconnect when opening the mailbox, by sending a FETCH per set of this many headers, instead of a single FETCH for all new headers.

--------------------------------------------------------------------------------

(imap-headers)=
## `$imap_headers`

- **Type:** string
- **Default:** (empty)
    ```
    set imap_headers = ""
    ```

NeoMutt requests these header fields in addition to the default headers ("Date:", "From:", "Sender:", "Subject:", "To:", "Cc:", "Message-Id:", "References:", "Content-Type:", "Content-Description:", "In-Reply-To:", "Reply-To:", "Lines:", "List-Post:", "X-Label:") from IMAP servers before displaying the index menu.
You may want to add more headers for spam detection.

**Note:** This is a space separated list, items should be uppercase and not contain the colon, e.g.
"X-BOGOSITY X-SPAM-STATUS" for the "X-Bogosity:" and "X-Spam-Status:" header fields.

--------------------------------------------------------------------------------

(imap-idle)=
## `$imap_idle`

- **Type:** boolean
- **Default:**
    ```
    set imap_idle = no
    ```

When _set_, NeoMutt will attempt to use the IMAP IDLE extension to check for new mail in the current mailbox.
Some servers (dovecot was the inspiration for this option) react badly to NeoMutt's implementation.
If your connection seems to freeze up periodically, try unsetting this.

--------------------------------------------------------------------------------

(imap-keep-alive)=
## `$imap_keep_alive`

- **Type:** number
- **Notes:** Not negative
- **Default:**
    ```
    set imap_keep_alive = 300
    ```

This variable specifies the maximum amount of time in seconds that NeoMutt will wait before polling open IMAP connections, to prevent the server from closing them before NeoMutt has finished with them.
The default is well within the RFC-specified minimum amount of time (30 minutes) before a server is allowed to do this, but in practice the RFC does get violated every now and then.
Reduce this number if you find yourself getting disconnected from your IMAP server due to inactivity.

--------------------------------------------------------------------------------

(imap-list-subscribed)=
## `$imap_list_subscribed`

- **Type:** boolean
- **Default:**
    ```
    set imap_list_subscribed = no
    ```

This variable configures whether IMAP folder browsing will look for only subscribed folders or all folders.
This can be toggled in the IMAP browser with the `<toggle-subscribed>` function.

--------------------------------------------------------------------------------

(imap-login)=
## `$imap_login`

- **Type:** string
- **Notes:** Sensitive
- **Default:** (empty)
    ```
    set imap_login = ""
    ```

Your login name on the IMAP server.

This variable defaults to the value of $$imap_user.

--------------------------------------------------------------------------------

(imap-oauth-refresh-command)=
## `$imap_oauth_refresh_command`

- **Type:** command (string)
- **Notes:** Sensitive
- **Default:** (empty)
    ```
    set imap_oauth_refresh_command = ""
    ```

The command to run to generate an OAUTH refresh token for authorizing your connection to your IMAP server.
This command will be run on every connection attempt that uses the OAUTHBEARER or XOAUTH2 authentication mechanisms.
See "$oauth" for details.

--------------------------------------------------------------------------------

(imap-pass)=
## `$imap_pass`

- **Type:** string
- **Notes:** Sensitive
- **Default:** (empty)
    ```
    set imap_pass = ""
    ```

Specifies the password for your IMAP account.
If _unset_, NeoMutt will prompt you for your password when you invoke the `<imap-fetch-mail>`
function or try to open an IMAP folder.

**Warning**: you should only use this option when you are on a fairly secure machine, because the superuser can read your neomuttrc even if you are the only one who can read the file.

--------------------------------------------------------------------------------

(imap-passive)=
## `$imap_passive`

- **Type:** boolean
- **Default:**
    ```
    set imap_passive = yes
    ```

When _set_, NeoMutt will not open new IMAP connections to check for new mail.
NeoMutt will only check for new mail over existing IMAP connections.
This is useful if you don't want to be prompted for user/password pairs on NeoMutt invocation, or if opening the connection is slow.

--------------------------------------------------------------------------------

(imap-peek)=
## `$imap_peek`

- **Type:** boolean
- **Default:**
    ```
    set imap_peek = yes
    ```

When _set_, NeoMutt will avoid implicitly marking your mail as read whenever you fetch a message from the server.
This is generally a good thing, but can make closing an IMAP folder somewhat slower.
This option exists to appease speed freaks.

--------------------------------------------------------------------------------

(imap-pipeline-depth)=
## `$imap_pipeline_depth`

- **Type:** number
- **Notes:** Not negative
- **Default:**
    ```
    set imap_pipeline_depth = 15
    ```

Controls the number of IMAP commands that may be queued up before they are sent to the server.
A deeper pipeline reduces the amount of time NeoMutt must wait for the server, and can make IMAP servers feel much more responsive.
But not all servers correctly handle pipelined commands, so if you have problems you might want to try setting this variable to 0.

**Note:** Changes to this variable have no effect on open connections.

--------------------------------------------------------------------------------

(imap-poll-timeout)=
## `$imap_poll_timeout`

- **Type:** number
- **Notes:** Not negative
- **Default:**
    ```
    set imap_poll_timeout = 15
    ```

This variable specifies the maximum amount of time in seconds that NeoMutt will wait for a response when polling IMAP connections for new mail, before timing out and closing the connection.
Set to 0 to disable timing out.

--------------------------------------------------------------------------------

(imap-qresync)=
## `$imap_qresync`

- **Type:** boolean
- **Default:**
    ```
    set imap_qresync = no
    ```

When _set_, NeoMutt will use the QRESYNC extension (RFC7162)
if advertised by the server.
NeoMutt's current implementation is basic, used only for initial message fetching and flag updates.

Note: this feature is currently experimental.
If you experience strange behavior, such as duplicate or missing messages please file a bug report to let us know.

--------------------------------------------------------------------------------

(imap-rfc5161)=
## `$imap_rfc5161`

- **Type:** boolean
- **Default:**
    ```
    set imap_rfc5161 = yes
    ```

When _set_, NeoMutt will use the IMAP ENABLE extension (RFC5161) to select CAPABILITIES.
Some servers (notably Coremail System IMap Server) do not properly respond to ENABLE commands, which might cause NeoMutt to hang.
If your connection seems to freeze at login, try unsetting this.
See also https://github.com/neomutt/neomutt/issues/1689 

--------------------------------------------------------------------------------

(imap-send-id)=
## `$imap_send_id`

- **Type:** boolean
- **Default:**
    ```
    set imap_send_id = no
    ```

When _set_, NeoMutt will send an IMAP ID command (RFC2971) to the server when logging in if advertised by the server.
This command provides information about the IMAP client, such as "NeoMutt" and the current version.

--------------------------------------------------------------------------------

(imap-server-noise)=
## `$imap_server_noise`

- **Type:** boolean
- **Default:**
    ```
    set imap_server_noise = yes
    ```

When _set_, NeoMutt will display warning messages from the IMAP server as error messages.
Since these messages are often harmless, or generated due to configuration problems on the server which are out of the users' hands, you may wish to suppress them at some point.

--------------------------------------------------------------------------------

(imap-user)=
## `$imap_user`

- **Type:** string
- **Notes:** Sensitive
- **Default:** (empty)
    ```
    set imap_user = ""
    ```

The name of the user whose mail you intend to access on the IMAP server.

This variable defaults to your user name on the local machine.

