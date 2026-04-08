---
title: History Dialog
description: The history picker for reusing past commands, searches, addresses, and other prompt input.
keywords: history, prompt, command line, search history, completion, reuse input
---

(tour-history)=
# History Dialog

## Introduction -- Where am I?

The History Dialog is the prompt history picker.
It appears when you ask NeoMutt to browse previous input for the current prompt category, such as commands, searches, filenames, or addresses.
Its purpose is to save typing and help you reuse complicated strings accurately.

<div class="term-window">
<div class="term-title">History Dialog</div>
<pre class="terminal">
<span>set alias_format                                                                                    </span>
<span>reset alias_format                                                                                  </span>
<span>set real_name="John Smith"                                                                          </span>
<span>set quit=ask-no                                                                                     </span>
<span>set all                                                                                             </span>
<span>reset folder_format                                                                                 </span>
<span>set folder_format="%2C %t %N %F %2l %-8.8u %-8.8g %8s %d %i"                                        </span>
<span>set hide_thread_subject=no                                                                          </span>
<span>set pager_index_lines=0                                                                             </span>
<span>reset status_format                                                                                 </span>
<span>                                                                                                    </span>
<span>                                                                                                    </span>
<span class="status">History 'set '                                                                                      </span>
<span class="prompt">:</span><span>set                                                                                                </span>
</pre>
</div>

## What am I looking at?

- The list shows prior inputs of the same history type, filtered by the text already present in the current prompt.
- The highlighted row is the history entry that will be inserted if you select it.
- The status line names the history category and the current filter text.
- The prompt line at the bottom shows the live input that will receive the selected history value.

## What can I do?

- Browse earlier commands, searches, addresses, filenames, and other prompt inputs.
- Reuse a previous entry without retyping it.
- Narrow the list by typing part of the text first, then opening history.
- Exit without changing the current prompt.
- Full reference: [Dialog Functions](fn-dialog), [Editor Functions](fn-editor).

## Where can I go next?

- Selecting an entry returns you to the [Message Window](message.md) prompt that opened history.
- Cancelling also returns you to the original prompt unchanged.

## Where did I come from?

- Any prompt handled by the [Message Window](message.md) can open history through editor history keys.
- Common sources are the command line, search prompts, limit prompts, filename prompts, and recipient-entry prompts.

## How do I configure this?

- Start with [History Config](ref-cfg-history).
- Common options include [`$history`](cfg-history), [`$history_file`](cfg-history-file), [`$history_format`](cfg-history-format), [`$history_remove_dups`](cfg-history-remove-dups), and [`$save_history`](cfg-save-history).
- History is usually tuned with generic commands such as [`:set`](cmd-set), [`:unset`](cmd-unset), and [`:reset`](cmd-reset).
- Colours come from [Colour Objects](ref-colors), especially `indicator`, `status`, `prompt`, `message`, and `normal`.
