---
title: How to Set Up SMTP
description: Configure NeoMutt to deliver messages through an SMTP server
keywords: smtp, smtp_url, smtp_authenticators, sendmail, mail delivery
---

# How to Set Up SMTP

Besides supporting traditional mail delivery through a sendmail-compatible program, NeoMutt supports delivery through SMTP.

## Configuring SMTP Delivery

1. Set the `$smtp_url` variable to the SMTP server URL. If this is set, NeoMutt will contact the given SMTP server to deliver messages; if it is unset, NeoMutt will use the program specified by `$sendmail`.

   ```
   set smtp_url="smtps://user@smtp.example.com"
   ```

   For details on the URL syntax, see **URL syntax**.

2. The built-in SMTP support supports encryption (the `smtps` protocol using SSL or TLS) as well as SMTP authentication using SASL.

3. Optionally configure the authentication mechanisms for SASL in `$smtp_authenticators`. This defaults to an empty list which makes NeoMutt try all available methods from most-secure to least-secure.

   ```
   set smtp_authenticators="login"
   ```
