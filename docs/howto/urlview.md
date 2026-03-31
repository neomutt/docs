---
title: Open URLs from Emails
description: Extract and open URLs from messages using urlview or urlscan with a NeoMutt macro
keywords: urlview, urlscan, url, links, browser, pipe-message, macro, xdg-open, extract urls, open links
---

# Open URLs from Emails

## Prerequisites

1. NeoMutt installed and working.
2. A URL picker installed — `urlview` or `urlscan`.
3. A web browser accessible from the command line.

On Fedora/RHEL:

```sh
sudo dnf install urlview     # or: pip install urlscan
```

On Debian/Ubuntu:

```sh
sudo apt install urlview     # or: pip install urlscan
```

On macOS:

```sh
brew install urlview         # or: pip install urlscan
```

## Set Up urlview

1. Create `~/.urlview` with your browser command:

```
COMMAND xdg-open
```

On macOS, use:

```
COMMAND open
```

Or use the `$BROWSER` environment variable:

```
COMMAND $BROWSER
```

2. Add a macro to NeoMutt:

```neomuttrc
macro index,pager \cb "<pipe-message>urlview<Enter>" "Extract and open URLs"
```

3. Open a message containing links and press `Ctrl-b`.

Expected result: urlview displays a numbered list of URLs found in the message. Select one and press `Enter` to open it in your browser.

## Set Up urlscan (Alternative)

urlscan is a more modern alternative with colour support and context display.

1. Install urlscan:

```sh
pip install urlscan
```

2. Add the NeoMutt macro:

```neomuttrc
macro index,pager \cb "<pipe-message>urlscan<Enter>" "Extract and open URLs"
```

3. Press `Ctrl-b` on a message with links.

Expected result: urlscan shows URLs with surrounding context and lets you select one to open.

## Configure the Browser

If links don't open, set `$BROWSER` in your shell profile:

```sh
# Linux
export BROWSER="xdg-open"

# macOS
export BROWSER="open"

# Specific browser
export BROWSER="firefox"
```

You can also set it inside NeoMutt:

```neomuttrc
setenv BROWSER xdg-open
```

Expected result: selected URLs open in the configured browser.

## Pipe Only the Message Body

By default, `<pipe-message>` sends the full message including headers.
To send only the decoded body:

```neomuttrc
set pipe_decode = yes
```

Expected result: urlview/urlscan receives clean body text without header noise.

## Copy a URL Instead of Opening It

urlscan can copy a URL to the clipboard instead of opening it.

```neomuttrc
macro index,pager \cb "<pipe-message>urlscan --pipe 'xclip -selection clipboard'<Enter>" "Copy URL to clipboard"
```

Expected result: selecting a URL copies it to the system clipboard.

See [Integrate External Tools](external-tools) for more on connecting NeoMutt to external programs.
