---
title: Query Dialog
description: XXX
keywords: XXX
---

(tour-query)=
# Query Dialog

The Query Dialog shows results from an external address book lookup, letting you select recipients for your message.

<div class="term-window">
<div class="term-title">Query Dialog</div>
<pre class="terminal">
<span >  1   Alan Jay Lerner           &lt;ajl@guava.com&gt;           |                        grammy,oscar,tony</span>
<span>  2   Alan Menken               &lt;am@mango.com&gt;            |                        grammy,oscar,tony</span>
<span>  3   Alex Lacamoire            &lt;al@tangerine.com&gt;        |                         emmy,grammy,tony</span>
<span>  4   Al Pacino                 &lt;ap@mango.com&gt;            |                          emmy,oscar,tony</span>
<span>  5   Andre De Shields          &lt;ads@cherry.com&gt;          |                         emmy,grammy,tony</span>
<span>  6   Andrew Lloyd Webber       &lt;alw@elderberry.com&gt;      |                   emmy,grammy,oscar,tony</span>
<span>  7   Anne Bancroft             &lt;ab@elderberry.com&gt;       |                          emmy,oscar,tony</span>
<span>  8   Anne Garefino             &lt;ag@ziziphus.com&gt;         |                         emmy,grammy,tony</span>
<span>  9   Audra McDonald            &lt;amd@fig.com&gt;             |                         emmy,grammy,tony</span>
<span> 10   Audrey Hepburn            &lt;ah@lemon.com&gt;            |                   emmy,grammy,oscar,tony</span>
<span> 11   Benj Pasek                &lt;bp@apple.com&gt;            |                        grammy,oscar,tony</span>
<span> 12   Bette Midler              &lt;bm@vanilla.com&gt;          |                         emmy,grammy,tony</span>
<span> 13   Bob Fosse                 &lt;bf@guava.com&gt;            |                          emmy,oscar,tony</span>
<span> 14   Christopher Plummer       &lt;cp@vanilla.com&gt;          |                          emmy,oscar,tony</span>
<span> 15   Cy Coleman                &lt;cc@damson.com&gt;           |                         emmy,grammy,tony</span>
<span> 16   Cyndi Lauper              &lt;cl@tangerine.com&gt;        |                         emmy,grammy,tony</span>
<span> 17   Cynthia Erivo             &lt;ce@lemon.com&gt;            |                         emmy,grammy,tony</span>
<span> 18   Cynthia Nixon             &lt;cn@nectarine.com&gt;        |                         emmy,grammy,tony</span>
<span> 19   Ellen Burstyn             &lt;eb@nectarine.com&gt;        |                          emmy,oscar,tony</span>
<span> 20   Elton John                &lt;ej@kumquat.com&gt;          |                        grammy,oscar,tony</span>
<span> 21   Frances McDormand         &lt;fmd@hawthorn.com&gt;        |                          emmy,oscar,tony</span>
<span> 22   Frank Loesser             &lt;fl@strawberry.com&gt;       |                        grammy,oscar,tony</span>
<span class="status">Query: tony                                                                                         </span>
<span class="prompt">To: </span><span>tony                                                                                            </span>
</pre>
</div>

Unlike the Alias Dialog which uses NeoMutt's local alias file, the Query Dialog calls an external command (configured via `$query_command`) to search an address book — such as an LDAP directory, a contacts database, or a custom script.
The results are displayed with each contact's name, email address, and any extra information returned by the query command.
You can select one or more entries to add to the message's recipient fields, making it easy to find and address people who aren't in your local alias list.

## See Also

- [Alias Config](ref-cfg-alias)
- [Query Functions](ref-fn-query)
  - mail, sort, limit, ...
- [Generic Functions](ref-fn-generic)
  - **Menu:** page up/down, search, tagging, ...
  - **Global:** enter command, show log message, ...

## And...

- alias dialog
- tutorial: address book
- tutorial: sending mail
- tutorial: tagging
- tutorial: searching

