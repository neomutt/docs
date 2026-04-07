---
title: Environment Variables
description: Reference for environment variables read and set by NeoMutt including standard Unix, XDG, and testing variables
keywords: neomutt, environment, variables, env, setenv, unsetenv, XDG, EDITOR, VISUAL, HOME, TMPDIR, MAIL, MAILDIR
---

(ref-env)=
# Environment Variables

NeoMutt reads and uses a number of environment variables.
Some are standard Unix variables; others are specific to NeoMutt or related tools.

Environment variables can be referenced in NeoMutt configuration files using the `$NAME` syntax and will be expanded when parsing config tokens (see [Config-File Expansion](#config-file-expansion)).
The [`:ifdef`](cmd-ifdef) / [`:ifndef`](cmd-ifndef) commands can also test whether an environment variable is set.
Finally, the [`:setenv`](cmd-setenv) and [`:unsetenv`](cmd-unsetenv) commands allow you to modify the environment that is passed to child processes.

---

## Standard Variables

### COLORTERM

**Source:** `main.c`

Indicates the terminal's colour capability.
When set to `truecolor` or `24bit` (case-sensitive) **and** ncurses reports
2{sup}`24` colours, NeoMutt enables direct-colour support by setting the
[`$color_directcolor`](cfg-color-directcolor) config variable to `yes`.

:::{seealso}
[Configuration], `$color_directcolor`
:::

### COLUMNS

**Source:** `gui/resize.c`, `attach/mutt_attach.c`

Fallback number of terminal columns used when the `TIOCGWINSZ` ioctl returns zero.
Defaults to **80** if unset or unparsable.

NeoMutt also temporarily injects `COLUMNS` into its private environment list (`NeoMutt->env`) before invoking mailcap commands so that external programs can format their output to the available width.

:::{seealso}
[LINES]
:::

### EDITOR

**Source:** `main.c`

Specifies the editor to use when composing messages if `VISUAL` is unset.
If neither `VISUAL` nor `EDITOR` is set, NeoMutt falls back to `vi`.

:::{seealso}
[VISUAL], `$editor`
:::

### ESCDELAY

**Source:** ncurses

Specifies the time (in milliseconds) that ncurses waits after receiving an {kbd}`Escape` character to determine whether it is the beginning of a terminal escape sequence.
The default is **1000 ms**.

Setting this to a low value (e.g. `25`) or `0` is recommended when [`$abort_key`](cfg-abort-key) is set to `<Esc>`, so that single {kbd}`Escape` presses are recognised immediately.

```sh
export ESCDELAY=25
```

:::{seealso}
[`$abort_key`](cfg-abort-key)
:::

### EGDSOCKET

**Source:** `conn/openssl.c`

Path to an Entropy Gathering Daemon (EGD) socket used by OpenSSL (≥ 0.9.5) to seed the random number generator.
Only used when NeoMutt is compiled with OpenSSL support and `HAVE_RAND_EGD` is defined.

If unset, NeoMutt also checks `~/.entropy` and `/tmp/entropy`.

:::{seealso}
[RANDFILE], `$entropy_file`
:::

### EMAIL

**Source:** `main.c`

The user's email address.
If set, it is used as the initial value for the `$from` config variable.

:::{seealso}
[`$from`](cfg-from)
:::

### HOME

**Source:** `core/neomutt.c`

Full path to the user's home directory.
Read at startup and stored in `NeoMutt->home_dir`.
Used throughout NeoMutt for tilde expansion (`~/…`), locating configuration
files, and constructing default paths.

:::{seealso}
`$folder`, [XDG_CONFIG_HOME]
:::

### LANG

**Source:** `core/neomutt.c`

Standard locale variable.
Checked (together with `LC_ALL` and `LC_CTYPE`) to determine whether a locale definition exists.
If any of these is set, NeoMutt enables locale-aware string handling (`OptLocales`).

:::{seealso}
[LC_ALL], [LC_CTYPE], `$charset`
:::

### LC_ALL

**Source:** `core/neomutt.c`

Overrides all other locale variables.
See [LANG] above.

### LC_CTYPE

**Source:** `core/neomutt.c`

Character-classification locale category.
See [LANG] above.

### LINES

**Source:** `gui/resize.c`

Fallback number of terminal rows used when the `TIOCGWINSZ` ioctl returns zero.
Defaults to **24** if unset or unparsable.

:::{seealso}
[COLUMNS]
:::

### MAIL

**Source:** `main.c`

Full path to the user's spool mailbox.
Used as the initial value for the `$spool_file` config variable.
If unset, NeoMutt falls back to `MAILDIR`.

:::{seealso}
[MAILDIR], `$spool_file`
:::

### MAILCAPS

**Source:** `main.c`

Colon-separated list of paths to search for mailcap files.
If unset, NeoMutt uses an RFC 1524-compliant search path extended with
NeoMutt-specific directories:

```
$HOME/.mailcap:<datadir>/mailcap:<sysconfdir>/mailcap:/etc/mailcap:/usr/etc/mailcap:/usr/local/etc/mailcap
```

:::{seealso}
`$mailcap_path`
:::

### MAILDIR

**Source:** `main.c`

Full path to the user's spool mailbox when `MAIL` is unset.
Commonly used when the spool mailbox is a Maildir folder.

:::{seealso}
[MAIL], [`$spool_file`](cfg-spool-file)
:::

### MM_NOASK

**Source:** `email/handler.c`

Controls automatic use of mailcap entries.

- If set to `1`, mailcap handlers are always invoked without prompting.
- If set to a colon-separated list of MIME types, only matching types are
  auto-viewed without prompting.

:::{seealso}
`$mailcap_path`, [MIME Support]
:::

### NNTPSERVER

**Source:** `main.c`

Domain name or address of the default NNTP (Usenet) server.
Precedence: command line `-g`, config [`$news_server`](cfg-news-server), `NNTPSERVER`,
then `<sysconfdir>/nntpserver`.

:::{seealso}
`$news_server`
:::

### RANDFILE

**Source:** `conn/openssl.c` (via OpenSSL's `RAND_file_name()`)

Path to a file containing random data used to seed the SSL random number generator.
If unset, `~/.rnd` is used.
**Do not** store important data in this file.

:::{seealso}
[EGDSOCKET], [`$entropy_file`](cfg-entropy-file)
:::

### REPLYTO

**Source:** `main.c`

When set, its value is used as a default `Reply-To:` header added via
NeoMutt's [`:my-header`](cmd-my-header) mechanism.

:::{seealso}
[`$from`](cfg-from)
:::

### TERM

**Source:** `gui/terminal.c`

The terminal type.
Used to determine whether the terminal supports the title-bar escape sequence.
NeoMutt checks `TERM` against a list of known terminal types (e.g. `xterm`, `screen`, `rxvt`).

:::{seealso}
[`$ts_enabled`](cfg-ts-enabled), [`$ts_status_format`](cfg-ts-status-format)
:::

### TEXTDOMAINDIR

**Source:** `core/neomutt.c`

Overrides the compiled-in path for GNU `gettext` message catalogues used for Native Language Support (NLS).
If unset, the default `MUTTLOCALEDIR` compile-time path is used.

### TMPDIR

**Source:** `main.c`

Directory in which temporary files are created.
If set, it overrides the compiled-in defaults for both [`$tmp_dir`](cfg-tmp-dir) and [`$tmp_draft_dir`](cfg-tmp-draft-dir).
If unset, `/tmp` is used for [`$tmp_dir`](cfg-tmp-dir) and `/var/tmp` for [`$tmp_draft_dir`](cfg-tmp-draft-dir).

:::{seealso}
[`$tmp_dir`](cfg-tmp-dir), [`$tmp_draft_dir`](cfg-tmp-draft-dir)
:::

### USER

**Source:** `core/neomutt.c`

The current user's login name.
Read at startup and stored in `NeoMutt->username`.
Used for constructing default paths, authenticating to servers, and other
identity-related operations.

### VISUAL

**Source:** `main.c`

Specifies the preferred editor for composing messages.
Takes precedence over `EDITOR`.
If neither is set, NeoMutt defaults to `vi`.

:::{seealso}
[EDITOR](ref-env), [`$editor`](cfg-editor)
:::

---

## XDG Variables

### XDG_CONFIG_HOME

**Source:** `main.c`, `muttlib.c`

Specifies the XDG Base Directory for user-specific configuration.
NeoMutt searches `$XDG_CONFIG_HOME/neomutt/neomuttrc` when no config file
is given on the command line.
Defaults to `$HOME/.config` if unset.

Can be overridden by the `-F` command-line option.

:::{seealso}
[XDG_CONFIG_DIRS], [HOME]
:::

### XDG_CONFIG_DIRS

**Source:** `muttlib.c`

Colon-separated list of system-wide XDG configuration directories.
NeoMutt searches each directory for `neomutt/neomuttrc`.
Defaults to `/etc/xdg` if unset.

Bypass loading with the `-n` command-line option.

:::{seealso}
[XDG_CONFIG_HOME]
:::

---

## Variables Set by NeoMutt

These variables are **set** by NeoMutt in its private environment (`NeoMutt->env`) for child processes rather than being read from the user's environment.

### COLUMNS {#columns-set}

Temporarily injected into the environment before executing mailcap commands
so that external viewer programs know the terminal width.

See [COLUMNS] above.

### GPG_TTY

**Source:** `ncrypt/pgp.c`

Set to the name of the controlling terminal (from [`ttyname(3)`](https://man7.org/linux/man-pages/man3/ttyname.3.html)) when `$pgp_use_gpg_agent` is enabled.
This allows `gpg-agent` to prompt for passphrases on the correct terminal.

Set in both the real process environment (`setenv`) and NeoMutt's private environment list.

:::{seealso}
`$pgp_use_gpg_agent`
:::

---

## Configuration Commands

NeoMutt provides built-in commands to manage environment variables from within configuration files or the command line:

**`setenv`**
: Set an environment variable in NeoMutt's private environment:

  ```neomuttrc
  setenv NAME value
  ```

**`unsetenv`**
: Remove an environment variable from NeoMutt's private environment:

  ```neomuttrc
  unsetenv NAME
  ```

**`ifdef` / `ifndef`**
: Conditionally execute a command based on whether a symbol (including
  environment variables) is defined:

  ```neomuttrc
  ifdef VISUAL 'set editor = "$VISUAL"'
  ```

:::{seealso}
[Configuration]
:::

---

(config-file-expansion)=
## Config-File Expansion

Any environment variable can be referenced in NeoMutt configuration files using the `$NAME` syntax.
When parsing a config token, NeoMutt first checks for a matching config variable; if none is found, it falls back to the environment (via `mutt_str_getenv`).

Example:

```neomuttrc
set spool_file = "$MAIL"
set record = "$HOME/sent-mail"
```

:::{seealso}
`neomuttrc(5)`
:::

---

## Testing Variable

### NEOMUTT_TEST_DIR

**Source:** `test/common.c`

Used exclusively by the NeoMutt test suite to locate test data files.
Not relevant for normal usage.
