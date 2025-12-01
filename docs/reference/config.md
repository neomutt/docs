---
title: Configuration reference
description: NeoMutt configuration options, grouped by topic.
sidebar: docs/reference/index
difficulty: Advanced
diataxis: Reference
last_updated: 2025-11-26
---

# Config Options

## A

| Config Option                   | Description                                                                 |
| :------------------------------ | :-------------------------------------------------------------------------- |
| `abort_backspace`               | Hitting backspace against an empty prompt aborts the prompt                 |
| `abort_key`                     | String representation of key to abort prompts                               |
| `abort_noattach`                | Abort sending the email if attachments are missing                          |
| `abort_noattach_regex`          | Regex to match text indicating attachments are expected                     |
| `abort_noattach_regexp`         | Renamed to: `abort_noattach_regex`                                          |
| `abort_nosubject`               | Abort creating the email if subject is missing                              |
| `abort_unmodified`              | Abort the sending if the message hasn't been edited                         |
| `account_command`               | Shell command to retrieve account credentials                               |
| `alias_file`                    | Save new aliases to this file                                               |
| `alias_format`                  | printf-like format string for the alias menu                                |
| `alias_sort`                    | Sort method for the alias menu                                              |
| `allow_8bit`                    | Allow 8-bit messages, don't use quoted-printable or base64                  |
| `allow_ansi`                    | Allow ANSI color codes in rich text messages                                |
| `arrow_cursor`                  | Use an arrow '->' instead of highlighting in the index                      |
| `arrow_string`                  | Use a custom string for `arrow_cursor`                                      |
| `ascii_chars`                   | Use plain ASCII characters, when drawing email threads                      |
| `askbcc`                        | Renamed to: `ask_bcc`                                                       |
| `askcc`                         | Renamed to: `ask_cc`                                                        |
| `ask_bcc`                       | Ask the user for the blind-carbon-copy recipients                           |
| `ask_cc`                        | Ask the user for the carbon-copy recipients                                 |
| `ask_followup_to`               | Ask the user for follow-up groups before editing                            |
| `ask_follow_up`                 | Renamed to: `ask_followup_to`                                               |
| `ask_x_comment_to`              | Ask the user for the 'X-Comment-To' field before editing                    |
| `assumed_charset`               | If a message is missing a character set, assume this character set          |
| `attach_charset`                | When attaching files, use one of these character sets                       |
| `attach_format`                 | printf-like format string for the attachment menu                           |
| `attach_keyword`                | Renamed to: `abort_noattach_regex`                                          |
| `attach_save_dir`               | Default directory where attachments are saved                               |
| `attach_save_without_prompting` | If true, then don't prompt to save                                          |
| `attach_sep`                    | Separator to add between saved/printed/piped attachments                    |
| `attach_split`                  | Save/print/pipe tagged messages individually                                |
| `attribution`                   | Renamed to: `attribution_intro`                                             |
| `attribution_intro`             | Message to start a reply, 'On DATE, PERSON wrote:'                          |
| `attribution_locale`            | Locale for dates in the `attribution` message                               |
| `attribution_trailer`           | Suffix message to add after reply text                                      |
| `autocrypt`                     | Enables the Autocrypt feature                                               |
| `autocrypt_acct_format`         | Format of the Autocrypt account menu                                        |
| `autocrypt_dir`                 | Location of Autocrypt files, including the GPG keyring and SQLite database  |
| `autocrypt_reply`               | Replying to an Autocrypt email automatically enables Autocrypt in the reply |
| `autoedit`                      | Renamed to: `auto_edit`                                                     |
| `auto_edit`                     | Skip the initial compose menu and edit the email                            |
| `auto_subscribe`                | Automatically check if the user is subscribed to a mailing list             |
| `auto_tag`                      | Automatically apply actions to all tagged messages                          |

## B

| Config Option                  | Description                                           |
| :----------------------------- | :---------------------------------------------------- |
| `beep`                         | Make a noise when an error occurs                     |
| `beep_new`                     | Make a noise when new mail arrives                    |
| `bounce`                       | Confirm before bouncing a message                     |
| `bounce_delivered`             | Add 'Delivered-To' to bounced messages                |
| `braille_friendly`             | Move the cursor to the beginning of the line          |
| `browser_abbreviate_mailboxes` | Abbreviate mailboxes using '~' and '=' in the browser |
| `browser_sort`                 | Sort method for the browser                           |
| `browser_sort_dirs_first`      | Group directories before files in the browser         |

## C

| Config Option                             | Description                                                                           |
| :---------------------------------------- | :------------------------------------------------------------------------------------ |
| `catchup_newsgroup`                       | Mark all articles as read when leaving a newsgroup                                    |
| `certificate_file`                        | File containing trusted certificates                                                  |
| `change_folder_next`                      | Suggest the next folder, rather than the first when using '<change-folder>'           |
| `charset`                                 | Default character set for displaying text on screen                                   |
| `check_mbox_size`                         | Use mailbox size as an indicator of new mail                                          |
| `check_new`                               | Check for new mail while the mailbox is open                                          |
| `collapse_all`                            | Collapse all threads when entering a folder                                           |
| `collapse_flagged`                        | Prevent the collapse of threads with flagged emails                                   |
| `collapse_unread`                         | Prevent the collapse of threads with unread emails                                    |
| `color_directcolor`                       | Use 24bit colors (aka truecolor aka directcolor)                                      |
| `compose_confirm_detach_first`            | Prevent the accidental deletion of the composed message                               |
| `compose_format`                          | printf-like format string for the Compose panel's status bar                          |
| `compose_preview_above_attachments`       | Show the message preview above the attachments list. By default it is shown below it. |
| `compose_preview_min_rows`                | Hide the preview if it has fewer than this number of rows                             |
| `compose_show_preview`                    | Display a preview of the message body in the Compose window                           |
| `compose_show_user_headers`               | Controls whether or not custom headers are shown in the compose envelope              |
| `config_charset`                          | Character set that the config files are in                                            |
| `confirmappend`                           | Renamed to: `confirm_append`                                                          |
| `confirmcreate`                           | Renamed to: `confirm_create`                                                          |
| `confirm_append`                          | Confirm before appending emails to a mailbox                                          |
| `confirm_create`                          | Confirm before creating a new mailbox                                                 |
| `confirm_empty_to`                        | Ask for a confirmation before sending an email with an empty To recipients list       |
| `connect_timeout`                         | Renamed to: `socket_timeout`                                                          |
| `content_type`                            | Default 'Content-Type' for newly composed messages                                    |
| `copy`                                    | Save outgoing emails to `$record`                                                     |
| `copy_decode_weed`                        | Controls whether to weed headers when copying or saving emails                        |
| `count_alternatives`                      | Recurse inside multipart/alternatives while counting attachments                      |
| `crypt_autoencrypt`                       | Renamed to: `crypt_auto_encrypt`                                                      |
| `crypt_autopgp`                           | Renamed to: `crypt_auto_pgp`                                                          |
| `crypt_autosign`                          | Renamed to: `crypt_auto_sign`                                                         |
| `crypt_autosmime`                         | Renamed to: `crypt_auto_smime`                                                        |
| `crypt_auto_encrypt`                      | Automatically PGP encrypt all outgoing mail                                           |
| `crypt_auto_pgp`                          | Allow automatic PGP functions                                                         |
| `crypt_auto_sign`                         | Automatically PGP sign all outgoing mail                                              |
| `crypt_auto_smime`                        | Allow automatic SMIME functions                                                       |
| `crypt_chars`                             | User-configurable crypto flags: signed, encrypted etc.                                |
| `crypt_confirmhook`                       | Renamed to: `crypt_confirm_hook`                                                      |
| `crypt_confirm_hook`                      | Prompt the user to confirm keys before use                                            |
| `crypt_encryption_info`                   | Add an informative block with details about the encryption                            |
| `crypt_opportunistic_encrypt`             | Enable encryption when the recipient's key is available                               |
| `crypt_opportunistic_encrypt_strong_keys` | Enable encryption only when strong a key is available                                 |
| `crypt_protected_headers_read`            | Display protected headers (Memory Hole) in the pager                                  |
| `crypt_protected_headers_save`            | Save the cleartext Subject with the headers                                           |
| `crypt_protected_headers_subject`         | Use this as the subject for encrypted emails                                          |
| `crypt_protected_headers_weed`            | Controls whether NeoMutt will weed protected header fields                            |
| `crypt_protected_headers_write`           | Generate protected header (Memory Hole) for signed and encrypted emails               |
| `crypt_replyencrypt`                      | Renamed to: `crypt_reply_encrypt`                                                     |
| `crypt_replysign`                         | Renamed to: `crypt_reply_sign`                                                        |
| `crypt_replysignencrypted`                | Renamed to: `crypt_reply_sign_encrypted`                                              |
| `crypt_reply_encrypt`                     | Encrypt replies to encrypted messages                                                 |
| `crypt_reply_sign`                        | Sign replies to signed messages                                                       |
| `crypt_reply_sign_encrypted`              | Sign replies to encrypted messages                                                    |
| `crypt_timestamp`                         | Add a timestamp to PGP or SMIME output to prevent spoofing                            |
| `crypt_use_gpgme`                         | Use GPGME crypto backend                                                              |
| `crypt_use_pka`                           | Use GPGME to use PKA (lookup PGP keys using DNS)                                      |
| `crypt_verify_sig`                        | Verify PGP or SMIME signatures                                                        |
| `cursor_overlay`                          | **Deprecated**                                                                        |

## D

| Config Option       | Description                                                                    |
| :------------------ | :----------------------------------------------------------------------------- |
| `date_format`       | strftime format string for the `%d` expando                                    |
| `debug_file`        | File to save debug logs                                                        |
| `debug_level`       | Logging level for debug logs                                                   |
| `default_hook`      | Pattern to use for hooks that only have a simple regex                         |
| `delete`            | Really delete messages, when the mailbox is closed                             |
| `delete_untag`      | Untag messages when they are marked for deletion                               |
| `devel_security`    | Devel feature: Security -- https://github.com/neomutt/neomutt/discussions/4251 |
| `digest_collapse`   | Hide the subparts of a multipart/digest                                        |
| `display_filter`    | External command to pre-process an email before display                        |
| `dsn_notify`        | Request notification for message delivery or delay                             |
| `dsn_return`        | What to send as a notification of message delivery or delay                    |
| `duplicate_threads` | Highlight messages with duplicated message IDs                                 |

## E

| Config Option             | Description                                                   |
| :------------------------ | :------------------------------------------------------------ |
| `editor`                  | External command to use as an email editor                    |
| `edit_hdrs`               | Renamed to: `edit_headers`                                    |
| `edit_headers`            | Let the user edit the email headers whilst editing an email   |
| `empty_subject`           | Subject to use when replying to an email with none            |
| `encode_from`             | Encode 'From ' as 'quote-printable' at the beginning of lines |
| `entropy_file`            | File/device containing random data to initialise SSL          |
| `envelope_from`           | Renamed to: `use_envelope_from`                               |
| `envelope_from_address`   | Manually set the sender for outgoing messages                 |
| `escape`                  | **Deprecated**                                                |
| `external_search_command` | External search command                                       |

## F

| Config Option                 | Description                                                                |
| :---------------------------- | :------------------------------------------------------------------------- |
| `fast_reply`                  | Don't prompt for the recipients and subject when replying/forwarding       |
| `fcc_attach`                  | Save sent message with all their attachments                               |
| `fcc_before_send`             | Save FCCs before sending the message                                       |
| `fcc_clear`                   | Save sent messages unencrypted and unsigned                                |
| `flag_chars`                  | User-configurable index flags: tagged, new, etc                            |
| `flag_safe`                   | Protect flagged messages from deletion                                     |
| `folder`                      | Base folder for a set of mailboxes                                         |
| `folder_format`               | printf-like format string for the browser's display of folders             |
| `followup_to`                 | Add the 'Mail-Followup-To' header is generated when sending mail           |
| `followup_to_poster`          | Reply to the poster if 'poster' is in the 'Followup-To' header             |
| `force_name`                  | Save outgoing mail in a folder of their name                               |
| `forward_attachments`         | Forward attachments when forwarding a message                              |
| `forward_attribution_intro`   | Prefix message for forwarded messages                                      |
| `forward_attribution_trailer` | Suffix message for forwarded messages                                      |
| `forward_decode`              | Decode the message when forwarding it                                      |
| `forward_decrypt`             | Decrypt the message when forwarding it                                     |
| `forward_edit`                | Automatically start the editor when forwarding a message                   |
| `forward_format`              | printf-like format string to control the subject when forwarding a message |
| `forward_quote`               | Automatically quote a forwarded message using `$indent_string`             |
| `forward_references`          | Set the 'In-Reply-To' and 'References' headers when forwarding a message   |
| `forw_decode`                 | Renamed to: `forward_decode`                                               |
| `forw_decrypt`                | Renamed to: `forward_decrypt`                                              |
| `forw_format`                 | Renamed to: `forward_format`                                               |
| `forw_quote`                  | Renamed to: `forward_quote`                                                |
| `from`                        | Default 'From' address to use, if isn't otherwise set                      |
| `from_chars`                  | User-configurable index flags: to address, cc address, etc                 |

## G

| Config Option        | Description                                                       |
| :------------------- | :---------------------------------------------------------------- |
| `gecos_mask`         | Regex for parsing GECOS field of /etc/passwd                      |
| `greeting`           | Greeting string added to the top of all messages                  |
| `group_index_format` | printf-like format string for the browser's display of newsgroups |

## H

| Config Option                  | Description                                                                |
| :----------------------------- | :------------------------------------------------------------------------- |
| `hdrs`                         | Add custom headers to outgoing mail                                        |
| `hdr_format`                   | Renamed to: `index_format`                                                 |
| `header`                       | Include the message headers in the reply email (Weed applies)              |
| `header_cache`                 | Directory/file for the header cache database                               |
| `header_cache_backend`         | Header cache backend to use                                                |
| `header_cache_compress`        | **Deprecated**                                                             |
| `header_cache_compress_level`  | Level of compression for method                                            |
| `header_cache_compress_method` | Enable generic hcache database compression                                 |
| `header_cache_pagesize`        | **Deprecated**                                                             |
| `header_color_partial`         | Only color the part of the header matching the regex                       |
| `help`                         | Display a help line with common key bindings                               |
| `hidden_host`                  | Don't use the hostname, just the domain, when generating the message id    |
| `hidden_tags`                  | List of tags that shouldn't be displayed on screen (comma-separated)       |
| `hide_limited`                 | Don't indicate hidden messages, in the thread tree                         |
| `hide_missing`                 | Don't indicate missing messages, in the thread tree                        |
| `hide_thread_subject`          | Hide subjects that are similar to that of the parent message               |
| `hide_top_limited`             | Don't indicate hidden top message, in the thread tree                      |
| `hide_top_missing`             | Don't indicate missing top message, in the thread tree                     |
| `history`                      | Number of history entries to keep in memory per category                   |
| `history_file`                 | File to save history in                                                    |
| `history_format`               | printf-like format string for the history menu                             |
| `history_remove_dups`          | Remove duplicate entries from the history                                  |
| `honor_disposition`            | Don't display MIME parts inline if they have a disposition of 'attachment' |
| `honor_followup_to`            | Honour the 'Mail-Followup-To' header when group replying                   |
| `hostname`                     | Fully-qualified domain name of this machine                                |

## I

| Config Option                | Description                                                               |
| :--------------------------- | :------------------------------------------------------------------------ |
| `idn_decode`                 | Decode international domain names                                         |
| `idn_encode`                 | Encode international domain names                                         |
| `ignore_linear_white_space`  | **Deprecated**                                                            |
| `ignore_list_reply_to`       | Ignore the 'Reply-To' header when using `<reply>` on a mailing list       |
| `imap_authenticators`        | List of allowed IMAP authentication methods (colon-separated)             |
| `imap_check_subscribed`      | When opening a mailbox, ask the server for a list of subscribed folders   |
| `imap_condstore`             | Enable the CONDSTORE extension                                            |
| `imap_deflate`               | Compress network traffic                                                  |
| `imap_delim_chars`           | Characters that denote separators in IMAP folders                         |
| `imap_fetch_chunk_size`      | Download headers in blocks of this size                                   |
| `imap_headers`               | Additional email headers to download when getting index                   |
| `imap_idle`                  | Use the IMAP IDLE extension to check for new mail                         |
| `imap_keepalive`             | Renamed to: `imap_keep_alive`                                             |
| `imap_keep_alive`            | Time to wait before polling an open IMAP connection                       |
| `imap_list_subscribed`       | When browsing a mailbox, only display subscribed folders                  |
| `imap_login`                 | Login name for the IMAP server (defaults to `$imap_user`)                 |
| `imap_oauth_refresh_command` | External command to generate OAUTH refresh token                          |
| `imap_pass`                  | Password for the IMAP server                                              |
| `imap_passive`               | Reuse an existing IMAP connection to check for new mail                   |
| `imap_peek`                  | Don't mark messages as read when fetching them from the server            |
| `imap_pipeline_depth`        | Number of IMAP commands that may be queued up                             |
| `imap_poll_timeout`          | Maximum time to wait for a server response                                |
| `imap_qresync`               | Enable the QRESYNC extension                                              |
| `imap_rfc5161`               | Use the IMAP ENABLE extension to select capabilities                      |
| `imap_send_id`               | Send ID command when logging in                                           |
| `imap_servernoise`           | Renamed to: `imap_server_noise`                                           |
| `imap_server_noise`          | Display server warnings as error messages                                 |
| `imap_user`                  | Username for the IMAP server                                              |
| `implicit_autoview`          | Renamed to: `implicit_auto_view`                                          |
| `implicit_auto_view`         | Display MIME attachments inline if a 'copiousoutput' mailcap entry exists |
| `include`                    | Include a copy of the email that's being replied to                       |
| `include_encrypted`          | Whether to include encrypted content when replying                        |
| `include_onlyfirst`          | Renamed to: `include_only_first`                                          |
| `include_only_first`         | Only include the first attachment when replying                           |
| `indent_str`                 | Renamed to: `indent_string`                                               |
| `indent_string`              | String used to indent 'reply' text                                        |
| `index_format`               | printf-like format string for the index menu (emails)                     |
| `inews`                      | External command to post news articles                                    |
| `ispell`                     | External command to perform spell-checking                                |

## K

| Config Option  | Description                                               |
| :------------- | :-------------------------------------------------------- |
| `keep_flagged` | Don't move flagged messages from `$spool_file` to `$mbox` |

## L

| Config Option       | Description                                                                           |
| :------------------ | :------------------------------------------------------------------------------------ |
| `local_date_header` | Convert the date in the Date header of sent emails into local timezone, UTC otherwise |

## M

| Config Option                 | Description                                                                                                  |
| :---------------------------- | :----------------------------------------------------------------------------------------------------------- |
| `mailbox_folder_format`       | printf-like format string for the browser's display of mailbox folders                                       |
| `mailcap_path`                | List of mailcap files (colon-separated)                                                                      |
| `mailcap_sanitize`            | Restrict the possible characters in mailcap expandos                                                         |
| `maildir_check_cur`           | Check both 'new' and 'cur' directories for new mail                                                          |
| `maildir_field_delimiter`     | Field delimiter to be used for maildir email files (default is colon, recommended alternative is semi-colon) |
| `maildir_header_cache_verify` | Check for maildir changes when opening mailbox                                                               |
| `maildir_trash`               | Use the maildir 'trashed' flag, rather than deleting                                                         |
| `mail_check`                  | Number of seconds before NeoMutt checks for new mail                                                         |
| `mail_check_recent`           | Notify the user about new mail since the last time the mailbox was opened                                    |
| `mail_check_stats`            | Periodically check for new mail                                                                              |
| `mail_check_stats_interval`   | How often to check for new mail                                                                              |
| `markers`                     | Display a '+' at the beginning of wrapped lines in the pager                                                 |
| `mark_macro_prefix`           | Prefix for macros using '<mark-message>'                                                                     |
| `mark_old`                    | Mark new emails as old when leaving the mailbox                                                              |
| `mask`                        | Only display files/dirs matching this regex in the browser                                                   |
| `mbox`                        | Folder that receives read emails (see Move)                                                                  |
| `mbox_type`                   | Default type for creating new mailboxes                                                                      |
| `menu_context`                | Number of lines of overlap when changing pages in the index                                                  |
| `menu_move_off`               | Allow the last menu item to move off the bottom of the screen                                                |
| `menu_scroll`                 | Scroll the menu/index by one line, rather than a page                                                        |
| `message_cachedir`            | Renamed to: `message_cache_dir`                                                                              |
| `message_cache_clean`         | Clean out obsolete entries from the message cache                                                            |
| `message_cache_dir`           | Directory for the message cache                                                                              |
| `message_format`              | printf-like format string for listing attached messages                                                      |
| `meta_key`                    | Interpret 'ALT-x' as 'ESC-x'                                                                                 |
| `metoo`                       | Renamed to: `me_too`                                                                                         |
| `me_too`                      | Remove the user's address from the list of recipients                                                        |
| `mh_purge`                    | Really delete files in MH mailboxes                                                                          |
| `mh_seq_flagged`              | MH sequence for flagged message                                                                              |
| `mh_seq_replied`              | MH sequence to tag replied messages                                                                          |
| `mh_seq_unseen`               | MH sequence for unseen messages                                                                              |
| `mime_forward`                | Forward a message as a 'message/RFC822' MIME part                                                            |
| `mime_forward_decode`         | Decode the forwarded message before attaching it                                                             |
| `mime_forward_rest`           | Forward all attachments, even if they can't be decoded                                                       |
| `mime_fwd`                    | Renamed to: `mime_forward`                                                                                   |
| `mime_subject`                | **Deprecated**                                                                                               |
| `mime_type_query_command`     | External command to determine the MIME type of an attachment                                                 |
| `mime_type_query_first`       | Run the `$mime_type_query_command` before the mime.types lookup                                              |
| `mixmaster`                   | **Deprecated**                                                                                               |
| `mix_entry_format`            | **Deprecated**                                                                                               |
| `move`                        | Move emails from `$spool_file` to `$mbox` when read                                                          |
| `msg_format`                  | Renamed to: `message_format`                                                                                 |

## N

| Config Option                      | Description                                                                 |
| :--------------------------------- | :-------------------------------------------------------------------------- |
| `narrow_tree`                      | Draw a narrower thread tree in the index                                    |
| `net_inc`                          | Update the progress bar after this many KB sent/received (0 to disable)     |
| `newsgroups_charset`               | Character set of newsgroups' descriptions                                   |
| `newsrc`                           | File containing list of subscribed newsgroups                               |
| `news_cache_dir`                   | Directory for cached news articles                                          |
| `news_server`                      | Url of the news server                                                      |
| `new_mail_command`                 | External command to run when new mail arrives                               |
| `nm_config_file`                   | Configuration file for notmuch. Use 'auto' to detect configuration.         |
| `nm_config_profile`                | Configuration profile for notmuch.                                          |
| `nm_db_limit`                      | Default limit for Notmuch queries                                           |
| `nm_default_uri`                   | Renamed to: `nm_default_url`                                                |
| `nm_default_url`                   | Path to the Notmuch database                                                |
| `nm_exclude_tags`                  | Exclude messages with these tags                                            |
| `nm_flagged_tag`                   | Tag to use for flagged messages                                             |
| `nm_open_timeout`                  | Database timeout                                                            |
| `nm_query_type`                    | Default query type: 'threads' or 'messages'                                 |
| `nm_query_window_current_position` | Position of current search window                                           |
| `nm_query_window_current_search`   | Current search parameters                                                   |
| `nm_query_window_duration`         | Time duration of the current search window                                  |
| `nm_query_window_enable`           | Enable query windows                                                        |
| `nm_query_window_or_terms`         | Additional notmuch search terms for messages to be shown regardless of date |
| `nm_query_window_timebase`         | Units for the time duration                                                 |
| `nm_record`                        | If the `$record` mailbox (sent mail) should be indexed                      |
| `nm_record_tags`                   | Tags to apply to the `$record` mailbox (sent mail)                          |
| `nm_replied_tag`                   | Tag to use for replied messages                                             |
| `nm_unread_tag`                    | Tag to use for unread messages                                              |
| `nntp_authenticators`              | Allowed authentication methods                                              |
| `nntp_context`                     | Maximum number of articles to list (0 for all articles)                     |
| `nntp_listgroup`                   | Check all articles when opening a newsgroup                                 |
| `nntp_load_description`            | Load descriptions for newsgroups when adding to the list                    |
| `nntp_pass`                        | Password for the news server                                                |
| `nntp_poll`                        | Interval between checks for new posts                                       |
| `nntp_user`                        | Username for the news server                                                |

## P

| Config Option                     | Description                                                            |
| :-------------------------------- | :--------------------------------------------------------------------- |
| `pager`                           | External command for viewing messages, or empty to use NeoMutt's       |
| `pager_context`                   | Number of lines of overlap when changing pages in the pager            |
| `pager_format`                    | printf-like format string for the pager's status bar                   |
| `pager_index_lines`               | Number of index lines to display above the pager                       |
| `pager_read_delay`                | Number of seconds to wait before marking a message read                |
| `pager_skip_quoted_context`       | Lines of context to show when skipping quoted text                     |
| `pager_stop`                      | Don't automatically open the next message when at the end of a message |
| `pattern_format`                  | printf-like format string for the pattern completion menu              |
| `pgp_autoencrypt`                 | Renamed to: `crypt_auto_encrypt`                                       |
| `pgp_autoinline`                  | Renamed to: `pgp_auto_inline`                                          |
| `pgp_autosign`                    | Renamed to: `crypt_auto_sign`                                          |
| `pgp_auto_decode`                 | Automatically decrypt PGP messages                                     |
| `pgp_auto_inline`                 | Use old-style inline PGP messages (not recommended)                    |
| `pgp_auto_traditional`            | Renamed to: `pgp_reply_inline`                                         |
| `pgp_check_exit`                  | Check the exit code of PGP subprocess                                  |
| `pgp_check_gpg_decrypt_status_fd` | File descriptor used for status info                                   |
| `pgp_clearsign_command`           | Renamed to: `pgp_clear_sign_command`                                   |
| `pgp_clear_sign_command`          | External command to inline-sign a message                              |
| `pgp_create_traditional`          | Renamed to: `pgp_auto_inline`                                          |
| `pgp_decode_command`              | External command to decode a PGP attachment                            |
| `pgp_decryption_okay`             | Text indicating a successful decryption                                |
| `pgp_decrypt_command`             | External command to decrypt a PGP message                              |
| `pgp_default_key`                 | Default key to use for PGP operations                                  |
| `pgp_encrypt_only_command`        | External command to encrypt, but not sign a message                    |
| `pgp_encrypt_self`                | **Deprecated**                                                         |
| `pgp_encrypt_sign_command`        | External command to encrypt and sign a message                         |
| `pgp_entry_format`                | printf-like format string for the PGP key selection menu               |
| `pgp_export_command`              | External command to export a public key from the user's keyring        |
| `pgp_getkeys_command`             | Renamed to: `pgp_get_keys_command`                                     |
| `pgp_get_keys_command`            | External command to download a key for an email address                |
| `pgp_good_sign`                   | Text indicating a good signature                                       |
| `pgp_ignore_subkeys`              | Only use the principal PGP key                                         |
| `pgp_import_command`              | External command to import a key into the user's keyring               |
| `pgp_key_sort`                    | Sort order for PGP keys                                                |
| `pgp_list_pubring_command`        | External command to list the public keys in a user's keyring           |
| `pgp_list_secring_command`        | External command to list the private keys in a user's keyring          |
| `pgp_long_ids`                    | Display long PGP key IDs to the user                                   |
| `pgp_mime_auto`                   | Prompt the user to use MIME if inline PGP fails                        |
| `pgp_replyencrypt`                | Renamed to: `crypt_reply_encrypt`                                      |
| `pgp_replyinline`                 | Renamed to: `pgp_reply_inline`                                         |
| `pgp_replysign`                   | Renamed to: `crypt_reply_sign`                                         |
| `pgp_replysignencrypted`          | Renamed to: `crypt_reply_sign_encrypted`                               |
| `pgp_reply_inline`                | Reply using old-style inline PGP messages (not recommended)            |
| `pgp_retainable_sigs`             | Create nested multipart/signed or encrypted messages                   |
| `pgp_self_encrypt`                | Encrypted messages will also be encrypted to `$pgp_default_key` too    |
| `pgp_self_encrypt_as`             | Renamed to: `pgp_default_key`                                          |
| `pgp_show_unusable`               | Show non-usable keys in the key selection                              |
| `pgp_sign_as`                     | Use this alternative key for signing messages                          |
| `pgp_sign_command`                | External command to create a detached PGP signature                    |
| `pgp_sort_keys`                   | Renamed to: `pgp_key_sort`                                             |
| `pgp_strict_enc`                  | Encode PGP signed messages with quoted-printable (don't unset)         |
| `pgp_timeout`                     | Time in seconds to cache a passphrase                                  |
| `pgp_use_gpg_agent`               | Use a PGP agent for caching passwords                                  |
| `pgp_verify_command`              | External command to verify PGP signatures                              |
| `pgp_verify_key_command`          | External command to verify key information                             |
| `pgp_verify_sig`                  | Renamed to: `crypt_verify_sig`                                         |
| `pipe_decode`                     | Decode the message when piping it                                      |
| `pipe_decode_weed`                | Control whether to weed headers when piping an email                   |
| `pipe_sep`                        | Separator to add between multiple piped messages                       |
| `pipe_split`                      | Run the pipe command on each message separately                        |
| `pop_authenticators`              | List of allowed authentication methods (colon-separated)               |
| `pop_auth_try_all`                | Try all available authentication methods                               |
| `pop_checkinterval`               | Renamed to: `pop_check_interval`                                       |
| `pop_check_interval`              | Interval between checks for new mail                                   |
| `pop_delete`                      | After downloading POP messages, delete them on the server              |
| `pop_host`                        | Url of the POP server                                                  |
| `pop_last`                        | Use the 'LAST' command to fetch new mail                               |
| `pop_oauth_refresh_command`       | External command to generate OAUTH refresh token                       |
| `pop_pass`                        | Password of the POP server                                             |
| `pop_reconnect`                   | Reconnect to the server is the connection is lost                      |
| `pop_user`                        | Username of the POP server                                             |
| `postpone`                        | Save messages to the `$postponed` folder                               |
| `postponed`                       | Folder to store postponed messages                                     |
| `postpone_encrypt`                | Self-encrypt postponed messages                                        |
| `postpone_encrypt_as`             | Fallback encryption key for postponed messages                         |
| `post_indent_str`                 | Renamed to: `post_indent_string`                                       |
| `post_indent_string`              | Renamed to: `attribution_trailer`                                      |
| `post_moderated`                  | Allow posting to moderated newsgroups                                  |
| `preconnect`                      | External command to run prior to opening a socket                      |
| `preferred_languages`             | List of Preferred Languages for multilingual MIME (comma-separated)    |
| `print`                           | Confirm before printing a message                                      |
| `print_cmd`                       | Renamed to: `print_command`                                            |
| `print_command`                   | External command to print a message                                    |
| `print_decode`                    | Decode message before printing it                                      |
| `print_decode_weed`               | Control whether to weed headers when printing an email                 |
| `print_split`                     | Print multiple messages separately                                     |
| `prompt_after`                    | Pause after running an external pager                                  |

## Q

| Config Option   | Description                                                 |
| :-------------- | :---------------------------------------------------------- |
| `query_command` | External command to query and external address book         |
| `query_format`  | printf-like format string for the query menu (address book) |
| `quit`          | Prompt before exiting NeoMutt                               |
| `quote_regex`   | Regex to match quoted text in a reply                       |
| `quote_regexp`  | Renamed to: `quote_regex`                                   |

## R

| Config Option               | Description                                                         |
| :-------------------------- | :------------------------------------------------------------------ |
| `read_inc`                  | Update the progress bar after this many records read (0 to disable) |
| `read_only`                 | Open folders in read-only mode                                      |
| `realname`                  | Renamed to: `real_name`                                             |
| `real_name`                 | Real name of the user                                               |
| `recall`                    | Recall postponed mesaages when asked to compose a message           |
| `record`                    | Folder to save 'sent' messages                                      |
| `reflow_space_quotes`       | Insert spaces into reply quotes for 'format=flowed' messages        |
| `reflow_text`               | Reformat paragraphs of 'format=flowed' text                         |
| `reflow_wrap`               | Maximum paragraph width for reformatting 'format=flowed' text       |
| `reply_regex`               | Regex to match message reply subjects like 're: '                   |
| `reply_regexp`              | Renamed to: `reply_regex`                                           |
| `reply_self`                | Really reply to yourself, when replying to your own email           |
| `reply_to`                  | Address to use as a 'Reply-To' header                               |
| `reply_with_xorig`          | Create 'From' header from 'X-Original-To' header                    |
| `resolve`                   | Move to the next email whenever a command modifies an email         |
| `resume_draft_files`        | Process draft files like postponed messages                         |
| `resume_edited_draft_files` | Resume editing previously saved draft files                         |
| `reverse_alias`             | Display the alias in the index, rather than the message's sender    |
| `reverse_name`              | Set the 'From' from the address the email was sent to               |
| `reverse_realname`          | Renamed to: `reverse_real_name`                                     |
| `reverse_real_name`         | Set the 'From' from the full 'To' address the email was sent to     |
| `rfc2047_parameters`        | Decode RFC2047-encoded MIME parameters                              |

## S

| Config Option                    | Description                                                                |
| :------------------------------- | :------------------------------------------------------------------------- |
| `save_address`                   | Use sender's full address as a default save folder                         |
| `save_empty`                     | Preserve empty mailboxes                                                   |
| `save_history`                   | Number of history entries to save per category                             |
| `save_name`                      | Save outgoing message to mailbox of recipient's name if it exists          |
| `save_unsubscribed`              | Save a list of unsubscribed newsgroups to the 'newsrc'                     |
| `score`                          | Use message scoring                                                        |
| `score_threshold_delete`         | Messages with a lower score will be automatically deleted                  |
| `score_threshold_flag`           | Messages with a greater score will be automatically flagged                |
| `score_threshold_read`           | Messages with a lower score will be automatically marked read              |
| `search_context`                 | Context to display around search matches                                   |
| `sendmail`                       | External command to send email                                             |
| `sendmail_wait`                  | Time to wait for sendmail to finish                                        |
| `send_charset`                   | Character sets for outgoing mail                                           |
| `shell`                          | External command to run subshells in                                       |
| `show_multipart_alternative`     | How to display 'multipart/alternative' MIME parts                          |
| `show_new_news`                  | Check for new newsgroups when entering the browser                         |
| `show_only_unread`               | Only show subscribed newsgroups with unread articles                       |
| `sidebar_component_depth`        | Strip leading path components from sidebar folders                         |
| `sidebar_delim_chars`            | Characters that separate nested folders                                    |
| `sidebar_divider_char`           | Character to draw between the sidebar and index                            |
| `sidebar_folder_indent`          | Indent nested folders                                                      |
| `sidebar_format`                 | printf-like format string for the sidebar panel                            |
| `sidebar_indent_string`          | Indent nested folders using this string                                    |
| `sidebar_new_mail_only`          | Only show folders with new/flagged mail                                    |
| `sidebar_next_new_wrap`          | Wrap around when searching for the next mailbox with new mail              |
| `sidebar_non_empty_mailbox_only` | Only show folders with a non-zero number of mail                           |
| `sidebar_on_right`               | Display the sidebar on the right                                           |
| `sidebar_short_path`             | Abbreviate the paths using the `$folder` variable                          |
| `sidebar_sort`                   | Method to sort the sidebar                                                 |
| `sidebar_sort_method`            | Renamed to: `sidebar_sort`                                                 |
| `sidebar_visible`                | Show the sidebar                                                           |
| `sidebar_width`                  | Width of the sidebar                                                       |
| `signature`                      | File containing a signature to append to all mail                          |
| `sig_dashes`                     | Insert `-- ` before the signature                                          |
| `sig_on_top`                     | Insert the signature before the quoted text                                |
| `simple_search`                  | Pattern to search for when search doesn't contain `~`s                     |
| `size_show_bytes`                | Show smaller sizes in bytes                                                |
| `size_show_fractions`            | Show size fractions with a single decimal place                            |
| `size_show_mb`                   | Show sizes in megabytes for sizes greater than 1 megabyte                  |
| `size_units_on_left`             | Show the units as a prefix to the size                                     |
| `skip_quoted_offset`             | Renamed to: `pager_skip_quoted_context`                                    |
| `sleep_time`                     | Time to pause after certain info messages                                  |
| `smart_wrap`                     | Wrap text at word boundaries                                               |
| `smileys`                        | Regex to match smileys to prevent mistakes when quoting text               |
| `smime_ask_cert_label`           | Prompt the user for a label for SMIME certificates                         |
| `smime_ca_location`              | File containing trusted certificates                                       |
| `smime_certificates`             | File containing user's public certificates                                 |
| `smime_decrypt_command`          | External command to decrypt an SMIME message                               |
| `smime_decrypt_use_default_key`  | Use the default key for decryption                                         |
| `smime_default_key`              | Default key for SMIME operations                                           |
| `smime_encrypt_command`          | External command to encrypt a message                                      |
| `smime_encrypt_self`             | **Deprecated**                                                             |
| `smime_encrypt_with`             | Algorithm for encryption                                                   |
| `smime_get_cert_command`         | External command to extract a certificate from a message                   |
| `smime_get_cert_email_command`   | External command to get a certificate for an email                         |
| `smime_get_signer_cert_command`  | External command to extract a certificate from an email                    |
| `smime_import_cert_command`      | External command to import a certificate                                   |
| `smime_is_default`               | Use SMIME rather than PGP by default                                       |
| `smime_keys`                     | File containing user's private certificates                                |
| `smime_pk7out_command`           | External command to extract a public certificate                           |
| `smime_self_encrypt`             | Encrypted messages will also be encrypt to `$smime_default_key` too        |
| `smime_self_encrypt_as`          | Renamed to: `smime_default_key`                                            |
| `smime_sign_as`                  | Use this alternative key for signing messages                              |
| `smime_sign_command`             | External command to sign a message                                         |
| `smime_sign_digest_alg`          | Digest algorithm                                                           |
| `smime_timeout`                  | Time in seconds to cache a passphrase                                      |
| `smime_verify_command`           | External command to verify a signed message                                |
| `smime_verify_opaque_command`    | External command to verify a signature                                     |
| `smtp_authenticators`            | List of allowed authentication methods (colon-separated)                   |
| `smtp_oauth_refresh_command`     | External command to generate OAUTH refresh token                           |
| `smtp_pass`                      | Password for the SMTP server                                               |
| `smtp_url`                       | Url of the SMTP server                                                     |
| `smtp_user`                      | Username for the SMTP server                                               |
| `socket_timeout`                 | Timeout for socket connect/read/write operations (-1 to wait indefinitely) |
| `sort`                           | Sort method for the index                                                  |
| `sort_alias`                     | Renamed to: `alias_sort`                                                   |
| `sort_aux`                       | Secondary sort method for the index                                        |
| `sort_browser`                   | Renamed to: `browser_sort`                                                 |
| `sort_re`                        | Whether `$reply_regex` must be matched when not `$strict_threads`          |
| `spam_separator`                 | Separator for multiple spam headers                                        |
| `spoolfile`                      | Renamed to: `spool_file`                                                   |
| `spool_file`                     | Inbox                                                                      |
| `ssl_ca_certificates_file`       | File containing trusted CA certificates                                    |
| `ssl_ciphers`                    | Ciphers to use when using SSL                                              |
| `ssl_client_cert`                | File containing client certificates                                        |
| `ssl_force_tls`                  | Require TLS encryption for all connections                                 |
| `ssl_min_dh_prime_bits`          | Minimum keysize for Diffie-Hellman key exchange                            |
| `ssl_starttls`                   | Use STARTTLS on servers advertising the capability                         |
| `ssl_usesystemcerts`             | Renamed to: `ssl_use_system_certs`                                         |
| `ssl_use_sslv2`                  | INSECURE: Use SSLv2 for authentication                                     |
| `ssl_use_sslv3`                  | INSECURE: Use SSLv3 for authentication                                     |
| `ssl_use_system_certs`           | Use CA certificates in the system-wide store                               |
| `ssl_use_tlsv1`                  | Use TLSv1 for authentication                                               |
| `ssl_use_tlsv1_1`                | Use TLSv1.1 for authentication                                             |
| `ssl_use_tlsv1_2`                | Use TLSv1.2 for authentication                                             |
| `ssl_use_tlsv1_3`                | Use TLSv1.3 for authentication                                             |
| `ssl_verify_dates`               | Verify the dates on the server certificate                                 |
| `ssl_verify_host`                | Verify the server's hostname against the certificate                       |
| `ssl_verify_partial_chains`      | Allow verification using partial certificate chains                        |
| `status_chars`                   | Indicator characters for the status bar                                    |
| `status_format`                  | printf-like format string for the index's status line                      |
| `status_on_top`                  | Display the status bar at the top                                          |
| `strict_threads`                 | Thread messages using 'In-Reply-To' and 'References' headers               |
| `suspend`                        | Allow the user to suspend NeoMutt using '^Z'                               |

## T

| Config Option               | Description                                                        |
| :-------------------------- | :----------------------------------------------------------------- |
| `text_flowed`               | Generate 'format=flowed' messages                                  |
| `thorough_search`           | Decode headers and messages before searching them                  |
| `thread_received`           | Sort threaded messages by their received date                      |
| `tilde`                     | Display '~' in the pager after the end of the email                |
| `timeout`                   | Time to wait for user input in menus                               |
| `time_inc`                  | Frequency of progress bar updates (milliseconds)                   |
| `tmpdir`                    | Renamed to: `tmp_dir`                                              |
| `tmp_dir`                   | Directory for temporary files                                      |
| `toggle_quoted_show_levels` | Number of quote levels to show with toggle-quoted                  |
| `to_chars`                  | Indicator characters for the 'To' field in the index               |
| `trash`                     | Folder to put deleted emails                                       |
| `ts_enabled`                | Allow NeoMutt to set the terminal status line and icon             |
| `ts_icon_format`            | printf-like format string for the terminal's icon title            |
| `ts_status_format`          | printf-like format string for the terminal's status (window title) |
| `tunnel`                    | Shell command to establish a tunnel                                |
| `tunnel_is_secure`          | Assume a tunneled connection is secure                             |

## U

| Config Option       | Description                                            |
| :------------------ | :----------------------------------------------------- |
| `uncollapse_jump`   | When opening a thread, jump to the next unread message |
| `uncollapse_new`    | Open collapsed threads when new mail arrives           |
| `user_agent`        | Add a 'User-Agent' header to outgoing mail             |
| `use_8bitmime`      | Renamed to: `use_8bit_mime`                            |
| `use_8bit_mime`     | Use 8-bit messages and ESMTP to send messages          |
| `use_domain`        | Qualify local addresses using this domain              |
| `use_envelope_from` | Set the envelope sender of the message                 |
| `use_from`          | Set the 'From' header for outgoing mail                |
| `use_ipv6`          | Lookup IPv6 addresses when making connections          |
| `use_threads`       | Whether to use threads for the index                   |

## V

| Config Option        | Description                                   |
| :------------------- | :-------------------------------------------- |
| `vfolder_format`     | **Deprecated**                                |
| `virtual_spoolfile`  | Renamed to: `virtual_spool_file`              |
| `virtual_spool_file` | Use the first virtual mailbox as a spool file |
| `visual`             | **Deprecated**                                |

## W

| Config Option  | Description                                                            |
| :------------- | :--------------------------------------------------------------------- |
| `wait_key`     | Prompt to press a key after running external commands                  |
| `weed`         | Filter headers when displaying/forwarding/printing/replying            |
| `wrap`         | Width to wrap text in the pager                                        |
| `wrap_headers` | Width to wrap headers in outgoing messages                             |
| `wrap_search`  | Wrap around when the search hits the end                               |
| `write_bcc`    | Write out the 'Bcc' field when preparing to send a mail                |
| `write_inc`    | Update the progress bar after this many records written (0 to disable) |

## X

| Config Option      | Description                                            |
|:------------------ |:------------------------------------------------------ |
| `xterm_icon`       | Renamed to: `ts_icon_format`                           |
| `xterm_set_titles` | Renamed to: `ts_enabled`                               |
| `xterm_title`      | Renamed to: `ts_status_format`                         |
| `x_comment_to`     | Add 'X-Comment-To' header that contains article author |

