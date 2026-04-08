---
title: Compose Flow
description: Understand the step-by-step order of header setting, hook execution, and encryption during message composition
keywords: compose, send, hooks, send-hook, reply-hook, send2-hook, fcc-hook, fcc, message flow, compose menu, editor, encryption, signing, my-header, reverse_name, fcc_before_send
---

# Compose Flow

This is a brief overview of the steps NeoMutt takes during message composition.
It also shows the order and timing of hook execution.

1. **Reply envelope settings.**
   [`$reverse_name`](cfg-reverse-name) processing. To, Cc, Subject, References header defaults.

2. **my-header processing** for To, Cc, Bcc, Subject headers.

3. **Prompts for To, Cc, Bcc, Subject headers.**
   See [`$ask_cc`](cfg-ask-cc), [`$ask_bcc`](cfg-ask-bcc), [`$fast_reply`](cfg-fast-reply).

4. **From header setting.**
   Note: this is so **send-hook**s below can match `~P`, but From is re-set
   further below in case a send-hook changes the value.

5. **reply-hook**

6. **send-hook**

7. **From header setting.**

8. **my-header processing** for From, Reply-To, Message-ID and user-defined
   headers. The To, Cc, Bcc, Subject, and Return-Path headers are ignored at this stage.

9. **Message body and signature generation.**

10. **send2-hook**

11. **[`$real_name`](cfg-real-name) part of From header setting.**

12. **[`$editor`](cfg-editor) invocation** for the message.

13. **send2-hook**

14. **Cryptographic settings.**

15. **fcc-hook.** Fcc setting.

16. **Compose menu.** Note: **send2-hook** is evaluated each time the headers are changed.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Compose menu during message composition

**Description:** The NeoMutt compose screen at step 16 of the flow, showing all header fields (From, To, Cc, Bcc, Subject, Reply-To, Fcc), the security/encryption settings, and the attachment list.
The message has been edited and is ready for final review before sending.

**Highlights:** The complete compose menu layout — header fields at the top, attachment list below, and the available key bindings (send, edit, attach, postpone, etc.) in the help bar.
This is the stage where `send2-hook` fires on each header change.
:::

17. **Message encryption and signing.** Key selection.

18. **Fcc saving** if [`$fcc_before_send`](cfg-fcc-before-send) is set.
  (Note the variable documentation for caveats of Fcc'ing before sending.)

19. **Message sending.**

20. **Fcc saving** if [`$fcc_before_send`](cfg-fcc-before-send) is unset (the default).
   The Fcc used to be saved before sending the message.
   It is now by default saved afterwards, but if the saving fails, the user is prompted.
