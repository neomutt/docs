---
title: Trash Folder
description: Automatically move deleted emails to a trash folder instead of permanently removing them, with purge-message for hard delete
keywords: trash, delete, purge, purge-message, trash folder, undelete, sync-mailbox, $trash, recycle bin, soft delete, deleted messages, folder-hook
---

# Trash Folder

## Introduction

In NeoMutt, when you "delete" an email it is first marked deleted.
The email isn't really gone until `<sync-mailbox>` is called.
This happens when the user leaves the folder, or the function is called manually.

After `<sync-mailbox>` has been called the email is gone forever.

The [`$trash`](cfg-trash) variable defines a folder in which to keep old emails.
As before, first you mark emails for deletion.
When `<sync-mailbox>` is called the emails are moved to the trash folder.

The [`$trash`](cfg-trash) path can be either a full directory, or be relative to the [`$folder`](cfg-folder) variable, like the `mailboxes` command.

:::{note}
Emails deleted from the trash folder are gone forever.
:::

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Trash folder in the sidebar

**Description:** The NeoMutt sidebar showing a list of mailboxes including a visible "Trash" folder entry with a message count, alongside other folders like Inbox, Sent, and Drafts.
The Trash folder should contain some messages to show it is in use.

**Highlights:** How the Trash folder appears as a regular mailbox in the sidebar, its unread/total message count, and how it fits into the overall mailbox hierarchy.
:::

## Variables

| Name  | Type   | Default |
|-------|--------|---------|
| trash | string | (none)  |

## Functions

| Menus       | Default Key | Function          | Description                                                 |
|-------------|-------------|-------------------|-------------------------------------------------------------|
| index,pager | (none)      | `<purge-message>` | really delete the current entry, bypassing the trash folder |

## neomuttrc

```neomuttrc
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

# vim: filetype=neomuttrc
```

## See Also

- **folder-hook**

