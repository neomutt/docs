---
title: How to Use OAuth Authentication
description: Configure NeoMutt to use OAUTHBEARER or XOAUTH2 for IMAP, POP, and SMTP
keywords: oauth, oauthbearer, xoauth2, gmail, office365, imap_oauth_refresh_command
---

# How to Use OAuth Authentication

Preliminary OAUTH support for IMAP, POP, and SMTP is provided via external scripts.

## Setting Up OAuth for Gmail

1. Download the `oauth2.py` script from Google's gmail-oauth2-tools:
   [https://github.com/google/gmail-oauth2-tools/blob/master/python/oauth2.py](https://github.com/google/gmail-oauth2-tools/blob/master/python/oauth2.py)

2. Get your own OAuth client credentials for Gmail here:
   [https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials)

3. Use `oauth2.py` with `--generate_oauth2_token` to get a refresh token.

4. Configure NeoMutt:

   ```neomuttrc
   set imap_authenticators="oauthbearer"
   set imap_oauth_refresh_command="/path/to/oauth2.py --quiet --user=[email_address]\
       --client_id=[client_id] --client_secret=[client_secret]\
       --refresh_token=[refresh_token]"
   ```

## Setting Up OAuth for Office365

1. Download the `mutt_oauth2.py` script written by Alexander Perlis:
   [https://github.com/neomutt/neomutt/blob/main/contrib/oauth2/mutt_oauth2.py](https://github.com/neomutt/neomutt/blob/main/contrib/oauth2/mutt_oauth2.py)

2. Get your own OAuth client credentials by following the script instructions:
   [https://github.com/neomutt/neomutt/blob/main/contrib/oauth2/README.md](https://github.com/neomutt/neomutt/blob/main/contrib/oauth2/README.md)

3. Configure NeoMutt:

   ```neomuttrc
   set imap_authenticators="xoauth2"
   set imap_oauth_refresh_command="/path/to/mutt_oauth2.py /path/to/token"
   ```

## Configuring for POP and SMTP

Substitute `pop` or `smtp` for `imap` in the above examples to configure for those protocols.

:::{note}
XOAUTH2 support has not yet been implemented for POP.
:::
