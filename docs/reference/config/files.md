---
title: Config File Locations
description: System and user configuration file search paths, naming conventions, and config priority order.
keywords: neomutt, config file, neomuttrc, muttrc, xdg, location, search order, system config, user config, priority, startup
---

(cfg-files)=
# Config File Locations

When NeoMutt starts up it looks for two config files — one "system" file and one "user" file.

NeoMutt first reads the system config file, then the user config file. The two files are merged in the sense that "last setting wins". That is, if a setting is defined in both files, the user config file's value for that setting is the one that takes precedence and becomes effective.

NeoMutt searches for several different file names when looking for config. It looks for NeoMutt config files before Mutt config files and versioned config before plain config.

## Config File Search Order

| Filename  |
|-----------|
| neomuttrc |
| muttrc    |

This allows the user to create separate NeoMutt and Mutt config files on the same system.

## System Config File Locations

NeoMutt will search for a system config file in a `neomutt` directory in several places. First it searches the locations specified in the `XDG_CONFIG_DIRS` environment variable, which defaults to `/etc/xdg`. Next, it looks in `/etc`. Finally, it tries `/usr/share`.

The system config file will not be read if the `-n` option is used on the command line.

NeoMutt will read just one file, the first file it finds, from the list below.

| File Location                  | Notes                         |
|--------------------------------|-------------------------------|
| `/etc/xdg/neomutt/neomuttrc`   |                               |
| `/etc/xdg/neomutt/Muttrc`      | Note the case of the filename |
| `/etc/neomuttrc`               |                               |
| `/etc/Muttrc`                  | Note the case of the filename |
| `/usr/share/neomutt/neomuttrc` |                               |
| `/usr/share/neomutt/Muttrc`    | Note the case of the filename |

## User Config File Locations

NeoMutt will search for a user config file in several places. First it looks in the directory specified in the `XDG_CONFIG_HOME` environment variable, which defaults to `~/.config/neomutt`. Next, it looks in `~` (your home directory). Finally, it tries `~/.neomutt`.

You may specify your own location for the user config file using the `-F` option on the command line.

NeoMutt will read just one file, the first file it finds, from the list below.

| File Location                 |
|-------------------------------|
| `~/.config/neomutt/neomuttrc` |
| `~/.config/neomutt/muttrc`    |
| `~/.config/mutt/neomuttrc`    |
| `~/.config/mutt/muttrc`       |
| `~/.neomutt/neomuttrc`        |
| `~/.neomutt/muttrc`           |
| `~/.mutt/neomuttrc`           |
| `~/.mutt/muttrc`              |
| `~/.neomuttrc`                |
| `~/.muttrc`                   |

## Config Priority

The majority of NeoMutt's config will be read from two files: the system config in `/etc` and the user config in, e.g. `~/.neomuttrc`.

The last file that gets read will overwrite any settings from previous config files.
This means that an administrator can set some defaults which the user can override.

Additionally, there are a handful of config items which can be set using an environment variable.
They have a lower priority than the NeoMutt config files: `$editor`, `$from`, `$mailcap_path`, `$news_server`, `$shell`, `$spool_file`, `$tmp_dir`.

Finally, it's possible to set some variables directly on the command-line using the `-e` option.

| Priority | Where         | Example                                               |
|----------|---------------|-------------------------------------------------------|
| Highest  | Command line  | `neomutt -e 'set from="John Doe <john@example.com>"'` |
|          | User Config   | `~/.neomuttrc`                                        |
|          | System Config | `/etc/neomuttrc`                                      |
|          | Environment   | `export EDITOR="/usr/bin/vim"`                        |
| Lowest   | Built-in      | Defaults hard-coded into NeoMutt                      |
