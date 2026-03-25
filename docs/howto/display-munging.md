---
title: How to Transform Message Display
description: Use subject-regex to modify how message subjects are displayed in NeoMutt
keywords: subject-regex, display munging, subject, regex, replacement, unsubject-regex
---

# How to Transform Message Display

## Display Munging

Working within the confines of a console or terminal window, it is often useful to be able to modify certain information elements in a non-destructive way — to change how they display, without changing the stored value of the information itself.
This is especially so of message subjects, which may often be polluted with extraneous metadata that either is reproduced elsewhere, or is of secondary interest.

**Usage:**

```neomuttrc
subject-regex regex replacement
unsubject-regex { * | regex }
```

:::{note}
Before 2026-01-13, these commands were called `subjectrx` and `unsubjectrx`.
:::

`subject-regex` specifies a regular expression which, if detected in a message subject, causes the subject to be replaced with the "replacement" value.
The replacement is subject to substitutions in the same way as for the **spam** command: `%L` for the text to the left of the match, `%R` for text to the right of the match, and `%1` for the first subgroup in the match (etc).
If you simply want to erase the match, set it to `%L%R`.
Any number of `subject-regex` commands may coexist.

:::{important}
The "replacement" value replaces the **entire** subject, not just the match!
:::

`unsubject-regex` removes a given subject-regex from the substitution list.
If `*` is used as the argument, all substitutions will be removed.

:::{admonition} Example: Subject Munging
:class: tip

```neomuttrc
# Erase [rt #12345] tags from Request Tracker (RT) e-mails
subject-regex '\[rt #[0-9]+\] *' '%L%R'
# Servicedesk is another RT that sends more complex subjects.
# Keep the ticket number.
subject-regex '\[servicedesk #([0-9]+)\] ([^.]+)\.([^.]+) - (new|open|pending|update) - ' '%L[#%1] %R'
# Strip out annoying [listname] prefixes in subjects
subject-regex '\[[^]]*\]:? *' '%L%R'
```
:::

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Index with transformed subject lines

**Description:** NeoMutt index view showing messages from a mailing list where `subject-regex` rules have been applied — the `[listname]` prefixes and `[rt #12345]` tags are stripped from subject lines, leaving clean, readable subjects.
Ideally a before/after comparison.

**Highlights:** The cleaner subject column after munging — list prefixes and ticket-system tags are gone, making subjects easier to scan in the index.
:::
