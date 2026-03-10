---
title: About OAuth2 in NeoMutt
description: How OAuth2 authentication works in NeoMutt and why it is implemented via external helpers
---

# About OAuth2 in NeoMutt

OAuth2 exists to replace long-lived passwords with short-lived access tokens. This matters for mail protocols because IMAP, POP, and SMTP all authenticate early in the session and historically relied on reusable passwords. Modern providers now prefer OAuth2 tokens, which limits exposure if credentials leak.

## OAUTHBEARER and XOAUTH2

NeoMutt supports two SASL mechanisms for OAuth2: `OAUTHBEARER` and `XOAUTH2`. Both carry an access token over the protocol, but they differ in history and server support. Some providers still only support XOAUTH2, while others support OAUTHBEARER. NeoMutt allows you to specify either (or both) in `imap_authenticators` and `smtp_authenticators` so it can negotiate successfully.

## Why NeoMutt Uses External Helpers

OAuth2 requires an out-of-band exchange to obtain tokens (browser-based authorization, device flow, or localhost callback). NeoMutt deliberately keeps this outside the core client, so it does not need to embed browser logic or provider-specific flows. Instead, it calls a helper script that returns an access token when needed. This makes the core code stable while still supporting provider changes over time.

## Token Lifecycles and Refresh

Access tokens are short-lived. The helper script stores a refresh token and uses it to fetch new access tokens automatically. NeoMutt calls the refresh command on each connection attempt, which keeps authentication fresh without embedding secrets in the main config.

## Where OAuth2 Fits in the Config Model

OAuth2 integration relies on the same configuration model as other credentials:

- `imap_oauth_refresh_command` and `smtp_oauth_refresh_command` point to helper scripts.
- `imap_authenticators` and `smtp_authenticators` select OAuth-capable mechanisms.
- `account_command` can also provide credentials, but OAuth2 helpers are more common for modern providers.

For the practical setup steps, see [How to Use OAuth Authentication](../howto/oauth) and the Gmail/Office 365 tutorials.

## Security Considerations

OAuth2 reduces the need for reusable passwords, but it does not eliminate risk. Token files should be protected, and any helper script should store secrets securely (e.g., GPG-encrypted token stores). If you are using a shared machine, avoid storing tokens in world-readable locations.

## See Also

- [How to Use OAuth Authentication](../howto/oauth)
- [Setting Up NeoMutt with Gmail](../tutorials/gmail-setup)
- [Setting Up NeoMutt with Office 365](../tutorials/office365-setup)
