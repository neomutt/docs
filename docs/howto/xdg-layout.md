---
title: Organise Config Files Using XDG Directories
description: Arrange NeoMutt configuration, cache, and mail data across XDG base directories for a clean home directory
keywords: xdg, xdg_config_home, xdg_cache_home, xdg_data_home, config layout, neomuttrc, header_cache, message_cachedir, maildir, folder, directory structure, dotfiles
---

# Organise Config Files Using XDG Directories

## Prerequisites

1. NeoMutt installed and working with a basic configuration.
2. Familiarity with where your current config, cache, and mail files live.

## The XDG Base Directory Layout

The XDG Base Directory Specification defines standard locations for configuration, data, and cache files.
Using these keeps your home directory clean and makes backup easier.

| Purpose       | XDG Variable       | Default              | NeoMutt usage                    |
|---------------|--------------------|-----------------------|----------------------------------|
| Configuration | `$XDG_CONFIG_HOME` | `~/.config`          | `~/.config/neomutt/neomuttrc`    |
| Data (mail)   | `$XDG_DATA_HOME`   | `~/.local/share`     | `~/.local/share/mail/`           |
| Cache         | `$XDG_CACHE_HOME`  | `~/.cache`           | `~/.cache/neomutt/`             |

## Move Configuration to XDG_CONFIG_HOME

1. Create the config directory:

```sh
mkdir -p ~/.config/neomutt
```

2. Move your config file:

```sh
mv ~/.neomuttrc ~/.config/neomutt/neomuttrc
```

3. Move any sourced files (aliases, account configs) into the same directory.

4. Start NeoMutt and confirm it finds the config.

Expected result: NeoMutt reads `~/.config/neomutt/neomuttrc` automatically — it is higher priority than `~/.neomuttrc` in the search order.

## Move Cache to XDG_CACHE_HOME

1. Create the cache directory:

```sh
mkdir -p ~/.cache/neomutt
```

2. Update your config:

```neomuttrc
set header_cache     = "~/.cache/neomutt/headers"
set message_cachedir = "~/.cache/neomutt/bodies"
```

Expected result: cache files are stored outside your config directory and can be safely excluded from backups.

## Store Mail in XDG_DATA_HOME

1. Create the mail directory:

```sh
mkdir -p ~/.local/share/mail
```

2. Update your config:

```neomuttrc
set folder = "~/.local/share/mail/you@example.com"
```

3. If you use mbsync, update `~/.mbsyncrc` to match:

```
MaildirStore you@example.com-local
Path ~/.local/share/mail/you@example.com/
Inbox ~/.local/share/mail/you@example.com/INBOX
```

4. If you use Notmuch, update `~/.notmuch-config`:

```ini
[database]
path=/home/you/.local/share/mail
```

Expected result: mail data lives in `~/.local/share/mail/`, separate from config and cache.

## Store msmtp Config in XDG_CONFIG_HOME

1. Create the directory:

```sh
mkdir -p ~/.config/msmtp
```

2. Place your msmtp config at `~/.config/msmtp/config`.
   msmtp checks this path by default on most systems.

Expected result: SMTP configuration follows the same layout as NeoMutt's.

## Organise Per-Account Config Files

For multi-account setups, keep per-account configs in subdirectories:

```
~/.config/neomutt/
├── neomuttrc
└── accounts/
    ├── personal.muttrc
    └── work.muttrc
```

Source them from your main config:

```neomuttrc
source ~/.config/neomutt/accounts/personal.muttrc
source ~/.config/neomutt/accounts/work.muttrc
```

Expected result: account-specific settings are isolated in their own files.

## Example: Complete XDG Directory Tree

```
~/.config/
├── neomutt/
│   ├── neomuttrc
│   ├── accounts/
│   │   └── you@example.com.muttrc
│   ├── aliases
│   └── mailcap
├── msmtp/
│   └── config
~/.cache/
└── neomutt/
    ├── headers/
    └── bodies/
~/.local/share/
└── mail/
    └── you@example.com/
        ├── INBOX/
        ├── Sent/
        └── Drafts/
```

## What to Back Up

| Directory              | Back up? | Notes                          |
|------------------------|----------|--------------------------------|
| `~/.config/neomutt/`   | Yes      | All configuration              |
| `~/.config/msmtp/`     | Yes      | SMTP configuration             |
| `~/.mbsyncrc`          | Yes      | Sync configuration             |
| `~/.notmuch-config`    | Yes      | Search configuration           |
| `~/.cache/neomutt/`    | No       | Regenerated automatically      |
| `~/.local/share/mail/` | Optional | Can be re-synced from server   |

See [Back Up Your Configuration](backup-config) for more on backups and [Writing Your First Configuration](../tutorials/first-config) for config file search order.
