---
title: How to Use the Compose Flow
description: Understand the order of steps and hook execution during NeoMutt message composition
keywords: compose, send, hooks, send-hook, reply-hook, fcc, message flow
---

# How to Use the Compose Flow

:::{admonition} Diátaxis: How-To Guide
:class: note

Write as **directions**. Assume the reader is competent and knows what they want to achieve.
Be practical and goal-focused. Use numbered steps for procedures. Don't explain why — link
to explanation pages instead. Keep it focused on the specific task. Start with prerequisites,
give the steps, show the expected result.
:::

This is a brief overview of the steps NeoMutt takes during message composition. It also
shows the order and timing of hook execution.

1. **Reply envelope settings.**
   {ref}`$reverse_name <reverse-name>` processing. To, Cc, Subject, References header defaults.

2. **{ref}`my-header <my-header>` processing** for To, Cc, Bcc, Subject headers.

3. **Prompts for To, Cc, Bcc, Subject headers.**
   See {ref}`$ask_cc <ask-cc>`, {ref}`$ask_bcc <ask-bcc>`, {ref}`$fast_reply <fast-reply>`.

4. **From header setting.**
   Note: this is so {ref}`send-hook <send-hook>`s below can match `~P`, but From is re-set
   further below in case a send-hook changes the value.

5. **{ref}`reply-hook <reply-hook>`**

6. **{ref}`send-hook <send-hook>`**

7. **From header setting.**

8. **{ref}`my-header <my-header>` processing** for From, Reply-To, Message-ID and user-defined
   headers. The To, Cc, Bcc, Subject, and Return-Path headers are ignored at this stage.

9. **Message body and signature generation.**

10. **{ref}`send2-hook <send2-hook>`**

11. **{ref}`$real_name <real-name>` part of From header setting.**

12. **{ref}`$editor <editor>` invocation** for the message.

13. **{ref}`send2-hook <send2-hook>`**

14. **Cryptographic settings.**

15. **{ref}`fcc-hook <fcc-hook>`.** Fcc setting.

16. **{ref}`Compose menu <compose-menu>`.** Note: {ref}`send2-hook <send2-hook>` is evaluated
    each time the headers are changed.

17. **Message encryption and signing.** Key selection.

18. **Fcc saving** if {ref}`$fcc_before_send <fcc-before-send>` is set. (Note the variable
    documentation for caveats of Fcc'ing before sending.)

19. **Message sending.**

20. **Fcc saving** if {ref}`$fcc_before_send <fcc-before-send>` is unset (the default). The Fcc
    used to be saved before sending the message. It is now by default saved afterwards, but if
    the saving fails, the user is prompted.
