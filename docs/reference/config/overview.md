---
title: Config Options
description: Complete alphabetical index of all NeoMutt configuration options
keywords: neomutt, configuration, options, settings, reference
---

# Config Options

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

```{toctree}
---
maxdepth: 1
hidden:
---
types
address
alias
attach
lib-autocrypt
browser
compose
conn
email
general
gui
hcache
lib-help
lib-history
hooks
imap
index
maildir
lib-mbox
menu
mh
ncrypt
nntp
notmuch
lib-pager
pattern
pop
progress
send
sidebar
```

## A

| Config Option                                                     | Description                                                                 |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [`$abort_backspace`](abort-backspace)                             | Hitting backspace against an empty prompt aborts the prompt                 |
| [`$abort_key`](abort-key)                                         | String representation of key to abort prompts                               |
| [`$abort_noattach`](abort-noattach)                               | Abort sending the email if attachments are missing                          |
| [`$abort_noattach_regex`](abort-noattach-regex)                   | Regex to match text indicating attachments are expected                     |
| `$abort_noattach_regexp`                                          | **Renamed to**: [`$abort_noattach_regex`](abort-noattach-regex)             |
| [`$abort_nosubject`](abort-nosubject)                             | Abort creating the email if subject is missing                              |
| [`$abort_unmodified`](abort-unmodified)                           | Abort the sending if the message hasn't been edited                         |
| [`$account_command`](account-command)                             | Shell command to retrieve account credentials                               |
| [`$alias_file`](alias-file)                                       | Save new aliases to this file                                               |
| [`$alias_format`](alias-format)                                   | printf-like format string for the alias menu                                |
| [`$alias_sort`](alias-sort)                                       | Sort method for the alias menu                                              |
| [`$allow_8bit`](allow-8bit)                                       | Allow 8-bit messages, don't use quoted-printable or base64                  |
| [`$allow_ansi`](allow-ansi)                                       | Allow ANSI color codes in rich text messages                                |
| [`$arrow_cursor`](arrow-cursor)                                   | Use an arrow `->` instead of highlighting in the index                      |
| [`$arrow_string`](arrow-string)                                   | Use a custom string for `arrow_cursor`                                      |
| [`$ascii_chars`](ascii-chars)                                     | Use plain ASCII characters, when drawing email threads                      |
| `$askbcc`                                                         | **Renamed to**: [`$ask_bcc`](ask-bcc)                                       |
| `$askcc`                                                          | **Renamed to**: [`$ask_cc`](ask-cc)                                         |
| [`$ask_bcc`](ask-bcc)                                             | Ask the user for the blind-carbon-copy recipients                           |
| [`$ask_cc`](ask-cc)                                               | Ask the user for the carbon-copy recipients                                 |
| [`$ask_followup_to`](ask-followup-to)                             | Ask the user for follow-up groups before editing                            |
| `$ask_follow_up`                                                  | **Renamed to**: [`$ask_followup_to`](ask-followup-to)                       |
| [`$ask_x_comment_to`](ask-x-comment-to)                           | Ask the user for the `X-Comment-To` field before editing                    |
| [`$assumed_charset`](assumed-charset)                             | If a message is missing a character set, assume this character set          |
| [`$attach_charset`](attach-charset)                               | When attaching files, use one of these character sets                       |
| [`$attach_format`](attach-format)                                 | printf-like format string for the attachment menu                           |
| `$attach_keyword`                                                 | **Renamed to**: [`$abort_noattach_regex`](abort-noattach-regex)             |
| [`$attach_save_dir`](attach-save-dir)                             | Default directory where attachments are saved                               |
| [`$attach_save_without_prompting`](attach-save-without-prompting) | If true, then don't prompt to save                                          |
| [`$attach_sep`](attach-sep)                                       | Separator to add between saved/printed/piped attachments                    |
| [`$attach_split`](attach-split)                                   | Save/print/pipe tagged messages individually                                |
| `$attribution`                                                    | **Renamed to**: [`$attribution_intro`](attribution-intro)                   |
| [`$attribution_intro`](attribution-intro)                         | Message to start a reply, "On DATE, PERSON wrote:"                          |
| [`$attribution_locale`](attribution-locale)                       | Locale for dates in the `$attribution` message                              |
| [`$attribution_trailer`](attribution-trailer)                     | Suffix message to add after reply text                                      |
| [`$autocrypt`](#autocrypt)                                         | Enables the Autocrypt feature                                               |
| [`$autocrypt_acct_format`](autocrypt-acct-format)                 | Format of the Autocrypt account menu                                        |
| [`$autocrypt_dir`](autocrypt-dir)                                 | Location of Autocrypt files, including the GPG keyring and SQLite database  |
| [`$autocrypt_reply`](autocrypt-reply)                             | Replying to an Autocrypt email automatically enables Autocrypt in the reply |
| `$autoedit`                                                       | **Renamed to**: [`$auto_edit`](auto-edit)                                   |
| [`$auto_edit`](auto-edit)                                         | Skip the initial compose menu and edit the email                            |
| [`$auto_subscribe`](auto-subscribe)                               | Automatically check if the user is subscribed to a mailing list             |
| [`$auto_tag`](auto-tag)                                           | Automatically apply actions to all tagged messages                          |

## B

| Config Option                                                   | Description                                           |
|-----------------------------------------------------------------|-------------------------------------------------------|
| [`$beep`](beep)                                                 | Make a noise when an error occurs                     |
| [`$beep_new`](beep-new)                                         | Make a noise when new mail arrives                    |
| [`$bounce`](bounce)                                             | Confirm before bouncing a message                     |
| [`$bounce_delivered`](bounce-delivered)                         | Add `Delivered-To` to bounced messages                |
| [`$braille_friendly`](braille-friendly)                         | Move the cursor to the beginning of the line          |
| [`$browser_abbreviate_mailboxes`](browser-abbreviate-mailboxes) | Abbreviate mailboxes using `~` and `=` in the browser |
| [`$browser_sort`](browser-sort)                                 | Sort method for the browser                           |
| [`$browser_sort_dirs_first`](browser-sort-dirs-first)           | Group directories before files in the browser         |

## C

| Config Option                                                                         | Description                                                                           |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [`$catchup_newsgroup`](catchup-newsgroup)                                             | Mark all articles as read when leaving a newsgroup                                    |
| [`$certificate_file`](certificate-file)                                               | File containing trusted certificates                                                  |
| [`$change_folder_next`](change-folder-next)                                           | Suggest the next folder, rather than the first when using `<change-folder>`           |
| [`$charset`](charset)                                                                 | Default character set for displaying text on screen                                   |
| [`$check_mbox_size`](check-mbox-size)                                                 | Use mailbox size as an indicator of new mail                                          |
| [`$check_new`](check-new)                                                             | Check for new mail while the mailbox is open                                          |
| [`$collapse_all`](collapse-all)                                                       | Collapse all threads when entering a folder                                           |
| [`$collapse_flagged`](collapse-flagged)                                               | Prevent the collapse of threads with flagged emails                                   |
| [`$collapse_unread`](collapse-unread)                                                 | Prevent the collapse of threads with unread emails                                    |
| [`$color_directcolor`](color-directcolor)                                             | Use 24bit colors (aka truecolor aka directcolor)                                      |
| [`$compose_confirm_detach_first`](compose-confirm-detach-first)                       | Prevent the accidental deletion of the composed message                               |
| [`$compose_format`](compose-format)                                                   | printf-like format string for the Compose panel's status bar                          |
| [`$compose_preview_above_attachments`](compose-preview-above-attachments)             | Show the message preview above the attachments list. By default it is shown below it. |
| [`$compose_preview_min_rows`](compose-preview-min-rows)                               | Hide the preview if it has fewer than this number of rows                             |
| [`$compose_show_preview`](compose-show-preview)                                       | Display a preview of the message body in the Compose window                           |
| [`$compose_show_user_headers`](compose-show-user-headers)                             | Controls whether or not custom headers are shown in the compose envelope              |
| [`$config_charset`](config-charset)                                                   | Character set that the config files are in                                            |
| `$confirmappend`                                                                      | **Renamed to**: [`$confirm_append`](confirm-append)                                   |
| `$confirmcreate`                                                                      | **Renamed to**: [`$confirm_create`](confirm-create)                                   |
| [`$confirm_append`](confirm-append)                                                   | Confirm before appending emails to a mailbox                                          |
| [`$confirm_create`](confirm-create)                                                   | Confirm before creating a new mailbox                                                 |
| [`$confirm_empty_to`](confirm-empty-to)                                               | Ask for a confirmation before sending an email with an empty To recipients list       |
| `$connect_timeout`                                                                    | **Renamed to**: [`$socket_timeout`](socket-timeout)                                   |
| [`$content_type`](content-type)                                                       | Default `Content-Type` for newly composed messages                                    |
| [`$copy`](copy)                                                                       | Save outgoing emails to [`$record`](record)                                           |
| [`$copy_decode_weed`](copy-decode-weed)                                               | Controls whether to weed headers when copying or saving emails                        |
| [`$count_alternatives`](count-alternatives)                                           | Recurse inside multipart/alternatives while counting attachments                      |
| `$crypt_autoencrypt`                                                                  | **Renamed to**: [`$crypt_auto_encrypt`](crypt-auto-encrypt)                           |
| `$crypt_autopgp`                                                                      | **Renamed to**: [`$crypt_auto_pgp`](crypt-auto-pgp)                                   |
| `$crypt_autosign`                                                                     | **Renamed to**: [`$crypt_auto_sign`](crypt-auto-sign)                                 |
| `$crypt_autosmime`                                                                    | **Renamed to**: [`$crypt_auto_smime`](crypt-auto-smime)                               |
| [`$crypt_auto_encrypt`](crypt-auto-encrypt)                                           | Automatically PGP encrypt all outgoing mail                                           |
| [`$crypt_auto_pgp`](crypt-auto-pgp)                                                   | Allow automatic PGP functions                                                         |
| [`$crypt_auto_sign`](crypt-auto-sign)                                                 | Automatically PGP sign all outgoing mail                                              |
| [`$crypt_auto_smime`](crypt-auto-smime)                                               | Allow automatic SMIME functions                                                       |
| [`$crypt_chars`](crypt-chars)                                                         | User-configurable crypto flags: signed, encrypted etc.                                |
| `$crypt_confirmhook`                                                                  | **Renamed to**: [`$crypt_confirm_hook`](crypt-confirm-hook)                           |
| [`$crypt_confirm_hook`](crypt-confirm-hook)                                           | Prompt the user to confirm keys before use                                            |
| [`$crypt_encryption_info`](crypt-encryption-info)                                     | Add an informative block with details about the encryption                            |
| [`$crypt_opportunistic_encrypt`](crypt-opportunistic-encrypt)                         | Enable encryption when the recipient's key is available                               |
| [`$crypt_opportunistic_encrypt_strong_keys`](crypt-opportunistic-encrypt-strong-keys) | Enable encryption only when strong a key is available                                 |
| [`$crypt_protected_headers_read`](crypt-protected-headers-read)                       | Display protected headers (Memory Hole) in the pager                                  |
| [`$crypt_protected_headers_save`](crypt-protected-headers-save)                       | Save the cleartext Subject with the headers                                           |
| [`$crypt_protected_headers_subject`](crypt-protected-headers-subject)                 | Use this as the subject for encrypted emails                                          |
| [`$crypt_protected_headers_weed`](crypt-protected-headers-weed)                       | Controls whether NeoMutt will weed protected header fields                            |
| [`$crypt_protected_headers_write`](crypt-protected-headers-write)                     | Generate protected header (Memory Hole) for signed and encrypted emails               |
| `$crypt_replyencrypt`                                                                 | **Renamed to**: [`$crypt_reply_encrypt`](crypt-reply-encrypt)                         |
| `$crypt_replysign`                                                                    | **Renamed to**: [`$crypt_reply_sign`](crypt-reply-sign)                               |
| `$crypt_replysignencrypted`                                                           | **Renamed to**: [`$crypt_reply_sign_encrypted`](crypt-reply-sign-encrypted)           |
| [`$crypt_reply_encrypt`](crypt-reply-encrypt)                                         | Encrypt replies to encrypted messages                                                 |
| [`$crypt_reply_sign`](crypt-reply-sign)                                               | Sign replies to signed messages                                                       |
| [`$crypt_reply_sign_encrypted`](crypt-reply-sign-encrypted)                           | Sign replies to encrypted messages                                                    |
| [`$crypt_timestamp`](crypt-timestamp)                                                 | Add a timestamp to PGP or SMIME output to prevent spoofing                            |
| [`$crypt_use_gpgme`](crypt-use-gpgme)                                                 | Use GPGME crypto backend                                                              |
| [`$crypt_use_pka`](crypt-use-pka)                                                     | Use GPGME to use PKA (lookup PGP keys using DNS)                                      |
| [`$crypt_verify_sig`](crypt-verify-sig)                                               | Verify PGP or SMIME signatures                                                        |
| `$cursor_overlay`                                                                     | **Deprecated**                                                                        |

## D

| Config Option                             | Description                                                                    |
|-------------------------------------------|--------------------------------------------------------------------------------|
| [`$date_format`](date-format)             | strftime format string for the `%d` expando                                    |
| [`$debug_file`](debug-file)               | File to save debug logs                                                        |
| [`$debug_level`](debug-level)             | Logging level for debug logs                                                   |
| [`$default_hook`](default-hook)           | Pattern to use for hooks that only have a simple regex                         |
| [`$delete`](delete)                       | Really delete messages, when the mailbox is closed                             |
| [`$delete_untag`](delete-untag)           | Untag messages when they are marked for deletion                               |
| [`$devel_security`](devel-security)       | Devel feature: Security -- https://github.com/neomutt/neomutt/discussions/4251 |
| [`$digest_collapse`](digest-collapse)     | Hide the subparts of a multipart/digest                                        |
| [`$display_filter`](display-filter)       | External command to pre-process an email before display                        |
| [`$dsn_notify`](dsn-notify)               | Request notification for message delivery or delay                             |
| [`$dsn_return`](dsn-return)               | What to send as a notification of message delivery or delay                    |
| [`$duplicate_threads`](duplicate-threads) | Highlight messages with duplicated message IDs                                 |

## E

| Config Option                                         | Description                                                   |
|-------------------------------------------------------|---------------------------------------------------------------|
| [`$editor`](editor)                                   | External command to use as an email editor                    |
| `$edit_hdrs`                                          | **Renamed to**: [`$edit_headers`](edit-headers)               |
| [`$edit_headers`](edit-headers)                       | Let the user edit the email headers whilst editing an email   |
| [`$empty_subject`](empty-subject)                     | Subject to use when replying to an email with none            |
| [`$encode_from`](encode-from)                         | Encode `From ` as "quote-printable" at the beginning of lines |
| [`$entropy_file`](entropy-file)                       | File/device containing random data to initialise SSL          |
| `$envelope_from`                                      | **Renamed to**: [`$use_envelope_from`](use-envelope-from)     |
| [`$envelope_from_address`](envelope-from-address)     | Manually set the sender for outgoing messages                 |
| `$escape`                                             | **Deprecated**                                                |
| [`$external_search_command`](external-search-command) | External search command                                       |

## F

| Config Option                                                 | Description                                                                     |
|---------------------------------------------------------------|---------------------------------------------------------------------------------|
| [`$fast_reply`](fast-reply)                                   | Don't prompt for the recipients and subject when replying/forwarding            |
| [`$fcc_attach`](fcc-attach)                                   | Save sent message with all their attachments                                    |
| [`$fcc_before_send`](fcc-before-send)                         | Save FCCs before sending the message                                            |
| [`$fcc_clear`](fcc-clear)                                     | Save sent messages unencrypted and unsigned                                     |
| [`$flag_chars`](flag-chars)                                   | User-configurable index flags: tagged, new, etc                                 |
| [`$flag_safe`](flag-safe)                                     | Protect flagged messages from deletion                                          |
| [`$folder`](folder)                                           | Base folder for a set of mailboxes                                              |
| [`$folder_format`](folder-format)                             | printf-like format string for the browser's display of folders                  |
| [`$followup_to`](followup-to)                                 | Add the `Mail-Followup-To` header is generated when sending mail                |
| [`$followup_to_poster`](followup-to-poster)                   | Reply to the poster if "poster" is in the `Followup-To` header                  |
| [`$force_name`](force-name)                                   | Save outgoing mail in a folder of their name                                    |
| [`$forward_attachments`](forward-attachments)                 | Forward attachments when forwarding a message                                   |
| [`$forward_attribution_intro`](forward-attribution-intro)     | Prefix message for forwarded messages                                           |
| [`$forward_attribution_trailer`](forward-attribution-trailer) | Suffix message for forwarded messages                                           |
| [`$forward_decode`](forward-decode)                           | Decode the message when forwarding it                                           |
| [`$forward_decrypt`](forward-decrypt)                         | Decrypt the message when forwarding it                                          |
| [`$forward_edit`](forward-edit)                               | Automatically start the editor when forwarding a message                        |
| [`$forward_format`](forward-format)                           | printf-like format string to control the subject when forwarding a message      |
| [`$forward_quote`](forward-quote)                             | Automatically quote a forwarded message using [`$indent_string`](indent-string) |
| [`$forward_references`](forward-references)                   | Set the `In-Reply-To` and `References` headers when forwarding a message        |
| `$forw_decode`                                                | **Renamed to**: [`$forward_decode`](forward-decode)                             |
| `$forw_decrypt`                                               | **Renamed to**: [`$forward_decrypt`](forward-decrypt)                           |
| `$forw_format`                                                | **Renamed to**: [`$forward_format`](forward-format)                             |
| `$forw_quote`                                                 | **Renamed to**: [`$forward_quote`](forward-quote)                               |
| [`$from`](from)                                               | Default `From` address to use, if isn't otherwise set                           |
| [`$from_chars`](from-chars)                                   | User-configurable index flags: to address, cc address, etc                      |

## G

| Config Option                               | Description                                                       |
|---------------------------------------------|-------------------------------------------------------------------|
| [`$gecos_mask`](gecos-mask)                 | Regex for parsing GECOS field of /etc/passwd                      |
| [`$greeting`](greeting)                     | Greeting string added to the top of all messages                  |
| [`$group_index_format`](group-index-format) | printf-like format string for the browser's display of newsgroups |

## H

| Config Option                                                   | Description                                                                |
|-----------------------------------------------------------------|----------------------------------------------------------------------------|
| [`$hdrs`](hdrs)                                                 | Add custom headers to outgoing mail                                        |
| `$hdr_format`                                                   | **Renamed to**: [`$index_format`](index-format)                            |
| [`$header`](header)                                             | Include the message headers in the reply email (Weed applies)              |
| [`$header_cache`](header-cache)                                 | Directory/file for the header cache database                               |
| [`$header_cache_backend`](header-cache-backend)                 | Header cache backend to use                                                |
| `$header_cache_compress`                                        | **Deprecated**                                                             |
| [`$header_cache_compress_level`](header-cache-compress-level)   | Level of compression for method                                            |
| [`$header_cache_compress_method`](header-cache-compress-method) | Enable generic hcache database compression                                 |
| `$header_cache_pagesize`                                        | **Deprecated**                                                             |
| [`$header_color_partial`](header-color-partial)                 | Only color the part of the header matching the regex                       |
| [`$help`](#help)                                                 | Display a help line with common key bindings                               |
| [`$hidden_host`](hidden-host)                                   | Don't use the hostname, just the domain, when generating the message id    |
| [`$hidden_tags`](hidden-tags)                                   | List of tags that shouldn't be displayed on screen (comma-separated)       |
| [`$hide_limited`](hide-limited)                                 | Don't indicate hidden messages, in the thread tree                         |
| [`$hide_missing`](hide-missing)                                 | Don't indicate missing messages, in the thread tree                        |
| [`$hide_thread_subject`](hide-thread-subject)                   | Hide subjects that are similar to that of the parent message               |
| [`$hide_top_limited`](hide-top-limited)                         | Don't indicate hidden top message, in the thread tree                      |
| [`$hide_top_missing`](hide-top-missing)                         | Don't indicate missing top message, in the thread tree                     |
| [`$history`](#history)                                           | Number of history entries to keep in memory per category                   |
| [`$history_file`](history-file)                                 | File to save history in                                                    |
| [`$history_format`](history-format)                             | printf-like format string for the history menu                             |
| [`$history_remove_dups`](history-remove-dups)                   | Remove duplicate entries from the history                                  |
| [`$honor_disposition`](honor-disposition)                       | Don't display MIME parts inline if they have a disposition of "attachment" |
| [`$honor_followup_to`](honor-followup-to)                       | Honour the `Mail-Followup-To` header when group replying                   |
| [`$hostname`](hostname)                                         | Fully-qualified domain name of this machine                                |

## I

| Config Option                                               | Description                                                               |
|-------------------------------------------------------------|---------------------------------------------------------------------------|
| [`$idn_decode`](idn-decode)                                 | Decode international domain names                                         |
| [`$idn_encode`](idn-encode)                                 | Encode international domain names                                         |
| `$ignore_linear_white_space`                                | **Deprecated**                                                            |
| [`$ignore_list_reply_to`](ignore-list-reply-to)             | Ignore the `Reply-To` header when using `<reply>` on a mailing list       |
| [`$imap_authenticators`](imap-authenticators)               | List of allowed IMAP authentication methods (colon-separated)             |
| [`$imap_check_subscribed`](imap-check-subscribed)           | When opening a mailbox, ask the server for a list of subscribed folders   |
| [`$imap_condstore`](imap-condstore)                         | Enable the CONDSTORE extension                                            |
| [`$imap_deflate`](imap-deflate)                             | Compress network traffic                                                  |
| [`$imap_delim_chars`](imap-delim-chars)                     | Characters that denote separators in IMAP folders                         |
| [`$imap_fetch_chunk_size`](imap-fetch-chunk-size)           | Download headers in blocks of this size                                   |
| [`$imap_headers`](imap-headers)                             | Additional email headers to download when getting index                   |
| [`$imap_idle`](imap-idle)                                   | Use the IMAP IDLE extension to check for new mail                         |
| `$imap_keepalive`                                           | **Renamed to**: [`$imap_keep_alive`](imap-keep-alive)                     |
| [`$imap_keep_alive`](imap-keep-alive)                       | Time to wait before polling an open IMAP connection                       |
| [`$imap_list_subscribed`](imap-list-subscribed)             | When browsing a mailbox, only display subscribed folders                  |
| [`$imap_login`](imap-login)                                 | Login name for the IMAP server (defaults to [`$imap_user`](imap-user))    |
| [`$imap_oauth_refresh_command`](imap-oauth-refresh-command) | External command to generate OAUTH refresh token                          |
| [`$imap_pass`](imap-pass)                                   | Password for the IMAP server                                              |
| [`$imap_passive`](imap-passive)                             | Reuse an existing IMAP connection to check for new mail                   |
| [`$imap_peek`](imap-peek)                                   | Don't mark messages as read when fetching them from the server            |
| [`$imap_pipeline_depth`](imap-pipeline-depth)               | Number of IMAP commands that may be queued up                             |
| [`$imap_poll_timeout`](imap-poll-timeout)                   | Maximum time to wait for a server response                                |
| [`$imap_qresync`](imap-qresync)                             | Enable the QRESYNC extension                                              |
| [`$imap_rfc5161`](imap-rfc5161)                             | Use the IMAP ENABLE extension to select capabilities                      |
| [`$imap_send_id`](imap-send-id)                             | Send ID command when logging in                                           |
| `$imap_servernoise`                                         | **Renamed to**: [`$imap_server_noise`](imap-server-noise)                 |
| [`$imap_server_noise`](imap-server-noise)                   | Display server warnings as error messages                                 |
| [`$imap_user`](imap-user)                                   | Username for the IMAP server                                              |
| `$implicit_autoview`                                        | **Renamed to**: [`$implicit_auto_view`](implicit-auto-view)               |
| [`$implicit_auto_view`](implicit-auto-view)                 | Display MIME attachments inline if a `copiousoutput` mailcap entry exists |
| [`$include`](include)                                       | Include a copy of the email that's being replied to                       |
| [`$include_encrypted`](include-encrypted)                   | Whether to include encrypted content when replying                        |
| `$include_onlyfirst`                                        | **Renamed to**: [`$include_only_first`](include-only-first)               |
| [`$include_only_first`](include-only-first)                 | Only include the first attachment when replying                           |
| `$indent_str`                                               | **Renamed to**: [`$indent_string`](indent-string)                         |
| [`$indent_string`](indent-string)                           | String used to indent "reply" text                                        |
| [`$index_format`](index-format)                             | printf-like format string for the index menu (emails)                     |
| [`$inews_command`](inews-command)                           | External command to post news articles                                    |
| [`$ispell`](ispell)                                         | External command to perform spell-checking                                |

## K

| Config Option                   | Description                                                                     |
|---------------------------------|---------------------------------------------------------------------------------|
| [`$keep_flagged`](keep-flagged) | Don't move flagged messages from [`$spool_file`](spool-file) to [`$mbox`](#mbox) |

## L

| Config Option                             | Description                                                                           |
|-------------------------------------------|---------------------------------------------------------------------------------------|
| [`$local_date_header`](local-date-header) | Convert the date in the Date header of sent emails into local timezone, UTC otherwise |

## M

| Config Option                                                 | Description                                                                                                  |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [`$mailbox_folder_format`](mailbox-folder-format)             | printf-like format string for the browser's display of mailbox folders                                       |
| [`$mailcap_path`](mailcap-path)                               | List of mailcap files (colon-separated)                                                                      |
| [`$mailcap_sanitize`](mailcap-sanitize)                       | Restrict the possible characters in mailcap expandos                                                         |
| [`$maildir_check_cur`](maildir-check-cur)                     | Check both `new` and `cur` directories for new mail                                                          |
| [`$maildir_field_delimiter`](maildir-field-delimiter)         | Field delimiter to be used for maildir email files (default is colon, recommended alternative is semi-colon) |
| [`$maildir_header_cache_verify`](maildir-header-cache-verify) | Check for maildir changes when opening mailbox                                                               |
| [`$maildir_trash`](maildir-trash)                             | Use the maildir `trashed` flag, rather than deleting                                                         |
| [`$mail_check`](mail-check)                                   | Number of seconds before NeoMutt checks for new mail                                                         |
| [`$mail_check_recent`](mail-check-recent)                     | Notify the user about new mail since the last time the mailbox was opened                                    |
| [`$mail_check_stats`](mail-check-stats)                       | Periodically check for new mail                                                                              |
| [`$mail_check_stats_interval`](mail-check-stats-interval)     | How often to check for new mail                                                                              |
| [`$markers`](markers)                                         | Display a `+` at the beginning of wrapped lines in the pager                                                 |
| [`$mark_macro_prefix`](mark-macro-prefix)                     | Prefix for macros using `<mark-message>`                                                                     |
| [`$mark_old`](mark-old)                                       | Mark new emails as old when leaving the mailbox                                                              |
| [`$mask`](mask)                                               | Only display files/dirs matching this regex in the browser                                                   |
| [`$mbox`](#mbox)                                               | Folder that receives read emails (see Move)                                                                  |
| [`$mbox_type`](mbox-type)                                     | Default type for creating new mailboxes                                                                      |
| [`$menu_context`](menu-context)                               | Number of lines of overlap when changing pages in the index                                                  |
| [`$menu_move_off`](menu-move-off)                             | Allow the last menu item to move off the bottom of the screen                                                |
| [`$menu_scroll`](menu-scroll)                                 | Scroll the menu/index by one line, rather than a page                                                        |
| `$message_cachedir`                                           | **Renamed to**: [`$message_cache_dir`](message-cache-dir)                                                    |
| [`$message_cache_clean`](message-cache-clean)                 | Clean out obsolete entries from the message cache                                                            |
| [`$message_cache_dir`](message-cache-dir)                     | Directory for the message cache                                                                              |
| [`$message_format`](message-format)                           | printf-like format string for listing attached messages                                                      |
| [`$message_id_format`](message-id-format)                     | printf-like format string for customising the `Message-Id`                                                   |
| [`$meta_key`](meta-key)                                       | Interpret 'ALT-x' as 'ESC-x'                                                                                 |
| `$metoo`                                                      | **Renamed to**: [`$me_too`](me-too)                                                                          |
| [`$me_too`](me-too)                                           | Remove the user's address from the list of recipients                                                        |
| [`$mh_purge`](mh-purge)                                       | Really delete files in MH mailboxes                                                                          |
| [`$mh_seq_flagged`](mh-seq-flagged)                           | MH sequence for flagged message                                                                              |
| [`$mh_seq_replied`](mh-seq-replied)                           | MH sequence to tag replied messages                                                                          |
| [`$mh_seq_unseen`](mh-seq-unseen)                             | MH sequence for unseen messages                                                                              |
| [`$mime_forward`](mime-forward)                               | Forward a message as a `message/RFC822` MIME part                                                            |
| [`$mime_forward_decode`](mime-forward-decode)                 | Decode the forwarded message before attaching it                                                             |
| [`$mime_forward_rest`](mime-forward-rest)                     | Forward all attachments, even if they can't be decoded                                                       |
| `$mime_fwd`                                                   | **Renamed to**: [`$mime_forward`](mime-forward)                                                              |
| `$mime_subject`                                               | **Deprecated**                                                                                               |
| [`$mime_type_query_command`](mime-type-query-command)         | External command to determine the MIME type of an attachment                                                 |
| [`$mime_type_query_first`](mime-type-query-first)             | Run the [`$mime_type_query_command`](mime-type-query-command) before the mime.types lookup                   |
| `$mixmaster`                                                  | **Deprecated**                                                                                               |
| `$mix_entry_format`                                           | **Deprecated**                                                                                               |
| [`$move`](move)                                               | Move emails from [`$spool_file`](spool-file) to [`$mbox`](#mbox) when read                                    |
| `$msg_format`                                                 | **Renamed to**: [`$message_format`](message-format)                                                          |

## N

| Config Option                                                           | Description                                                                 |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [`$narrow_tree`](narrow-tree)                                           | Draw a narrower thread tree in the index                                    |
| [`$net_inc`](net-inc)                                                   | Update the progress bar after this many KB sent/received (0 to disable)     |
| [`$newsgroups_charset`](newsgroups-charset)                             | Character set of newsgroups' descriptions                                   |
| [`$newsrc`](newsrc)                                                     | File containing list of subscribed newsgroups                               |
| [`$news_cache_dir`](news-cache-dir)                                     | Directory for cached news articles                                          |
| [`$news_server`](news-server)                                           | Url of the news server                                                      |
| [`$new_mail_command`](new-mail-command)                                 | External command to run when new mail arrives                               |
| [`$nm_config_file`](nm-config-file)                                     | Configuration file for notmuch. Use `auto` to detect configuration.         |
| [`$nm_config_profile`](nm-config-profile)                               | Configuration profile for notmuch.                                          |
| [`$nm_db_limit`](nm-db-limit)                                           | Default limit for Notmuch queries                                           |
| `$nm_default_uri`                                                       | **Renamed to**: [`$nm_default_url`](nm-default-url)                         |
| [`$nm_default_url`](nm-default-url)                                     | Path to the Notmuch database                                                |
| [`$nm_exclude_tags`](nm-exclude-tags)                                   | Exclude messages with these tags                                            |
| [`$nm_flagged_tag`](nm-flagged-tag)                                     | Tag to use for flagged messages                                             |
| [`$nm_open_timeout`](nm-open-timeout)                                   | Database timeout                                                            |
| [`$nm_query_type`](nm-query-type)                                       | Default query type: `threads` or `messages`                                 |
| [`$nm_query_window_current_position`](nm-query-window-current-position) | Position of current search window                                           |
| [`$nm_query_window_current_search`](nm-query-window-current-search)     | Current search parameters                                                   |
| [`$nm_query_window_duration`](nm-query-window-duration)                 | Time duration of the current search window                                  |
| [`$nm_query_window_enable`](nm-query-window-enable)                     | Enable query windows                                                        |
| [`$nm_query_window_or_terms`](nm-query-window-or-terms)                 | Additional notmuch search terms for messages to be shown regardless of date |
| [`$nm_query_window_timebase`](nm-query-window-timebase)                 | Units for the time duration                                                 |
| [`$nm_record`](nm-record)                                               | If the [`$record`](record) mailbox (sent mail) should be indexed            |
| [`$nm_record_tags`](nm-record-tags)                                     | Tags to apply to the [`$record`](record) mailbox (sent mail)                |
| [`$nm_replied_tag`](nm-replied-tag)                                     | Tag to use for replied messages                                             |
| [`$nm_unread_tag`](nm-unread-tag)                                       | Tag to use for unread messages                                              |
| [`$nntp_authenticators`](nntp-authenticators)                           | Allowed authentication methods                                              |
| [`$nntp_context`](nntp-context)                                         | Maximum number of articles to list (0 for all articles)                     |
| [`$nntp_listgroup`](nntp-listgroup)                                     | Check all articles when opening a newsgroup                                 |
| [`$nntp_load_description`](nntp-load-description)                       | Load descriptions for newsgroups when adding to the list                    |
| [`$nntp_pass`](nntp-pass)                                               | Password for the news server                                                |
| [`$nntp_poll`](nntp-poll)                                               | Interval between checks for new posts                                       |
| [`$nntp_user`](nntp-user)                                               | Username for the news server                                                |

## P

| Config Option                                                         | Description                                                                            |
|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [`$pager`](#pager)                                                     | External command for viewing messages, or empty to use NeoMutt's                       |
| [`$pager_context`](pager-context)                                     | Number of lines of overlap when changing pages in the pager                            |
| [`$pager_format`](pager-format)                                       | printf-like format string for the pager's status bar                                   |
| [`$pager_index_lines`](pager-index-lines)                             | Number of index lines to display above the pager                                       |
| [`$pager_read_delay`](pager-read-delay)                               | Number of seconds to wait before marking a message read                                |
| [`$pager_skip_quoted_context`](pager-skip-quoted-context)             | Lines of context to show when skipping quoted text                                     |
| [`$pager_stop`](pager-stop)                                           | Don't automatically open the next message when at the end of a message                 |
| [`$pattern_format`](pattern-format)                                   | printf-like format string for the pattern completion menu                              |
| `$pgp_autoencrypt`                                                    | **Renamed to**: [`$crypt_auto_encrypt`](crypt-auto-encrypt)                            |
| `$pgp_autoinline`                                                     | **Renamed to**: [`$pgp_auto_inline`](pgp-auto-inline)                                  |
| `$pgp_autosign`                                                       | **Renamed to**: [`$crypt_auto_sign`](crypt-auto-sign)                                  |
| [`$pgp_auto_decode`](pgp-auto-decode)                                 | Automatically decrypt PGP messages                                                     |
| [`$pgp_auto_inline`](pgp-auto-inline)                                 | Use old-style inline PGP messages (not recommended)                                    |
| `$pgp_auto_traditional`                                               | **Renamed to**: [`$pgp_reply_inline`](pgp-reply-inline)                                |
| [`$pgp_check_exit`](pgp-check-exit)                                   | Check the exit code of PGP subprocess                                                  |
| [`$pgp_check_gpg_decrypt_status_fd`](pgp-check-gpg-decrypt-status-fd) | File descriptor used for status info                                                   |
| `$pgp_clearsign_command`                                              | **Renamed to**: [`$pgp_clear_sign_command`](pgp-clear-sign-command)                    |
| [`$pgp_clear_sign_command`](pgp-clear-sign-command)                   | External command to inline-sign a message                                              |
| `$pgp_create_traditional`                                             | **Renamed to**: [`$pgp_auto_inline`](pgp-auto-inline)                                  |
| [`$pgp_decode_command`](pgp-decode-command)                           | External command to decode a PGP attachment                                            |
| [`$pgp_decryption_okay`](pgp-decryption-okay)                         | Text indicating a successful decryption                                                |
| [`$pgp_decrypt_command`](pgp-decrypt-command)                         | External command to decrypt a PGP message                                              |
| [`$pgp_default_key`](pgp-default-key)                                 | Default key to use for PGP operations                                                  |
| [`$pgp_encrypt_only_command`](pgp-encrypt-only-command)               | External command to encrypt, but not sign a message                                    |
| `$pgp_encrypt_self`                                                   | **Deprecated**                                                                         |
| [`$pgp_encrypt_sign_command`](pgp-encrypt-sign-command)               | External command to encrypt and sign a message                                         |
| [`$pgp_entry_format`](pgp-entry-format)                               | printf-like format string for the PGP key selection menu                               |
| [`$pgp_export_command`](pgp-export-command)                           | External command to export a public key from the user's keyring                        |
| `$pgp_getkeys_command`                                                | **Renamed to**: [`$pgp_get_keys_command`](pgp-get-keys-command)                        |
| [`$pgp_get_keys_command`](pgp-get-keys-command)                       | External command to download a key for an email address                                |
| [`$pgp_good_sign`](pgp-good-sign)                                     | Text indicating a good signature                                                       |
| [`$pgp_ignore_subkeys`](pgp-ignore-subkeys)                           | Only use the principal PGP key                                                         |
| [`$pgp_import_command`](pgp-import-command)                           | External command to import a key into the user's keyring                               |
| [`$pgp_key_sort`](pgp-key-sort)                                       | Sort order for PGP keys                                                                |
| [`$pgp_list_pubring_command`](pgp-list-pubring-command)               | External command to list the public keys in a user's keyring                           |
| [`$pgp_list_secring_command`](pgp-list-secring-command)               | External command to list the private keys in a user's keyring                          |
| [`$pgp_long_ids`](pgp-long-ids)                                       | Display long PGP key IDs to the user                                                   |
| [`$pgp_mime_auto`](pgp-mime-auto)                                     | Prompt the user to use MIME if inline PGP fails                                        |
| `$pgp_replyencrypt`                                                   | **Renamed to**: [`$crypt_reply_encrypt`](crypt-reply-encrypt)                          |
| `$pgp_replyinline`                                                    | **Renamed to**: [`$pgp_reply_inline`](pgp-reply-inline)                                |
| `$pgp_replysign`                                                      | **Renamed to**: [`$crypt_reply_sign`](crypt-reply-sign)                                |
| `$pgp_replysignencrypted`                                             | **Renamed to**: [`$crypt_reply_sign_encrypted`](crypt-reply-sign-encrypted)            |
| [`$pgp_reply_inline`](pgp-reply-inline)                               | Reply using old-style inline PGP messages (not recommended)                            |
| [`$pgp_retainable_sigs`](pgp-retainable-sigs)                         | Create nested multipart/signed or encrypted messages                                   |
| [`$pgp_self_encrypt`](pgp-self-encrypt)                               | Encrypted messages will also be encrypted to [`$pgp_default_key`](pgp-default-key) too |
| `$pgp_self_encrypt_as`                                                | **Renamed to**: [`$pgp_default_key`](pgp-default-key)                                  |
| [`$pgp_show_unusable`](pgp-show-unusable)                             | Show non-usable keys in the key selection                                              |
| [`$pgp_sign_as`](pgp-sign-as)                                         | Use this alternative key for signing messages                                          |
| [`$pgp_sign_command`](pgp-sign-command)                               | External command to create a detached PGP signature                                    |
| `$pgp_sort_keys`                                                      | **Renamed to**: [`$pgp_key_sort`](pgp-key-sort)                                        |
| [`$pgp_strict_enc`](pgp-strict-enc)                                   | Encode PGP signed messages with quoted-printable (don't unset)                         |
| [`$pgp_timeout`](pgp-timeout)                                         | Time in seconds to cache a passphrase                                                  |
| [`$pgp_use_gpg_agent`](pgp-use-gpg-agent)                             | Use a PGP agent for caching passwords                                                  |
| [`$pgp_verify_command`](pgp-verify-command)                           | External command to verify PGP signatures                                              |
| [`$pgp_verify_key_command`](pgp-verify-key-command)                   | External command to verify key information                                             |
| `$pgp_verify_sig`                                                     | **Renamed to**: [`$crypt_verify_sig`](crypt-verify-sig)                                |
| [`$pipe_decode`](pipe-decode)                                         | Decode the message when piping it                                                      |
| [`$pipe_decode_weed`](pipe-decode-weed)                               | Control whether to weed headers when piping an email                                   |
| [`$pipe_sep`](pipe-sep)                                               | Separator to add between multiple piped messages                                       |
| [`$pipe_split`](pipe-split)                                           | Run the pipe command on each message separately                                        |
| [`$pop_authenticators`](pop-authenticators)                           | List of allowed authentication methods (colon-separated)                               |
| [`$pop_auth_try_all`](pop-auth-try-all)                               | Try all available authentication methods                                               |
| `$pop_checkinterval`                                                  | **Renamed to**: [`$pop_check_interval`](pop-check-interval)                            |
| [`$pop_check_interval`](pop-check-interval)                           | Interval between checks for new mail                                                   |
| [`$pop_delete`](pop-delete)                                           | After downloading POP messages, delete them on the server                              |
| [`$pop_host`](pop-host)                                               | Url of the POP server                                                                  |
| [`$pop_last`](pop-last)                                               | Use the `LAST` command to fetch new mail                                               |
| [`$pop_oauth_refresh_command`](pop-oauth-refresh-command)             | External command to generate OAUTH refresh token                                       |
| [`$pop_pass`](pop-pass)                                               | Password of the POP server                                                             |
| [`$pop_reconnect`](pop-reconnect)                                     | Reconnect to the server is the connection is lost                                      |
| [`$pop_user`](pop-user)                                               | Username of the POP server                                                             |
| [`$postpone`](postpone)                                               | Save messages to the [`$postponed`](postponed) folder                                  |
| [`$postponed`](postponed)                                             | Folder to store postponed messages                                                     |
| [`$postpone_encrypt`](postpone-encrypt)                               | Self-encrypt postponed messages                                                        |
| [`$postpone_encrypt_as`](postpone-encrypt-as)                         | Fallback encryption key for postponed messages                                         |
| `$post_indent_str`                                                    | **Renamed to**: `$post_indent_string`                                                  |
| `$post_indent_string`                                                 | **Renamed to**: [`$attribution_trailer`](attribution-trailer)                          |
| [`$post_moderated`](post-moderated)                                   | Allow posting to moderated newsgroups                                                  |
| [`$preconnect`](preconnect)                                           | External command to run prior to opening a socket                                      |
| [`$preferred_languages`](preferred-languages)                         | List of Preferred Languages for multilingual MIME (comma-separated)                    |
| [`$print`](print)                                                     | Confirm before printing a message                                                      |
| `$print_cmd`                                                          | **Renamed to**: [`$print_command`](print-command)                                      |
| [`$print_command`](print-command)                                     | External command to print a message                                                    |
| [`$print_decode`](print-decode)                                       | Decode message before printing it                                                      |
| [`$print_decode_weed`](print-decode-weed)                             | Control whether to weed headers when printing an email                                 |
| [`$print_split`](print-split)                                         | Print multiple messages separately                                                     |
| [`$prompt_after`](prompt-after)                                       | Pause after running an external pager                                                  |

## Q

| Config Option                     | Description                                                 |
|-----------------------------------|-------------------------------------------------------------|
| [`$query_command`](query-command) | External command to query and external address book         |
| [`$query_format`](query-format)   | printf-like format string for the query menu (address book) |
| [`$quit`](quit)                   | Prompt before exiting NeoMutt                               |
| [`$quote_regex`](quote-regex)     | Regex to match quoted text in a reply                       |
| `$quote_regexp`                   | **Renamed to**: [`$quote_regex`](quote-regex)               |

## R

| Config Option                                             | Description                                                         |
|-----------------------------------------------------------|---------------------------------------------------------------------|
| [`$read_inc`](read-inc)                                   | Update the progress bar after this many records read (0 to disable) |
| [`$read_only`](read-only)                                 | Open folders in read-only mode                                      |
| `$realname`                                               | **Renamed to**: [`$real_name`](real-name)                           |
| [`$real_name`](real-name)                                 | Real name of the user                                               |
| [`$recall`](recall)                                       | Recall postponed mesaages when asked to compose a message           |
| [`$record`](record)                                       | Folder to save 'sent' messages                                      |
| [`$reflow_space_quotes`](reflow-space-quotes)             | Insert spaces into reply quotes for `format=flowed` messages        |
| [`$reflow_text`](reflow-text)                             | Reformat paragraphs of `format=flowed` text                         |
| [`$reflow_wrap`](reflow-wrap)                             | Maximum paragraph width for reformatting `format=flowed` text       |
| [`$reply_regex`](reply-regex)                             | Regex to match message reply subjects like `re: `                   |
| `$reply_regexp`                                           | **Renamed to**: [`$reply_regex`](reply-regex)                       |
| [`$reply_self`](reply-self)                               | Really reply to yourself, when replying to your own email           |
| [`$reply_to`](reply-to)                                   | Address to use as a `Reply-To` header                               |
| [`$reply_with_xorig`](reply-with-xorig)                   | Create `From` header from `X-Original-To` header                    |
| [`$resolve`](resolve)                                     | Move to the next email whenever a command modifies an email         |
| [`$resume_draft_files`](resume-draft-files)               | Process draft files like postponed messages                         |
| [`$resume_edited_draft_files`](resume-edited-draft-files) | Resume editing previously saved draft files                         |
| [`$reverse_alias`](reverse-alias)                         | Display the alias in the index, rather than the message's sender    |
| [`$reverse_name`](reverse-name)                           | Set the `From` from the address the email was sent to               |
| `$reverse_realname`                                       | **Renamed to**: [`$reverse_real_name`](reverse-real-name)           |
| [`$reverse_real_name`](reverse-real-name)                 | Set the `From` from the full `To` address the email was sent to     |
| [`$rfc2047_parameters`](rfc2047-parameters)               | Decode RFC2047-encoded MIME parameters                              |

## S

| Config Option                                                       | Description                                                                                        |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [`$save_address`](save-address)                                     | Use sender's full address as a default save folder                                                 |
| [`$save_empty`](save-empty)                                         | Preserve empty mailboxes                                                                           |
| [`$save_history`](save-history)                                     | Number of history entries to save per category                                                     |
| [`$save_name`](save-name)                                           | Save outgoing message to mailbox of recipient's name if it exists                                  |
| [`$save_unsubscribed`](save-unsubscribed)                           | Save a list of unsubscribed newsgroups to the `newsrc`                                             |
| [`$score`](score)                                                   | Use message scoring                                                                                |
| [`$score_threshold_delete`](score-threshold-delete)                 | Messages with a lower score will be automatically deleted                                          |
| [`$score_threshold_flag`](score-threshold-flag)                     | Messages with a greater score will be automatically flagged                                        |
| [`$score_threshold_read`](score-threshold-read)                     | Messages with a lower score will be automatically marked read                                      |
| [`$search_context`](search-context)                                 | Context to display around search matches                                                           |
| [`$sendmail`](sendmail)                                             | External command to send email                                                                     |
| [`$sendmail_wait`](sendmail-wait)                                   | Time to wait for sendmail to finish                                                                |
| [`$send_charset`](send-charset)                                     | Character sets for outgoing mail                                                                   |
| [`$shell`](shell)                                                   | External command to run subshells in                                                               |
| [`$show_multipart_alternative`](show-multipart-alternative)         | How to display `multipart/alternative` MIME parts                                                  |
| [`$show_new_news`](show-new-news)                                   | Check for new newsgroups when entering the browser                                                 |
| [`$show_only_unread`](show-only-unread)                             | Only show subscribed newsgroups with unread articles                                               |
| [`$sidebar_component_depth`](sidebar-component-depth)               | Strip leading path components from sidebar folders                                                 |
| [`$sidebar_delim_chars`](sidebar-delim-chars)                       | Characters that separate nested folders                                                            |
| [`$sidebar_divider_char`](sidebar-divider-char)                     | Character to draw between the sidebar and index                                                    |
| [`$sidebar_folder_indent`](sidebar-folder-indent)                   | Indent nested folders                                                                              |
| [`$sidebar_format`](sidebar-format)                                 | printf-like format string for the sidebar panel                                                    |
| [`$sidebar_indent_string`](sidebar-indent-string)                   | Indent nested folders using this string                                                            |
| [`$sidebar_new_mail_only`](sidebar-new-mail-only)                   | Only show folders with new/flagged mail                                                            |
| [`$sidebar_next_new_wrap`](sidebar-next-new-wrap)                   | Wrap around when searching for the next mailbox with new mail                                      |
| [`$sidebar_non_empty_mailbox_only`](sidebar-non-empty-mailbox-only) | Only show folders with a non-zero number of mail                                                   |
| [`$sidebar_on_right`](sidebar-on-right)                             | Display the sidebar on the right                                                                   |
| [`$sidebar_short_path`](sidebar-short-path)                         | Abbreviate the paths using the [`$folder`](folder) variable                                        |
| [`$sidebar_sort`](sidebar-sort)                                     | Method to sort the sidebar                                                                         |
| `$sidebar_sort_method`                                              | **Renamed to**: [`$sidebar_sort`](sidebar-sort)                                                    |
| [`$sidebar_visible`](sidebar-visible)                               | Show the sidebar                                                                                   |
| [`$sidebar_width`](sidebar-width)                                   | Width of the sidebar                                                                               |
| [`$signature`](signature)                                           | File containing a signature to append to all mail                                                  |
| [`$sig_dashes`](sig-dashes)                                         | Insert `-- ` before the signature                                                                  |
| [`$sig_on_top`](sig-on-top)                                         | Insert the signature before the quoted text                                                        |
| [`$simple_search`](simple-search)                                   | Pattern to search for when search doesn't contain `~`s                                             |
| [`$size_show_bytes`](size-show-bytes)                               | Show smaller sizes in bytes                                                                        |
| [`$size_show_fractions`](size-show-fractions)                       | Show size fractions with a single decimal place                                                    |
| [`$size_show_mb`](size-show-mb)                                     | Show sizes in megabytes for sizes greater than 1 megabyte                                          |
| [`$size_units_on_left`](size-units-on-left)                         | Show the units as a prefix to the size                                                             |
| `$skip_quoted_offset`                                               | **Renamed to**: [`$pager_skip_quoted_context`](pager-skip-quoted-context)                          |
| [`$sleep_time`](sleep-time)                                         | Time to pause after certain info messages                                                          |
| [`$smart_wrap`](smart-wrap)                                         | Wrap text at word boundaries                                                                       |
| [`$smileys`](smileys)                                               | Regex to match smileys to prevent mistakes when quoting text                                       |
| [`$smime_ask_cert_label`](smime-ask-cert-label)                     | Prompt the user for a label for SMIME certificates                                                 |
| [`$smime_ca_location`](smime-ca-location)                           | File containing trusted certificates                                                               |
| [`$smime_certificates`](smime-certificates)                         | File containing user's public certificates                                                         |
| [`$smime_decrypt_command`](smime-decrypt-command)                   | External command to decrypt an SMIME message                                                       |
| [`$smime_decrypt_use_default_key`](smime-decrypt-use-default-key)   | Use the default key for decryption                                                                 |
| [`$smime_default_key`](smime-default-key)                           | Default key for SMIME operations                                                                   |
| [`$smime_encrypt_command`](smime-encrypt-command)                   | External command to encrypt a message                                                              |
| `$smime_encrypt_self`                                               | **Deprecated**                                                                                     |
| [`$smime_encrypt_with`](smime-encrypt-with)                         | Algorithm for encryption                                                                           |
| [`$smime_get_cert_command`](smime-get-cert-command)                 | External command to extract a certificate from a message                                           |
| [`$smime_get_cert_email_command`](smime-get-cert-email-command)     | External command to get a certificate for an email                                                 |
| [`$smime_get_signer_cert_command`](smime-get-signer-cert-command)   | External command to extract a certificate from an email                                            |
| [`$smime_import_cert_command`](smime-import-cert-command)           | External command to import a certificate                                                           |
| [`$smime_is_default`](smime-is-default)                             | Use SMIME rather than PGP by default                                                               |
| [`$smime_keys`](smime-keys)                                         | File containing user's private certificates                                                        |
| [`$smime_pk7out_command`](smime-pk7out-command)                     | External command to extract a public certificate                                                   |
| [`$smime_self_encrypt`](smime-self-encrypt)                         | Encrypted messages will also be encrypt to [`$smime_default_key`](smime-default-key) too           |
| `$smime_self_encrypt_as`                                            | **Renamed to**: [`$smime_default_key`](smime-default-key)                                          |
| [`$smime_sign_as`](smime-sign-as)                                   | Use this alternative key for signing messages                                                      |
| [`$smime_sign_command`](smime-sign-command)                         | External command to sign a message                                                                 |
| [`$smime_sign_digest_alg`](smime-sign-digest-alg)                   | Digest algorithm                                                                                   |
| [`$smime_timeout`](smime-timeout)                                   | Time in seconds to cache a passphrase                                                              |
| [`$smime_verify_command`](smime-verify-command)                     | External command to verify a signed message                                                        |
| [`$smime_verify_opaque_command`](smime-verify-opaque-command)       | External command to verify a signature                                                             |
| [`$smtp_authenticators`](smtp-authenticators)                       | List of allowed authentication methods (colon-separated)                                           |
| [`$smtp_oauth_refresh_command`](smtp-oauth-refresh-command)         | External command to generate OAUTH refresh token                                                   |
| [`$smtp_pass`](smtp-pass)                                           | Password for the SMTP server                                                                       |
| [`$smtp_url`](smtp-url)                                             | Url of the SMTP server                                                                             |
| [`$smtp_user`](smtp-user)                                           | Username for the SMTP server                                                                       |
| [`$socket_timeout`](socket-timeout)                                 | Timeout for socket connect/read/write operations (-1 to wait indefinitely)                         |
| [`$sort`](sort)                                                     | Sort method for the index                                                                          |
| `$sort_alias`                                                       | **Renamed to**: [`$alias_sort`](alias-sort)                                                        |
| [`$sort_aux`](sort-aux)                                             | Secondary sort method for the index                                                                |
| `$sort_browser`                                                     | **Renamed to**: [`$browser_sort`](browser-sort)                                                    |
| [`$sort_re`](sort-re)                                               | Whether [`$reply_regex`](reply-regex) must be matched when not [`$strict_threads`](strict-threads) |
| [`$spam_separator`](spam-separator)                                 | Separator for multiple spam headers                                                                |
| `$spoolfile`                                                        | **Renamed to**: [`$spool_file`](spool-file)                                                        |
| [`$spool_file`](spool-file)                                         | Inbox                                                                                              |
| [`$ssl_ca_certificates_file`](ssl-ca-certificates-file)             | File containing trusted CA certificates                                                            |
| [`$ssl_ciphers`](ssl-ciphers)                                       | Ciphers to use when using SSL                                                                      |
| [`$ssl_client_cert`](ssl-client-cert)                               | File containing client certificates                                                                |
| [`$ssl_force_tls`](ssl-force-tls)                                   | Require TLS encryption for all connections                                                         |
| [`$ssl_min_dh_prime_bits`](ssl-min-dh-prime-bits)                   | Minimum keysize for Diffie-Hellman key exchange                                                    |
| [`$ssl_starttls`](ssl-starttls)                                     | Use STARTTLS on servers advertising the capability                                                 |
| `$ssl_usesystemcerts`                                               | **Renamed to**: [`$ssl_use_system_certs`](ssl-use-system-certs)                                    |
| `$ssl_use_sslv2`                                                    | **Deprecated**                                                                                     |
| `$ssl_use_sslv3`                                                    | **Deprecated**                                                                                     |
| [`$ssl_use_system_certs`](ssl-use-system-certs)                     | Use CA certificates in the system-wide store                                                       |
| `$ssl_use_tlsv1`                                                    | **Deprecated**                                                                                     |
| `$ssl_use_tlsv1_1`                                                  | **Deprecated**                                                                                     |
| [`$ssl_use_tlsv1_2`](ssl-use-tlsv1-2)                               | Use TLSv1.2 for authentication                                                                     |
| [`$ssl_use_tlsv1_3`](ssl-use-tlsv1-3)                               | Use TLSv1.3 for authentication                                                                     |
| [`$ssl_verify_dates`](ssl-verify-dates)                             | Verify the dates on the server certificate                                                         |
| [`$ssl_verify_host`](ssl-verify-host)                               | Verify the server's hostname against the certificate                                               |
| [`$ssl_verify_partial_chains`](ssl-verify-partial-chains)           | Allow verification using partial certificate chains                                                |
| [`$status_chars`](status-chars)                                     | Indicator characters for the status bar                                                            |
| [`$status_format`](status-format)                                   | printf-like format string for the index's status line                                              |
| [`$status_on_top`](status-on-top)                                   | Display the status bar at the top                                                                  |
| [`$strict_threads`](strict-threads)                                 | Thread messages using `In-Reply-To` and `References` headers                                       |
| [`$suspend`](suspend)                                               | Allow the user to suspend NeoMutt using `^Z`                                                       |

## T

| Config Option                                             | Description                                                        |
|-----------------------------------------------------------|--------------------------------------------------------------------|
| [`$text_flowed`](text-flowed)                             | Generate `format=flowed` messages                                  |
| [`$thorough_search`](thorough-search)                     | Decode headers and messages before searching them                  |
| [`$thread_received`](thread-received)                     | Sort threaded messages by their received date                      |
| [`$tilde`](tilde)                                         | Display `~` in the pager after the end of the email                |
| [`$timeout`](timeout)                                     | Time to wait for user input in menus                               |
| [`$time_inc`](time-inc)                                   | Frequency of progress bar updates (milliseconds)                   |
| `$tmpdir`                                                 | **Renamed to**: [`$tmp_dir`](tmp-dir)                              |
| [`$tmp_dir`](tmp-dir)                                     | Directory for temporary files                                      |
| [`$toggle_quoted_show_levels`](toggle-quoted-show-levels) | Number of quote levels to show with toggle-quoted                  |
| [`$to_chars`](to-chars)                                   | Indicator characters for the `To` field in the index               |
| [`$trash`](trash)                                         | Folder to put deleted emails                                       |
| [`$ts_enabled`](ts-enabled)                               | Allow NeoMutt to set the terminal status line and icon             |
| [`$ts_icon_format`](ts-icon-format)                       | printf-like format string for the terminal's icon title            |
| [`$ts_status_format`](ts-status-format)                   | printf-like format string for the terminal's status (window title) |
| [`$tunnel`](tunnel)                                       | Shell command to establish a tunnel                                |
| [`$tunnel_is_secure`](tunnel-is-secure)                   | Assume a tunneled connection is secure                             |

## U

| Config Option                             | Description                                            |
|-------------------------------------------|--------------------------------------------------------|
| [`$uncollapse_jump`](uncollapse-jump)     | When opening a thread, jump to the next unread message |
| [`$uncollapse_new`](uncollapse-new)       | Open collapsed threads when new mail arrives           |
| [`$user_agent`](user-agent)               | Add a `User-Agent` header to outgoing mail             |
| `$use_8bitmime`                           | **Renamed to**: [`$use_8bit_mime`](use-8bit-mime)      |
| [`$use_8bit_mime`](use-8bit-mime)         | Use 8-bit messages and ESMTP to send messages          |
| [`$use_domain`](use-domain)               | Qualify local addresses using this domain              |
| [`$use_envelope_from`](use-envelope-from) | Set the envelope sender of the message                 |
| [`$use_from`](use-from)                   | Set the `From` header for outgoing mail                |
| [`$use_ipv6`](use-ipv6)                   | Lookup IPv6 addresses when making connections          |
| [`$use_threads`](use-threads)             | Whether to use threads for the index                   |

## V

| Config Option                               | Description                                                 |
|---------------------------------------------|-------------------------------------------------------------|
| `$vfolder_format`                           | **Deprecated**                                              |
| `$virtual_spoolfile`                        | **Renamed to**: [`$virtual_spool_file`](virtual-spool-file) |
| [`$virtual_spool_file`](virtual-spool-file) | Use the first virtual mailbox as a spool file               |
| `$visual`                                   | **Deprecated**                                              |

## W

| Config Option                   | Description                                                            |
|---------------------------------|------------------------------------------------------------------------|
| [`$wait_key`](wait-key)         | Prompt to press a key after running external commands                  |
| [`$weed`](weed)                 | Filter headers when displaying/forwarding/printing/replying            |
| [`$wrap`](wrap)                 | Width to wrap text in the pager                                        |
| [`$wrap_headers`](wrap-headers) | Width to wrap headers in outgoing messages                             |
| [`$wrap_search`](wrap-search)   | Wrap around when the search hits the end                               |
| [`$write_bcc`](write-bcc)       | Write out the `Bcc` field when preparing to send a mail                |
| [`$write_inc`](write-inc)       | Update the progress bar after this many records written (0 to disable) |

## X

| Config Option                   | Description                                             |
|---------------------------------|---------------------------------------------------------|
| `$xterm_icon`                   | **Renamed to**: [`$ts_icon_format`](ts-icon-format)     |
| `$xterm_set_titles`             | **Renamed to**: [`$ts_enabled`](ts-enabled)             |
| `$xterm_title`                  | **Renamed to**: [`$ts_status_format`](ts-status-format) |
| [`$x_comment_to`](x-comment-to) | Add `X-Comment-To` header that contains article author  |

