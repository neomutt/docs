---
title: Edit and Navigate Threads
description: Link broken threads, break off-topic subthreads, and configure flat, threaded, or reverse threading views in NeoMutt
keywords: threads, link-threads, break-thread, use_threads, sort, sort_aux, threading, conversation view, tree display, flat view, reverse threads, last-date, sort-mailbox, status_format, %T
---

# Edit and Navigate Threads

## Editing Threads

NeoMutt has the ability to dynamically restructure threads that are broken either by misconfigured software or bad behavior from some correspondents.
This allows you to clean your mailboxes from these annoyances which make it hard to follow a discussion.

### Linking Threads

Some mailers tend to "forget" to correctly set the "In-Reply-To:" and "References:" headers when replying to a message.
This results in broken discussions because NeoMutt has not enough information to guess the correct threading.

1. Tag a number of replies that belong to the same thread.
2. Move to the parent message.
3. Use the `<link-threads>` function (bound to `&` by default).

The replies will then be connected to this parent message.

### Breaking Threads

On mailing lists, some people are in the bad habit of starting a new discussion by hitting "reply" to any message from the list and changing the subject to a totally unrelated one.

1. Navigate to the message where the off-topic subthread begins.
2. Use the `<break-thread>` function (bound to `#` by default).

This will turn the subthread starting from the current message into a whole different thread.

:::{admonition} 📷 Screenshot Needed
:class: tip

**Subject:** Linked and broken threads in the index

**Description:** NeoMutt index view showing a thread that has been repaired with `<link-threads>` — several replies are now correctly nested under a parent message with tree-drawing characters (`|->`, `` `-> ``) connecting them.

**Highlights:** The tree structure showing parent-child relationships between messages, with the thread connector characters visible in the index.
:::

## Use Threads Feature

**Since:** NeoMutt 2021-08-01

### Introduction

The "Use Threads" feature adds a new config option to allow more precise control of how threads are displayed in the index.
Whether threads are in use is now orthogonal from how messages are sorted.

### Functions

The "Use Threads" feature adds no new functions to NeoMutt.
The existing functions `<sort-mailbox>` and `<sort-reverse>` are updated to toggle the state of `$use_threads` once it has been set, while preserving backwards-compatible behavior on `$sort` if this feature is not used.

### Variables

The "Use Threads" feature adds one new config option, {ref}`$use_threads <use-threads>`, which is an enumeration of possible thread views.
The variable defaults to unset for the original behavior of overloading {ref}`$sort=threads <sort>` to enable sorting.
It can be set to `flat` (or `no`) for an unthreaded view based on `$sort`, to `threads` (or `yes`) for a threaded view where roots appear above children, or to `reverse` for a threaded view where children appear above roots.

When sorting by threads, the value of {ref}`$sort <sort>` determines which thread floats to the top.
If `$sort` does not contain `reverse-`, the latest thread goes to the bottom for `use_threads=threads` and to the top for `use_threads=reverse`; the direction of float is swapped if `$sort` also uses `reverse-`.
If `$sort` includes `last-`, the overall thread is sorted by its descendant at any depth which would sort last in a flat view; otherwise, the overall thread is sorted solely by the thread root.
The `last-` prefix is ignored when `use_threads=flat`.

Within a single thread, the value of `$sort_aux` determines how siblings are sorted.
The same prefixes apply as for `$sort`, although it is less common to use the `last-` prefix.

The "Use Threads" feature also modifies the existing config option `$status_format`, adding the `%T` expando which shows the current threading method.

### Use Threads Variable

| Name          | Type | Default |
|---------------|------|---------|
| `use_threads` | enum | `unset` |

### neomuttrc

**Flat View**

<div class="term-window">
<div class="term-title">Flat View</div>
<pre class="terminal">
<span class="index index_date">12:01</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index index_subject">cover letter for thread 1</span><span class="index">                                                         </span>
<span class="index index_date">12:02</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index index_subject">part 1 of thread 1</span><span class="index">                                                                </span>
<span class="index index_date">12:03</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index index_subject">part 2 of thread 1</span><span class="index">                                                                </span>
<span class="index index_date">12:04</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index index_subject">part 3 of thread 1</span><span class="index">                                                                </span>
<span class="index index_date">12:05</span><span class="index">  </span><span class="index index_author">Barbara  </span><span class="index">  </span><span class="index index_subject">thread 2</span><span class="index">                                                                          </span>
<span class="index index_date">12:06</span><span class="index">  </span><span class="index index_author">Claire   </span><span class="index">  </span><span class="index index_subject">thread 3</span><span class="index">                                                                          </span>
<span class="index index_date">12:07</span><span class="index">  </span><span class="index index_author">Diane    </span><span class="index">  </span><span class="index index_subject">re: part 2 of thread 1</span><span class="index">                                                            </span>
<span class="index index_date">12:08</span><span class="index">  </span><span class="index index_author">Erica    </span><span class="index">  </span><span class="index index_subject">re: thread 2</span><span class="index">                                                                      </span>
</pre>
</div>

```neomuttrc
# Default configuration: flat view sorted by date
# selecting threads with <sort-mailbox> changes $sort
# set use_threads=unset sort=date sort_aux=date
# Modern configuration: explicit flat view sorted by date
# selecting threads with <sort-mailbox> changes $use_threads
set use_threads=no sort=date sort_aux=date
```

---

**Threaded View**

<div class="term-window">
<div class="term-title">Threaded View</div>
<pre class="terminal">
<span class="index index_date">12:01</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index index_subject">cover letter for thread 1</span><span class="index">                                                         </span>
<span class="index index_date">12:02</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index tree">├─&gt;</span><span class="index index_subject">part 1 of thread 1</span><span class="index">                                                             </span>
<span class="index index_date">12:03</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index tree">├─&gt;</span><span class="index index_subject">part 2 of thread 1</span><span class="index">                                                             </span>
<span class="index index_date">12:07</span><span class="index">  </span><span class="index index_author">Diane    </span><span class="index">  </span><span class="index tree">│ └─&gt;</span><span class="index">                                                                             </span>
<span class="index index_date">12:04</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index tree">└─&gt;</span><span class="index index_subject">part 3 of thread 1</span><span class="index">                                                             </span>
<span class="index index_date">12:05</span><span class="index">  </span><span class="index index_author">Barbara  </span><span class="index">  </span><span class="index index_subject">thread 2</span><span class="index">                                                                          </span>
<span class="index index_date">12:08</span><span class="index">  </span><span class="index index_author">Erica    </span><span class="index">  </span><span class="index tree">└─&gt;</span><span class="index">                                                                               </span>
<span class="index index_date">12:06</span><span class="index">  </span><span class="index index_author">Claire   </span><span class="index">  </span><span class="index index_subject">thread 3</span><span class="index">                                                                          </span>
</pre>
</div>

```neomuttrc
# Legacy configuration: sorting threads by date started
# set sort=threads sort_aux=date
# Modern configuration for the same
# Latest root message sorts last
set use_threads=yes sort=date sort_aux=date
```

---

**Reverse Threaded View**

<div class="term-window">
<div class="term-title">Reverse Threaded View</div>
<pre class="terminal">
<span class="index index_date">12:06</span><span class="index">  </span><span class="index index_author">Claire   </span><span class="index">  </span><span class="index index_subject">thread 3</span><span class="index">                                                                          </span>
<span class="index index_date">12:08</span><span class="index">  </span><span class="index index_author">Erica    </span><span class="index">  </span><span class="index tree">┌─&gt;</span><span class="index">                                                                               </span>
<span class="index index_date">12:05</span><span class="index">  </span><span class="index index_author">Barbara  </span><span class="index">  </span><span class="index index_subject">thread 2</span><span class="index">                                                                          </span>
<span class="index index_date">12:04</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index tree">┌─&gt;</span><span class="index index_subject">part 3 of thread 1</span><span class="index">                                                             </span>
<span class="index index_date">12:07</span><span class="index">  </span><span class="index index_author">Diane    </span><span class="index">  </span><span class="index tree">│ ┌─&gt;</span><span class="index">                                                                             </span>
<span class="index index_date">12:03</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index tree">├─&gt;</span><span class="index index_subject">part 2 of thread 1</span><span class="index">                                                             </span>
<span class="index index_date">12:02</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index tree">├─&gt;</span><span class="index index_subject">part 1 of thread 1</span><span class="index">                                                             </span>
<span class="index index_date">12:01</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index index_subject">cover letter for thread 1</span><span class="index">                                                         </span>
</pre>
</div>

```neomuttrc
# Legacy configuration: display threads upside-down
# set sort=reverse-threads sort_aux=date
# Modern configuration for the same
# Latest root message sorts first
set use_threads=reverse sort=date sort_aux=date
```

---

**Recently Active First**

<div class="term-window">
<div class="term-title">Recently Active First</div>
<pre class="terminal">
<span class="index index_date">12:05</span><span class="index">  </span><span class="index index_author">Barbara  </span><span class="index">  </span><span class="index index_subject">thread 2</span><span class="index">                                                                          </span>
<span class="index index_date">12:08</span><span class="index">  </span><span class="index index_author">Erica    </span><span class="index">  </span><span class="index tree">└─&gt;</span><span class="index">                                                                               </span>
<span class="index index_date">12:01</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index index_subject">cover letter for thread 1</span><span class="index">                                                         </span>
<span class="index index_date">12:03</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index tree">├─&gt;</span><span class="index index_subject">part 2 of thread 1</span><span class="index">                                                             </span>
<span class="index index_date">12:07</span><span class="index">  </span><span class="index index_author">Diane    </span><span class="index">  </span><span class="index tree">│ └─&gt;</span><span class="index">                                                                             </span>
<span class="index index_date">12:04</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index tree">├─&gt;</span><span class="index index_subject">part 3 of thread 1</span><span class="index">                                                             </span>
<span class="index index_date">12:02</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index tree">└─&gt;</span><span class="index index_subject">part 1 of thread 1</span><span class="index">                                                             </span>
<span class="index index_date">12:06</span><span class="index">  </span><span class="index index_author">Claire   </span><span class="index">  </span><span class="index index_subject">thread 3</span><span class="index">                                                                          </span>
</pre>
</div>

```neomuttrc
# Legacy configuration: recently active thread/subthread first
# set sort=threads sort_aux=reverse-last-date
# Modern configuration for the same
# Note that subthreads are also rearranged
set use_threads=threads sort=reverse-last-date sort_aux=reverse-last-date
```

---

**Recently Active Last**

<div class="term-window">
<div class="term-title">Recently Active Last</div>
<pre class="terminal">
<span class="index index_date">12:06</span><span class="index">  </span><span class="index index_author">Claire   </span><span class="index">  </span><span class="index index_subject">thread 3</span><span class="index">                                                                          </span>
<span class="index index_date">12:01</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index index_subject">cover letter for thread 1</span><span class="index">                                                         </span>
<span class="index index_date">12:02</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index tree">├─&gt;</span><span class="index index_subject">part 1 of thread 1</span><span class="index">                                                             </span>
<span class="index index_date">12:03</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index tree">├─&gt;</span><span class="index index_subject">part 2 of thread 1</span><span class="index">                                                             </span>
<span class="index index_date">12:07</span><span class="index">  </span><span class="index index_author">Diane    </span><span class="index">  </span><span class="index tree">│ └─&gt;</span><span class="index">                                                                             </span>
<span class="index index_date">12:04</span><span class="index">  </span><span class="index index_author">Anne     </span><span class="index">  </span><span class="index tree">└─&gt;</span><span class="index index_subject">part 3 of thread 1</span><span class="index">                                                             </span>
<span class="index index_date">12:05</span><span class="index">  </span><span class="index index_author">Barbara  </span><span class="index">  </span><span class="index index_subject">thread 2</span><span class="index">                                                                          </span>
<span class="index index_date">12:08</span><span class="index">  </span><span class="index index_author">Erica    </span><span class="index">  </span><span class="index tree">└─&gt;</span><span class="index">                                                                               </span>
</pre>
</div>

```neomuttrc
# Modern configuration: threads keep date order, recently active thread last
# (not possible with legacy configuration)
set use_threads=threads sort=last-date sort_aux=date
```

### Known Bugs

Even though `use_threads` accepts the values `yes` and `no`, it does not behave like a boolean or quad-option variable.
A bare `set use_threads` performs a query rather than setting it to `yes`, and the variable is not usable with `toggle`.

