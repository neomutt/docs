---
title: Alias Dialog
description: XXX
keywords: XXX
---

(tour-alias)=
# Alias Dialog

The Address Book Dialog lets you browse, select, and manage your saved email aliases.

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

When you need to address an email, NeoMutt can look up recipients from your personal address book.
The Alias Dialog displays all the aliases defined in your `alias_file`, showing each alias's short name, the real name, the email address, and any tags.
You can search, sort, and filter the list to quickly find contacts, then select one or more to insert into the To, Cc, or Bcc fields of your message.

New aliases can be added from this dialog and will be saved to `$alias_file`.
Aliases can also be deleted, though deletions only take effect in memory for the current session.

## See Also

- [Alias Config](ref-cfg-alias)
- [Alias Functions](ref-fn-alias)
  - mail, sort, limit, ...
- [Generic Functions](ref-fn-generic)
  - **Menu:** page up/down, search, tagging, ...
  - **Global:** enter command, show log message, ...

## And...

- query dialog
- tutorial: address book
- tutorial: sending mail
- tutorial: tagging
- tutorial: searching

