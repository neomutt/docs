---
title: Set Up Periodic Mail Sync with cron or systemd
description: Automate mbsync and notmuch new using cron jobs or systemd timers for hands-free mail synchronisation
keywords: mbsync, notmuch, cron, systemd, timer, sync, automation, periodic, schedule, new mail, offline, isync
---

# Set Up Periodic Mail Sync with cron or systemd

## Prerequisites

1. `mbsync` configured and working (see [Setting Up Offline Email with mbsync](../tutorials/mbsync-setup)).
2. Optionally, `notmuch` configured if you use full-text search (see [Setting Up Notmuch for Email Search](../tutorials/notmuch-setup)).
3. Access to `cron` or `systemd --user` on your system.

## Create a Sync Script

1. Write a small wrapper script at `~/.local/bin/mailsync`:

```sh
#!/bin/sh
# Sync all IMAP accounts and update the Notmuch index.
mbsync -a 2>&1
notmuch new 2>&1
```

2. Make it executable:

```sh
chmod +x ~/.local/bin/mailsync
```

3. Test it:

```sh
~/.local/bin/mailsync
```

Expected result: mail syncs and the Notmuch database is updated.

If you don't use Notmuch, remove the `notmuch new` line.

## Option A: Use cron

1. Open your user crontab:

```sh
crontab -e
```

2. Add a line to run the script every 5 minutes:

```
*/5 * * * * ~/.local/bin/mailsync
```

3. Save and exit.

Expected result: `crontab -l` shows the new entry and mail syncs automatically.

### Pass the GPG Passphrase in cron

If `mbsync` uses `pass` or GPG for passwords, cron may not have access to `gpg-agent`.
Add environment variables to the crontab:

```
GPG_TTY=/dev/null
DISPLAY=:0
*/5 * * * * export GPG_TTY DISPLAY && ~/.local/bin/mailsync
```

Or configure `gpg-agent` to allow preset passphrases — see the `gpg-preset-passphrase` man page.

## Option B: Use systemd User Timers

### Create the Service Unit

1. Create `~/.config/systemd/user/mailsync.service`:

```ini
[Unit]
Description=Sync mail with mbsync and update Notmuch

[Service]
Type=oneshot
ExecStart=%h/.local/bin/mailsync
```

### Create the Timer Unit

2. Create `~/.config/systemd/user/mailsync.timer`:

```ini
[Unit]
Description=Run mailsync every 5 minutes

[Timer]
OnBootSec=1min
OnUnitActiveSec=5min

[Install]
WantedBy=timers.target
```

### Enable and Start the Timer

3. Reload and enable:

```sh
systemctl --user daemon-reload
systemctl --user enable --now mailsync.timer
```

4. Verify:

```sh
systemctl --user status mailsync.timer
systemctl --user list-timers
```

Expected result: the timer is active and `mailsync.service` runs every 5 minutes.

### Check Logs

```sh
journalctl --user -u mailsync.service -n 20
```

Expected result: recent sync output appears in the journal.

## Add a Desktop Notification

1. Extend `~/.local/bin/mailsync` to notify on new mail:

```sh
#!/bin/sh
mbsync -a 2>&1
notmuch new 2>&1

new_count=$(notmuch count tag:unread AND tag:inbox)
if [ "$new_count" -gt 0 ]; then
    notify-send "New mail" "$new_count unread messages"
fi
```

Expected result: a desktop notification appears when unread mail arrives.

## Trigger Sync from Inside NeoMutt

You can still sync manually from NeoMutt alongside the timer:

```neomuttrc
macro index o "<shell-escape>~/.local/bin/mailsync<Enter>" "Sync mail now"
```

Expected result: pressing {kbd}`o` runs the same sync script on demand.

See [Setting Up Offline Email with mbsync](../tutorials/mbsync-setup) for the mbsync configuration and [Setting Up Notmuch for Email Search](../tutorials/notmuch-setup) for the Notmuch setup.
