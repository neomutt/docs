---
title: Sidebar Panel
description: The optional mailbox sidebar shown beside the index or pager for quick folder navigation.
keywords: sidebar, mailbox list, panel, navigation, unread counts, pinned mailboxes
---

(tour-sidebar)=
# Sidebar Panel

## Introduction -- Where am I?

The Sidebar Panel is NeoMutt's always-available mailbox list.
Unlike the other tour pages, this is not a standalone dialog with its own event loop; it is an embedded panel that sits beside the [Index Dialog](index2.md) or [Pager Dialog](pager.md).
Its job is to keep your folder tree visible so you can change mailboxes quickly.

<div class="term-window">
<div class="term-title">Sidebar Panel</div>
<pre class="terminal">
<span class="sidebar_background">Inbox              </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">Work               </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">  Projects         </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">    NeoMutt        </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">    Vim            </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">  Lists            </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">    NeoMutt        </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">    Kernel         </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">Personal           </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">  Family           </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">  Friends          </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">  Travel           </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">Spam               </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">Drafts             </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">                   </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">                   </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">                   </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">                   </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">                   </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">                   </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">                   </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">                   </span><span class="sidebar_background sidebar_divider"> </span>
<span class="sidebar_background">                   </span><span class="sidebar_background sidebar_divider"> </span>
<span>                    </span>
</pre>
</div>

## What am I looking at?

- The main content is a vertical tree of mailboxes, optionally indented to reflect folder hierarchy.
- The highlight shows the mailbox currently selected inside the sidebar.
- Separate colour objects can distinguish the open mailbox, mailboxes with unread mail, flagged mailboxes, and the spool mailbox.
- The divider visually separates the sidebar from the index or pager beside it.

## What can I do?

- Move the sidebar highlight up and down through the mailbox list.
- Jump straight to the next or previous mailbox with new mail.
- Open the highlighted mailbox in the [Index Dialog](index2.md).
- Search the sidebar mailbox list and toggle between regular and virtual mailboxes.
- Hide or show the panel without changing the rest of the screen layout.
- Full reference: [Sidebar Functions](fn-sidebar).

## Where can I go next?

- `<sidebar-open>` loads the highlighted mailbox in the [Index Dialog](index2.md), and the [Pager Dialog](pager.md) follows that mailbox if it is visible.
- `<sidebar-toggle-visible>` simply removes or restores the panel while leaving you in the current dialog.
- Sidebar search returns you to the same screen once the mailbox has been chosen or the search is cancelled.

## Where did I come from?

- The sidebar appears as part of the [Index Dialog](index2.md) or [Pager Dialog](pager.md) whenever it is enabled.
- It is populated from your configured mailbox list rather than being opened directly like the [Browser Dialog](browser.md).

## How do I configure this?

- Start with [Sidebar Config](ref-cfg-sidebar) and the main [Commands Reference](ref-commands).
- Common options include [`$sidebar_visible`](cfg-sidebar-visible), [`$sidebar_width`](cfg-sidebar-width), [`$sidebar_format`](cfg-sidebar-format), [`$sidebar_sort`](cfg-sidebar-sort), [`$sidebar_folder_indent`](cfg-sidebar-folder-indent), [`$sidebar_indent_string`](cfg-sidebar-indent-string), [`$sidebar_new_mail_only`](cfg-sidebar-new-mail-only), and [`$sidebar_on_right`](cfg-sidebar-on-right).
- Mailboxes shown in the panel are usually defined with [`:mailboxes`](cmd-mailboxes), [`:named-mailboxes`](cmd-named-mailboxes), [`:sidebar-pin`](cmd-sidebar-pin), and [`:sidebar-unpin`](cmd-sidebar-unpin).
- Colours come from [Colour Objects](ref-colors), especially `sidebar_background`, `sidebar_divider`, `sidebar_indicator`, `sidebar_highlight`, `sidebar_new`, `sidebar_unread`, `sidebar_flagged`, `sidebar_ordinary`, and `sidebar_spool_file`.
