# How to Back Up Your Configuration

## Prerequisites

1. Identify which configuration file NeoMutt uses on your system.
2. Decide where you want your backups stored (local disk, external disk, or a private repo).

## Which Files to Back Up

1. Back up your main config file from the location NeoMutt is using. See [Configuration File Locations](../reference/config-locations).
2. Back up any files referenced with `source`, such as separate alias or account files.
3. Back up user-defined files pointed to by variables such as:

- `$alias_file`
- `$mailcap_path`
- `$signature`
- `$pgp_default_key` or S/MIME files if you use crypto

Expected result: all files you actively use in your configuration are captured.

## Where NeoMutt Stores Data

Some data lives outside the main config file.
Check the variables that define where it is stored:

- `$header_cache` and `$message_cachedir` (cache)
- `$history_file` (command and prompt history)
- `$certificate_file` (TLS certificates)

Expected result: cache and metadata files are included if you want a full restore, or excluded if you only want configuration.

## Using Version Control for Config Management

1. Create a private git repository for your config files.
2. Add your main config file and any sourced files.
3. Add a `.gitignore` for transient cache files if you do not want them in version control.

Expected result: your configuration has history, and changes are trackable and reversible.

## Restoring Configuration on a New Machine

1. Install NeoMutt and required tools (GPG, notmuch, msmtp, etc.).
2. Restore your config files into the expected locations.
3. Verify any external paths (mail directories, token files, keyrings).

Expected result: NeoMutt starts without errors and uses your familiar settings.

## Managing Config Across Multiple Machines

1. Keep a shared config repo and clone it on each machine.
2. Use `ifdef` or environment variables to handle machine-specific differences.
3. Store secrets outside the repo and load them dynamically.

Expected result: the same config works across systems with minimal overrides.

## Sensitive Data Considerations

1. Avoid storing passwords directly in config files.
2. Prefer `account_command` or encrypted helpers (GPG, `pass`, Keychain).
3. If you must store secrets, restrict file permissions to your user.

Expected result: your backups are safe to store and sync without exposing credentials.
