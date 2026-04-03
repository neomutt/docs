---
title: Sending Email from the Command Line
description: Guide to composing, attaching files, piping, encrypting, and sending email from the NeoMutt command line
keywords: neomutt, send, email, command-line, attach, draft, pipe, encrypt, sign, batch mode, smtp, sendmail, subject, recipients, scripting
---

(ref-cli-sending)=
# Sending Email from the Command Line

NeoMutt can send email directly from the command line — no interactive interface required.
This guide walks through every way to compose, attach, sign, encrypt, and send messages without ever opening the full NeoMutt application.

:::{admonition} Before You Start
:class: tip

NeoMutt must be configured with a working mail delivery method before you can send.
Check that one of the following is set in your `~/.neomuttrc`:

```neomuttrc
# Option A: Use a local sendmail program (the default)
set sendmail = "/usr/sbin/sendmail -oem -oi"

# Option B: Use an SMTP server
set smtp_url = "smtps://you@mail.example.com:465"
set smtp_pass = "your-password"
```

If you're unsure which you have, run:

```sh
neomutt --query sendmail smtp_url
```
:::

---

## Your First Email

The simplest way to send an email is to give NeoMutt a recipient and a
subject:

```sh
neomutt --subject 'Hello' -- alice@example.com
```

NeoMutt opens your text editor so you can type the message body.
When you save and close the editor, NeoMutt presents the compose screen where you can review the message, then press `y` to send.

:::{admonition} Which editor?
:class: note

NeoMutt uses the editor set by `$editor` in your config, or the `VISUAL` or `EDITOR` environment variables.
If none is set, it defaults to `vi`.
:::

---

## Recipients

### To: Addresses

Recipients can appear in two places on the command line:

```sh
# Before any options (leading arguments)
neomutt alice@example.com --subject 'Hello'

# After the -- separator (trailing arguments)
neomutt --subject 'Hello' -- alice@example.com
```

You can send to multiple people by listing several addresses:

```sh
neomutt --subject 'Team Lunch' -- alice@example.com bob@example.com carol@example.com
```

### Cc: and Bcc: Addresses

Add Cc: (carbon copy) and Bcc: (blind carbon copy) recipients with `--cc`
and `--bcc`:

```sh
neomutt --subject 'Project Update' \
  --cc manager@example.com \
  --bcc archive@example.com \
  -- team@example.com
```

Both `--cc` and `--bcc` can be used multiple times:

```sh
neomutt --subject 'Announcement' \
  --cc alice@example.com \
  --cc bob@example.com \
  --bcc records@example.com \
  -- staff@example.com
```

### Using Aliases

If you have aliases defined in your NeoMutt config:

```neomuttrc
# In ~/.neomuttrc
alias boss   Jane Smith <jane@example.com>
alias team   Alice <alice@example.com>, Bob <bob@example.com>
```

You can use the alias name instead of the full address:

```sh
neomutt --subject 'Weekly Report' --cc team -- boss
```

---

## Setting the Subject

Use `--subject` (or `-s`) to set the email's subject line:

```sh
neomutt --subject 'Meeting Tomorrow at 2pm' -- alice@example.com
```

If your subject contains spaces or special characters, wrap it in quotes:

```sh
neomutt --subject 'Re: Budget (Q3) — Final Numbers' -- finance@example.com
```

If you omit the subject, NeoMutt will prompt you for one in the compose
screen.

---

## Writing the Message Body

There are three ways to provide the email body from the command line.

### Option 1: Include a Text File

Use `--include` (or `-i`) to load the contents of a file as the message
body:

```sh
neomutt --subject 'Meeting Notes' \
  --include notes.txt \
  -- team@example.com
```

NeoMutt copies the file's contents into the message and opens the compose
screen so you can review (and optionally edit) the result before sending.

This is useful when you've already written the message in another
application, or when a script generates the body text:

```sh
# Include output from a script
./generate-report.sh > /tmp/report.txt
neomutt --subject 'Monthly Report' \
  --include /tmp/report.txt \
  -- manager@example.com
```

### Option 2: Pipe Text from Another Command

You can pipe text directly into NeoMutt using standard shell piping:

```sh
echo 'The nightly build succeeded.' | \
  neomutt --subject 'Build Report' -- dev@example.com
```

When NeoMutt receives piped input, it enters **batch mode** — the message is sent without opening an editor or the compose screen.
This makes piping ideal for automated and scripted emails.

More realistic piping examples:

```sh
# Email the output of a command
df -h | neomutt --subject 'Disk Usage Report' -- admin@example.com

# Email the contents of a log file
tail -50 /var/log/app.log | \
  neomutt --subject 'Recent Log Entries' -- support@example.com

# Email a diff
diff -u old-config.txt new-config.txt | \
  neomutt --subject 'Config Changes' -- sysadmin@example.com
```

:::{admonition} Batch mode is non-interactive
:class: important

When you pipe input to NeoMutt, it runs silently.
There are no prompts, no editor, and no compose screen.
The message is sent immediately.
Make sure your subject and recipients are correct before running the command.
:::

### Option 3: Use a Draft File

A draft file is a complete email — headers and body together — in standard email format.
Use `--draft` (or `-H`) to load one:

```sh
neomutt --draft ~/drafts/proposal.eml
```

See Draft Files below for the full details.

---

## Attaching Files

Use `--attach` (or `-a`) to attach one or more files to the email:

```sh
# Attach a single file
neomutt --subject 'Signed Contract' \
  --attach contract.pdf \
  -- legal@example.com
```

You can attach several files in one go by listing them after `--attach`.
The list of files ends when NeoMutt sees `--` or another option flag:

```sh
# Attach multiple files
neomutt --subject 'Holiday Photos' \
  --attach photo1.jpg photo2.jpg photo3.jpg \
  -- family@example.com
```

### Combining Attachments with a Message Body

Attach files while also including body text from a file:

```sh
neomutt --subject 'Invoice for March' \
  --include cover-letter.txt \
  --attach invoice-march.pdf receipt.pdf \
  -- accounts@example.com
```

Or pipe the body and attach files:

```sh
echo 'Please find the reports attached.' | \
  neomutt --subject 'Quarterly Reports' \
    --attach q1.pdf q2.pdf q3.pdf \
    -- board@example.com
```

### Attaching with a Draft File

Attachments specified on the command line are added to the draft:

```sh
neomutt --draft status-update.eml \
  --attach spreadsheet.xlsx \
  -- boss@example.com
```

### Tips for Attachments

- Use full file paths if NeoMutt can't find the file:
  `--attach /home/you/Documents/report.pdf`
- Attach glob patterns using your shell:
  `--attach ~/receipts/2025-03-*.pdf`
- NeoMutt detects MIME types automatically — a `.pdf` is sent as
  `application/pdf`, a `.jpg` as `image/jpeg`, and so on.

---

## Draft Files

A draft file is the most powerful way to compose an email from the command line.
It lets you pre-fill every part of the message — recipients, subject, custom headers, and the body — in a single file.

### Basic Format

A draft file looks like a standard email.
Headers come first, followed by a blank line, then the message body:

```email
To: alice@example.com
Subject: Lunch on Friday?

Hi Alice,

Are you free for lunch on Friday?  I was thinking we could
try that new place on Market Street.

Cheers,
Bob
```

Save this as (for example) `lunch.eml`, then send it:

```sh
neomutt --draft lunch.eml
```

### Supported Headers

You can include any standard email header in a draft file:

```email
From: Bob <bob@example.com>
To: alice@example.com, carol@example.com
Cc: dave@example.com
Bcc: archive@example.com
Subject: Project Kickoff
Reply-To: team-lead@example.com
In-Reply-To: <original-message-id@example.com>
References: <original-message-id@example.com>

This is the body of the email.
```

### NeoMutt-Specific Headers

Draft files can include special headers that NeoMutt understands but does
not send to the recipient:

| Header               | Purpose                                         |
|----------------------|-------------------------------------------------|
| `X-Mutt-Fcc:`        | Save a copy to this folder instead of `$record` |
| `X-Mutt-PGP:`        | Set PGP options (e.g. `sign`, `encrypt`)        |
| `X-Mutt-SMIME:`      | Set S/MIME options (e.g. `sign`, `encrypt`)     |
| `X-Mutt-References:` | Message-ID to thread this as a reply            |

These headers are stripped before sending.
They only control NeoMutt's behavior.

### Example: Draft with Security and Filing

```email
To: legal@example.com
Subject: Confidential: Contract Review
X-Mutt-Fcc: ~/Mail/sent-legal
X-Mutt-PGP: sign, encrypt

Please review the attached contract before Friday.

Regards,
Alice
```

```sh
neomutt --draft contract-review.eml --attach contract.pdf
```

### Example: Draft as a Reply

To send a message that threads as a reply to an existing conversation, use
the `X-Mutt-References` header with the Message-ID of the original:

```email
To: alice@example.com
Subject: Re: Lunch on Friday?
X-Mutt-References: <abc123@mail.example.com>

Friday works for me!  Let's meet at noon.
```

### Overriding Draft Headers from the Command Line

Command-line options merge with (and can override) draft file headers:

```sh
# Override the subject and add a Cc: not in the draft
neomutt --draft proposal.eml \
  --subject 'Revised Proposal' \
  --cc manager@example.com
```

The `--subject` replaces the draft's `Subject:` header.
The `--cc` address is added to any `Cc:` addresses already in the draft.
Addresses from `--` are added to the `To:` list.

### Reading a Draft from Standard Input

You can pipe a draft (headers and body) into NeoMutt using `-H -`:

```sh
cat <<'EOF' | neomutt --draft -
To: alice@example.com
Subject: Automated Notification

The backup completed successfully at $(date).
EOF
```

:::{admonition} Cannot edit piped drafts
:class: warning

You cannot use `--edit-message` with piped input (`--draft -`).
NeoMutt needs a real file on disk when editing is enabled.
:::

---

## Editing Before Sending

By default, NeoMutt opens the compose screen after loading a draft or include file.
The `--edit-message` (or `-E`) option goes further: it opens the **original file** in your editor, so your changes are saved back to that file.

This is useful when you want to refine a draft and keep the updated version
on disk:

```sh
# Edit the draft file in-place, then send
neomutt --edit-message --draft ~/drafts/proposal.eml
```

Without `--edit-message`, NeoMutt works on a temporary copy and the original file is untouched.
With `--edit-message`, the original is edited directly.

### Editing an Include File

The same applies to include files:

```sh
# Edit notes.txt in-place, then use it as the body
neomutt --edit-message \
  --include notes.txt \
  --subject 'Updated Notes' \
  -- team@example.com
```

### What Happens if You Don't Send?

If you decide not to send (for example, you postpone the message), NeoMutt saves the current state back to the original file.
This means you can come back to it later:

```sh
# Start composing — decide to postpone
neomutt --edit-message --draft ~/drafts/big-announcement.eml

# Later, resume where you left off
neomutt --edit-message --draft ~/drafts/big-announcement.eml
```

---

## Signing and Encrypting

The `--crypto` (or `-C`) option tells NeoMutt to apply your configured
cryptographic settings when sending from the command line:

```sh
neomutt --crypto \
  --subject 'Confidential Report' \
  --attach financials.pdf \
  -- cfo@example.com
```

### What `--crypto` Does

The `--crypto` flag activates whatever signing and encryption you have configured in your `~/.neomuttrc`.
The relevant settings are:

```neomuttrc
# Automatically sign all outgoing messages
set crypt_auto_sign = yes

# Automatically encrypt when the recipient's key is available
set crypt_opportunistic_encrypt = yes

# Use PGP (or S/MIME — or both)
set crypt_auto_pgp = yes
set crypt_auto_smime = yes
```

Without `--crypto`, batch-mode messages (piped input) skip cryptographic processing.
With `--crypto`, your crypto settings are applied even in batch mode.

### Signing Only

If your config has signing enabled but not encryption:

```neomuttrc
set crypt_auto_sign = yes
set crypt_auto_encrypt = no
```

Then `--crypto` signs the message:

```sh
echo 'Please see the attached patch.' | \
  neomutt --crypto \
    --subject 'Patch for Review' \
    --attach fix.patch \
    -- maintainer@example.com
```

### Encrypting Only

If your config has encryption enabled but not signing:

```neomuttrc
set crypt_auto_sign = no
set crypt_auto_encrypt = yes
```

Then `--crypto` encrypts the message (provided you have the recipient's
public key):

```sh
neomutt --crypto \
  --subject 'Account Credentials' \
  --include credentials.txt \
  -- sysadmin@example.com
```

### Sign and Encrypt

With both enabled, `--crypto` does both:

```neomuttrc
set crypt_auto_sign = yes
set crypt_auto_encrypt = yes
```

```sh
echo 'Wire transfer details inside.' | \
  neomutt --crypto \
    --subject 'Payment Instructions' \
    -- finance@example.com
```

### Using Draft Headers for Crypto

Instead of relying on global config, you can set crypto options per-message
in a draft file:

```email
To: lawyer@example.com
Subject: Privileged Communication
X-Mutt-PGP: sign, encrypt

The details of the settlement are as follows...
```

```sh
neomutt --draft privileged.eml
```

For S/MIME instead of PGP:

```email
To: partner@example.com
Subject: Signed Agreement
X-Mutt-SMIME: sign

Please find my digitally signed confirmation below.
```

---

## Batch Mode and Automation

When NeoMutt's standard input is not a terminal (i.e., you're piping data to it), it enters **batch mode** automatically.
In batch mode:

- No editor opens
- No compose screen appears
- No confirmation prompts
- The message is sent immediately

This makes batch mode perfect for scripts, cron jobs, and automated alerts.

### Scripted Alerts

```sh
#!/bin/sh
# alert-disk-full.sh — email an alert when disk usage exceeds 90%

usage=$(df / | awk 'NR==2 {print $5}' | tr -d '%')

if [ "$usage" -gt 90 ]; then
  df -h | neomutt \
    --subject "ALERT: Disk usage at ${usage}%" \
    -- admin@example.com
fi
```

### Cron Job Reports

```sh
# In crontab: send a daily summary at 8am
0 8 * * * /usr/local/bin/daily-summary.sh | neomutt --subject "Daily Summary — $(date +\%F)" -- team@example.com
```

### Build Notifications

```sh
#!/bin/sh
# notify-build.sh — run after a CI build

if make all 2>&1 | tee /tmp/build.log; then
  echo 'Build succeeded.' | \
    neomutt --subject 'Build OK' -- dev@example.com
else
  neomutt --subject 'BUILD FAILED' \
    --include /tmp/build.log \
    -- dev@example.com
fi
```

### Sending Without a Config File

For minimal automation environments, you can use `--command` to set config
options inline:

```sh
echo 'Test message' | \
  neomutt --no-system-config \
    --command 'set sendmail = "/usr/sbin/sendmail -oem -oi"' \
    --command 'set from = "noreply@example.com"' \
    --command 'set realname = "Automated Sender"' \
    --subject 'Automated Message' \
    -- recipient@example.com
```

Or point to a dedicated config file:

```sh
echo 'Server alert' | \
  neomutt --config /etc/neomutt/alerts.rc \
    --subject 'Alert' \
    -- ops@example.com
```

---

## Complete Examples

Here are realistic, end-to-end examples that combine multiple options.

### Send a Report with Attachments

```sh
neomutt \
  --subject 'Q1 Financial Report' \
  --cc cfo@example.com \
  --bcc archive@example.com \
  --include cover-letter.txt \
  --attach q1-report.pdf q1-spreadsheet.xlsx \
  -- board@example.com
```

This sends an email to the board, Cc's the CFO, Bcc's the archive, uses the
cover letter as the body, and attaches the report and spreadsheet.

### Pipe a Log and Attach the Full File

```sh
tail -20 /var/log/errors.log | \
  neomutt \
    --subject 'Error Summary — Last 20 Lines' \
    --attach /var/log/errors.log \
    -- support@example.com
```

The email body contains the last 20 lines, and the full log file is
attached.

### Send an Encrypted Draft with Attachments

```sh
neomutt --crypto \
  --draft confidential-memo.eml \
  --attach evidence-a.pdf evidence-b.pdf \
  -- lawyer@example.com
```

### Compose Interactively with Pre-filled Fields

```sh
neomutt \
  --subject 'Follow-up from our call' \
  --cc assistant@example.com \
  --include call-notes.txt \
  -- client@example.com
```

NeoMutt opens the compose screen with the subject, Cc, and body already filled in.
You can edit the body, add more attachments, and adjust recipients before sending.

### Script-Generated Draft

```sh
#!/bin/sh
# Generate and send a personalised draft

for name in Alice Bob Carol; do
  email=$(echo "$name" | tr 'A-Z' 'a-z')@example.com

  cat > /tmp/draft-${name}.eml <<EOF
To: ${email}
Subject: Your Personalised Invitation

Dear ${name},

You are invited to the annual company picnic on Saturday.
Please RSVP by Friday.

Best regards,
The Events Team
EOF

  neomutt --draft /tmp/draft-${name}.eml
  rm /tmp/draft-${name}.eml
done
```

### Using an Alternate Config for a Work Account

```sh
neomutt --config ~/.config/neomutt/work.rc \
  --subject 'Expense Claim' \
  --attach receipts.pdf \
  -- expenses@company.com
```

---

## Configuration That Affects Sending

These `~/.neomuttrc` settings are most relevant to command-line sending:

### Mail Delivery

```neomuttrc
# Use a local sendmail program
set sendmail = "/usr/sbin/sendmail -oem -oi"

# Or use an SMTP server directly
set smtp_url = "smtps://you@smtp.example.com:465"
set smtp_pass = "your-password"
```

### Sent Mail Copy

```neomuttrc
# Folder where sent messages are saved
set record = "~/Mail/sent"

# Whether to save sent messages (yes, no, or ask)
set copy = yes
```

### Your Identity

```neomuttrc
set from = "you@example.com"
set realname = "Your Name"
```

### Editor

```neomuttrc
# Editor used for composing messages
set editor = "nano"
```

### Signature

```neomuttrc
# Signature file appended to outgoing messages
set signature = "~/.signature"

# Add '-- ' separator before signature
set sig_dashes = yes
```

### Crypto Defaults

```neomuttrc
# Automatically sign outgoing messages
set crypt_auto_sign = yes

# Encrypt when the recipient's key is available
set crypt_opportunistic_encrypt = yes

# Prefer PGP over S/MIME
set crypt_auto_pgp = yes
set crypt_auto_smime = no
```

---

## Option Quick Reference

```
neomutt [<address> ...] [options] [-- <address> ...]

Send Options:
  -s, --subject <text>          Set the Subject: header
  -a, --attach <file> [...]     Attach files (end list with -- or -X)
  -c, --cc <address>            Add a Cc: recipient (repeatable)
  -b, --bcc <address>           Add a Bcc: recipient (repeatable)
  -i, --include <file>          Use a file as the message body
  -H, --draft <file>            Load a complete draft (headers + body)
  -E, --edit-message            Edit the draft/include file in place
  -C, --crypto                  Apply crypto settings (sign/encrypt)

Useful Shared Options:
  -F, --config <file>           Use a custom config file
  -e, --command <command>       Run a config command
  -n, --no-system-config        Skip the system config file
```

---

## Troubleshooting

### "No recipients specified"

You forgot to provide a To: address.
Add one after `--`:
```sh
neomutt --subject 'Hello' -- someone@example.com
```

### Email not sending in batch mode

Check that your sendmail or SMTP settings are correct:

```sh
neomutt --query sendmail smtp_url
```

### Attachments not found

NeoMutt looks for files relative to your current directory.
Use full paths to be safe:

```sh
neomutt --attach /home/you/Documents/file.pdf -- recipient@example.com
```

### Editor not opening

If NeoMutt sends without opening an editor, you're likely in batch mode because something is connected to stdin.
Make sure stdin is a terminal:

```sh
# This enters batch mode (stdin is a pipe)
echo 'text' | neomutt --subject 'Hi' -- alice@example.com

# This opens the editor (stdin is a terminal)
neomutt --subject 'Hi' -- alice@example.com
```

### "Can't use -E flag with stdin"

You cannot combine `--edit-message` with piped input.
Write the input to a file first:

```sh
# Instead of this (which fails):
echo 'text' | neomutt --edit-message --include - -- alice@example.com

# Do this:
echo 'text' > /tmp/body.txt
neomutt --edit-message --include /tmp/body.txt -- alice@example.com
```

---

## See Also

- [Command-Line Options](cli-syntax.md) — complete reference of all NeoMutt options
- [NeoMutt Manual](https://neomutt.org/guide/) — full documentation
- [Configuration Guide](https://neomutt.org/guide/configuration) — setting up your `~/.neomuttrc`
