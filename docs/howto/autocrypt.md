---
title: "Set Up Autocrypt"
description: Enable and configure Autocrypt for automatic opportunistic email encryption in NeoMutt
keywords: neomutt, autocrypt, encryption, gpgme, ecc, opportunistic, keys
---

# Set Up Autocrypt

## Overview

NeoMutt can be compiled with Autocrypt support by running `configure` with the `--autocrypt` flag.
Autocrypt provides easy to use, passive protection against data collection.
Keys are distributed via an `Autocrypt:` header added to emails.
It does *not* protect against active adversaries, and so should not be considered a substitute for normal encryption via your keyring, using key signing and the web of trust to verify identities.
With an understanding of these limitations, Autocrypt still provides an easy way to minimize cleartext emails sent between common correspondents, without having to explicitly exchange keys.
More information can be found at [https://autocrypt.org/](https://autocrypt.org/).

## Prerequisites

- **GnuPG 2.1 or greater** — Autocrypt requires support for ECC cryptography, and NeoMutt by default will generate ECC keys.
- **GPGME 1.8.0 or later** — NeoMutt's Autocrypt implementation uses GPGME.
- **SQLite3** — Account and peer information is stored in a sqlite3 database.
   NeoMutt must be configured with `--with-sqlite` when autocrypt is enabled.
- **IDN2 support** (recommended) — Configure NeoMutt with `--idn2` (enabled by default) so that Autocrypt can properly deal with international domain names.
- While NeoMutt uses GPGME for Autocrypt, normal keyring operations can still be performed via classic mode (i.e. with `$crypt_use_gpgme` unset).
   However, to avoid unnecessary prompts, it is recommended gpg not be configured in `loopback pinentry` mode, and that `$pgp_use_gpg_agent` remain set (the default).

## First Run

1. Set `$autocrypt` in your `neomuttrc`, and optionally change the value of
   `$autocrypt_dir`:

   ```neomuttrc
   set autocrypt
   # set autocrypt_dir = "~/.local/share/autocrypt"
   ```

2. The first time NeoMutt is run after that, you will be prompted to create
   `$autocrypt_dir`. NeoMutt will then automatically create an sqlite3 database
   and GPG keyring in that directory. Since these files should be considered
   private, NeoMutt will create this directory with mode `700`. If you create
   the directory manually, you should do the same.

3. NeoMutt recommends keeping the `$autocrypt_dir` directory set differently
   from your GnuPG keyring directory (e.g. `~/.gnupg`). Keys are automatically
   imported into the keyring from `Autocrypt:` headers. Compared to standard
   "web of trust" keys, Autocrypt keys are somewhat ephemeral, and the autocrypt
   database is used to track when keys change or fall out of use. Having these
   keys mixed in with your normal keyring will make it more difficult to use
   features such as `$crypt_opportunistic_encrypt` and Autocrypt at the same
   time.

4. The `$autocrypt_dir` variable is not designed to be changed while NeoMutt is
   running. The database is created (if necessary) and connected to during
   startup. Changing the variable can result in a situation where NeoMutt is
   looking in one place for the database and a different place for the GPG
   keyring, resulting in strange behavior.

5. Once the directory, keyring, and database are created, NeoMutt will ask
   whether you would like to create an account. In order to use Autocrypt, each
   sending address needs an account. As a convenience you can create an account
   during the first run. If you would like to add additional accounts later,
   this can be done via the `<autocrypt-acct-menu>` function in the index, by
   default bound to `A`.

6. Account creation will first ask you for an email address. Next, it will ask
   whether you want to create a new key or select an existing key. (Note key
   selection takes place from the `$autocrypt_dir` keyring, which will normally
   be empty during first run). Finally, it will ask whether this address should
   prefer encryption or not. Autocrypt 1.1 allows automatically enabling
   encryption if *both* sender and receiver have set "prefer encryption".
   Otherwise, you will need to manually enable autocrypt encryption in the
   compose menu.

7. After optionally creating an account, NeoMutt will prompt you to scan
   mailboxes for Autocrypt headers. This step occurs because header cached
   messages are not re-scanned for Autocrypt headers. Scanning during this step
   will temporarily disable the header cache while opening each mailbox. If you
   wish to do this manually later, you can simulate the same thing by unsetting
   `$header_cache` and opening a mailbox.

:::{note}
The first run process takes place between reading the neomuttrc and opening the initial mailbox.
Some neomuttrc files will `push` macros to be run after opening the mailbox.
To prevent this from interfering with the first run prompts, NeoMutt disables all macros during the first run.
:::

## Compose Menu

When enabled, Autocrypt will add a line to the compose menu with two fields: `Autocrypt:` and `Recommendation:`.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Compose menu with Autocrypt fields

**Description:** The NeoMutt compose screen with Autocrypt enabled, showing the additional `Autocrypt:` and `Recommendation:` fields alongside the standard header fields (From, To, Cc, Subject, Fcc).
The `Autocrypt:` field displays "Off" and the `Recommendation:` field shows a value such as "Available" or "Yes".

**Highlights:** The two Autocrypt-specific fields in the compose header area, showing how they integrate with the standard compose layout and provide at-a-glance encryption status.
:::

### The Autocrypt Field

The `Autocrypt:` field shows whether the message will be encrypted by Autocrypt when sent.
It has two values: `Encrypt` and `Off`. `Encrypt` can be enabled using the `<autocrypt-menu>` function, by default bound to `o`.

### The Recommendation Field

The `Recommendation:` field shows the output of the Autocrypt recommendation engine.
This can have one of five values:

- **`Off`** — The engine is disabled. This can happen if the From address doesn't have an autocrypt account, or if the account has been manually disabled.
- **`No`** — One or more recipients are missing an autocrypt key, or the key found is unusable (i.e. expired, revoked, disabled, invalid, or not usable for encryption).
- **`Discouraged`** — A key was found for every recipient, but the engine is not confident the message will be decryptable by the recipient.
   This can happen if the key hasn't been used recently (compared to their last seen email).
   It can also happen if the key wasn't seen first-hand from the sender.
   Autocrypt has a feature where recipient keys can be included in group-encrypted emails.
   This allows you to reply to a conversation where you don't have a key first-hand from one of the other recipients.
   However, those keys are not trusted as much as from first-hand emails, so the engine warns you with a `Discouraged` status.
- **`Available`** — A key was found for every recipient, and the engine believes all keys are recent and seen from the recipient first hand.
   However, either you or one of the recipients chose not to specify "prefer encryption".
- **`Yes`** — The same as `Available`, with the addition that you and all recipients have specified "prefer encryption".
   This value will automatically enable encryption, unless you have manually switched it off or enabled regular encryption or signing via the `<pgp-menu>`.

### Changing the Autocrypt Encryption Setting

The `<autocrypt-menu>` function, by default bound to `o`, can be used to change the `Encrypt:` field value:

- **(e)ncrypt** — toggle encryption on
- **(c)lear** — toggle encryption off
- **(a)utomatic** — set the value based on the recommendation engine's output

If either `(e)ncrypt` or `(c)lear` are chosen, the field will remain in that state despite what the `Recommendation:` field shows.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Autocrypt encryption toggle menu

**Description:** The NeoMutt Autocrypt menu popup in the compose screen, triggered by pressing `o`.
The menu shows the three options: (e)ncrypt, (c)lear, and (a)utomatic.
The compose screen is visible in the background with the Autocrypt fields.

**Highlights:** The three toggle options and how the current selection affects the `Autocrypt:` field value in the compose header.
:::

### Interaction with Normal Encryption

Autocrypt encryption defers to normal encryption or signing. *Anything* that enables normal encryption or signing will cause autocrypt encryption to turn off.
The only exception is when replying to an autocrypt-encrypted email (i.e. an email decrypted from the `$autocrypt_dir` keyring).
Then, if `$autocrypt_reply` is *set*, autocrypt mode will be forced on, overriding the settings `$crypt_auto_sign`, `$crypt_auto_encrypt`, `$crypt_reply_encrypt`, `$crypt_reply_sign`, `$crypt_reply_sign_encrypted`, and `$crypt_opportunistic_encrypt`.

### Postponing Messages

When postponing a message, autocrypt will respect `$postpone_encrypt`, but will use the autocrypt account key to encrypt the message.
Be sure to set `$postpone_encrypt` to ensure postponed messages marked for autocrypt encryption are encrypted.

## Account Management

The Autocrypt Account Menu is available from the index via `<autocrypt-acct-menu>`, by default bound to `A`.
See the Autocrypt Account Menu for the list of functions and their default keybindings.

In this menu, you can:

- Create new accounts
- Delete accounts
- Toggle an account active/inactive
- Toggle the "prefer encryption" flag for an account

Deleting an account only removes the account from the database.
The GPG key is kept, to ensure you still have the ability to read past encrypted emails.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Autocrypt Account Menu

**Description:** The NeoMutt Autocrypt Account Menu accessed via `A` from the index.
The menu lists configured Autocrypt accounts with their email addresses, active/inactive status, and prefer-encryption flag.

**Highlights:** The account list with status indicators, and the available key bindings for creating, deleting, toggling active/inactive, and toggling the prefer-encryption flag.
:::

:::{note}
The Autocrypt 1.1 "Setup Message" feature is not available yet, but will be added in the future.
:::

## Alternative Key and Keyring Strategies

NeoMutt by default partitions Autocrypt from normal keyring encryption/signing.
It does this by using a separate GPG keyring (in `$autocrypt_dir`) and creating a new ECC key in that keyring for accounts.
There are good reasons for doing this by default:

- It keeps random keys found inside email headers out of your normal keyring.
- ECC keys are compact and better suited for email headers.
- Autocrypt key selection is completely different from "web of trust" key selection, based on last-seen rules as opposed to trust and validity.
- It also allows NeoMutt to distinguish Autocrypt encrypted emails from regular encrypted emails, and set the mode appropriately when replying to each type.

### Using an Existing Key from Your Normal Keyring

Some users may want to use an existing key from their normal keyring for Autocrypt too.
There are two ways this can be accomplished.

**Recommended method:** Set `$autocrypt_dir` to your normal keyring directory (e.g. `~/.gnupg`).
During account creation, choosing "(s)elect existing GPG key" will then list and allow selecting your existing key for the new account.

**Alternative method:** Copy your key over to the Autocrypt keyring.
However, there is a severe downside.
NeoMutt *first* tries to decrypt messages using the Autocrypt keyring, and if that fails tries the normal keyring second.
This means all encrypted emails to that key will be decrypted, and have signatures verified from, the Autocrypt keyring.
Key signatures and web of trust from your normal keyring will no longer show up in signatures when decrypting.

For that reason, if you want to use an existing key from your normal keyring, it is recommended to just set `$autocrypt_dir` to `~/.gnupg`.
This allows "web of trust" to show an appropriate signature message for verified messages.
Autocrypt header keys will be imported into your keyring, but if you don't want them mixed you should strongly consider using a separate autocrypt key and keyring instead.

### Caveats for Both Methods

- Replying to an Autocrypt decrypted message by default forces Autocrypt mode on.
   By sharing the same key, all replies will then start in Autocrypt mode, even if a message wasn't sent by one of your Autocrypt peers. `$autocrypt_reply` can be *unset* to allow manual control of the mode when replying.

- When NeoMutt creates an account from a GPG key, it exports the public key, base64 encodes it, and stores that value in the sqlite3 database.
   The value is then used in the Autocrypt header added to outgoing emails.
   The ECC keys NeoMutt creates don't change, but if you use external keys that expire, when you resign to extend the expiration you will need to recreate the Autocrypt account using the account menu.
   Otherwise the Autocrypt header will contain the old expired exported keydata.
