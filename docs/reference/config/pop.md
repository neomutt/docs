---
title: POP3 Options
description: Configuration variables for POP3 server connections, authentication, polling, and message retrieval.
keywords: neomutt, pop3, pop, pop_host, pop_user, pop_pass, pop_authenticators, pop_check_interval, pop_delete, oauth, remote mail, fetch mail
---

(ref-cfg-pop)=
# POP3 Options

(cfg-pop-authenticators)=
## `$pop_authenticators`

:Type: [String List](type-slist)
:Notes: [Colon-separated](type-slist)
:Default: (empty)
    ```neomuttrc
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

(cfg-pop-auth-try-all)=
## `$pop_auth_try_all`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set pop_auth_try_all = yes
    ```

If _set_, NeoMutt will try all available authentication methods.
When _unset_, NeoMutt will only fall back to other authentication methods if the previous methods are unavailable.
If a method is available but authentication fails, NeoMutt will not connect to the POP server.

--------------------------------------------------------------------------------

(cfg-pop-check-interval)=
## `$pop_check_interval`

:Type: [Number](type-number)
:Notes: [Not Negative](type-general)
:Default:
    ```neomuttrc
    set pop_check_interval = 60
    ```

This variable configures how often (in seconds) NeoMutt should look for new mail in the currently selected mailbox if it is a POP mailbox.

--------------------------------------------------------------------------------

(cfg-pop-delete)=
## `$pop_delete`

:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set pop_delete = ask-no
    ```

If _set_, NeoMutt will delete successfully downloaded messages from the POP server when using the [`<fetch-mail>`](ref-fn-index) function.
When _unset_, NeoMutt will download messages but also leave them on the POP server.

--------------------------------------------------------------------------------

(cfg-pop-host)=
## `$pop_host`

:Type: [String](type-string)
:Default: (empty)
    ```neomuttrc
    set pop_host = ""
    ```

The name of your POP server for the [`<fetch-mail>`](ref-fn-index) function.
You can also specify an alternative port, username and password, i.e.:

```
[pop[s]://][username[:password]@]popserver[:port]
```

where "[...]" denotes an optional part.

--------------------------------------------------------------------------------

(cfg-pop-last)=
## `$pop_last`

:Type: [Boolean](type-bool)
:Default:
    ```neomuttrc
    set pop_last = no
    ```

If this variable is _set_, NeoMutt will try to use the "`LAST`" POP command for retrieving only unread messages from the POP server when using the [`<fetch-mail>`](ref-fn-index) function.

--------------------------------------------------------------------------------

(cfg-pop-oauth-refresh-command)=
## `$pop_oauth_refresh_command`

:Type: [Command (String)](type-string)
:Notes: [Sensitive](type-general)
:Default: (empty)
    ```neomuttrc
    set pop_oauth_refresh_command = ""
    ```

The command to run to generate an OAUTH refresh token for authorizing your connection to your POP server.
This command will be run on every connection attempt that uses the OAUTHBEARER authentication mechanism.
See "$oauth" for details.

--------------------------------------------------------------------------------

(cfg-pop-pass)=
## `$pop_pass`

:Type: [String](type-string)
:Notes: [Sensitive](type-general)
:Default: (empty)
    ```neomuttrc
    set pop_pass = ""
    ```

Specifies the password for your POP account.
If _unset_, NeoMutt will prompt you for your password when you open a POP mailbox.

:::{warning}
Only use this option when you are on a fairly secure machine, because the superuser can read your neomuttrc even if you are the only one who can read the file.
:::

--------------------------------------------------------------------------------

(cfg-pop-reconnect)=
## `$pop_reconnect`

:Type: [Quad-Option](type-quad)
:Default:
    ```neomuttrc
    set pop_reconnect = ask-yes
    ```

Controls whether or not NeoMutt will try to reconnect to the POP server if the connection is lost.

--------------------------------------------------------------------------------

(cfg-pop-user)=
## `$pop_user`

:Type: [String](type-string)
:Notes: [Sensitive](type-general)
:Default: (empty)
    ```neomuttrc
    set pop_user = ""
    ```

Your login name on the POP server.

This variable defaults to your user name on the local machine.

