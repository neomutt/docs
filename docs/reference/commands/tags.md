---
title: Tags (Notmuch)
description: Commands for defining display formats and visual transformations for Notmuch tags in the index view.
keywords: tag-formats, tag-transforms, notmuch, tags, index_format, expandos, tag display, tag icons, labeling, virtual mailbox
---

# Tags (Notmuch)

Commands for defining tag display formats and transformations.

(cmd-tag-formats)=
## `tag-formats`

Define expando format strings for Notmuch tags, making them available as
variables for use in `$index_format`.

- `tag-formats <tag> <format-string> [...]` — assign a format letter to a tag

```neomuttrc
tag-formats "inbox"      "GI"
tag-formats "signed"     "GS"
tag-formats "important"  "GP"
```

(cmd-tag-transforms)=
## `tag-transforms`

Transform tags into short strings or icons for display.

- `tag-transforms <tag> <display-string> [...]`

```neomuttrc
tag-transforms "inbox"      "I"
tag-transforms "unread"     "N"
tag-transforms "replied"    "R"
tag-transforms "signed"     "S"
tag-transforms "important"  "!"
```

