---
title: Compose Preview
description: Display a live preview of the email body inside the compose dialog before sending in NeoMutt
keywords: compose, preview, message preview, compose dialog, compose_show_preview, compose_preview_min_rows, compose_preview_above_attachments, preview-page-down, preview-page-up, email body, sending
since: 2024-12-12
---

# Compose Preview 🔥

## Support

**Since:** NeoMutt 2024-12-12

## Introduction

NeoMutt shows you a preview of the message you are about to send in the compose dialog.

## Variables

| Name                                | Type    | Default | Description                                               |
|-------------------------------------|---------|---------|-----------------------------------------------------------|
| `compose_preview_above_attachments` | boolean | `no`    | Show the message preview above the attachments list.      |
| `compose_preview_min_rows`          | number  | `5`     | Hide the preview if it has fewer than this number of rows |
| `compose_show_preview`              | boolean | `no`    | Enable or disable the message preview feature             |

## Functions

The message preview is controlled by the following functions.

| Menus   | Function              | Description                           | Default      |
|---------|-----------------------|---------------------------------------|--------------|
| compose | [`<preview-page-down>`](fn-preview-page-down) | Show the next page of the message     | {kbd}`<Page Down>` |
| compose | [`<preview-page-up>`](fn-preview-page-up)   | Show the previous page of the message | {kbd}`<Page Up>`   |

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Compose dialog with message preview

**Description:** The NeoMutt compose dialog with [`$compose_show_preview`](cfg-compose-show-preview) enabled.
The screen shows the message header fields at the top, the attachment list, and the message body preview pane displaying a portion of the email text.
Show the default layout with the preview below the attachment list.

**Highlights:** The message preview pane integrated into the compose dialog, showing how the email body appears before sending.
The preview can be repositioned above attachments with [`$compose_preview_above_attachments`](cfg-compose-preview-above-attachments), and scrolled with PageUp/PageDown.
:::

## Limitations

This is a new feature and it's still under development.
If you find any problems, or you'd like to help improve it, please let us know.

- Pager displays simple text, no colour or attributes
- Smart text wrapping is not supported

## Credits

Dennis Schön
