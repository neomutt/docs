---
title: How to Use Delivery Status Notifications
description: Configure NeoMutt to request Delivery Status Notifications (DSN) for return receipts on sent messages
keywords: dsn, delivery status, notification, return receipt, sendmail, smtp
---

# How to Use Delivery Status Notifications

[RFC1894](https://www.rfc-editor.org/rfc/rfc1894.html) defines a set of MIME content types for relaying information about the status of electronic mail messages.
These can be thought of as "return receipts."

## Configure DSN Variables

To support DSN, there are two variables:

- `$dsn_notify` is used to request receipts for different results (such as failed message, message delivered, etc.).
- `$dsn_return` requests how much of your message should be returned with the receipt (headers or full message).

## Using Sendmail for Delivery

When using `$sendmail` for mail delivery, you need to use either Berkeley sendmail 8.8.x (or greater) or a MTA supporting DSN command line options compatible to Sendmail: The `-N` and `-R` options can be used by the mail client to make requests as to what type of status messages should be returned.
Please consider your MTA documentation whether DSN is supported.

## Using SMTP for Delivery

For SMTP delivery using `$smtp_url`, it depends on the capabilities announced by the server whether NeoMutt will attempt to request DSN or not.
