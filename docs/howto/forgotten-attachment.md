---
title: Detect Forgotten Attachments
description: Warn before sending when the message body mentions attachments but none are attached
keywords: forgotten attachment, abort_noattach, abort_noattach_regex, attachment reminder, regex, missing attachment, attachment warning, quadoption, send guard, quote_regex
---

# Detect Forgotten Attachments

## Introduction

The "forgotten-attachment" feature provides a new setting for NeoMutt that alerts the user if the message body contains a certain keyword but there are no attachments added.
This is meant to ensure that the user does not forget to attach a file after promising to do so in the mail.
The attachment keyword will not be scanned in text matched by [`$quote_regex`](cfg-quote-regex).

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Forgotten attachment warning prompt

**Description:** The NeoMutt screen showing the abort prompt that appears when the user tries to send a message containing an attachment keyword (e.g., "see attached") but no files are attached.
The prompt at the bottom of the screen asks whether to abort sending.

**Highlights:** The warning prompt triggered by [`$abort_noattach`](cfg-abort-noattach), showing the quadoption question that lets the user choose to abort or proceed with sending the message without an attachment.
:::

## Variables

| Name                   | Type               | Default                                  |
|------------------------|--------------------|------------------------------------------|
| `abort_noattach_regex` | regular expression | `\\<(attach\|attached\|attachments?)\\>` |
| `abort_noattach`       | quadoption         | `no`                                     |

## neomuttrc

```neomuttrc
# Example NeoMutt config file for the forgotten-attachment feature.

# The 'forgotten-attachment' feature provides a new setting for NeoMutt that
# alerts the user if the message body contains a certain regular expression but there are
# no attachments added. This is meant to ensure that the user does not forget
# to attach a file after promising to do so in the mail.

# Ask if the user wishes to abort sending if $abort_noattach_regex is found in the
# body, but no attachments have been added
# It can be set to:
#    "yes"     : always abort
#    "ask-yes" : ask whether to abort
#    "no"      : send the mail
set abort_noattach = no
# Search for the following regular expression in the body of the email
# English: attach, attached, attachment, attachments
set abort_noattach_regex = "\\<attach(|ed|ments?)\\>"
# Nederlands:
# set abort_noattach_regex = "\\<(bijvoegen|bijgevoegd|bijlage|bijlagen)\\>"
# Deutsch:
# set abort_noattach_regex = "\\<(anhängen|angehängt|anhang|anhänge|hängt an)\\>"
# Français:
# set abort_noattach_regex = "\\<(attaché|attachés|attache|attachons|joint|jointe|joints|jointes|joins|joignons)\\>"

# vim: filetype=neomuttrc
```

## See Also

- **The Attachment Menu**
- **The Attachment Menu key mappings**

