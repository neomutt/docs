# How to Use a Password Manager

## Prerequisites

1. Install the password tool you plan to use (`pass`, GPG, GNOME Keyring, or macOS Keychain).
2. Confirm NeoMutt can access your mail servers without hard-coded passwords.

## Using `pass` (password-store)

1. Store your password in `pass` (see the pass documentation).
2. Reference it from NeoMutt:

```neomuttrc
set imap_pass = "`pass show mail/example`"
set smtp_pass = "`pass show mail/example`"
```

Expected result: NeoMutt retrieves credentials from `pass` at startup.

## Using GPG-Encrypted Password Files

1. Encrypt a small file with GPG that contains only the password.
2. Reference it with backticks:

```neomuttrc
set imap_pass = "`gpg --batch -q --decrypt ~/.neomutt/account.gpg`"
set smtp_pass = "`gpg --batch -q --decrypt ~/.neomutt/account.gpg`"
```

Expected result: NeoMutt decrypts the password at startup.

## Using GNOME Keyring / `secret-tool`

1. Store a secret in GNOME Keyring (see GNOME Keyring docs).
2. Query it from NeoMutt:

```neomuttrc
set imap_pass = "`secret-tool lookup service imap user you@example.com`"
```

Expected result: the password is retrieved from the keyring on demand.

## Using macOS Keychain

1. Store a generic password in Keychain.
2. Query it from NeoMutt:

```neomuttrc
set imap_pass = "`security find-generic-password -w -s \"Mail IMAP\" -a \"you@example.com\"`"
```

Expected result: NeoMutt reads the password from Keychain.

## Configuring `account_command`

`account_command` lets NeoMutt call a script that returns credentials for IMAP/POP/SMTP.
This avoids storing secrets in config options.

1. Create a script that prints key/value pairs to stdout:

```
username: you@example.com
password: your-password
```

2. Configure NeoMutt:

```neomuttrc
set account_command = "/path/to/cred-helper.sh"
```

Expected result: NeoMutt uses your script to populate account credentials.

See the `account_command` section in the manual for the full interface.

## Using Backtick Commands for `imap_pass` and `smtp_pass`

If you cannot use `account_command`, backticks are the next best option.
Any command that prints the password to stdout can be used:

```neomuttrc
set imap_pass = "`your-command-here`"
set smtp_pass = "`your-command-here`"
```

## Security Considerations

1. Avoid storing plaintext passwords in config files.
2. Use password managers or `account_command` to keep credentials out of `set` output.
3. Restrict permissions on token files and keyrings.
