---
title: Viewing HTML Email and Opening Links
description: Set up mailcap to render HTML email as text and use urlview or urlscan to open links from messages
keywords: neomutt, html, mailcap, urlview, urlscan, links, browser, auto-view, copiousoutput, w3m, lynx, text/html, tutorial
diataxis_type: tutorial
---

# Viewing HTML Email and Opening Links

This tutorial gets HTML email rendering and link opening working in NeoMutt.
You'll set up a mailcap file to convert HTML to readable text, enable auto-view, and configure a URL picker so you can open links from messages.

## Prerequisites

1. NeoMutt installed and configured with at least one account.
2. A text-mode browser installed — `w3m`, `lynx`, or `elinks`.
3. A URL picker installed — `urlview` or `urlscan`.

On Fedora/RHEL:

```sh
sudo dnf install w3m urlview
```

On Debian/Ubuntu:

```sh
sudo apt install w3m urlview
```

On macOS:

```sh
brew install w3m urlview
```

## Part 1: Rendering HTML Email

### Create a Mailcap File

Mailcap tells NeoMutt how to display non-text MIME types.
NeoMutt searches several locations for a mailcap file.
The most common is `~/.mailcap`.

1. Create `~/.mailcap` with an entry for `text/html`:

```
text/html; w3m -dump -T text/html %s; copiousoutput
```

`copiousoutput` tells NeoMutt that the command produces text suitable for piping into the pager.

### Alternative Renderers

Pick the one you prefer:

```
text/html; lynx -dump %s; copiousoutput
```

```
text/html; elinks -dump %s; copiousoutput
```

### Enable Auto-View in NeoMutt

1. Add these lines to your `neomuttrc`:

```neomuttrc
auto-view text/html
alternative_order text/plain text/html
```

`auto-view` tells NeoMutt to render HTML parts automatically.
`alternative_order` tells NeoMutt to prefer plain text when a message includes both formats.

2. Open a message that contains HTML.

Expected result: the HTML content appears as readable text in the pager, converted by your chosen browser.

### Verify the Mailcap Path

If rendering doesn't work, check which mailcap file NeoMutt is using:

```sh
neomutt -nF /dev/null -Q mailcap_path
```

Expected result: the output includes the path to your mailcap file.

## Part 2: Opening Links from Messages

### Set Up urlview

urlview extracts URLs from a message and presents them in a selectable list.

1. Create `~/.urlview` (urlview's config file) to set your browser:

```
COMMAND $BROWSER
```

This uses whatever is set in your `$BROWSER` environment variable.
You can also hard-code a browser:

```
COMMAND xdg-open
```

2. Add a macro to NeoMutt to pipe the current message to urlview:

```neomuttrc
macro index,pager \cb "<pipe-message>urlview<Enter>" "Extract and open URLs"
```

3. Open a message with links and press {kbd}`Ctrl-B`.

Expected result: a list of URLs appears.
Select one and press {kbd}`Enter` to open it in your browser.

### Alternative: Use urlscan

urlscan is a more modern alternative to urlview with colour support.

```sh
pip install urlscan
```

Replace the macro command:

```neomuttrc
macro index,pager \cb "<pipe-message>urlscan<Enter>" "Extract and open URLs"
```

### Set the BROWSER Variable

If links don't open, make sure `$BROWSER` is set in your shell profile:

```sh
export BROWSER="xdg-open"     # Linux
export BROWSER="open"         # macOS
```

## Putting It All Together

Here is a minimal config block that covers both HTML rendering and URL extraction:

```neomuttrc
# HTML rendering
auto-view text/html
alternative_order text/plain text/html

# URL extraction
macro index,pager \cb "<pipe-message>urlview<Enter>" "Extract and open URLs"
```

And the corresponding `~/.mailcap`:

```
text/html; w3m -dump -T text/html %s; copiousoutput
```

## Next Steps

- "I want to know more about MIME handling." See [MIME](../howto/mime) and [Render HTML Email with Mailcap](../howto/mailcap-html).
- "I want to read mail offline." See [Setting Up Offline Email with mbsync](mbsync-setup).
- "I want to customise the pager display." See [Header Display](../howto/header-display) and [Colours](../howto/colours).
