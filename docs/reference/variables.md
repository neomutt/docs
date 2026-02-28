---
title: Configuration Variables
description: Complete alphabetical index of all NeoMutt configuration variables
keywords: neomutt, configuration, variables, settings, reference
---

# Configuration Variables

:::{admonition} Diátaxis: Reference
:class: note

Write as **austere description**. Be factual, precise, and complete. Use consistent formatting
throughout. Describe what things ARE, not how to use them. Use tables for structured data.
Mirror the structure of the software itself. Avoid instruction or explanation — link out to
how-to guides and explanation pages instead.
:::

NeoMutt has **474** configuration variables that control its behavior.
Each variable can be set in the `neomuttrc` configuration file or at the NeoMutt command line.
Variable names use underscores (e.g., `$smtp_pass`) in configuration;
the XML source uses hyphens (e.g., `smtp-pass`).

Variables are organized into groups by functional area.
Click the **Group** link to see full details including type, default value, and complete description.

| Variable | Description | Group |
| :------- | :---------- | :---- |
| `$abort_backspace` | If set, hitting backspace against an empty prompt aborts the prompt. | [General](variables/general) |
| `$abort_key` | Specifies the key that can be used to abort prompts. | [General](variables/general) |
| `$abort_noattach` | If set to yes, when composing messages containing the regular expression specified by $abort_noattach_regex and no at... | [General](variables/general) |
| `$abort_noattach_regex` | Specifies a regular expression to match against the body of the message, to determine if an attachment was mentioned ... | [General](variables/general) |
| `$abort_nosubject` | If set to yes, when composing messages and no subject is given at the subject prompt, composition will be aborted. | [General](variables/general) |
| `$abort_unmodified` | If set to yes, composition will automatically abort after editing the message body if no changes are made to the file... | [General](variables/general) |
| `$account_command` | If set, this command is used to retrieve account credentials. | [General](variables/general) |
| `$alias_file` | The default file in which to save aliases created by the <create-alias> function. | [Alias](variables/alias) |
| `$alias_format` | Specifies the format of the data displayed for the "alias" menu. | [Alias](variables/alias) |
| `$alias_sort` | Specifies how the entries in the "alias" and "query" menus are sorted. | [Alias](variables/alias) |
| `$allow_8bit` | Controls whether 8-bit data is converted to 7-bit using either Quoted- Printable or Base64 encoding when sending mail. | [General](variables/general) |
| `$allow_ansi` | Controls whether ANSI color codes in messages (and color tags in rich text messages) are to be interpreted. | [General](variables/general) |
| `$arrow_cursor` | When set, an arrow ("->") will be used to indicate the current entry in menus instead of highlighting the whole line. | [General](variables/general) |
| `$arrow_string` | Specifies the string of arrow_cursor when arrow_cursor enabled. | [General](variables/general) |
| `$ascii_chars` | If set, NeoMutt will use plain ASCII characters when displaying thread and attachment trees, instead of the default A... | [General](variables/general) |
| `$ask_bcc` | If set, NeoMutt will prompt you for blind-carbon-copy (Bcc) recipients before editing an outgoing message. | [General](variables/general) |
| `$ask_cc` | If set, NeoMutt will prompt you for carbon-copy (Cc) recipients before editing the body of an outgoing message. | [General](variables/general) |
| `$ask_followup_to` | If set, NeoMutt will prompt you for follow-up groups before editing the body of an outgoing message. | [General](variables/general) |
| `$ask_x_comment_to` | If set, NeoMutt will prompt you for x-comment-to field before editing the body of an outgoing message. | [General](variables/general) |
| `$assumed_charset` | This variable is a colon-separated list of character encoding schemes for messages without character encoding indicat... | [General](variables/general) |
| `$attach_charset` | This variable is a colon-separated list of character encoding schemes for text file attachments. | [Attachment](variables/attach) |
| `$attach_format` | This variable describes the format of the "attachment" menu. | [Attachment](variables/attach) |
| `$attach_save_dir` | The directory where attachments are saved. | [Attachment](variables/attach) |
| `$attach_save_without_prompting` | This variable, when set to true, will cause attachments to be saved to the 'attach_save_dir' location without prompti... | [Attachment](variables/attach) |
| `$attach_sep` | The separator to add between attachments when operating (saving, printing, piping, etc) on a list of tagged attachments. | [Attachment](variables/attach) |
| `$attach_split` | If this variable is unset, when operating (saving, printing, piping, etc) on a list of tagged attachments, NeoMutt wi... | [Attachment](variables/attach) |
| `$attribution_intro` | This is the string that will precede a replied-to message which is quoted in the main body of the reply (this is the ... | [General](variables/general) |
| `$attribution_locale` | The locale used by strftime(3) to format dates in the attribution strings. | [General](variables/general) |
| `$attribution_trailer` | Similar to the $attribution_intro variable, this is the string that will come after a replied-to message which is quo... | [General](variables/general) |
| `$auto_edit` | When set along with $edit_headers, NeoMutt will skip the initial send-menu (prompting for subject and recipients) and... | [General](variables/general) |
| `$auto_subscribe` | When set, NeoMutt assumes the presence of a List-Post header means the recipient is subscribed to the list. | [General](variables/general) |
| `$auto_tag` | When set, functions in the index menu which affect a message will be applied to all tagged messages (if there are any). | [General](variables/general) |
| `$autocrypt` | When set, enables autocrypt, which provides passive encryption protection with keys exchanged via headers. | [General](variables/general) |
| `$autocrypt_acct_format` | This variable describes the format of the "autocrypt account" menu. | [Autocrypt](variables/autocrypt) |
| `$autocrypt_dir` | This variable sets where autocrypt files are stored, including the GPG keyring and SQLite database. | [Autocrypt](variables/autocrypt) |
| `$autocrypt_reply` | When set, replying to an autocrypt email automatically enables autocrypt in the reply. | [Autocrypt](variables/autocrypt) |
| `$beep` | When this variable is set, NeoMutt will beep when an error occurs. | [General](variables/general) |
| `$beep_new` | When this variable is set, NeoMutt will beep whenever it prints a message notifying you of new mail. | [General](variables/general) |
| `$bounce` | Controls whether you will be asked to confirm bouncing messages. | [General](variables/general) |
| `$bounce_delivered` | When this variable is set, NeoMutt will include Delivered-To headers when bouncing messages. | [General](variables/general) |
| `$braille_friendly` | When this variable is set, NeoMutt will place the cursor at the beginning of the current line in menus, even when the... | [General](variables/general) |
| `$browser_abbreviate_mailboxes` | When this variable is set, NeoMutt will abbreviate mailbox names in the browser mailbox list, using '~' and '=' short... | [Browser](variables/browser) |
| `$browser_sort` | Specifies how to sort entries in the file browser. | [Browser](variables/browser) |
| `$browser_sort_dirs_first` | If this variable is set, the browser will group directories before files. | [Browser](variables/browser) |
| `$catchup_newsgroup` | If this variable is set, NeoMutt will mark all articles in newsgroup as read when you quit the newsgroup (catchup new... | [General](variables/general) |
| `$certificate_file` | This variable specifies the file where the certificates you trust are saved. | [General](variables/general) |
| `$change_folder_next` | When this variable is set, the <change-folder> function mailbox suggestion will start at the next folder in your "mai... | [General](variables/general) |
| `$charset` | Character set your terminal uses to display and enter textual data. | [General](variables/general) |
| `$check_mbox_size` | When this variable is set, NeoMutt will use file size attribute instead of access time when checking for new mail in ... | [General](variables/general) |
| `$check_new` | Note: this option only affects maildir and MH style mailboxes. | [General](variables/general) |
| `$collapse_all` | When set, NeoMutt will collapse all threads when entering a folder. | [General](variables/general) |
| `$collapse_flagged` | When unset, NeoMutt will not collapse a thread if it contains any flagged messages. | [General](variables/general) |
| `$collapse_unread` | When unset, NeoMutt will not collapse a thread if it contains any unread messages. | [General](variables/general) |
| `$color_directcolor` | When set, NeoMutt will use and allow 24-bit colours (aka truecolor aka directcolor). | [General](variables/general) |
| `$compose_confirm_detach_first` | When set, NeoMutt will prompt for confirmation when trying to use <detach-file> on the first entry in the compose menu. | [Compose](variables/compose) |
| `$compose_format` | Controls the format of the status line displayed in the "compose" menu. | [Compose](variables/compose) |
| `$compose_preview_above_attachments` | Show the message preview above the attachments list. | [Compose](variables/compose) |
| `$compose_preview_min_rows` | This variable specifies the minimum number of rows that have to be available for the message preview window to shown. | [Compose](variables/compose) |
| `$compose_show_preview` | When set, NeoMutt will display a preview of message in the compose view. | [Compose](variables/compose) |
| `$compose_show_user_headers` | When set, NeoMutt will display user-defined headers (set via my-header or from editing with edit-headers). | [Compose](variables/compose) |
| `$config_charset` | When defined, NeoMutt will recode commands in rc files from this encoding to the current character set as specified b... | [General](variables/general) |
| `$confirm_append` | When set, NeoMutt will prompt for confirmation when appending messages to an existing mailbox. | [General](variables/general) |
| `$confirm_create` | When set, NeoMutt will prompt for confirmation when saving messages to a mailbox which does not yet exist before crea... | [General](variables/general) |
| `$confirm_empty_to` | When set, NeoMutt will prompt for confirmation when sending an e-mail with an empty To recipients list. | [General](variables/general) |
| `$content_type` | Sets the default Content-Type for the body of newly composed messages. | [General](variables/general) |
| `$copy` | This variable controls whether or not copies of your outgoing messages will be saved for later references. | [General](variables/general) |
| `$copy_decode_weed` | Controls whether NeoMutt will weed headers when invoking the <decode-copy> or <decode-save> functions. | [General](variables/general) |
| `$count_alternatives` | When set, NeoMutt will recurse inside multipart/alternatives while performing attachment searching and counting(see a... | [General](variables/general) |
| `$crypt_auto_encrypt` | Setting this variable will cause NeoMutt to always attempt to PGP encrypt outgoing messages. | [Crypto](variables/crypto) |
| `$crypt_auto_pgp` | This variable controls whether or not NeoMutt may automatically enable PGP encryption/signing for messages. | [Crypto](variables/crypto) |
| `$crypt_auto_sign` | Setting this variable will cause NeoMutt to always attempt to cryptographically sign outgoing messages. | [Crypto](variables/crypto) |
| `$crypt_auto_smime` | This variable controls whether or not NeoMutt may automatically enable S/MIME encryption/signing for messages. | [Crypto](variables/crypto) |
| `$crypt_chars` | Controls the characters used in cryptography flags. | [Crypto](variables/crypto) |
| `$crypt_confirm_hook` | If set, then you will be prompted for confirmation of keys when using the crypt-hook command. | [Crypto](variables/crypto) |
| `$crypt_encryption_info` | If set, NeoMutt will include an informative block before an encrypted part, with details about the encryption. | [Crypto](variables/crypto) |
| `$crypt_opportunistic_encrypt` | Setting this variable will cause NeoMutt to automatically enable and disable encryption, based on whether all message... | [Crypto](variables/crypto) |
| `$crypt_opportunistic_encrypt_strong_keys` | When set, this modifies the behavior of $crypt_opportunistic_encrypt to only search for "strong keys", that is, keys ... | [Crypto](variables/crypto) |
| `$crypt_protected_headers_read` | When set, NeoMutt will display protected headers ("Memory Hole") in the pager, When set, NeoMutt will display protect... | [Crypto](variables/crypto) |
| `$crypt_protected_headers_save` | When $crypt_protected_headers_read is set, and a message with a protected Subject is opened, NeoMutt will save the up... | [Crypto](variables/crypto) |
| `$crypt_protected_headers_subject` | When $crypt_protected_headers_write is set, and the message is marked for encryption, this will be substituted into t... | [Crypto](variables/crypto) |
| `$crypt_protected_headers_weed` | Controls whether NeoMutt will weed protected header fields. | [Crypto](variables/crypto) |
| `$crypt_protected_headers_write` | When set, NeoMutt will generate protected headers for signed and encrypted emails. | [Crypto](variables/crypto) |
| `$crypt_reply_encrypt` | If set, automatically PGP or OpenSSL encrypt replies to messages which are encrypted. | [Crypto](variables/crypto) |
| `$crypt_reply_sign` | If set, automatically PGP or OpenSSL sign replies to messages which are signed. | [Crypto](variables/crypto) |
| `$crypt_reply_sign_encrypted` | If set, automatically PGP or OpenSSL sign replies to messages which are encrypted. | [Crypto](variables/crypto) |
| `$crypt_timestamp` | If set, NeoMutt will include a time stamp in the lines surrounding PGP or S/MIME output, so spoofing such lines is mo... | [Crypto](variables/crypto) |
| `$crypt_use_gpgme` | This variable controls the use of the GPGME-enabled crypto backends. | [Crypto](variables/crypto) |
| `$crypt_use_pka` | Controls whether NeoMutt uses PKA during signature verification (only supported by the GPGME backend). | [Crypto](variables/crypto) |
| `$crypt_verify_sig` | If "yes", always attempt to verify PGP or S/MIME signatures. | [Crypto](variables/crypto) |
| `$date_format` | Instead of using $date_format it is encouraged to use "%[fmt]" directly in the corresponding format strings, where "f... | [General](variables/general) |
| `$debug_file` | Debug logging is controlled by the variables $debug_file and $debug_level. | [General](variables/general) |
| `$debug_level` | Debug logging is controlled by the variables $debug_file and $debug_level. | [General](variables/general) |
| `$default_hook` | This variable controls how some hooks are interpreted if their pattern is a plain string or a regex. | [General](variables/general) |
| `$delete` | Controls whether or not messages are really deleted when closing or synchronizing a mailbox. | [General](variables/general) |
| `$delete_untag` | If this option is set, NeoMutt will untag messages when marking them for deletion. | [General](variables/general) |
| `$devel_security` | If this option is set, NeoMutt will enable the Security development features. | [General](variables/general) |
| `$digest_collapse` | If this option is set, NeoMutt's received-attachments menu will not show the subparts of individual messages in a mul... | [General](variables/general) |
| `$display_filter` | When set, specifies a command used to filter messages. | [General](variables/general) |
| `$dsn_notify` | This variable sets the request for when notification is returned. | [General](variables/general) |
| `$dsn_return` | This variable controls how much of your message is returned in DSN messages. | [General](variables/general) |
| `$duplicate_threads` | This variable controls whether NeoMutt, when $sort is set to threads, threads messages with the same Message-Id toget... | [General](variables/general) |
| `$edit_headers` | This option allows you to edit the header of your outgoing messages along with the body of your message. | [General](variables/general) |
| `$editor` | This variable specifies which editor is used by NeoMutt. | [General](variables/general) |
| `$empty_subject` | This variable specifies the subject to be used when replying to an email with an empty subject. | [General](variables/general) |
| `$encode_from` | When set, NeoMutt will quoted-printable encode messages when they contain the string "From " (note the trailing space... | [General](variables/general) |
| `$entropy_file` | The file which includes random data that is used to initialize SSL library functions. | [General](variables/general) |
| `$envelope_from_address` | Manually sets the envelope sender for outgoing messages. | [General](variables/general) |
| `$external_search_command` | If set, contains the name of the external program used by "~I" patterns. | [General](variables/general) |
| `$fast_reply` | When set, the initial prompt for recipients (to, cc, bcc) and subject are skipped when the relevant information is al... | [General](variables/general) |
| `$fcc_attach` | This variable controls whether or not attachments on outgoing messages are saved along with the main body of your mes... | [General](variables/general) |
| `$fcc_before_send` | When this variable is set, FCCs will occur before sending the message. | [General](variables/general) |
| `$fcc_clear` | When this variable is set, FCCs will be stored unencrypted and unsigned, even when the actual message is encrypted an... | [General](variables/general) |
| `$flag_chars` | Controls the characters used in several flags. | [General](variables/general) |
| `$flag_safe` | If set, flagged messages can't be deleted. | [General](variables/general) |
| `$folder` | Specifies the default location of your mailboxes. | [General](variables/general) |
| `$folder_format` | This variable allows you to customize the file browser display to your personal taste. | [General](variables/general) |
| `$followup_to` | Controls whether or not the "Mail-Followup-To:" header field is generated when sending mail. | [General](variables/general) |
| `$followup_to_poster` | If this variable is set and the keyword "poster" is present in Followup-To header, follow-up to newsgroup function is... | [General](variables/general) |
| `$force_name` | This variable is similar to $save_name, except that NeoMutt will store a copy of your outgoing message by the usernam... | [General](variables/general) |
| `$forward_attachments` | When forwarding inline (i.e. | [Forwarding](variables/forward) |
| `$forward_attribution_intro` | This is the string that will precede a message which has been forwarded in the main body of a message (when $mime_for... | [Forwarding](variables/forward) |
| `$forward_attribution_trailer` | This is the string that will follow a message which has been forwarded in the main body of a message (when $mime_forw... | [Forwarding](variables/forward) |
| `$forward_decode` | Controls the decoding of complex MIME messages into text/plain when forwarding a message. | [Forwarding](variables/forward) |
| `$forward_decrypt` | Controls the handling of encrypted messages when forwarding a message. | [Forwarding](variables/forward) |
| `$forward_edit` | This quadoption controls whether or not the user is automatically placed in the editor when forwarding messages. | [Forwarding](variables/forward) |
| `$forward_format` | This variable controls the default subject when forwarding a message. | [Forwarding](variables/forward) |
| `$forward_quote` | When set, forwarded messages included in the main body of the message (when $mime_forward is unset) will be quoted us... | [Forwarding](variables/forward) |
| `$forward_references` | When set, forwarded messages set the "In-Reply-To:" and "References:" headers in the same way as normal replies would. | [Forwarding](variables/forward) |
| `$from` | When set, this variable contains a default "from" address. | [General](variables/general) |
| `$from_chars` | Controls the character used to prefix the %F and %L fields in the index. | [General](variables/general) |
| `$gecos_mask` | A regular expression used by NeoMutt to parse the GECOS field of a password entry when expanding the alias. | [General](variables/general) |
| `$greeting` | When set, this is the string that will precede every message as a greeting phrase to the recipients. | [General](variables/general) |
| `$group_index_format` | This variable allows you to customize the newsgroup browser display to your personal taste. | [General](variables/general) |
| `$hdrs` | When unset, the header fields normally added by the "my-header" command are not created. | [General](variables/general) |
| `$header` | When set, this variable causes NeoMutt to include the header of the message you are replying to into the edit buffer. | [General](variables/general) |
| `$header_cache` | This variable points to the header cache database. | [Header Cache](variables/header) |
| `$header_cache_backend` | This variable specifies the header cache backend. | [Header Cache](variables/header) |
| `$header_cache_compress_level` | When NeoMutt is compiled with lz4, zstd or zlib, this option can be used to setup the compression level. | [Header Cache](variables/header) |
| `$header_cache_compress_method` | When NeoMutt is compiled with lz4, zstd or zlib, the header cache backend can use these compression methods for compr... | [Header Cache](variables/header) |
| `$header_color_partial` | When set, color header regexes behave like color body regexes: color is applied to the exact text matched by the regex. | [Header Cache](variables/header) |
| `$help` | When set, help lines describing the bindings for the major functions provided by each menu are displayed on the first... | [General](variables/general) |
| `$hidden_host` | When set, NeoMutt will skip the host name part of $hostname variable when adding the domain part to addresses. | [General](variables/general) |
| `$hidden_tags` | This variable specifies a list of comma-separated private notmuch/imap tags which should not be printed on screen. | [General](variables/general) |
| `$hide_limited` | When set, NeoMutt will not show the presence of messages that are hidden by limiting, in the thread tree. | [General](variables/general) |
| `$hide_missing` | When set, NeoMutt will not show the presence of missing messages in the thread tree. | [General](variables/general) |
| `$hide_thread_subject` | When set, NeoMutt will not show the subject of messages in the thread tree that have the same subject as their parent... | [General](variables/general) |
| `$hide_top_limited` | When set, NeoMutt will not show the presence of messages that are hidden by limiting, at the top of threads in the th... | [General](variables/general) |
| `$hide_top_missing` | When set, NeoMutt will not show the presence of missing messages at the top of threads in the thread tree. | [General](variables/general) |
| `$history` | This variable controls the size (in number of strings remembered) of the string history buffer per category. | [General](variables/general) |
| `$history_file` | The file in which NeoMutt will save its history. | [History](variables/history) |
| `$history_format` | Controls the format of the entries of the history list. | [History](variables/history) |
| `$history_remove_dups` | When set, all of the string history will be scanned for duplicates when a new entry is added. | [History](variables/history) |
| `$honor_disposition` | When set, NeoMutt will not display attachments with a disposition of "attachment" inline even if it could render the ... | [General](variables/general) |
| `$honor_followup_to` | This variable controls whether or not a Mail-Followup-To header is honored when group-replying to a message. | [General](variables/general) |
| `$hostname` | Specifies the fully-qualified hostname of the system NeoMutt is running on containing the host's name and the DNS dom... | [General](variables/general) |
| `$idn_decode` | When set, NeoMutt will show you international domain names decoded. | [General](variables/general) |
| `$idn_encode` | When set, NeoMutt will encode international domain names using IDN. | [General](variables/general) |
| `$ignore_list_reply_to` | Affects the behavior of the <reply> function when replying to messages from mailing lists (as defined by the "subscri... | [General](variables/general) |
| `$imap_authenticators` | This is a colon-separated list of authentication methods NeoMutt may attempt to use to log in to an IMAP server, in t... | [IMAP](variables/imap) |
| `$imap_check_subscribed` | When set, NeoMutt will fetch the set of subscribed folders from your server whenever a mailbox is selected, and add t... | [IMAP](variables/imap) |
| `$imap_condstore` | When set, NeoMutt will use the CONDSTORE extension (RFC7162) if advertised by the server. | [IMAP](variables/imap) |
| `$imap_deflate` | When set, NeoMutt will use the COMPRESS=DEFLATE extension (RFC4978) if advertised by the server. | [IMAP](variables/imap) |
| `$imap_delim_chars` | This contains the list of characters that NeoMutt will use as folder separators for IMAP paths, when no separator is ... | [IMAP](variables/imap) |
| `$imap_fetch_chunk_size` | When set to a value greater than 0, new headers will be downloaded in groups of this many headers per request. | [IMAP](variables/imap) |
| `$imap_headers` | NeoMutt requests these header fields in addition to the default headers ("Date:", "From:", "Sender:", "Subject:", "To... | [IMAP](variables/imap) |
| `$imap_idle` | When set, NeoMutt will attempt to use the IMAP IDLE extension to check for new mail in the current mailbox. | [IMAP](variables/imap) |
| `$imap_keep_alive` | This variable specifies the maximum amount of time in seconds that NeoMutt will wait before polling open IMAP connect... | [IMAP](variables/imap) |
| `$imap_list_subscribed` | This variable configures whether IMAP folder browsing will look for only subscribed folders or all folders. | [IMAP](variables/imap) |
| `$imap_login` | Your login name on the IMAP server. | [IMAP](variables/imap) |
| `$imap_oauth_refresh_command` | The command to run to generate an OAUTH refresh token for authorizing your connection to your IMAP server. | [IMAP](variables/imap) |
| `$imap_pass` | Specifies the password for your IMAP account. | [IMAP](variables/imap) |
| `$imap_passive` | When set, NeoMutt will not open new IMAP connections to check for new mail. | [IMAP](variables/imap) |
| `$imap_peek` | When set, NeoMutt will avoid implicitly marking your mail as read whenever you fetch a message from the server. | [IMAP](variables/imap) |
| `$imap_pipeline_depth` | Controls the number of IMAP commands that may be queued up before they are sent to the server. | [IMAP](variables/imap) |
| `$imap_poll_timeout` | This variable specifies the maximum amount of time in seconds that NeoMutt will wait for a response when polling IMAP... | [IMAP](variables/imap) |
| `$imap_qresync` | When set, NeoMutt will use the QRESYNC extension (RFC7162) if advertised by the server. | [IMAP](variables/imap) |
| `$imap_rfc5161` | When set, NeoMutt will use the IMAP ENABLE extension (RFC5161) to select CAPABILITIES. | [IMAP](variables/imap) |
| `$imap_send_id` | When set, NeoMutt will send an IMAP ID command (RFC2971) to the server when logging in if advertised by the server. | [IMAP](variables/imap) |
| `$imap_server_noise` | When set, NeoMutt will display warning messages from the IMAP server as error messages. | [IMAP](variables/imap) |
| `$imap_user` | The name of the user whose mail you intend to access on the IMAP server. | [IMAP](variables/imap) |
| `$implicit_auto_view` | If set to "yes", NeoMutt will look for a mailcap entry with the "copiousoutput" flag set for every MIME attachment it... | [General](variables/general) |
| `$include` | Controls whether or not a copy of the message(s) you are replying to is included in your reply. | [General](variables/general) |
| `$include_encrypted` | Controls whether or not NeoMutt includes separately encrypted attachment contents when replying. | [General](variables/general) |
| `$include_only_first` | Controls whether or not NeoMutt includes only the first attachment of the message you are replying. | [General](variables/general) |
| `$indent_string` | Specifies the string to prepend to each line of text quoted in a message to which you are replying. | [General](variables/general) |
| `$index_format` | This variable allows you to customize the message index display to your personal taste. | [General](variables/general) |
| `$inews_command` | If set, specifies the program and arguments used to deliver news posted by NeoMutt. | [General](variables/general) |
| `$ispell` | How to invoke ispell (GNU's spell-checking software). | [General](variables/general) |
| `$keep_flagged` | If set, read messages marked as flagged will not be moved from your spool mailbox to your $mbox mailbox or to the "mb... | [General](variables/general) |
| `$local_date_header` | If set, the date in the Date header of emails that you send will be in your local timezone. | [General](variables/general) |
| `$mail_check` | This variable configures how often (in seconds) NeoMutt should look for new mail. | [General](variables/general) |
| `$mail_check_recent` | When set, NeoMutt will only notify you about new mail that has been received since the last time you opened the mailbox. | [General](variables/general) |
| `$mail_check_stats` | When set, NeoMutt will periodically calculate message statistics of a mailbox while polling for new mail. | [General](variables/general) |
| `$mail_check_stats_interval` | When $mail_check_stats is set, this variable configures how often (in seconds) NeoMutt will update message counts. | [General](variables/general) |
| `$mailbox_folder_format` | This variable allows you to customize the file browser display to your personal taste. | [General](variables/general) |
| `$mailcap_path` | This variable specifies a list of colon-separated files to consult when attempting to display MIME bodies not directl... | [General](variables/general) |
| `$mailcap_sanitize` | If set, NeoMutt will restrict possible characters in mailcap % expandos to a well-defined set of safe characters. | [General](variables/general) |
| `$maildir_check_cur` | If set, NeoMutt will poll both the new and cur directories of a maildir folder for new messages. | [Maildir](variables/maildir) |
| `$maildir_field_delimiter` | Use the value as maildir field delimiter. | [Maildir](variables/maildir) |
| `$maildir_header_cache_verify` | Check for Maildir unaware programs other than NeoMutt having modified maildir files when the header cache is in use. | [Maildir](variables/maildir) |
| `$maildir_trash` | If set, messages marked as deleted will be saved with the maildir trashed flag instead of unlinked. | [Maildir](variables/maildir) |
| `$mark_macro_prefix` | Prefix for macros created using mark-message. | [General](variables/general) |
| `$mark_old` | Controls whether or not NeoMutt marks new unread messages as old if you exit a mailbox without reading them. | [General](variables/general) |
| `$markers` | Controls the display of wrapped lines in the internal pager. | [General](variables/general) |
| `$mask` | A regular expression used in the file browser, optionally preceded by the not operator "!". | [General](variables/general) |
| `$mbox` | This specifies the folder into which read mail in your $spool_file folder will be appended. | [General](variables/general) |
| `$mbox_type` | The default mailbox type used when creating new folders. | [General](variables/general) |
| `$me_too` | If unset, NeoMutt will remove your address (see the "alternates" command) from the list of recipients when replying t... | [General](variables/general) |
| `$menu_context` | This variable controls the number of lines of context that are given when scrolling through menus. | [General](variables/general) |
| `$menu_move_off` | When unset, the bottom entry of menus will never scroll up past the bottom of the screen, unless there are less entri... | [General](variables/general) |
| `$menu_scroll` | When set, menus will be scrolled up or down one line when you attempt to move across a screen boundary. | [General](variables/general) |
| `$message_cache_clean` | If set, NeoMutt will clean out obsolete entries from the message cache when the mailbox is synchronized. | [General](variables/general) |
| `$message_cache_dir` | Set this to a directory and NeoMutt will cache copies of messages from your IMAP and POP servers here. | [General](variables/general) |
| `$message_format` | This is the string displayed in the "attachment" menu for attachments of type message/rfc822. | [General](variables/general) |
| `$message_id_format` | This variable allows you to choose a custom format for the Message-Id when sending messages. | [General](variables/general) |
| `$meta_key` | If set, forces NeoMutt to interpret keystrokes with the high bit (bit 8) set as if the user had pressed the Esc key a... | [General](variables/general) |
| `$mh_purge` | When unset, NeoMutt will mimic mh's behavior and rename deleted messages to ,<old file name> in mh folders instead of... | [MH](variables/mh) |
| `$mh_seq_flagged` | The name of the MH sequence used for flagged messages. | [MH](variables/mh) |
| `$mh_seq_replied` | The name of the MH sequence used to tag replied messages. | [MH](variables/mh) |
| `$mh_seq_unseen` | The name of the MH sequence used for unseen messages. | [MH](variables/mh) |
| `$mime_forward` | When set, the message you are forwarding will be attached as a separate message/rfc822 MIME part instead of included ... | [MIME](variables/mime) |
| `$mime_forward_decode` | Controls the decoding of complex MIME messages into text/plain when forwarding a message while $mime_forward is set. | [MIME](variables/mime) |
| `$mime_forward_rest` | When forwarding multiple attachments of a MIME message from the attachment menu, attachments which can't be decoded i... | [MIME](variables/mime) |
| `$mime_type_query_command` | This specifies a command to run, to determine the mime type of a new attachment when composing a message. | [MIME](variables/mime) |
| `$mime_type_query_first` | When set, the $mime_type_query_command will be run before the mime.types lookup. | [MIME](variables/mime) |
| `$move` | If this variable is set, then NeoMutt will move read messages from your spool mailbox to your $mbox mailbox or to the... | [General](variables/general) |
| `$narrow_tree` | This variable, when set, makes the thread tree narrower, allowing deeper threads to fit on the screen. | [General](variables/general) |
| `$net_inc` | Operations that expect to transfer a large amount of data over the network will update their progress every $net_inc ... | [General](variables/general) |
| `$new_mail_command` | If set, NeoMutt will call this command after a new message is received. | [General](variables/general) |
| `$news_cache_dir` | This variable pointing to directory where NeoMutt will save cached news articles and headers in. | [General](variables/general) |
| `$news_server` | This variable specifies domain name or address of NNTP server. | [General](variables/general) |
| `$newsgroups_charset` | Character set of newsgroups descriptions. | [General](variables/general) |
| `$newsrc` | The file, containing info about subscribed newsgroups - names and indexes of read articles. | [General](variables/general) |
| `$nm_config_file` | Configuration file for notmuch. | [Notmuch](variables/notmuch) |
| `$nm_config_profile` | Configuration profile for notmuch. | [Notmuch](variables/notmuch) |
| `$nm_db_limit` | This variable specifies the default limit used in notmuch queries. | [Notmuch](variables/notmuch) |
| `$nm_default_url` | This variable specifies the default Notmuch database in format notmuch://<absolute path>. | [Notmuch](variables/notmuch) |
| `$nm_exclude_tags` | The messages tagged with these tags are excluded and not loaded from notmuch DB to NeoMutt unless specified explicitly. | [Notmuch](variables/notmuch) |
| `$nm_flagged_tag` | This variable specifies notmuch tag which is used for flagged messages. | [Notmuch](variables/notmuch) |
| `$nm_open_timeout` | This variable specifies the timeout for database open in seconds. | [Notmuch](variables/notmuch) |
| `$nm_query_type` | This variable specifies the default query type (threads or messages) used in notmuch queries. | [Notmuch](variables/notmuch) |
| `$nm_query_window_current_position` | This variable contains the position of the current search for window based vfolder. | [Notmuch](variables/notmuch) |
| `$nm_query_window_current_search` | This variable contains the currently setup notmuch search for window based vfolder. | [Notmuch](variables/notmuch) |
| `$nm_query_window_duration` | This variable sets the time duration of a windowed notmuch query. | [Notmuch](variables/notmuch) |
| `$nm_query_window_enable` | This variable enables windowed notmuch queries even if window duration is 0. | [Notmuch](variables/notmuch) |
| `$nm_query_window_or_terms` | This variable contains additional notmuch search terms for messages to be shown regardless of date. | [Notmuch](variables/notmuch) |
| `$nm_query_window_timebase` | This variable sets the time base of a windowed notmuch query. | [Notmuch](variables/notmuch) |
| `$nm_record` | This variable specifies whether, when writing a just-sent message to the $record, the message should also be added to... | [Notmuch](variables/notmuch) |
| `$nm_record_tags` | This variable specifies the notmuch tag modifications (addition, removal, toggling) applied to messages added to the ... | [Notmuch](variables/notmuch) |
| `$nm_replied_tag` | This variable specifies notmuch tag which is used for replied messages. | [Notmuch](variables/notmuch) |
| `$nm_unread_tag` | This variable specifies notmuch tag which is used for unread messages. | [Notmuch](variables/notmuch) |
| `$nntp_authenticators` | This is a colon-delimited list of authentication methods NeoMutt may attempt to use to log in to a news server, in th... | [NNTP](variables/nntp) |
| `$nntp_context` | This variable defines number of articles which will be in index when newsgroup entered. | [NNTP](variables/nntp) |
| `$nntp_listgroup` | This variable controls whether or not existence of each article is checked when newsgroup is entered. | [NNTP](variables/nntp) |
| `$nntp_load_description` | This variable controls whether or not descriptions for each newsgroup must be loaded when newsgroup is added to list ... | [NNTP](variables/nntp) |
| `$nntp_pass` | Your password for NNTP account. | [NNTP](variables/nntp) |
| `$nntp_poll` | The time in seconds until any operations on newsgroup except post new article will cause recheck for new news. | [NNTP](variables/nntp) |
| `$nntp_user` | Your login name on the NNTP server. | [NNTP](variables/nntp) |
| `$pager` | This variable specifies which pager you would like to use to view messages. | [General](variables/general) |
| `$pager_context` | This variable controls the number of lines of context that are given when displaying the next or previous page in the... | [Pager](variables/pager) |
| `$pager_format` | This variable controls the format of the one-line message "status" displayed before each message in either the intern... | [Pager](variables/pager) |
| `$pager_index_lines` | Determines the number of lines of a mini-index which is shown when in the pager. | [Pager](variables/pager) |
| `$pager_read_delay` | Determines the number of seconds that must elapse after first opening a new message in the pager before that message ... | [Pager](variables/pager) |
| `$pager_skip_quoted_context` | Determines the number of lines of context to show before the unquoted text when using the <skip-quoted> function. | [Pager](variables/pager) |
| `$pager_stop` | When set, the internal-pager will not move to the next message when you are at the end of a message and invoke the <n... | [Pager](variables/pager) |
| `$pattern_format` | This variable describes the format of the "pattern completion" menu. | [General](variables/general) |
| `$pgp_auto_decode` | If set, NeoMutt will automatically attempt to decrypt traditional PGP messages whenever the user performs an operatio... | [PGP](variables/pgp) |
| `$pgp_auto_inline` | This option controls whether NeoMutt generates old-style inline (traditional) PGP encrypted or signed messages under ... | [PGP](variables/pgp) |
| `$pgp_check_exit` | If set, NeoMutt will check the exit code of the PGP subprocess when signing or encrypting. | [PGP](variables/pgp) |
| `$pgp_check_gpg_decrypt_status_fd` | If set, NeoMutt will check the status file descriptor output of $pgp_decrypt_command and $pgp_decode_command for GnuP... | [PGP](variables/pgp) |
| `$pgp_clear_sign_command` | This format is used to create an old-style "clearsigned" PGP message. | [PGP](variables/pgp) |
| `$pgp_decode_command` | This format strings specifies a command which is used to decode application/pgp attachments. | [PGP](variables/pgp) |
| `$pgp_decrypt_command` | This command is used to decrypt a PGP encrypted message. | [PGP](variables/pgp) |
| `$pgp_decryption_okay` | If you assign text to this variable, then an encrypted PGP message is only considered successfully decrypted if the o... | [PGP](variables/pgp) |
| `$pgp_default_key` | This is the default key-pair to use for PGP operations. | [PGP](variables/pgp) |
| `$pgp_encrypt_only_command` | This command is used to encrypt a body part without signing it. | [PGP](variables/pgp) |
| `$pgp_encrypt_sign_command` | This command is used to both sign and encrypt a body part. | [PGP](variables/pgp) |
| `$pgp_entry_format` | This variable allows you to customize the PGP key selection menu to your personal taste. | [PGP](variables/pgp) |
| `$pgp_export_command` | This command is used to export a public key from the user's key ring. | [PGP](variables/pgp) |
| `$pgp_get_keys_command` | This command is invoked whenever NeoMutt needs to fetch the public key associated with an email address. | [PGP](variables/pgp) |
| `$pgp_good_sign` | If you assign a text to this variable, then a PGP signature is only considered verified if the output from $pgp_verif... | [PGP](variables/pgp) |
| `$pgp_ignore_subkeys` | Setting this variable will cause NeoMutt to ignore OpenPGP subkeys. | [PGP](variables/pgp) |
| `$pgp_import_command` | This command is used to import a key from a message into the user's public key ring. | [PGP](variables/pgp) |
| `$pgp_key_sort` | Specifies how the entries in the pgp menu are sorted. | [PGP](variables/pgp) |
| `$pgp_list_pubring_command` | This command is used to list the public key ring's contents. | [PGP](variables/pgp) |
| `$pgp_list_secring_command` | This command is used to list the secret key ring's contents. | [PGP](variables/pgp) |
| `$pgp_long_ids` | If set, use 64-bit PGP key IDs, if unset use the normal 32-bit key IDs. | [PGP](variables/pgp) |
| `$pgp_mime_auto` | This option controls whether NeoMutt will prompt you for automatically sending a (signed/encrypted) message using PGP... | [PGP](variables/pgp) |
| `$pgp_reply_inline` | Setting this variable will cause NeoMutt to always attempt to create an inline (traditional) message when replying to... | [PGP](variables/pgp) |
| `$pgp_retainable_sigs` | If set, signed and encrypted messages will consist of nested multipart/signed and multipart/encrypted body parts. | [PGP](variables/pgp) |
| `$pgp_self_encrypt` | When set, PGP encrypted messages will also be encrypted using the key in $pgp_default_key. | [PGP](variables/pgp) |
| `$pgp_show_unusable` | If set, NeoMutt will display non-usable keys on the PGP key selection menu. | [PGP](variables/pgp) |
| `$pgp_sign_as` | If you have a different key pair to use for signing, you should set this to the signing key. | [PGP](variables/pgp) |
| `$pgp_sign_command` | This command is used to create the detached PGP signature for a multipart/signed PGP/MIME body part. | [PGP](variables/pgp) |
| `$pgp_strict_enc` | If set, NeoMutt will automatically encode PGP/MIME signed messages as quoted-printable. | [PGP](variables/pgp) |
| `$pgp_timeout` | The number of seconds after which a cached passphrase will expire if not used. | [PGP](variables/pgp) |
| `$pgp_use_gpg_agent` | If set, NeoMutt expects a gpg-agent(1) process will handle private key passphrase prompts. | [PGP](variables/pgp) |
| `$pgp_verify_command` | This command is used to verify PGP signatures. | [PGP](variables/pgp) |
| `$pgp_verify_key_command` | This command is used to verify key information from the key selection menu. | [PGP](variables/pgp) |
| `$pipe_decode` | Used in connection with the <pipe-message> function. | [Piping](variables/pipe) |
| `$pipe_decode_weed` | For <pipe-message>, when $pipe_decode is set, this further controls whether NeoMutt will weed headers. | [Piping](variables/pipe) |
| `$pipe_sep` | The separator to add between messages when piping a list of tagged messages to an external Unix command. | [Piping](variables/pipe) |
| `$pipe_split` | Used in connection with the <pipe-message> function following <tag-prefix>. | [Piping](variables/pipe) |
| `$pop_auth_try_all` | If set, NeoMutt will try all available authentication methods. | [POP](variables/pop) |
| `$pop_authenticators` | This is a colon-separated list of authentication methods NeoMutt may attempt to use to log in to an POP server, in th... | [POP](variables/pop) |
| `$pop_check_interval` | This variable configures how often (in seconds) NeoMutt should look for new mail in the currently selected mailbox if... | [POP](variables/pop) |
| `$pop_delete` | If set, NeoMutt will delete successfully downloaded messages from the POP server when using the <fetch-mail> function. | [POP](variables/pop) |
| `$pop_host` | The name of your POP server for the <fetch-mail> function. | [POP](variables/pop) |
| `$pop_last` | If this variable is set, NeoMutt will try to use the "LAST" POP command for retrieving only unread messages from the ... | [POP](variables/pop) |
| `$pop_oauth_refresh_command` | The command to run to generate an OAUTH refresh token for authorizing your connection to your POP server. | [POP](variables/pop) |
| `$pop_pass` | Specifies the password for your POP account. | [POP](variables/pop) |
| `$pop_reconnect` | Controls whether or not NeoMutt will try to reconnect to the POP server if the connection is lost. | [POP](variables/pop) |
| `$pop_user` | Your login name on the POP server. | [POP](variables/pop) |
| `$post_moderated` | If set to yes, NeoMutt will post article to newsgroup that have not permissions to posting (e.g. | [General](variables/general) |
| `$postpone` | Controls whether or not messages are saved in the $postponed mailbox when you elect not to send immediately. | [General](variables/general) |
| `$postpone_encrypt` | When set, postponed messages that are marked for encryption will be self-encrypted. | [General](variables/general) |
| `$postpone_encrypt_as` | When set, NeoMutt will use this as a fallback encryption key for postponed messages. | [General](variables/general) |
| `$postponed` | NeoMutt allows you to indefinitely "postpone sending a message" which you are editing. | [General](variables/general) |
| `$preconnect` | If set, a shell command to be executed if NeoMutt fails to establish a connection to the server. | [General](variables/general) |
| `$preferred_languages` | This variable specifies a list of comma-separated languages. | [General](variables/general) |
| `$print` | Controls whether or not NeoMutt really prints messages. | [General](variables/general) |
| `$print_command` | This specifies the command pipe that should be used to print messages. | [Printing](variables/print) |
| `$print_decode` | Used in connection with the <print-message> function. | [Printing](variables/print) |
| `$print_decode_weed` | For <print-message>, when $print_decode is set, this further controls whether NeoMutt will weed headers. | [Printing](variables/print) |
| `$print_split` | Used in connection with the <print-message> function. | [Printing](variables/print) |
| `$prompt_after` | If you use an external $pager, setting this variable will cause NeoMutt to prompt you for a command when the pager ex... | [General](variables/general) |
| `$query_command` | This specifies the command NeoMutt will use to make external address queries. | [General](variables/general) |
| `$query_format` | This variable describes the format of the "query" menu. | [General](variables/general) |
| `$quit` | This variable controls whether "quit" and "exit" actually quit from NeoMutt. | [General](variables/general) |
| `$quote_regex` | A regular expression used in the internal pager to determine quoted sections of text in the body of a message. | [General](variables/general) |
| `$read_inc` | If set to a value greater than 0, NeoMutt will display which message it is currently on when reading a mailbox or whe... | [General](variables/general) |
| `$read_only` | If set, all folders are opened in read-only mode. | [General](variables/general) |
| `$real_name` | This variable specifies what "real" or "personal" name should be used when sending messages. | [General](variables/general) |
| `$recall` | Controls whether or not NeoMutt recalls postponed messages when composing a new message. | [General](variables/general) |
| `$record` | This specifies the file into which your outgoing messages should be appended. | [General](variables/general) |
| `$reflow_space_quotes` | This option controls how quotes from format=flowed messages are displayed in the pager and when replying (with $text_... | [General](variables/general) |
| `$reflow_text` | When set, NeoMutt will reformat paragraphs in text/plain parts marked format=flowed. | [General](variables/general) |
| `$reflow_wrap` | This variable controls the maximum paragraph width when reformatting text/plain parts when $reflow_text is set. | [General](variables/general) |
| `$reply_regex` | A regular expression used to recognize reply messages when threading and replying. | [General](variables/general) |
| `$reply_self` | If unset and you are replying to a message sent by you, NeoMutt will assume that you want to reply to the recipients ... | [General](variables/general) |
| `$reply_to` | If set, when replying to a message, NeoMutt will use the address listed in the Reply-to: header as the recipient of t... | [General](variables/general) |
| `$reply_with_xorig` | This variable provides a toggle. | [General](variables/general) |
| `$resolve` | When set, the cursor in a list will be automatically advanced to the next (possibly undeleted) message/attachment/ent... | [General](variables/general) |
| `$resume_draft_files` | If set, draft files (specified by -H on the command line) are processed similarly to when resuming a postponed message. | [General](variables/general) |
| `$resume_edited_draft_files` | If set, draft files previously edited (via -E -H on the command line) will have $resume_draft_files automatically set... | [General](variables/general) |
| `$reverse_alias` | This variable controls whether or not NeoMutt will display the "personal" name from your aliases in the index menu if... | [General](variables/general) |
| `$reverse_name` | It may sometimes arrive that you receive mail to a certain machine, move the messages to another machine, and reply t... | [General](variables/general) |
| `$reverse_real_name` | This variable fine-tunes the behavior of the $reverse_name feature. | [General](variables/general) |
| `$rfc2047_parameters` | When this variable is set, NeoMutt will decode RFC2047-encoded MIME parameters. | [General](variables/general) |
| `$save_address` | If set, NeoMutt will take the sender's full address when choosing a default folder for saving a mail. | [General](variables/general) |
| `$save_empty` | When unset, mailboxes which contain no saved messages will be removed when closed (the exception is $spool_file which... | [General](variables/general) |
| `$save_history` | This variable controls the size of the history (per category) saved in the $history_file file. | [General](variables/general) |
| `$save_name` | This variable controls how copies of outgoing messages are saved. | [General](variables/general) |
| `$save_unsubscribed` | When set, info about unsubscribed newsgroups will be saved into "newsrc" file and into cache. | [General](variables/general) |
| `$score` | When this variable is unset, scoring is turned off. | [General](variables/general) |
| `$score_threshold_delete` | Messages which have been assigned a score equal to or lower than the value of this variable are automatically marked ... | [Scoring](variables/score) |
| `$score_threshold_flag` | Messages which have been assigned a score greater than or equal to this variable's value are automatically marked "fl... | [Scoring](variables/score) |
| `$score_threshold_read` | Messages which have been assigned a score equal to or lower than the value of this variable are automatically marked ... | [Scoring](variables/score) |
| `$search_context` | For the pager, this variable specifies the number of lines shown before search results. | [General](variables/general) |
| `$send_charset` | A colon-delimited list of character sets for outgoing messages. | [General](variables/general) |
| `$sendmail` | Specifies the program and arguments used to deliver mail sent by NeoMutt. | [General](variables/general) |
| `$sendmail_wait` | Specifies the number of seconds to wait for the $sendmail process to finish before giving up and putting delivery in ... | [General](variables/general) |
| `$shell` | Command to use when spawning a subshell. | [General](variables/general) |
| `$show_multipart_alternative` | When set to info, the multipart/alternative information is shown. | [General](variables/general) |
| `$show_new_news` | If set, news server will be asked for new newsgroups on entering the browser. | [General](variables/general) |
| `$show_only_unread` | If set, only subscribed newsgroups that contain unread articles will be displayed in browser. | [General](variables/general) |
| `$sidebar_component_depth` | By default the sidebar will show the mailbox's path, relative to the $folder variable. | [Sidebar](variables/sidebar) |
| `$sidebar_delim_chars` | This contains the list of characters which you would like to treat as folder separators for displaying paths in the s... | [Sidebar](variables/sidebar) |
| `$sidebar_divider_char` | The default is a Unicode vertical line. | [Sidebar](variables/sidebar) |
| `$sidebar_folder_indent` | Set this to indent mailboxes in the sidebar. | [Sidebar](variables/sidebar) |
| `$sidebar_format` | This variable allows you to customize the sidebar display. | [Sidebar](variables/sidebar) |
| `$sidebar_indent_string` | This specifies the string that is used to indent mailboxes in the sidebar. | [Sidebar](variables/sidebar) |
| `$sidebar_new_mail_only` | When set, the sidebar will only display mailboxes containing new, or flagged, mail. | [Sidebar](variables/sidebar) |
| `$sidebar_next_new_wrap` | When set, the <sidebar-next-new> command will not stop at the end of the list of mailboxes, but wrap around to the be... | [Sidebar](variables/sidebar) |
| `$sidebar_non_empty_mailbox_only` | When set, the sidebar will only display mailboxes that contain one or more mails. | [Sidebar](variables/sidebar) |
| `$sidebar_on_right` | When set, the sidebar will appear on the right-hand side of the screen. | [Sidebar](variables/sidebar) |
| `$sidebar_short_path` | By default the sidebar will show the mailbox's path, relative to the $folder variable. | [Sidebar](variables/sidebar) |
| `$sidebar_sort` | Specifies how to sort mailbox entries in the sidebar. | [Sidebar](variables/sidebar) |
| `$sidebar_visible` | This specifies whether or not to show sidebar. | [Sidebar](variables/sidebar) |
| `$sidebar_width` | This controls the width of the sidebar. | [Sidebar](variables/sidebar) |
| `$sig_dashes` | If set, a line containing "-- " (note the trailing space) will be inserted before your $signature. | [General](variables/general) |
| `$sig_on_top` | If set, the signature will be included before any quoted or forwarded text. | [General](variables/general) |
| `$signature` | Specifies the filename of your signature, which is appended to all outgoing messages. | [General](variables/general) |
| `$simple_search` | Specifies how NeoMutt should expand a simple search into a real search pattern. | [General](variables/general) |
| `$size_show_bytes` | If set, message sizes will display bytes for values less than 1 kilobyte. | [General](variables/general) |
| `$size_show_fractions` | If set, message sizes will be displayed with a single decimal value for sizes from 0 to 10 kilobytes and 1 to 10 mega... | [General](variables/general) |
| `$size_show_mb` | If set, message sizes will display megabytes for values greater than or equal to 1 megabyte. | [General](variables/general) |
| `$size_units_on_left` | If set, message sizes units will be displayed to the left of the number. | [General](variables/general) |
| `$sleep_time` | Specifies time, in seconds, to pause while displaying certain informational messages, while moving from folder to fol... | [General](variables/general) |
| `$smart_wrap` | Controls the display of lines longer than the screen width in the internal pager. | [General](variables/general) |
| `$smileys` | The pager uses this variable to catch some common false positives of $quote_regex, most notably smileys and not consi... | [General](variables/general) |
| `$smime_ask_cert_label` | This flag controls whether you want to be asked to enter a label for a certificate about to be added to the database ... | [S/MIME](variables/smime) |
| `$smime_ca_location` | This variable contains the name of either a directory, or a file which contains trusted certificates for use with Ope... | [S/MIME](variables/smime) |
| `$smime_certificates` | Since for S/MIME there is no pubring/secring as with PGP, NeoMutt has to handle storage and retrieval of keys by itself. | [S/MIME](variables/smime) |
| `$smime_decrypt_command` | This format string specifies a command which is used to decrypt application/pkcs7-mime attachments. | [S/MIME](variables/smime) |
| `$smime_decrypt_use_default_key` | If set (default) this tells NeoMutt to use the default key for decryption. | [S/MIME](variables/smime) |
| `$smime_default_key` | This is the default key-pair to use for S/MIME operations, and must be set to the keyid (the hash-value that OpenSSL ... | [S/MIME](variables/smime) |
| `$smime_encrypt_command` | This command is used to create encrypted S/MIME messages. | [S/MIME](variables/smime) |
| `$smime_encrypt_with` | This sets the algorithm that should be used for encryption. | [S/MIME](variables/smime) |
| `$smime_get_cert_command` | This command is used to extract X509 certificates from a PKCS7 structure. | [S/MIME](variables/smime) |
| `$smime_get_cert_email_command` | This command is used to extract the mail address(es) used for storing X509 certificates, and for verification purpose... | [S/MIME](variables/smime) |
| `$smime_get_signer_cert_command` | This command is used to extract only the signers X509 certificate from a S/MIME signature, so that the certificate's ... | [S/MIME](variables/smime) |
| `$smime_import_cert_command` | This command is used to import a certificate via smime_keys. | [S/MIME](variables/smime) |
| `$smime_is_default` | The default behavior of NeoMutt is to use PGP on all auto-sign/encryption operations. | [S/MIME](variables/smime) |
| `$smime_keys` | Since for S/MIME there is no pubring/secring as with PGP, NeoMutt has to handle storage and retrieval of keys/certs b... | [S/MIME](variables/smime) |
| `$smime_pk7out_command` | This command is used to extract PKCS7 structures of S/MIME signatures, in order to extract the public X509 certificat... | [S/MIME](variables/smime) |
| `$smime_self_encrypt` | When set, S/MIME encrypted messages will also be encrypted using the certificate in $smime_default_key. | [S/MIME](variables/smime) |
| `$smime_sign_as` | If you have a separate key to use for signing, you should set this to the signing key. | [S/MIME](variables/smime) |
| `$smime_sign_command` | This command is used to created S/MIME signatures of type multipart/signed, which can be read by all mail clients. | [S/MIME](variables/smime) |
| `$smime_sign_digest_alg` | This sets the algorithm that should be used for the signature message digest. | [S/MIME](variables/smime) |
| `$smime_timeout` | The number of seconds after which a cached passphrase will expire if not used. | [S/MIME](variables/smime) |
| `$smime_verify_command` | This command is used to verify S/MIME signatures of type multipart/signed. | [S/MIME](variables/smime) |
| `$smime_verify_opaque_command` | This command is used to verify S/MIME signatures of type application/pkcs7-mime. | [S/MIME](variables/smime) |
| `$smtp_authenticators` | This is a colon-separated list of authentication methods NeoMutt may attempt to use to log in to an SMTP server, in t... | [SMTP](variables/smtp) |
| `$smtp_oauth_refresh_command` | The command to run to generate an OAUTH refresh token for authorizing your connection to your SMTP server. | [SMTP](variables/smtp) |
| `$smtp_pass` | Specifies the password for your SMTP account. | [SMTP](variables/smtp) |
| `$smtp_url` | Defines the SMTP smarthost where sent messages should relayed for delivery. | [SMTP](variables/smtp) |
| `$smtp_user` | The username for the SMTP server. | [SMTP](variables/smtp) |
| `$socket_timeout` | Causes NeoMutt to timeout any socket connect/read/write operation (for IMAP, POP or SMTP) after this many seconds. | [General](variables/general) |
| `$sort` | Specifies how to sort messages in the "index" menu. | [General](variables/general) |
| `$sort_aux` | This provides a secondary sort for messages in the "index" menu, used when the $sort value is equal for two messages. | [Sorting](variables/sort) |
| `$sort_re` | This variable is only useful when sorting by threads with $strict_threads unset. | [Sorting](variables/sort) |
| `$spam_separator` | This variable controls what happens when multiple spam headers are matched: if unset, each successive header will ove... | [General](variables/general) |
| `$spool_file` | If your spool mailbox is in a non-default place where NeoMutt can't find it, you can specify its location with this v... | [General](variables/general) |
| `$ssl_ca_certificates_file` | This variable specifies a file containing trusted CA certificates. | [SSL/TLS](variables/ssl) |
| `$ssl_ciphers` | Contains a colon-separated list of ciphers to use when using SSL. | [SSL/TLS](variables/ssl) |
| `$ssl_client_cert` | The file containing a client certificate and its associated private key. | [SSL/TLS](variables/ssl) |
| `$ssl_force_tls` | If this variable is set, NeoMutt will require that all connections to remote servers be encrypted. | [SSL/TLS](variables/ssl) |
| `$ssl_min_dh_prime_bits` | This variable specifies the minimum acceptable prime size (in bits) for use in any Diffie-Hellman key exchange. | [SSL/TLS](variables/ssl) |
| `$ssl_starttls` | If set (the default), NeoMutt will attempt to use STARTTLS on servers advertising the capability. | [SSL/TLS](variables/ssl) |
| `$ssl_use_system_certs` | If set to yes, NeoMutt will use CA certificates in the system-wide certificate store when checking if a server certif... | [SSL/TLS](variables/ssl) |
| `$ssl_use_tlsv1_2` | If set , NeoMutt will use TLSv1.2 when communicating with servers that request it. | [SSL/TLS](variables/ssl) |
| `$ssl_use_tlsv1_3` | If set , NeoMutt will use TLSv1.3 when communicating with servers that request it. | [SSL/TLS](variables/ssl) |
| `$ssl_verify_dates` | If set (the default), NeoMutt will not automatically accept a server certificate that is either not yet valid or alre... | [SSL/TLS](variables/ssl) |
| `$ssl_verify_host` | If set (the default), NeoMutt will not automatically accept a server certificate whose host name does not match the h... | [SSL/TLS](variables/ssl) |
| `$ssl_verify_partial_chains` | This option should not be changed from the default unless you understand what you are doing. | [SSL/TLS](variables/ssl) |
| `$status_chars` | Controls the characters used by the "%r" indicator in $status_format. | [Status Bar](variables/status) |
| `$status_format` | Controls the format of the status line displayed in the "index" menu. | [Status Bar](variables/status) |
| `$status_on_top` | Setting this variable causes the "status bar" to be displayed on the first line of the screen rather than near the bo... | [Status Bar](variables/status) |
| `$strict_threads` | If set, threading will only make use of the "In-Reply-To" and "References:" fields when you $sort by message threads. | [General](variables/general) |
| `$suspend` | When unset, NeoMutt won't stop when the user presses the terminal's susp key, usually "^Z". | [General](variables/general) |
| `$text_flowed` | When set, NeoMutt will generate "format=flowed" bodies with a content type of "text/plain; format=flowed". | [General](variables/general) |
| `$thorough_search` | Affects the ~b, ~B, and ~h search operations described in section "patterns". | [General](variables/general) |
| `$thread_received` | If $strict_threads is unset, then messages may also be grouped by subject. | [General](variables/general) |
| `$tilde` | When set, the internal-pager will pad blank lines to the bottom of the screen with a tilde ("~"). | [General](variables/general) |
| `$time_inc` | Along with $read_inc, $write_inc, and $net_inc, this variable controls the frequency with which progress updates are ... | [General](variables/general) |
| `$timeout` | This variable sets the time interval in seconds in which timeout-hook commands get executed while waiting for user in... | [General](variables/general) |
| `$tmp_dir` | This variable allows you to specify where NeoMutt will place its temporary files needed for displaying and composing ... | [General](variables/general) |
| `$to_chars` | Controls the character used to indicate mail addressed to you. | [General](variables/general) |
| `$toggle_quoted_show_levels` | Quoted text may be filtered out using the <toggle-quoted> command. | [General](variables/general) |
| `$trash` | If set, this variable specifies the path of the trash folder where the mails marked for deletion will be moved, inste... | [General](variables/general) |
| `$ts_enabled` | Controls whether NeoMutt tries to set the terminal status line and icon name. | [General](variables/general) |
| `$ts_icon_format` | Controls the format of the icon title, as long as "$ts_enabled" is set. | [General](variables/general) |
| `$ts_status_format` | Controls the format of the terminal status line (or window title), provided that "$ts_enabled" has been set. | [General](variables/general) |
| `$tunnel` | Setting this variable will cause NeoMutt to open a pipe to a command instead of a raw socket. | [General](variables/general) |
| `$tunnel_is_secure` | When set, NeoMutt will assume the $tunnel connection does not need STARTTLS to be enabled. | [General](variables/general) |
| `$uncollapse_jump` | When set, NeoMutt will jump to the next unread message, if any, when the current thread is uncollapsed. | [General](variables/general) |
| `$uncollapse_new` | When set, NeoMutt will automatically uncollapse any collapsed thread that receives a newly delivered message. | [General](variables/general) |
| `$use_8bit_mime` | Warning: do not set this variable unless you are using a version of sendmail which supports the -B8BITMIME flag (such... | [General](variables/general) |
| `$use_domain` | When set, NeoMutt will qualify all local addresses (ones without the "@host" portion) with the value of $hostname. | [General](variables/general) |
| `$use_envelope_from` | When set, NeoMutt will set the envelope sender of the message. | [General](variables/general) |
| `$use_from` | When set, NeoMutt will generate the "From:" header field when sending messages. | [General](variables/general) |
| `$use_ipv6` | When set, NeoMutt will look for IPv6 addresses of hosts it tries to contact. | [General](variables/general) |
| `$use_threads` | The style of threading used in the index. | [General](variables/general) |
| `$user_agent` | When set, NeoMutt will add a "User-Agent:" header to outgoing messages, indicating which version of NeoMutt was used ... | [General](variables/general) |
| `$virtual_spool_file` | When set, NeoMutt will use the first Notmuch virtual mailbox as a spool file. | [General](variables/general) |
| `$wait_key` | Controls whether NeoMutt will ask you to press a key after an external command has been invoked by these functions: <... | [General](variables/general) |
| `$weed` | When set, NeoMutt will weed headers when displaying, forwarding, or replying to messages. | [General](variables/general) |
| `$wrap` | When set to a positive value, NeoMutt will wrap text at $wrap characters. | [General](variables/general) |
| `$wrap_headers` | This option specifies the number of characters to use for wrapping an outgoing message's headers. | [General](variables/general) |
| `$wrap_search` | Controls whether searches wrap around the end. | [General](variables/general) |
| `$write_bcc` | Controls whether NeoMutt writes out the "Bcc:" header when preparing messages to be sent. | [General](variables/general) |
| `$write_inc` | When writing a mailbox, a message will be printed every $write_inc messages to indicate progress. | [General](variables/general) |
| `$x_comment_to` | If set, NeoMutt will add "X-Comment-To:" field (that contains full name of original article author) to article that f... | [General](variables/general) |

