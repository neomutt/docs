---
title: Message Window
description: The prompt and status area NeoMutt uses for commands, searches, questions, progress, and temporary messages.
keywords: message window, prompt, status, command line, history, search, progress, editor
---

(tour-message)=
# Message Window

## Introduction -- Where am I?

The Message Window is the prompt-and-status area at the bottom of NeoMutt.
It is not a full dialog like the index or pager; instead, it is the place where NeoMutt asks questions, accepts typed input, reports status, and shows progress.
If NeoMutt needs a short answer from you, it usually appears here.

<div class="term-window">
<div class="term-title">Message Window</div>
<pre class="terminal" role="img" aria-label="Screenshot of NeoMutt's Message Window area at the bottom of the screen, showing the status bar above and the message/prompt line below.">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">Status Bar                                                                                          </span>
<span>Message Window                                                                                      </span>
</pre>
</div>

## What am I looking at?

- The status line shows short-lived information such as mailbox state, help, errors, and progress.
- The prompt line is where you type commands, searches, filenames, addresses, and answers to questions.
- Highlighted option characters in prompts show the valid one-key responses for yes/no and multi-choice questions.
- Depending on the prompt, this line can temporarily hand off to the [History Dialog](history.md), [Pattern Dialog](pattern.md), [Alias Dialog](alias.md), [Query Dialog](query.md), or [Browser Dialog](browser.md).

## What can I do?

- Enter NeoMutt commands with {kbd}`:` and answer free-form prompts such as searches, limits, addresses, and filenames.
- Use editor keys for cursor movement, deletion, history, completion, and query completion.
- Answer yes/no and multi-choice prompts that control quitting, crypto, flags, and other decisions.
- Watch transfer and background progress without leaving the current screen.
- Use `:exec what-key` to inspect how NeoMutt sees a key press.
- Full reference: [Editor Functions](menu-editor), [Generic Functions](menu-generic).

## Where can I go next?

- Submitting a prompt usually returns you to the dialog that asked the question, such as the [Index Dialog](index2.md), [Pager Dialog](pager.md), [Compose Dialog](compose.md), or [Browser Dialog](browser.md).
- Address completion can open the [Alias Dialog](alias.md) or [Query Dialog](query.md).
- Filename browsing can open the [Browser Dialog](browser.md).
- History keys can open the [History Dialog](history.md).
- Pattern help can open the [Pattern Dialog](pattern.md).

## Where did I come from?

- Almost every major dialog uses the message window for searches, limits, commands, confirmations, filenames, and recipient entry.
- The [Index Dialog](index2.md), [Pager Dialog](pager.md), and [Compose Dialog](compose.md) are the most common callers.

## How do I configure this?

- Start with [Editor Functions](menu-editor), [History Config](ref-cfg-history), [Pattern Options](ref-cfg-pattern), and [General Config](ref-cfg-general).
- Common options include [`$help`](cfg-help), [`$wait_key`](cfg-wait-key), [`$history`](cfg-history), [`$history_file`](cfg-history-file), [`$simple_search`](cfg-simple-search), and [`$external_search_command`](cfg-external-search-command).
- Useful commands include [`:set`](cmd-set), [`:unset`](cmd-unset), [`:toggle`](cmd-toggle), [`:exec`](cmd-exec), [`:echo`](cmd-echo), [`:bind`](cmd-bind), and [`:macro`](cmd-macro).
- Colours come from [Colour Objects](ref-colors), especially `prompt`, `options`, `message`, `warning`, `error`, `progress`, and `status`.

## Common Prompt Types

## Enter Command

Function `<enter-command>` (Key: {kbd}`:`)

<div class="term-window">
<pre class="terminal" role="img" aria-label="Screenshot of NeoMutt's Enter Command prompt showing a colon followed by the typed command echo hello.">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">:</span><span>echo "hello"                                                                                       </span>
</pre>
</div>

Type any NeoMutt command here, from quick experiments like `set` and `echo` to full configuration commands.

## Yes / No / Help

<div class="term-window">
<pre class="terminal" role="img" aria-label="Screenshot of a yes/no confirmation prompt asking Exit NeoMutt without saving, with yes as the default.">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">Exit NeoMutt without saving? ([yes]/no):</span><span>                                                            </span>
</pre>
</div>

Simple confirmation prompts usually accept one keypress, and some of them support {kbd}`?` for inline help about the option being asked.

<div class="term-window">
<pre class="terminal" role="img" aria-label="Screenshot of a quit confirmation prompt asking Quit NeoMutt with no as the default, and a question-mark option for inline help.">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">Quit NeoMutt? ([no]/yes/?): </span><span>                                                                        </span>
</pre>
</div>

<div class="term-window">
<pre class="terminal" role="img" aria-label="Screenshot of the same quit prompt after pressing question mark, showing inline help text explaining the quit config variable and a link to its documentation.">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span>$quit - Prompt before exiting NeoMutt                                                               </span>
<span>https://neomutt.org/guide/reference#quit                                                            </span>
<span class="prompt">Quit NeoMutt? ([no]/yes/?): </span><span>                                                                        </span>
</pre>
</div>

The inline help version is especially useful when a confirmation is driven by a configuration option you do not recognise.

## Multi-choice



<div class="term-window">
<pre class="terminal" role="img" aria-label="Screenshot of a PGP multi-choice prompt offering encrypt, sign, sign-as, both, S/MIME, or clear options, each activated by a single keypress.">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">PGP (e)ncrypt, (s)ign, sign (a)s, (b)oth, s/(m)ime or (c)lear? </span><span>                                     </span>
</pre>
</div>

Multi-choice prompts are common for crypto decisions, where a single keypress changes signing or encryption state.

<div class="term-window">
<pre class="terminal" role="img" aria-label="Screenshot of the same PGP multi-choice prompt with the shortcut letters e, s, a, b, m, and c highlighted in a different colour to indicate the valid single-key responses.">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">PGP </span><span class="prompt options">e</span><span class="prompt">ncrypt, </span><span class="prompt options">s</span><span class="prompt">ign, sign </span><span class="prompt options">a</span><span class="prompt">s, </span><span class="prompt options">b</span><span class="prompt">oth, s/</span><span class="prompt options">m</span><span class="prompt">ime or </span><span class="prompt options">c</span><span class="prompt">lear?</span><span>                                                  </span>
</pre>
</div>

## Custom Flags

<div class="term-window">
<pre class="terminal" role="img" aria-label="Screenshot of a custom flags prompt asking Set flag with single-character choices D, N, O, r, asterisk, and exclamation mark.">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">Set flag? (D/N/O/r/*/!):</span><span>                                                                            </span>
</pre>
</div>

Some prompts expect one short symbolic choice rather than free-form text.

## Free Form Question

<div class="term-window">
<pre class="terminal" role="img" aria-label="Screenshot of a free-form search prompt showing Search for followed by a text-entry cursor.">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="prompt">Search for: </span><span>                                                                                        </span>
</pre>
</div>

Searches, limits, addresses, filenames, and many configuration prompts use free-form entry with the full line editor.

## Progress Bar

<div class="term-window">
<pre class="terminal" role="img" aria-label="Screenshot of a progress bar showing Fetching message headers, 8806 of 37928 at 23 percent.">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span class="progress2">Fetching message headers... 8806</span><span>/37928 (23%)                                                        </span>
</pre>
</div>

Long-running operations such as fetching headers or sending large messages report progress here instead of interrupting the whole screen.

## What Key?

```
:exec what-key
```

<div class="term-window">
<pre class="terminal" role="img" aria-label="Screenshot of the what-key diagnostic showing the character f with its octal value 146 and decimal value 102, plus a prompt to enter more keys or press Ctrl-G to abort.">
<span class="index">                                                                                                    </span>
<span class="index">                                                                                                    </span>
<span class="status">                                                                                                    </span>
<span>Char = f, Octal = 146, Decimal = 102                                                                </span>
<span>Enter keys (^G to abort):                                                                           </span>
</pre>
</div>

This is the quickest way to discover how NeoMutt names a key before rebinding it.
