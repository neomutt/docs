# Command Line

## Intro

NeoMutt has four modes of operation: `help`, `info`, `send`, `tui`.

The default mode, if no command line arguments are specified, is `tui`.

**help** -- Get command line help for NeoMutt:

| Command Line        | Description              |
| :------------------ | :----------------------- |
| `neomutt -h <mode>` | Detailed help for a mode |
| `neomutt -v[v]`     | Version or license       |

**shared** -- Options that apply to all modes:

| Command Line           | Description                   |
| :--------------------- | :---------------------------- |
| `neomutt -n`           | Don't read system config file |
| `neomutt -F <config>`  | Use this user config file     |
| `neomutt -e <command>` | Run extra commands            |
| `neomutt -m <type>`    | Set default mailbox type      |
| `neomutt -d <level>`   | Set logging level (1..5)      |
| `neomutt -l <file>`    | Set logging file              |

**info** -- Ask NeoMutt for config information:

| Command Line                          | Description          |
| :------------------------------------ | :------------------- |
| `neomutt -A <alias> [...]`            | Lookup email aliases |
| `neomutt -D [-D] [-O] [-S]`           | Dump the config      |
| `neomutt -Q <option> [...] [-O] [-S]` | Query config options |

**send** -- Send an email from the command line:

| Command Line         | Description                     |
| :------------------- | :------------------------------ |
| `-a <file> [...]`    | Attach files                    |
| `-b <address>`       | Add Bcc: address                |
| `-C`                 | Use crypto (signing/encryption) |
| `-c <address>`       | Add Cc: address                 |
| `-E`                 | Edit message                    |
| `-H <draft>`         | Use draft email                 |
| `-i <include>`       | Include body file               |
| `-s <subject>`       | Set Subject:                    |
| `-- <address> [...]` | Add To: addresses               |

**tui** -- Start NeoMutt's TUI (Terminal User Interface):

| Command Line           | Description            |
| :--------------------- | :-------------------   |
| `neomutt`              | Start NeoMutt's TUI    |
| `neomutt -f <mailbox>` | Open this mailbox      |
| `neomutt -G`           | Open NNTP browser      |
| `neomutt -g <server>`  | Use this NNTP server   |
| `neomutt -p`           | Resume postponed email |
| `neomutt -R`           | Open mailbox read-only |
| `neomutt -y`           | Open mailbox browser   |
| `neomutt -Z`           | Check for new mail     |
| `neomutt -z`           | Check for any mail     |

---

## Shared

**shared**: Options that apply to all modes

By default NeoMutt loads one system and one user config file,
e.g. `/etc/neomuttrc` and `~/.neomuttrc`

| Command Line           | Description                   |
| :--------------------- | :-------------------          |
| `neomutt -n`           | Don't read system config file |
| `neomutt -F <config>`  | Use this user config file<br> May be used multiple times |

These options override the config:

| Command Line           | Description            |
| :--------------------- | :-------------------   |
| `neomutt -m <type>` | Set default mailbox type<br>May be: maildir, mbox, mh, mmdf |
| `neomutt -e <command>` | Run extra commands<br>May be used multiple times |

These logging options override the config:

| Command Line           | Description                                         |
| :--------------------- | :-------------------                                |
| `neomutt -d <level>`   | Set logging level<br>0 (off), 1 (low) .. 5 (high)   |
| `neomutt -l <file>`    | Set logging file<br>Default file `~/.neomuttdebug0` |

**Examples:**

```sh
neomutt -n
neomutt -F work.rc
neomutt -F work.rc -F colours.rc

neomutt -m maildir
neomutt -e 'set ask_cc = yes'

neomutt -d 2
neomutt -d 5 -l neolog
```

See also:
- Config files: https://neomutt.org/guide/configuration

## Help

**help**: Get command line help for NeoMutt

| Command Line        | Description                                                       |
| :------------------ | :---------------------------------------------------------------- |
| `neomutt -h`        | Overview of command line options                                  |
| `neomutt -h <mode>` | Detailed help for: `shared`, `help`, `info`, `send`, `tui`, `all` |
| `neomutt -v`        | NeoMutt version and build parameters                              |
| `neomutt -vv`       | NeoMutt Copyright and license                                     |

**Examples:**

```sh
neomutt -h info
neomutt -vv
```

## Info

**info**: Ask NeoMutt for config information

| Command Line                | Description                                                                 |
| :-------------------------- | :-------------------------------------------------------------------------- |
| `neomutt -A <alias> [...]`  | Lookup email aliases<br>Multiple aliases can be looked up (space-separated) |
| `neomutt -D`                | Dump all the config options                                                 |
| `neomutt -D -D`             | (or -DD) Like -D, but only show changed config                              |
| `neomutt -Q <option> [...]` | Query config options<br>Multiple options can be looked up (space-separated) |

Modify the `-D` and `-Q` options:

| Command Line | Description                         |
| :----------- | :---------------------------------- |
| `neomutt -O` | Add one-liner documentation         |
| `neomutt -S` | Hide the value of sensitive options |

**Examples:**

```sh
neomutt -A flatcap gahr
neomutt -D -O
neomutt -DD -S
neomutt -O -Q alias_format index_format
```

## Send

**send**: Send an email from the command line

These options can supply everything NeoMutt needs to send an email.

If any parts are missing, NeoMutt will start the TUI to ask for them.

Addresses may be used before the options, or after a `--` marker.

Aliases may be used in place of addresses.

| Command Line                 | Description                                                          |
| :--------------------------- | :------------------------------------------------------------------- |
| `neomutt -a <file> [...]`    | Attach files<br>Terminated by `--` or another option                 |
| `neomutt -b <address>`       | Add `Bcc:` address                                                   |
| `neomutt -C`                 | Use crypto (signing/encryption)<br>Must be set up in the config file |
| `neomutt -c <address>`       | Add `Cc:` address                                                    |
| `neomutt -E`                 | Edit message (supplied by `-H` or `-i`)                              |
| `neomutt -H <draft>`         | Use draft email<br>Full email with headers and body                  |
| `neomutt -i <include>`       | Include body file                                                    |
| `neomutt -s <subject>`       | Set `Subject:`                                                       |
| `neomutt -- <address> [...]` | Add `To:` addresses                                                  |

**Examples:**

```sh
neomutt flatcap -s 'Meeting' < meeting.txt
neomutt jim@example.com -c bob@example.com -s 'Party' -i party.txt
neomutt -s 'Receipts' -a receipt1.pdf receipt2.pdf -- rocco
cat secret.txt | neomutt gahr -s 'Secret' -C
```

## TUI

**tui**: Start NeoMutt's TUI (Terminal User Interface)

Running NeoMutt with no options will read the config and start the TUI.
By default, it will open the Index Dialog with the `$spool_file` Mailbox.

These options cause NeoMutt to check a mailbox for mail.
If the condition isn't matched, NeoMutt exits.

| Command Line  | Description            |
| :------------ | :--------------------- |
| `neomutt -p`  | Resume postponed email |
| `neomutt -Z`  | Check for new mail     |
| `neomutt -z`  | Check for any mail     |

These options change the starting behaviour:

| Command Line           | Description             |
| :--------------------- | :---------------------- |
| `neomutt -f <mailbox>` | Open this mailbox       |
| `neomutt -G`           | Open NNTP browser       |
| `neomutt -g <server>`  | Use this NNTP server    |
| `neomutt -R`           | Open mailbox read-only  |
| `neomutt -y`           | Open mailbox browser    |

**Examples:**

```sh
neomutt -f ~/mail -Z
neomutt -p
neomutt -y
```

