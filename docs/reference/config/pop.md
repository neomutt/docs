---
title: POP3 Options
description: POP3 protocol configuration variables for NeoMutt
keywords: pop_auth_try_all, pop_authenticators, pop_check_interval, pop_delete, pop_host, pop_last, pop_oauth_refresh_command, pop_pass, pop_reconnect, pop_user
---

# POP3 Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

--------------------------------------------------------------------------------

(pop-authenticators)=
## `$pop_authenticators`

- **Type:** string list
- **Notes:** Colon-separated
- **Default:** (empty)
    ```
    set pop_authenticators = ""
    ```

This is a colon-separated list of authentication methods NeoMutt may attempt to use to log in to an POP server, in the order NeoMutt should try them.
Authentication methods are either "user", "apop" or any SASL mechanism, e.g.
"digest-md5", "gssapi" or "cram-md5".
This option is case-insensitive.
If this option is _unset_ (the default) NeoMutt will try all available methods, in order from most-secure to least-secure.

Example:

```neomuttrc
set pop_authenticators = "digest-md5:apop:user"
```

--------------------------------------------------------------------------------

(pop-auth-try-all)=
## `$pop_auth_try_all`

- **Type:** boolean
- **Default:**
    ```neomuttrc
    set pop_auth_try_all = yes
    ```

If _set_, NeoMutt will try all available authentication methods.
When _unset_, NeoMutt will only fall back to other authentication methods if the previous methods are unavailable.
If a method is available but authentication fails, NeoMutt will not connect to the POP server.

--------------------------------------------------------------------------------

(pop-check-interval)=
## `$pop_check_interval`

- **Type:** number
- **Notes:** Not negative
- **Default:**
    ```neomuttrc
    set pop_check_interval = 60
    ```

This variable configures how often (in seconds) NeoMutt should look for new mail in the currently selected mailbox if it is a POP mailbox.

--------------------------------------------------------------------------------

(pop-delete)=
## `$pop_delete`

- **Type:** quad-option
- **Default:**
    ```neomuttrc
    set pop_delete = ask-no
    ```

If _set_, NeoMutt will delete successfully downloaded messages from the POP server when using the `$<fetch-mail>` function.
When _unset_, NeoMutt will download messages but also leave them on the POP server.

--------------------------------------------------------------------------------

(pop-host)=
## `$pop_host`

- **Type:** string
- **Default:** (empty)
    ```
    set pop_host = ""
    ```

The name of your POP server for the `$<fetch-mail>` function.
You can also specify an alternative port, username and password, i.e.:

```
[pop[s]://][username[:password]@]popserver[:port] 
```

where "[...]" denotes an optional part.

--------------------------------------------------------------------------------

(pop-last)=
## `$pop_last`

- **Type:** boolean
- **Default:**
    ```neomuttrc
    set pop_last = no
    ```

If this variable is _set_, NeoMutt will try to use the "`LAST`" POP command for retrieving only unread messages from the POP server when using the `$<fetch-mail>` function.

--------------------------------------------------------------------------------

(pop-oauth-refresh-command)=
## `$pop_oauth_refresh_command`

- **Type:** command (string)
- **Notes:** Sensitive
- **Default:** (empty)
    ```
    set pop_oauth_refresh_command = ""
    ```

The command to run to generate an OAUTH refresh token for authorizing your connection to your POP server.
This command will be run on every connection attempt that uses the OAUTHBEARER authentication mechanism.
See "$oauth" for details.

--------------------------------------------------------------------------------

(pop-pass)=
## `$pop_pass`

- **Type:** string
- **Notes:** Sensitive
- **Default:** (empty)
    ```
    set pop_pass = ""
    ```

Specifies the password for your POP account.
If _unset_, NeoMutt will prompt you for your password when you open a POP mailbox.

**Warning**: you should only use this option when you are on a fairly secure machine, because the superuser can read your neomuttrc even if you are the only one who can read the file.

--------------------------------------------------------------------------------

(pop-reconnect)=
## `$pop_reconnect`

- **Type:** quad-option
- **Default:**
    ```neomuttrc
    set pop_reconnect = ask-yes
    ```

Controls whether or not NeoMutt will try to reconnect to the POP server if the connection is lost.

--------------------------------------------------------------------------------

(pop-user)=
## `$pop_user`

- **Type:** string
- **Notes:** Sensitive
- **Default:** (empty)
    ```
    set pop_user = ""
    ```

Your login name on the POP server.

This variable defaults to your user name on the local machine.

