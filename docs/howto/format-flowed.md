---
title: Send Format=Flowed Messages
description: Compose and display format=flowed (f=f) text/plain messages with paragraph reflowing and space-stuffing
keywords: format=flowed, f=f, text_flowed, reflow, rfc3676, space-stuffing, reflow_text, reflow_wrap, reflow_space_quotes, paragraph, line wrapping, plain text, vim formatoptions
---

# Send Format=Flowed Messages

## Concept

`format=flowed`-style messages (or `f=f` for short) are `text/plain` messages that consist of paragraphs which a receiver's mail client may reformat to its own needs, which mostly means to customize line lengths regardless of what the sender sent.
Technically this is achieved by letting lines of a "flowable" paragraph end in spaces except for the last line.

While for text-mode clients like NeoMutt it's best to assume only a standard 80×24 character cell terminal, it may be desired to let the receiver decide completely how to view a message.

## NeoMutt Support

NeoMutt only supports setting the required `format=flowed` MIME parameter on outgoing messages if the {ref}`$text_flowed <cfg-text-flowed>` variable is set, specifically it does not add the trailing spaces.

After editing, NeoMutt properly space-stuffs the message.
*Space-stuffing* is required by [RFC3676](https://www.rfc-editor.org/rfc/rfc3676.html), defining `format=flowed`, and means to prepend a space to:

- all lines starting with a space
- lines starting with the word `From` followed by space
- all lines starting with `>`, which is not intended to be a quote character

:::{note}
NeoMutt only supports space-stuffing for the first two types of lines but not for the third: It is impossible to safely detect whether a leading `>` character starts a quote or not.
:::

All leading spaces are to be removed by receiving clients to restore the original message prior to further processing.

## Editor Considerations

As NeoMutt provides no additional features to compose `f=f` messages, it's completely up to the user and his editor to produce proper messages.
Please consider your editor's documentation if you intend to send `f=f` messages.

For example, *vim* provides the `w` flag for its `formatoptions` setting to assist in creating `f=f` messages, see `:help fo-table` for details.

## Reformatting

NeoMutt has some support for reformatting when viewing and replying to `format=flowed` messages.
In order to take advantage of these, {ref}`$reflow_text <cfg-reflow-text>` must be set.

- Paragraphs are automatically reflowed and wrapped at a width specified by {ref}`$reflow_wrap <cfg-reflow-wrap>`.
- In its original format, the quoting style of `format=flowed` messages can be difficult to read, and doesn't intermix well with non-flowed replies.
   Setting {ref}`$reflow_space_quotes <cfg-reflow-space-quotes>` adds spaces after each level of quoting when in the pager and replying in a non-flowed format (i.e. with {ref}`$text_flowed <cfg-text-flowed>` unset).
- If {ref}`$reflow_space_quotes <cfg-reflow-space-quotes>` is unset, NeoMutt will still add one trailing space after all the quotes in the pager (but not when replying).

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Flowed vs fixed text in the pager

**Description:** The NeoMutt pager showing a format=flowed message with `$reflow_text` enabled, demonstrating how paragraphs are reflowed and wrapped cleanly to the terminal width.
Ideally show a quoted reply with `$reflow_space_quotes` set, displaying the added spaces between quote level markers.

**Highlights:** How reflowed paragraphs wrap cleanly compared to fixed-width text with hard line breaks, and how `$reflow_space_quotes` improves readability by adding spaces after `>` quote markers.
:::
