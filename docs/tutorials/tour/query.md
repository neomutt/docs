---
title: Query Dialog
description: The external address-book results view used to search for recipients outside your local aliases.
keywords: query, address book, ldap, contacts, recipient lookup, create alias
---

(tour-query)=
# Query Dialog

## Introduction -- Where am I?

The Query Dialog shows matches from an external address-book query.
Unlike the [Alias Dialog](alias.md), which reads NeoMutt's local aliases, this dialog is filled by an external command such as an LDAP lookup, contacts script, or directory search.
Its job is to help you find recipients who are not already stored in your alias list.

<div class="term-window">
<div class="term-title">Query Dialog</div>
<pre class="terminal">
<span>  1   Alan Jay Lerner           &lt;ajl@guava.com&gt;           |                        grammy,oscar,tony</span>
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

## What am I looking at?

- Each result row shows the display name, email address, and any extra text returned by the query backend.
- The highlighted row is the address that will be inserted, mailed to, or turned into an alias.
- The status line records the current query string.
- The prompt line shows the live recipient or search text that produced these results.

## What can I do?

- Select one or more addresses to insert into the current recipient field.
- Run a new query or append more results to the current list.
- Sort, limit, and tag results to narrow large address-book searches.
- Create a local alias from a selected query result.
- Compose a new message directly to the selected address.
- Full reference: [Query Functions](menu-query), [Generic Functions](menu-generic).

## Where can I go next?

- Selecting entries usually returns you to the [Compose Dialog](compose.md) or the [Message Window](message.md) prompt that asked for recipients.
- `<mail>` opens the [Compose Dialog](compose.md) directly.
- Creating an alias affects what you will later see in the [Alias Dialog](alias.md).
- `q` cancels and returns to the caller.

## Where did I come from?

- `<query>` from the [Index Dialog](index2.md) opens this dialog explicitly.
- Address completion from the [Message Window](message.md) can open it when you use query completion.
- Editing recipient fields in the [Compose Dialog](compose.md) is a common path into this dialog.

## How do I configure this?

- Start with [Alias Config](ref-cfg-alias).
- Common options include [`$query_command`](cfg-query-command), [`$query_format`](cfg-query-format), and, for local aliases alongside query results, [`$alias_file`](cfg-alias-file) and [`$alias_format`](cfg-alias-format).
- Query results often become persistent local data via [`:alias`](cmd-alias), [`:group`](cmd-group), and related alias commands.
- Colours come from [Colour Objects](ref-colors), especially `indicator`, `status`, `prompt`, `message`, and `normal`.
