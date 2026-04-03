---
title: Config Options
description: Complete alphabetical index of all NeoMutt configuration variables with brief descriptions and cross-references.
keywords: neomutt, configuration, options, settings, reference, alphabetical index, variable list, config overview, all options
---

(ref-config)=
# Config Options

This section is a reference list of NeoMutt configuration options: what they are called, what they do.

If you're new to configuration, you may find it helpful to first read about:

```{toctree}
---
maxdepth: 1
---
files
syntax
types
```

These pages explain how these settings work and how to apply them.

## A

| Config Option                                                         | Description                                                                         |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [`$abort_backspace`](cfg-abort-backspace)                             | Hitting backspace against an empty prompt aborts the prompt                         |
| [`$abort_key`](cfg-abort-key)                                         | String representation of key to abort prompts                                       |
| [`$abort_noattach`](cfg-abort-noattach)                               | Abort sending the email if attachments are missing                                  |
| [`$abort_noattach_regex`](cfg-abort-noattach-regex)                   | Regex to match text indicating attachments are expected                             |
| `$abort_noattach_regexp`                                              | {bdg-warning-line}`Renamed to:` [`$abort_noattach_regex`](cfg-abort-noattach-regex) |
| [`$abort_nosubject`](cfg-abort-nosubject)                             | Abort creating the email if subject is missing                                      |
| [`$abort_unmodified`](cfg-abort-unmodified)                           | Abort the sending if the message hasn't been edited                                 |
| [`$account_command`](cfg-account-command)                             | Shell command to retrieve account credentials                                       |
| [`$alias_file`](cfg-alias-file)                                       | Save new aliases to this file                                                       |
| [`$alias_format`](cfg-alias-format)                                   | printf-like format string for the alias menu                                        |
| [`$alias_sort`](cfg-alias-sort)                                       | Sort method for the alias menu                                                      |
| [`$allow_8bit`](cfg-allow-8bit)                                       | Allow 8-bit messages, don't use quoted-printable or base64                          |
| [`$allow_ansi`](cfg-allow-ansi)                                       | Allow ANSI color codes in rich text messages                                        |
| [`$arrow_cursor`](cfg-arrow-cursor)                                   | Use an arrow `->` instead of highlighting in the index                              |
| [`$arrow_string`](cfg-arrow-string)                                   | Use a custom string for `arrow_cursor`                                              |
| [`$ascii_chars`](cfg-ascii-chars)                                     | Use plain ASCII characters, when drawing email threads                              |
| `$askbcc`                                                             | {bdg-warning-line}`Renamed to:` [`$ask_bcc`](cfg-ask-bcc)                           |
| `$askcc`                                                              | {bdg-warning-line}`Renamed to:` [`$ask_cc`](cfg-ask-cc)                             |
| [`$ask_bcc`](cfg-ask-bcc)                                             | Ask the user for the blind-carbon-copy recipients                                   |
| [`$ask_cc`](cfg-ask-cc)                                               | Ask the user for the carbon-copy recipients                                         |
| [`$ask_followup_to`](cfg-ask-followup-to)                             | Ask the user for follow-up groups before editing                                    |
| `$ask_follow_up`                                                      | {bdg-warning-line}`Renamed to:` [`$ask_followup_to`](cfg-ask-followup-to)           |
| [`$ask_x_comment_to`](cfg-ask-x-comment-to)                           | Ask the user for the `X-Comment-To` field before editing                            |
| [`$assumed_charset`](cfg-assumed-charset)                             | If a message is missing a character set, assume this character set                  |
| [`$attach_charset`](cfg-attach-charset)                               | When attaching files, use one of these character sets                               |
| [`$attach_format`](cfg-attach-format)                                 | printf-like format string for the attachment menu                                   |
| `$attach_keyword`                                                     | {bdg-warning-line}`Renamed to:` [`$abort_noattach_regex`](cfg-abort-noattach-regex) |
| [`$attach_save_dir`](cfg-attach-save-dir)                             | Default directory where attachments are saved                                       |
| [`$attach_save_without_prompting`](cfg-attach-save-without-prompting) | If true, then don't prompt to save                                                  |
| [`$attach_sep`](cfg-attach-sep)                                       | Separator to add between saved/printed/piped attachments                            |
| [`$attach_split`](cfg-attach-split)                                   | Save/print/pipe tagged messages individually                                        |
| `$attribution`                                                        | {bdg-warning-line}`Renamed to:` [`$attribution_intro`](cfg-attribution-intro)       |
| [`$attribution_intro`](cfg-attribution-intro)                         | Message to start a reply, "On DATE, PERSON wrote:"                                  |
| [`$attribution_locale`](cfg-attribution-locale)                       | Locale for dates in the `$attribution` message                                      |
| [`$attribution_trailer`](cfg-attribution-trailer)                     | Suffix message to add after reply text                                              |
| [`$autocrypt`](cfg-autocrypt)                                         | Enables the Autocrypt feature                                                       |
| [`$autocrypt_acct_format`](cfg-autocrypt-acct-format)                 | Format of the Autocrypt account menu                                                |
| [`$autocrypt_dir`](cfg-autocrypt-dir)                                 | Location of Autocrypt files, including the GPG keyring and SQLite database          |
| [`$autocrypt_reply`](cfg-autocrypt-reply)                             | Replying to an Autocrypt email automatically enables Autocrypt in the reply         |
| `$autoedit`                                                           | {bdg-warning-line}`Renamed to:` [`$auto_edit`](cfg-auto-edit)                       |
| [`$auto_edit`](cfg-auto-edit)                                         | Skip the initial compose menu and edit the email                                    |
| [`$auto_subscribe`](cfg-auto-subscribe)                               | Automatically check if the user is subscribed to a mailing list                     |
| [`$auto_tag`](cfg-auto-tag)                                           | Automatically apply actions to all tagged messages                                  |

## B

| Config Option                                                       | Description                                           |
|---------------------------------------------------------------------|-------------------------------------------------------|
| [`$beep`](cfg-beep)                                                 | Make a noise when an error occurs                     |
| [`$beep_new`](cfg-beep-new)                                         | Make a noise when new mail arrives                    |
| [`$bounce`](cfg-bounce)                                             | Confirm before bouncing a message                     |
| [`$bounce_delivered`](cfg-bounce-delivered)                         | Add `Delivered-To` to bounced messages                |
| [`$braille_friendly`](cfg-braille-friendly)                         | Move the cursor to the beginning of the line          |
| [`$browser_abbreviate_mailboxes`](cfg-browser-abbreviate-mailboxes) | Abbreviate mailboxes using `~` and `=` in the browser |
| [`$browser_sort`](cfg-browser-sort)                                 | Sort method for the browser                           |
| [`$browser_sort_dirs_first`](cfg-browser-sort-dirs-first)           | Group directories before files in the browser         |

## C

| Config Option                                                                             | Description                                                                                     |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [`$catchup_newsgroup`](cfg-catchup-newsgroup)                                             | Mark all articles as read when leaving a newsgroup                                              |
| [`$certificate_file`](cfg-certificate-file)                                               | File containing trusted certificates                                                            |
| [`$change_folder_next`](cfg-change-folder-next)                                           | Suggest the next folder, rather than the first when using `<change-folder>`                     |
| [`$charset`](cfg-charset)                                                                 | Default character set for displaying text on screen                                             |
| [`$check_mbox_size`](cfg-check-mbox-size)                                                 | Use mailbox size as an indicator of new mail                                                    |
| [`$check_new`](cfg-check-new)                                                             | Check for new mail while the mailbox is open                                                    |
| [`$collapse_all`](cfg-collapse-all)                                                       | Collapse all threads when entering a folder                                                     |
| [`$collapse_flagged`](cfg-collapse-flagged)                                               | Prevent the collapse of threads with flagged emails                                             |
| [`$collapse_unread`](cfg-collapse-unread)                                                 | Prevent the collapse of threads with unread emails                                              |
| [`$color_directcolor`](cfg-color-directcolor)                                             | Use 24bit colors (aka truecolor aka directcolor)                                                |
| [`$compose_confirm_detach_first`](cfg-compose-confirm-detach-first)                       | Prevent the accidental deletion of the composed message                                         |
| [`$compose_format`](cfg-compose-format)                                                   | printf-like format string for the Compose panel's status bar                                    |
| [`$compose_preview_above_attachments`](cfg-compose-preview-above-attachments)             | Show the message preview above the attachments list. By default it is shown below it.           |
| [`$compose_preview_min_rows`](cfg-compose-preview-min-rows)                               | Hide the preview if it has fewer than this number of rows                                       |
| [`$compose_show_preview`](cfg-compose-show-preview)                                       | Display a preview of the message body in the Compose window                                     |
| [`$compose_show_user_headers`](cfg-compose-show-user-headers)                             | Controls whether or not custom headers are shown in the compose envelope                        |
| [`$config_charset`](cfg-config-charset)                                                   | Character set that the config files are in                                                      |
| `$confirmappend`                                                                          | {bdg-warning-line}`Renamed to:` [`$confirm_append`](cfg-confirm-append)                         |
| `$confirmcreate`                                                                          | {bdg-warning-line}`Renamed to:` [`$confirm_create`](cfg-confirm-create)                         |
| [`$confirm_append`](cfg-confirm-append)                                                   | Confirm before appending emails to a mailbox                                                    |
| [`$confirm_create`](cfg-confirm-create)                                                   | Confirm before creating a new mailbox                                                           |
| [`$confirm_empty_to`](cfg-confirm-empty-to)                                               | Ask for a confirmation before sending an email with an empty To recipients list                 |
| `$connect_timeout`                                                                        | {bdg-warning-line}`Renamed to:` [`$socket_timeout`](cfg-socket-timeout)                         |
| [`$content_type`](cfg-content-type)                                                       | Default `Content-Type` for newly composed messages                                              |
| [`$copy`](cfg-copy)                                                                       | Save outgoing emails to [`$record`](cfg-record)                                                 |
| [`$copy_decode_weed`](cfg-copy-decode-weed)                                               | Controls whether to weed headers when copying or saving emails                                  |
| [`$count_alternatives`](cfg-count-alternatives)                                           | Recurse inside multipart/alternatives while counting attachments                                |
| `$crypt_autoencrypt`                                                                      | {bdg-warning-line}`Renamed to:` [`$crypt_auto_encrypt`](cfg-crypt-auto-encrypt)                 |
| `$crypt_autopgp`                                                                          | {bdg-warning-line}`Renamed to:` [`$crypt_auto_pgp`](cfg-crypt-auto-pgp)                         |
| `$crypt_autosign`                                                                         | {bdg-warning-line}`Renamed to:` [`$crypt_auto_sign`](cfg-crypt-auto-sign)                       |
| `$crypt_autosmime`                                                                        | {bdg-warning-line}`Renamed to:` [`$crypt_auto_smime`](cfg-crypt-auto-smime)                     |
| [`$crypt_auto_encrypt`](cfg-crypt-auto-encrypt)                                           | Automatically PGP encrypt all outgoing mail                                                     |
| [`$crypt_auto_pgp`](cfg-crypt-auto-pgp)                                                   | Allow automatic PGP functions                                                                   |
| [`$crypt_auto_sign`](cfg-crypt-auto-sign)                                                 | Automatically PGP sign all outgoing mail                                                        |
| [`$crypt_auto_smime`](cfg-crypt-auto-smime)                                               | Allow automatic SMIME functions                                                                 |
| [`$crypt_chars`](cfg-crypt-chars)                                                         | User-configurable crypto flags: signed, encrypted etc.                                          |
| `$crypt_confirmhook`                                                                      | {bdg-warning-line}`Renamed to:` [`$crypt_confirm_hook`](cfg-crypt-confirm-hook)                 |
| [`$crypt_confirm_hook`](cfg-crypt-confirm-hook)                                           | Prompt the user to confirm keys before use                                                      |
| [`$crypt_encryption_info`](cfg-crypt-encryption-info)                                     | Add an informative block with details about the encryption                                      |
| [`$crypt_opportunistic_encrypt`](cfg-crypt-opportunistic-encrypt)                         | Enable encryption when the recipient's key is available                                         |
| [`$crypt_opportunistic_encrypt_strong_keys`](cfg-crypt-opportunistic-encrypt-strong-keys) | Enable encryption only when strong a key is available                                           |
| [`$crypt_protected_headers_read`](cfg-crypt-protected-headers-read)                       | Display protected headers (Memory Hole) in the pager                                            |
| [`$crypt_protected_headers_save`](cfg-crypt-protected-headers-save)                       | Save the cleartext Subject with the headers                                                     |
| [`$crypt_protected_headers_subject`](cfg-crypt-protected-headers-subject)                 | Use this as the subject for encrypted emails                                                    |
| [`$crypt_protected_headers_weed`](cfg-crypt-protected-headers-weed)                       | Controls whether NeoMutt will weed protected header fields                                      |
| [`$crypt_protected_headers_write`](cfg-crypt-protected-headers-write)                     | Generate protected header (Memory Hole) for signed and encrypted emails                         |
| `$crypt_replyencrypt`                                                                     | {bdg-warning-line}`Renamed to:` [`$crypt_reply_encrypt`](cfg-crypt-reply-encrypt)               |
| `$crypt_replysign`                                                                        | {bdg-warning-line}`Renamed to:` [`$crypt_reply_sign`](cfg-crypt-reply-sign)                     |
| `$crypt_replysignencrypted`                                                               | {bdg-warning-line}`Renamed to:` [`$crypt_reply_sign_encrypted`](cfg-crypt-reply-sign-encrypted) |
| [`$crypt_reply_encrypt`](cfg-crypt-reply-encrypt)                                         | Encrypt replies to encrypted messages                                                           |
| [`$crypt_reply_sign`](cfg-crypt-reply-sign)                                               | Sign replies to signed messages                                                                 |
| [`$crypt_reply_sign_encrypted`](cfg-crypt-reply-sign-encrypted)                           | Sign replies to encrypted messages                                                              |
| [`$crypt_timestamp`](cfg-crypt-timestamp)                                                 | Add a timestamp to PGP or SMIME output to prevent spoofing                                      |
| [`$crypt_use_gpgme`](cfg-crypt-use-gpgme)                                                 | Use GPGME crypto backend                                                                        |
| [`$crypt_use_pka`](cfg-crypt-use-pka)                                                     | Use GPGME to use PKA (lookup PGP keys using DNS)                                                |
| [`$crypt_verify_sig`](cfg-crypt-verify-sig)                                               | Verify PGP or SMIME signatures                                                                  |
| `$cursor_overlay`                                                                         | {bdg-danger-line}`Deprecated`                                                                   |

## D

| Config Option                                 | Description                                                                    |
|-----------------------------------------------|--------------------------------------------------------------------------------|
| [`$date_format`](cfg-date-format)             | strftime format string for the `%d` expando                                    |
| [`$debug_file`](cfg-debug-file)               | File to save debug logs                                                        |
| [`$debug_level`](cfg-debug-level)             | Logging level for debug logs                                                   |
| [`$default_hook`](cfg-default-hook)           | Pattern to use for hooks that only have a simple regex                         |
| [`$delete`](cfg-delete)                       | Really delete messages, when the mailbox is closed                             |
| [`$delete_untag`](cfg-delete-untag)           | Untag messages when they are marked for deletion                               |
| [`$devel_security`](cfg-devel-security)       | Devel feature: Security -- https://github.com/neomutt/neomutt/discussions/4251 |
| [`$digest_collapse`](cfg-digest-collapse)     | Hide the subparts of a multipart/digest                                        |
| [`$display_filter`](cfg-display-filter)       | External command to pre-process an email before display                        |
| [`$dsn_notify`](cfg-dsn-notify)               | Request notification for message delivery or delay                             |
| [`$dsn_return`](cfg-dsn-return)               | What to send as a notification of message delivery or delay                    |
| [`$duplicate_threads`](cfg-duplicate-threads) | Highlight messages with duplicated message IDs                                 |

## E

| Config Option                                             | Description                                                                   |
|-----------------------------------------------------------|-------------------------------------------------------------------------------|
| [`$editor`](cfg-editor)                                   | External command to use as an email editor                                    |
| `$edit_hdrs`                                              | {bdg-warning-line}`Renamed to:` [`$edit_headers`](cfg-edit-headers)           |
| [`$edit_headers`](cfg-edit-headers)                       | Let the user edit the email headers whilst editing an email                   |
| [`$empty_subject`](cfg-empty-subject)                     | Subject to use when replying to an email with none                            |
| [`$encode_from`](cfg-encode-from)                         | Encode `From ` as "quote-printable" at the beginning of lines                 |
| [`$entropy_file`](cfg-entropy-file)                       | File/device containing random data to initialise SSL                          |
| `$envelope_from`                                          | {bdg-warning-line}`Renamed to:` [`$use_envelope_from`](cfg-use-envelope-from) |
| [`$envelope_from_address`](cfg-envelope-from-address)     | Manually set the sender for outgoing messages                                 |
| `$escape`                                                 | {bdg-danger-line}`Deprecated`                                                 |
| [`$external_search_command`](cfg-external-search-command) | External search command                                                       |

## F

| Config Option                                                     | Description                                                                         |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [`$fast_reply`](cfg-fast-reply)                                   | Don't prompt for the recipients and subject when replying/forwarding                |
| [`$fcc_attach`](cfg-fcc-attach)                                   | Save sent message with all their attachments                                        |
| [`$fcc_before_send`](cfg-fcc-before-send)                         | Save FCCs before sending the message                                                |
| [`$fcc_clear`](cfg-fcc-clear)                                     | Save sent messages unencrypted and unsigned                                         |
| [`$flag_chars`](cfg-flag-chars)                                   | User-configurable index flags: tagged, new, etc                                     |
| [`$flag_safe`](cfg-flag-safe)                                     | Protect flagged messages from deletion                                              |
| [`$folder`](cfg-folder)                                           | Base folder for a set of mailboxes                                                  |
| [`$folder_format`](cfg-folder-format)                             | printf-like format string for the browser's display of folders                      |
| [`$followup_to`](cfg-followup-to)                                 | Add the `Mail-Followup-To` header is generated when sending mail                    |
| [`$followup_to_poster`](cfg-followup-to-poster)                   | Reply to the poster if "poster" is in the `Followup-To` header                      |
| [`$force_name`](cfg-force-name)                                   | Save outgoing mail in a folder of their name                                        |
| [`$forward_attachments`](cfg-forward-attachments)                 | Forward attachments when forwarding a message                                       |
| [`$forward_attribution_intro`](cfg-forward-attribution-intro)     | Prefix message for forwarded messages                                               |
| [`$forward_attribution_trailer`](cfg-forward-attribution-trailer) | Suffix message for forwarded messages                                               |
| [`$forward_decode`](cfg-forward-decode)                           | Decode the message when forwarding it                                               |
| [`$forward_decrypt`](cfg-forward-decrypt)                         | Decrypt the message when forwarding it                                              |
| [`$forward_edit`](cfg-forward-edit)                               | Automatically start the editor when forwarding a message                            |
| [`$forward_format`](cfg-forward-format)                           | printf-like format string to control the subject when forwarding a message          |
| [`$forward_quote`](cfg-forward-quote)                             | Automatically quote a forwarded message using [`$indent_string`](cfg-indent-string) |
| [`$forward_references`](cfg-forward-references)                   | Set the `In-Reply-To` and `References` headers when forwarding a message            |
| `$forw_decode`                                                    | {bdg-warning-line}`Renamed to:` [`$forward_decode`](cfg-forward-decode)             |
| `$forw_decrypt`                                                   | {bdg-warning-line}`Renamed to:` [`$forward_decrypt`](cfg-forward-decrypt)           |
| `$forw_format`                                                    | {bdg-warning-line}`Renamed to:` [`$forward_format`](cfg-forward-format)             |
| `$forw_quote`                                                     | {bdg-warning-line}`Renamed to:` [`$forward_quote`](cfg-forward-quote)               |
| [`$from`](cfg-from)                                               | Default `From` address to use, if isn't otherwise set                               |
| [`$from_chars`](cfg-from-chars)                                   | User-configurable index flags: to address, cc address, etc                          |

## G

| Config Option                                   | Description                                                       |
|-------------------------------------------------|-------------------------------------------------------------------|
| [`$gecos_mask`](cfg-gecos-mask)                 | Regex for parsing GECOS field of /etc/passwd                      |
| [`$greeting`](cfg-greeting)                     | Greeting string added to the top of all messages                  |
| [`$group_index_format`](cfg-group-index-format) | printf-like format string for the browser's display of newsgroups |

## H

| Config Option                                                       | Description                                                                |
|---------------------------------------------------------------------|----------------------------------------------------------------------------|
| [`$hdrs`](cfg-hdrs)                                                 | Add custom headers to outgoing mail                                        |
| `$hdr_format`                                                       | {bdg-warning-line}`Renamed to:` [`$index_format`](cfg-index-format)        |
| [`$header`](cfg-header)                                             | Include the message headers in the reply email (Weed applies)              |
| [`$header_cache`](cfg-header-cache)                                 | Directory/file for the header cache database                               |
| [`$header_cache_backend`](cfg-header-cache-backend)                 | Header cache backend to use                                                |
| `$header_cache_compress`                                            | {bdg-danger-line}`Deprecated`                                              |
| [`$header_cache_compress_level`](cfg-header-cache-compress-level)   | Level of compression for method                                            |
| [`$header_cache_compress_method`](cfg-header-cache-compress-method) | Enable generic hcache database compression                                 |
| `$header_cache_pagesize`                                            | {bdg-danger-line}`Deprecated`                                              |
| [`$header_color_partial`](cfg-header-color-partial)                 | Only color the part of the header matching the regex                       |
| [`$help`](cfg-help)                                                 | Display a help line with common key bindings                               |
| [`$hidden_host`](cfg-hidden-host)                                   | Don't use the hostname, just the domain, when generating the message id    |
| [`$hidden_tags`](cfg-hidden-tags)                                   | List of tags that shouldn't be displayed on screen (comma-separated)       |
| [`$hide_limited`](cfg-hide-limited)                                 | Don't indicate hidden messages, in the thread tree                         |
| [`$hide_missing`](cfg-hide-missing)                                 | Don't indicate missing messages, in the thread tree                        |
| [`$hide_thread_subject`](cfg-hide-thread-subject)                   | Hide subjects that are similar to that of the parent message               |
| [`$hide_top_limited`](cfg-hide-top-limited)                         | Don't indicate hidden top message, in the thread tree                      |
| [`$hide_top_missing`](cfg-hide-top-missing)                         | Don't indicate missing top message, in the thread tree                     |
| [`$history`](cfg-history)                                           | Number of history entries to keep in memory per category                   |
| [`$history_file`](cfg-history-file)                                 | File to save history in                                                    |
| [`$history_format`](cfg-history-format)                             | printf-like format string for the history menu                             |
| [`$history_remove_dups`](cfg-history-remove-dups)                   | Remove duplicate entries from the history                                  |
| [`$honor_disposition`](cfg-honor-disposition)                       | Don't display MIME parts inline if they have a disposition of "attachment" |
| [`$honor_followup_to`](cfg-honor-followup-to)                       | Honour the `Mail-Followup-To` header when group replying                   |
| [`$hostname`](cfg-hostname)                                         | Fully-qualified domain name of this machine                                |

## I

| Config Option                                                   | Description                                                                     |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------|
| [`$idn_decode`](cfg-idn-decode)                                 | Decode international domain names                                               |
| [`$idn_encode`](cfg-idn-encode)                                 | Encode international domain names                                               |
| `$ignore_linear_white_space`                                    | {bdg-danger-line}`Deprecated`                                                   |
| [`$ignore_list_reply_to`](cfg-ignore-list-reply-to)             | Ignore the `Reply-To` header when using `<reply>` on a mailing list             |
| [`$imap_authenticators`](cfg-imap-authenticators)               | List of allowed IMAP authentication methods (colon-separated)                   |
| [`$imap_check_subscribed`](cfg-imap-check-subscribed)           | When opening a mailbox, ask the server for a list of subscribed folders         |
| [`$imap_condstore`](cfg-imap-condstore)                         | Enable the CONDSTORE extension                                                  |
| [`$imap_deflate`](cfg-imap-deflate)                             | Compress network traffic                                                        |
| [`$imap_delim_chars`](cfg-imap-delim-chars)                     | Characters that denote separators in IMAP folders                               |
| [`$imap_fetch_chunk_size`](cfg-imap-fetch-chunk-size)           | Download headers in blocks of this size                                         |
| [`$imap_headers`](cfg-imap-headers)                             | Additional email headers to download when getting index                         |
| [`$imap_idle`](cfg-imap-idle)                                   | Use the IMAP IDLE extension to check for new mail                               |
| `$imap_keepalive`                                               | {bdg-warning-line}`Renamed to:` [`$imap_keep_alive`](cfg-imap-keep-alive)       |
| [`$imap_keep_alive`](cfg-imap-keep-alive)                       | Time to wait before polling an open IMAP connection                             |
| [`$imap_list_subscribed`](cfg-imap-list-subscribed)             | When browsing a mailbox, only display subscribed folders                        |
| [`$imap_login`](cfg-imap-login)                                 | Login name for the IMAP server (defaults to [`$imap_user`](cfg-imap-user))      |
| [`$imap_oauth_refresh_command`](cfg-imap-oauth-refresh-command) | External command to generate OAUTH refresh token                                |
| [`$imap_pass`](cfg-imap-pass)                                   | Password for the IMAP server                                                    |
| [`$imap_passive`](cfg-imap-passive)                             | Reuse an existing IMAP connection to check for new mail                         |
| [`$imap_peek`](cfg-imap-peek)                                   | Don't mark messages as read when fetching them from the server                  |
| [`$imap_pipeline_depth`](cfg-imap-pipeline-depth)               | Number of IMAP commands that may be queued up                                   |
| [`$imap_poll_timeout`](cfg-imap-poll-timeout)                   | Maximum time to wait for a server response                                      |
| [`$imap_qresync`](cfg-imap-qresync)                             | Enable the QRESYNC extension                                                    |
| [`$imap_rfc5161`](cfg-imap-rfc5161)                             | Use the IMAP ENABLE extension to select capabilities                            |
| [`$imap_send_id`](cfg-imap-send-id)                             | Send ID command when logging in                                                 |
| `$imap_servernoise`                                             | {bdg-warning-line}`Renamed to:` [`$imap_server_noise`](cfg-imap-server-noise)   |
| [`$imap_server_noise`](cfg-imap-server-noise)                   | Display server warnings as error messages                                       |
| [`$imap_user`](cfg-imap-user)                                   | Username for the IMAP server                                                    |
| `$implicit_autoview`                                            | {bdg-warning-line}`Renamed to:` [`$implicit_auto_view`](cfg-implicit-auto-view) |
| [`$implicit_auto_view`](cfg-implicit-auto-view)                 | Display MIME attachments inline if a `copiousoutput` mailcap entry exists       |
| [`$include`](cfg-include)                                       | Include a copy of the email that's being replied to                             |
| [`$include_encrypted`](cfg-include-encrypted)                   | Whether to include encrypted content when replying                              |
| `$include_onlyfirst`                                            | {bdg-warning-line}`Renamed to:` [`$include_only_first`](cfg-include-only-first) |
| [`$include_only_first`](cfg-include-only-first)                 | Only include the first attachment when replying                                 |
| `$indent_str`                                                   | {bdg-warning-line}`Renamed to:` [`$indent_string`](cfg-indent-string)           |
| [`$indent_string`](cfg-indent-string)                           | String used to indent "reply" text                                              |
| [`$index_format`](cfg-index-format)                             | printf-like format string for the index menu (emails)                           |
| [`$inews_command`](cfg-inews-command)                           | External command to post news articles                                          |
| [`$ispell`](cfg-ispell)                                         | External command to perform spell-checking                                      |

## K

| Config Option                       | Description                                                                             |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| [`$keep_flagged`](cfg-keep-flagged) | Don't move flagged messages from [`$spool_file`](cfg-spool-file) to [`$mbox`](cfg-mbox) |

## L

| Config Option                                 | Description                                                                           |
|-----------------------------------------------|---------------------------------------------------------------------------------------|
| [`$local_date_header`](cfg-local-date-header) | Convert the date in the Date header of sent emails into local timezone, UTC otherwise |

## M

| Config Option                                                     | Description                                                                                                  |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [`$mailbox_folder_format`](cfg-mailbox-folder-format)             | printf-like format string for the browser's display of mailbox folders                                       |
| [`$mailcap_path`](cfg-mailcap-path)                               | List of mailcap files (colon-separated)                                                                      |
| [`$mailcap_sanitize`](cfg-mailcap-sanitize)                       | Restrict the possible characters in mailcap expandos                                                         |
| [`$maildir_check_cur`](cfg-maildir-check-cur)                     | Check both `new` and `cur` directories for new mail                                                          |
| [`$maildir_field_delimiter`](cfg-maildir-field-delimiter)         | Field delimiter to be used for maildir email files (default is colon, recommended alternative is semi-colon) |
| [`$maildir_header_cache_verify`](cfg-maildir-header-cache-verify) | Check for maildir changes when opening mailbox                                                               |
| [`$maildir_trash`](cfg-maildir-trash)                             | Use the maildir `trashed` flag, rather than deleting                                                         |
| [`$mail_check`](cfg-mail-check)                                   | Number of seconds before NeoMutt checks for new mail                                                         |
| [`$mail_check_recent`](cfg-mail-check-recent)                     | Notify the user about new mail since the last time the mailbox was opened                                    |
| [`$mail_check_stats`](cfg-mail-check-stats)                       | Periodically check for new mail                                                                              |
| [`$mail_check_stats_interval`](cfg-mail-check-stats-interval)     | How often to check for new mail                                                                              |
| [`$markers`](cfg-markers)                                         | Display a `+` at the beginning of wrapped lines in the pager                                                 |
| [`$mark_macro_prefix`](cfg-mark-macro-prefix)                     | Prefix for macros using `<mark-message>`                                                                     |
| [`$mark_old`](cfg-mark-old)                                       | Mark new emails as old when leaving the mailbox                                                              |
| [`$mask`](cfg-mask)                                               | Only display files/dirs matching this regex in the browser                                                   |
| [`$mbox`](cfg-mbox)                                               | Folder that receives read emails (see Move)                                                                  |
| [`$mbox_type`](cfg-mbox-type)                                     | Default type for creating new mailboxes                                                                      |
| [`$menu_context`](cfg-menu-context)                               | Number of lines of overlap when changing pages in the index                                                  |
| [`$menu_move_off`](cfg-menu-move-off)                             | Allow the last menu item to move off the bottom of the screen                                                |
| [`$menu_scroll`](cfg-menu-scroll)                                 | Scroll the menu/index by one line, rather than a page                                                        |
| `$message_cachedir`                                               | {bdg-warning-line}`Renamed to:` [`$message_cache_dir`](cfg-message-cache-dir)                                |
| [`$message_cache_clean`](cfg-message-cache-clean)                 | Clean out obsolete entries from the message cache                                                            |
| [`$message_cache_dir`](cfg-message-cache-dir)                     | Directory for the message cache                                                                              |
| [`$message_format`](cfg-message-format)                           | printf-like format string for listing attached messages                                                      |
| [`$message_id_format`](cfg-message-id-format)                     | printf-like format string for customising the `Message-Id`                                                   |
| [`$meta_key`](cfg-meta-key)                                       | Interpret 'ALT-x' as 'ESC-x'                                                                                 |
| `$metoo`                                                          | {bdg-warning-line}`Renamed to:` [`$me_too`](cfg-me-too)                                                      |
| [`$me_too`](cfg-me-too)                                           | Remove the user's address from the list of recipients                                                        |
| [`$mh_purge`](cfg-mh-purge)                                       | Really delete files in MH mailboxes                                                                          |
| [`$mh_seq_flagged`](cfg-mh-seq-flagged)                           | MH sequence for flagged message                                                                              |
| [`$mh_seq_replied`](cfg-mh-seq-replied)                           | MH sequence to tag replied messages                                                                          |
| [`$mh_seq_unseen`](cfg-mh-seq-unseen)                             | MH sequence for unseen messages                                                                              |
| [`$mime_forward`](cfg-mime-forward)                               | Forward a message as a `message/RFC822` MIME part                                                            |
| [`$mime_forward_decode`](cfg-mime-forward-decode)                 | Decode the forwarded message before attaching it                                                             |
| [`$mime_forward_rest`](cfg-mime-forward-rest)                     | Forward all attachments, even if they can't be decoded                                                       |
| `$mime_fwd`                                                       | {bdg-warning-line}`Renamed to:` [`$mime_forward`](cfg-mime-forward)                                          |
| `$mime_subject`                                                   | {bdg-danger-line}`Deprecated`                                                                                |
| [`$mime_type_query_command`](cfg-mime-type-query-command)         | External command to determine the MIME type of an attachment                                                 |
| [`$mime_type_query_first`](cfg-mime-type-query-first)             | Run the [`$mime_type_query_command`](cfg-mime-type-query-command) before the mime.types lookup               |
| `$mixmaster`                                                      | {bdg-danger-line}`Deprecated`                                                                                |
| `$mix_entry_format`                                               | {bdg-danger-line}`Deprecated`                                                                                |
| [`$move`](cfg-move)                                               | Move emails from [`$spool_file`](cfg-spool-file) to [`$mbox`](cfg-mbox) when read                            |
| `$msg_format`                                                     | {bdg-warning-line}`Renamed to:` [`$message_format`](cfg-message-format)                                      |

## N

| Config Option                                                               | Description                                                                 |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [`$narrow_tree`](cfg-narrow-tree)                                           | Draw a narrower thread tree in the index                                    |
| [`$net_inc`](cfg-net-inc)                                                   | Update the progress bar after this many KB sent/received (0 to disable)     |
| [`$newsgroups_charset`](cfg-newsgroups-charset)                             | Character set of newsgroups' descriptions                                   |
| [`$newsrc`](cfg-newsrc)                                                     | File containing list of subscribed newsgroups                               |
| [`$news_cache_dir`](cfg-news-cache-dir)                                     | Directory for cached news articles                                          |
| [`$news_server`](cfg-news-server)                                           | Url of the news server                                                      |
| [`$new_mail_command`](cfg-new-mail-command)                                 | External command to run when new mail arrives                               |
| [`$nm_config_file`](cfg-nm-config-file)                                     | Configuration file for notmuch. Use `auto` to detect configuration.         |
| [`$nm_config_profile`](cfg-nm-config-profile)                               | Configuration profile for notmuch.                                          |
| [`$nm_db_limit`](cfg-nm-db-limit)                                           | Default limit for Notmuch queries                                           |
| `$nm_default_uri`                                                           | {bdg-warning-line}`Renamed to:` [`$nm_default_url`](cfg-nm-default-url)     |
| [`$nm_default_url`](cfg-nm-default-url)                                     | Path to the Notmuch database                                                |
| [`$nm_exclude_tags`](cfg-nm-exclude-tags)                                   | Exclude messages with these tags                                            |
| [`$nm_flagged_tag`](cfg-nm-flagged-tag)                                     | Tag to use for flagged messages                                             |
| [`$nm_open_timeout`](cfg-nm-open-timeout)                                   | Database timeout                                                            |
| [`$nm_query_type`](cfg-nm-query-type)                                       | Default query type: `threads` or `messages`                                 |
| [`$nm_query_window_current_position`](cfg-nm-query-window-current-position) | Position of current search window                                           |
| [`$nm_query_window_current_search`](cfg-nm-query-window-current-search)     | Current search parameters                                                   |
| [`$nm_query_window_duration`](cfg-nm-query-window-duration)                 | Time duration of the current search window                                  |
| [`$nm_query_window_enable`](cfg-nm-query-window-enable)                     | Enable query windows                                                        |
| [`$nm_query_window_or_terms`](cfg-nm-query-window-or-terms)                 | Additional notmuch search terms for messages to be shown regardless of date |
| [`$nm_query_window_timebase`](cfg-nm-query-window-timebase)                 | Units for the time duration                                                 |
| [`$nm_record`](cfg-nm-record)                                               | If the [`$record`](cfg-record) mailbox (sent mail) should be indexed        |
| [`$nm_record_tags`](cfg-nm-record-tags)                                     | Tags to apply to the [`$record`](cfg-record) mailbox (sent mail)            |
| [`$nm_replied_tag`](cfg-nm-replied-tag)                                     | Tag to use for replied messages                                             |
| [`$nm_unread_tag`](cfg-nm-unread-tag)                                       | Tag to use for unread messages                                              |
| [`$nntp_authenticators`](cfg-nntp-authenticators)                           | Allowed authentication methods                                              |
| [`$nntp_context`](cfg-nntp-context)                                         | Maximum number of articles to list (0 for all articles)                     |
| [`$nntp_listgroup`](cfg-nntp-listgroup)                                     | Check all articles when opening a newsgroup                                 |
| [`$nntp_load_description`](cfg-nntp-load-description)                       | Load descriptions for newsgroups when adding to the list                    |
| [`$nntp_pass`](cfg-nntp-pass)                                               | Password for the news server                                                |
| [`$nntp_poll`](cfg-nntp-poll)                                               | Interval between checks for new posts                                       |
| [`$nntp_user`](cfg-nntp-user)                                               | Username for the news server                                                |

## P

| Config Option                                                             | Description                                                                                     |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [`$pager`](cfg-pager)                                                     | External command for viewing messages, or empty to use NeoMutt's                                |
| [`$pager_context`](cfg-pager-context)                                     | Number of lines of overlap when changing pages in the pager                                     |
| [`$pager_format`](cfg-pager-format)                                       | printf-like format string for the pager's status bar                                            |
| [`$pager_index_lines`](cfg-pager-index-lines)                             | Number of index lines to display above the pager                                                |
| [`$pager_read_delay`](cfg-pager-read-delay)                               | Number of seconds to wait before marking a message read                                         |
| [`$pager_skip_quoted_context`](cfg-pager-skip-quoted-context)             | Lines of context to show when skipping quoted text                                              |
| [`$pager_stop`](cfg-pager-stop)                                           | Don't automatically open the next message when at the end of a message                          |
| [`$pattern_format`](cfg-pattern-format)                                   | printf-like format string for the pattern completion menu                                       |
| `$pgp_autoencrypt`                                                        | {bdg-warning-line}`Renamed to:` [`$crypt_auto_encrypt`](cfg-crypt-auto-encrypt)                 |
| `$pgp_autoinline`                                                         | {bdg-warning-line}`Renamed to:` [`$pgp_auto_inline`](cfg-pgp-auto-inline)                       |
| `$pgp_autosign`                                                           | {bdg-warning-line}`Renamed to:` [`$crypt_auto_sign`](cfg-crypt-auto-sign)                       |
| [`$pgp_auto_decode`](cfg-pgp-auto-decode)                                 | Automatically decrypt PGP messages                                                              |
| [`$pgp_auto_inline`](cfg-pgp-auto-inline)                                 | Use old-style inline PGP messages (not recommended)                                             |
| `$pgp_auto_traditional`                                                   | {bdg-warning-line}`Renamed to:` [`$pgp_reply_inline`](cfg-pgp-reply-inline)                     |
| [`$pgp_check_exit`](cfg-pgp-check-exit)                                   | Check the exit code of PGP subprocess                                                           |
| [`$pgp_check_gpg_decrypt_status_fd`](cfg-pgp-check-gpg-decrypt-status-fd) | File descriptor used for status info                                                            |
| `$pgp_clearsign_command`                                                  | {bdg-warning-line}`Renamed to:` [`$pgp_clear_sign_command`](cfg-pgp-clear-sign-command)         |
| [`$pgp_clear_sign_command`](cfg-pgp-clear-sign-command)                   | External command to inline-sign a message                                                       |
| `$pgp_create_traditional`                                                 | {bdg-warning-line}`Renamed to:` [`$pgp_auto_inline`](cfg-pgp-auto-inline)                       |
| [`$pgp_decode_command`](cfg-pgp-decode-command)                           | External command to decode a PGP attachment                                                     |
| [`$pgp_decryption_okay`](cfg-pgp-decryption-okay)                         | Text indicating a successful decryption                                                         |
| [`$pgp_decrypt_command`](cfg-pgp-decrypt-command)                         | External command to decrypt a PGP message                                                       |
| [`$pgp_default_key`](cfg-pgp-default-key)                                 | Default key to use for PGP operations                                                           |
| [`$pgp_encrypt_only_command`](cfg-pgp-encrypt-only-command)               | External command to encrypt, but not sign a message                                             |
| `$pgp_encrypt_self`                                                       | {bdg-danger-line}`Deprecated`                                                                   |
| [`$pgp_encrypt_sign_command`](cfg-pgp-encrypt-sign-command)               | External command to encrypt and sign a message                                                  |
| [`$pgp_entry_format`](cfg-pgp-entry-format)                               | printf-like format string for the PGP key selection menu                                        |
| [`$pgp_export_command`](cfg-pgp-export-command)                           | External command to export a public key from the user's keyring                                 |
| `$pgp_getkeys_command`                                                    | {bdg-warning-line}`Renamed to:` [`$pgp_get_keys_command`](cfg-pgp-get-keys-command)             |
| [`$pgp_get_keys_command`](cfg-pgp-get-keys-command)                       | External command to download a key for an email address                                         |
| [`$pgp_good_sign`](cfg-pgp-good-sign)                                     | Text indicating a good signature                                                                |
| [`$pgp_ignore_subkeys`](cfg-pgp-ignore-subkeys)                           | Only use the principal PGP key                                                                  |
| [`$pgp_import_command`](cfg-pgp-import-command)                           | External command to import a key into the user's keyring                                        |
| [`$pgp_key_sort`](cfg-pgp-key-sort)                                       | Sort order for PGP keys                                                                         |
| [`$pgp_list_pubring_command`](cfg-pgp-list-pubring-command)               | External command to list the public keys in a user's keyring                                    |
| [`$pgp_list_secring_command`](cfg-pgp-list-secring-command)               | External command to list the private keys in a user's keyring                                   |
| [`$pgp_long_ids`](cfg-pgp-long-ids)                                       | Display long PGP key IDs to the user                                                            |
| [`$pgp_mime_auto`](cfg-pgp-mime-auto)                                     | Prompt the user to use MIME if inline PGP fails                                                 |
| `$pgp_replyencrypt`                                                       | {bdg-warning-line}`Renamed to:` [`$crypt_reply_encrypt`](cfg-crypt-reply-encrypt)               |
| `$pgp_replyinline`                                                        | {bdg-warning-line}`Renamed to:` [`$pgp_reply_inline`](cfg-pgp-reply-inline)                     |
| `$pgp_replysign`                                                          | {bdg-warning-line}`Renamed to:` [`$crypt_reply_sign`](cfg-crypt-reply-sign)                     |
| `$pgp_replysignencrypted`                                                 | {bdg-warning-line}`Renamed to:` [`$crypt_reply_sign_encrypted`](cfg-crypt-reply-sign-encrypted) |
| [`$pgp_reply_inline`](cfg-pgp-reply-inline)                               | Reply using old-style inline PGP messages (not recommended)                                     |
| [`$pgp_retainable_sigs`](cfg-pgp-retainable-sigs)                         | Create nested multipart/signed or encrypted messages                                            |
| [`$pgp_self_encrypt`](cfg-pgp-self-encrypt)                               | Encrypted messages will also be encrypted to [`$pgp_default_key`](cfg-pgp-default-key) too      |
| `$pgp_self_encrypt_as`                                                    | {bdg-warning-line}`Renamed to:` [`$pgp_default_key`](cfg-pgp-default-key)                       |
| [`$pgp_show_unusable`](cfg-pgp-show-unusable)                             | Show non-usable keys in the key selection                                                       |
| [`$pgp_sign_as`](cfg-pgp-sign-as)                                         | Use this alternative key for signing messages                                                   |
| [`$pgp_sign_command`](cfg-pgp-sign-command)                               | External command to create a detached PGP signature                                             |
| `$pgp_sort_keys`                                                          | {bdg-warning-line}`Renamed to:` [`$pgp_key_sort`](cfg-pgp-key-sort)                             |
| [`$pgp_strict_enc`](cfg-pgp-strict-enc)                                   | Encode PGP signed messages with quoted-printable (don't unset)                                  |
| [`$pgp_timeout`](cfg-pgp-timeout)                                         | Time in seconds to cache a passphrase                                                           |
| [`$pgp_use_gpg_agent`](cfg-pgp-use-gpg-agent)                             | Use a PGP agent for caching passwords                                                           |
| [`$pgp_verify_command`](cfg-pgp-verify-command)                           | External command to verify PGP signatures                                                       |
| [`$pgp_verify_key_command`](cfg-pgp-verify-key-command)                   | External command to verify key information                                                      |
| `$pgp_verify_sig`                                                         | {bdg-warning-line}`Renamed to:` [`$crypt_verify_sig`](cfg-crypt-verify-sig)                     |
| [`$pipe_decode`](cfg-pipe-decode)                                         | Decode the message when piping it                                                               |
| [`$pipe_decode_weed`](cfg-pipe-decode-weed)                               | Control whether to weed headers when piping an email                                            |
| [`$pipe_sep`](cfg-pipe-sep)                                               | Separator to add between multiple piped messages                                                |
| [`$pipe_split`](cfg-pipe-split)                                           | Run the pipe command on each message separately                                                 |
| [`$pop_authenticators`](cfg-pop-authenticators)                           | List of allowed authentication methods (colon-separated)                                        |
| [`$pop_auth_try_all`](cfg-pop-auth-try-all)                               | Try all available authentication methods                                                        |
| `$pop_checkinterval`                                                      | {bdg-warning-line}`Renamed to:` [`$pop_check_interval`](cfg-pop-check-interval)                 |
| [`$pop_check_interval`](cfg-pop-check-interval)                           | Interval between checks for new mail                                                            |
| [`$pop_delete`](cfg-pop-delete)                                           | After downloading POP messages, delete them on the server                                       |
| [`$pop_host`](cfg-pop-host)                                               | Url of the POP server                                                                           |
| [`$pop_last`](cfg-pop-last)                                               | Use the `LAST` command to fetch new mail                                                        |
| [`$pop_oauth_refresh_command`](cfg-pop-oauth-refresh-command)             | External command to generate OAUTH refresh token                                                |
| [`$pop_pass`](cfg-pop-pass)                                               | Password of the POP server                                                                      |
| [`$pop_reconnect`](cfg-pop-reconnect)                                     | Reconnect to the server is the connection is lost                                               |
| [`$pop_user`](cfg-pop-user)                                               | Username of the POP server                                                                      |
| [`$postpone`](cfg-postpone)                                               | Save messages to the [`$postponed`](cfg-postponed) folder                                       |
| [`$postponed`](cfg-postponed)                                             | Folder to store postponed messages                                                              |
| [`$postpone_encrypt`](cfg-postpone-encrypt)                               | Self-encrypt postponed messages                                                                 |
| [`$postpone_encrypt_as`](cfg-postpone-encrypt-as)                         | Fallback encryption key for postponed messages                                                  |
| `$post_indent_str`                                                        | {bdg-warning-line}`Renamed to:` `$post_indent_string`                                           |
| `$post_indent_string`                                                     | {bdg-warning-line}`Renamed to:` [`$attribution_trailer`](cfg-attribution-trailer)               |
| [`$post_moderated`](cfg-post-moderated)                                   | Allow posting to moderated newsgroups                                                           |
| [`$preconnect`](cfg-preconnect)                                           | External command to run prior to opening a socket                                               |
| [`$preferred_languages`](cfg-preferred-languages)                         | List of Preferred Languages for multilingual MIME (comma-separated)                             |
| [`$print`](cfg-print)                                                     | Confirm before printing a message                                                               |
| `$print_cmd`                                                              | {bdg-warning-line}`Renamed to:` [`$print_command`](cfg-print-command)                           |
| [`$print_command`](cfg-print-command)                                     | External command to print a message                                                             |
| [`$print_decode`](cfg-print-decode)                                       | Decode message before printing it                                                               |
| [`$print_decode_weed`](cfg-print-decode-weed)                             | Control whether to weed headers when printing an email                                          |
| [`$print_split`](cfg-print-split)                                         | Print multiple messages separately                                                              |
| [`$prompt_after`](cfg-prompt-after)                                       | Pause after running an external pager                                                           |

## Q

| Config Option                         | Description                                                       |
|---------------------------------------|-------------------------------------------------------------------|
| [`$query_command`](cfg-query-command) | External command to query and external address book               |
| [`$query_format`](cfg-query-format)   | printf-like format string for the query menu (address book)       |
| [`$quit`](cfg-quit)                   | Prompt before exiting NeoMutt                                     |
| [`$quote_regex`](cfg-quote-regex)     | Regex to match quoted text in a reply                             |
| `$quote_regexp`                       | {bdg-warning-line}`Renamed to:` [`$quote_regex`](cfg-quote-regex) |

## R

| Config Option                                                 | Description                                                                   |
|---------------------------------------------------------------|-------------------------------------------------------------------------------|
| [`$read_inc`](cfg-read-inc)                                   | Update the progress bar after this many records read (0 to disable)           |
| [`$read_only`](cfg-read-only)                                 | Open folders in read-only mode                                                |
| `$realname`                                                   | {bdg-warning-line}`Renamed to:` [`$real_name`](cfg-real-name)                 |
| [`$real_name`](cfg-real-name)                                 | Real name of the user                                                         |
| [`$recall`](cfg-recall)                                       | Recall postponed mesaages when asked to compose a message                     |
| [`$record`](cfg-record)                                       | Folder to save 'sent' messages                                                |
| [`$reflow_space_quotes`](cfg-reflow-space-quotes)             | Insert spaces into reply quotes for `format=flowed` messages                  |
| [`$reflow_text`](cfg-reflow-text)                             | Reformat paragraphs of `format=flowed` text                                   |
| [`$reflow_wrap`](cfg-reflow-wrap)                             | Maximum paragraph width for reformatting `format=flowed` text                 |
| [`$reply_regex`](cfg-reply-regex)                             | Regex to match message reply subjects like `re: `                             |
| `$reply_regexp`                                               | {bdg-warning-line}`Renamed to:` [`$reply_regex`](cfg-reply-regex)             |
| [`$reply_self`](cfg-reply-self)                               | Really reply to yourself, when replying to your own email                     |
| [`$reply_to`](cfg-reply-to)                                   | Address to use as a `Reply-To` header                                         |
| [`$reply_with_xorig`](cfg-reply-with-xorig)                   | Create `From` header from `X-Original-To` header                              |
| [`$resolve`](cfg-resolve)                                     | Move to the next email whenever a command modifies an email                   |
| [`$resume_draft_files`](cfg-resume-draft-files)               | Process draft files like postponed messages                                   |
| [`$resume_edited_draft_files`](cfg-resume-edited-draft-files) | Resume editing previously saved draft files                                   |
| [`$reverse_alias`](cfg-reverse-alias)                         | Display the alias in the index, rather than the message's sender              |
| [`$reverse_name`](cfg-reverse-name)                           | Set the `From` from the address the email was sent to                         |
| `$reverse_realname`                                           | {bdg-warning-line}`Renamed to:` [`$reverse_real_name`](cfg-reverse-real-name) |
| [`$reverse_real_name`](cfg-reverse-real-name)                 | Set the `From` from the full `To` address the email was sent to               |
| [`$rfc2047_parameters`](cfg-rfc2047-parameters)               | Decode RFC2047-encoded MIME parameters                                        |

## S

| Config Option                                                           | Description                                                                                                |
|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [`$save_address`](cfg-save-address)                                     | Use sender's full address as a default save folder                                                         |
| [`$save_empty`](cfg-save-empty)                                         | Preserve empty mailboxes                                                                                   |
| [`$save_history`](cfg-save-history)                                     | Number of history entries to save per category                                                             |
| [`$save_name`](cfg-save-name)                                           | Save outgoing message to mailbox of recipient's name if it exists                                          |
| [`$save_unsubscribed`](cfg-save-unsubscribed)                           | Save a list of unsubscribed newsgroups to the `newsrc`                                                     |
| [`$score`](cfg-score)                                                   | Use message scoring                                                                                        |
| [`$score_threshold_delete`](cfg-score-threshold-delete)                 | Messages with a lower score will be automatically deleted                                                  |
| [`$score_threshold_flag`](cfg-score-threshold-flag)                     | Messages with a greater score will be automatically flagged                                                |
| [`$score_threshold_read`](cfg-score-threshold-read)                     | Messages with a lower score will be automatically marked read                                              |
| [`$search_context`](cfg-search-context)                                 | Context to display around search matches                                                                   |
| [`$sendmail`](cfg-sendmail)                                             | External command to send email                                                                             |
| [`$sendmail_wait`](cfg-sendmail-wait)                                   | Time to wait for sendmail to finish                                                                        |
| [`$send_charset`](cfg-send-charset)                                     | Character sets for outgoing mail                                                                           |
| [`$shell`](cfg-shell)                                                   | External command to run subshells in                                                                       |
| [`$show_multipart_alternative`](cfg-show-multipart-alternative)         | How to display `multipart/alternative` MIME parts                                                          |
| [`$show_new_news`](cfg-show-new-news)                                   | Check for new newsgroups when entering the browser                                                         |
| [`$show_only_unread`](cfg-show-only-unread)                             | Only show subscribed newsgroups with unread articles                                                       |
| [`$sidebar_component_depth`](cfg-sidebar-component-depth)               | Strip leading path components from sidebar folders                                                         |
| [`$sidebar_delim_chars`](cfg-sidebar-delim-chars)                       | Characters that separate nested folders                                                                    |
| [`$sidebar_divider_char`](cfg-sidebar-divider-char)                     | Character to draw between the sidebar and index                                                            |
| [`$sidebar_folder_indent`](cfg-sidebar-folder-indent)                   | Indent nested folders                                                                                      |
| [`$sidebar_format`](cfg-sidebar-format)                                 | printf-like format string for the sidebar panel                                                            |
| [`$sidebar_indent_string`](cfg-sidebar-indent-string)                   | Indent nested folders using this string                                                                    |
| [`$sidebar_new_mail_only`](cfg-sidebar-new-mail-only)                   | Only show folders with new/flagged mail                                                                    |
| [`$sidebar_next_new_wrap`](cfg-sidebar-next-new-wrap)                   | Wrap around when searching for the next mailbox with new mail                                              |
| [`$sidebar_non_empty_mailbox_only`](cfg-sidebar-non-empty-mailbox-only) | Only show folders with a non-zero number of mail                                                           |
| [`$sidebar_on_right`](cfg-sidebar-on-right)                             | Display the sidebar on the right                                                                           |
| [`$sidebar_short_path`](cfg-sidebar-short-path)                         | Abbreviate the paths using the [`$folder`](cfg-folder) variable                                            |
| [`$sidebar_sort`](cfg-sidebar-sort)                                     | Method to sort the sidebar                                                                                 |
| `$sidebar_sort_method`                                                  | {bdg-warning-line}`Renamed to:` [`$sidebar_sort`](cfg-sidebar-sort)                                        |
| [`$sidebar_visible`](cfg-sidebar-visible)                               | Show the sidebar                                                                                           |
| [`$sidebar_width`](cfg-sidebar-width)                                   | Width of the sidebar                                                                                       |
| [`$signature`](cfg-signature)                                           | File containing a signature to append to all mail                                                          |
| [`$sig_dashes`](cfg-sig-dashes)                                         | Insert `-- ` before the signature                                                                          |
| [`$sig_on_top`](cfg-sig-on-top)                                         | Insert the signature before the quoted text                                                                |
| [`$simple_search`](cfg-simple-search)                                   | Pattern to search for when search doesn't contain `~`s                                                     |
| [`$size_show_bytes`](cfg-size-show-bytes)                               | Show smaller sizes in bytes                                                                                |
| [`$size_show_fractions`](cfg-size-show-fractions)                       | Show size fractions with a single decimal place                                                            |
| [`$size_show_mb`](cfg-size-show-mb)                                     | Show sizes in megabytes for sizes greater than 1 megabyte                                                  |
| [`$size_units_on_left`](cfg-size-units-on-left)                         | Show the units as a prefix to the size                                                                     |
| `$skip_quoted_offset`                                                   | {bdg-warning-line}`Renamed to:` [`$pager_skip_quoted_context`](cfg-pager-skip-quoted-context)              |
| [`$sleep_time`](cfg-sleep-time)                                         | Time to pause after certain info messages                                                                  |
| [`$smart_wrap`](cfg-smart-wrap)                                         | Wrap text at word boundaries                                                                               |
| [`$smileys`](cfg-smileys)                                               | Regex to match smileys to prevent mistakes when quoting text                                               |
| [`$smime_ask_cert_label`](cfg-smime-ask-cert-label)                     | Prompt the user for a label for SMIME certificates                                                         |
| [`$smime_ca_location`](cfg-smime-ca-location)                           | File containing trusted certificates                                                                       |
| [`$smime_certificates`](cfg-smime-certificates)                         | File containing user's public certificates                                                                 |
| [`$smime_decrypt_command`](cfg-smime-decrypt-command)                   | External command to decrypt an SMIME message                                                               |
| [`$smime_decrypt_use_default_key`](cfg-smime-decrypt-use-default-key)   | Use the default key for decryption                                                                         |
| [`$smime_default_key`](cfg-smime-default-key)                           | Default key for SMIME operations                                                                           |
| [`$smime_encrypt_command`](cfg-smime-encrypt-command)                   | External command to encrypt a message                                                                      |
| `$smime_encrypt_self`                                                   | {bdg-danger-line}`Deprecated`                                                                              |
| [`$smime_encrypt_with`](cfg-smime-encrypt-with)                         | Algorithm for encryption                                                                                   |
| [`$smime_get_cert_command`](cfg-smime-get-cert-command)                 | External command to extract a certificate from a message                                                   |
| [`$smime_get_cert_email_command`](cfg-smime-get-cert-email-command)     | External command to get a certificate for an email                                                         |
| [`$smime_get_signer_cert_command`](cfg-smime-get-signer-cert-command)   | External command to extract a certificate from an email                                                    |
| [`$smime_import_cert_command`](cfg-smime-import-cert-command)           | External command to import a certificate                                                                   |
| [`$smime_is_default`](cfg-smime-is-default)                             | Use SMIME rather than PGP by default                                                                       |
| [`$smime_keys`](cfg-smime-keys)                                         | File containing user's private certificates                                                                |
| [`$smime_pk7out_command`](cfg-smime-pk7out-command)                     | External command to extract a public certificate                                                           |
| [`$smime_self_encrypt`](cfg-smime-self-encrypt)                         | Encrypted messages will also be encrypt to [`$smime_default_key`](cfg-smime-default-key) too               |
| `$smime_self_encrypt_as`                                                | {bdg-warning-line}`Renamed to:` [`$smime_default_key`](cfg-smime-default-key)                              |
| [`$smime_sign_as`](cfg-smime-sign-as)                                   | Use this alternative key for signing messages                                                              |
| [`$smime_sign_command`](cfg-smime-sign-command)                         | External command to sign a message                                                                         |
| [`$smime_sign_digest_alg`](cfg-smime-sign-digest-alg)                   | Digest algorithm                                                                                           |
| [`$smime_timeout`](cfg-smime-timeout)                                   | Time in seconds to cache a passphrase                                                                      |
| [`$smime_verify_command`](cfg-smime-verify-command)                     | External command to verify a signed message                                                                |
| [`$smime_verify_opaque_command`](cfg-smime-verify-opaque-command)       | External command to verify a signature                                                                     |
| [`$smtp_authenticators`](cfg-smtp-authenticators)                       | List of allowed authentication methods (colon-separated)                                                   |
| [`$smtp_oauth_refresh_command`](cfg-smtp-oauth-refresh-command)         | External command to generate OAUTH refresh token                                                           |
| [`$smtp_pass`](cfg-smtp-pass)                                           | Password for the SMTP server                                                                               |
| [`$smtp_url`](cfg-smtp-url)                                             | Url of the SMTP server                                                                                     |
| [`$smtp_user`](cfg-smtp-user)                                           | Username for the SMTP server                                                                               |
| [`$socket_timeout`](cfg-socket-timeout)                                 | Timeout for socket connect/read/write operations (-1 to wait indefinitely)                                 |
| [`$sort`](cfg-sort)                                                     | Sort method for the index                                                                                  |
| `$sort_alias`                                                           | {bdg-warning-line}`Renamed to:` [`$alias_sort`](cfg-alias-sort)                                            |
| [`$sort_aux`](cfg-sort-aux)                                             | Secondary sort method for the index                                                                        |
| `$sort_browser`                                                         | {bdg-warning-line}`Renamed to:` [`$browser_sort`](cfg-browser-sort)                                        |
| [`$sort_re`](cfg-sort-re)                                               | Whether [`$reply_regex`](cfg-reply-regex) must be matched when not [`$strict_threads`](cfg-strict-threads) |
| [`$spam_separator`](cfg-spam-separator)                                 | Separator for multiple spam headers                                                                        |
| `$spoolfile`                                                            | {bdg-warning-line}`Renamed to:` [`$spool_file`](cfg-spool-file)                                            |
| [`$spool_file`](cfg-spool-file)                                         | Inbox                                                                                                      |
| [`$ssl_ca_certificates_file`](cfg-ssl-ca-certificates-file)             | File containing trusted CA certificates                                                                    |
| [`$ssl_ciphers`](cfg-ssl-ciphers)                                       | Ciphers to use when using SSL                                                                              |
| [`$ssl_client_cert`](cfg-ssl-client-cert)                               | File containing client certificates                                                                        |
| [`$ssl_force_tls`](cfg-ssl-force-tls)                                   | Require TLS encryption for all connections                                                                 |
| [`$ssl_min_dh_prime_bits`](cfg-ssl-min-dh-prime-bits)                   | Minimum keysize for Diffie-Hellman key exchange                                                            |
| [`$ssl_starttls`](cfg-ssl-starttls)                                     | Use STARTTLS on servers advertising the capability                                                         |
| `$ssl_usesystemcerts`                                                   | {bdg-warning-line}`Renamed to:` [`$ssl_use_system_certs`](cfg-ssl-use-system-certs)                        |
| `$ssl_use_sslv2`                                                        | {bdg-danger-line}`Deprecated`                                                                              |
| `$ssl_use_sslv3`                                                        | {bdg-danger-line}`Deprecated`                                                                              |
| [`$ssl_use_system_certs`](cfg-ssl-use-system-certs)                     | Use CA certificates in the system-wide store                                                               |
| `$ssl_use_tlsv1`                                                        | {bdg-danger-line}`Deprecated`                                                                              |
| `$ssl_use_tlsv1_1`                                                      | {bdg-danger-line}`Deprecated`                                                                              |
| [`$ssl_use_tlsv1_2`](cfg-ssl-use-tlsv1-2)                               | Use TLSv1.2 for authentication                                                                             |
| [`$ssl_use_tlsv1_3`](cfg-ssl-use-tlsv1-3)                               | Use TLSv1.3 for authentication                                                                             |
| [`$ssl_verify_dates`](cfg-ssl-verify-dates)                             | Verify the dates on the server certificate                                                                 |
| [`$ssl_verify_host`](cfg-ssl-verify-host)                               | Verify the server's hostname against the certificate                                                       |
| [`$ssl_verify_partial_chains`](cfg-ssl-verify-partial-chains)           | Allow verification using partial certificate chains                                                        |
| [`$status_chars`](cfg-status-chars)                                     | Indicator characters for the status bar                                                                    |
| [`$status_format`](cfg-status-format)                                   | printf-like format string for the index's status line                                                      |
| [`$status_on_top`](cfg-status-on-top)                                   | Display the status bar at the top                                                                          |
| [`$strict_threads`](cfg-strict-threads)                                 | Thread messages using `In-Reply-To` and `References` headers                                               |
| [`$suspend`](cfg-suspend)                                               | Allow the user to suspend NeoMutt using `^Z`                                                               |

## T

| Config Option                                                 | Description                                                        |
|---------------------------------------------------------------|--------------------------------------------------------------------|
| [`$text_flowed`](cfg-text-flowed)                             | Generate `format=flowed` messages                                  |
| [`$thorough_search`](cfg-thorough-search)                     | Decode headers and messages before searching them                  |
| [`$thread_received`](cfg-thread-received)                     | Sort threaded messages by their received date                      |
| [`$tilde`](cfg-tilde)                                         | Display `~` in the pager after the end of the email                |
| [`$timeout`](cfg-timeout)                                     | Time to wait for user input in menus                               |
| [`$time_inc`](cfg-time-inc)                                   | Frequency of progress bar updates (milliseconds)                   |
| `$tmpdir`                                                     | {bdg-warning-line}`Renamed to:` [`$tmp_dir`](cfg-tmp-dir)          |
| [`$tmp_dir`](cfg-tmp-dir)                                     | Directory for temporary files                                      |
| [`$toggle_quoted_show_levels`](cfg-toggle-quoted-show-levels) | Number of quote levels to show with toggle-quoted                  |
| [`$to_chars`](cfg-to-chars)                                   | Indicator characters for the `To` field in the index               |
| [`$trash`](cfg-trash)                                         | Folder to put deleted emails                                       |
| [`$ts_enabled`](cfg-ts-enabled)                               | Allow NeoMutt to set the terminal status line and icon             |
| [`$ts_icon_format`](cfg-ts-icon-format)                       | printf-like format string for the terminal's icon title            |
| [`$ts_status_format`](cfg-ts-status-format)                   | printf-like format string for the terminal's status (window title) |
| [`$tunnel`](cfg-tunnel)                                       | Shell command to establish a tunnel                                |
| [`$tunnel_is_secure`](cfg-tunnel-is-secure)                   | Assume a tunneled connection is secure                             |

## U

| Config Option                                 | Description                                                           |
|-----------------------------------------------|-----------------------------------------------------------------------|
| [`$uncollapse_jump`](cfg-uncollapse-jump)     | When opening a thread, jump to the next unread message                |
| [`$uncollapse_new`](cfg-uncollapse-new)       | Open collapsed threads when new mail arrives                          |
| [`$user_agent`](cfg-user-agent)               | Add a `User-Agent` header to outgoing mail                            |
| `$use_8bitmime`                               | {bdg-warning-line}`Renamed to:` [`$use_8bit_mime`](cfg-use-8bit-mime) |
| [`$use_8bit_mime`](cfg-use-8bit-mime)         | Use 8-bit messages and ESMTP to send messages                         |
| [`$use_domain`](cfg-use-domain)               | Qualify local addresses using this domain                             |
| [`$use_envelope_from`](cfg-use-envelope-from) | Set the envelope sender of the message                                |
| [`$use_from`](cfg-use-from)                   | Set the `From` header for outgoing mail                               |
| [`$use_ipv6`](cfg-use-ipv6)                   | Lookup IPv6 addresses when making connections                         |
| [`$use_threads`](cfg-use-threads)             | Whether to use threads for the index                                  |

## V

| Config Option                                   | Description                                                                     |
|-------------------------------------------------|---------------------------------------------------------------------------------|
| `$vfolder_format`                               | {bdg-danger-line}`Deprecated`                                                   |
| `$virtual_spoolfile`                            | {bdg-warning-line}`Renamed to:` [`$virtual_spool_file`](cfg-virtual-spool-file) |
| [`$virtual_spool_file`](cfg-virtual-spool-file) | Use the first virtual mailbox as a spool file                                   |
| `$visual`                                       | {bdg-danger-line}`Deprecated`                                                   |

## W

| Config Option                       | Description                                                            |
|-------------------------------------|------------------------------------------------------------------------|
| [`$wait_key`](cfg-wait-key)         | Prompt to press a key after running external commands                  |
| [`$weed`](cfg-weed)                 | Filter headers when displaying/forwarding/printing/replying            |
| [`$wrap`](cfg-wrap)                 | Width to wrap text in the pager                                        |
| [`$wrap_headers`](cfg-wrap-headers) | Width to wrap headers in outgoing messages                             |
| [`$wrap_search`](cfg-wrap-search)   | Wrap around when the search hits the end                               |
| [`$write_bcc`](cfg-write-bcc)       | Write out the `Bcc` field when preparing to send a mail                |
| [`$write_inc`](cfg-write-inc)       | Update the progress bar after this many records written (0 to disable) |

## X

| Config Option                       | Description                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|
| `$xterm_icon`                       | {bdg-warning-line}`Renamed to:` [`$ts_icon_format`](cfg-ts-icon-format)     |
| `$xterm_set_titles`                 | {bdg-warning-line}`Renamed to:` [`$ts_enabled`](cfg-ts-enabled)             |
| `$xterm_title`                      | {bdg-warning-line}`Renamed to:` [`$ts_status_format`](cfg-ts-status-format) |
| [`$x_comment_to`](cfg-x-comment-to) | Add `X-Comment-To` header that contains article author                      |

```{toctree}
---
maxdepth: 1
hidden:
---
address
alias
attach
autocrypt
browser
compose
conn
email
general
gui
hcache
history
hooks
imap
index2
maildir
mbox
menu
mh
ncrypt
nntp
notmuch
pager
pattern
pop
progress
send
sidebar
```

