---
title: Setting Up pass and GPG for Email Passwords
description: Generate a GPG key, initialise the pass password store, and use it to supply credentials to NeoMutt, mbsync, and msmtp
keywords: neomutt, pass, password-store, gpg, gnupg, password, credentials, security, tutorial, encryption, gpg-agent
diataxis_type: tutorial
---

# Setting Up pass and GPG for Email Passwords

This tutorial walks you through creating a GPG key, initialising the `pass` password manager, storing your email password, and using it from NeoMutt and related tools.

If you only need a quick reference on the different password options NeoMutt supports, see [Password Manager](../howto/password-manager).

## Why Use pass?

Storing passwords in plain text config files is risky.
`pass` (the standard Unix password manager) stores each password as a GPG-encrypted file.
NeoMutt, mbsync, and msmtp can all call `pass` to retrieve credentials at runtime, so your password never appears in any config file.

## Prerequisites

1. `gpg` (GnuPG) installed.
2. `pass` installed.

On Fedora/RHEL:

```sh
sudo dnf install gnupg2 pass
```

On Debian/Ubuntu:

```sh
sudo apt install gnupg pass
```

On macOS:

```sh
brew install gnupg pass
```

## Generate a GPG Key

If you already have a GPG key, skip to the next section.

1. Generate a new key:

```sh
gpg --generate-key
```

2. Follow the prompts: enter your name and email address.
   Accept the defaults for key type and expiry unless you have a reason to change them.

3. Confirm the key exists:

```sh
gpg --list-keys --keyid-format short
```

Expected result: you see your new key with your name and email.
Note the short key ID or email — you'll use it to initialise `pass`.

## Initialise the Password Store

1. Initialise `pass` with your GPG key:

```sh
pass init "you@example.com"
```

Use the email address or key ID from the previous step.

Expected result: `pass` creates `~/.password-store/` and prints a confirmation.

## Store Your Email Password

1. Insert your mail account password:

```sh
pass insert mail/you@example.com
```

2. Type the password when prompted (twice to confirm).

3. Verify it was stored:

```sh
pass mail/you@example.com
```

Expected result: your password is printed to the terminal.
GPG may prompt for your passphrase the first time.

### Alternative: Import from a File

If you have the password in a file, you can pipe it in:

```sh
cat /tmp/mypassword | pass insert -e mail/you@example.com
```

Delete the temporary file afterwards.

## Use pass in NeoMutt

1. Add these lines to your `neomuttrc`:

```neomuttrc
set imap_pass = "`pass mail/you@example.com`"
set smtp_pass = "`pass mail/you@example.com`"
```

2. Start NeoMutt.

Expected result: NeoMutt retrieves the password from `pass` and authenticates without prompting.

## Use pass in mbsync

In your `~/.mbsyncrc`, set the `PassCmd`:

```
PassCmd "pass mail/you@example.com"
```

Expected result: mbsync retrieves the password from `pass` when syncing.

See [Setting Up Offline Email with mbsync](mbsync-setup) for the full mbsync tutorial.

## Use pass in msmtp

In your msmtp config, set `passwordeval`:

```
passwordeval "pass mail/you@example.com"
```

Expected result: msmtp retrieves the password from `pass` when sending.

See [Setting Up msmtp for Sending](msmtp-setup) for the full msmtp tutorial.

## GPG Agent and Passphrase Caching

By default, `gpg-agent` caches your GPG passphrase for a short time so you aren't prompted repeatedly.
You can adjust the timeout in `~/.gnupg/gpg-agent.conf`:

```
default-cache-ttl 3600
max-cache-ttl 7200
```

After editing, reload the agent:

```sh
gpg-connect-agent reloadagent /bye
```

Expected result: the passphrase is cached for longer between prompts.

## Troubleshooting

**`pass` prints nothing or errors with "No secret key":**
Check that `gpg --list-secret-keys` shows your key.
If you moved machines, you need to import your private key first.

**NeoMutt hangs at startup:**
The GPG agent may be waiting for a passphrase in a pinentry dialog you can't see.
Set `GPG_TTY` in your shell profile:

```sh
export GPG_TTY=$(tty)
```

**Wrong password retrieved:**
Verify the `pass` path matches exactly between your config files.
Run `pass mail/you@example.com` manually to confirm.

## Next Steps

- "I want to set up offline email." See [Setting Up Offline Email with mbsync](mbsync-setup).
- "I want to set up sending." See [Setting Up msmtp for Sending](msmtp-setup).
- "I want to see all password options." See [Password Manager](../howto/password-manager).
