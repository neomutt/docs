---
title: SMTP Options
description: SMTP protocol configuration variables for NeoMutt
keywords: smtp_authenticators, smtp_oauth_refresh_command, smtp_pass, smtp_url, smtp_user
---

# SMTP Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

(smtp-authenticators)=
## `$smtp_authenticators`

- **Type:** string list
- **Default:** (empty)

This is a colon-separated list of authentication methods NeoMutt may
attempt to use to log in to an SMTP server, in the order NeoMutt should
try them.  Authentication methods are any SASL mechanism, e.g. "plain",
"digest-md5", "gssapi" or "cram-md5".
This option is case-insensitive. If it is "unset"
(the default) NeoMutt will try all available methods, in order from
most-secure to least-secure. Support for the "plain" mechanism is
bundled; other mechanisms are provided by an external SASL library (look
for '+sasl' in the output of neomutt -v).

Example:


```neomuttrc
set smtp_authenticators="digest-md5:cram-md5"
```


(smtp-oauth-refresh-command)=
## `$smtp_oauth_refresh_command`

- **Type:** command
- **Default:** (empty)

The command to run to generate an OAUTH refresh token for
authorizing your connection to your SMTP server.  This command will be
run on every connection attempt that uses the OAUTHBEARER or XOAUTH2
authentication mechanisms.  See [OAuth](../../howto/oauth.md) for details.

(smtp-pass)=
## `$smtp_pass`

- **Type:** string
- **Default:** (empty)

Specifies the password for your SMTP account.  If *unset*, NeoMutt will
prompt you for your password when you first send mail via SMTP.
See [$smtp_url](#smtp-url) to configure NeoMutt to send mail via SMTP.

**Warning**: you should only use this option when you are on a
fairly secure machine, because the superuser can read your neomuttrc even
if you are the only one who can read the file.

(smtp-url)=
## `$smtp_url`

- **Type:** string
- **Default:** (empty)

Defines the SMTP smarthost where sent messages should relayed for
delivery. This should take the form of an SMTP URL, e.g.:


```
smtp[s]://[user[:pass]@]host[:port]
```


where "[...]" denotes an optional part.
Setting this variable overrides the value of the [$sendmail](#sendmail)
variable.

Also see [$write_bcc](#write-bcc).

(smtp-user)=
## `$smtp_user`

- **Type:** string
- **Default:** (empty)

The username for the SMTP server.

This variable defaults to your user name on the local machine.
