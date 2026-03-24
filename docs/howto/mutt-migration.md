# How to Migrate from Mutt to NeoMutt

## Prerequisites

1. Install NeoMutt alongside your existing Mutt installation.
2. Make a backup of your current Mutt configuration.

## Key Differences Between Mutt and NeoMutt

1. NeoMutt is a fork of Mutt that aggregates long-standing patches and features.
2. It keeps Mutt compatibility where possible while adding features like Notmuch integration, sidebar, and extra hooks.

Expected result: you understand that most Mutt configuration still works, but NeoMutt adds optional features you can enable.

## Config File Compatibility

1. Copy your Mutt config to a NeoMutt config file location:

```
~/.neomuttrc
```

2. Start NeoMutt with that file:

```sh
neomutt -F ~/.neomuttrc
```

Expected result: NeoMutt starts using your existing configuration.

See [Configuration File Locations](../reference/config-locations).

## New Features in NeoMutt

1. Review NeoMutt features in the project README.
2. Enable features you want in small steps.

Expected result: you can add features without breaking your base config.

## Deprecated or Changed Settings

1. Start NeoMutt and watch for warnings on startup.
2. Look up any warnings in the reference documentation.

Expected result: any incompatible settings are identified early.

## Testing Your Existing Config

1. Run NeoMutt with system config disabled to isolate issues:

```sh
neomutt -nF ~/.neomuttrc
```

2. Add sections of your config back in gradually if needed.

Expected result: you can pinpoint which settings cause problems.

## Common Migration Issues

1. Missing optional features because your build lacks certain libraries (IMAP, Notmuch, crypto).
2. External tool integrations not installed on the new system.
3. Different config file location or `$folder` paths.

Expected result: you can resolve issues by installing missing dependencies or fixing paths.

## Running Mutt and NeoMutt Side by Side

1. Keep separate config files, for example `~/.muttrc` and `~/.neomuttrc`.
2. Start each client with its own config:

```sh
mutt -F ~/.muttrc
neomutt -F ~/.neomuttrc
```

Expected result: you can compare behavior while migrating without downtime.
