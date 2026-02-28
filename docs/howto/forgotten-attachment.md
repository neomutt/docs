---
title: How to Detect Forgotten Attachments
description: Alert the user when they forget to attach a file to an outgoing email in NeoMutt
keywords: forgotten attachment, abort_noattach, attachment reminder, regex
---

# How to Detect Forgotten Attachments

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

## Introduction

The "forgotten-attachment" feature provides a new setting for NeoMutt that alerts the user if
the message body contains a certain keyword but there are no attachments added. This is meant
to ensure that the user does not forget to attach a file after promising to do so in the mail.
The attachment keyword will not be scanned in text matched by
{ref}`$quote_regex <quote-regex>`.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Forgotten attachment warning prompt

**Description:** The NeoMutt screen showing the abort prompt that appears when the user tries to send a message containing an attachment keyword (e.g., "see attached") but no files are attached. The prompt at the bottom of the screen asks whether to abort sending.

**Highlights:** The warning prompt triggered by `$abort_noattach`, showing the quadoption question that lets the user choose to abort or proceed with sending the message without an attachment.
:::

## Variables

| Name                   | Type               | Default                                      |
|------------------------|--------------------|----------------------------------------------|
| `abort_noattach_regex` | regular expression | `\\<(attach\|attached\|attachments?)\\>`     |
| `abort_noattach`       | quadoption         | `no`                                         |

## neomuttrc

```
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

# vim: syntax=neomuttrc
```

## See Also

- {ref}`The Attachment Menu <attach-menu>`
- {ref}`The Attachment Menu key mappings <attachment-map>`

## Known Bugs

None

## Credits

Darshit Shah, Richard Russon, Johannes Weißl, Steven Ragnarök
