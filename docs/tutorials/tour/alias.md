---
title: Alias Dialog
description: NeoMutt's personal address book view for browsing, selecting, and mailing saved aliases.
keywords: alias, address book, contacts, compose, recipient completion, groups
---

(tour-alias)=
# Alias Dialog

## Introduction -- Where am I?

The Alias Dialog is NeoMutt's built-in address book.
It lists the aliases you have defined in your configuration and lets you choose one or more recipients when addressing a message.
You may also hear it described as the alias menu or contact list.

<div class="term-window">
<div class="term-title">Alias Dialog</div>
<pre class="terminal">
<span>  1    alp             Al Pacino &lt;alp@apple.com&gt;                                | oscar             </span>
<span>  2    amya            Amy Adams &lt;amya@hawthorn.com&gt;                            | oscar             </span>
<span>  3    angelab         Angela Bassett &lt;angelab@elderberry.com&gt;                  | emmy,oscar,tony   </span>
<span>  4    anneh           Anne Hathaway &lt;anneh@xigua.com&gt;                          | oscar,tony        </span>
<span>  5    anthonyh        Anthony Hopkins &lt;anthonyh@cherry.com&gt;                    | oscar             </span>
<span>  6    beniciot        Benicio del Toro &lt;beniciot@banana.com&gt;                   | oscar             </span>
<span>  7    billyt          Billy Bob Thornton &lt;billyt@apple.com&gt;                    | emmy,oscar        </span>
<span>  8    denzelw         Denzel Washington &lt;denzelw@ziziphus.com&gt;                 | oscar,tony        </span>
<span>  9    dianew          Diane Wiest &lt;dianew@apple.com&gt;                           | emmy,oscar        </span>
<span> 10    eddier          Eddie Redmayne &lt;eddier@wolfberry.com&gt;                    | oscar,tony        </span>
<span> 11    edh             Ed Harris &lt;edh@fig.com&gt;                                  | emmy,oscar        </span>
<span> 12    ellenb          Ellen Burstyn &lt;ellenb@kumquat.com&gt;                       | emmy,oscar        </span>
<span> 13    forestw         Forest Whitaker &lt;forestw@elderberry.com&gt;                 | oscar,tony        </span>
<span> 14    francism        Francis McDormand &lt;francism@guava.com&gt;                   | emmy,oscar        </span>
<span> 15    georgec         George Clooney &lt;georgec@yew.com&gt;                         | oscar,tony        </span>
<span> 16    glennc          Glenn Close &lt;glennc@kumquat.com&gt;                         | emmy,oscar,tony   </span>
<span> 17    hughg           Hugh Grant &lt;hughg@damson.com&gt;                            | oscar             </span>
<span> 18    hughj           Hugh Jackman &lt;hughj@lemon.com&gt;                           | grammy,oscar,tony </span>
<span> 19    jamesf          James Franco &lt;jamesf@xigua.com&gt;                          | oscar             </span>
<span> 20    jamiec          Jamie Lee Curtis &lt;jamiec@raspberry.com&gt;                  | emmy,oscar,tony   </span>
<span> 21    jamief          Jamie Foxx &lt;jamief@olive.com&gt;                            | emmy,grammy,oscar </span>
<span> 22    jessicac        Jessica Chastain &lt;jessicac@raspberry.com&gt;                | oscar             </span>
<span class="status">Aliases - Limit: ~Y oscar                                                                           </span>
<span class="prompt">To: </span><span>                                                                                                </span>
</pre>
</div>

## What am I looking at?

- The main list shows each alias key, the expanded real name and address, and any tags or groups.
- The highlighted row is the alias that will be inserted or acted on.
- The status line shows the current limit or sort state.
- The prompt line at the bottom reminds you which field is currently being completed.

## What can I do?

- Select one or more aliases to insert into a `To:`, `Cc:`, or `Bcc:` field.
- Compose a new message directly to the currently selected alias with `<mail>`.
- Limit, sort, tag, delete, and undelete alias entries while you browse.
- Use the dialog as a quick way to inspect how an alias expands before sending mail.
- Full reference: [Alias Functions](ref-fn-alias), [Generic Functions](ref-fn-generic).

## Where can I go next?

- Selecting entries usually returns you to the [Compose Dialog](compose.md) or the [Message Window](message.md) prompt that asked for recipients.
- `<mail>` opens the [Compose Dialog](compose.md) directly.
- `q` cancels and returns to the caller without inserting anything.

## Where did I come from?

- Address completion in the [Message Window](message.md) can open this dialog when NeoMutt finds multiple alias matches.
- Editing recipient fields in the [Compose Dialog](compose.md) can lead here through completion.
- Some setups also bind `<alias-dialog>` from the [Index Dialog](index2.md) so you can browse aliases explicitly.

## How do I configure this?

- Start with [Alias Config](ref-cfg-alias).
- Common options include [`$alias_file`](cfg-alias-file), [`$alias_format`](cfg-alias-format), and [`$alias_sort`](cfg-alias-sort).
- Alias data is maintained with [`:alias`](cmd-alias), [`:unalias`](cmd-unalias), [`:group`](cmd-group), [`:ungroup`](cmd-ungroup), [`:alternates`](cmd-alternates), and [`:unalternates`](cmd-unalternates).
- Colours come from [Colour Objects](ref-colors), especially `indicator`, `status`, `prompt`, `message`, and `normal`.
