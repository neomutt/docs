---
title: How to Use the Trash Folder
description: Automatically move deleted emails to a trash bin instead of permanently removing them
keywords: trash, delete, purge, purge-message, trash folder, undelete
---

# How to Use the Trash Folder

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

## Introduction

In NeoMutt, when you "delete" an email it is first marked deleted. The email isn't really gone until `<sync-mailbox>` is called. This happens when the user leaves the folder, or the function is called manually.

After `<sync-mailbox>` has been called the email is gone forever.

The `$trash` variable defines a folder in which to keep old emails. As before, first you mark emails for deletion. When `<sync-mailbox>` is called the emails are moved to the trash folder.

The `$trash` path can be either a full directory, or be relative to the `$folder` variable, like the `mailboxes` command.

:::{note}
Emails deleted from the trash folder are gone forever.
:::

## Variables

| Name | Type | Default |
|------|------|---------|
| trash | string | (none) |

## Functions

| Menus | Default Key | Function | Description |
|-------|-------------|----------|-------------|
| index,pager | (none) | `<purge-message>` | really delete the current entry, bypassing the trash folder |

## neomuttrc

```
# Example NeoMutt config file for the 'trash' feature.

# This feature defines a new 'trash' folder.

# When mail is deleted it will be moved to this folder.

# Folder in which to put deleted emails
set trash='+Trash'
set trash='/home/flatcap/Mail/Trash'
# The default delete key 'd' will move an email to the 'trash' folder
# Bind 'D' to REALLY delete an email
bind index D purge-message
# Note: Deleting emails from the 'trash' folder will REALLY delete them.

# vim: syntax=neomuttrc
```

## See Also

- {ref}`folder-hook <folder-hook>`

## Known Bugs

None

## Credits

Cedric Duval, Benjamin Kuperman, Paul Miller, Richard Russon
