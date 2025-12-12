# Compose Email Dialog

dlg_compose() MENU_COMPOSE - Compose Email Dialog

compose/dlg_compose.c:434:6: dlg_compose()
	menu_tagging_dispatcher()
	km_dokey(MENU_COMPOSE)
	km_dokey(MENU_GENERIC)
	compose_function_dispatcher()
	env_function_dispatcher()
	preview_function_dispatcher()
	menu_function_dispatcher()
	global_function_dispatcher()

MENU_COMPOSE - OpCompose
	"attach-file"                 OP_ATTACHMENT_ATTACH_FILE
	"attach-key"                  OP_ATTACHMENT_ATTACH_KEY
	"attach-message"              OP_ATTACHMENT_ATTACH_MESSAGE
	"attach-news-message"         OP_ATTACHMENT_ATTACH_NEWS_MESSAGE
	"autocrypt-menu"              OP_COMPOSE_AUTOCRYPT_MENU
	"copy-file"                   OP_ATTACHMENT_SAVE
	"detach-file"                 OP_ATTACHMENT_DETACH
	"display-toggle-weed"         OP_DISPLAY_HEADERS
	"edit-bcc"                    OP_ENVELOPE_EDIT_BCC
	"edit-cc"                     OP_ENVELOPE_EDIT_CC
	"edit-content-id"             OP_ATTACHMENT_EDIT_CONTENT_ID
	"edit-description"            OP_ATTACHMENT_EDIT_DESCRIPTION
	"edit-encoding"               OP_ATTACHMENT_EDIT_ENCODING
	"edit-fcc"                    OP_ENVELOPE_EDIT_FCC
	"edit-file"                   OP_COMPOSE_EDIT_FILE
	"edit-followup-to"            OP_ENVELOPE_EDIT_FOLLOWUP_TO
	"edit-from"                   OP_ENVELOPE_EDIT_FROM
	"edit-headers"                OP_ENVELOPE_EDIT_HEADERS
	"edit-language"               OP_ATTACHMENT_EDIT_LANGUAGE
	"edit-message"                OP_COMPOSE_EDIT_MESSAGE
	"edit-mime"                   OP_ATTACHMENT_EDIT_MIME
	"edit-newsgroups"             OP_ENVELOPE_EDIT_NEWSGROUPS
	"edit-reply-to"               OP_ENVELOPE_EDIT_REPLY_TO
	"edit-subject"                OP_ENVELOPE_EDIT_SUBJECT
	"edit-to"                     OP_ENVELOPE_EDIT_TO
	"edit-type"                   OP_ATTACHMENT_EDIT_TYPE
	"edit-x-comment-to"           OP_ENVELOPE_EDIT_X_COMMENT_TO
	"exit"                        OP_EXIT
	"filter-entry"                OP_ATTACHMENT_FILTER
	"forget-passphrase"           OP_FORGET_PASSPHRASE
	"get-attachment"              OP_ATTACHMENT_GET_ATTACHMENT
	"group-alternatives"          OP_ATTACHMENT_GROUP_ALTS
	"group-multilingual"          OP_ATTACHMENT_GROUP_LINGUAL
	"group-related"               OP_ATTACHMENT_GROUP_RELATED
	"ispell"                      OP_COMPOSE_ISPELL
	"move-down"                   OP_ATTACHMENT_MOVE_DOWN
	"move-up"                     OP_ATTACHMENT_MOVE_UP
	"new-mime"                    OP_ATTACHMENT_NEW_MIME
	"pgp-menu"                    OP_COMPOSE_PGP_MENU
	"pipe-entry"                  OP_PIPE
	"pipe-message"                OP_PIPE
	"postpone-message"            OP_COMPOSE_POSTPONE_MESSAGE
	"preview-page-down"           OP_PREVIEW_PAGE_DOWN
	"preview-page-up"             OP_PREVIEW_PAGE_UP
	"print-entry"                 OP_ATTACHMENT_PRINT
	"rename-attachment"           OP_ATTACHMENT_RENAME_ATTACHMENT
	"rename-file"                 OP_COMPOSE_RENAME_FILE
	"send-message"                OP_COMPOSE_SEND_MESSAGE
	"smime-menu"                  OP_COMPOSE_SMIME_MENU
	"toggle-disposition"          OP_ATTACHMENT_TOGGLE_DISPOSITION
	"toggle-recode"               OP_ATTACHMENT_TOGGLE_RECODE
	"toggle-unlink"               OP_ATTACHMENT_TOGGLE_UNLINK
	"ungroup-attachment"          OP_ATTACHMENT_UNGROUP
	"update-encoding"             OP_ATTACHMENT_UPDATE_ENCODING
	"view-attach"                 OP_ATTACHMENT_VIEW
	"view-mailcap"                OP_ATTACHMENT_VIEW_MAILCAP
	"view-pager"                  OP_ATTACHMENT_VIEW_PAGER
	"view-text"                   OP_ATTACHMENT_VIEW_TEXT
	"write-fcc"                   OP_COMPOSE_WRITE_MESSAGE

MENU_GENERIC - OpGeneric
	"bottom-page"                 OP_BOTTOM_PAGE
	"check-stats"                 OP_CHECK_STATS
	"current-bottom"              OP_CURRENT_BOTTOM
	"current-middle"              OP_CURRENT_MIDDLE
	"current-top"                 OP_CURRENT_TOP
	"end-cond"                    OP_END_COND
	"enter-command"               OP_ENTER_COMMAND
	"exit"                        OP_EXIT
	"first-entry"                 OP_FIRST_ENTRY
	"half-down"                   OP_HALF_DOWN
	"half-up"                     OP_HALF_UP
	"help"                        OP_HELP
	"jump"                        OP_JUMP
	"jump"                        OP_JUMP_1
	"jump"                        OP_JUMP_2
	"jump"                        OP_JUMP_3
	"jump"                        OP_JUMP_4
	"jump"                        OP_JUMP_5
	"jump"                        OP_JUMP_6
	"jump"                        OP_JUMP_7
	"jump"                        OP_JUMP_8
	"jump"                        OP_JUMP_9
	"last-entry"                  OP_LAST_ENTRY
	"middle-page"                 OP_MIDDLE_PAGE
	"next-entry"                  OP_NEXT_ENTRY
	"next-line"                   OP_NEXT_LINE
	"next-page"                   OP_NEXT_PAGE
	"previous-entry"              OP_PREV_ENTRY
	"previous-line"               OP_PREV_LINE
	"previous-page"               OP_PREV_PAGE
	"redraw-screen"               OP_REDRAW
	"search"                      OP_SEARCH
	"search-next"                 OP_SEARCH_NEXT
	"search-opposite"             OP_SEARCH_OPPOSITE
	"search-reverse"              OP_SEARCH_REVERSE
	"select-entry"                OP_GENERIC_SELECT_ENTRY
	"shell-escape"                OP_SHELL_ESCAPE
	"show-log-messages"           OP_SHOW_LOG_MESSAGES
	"show-version"                OP_VERSION
	"tag-entry"                   OP_TAG
	"tag-prefix"                  OP_TAG_PREFIX
	"tag-prefix-cond"             OP_TAG_PREFIX_COND
	"top-page"                    OP_TOP_PAGE
	"what-key"                    OP_WHAT_KEY

menu/tagging.c:228:17: menu_tagging_dispatcher()
	OP_ABORT                            menu_abort
	OP_END_COND                         op_end_cond
	OP_TAG                              op_tag
	OP_TAG_PREFIX                       op_tag_prefix
	OP_TAG_PREFIX_COND                  op_tag_prefix_cond
	OP_TIMEOUT                          menu_timeout

compose/functions.c:2139:21: compose_function_dispatcher - ComposeFunctions[]
	OP_ATTACHMENT_ATTACH_FILE           op_attachment_attach_file
	OP_ATTACHMENT_ATTACH_KEY            op_attachment_attach_key
	OP_ATTACHMENT_ATTACH_MESSAGE        op_attachment_attach_message
	OP_ATTACHMENT_ATTACH_NEWS_MESSAGE   op_attachment_attach_message
	OP_ATTACHMENT_DETACH                op_attachment_detach
	OP_ATTACHMENT_EDIT_CONTENT_ID       op_attachment_edit_content_id
	OP_ATTACHMENT_EDIT_DESCRIPTION      op_attachment_edit_description
	OP_ATTACHMENT_EDIT_ENCODING         op_attachment_edit_encoding
	OP_ATTACHMENT_EDIT_LANGUAGE         op_attachment_edit_language
	OP_ATTACHMENT_EDIT_MIME             op_attachment_edit_mime
	OP_ATTACHMENT_EDIT_TYPE             op_attachment_edit_type
	OP_ATTACHMENT_FILTER                op_attachment_filter
	OP_ATTACHMENT_GET_ATTACHMENT        op_attachment_get_attachment
	OP_ATTACHMENT_GROUP_ALTS            op_attachment_group_alts
	OP_ATTACHMENT_GROUP_LINGUAL         op_attachment_group_lingual
	OP_ATTACHMENT_GROUP_RELATED         op_attachment_group_related
	OP_ATTACHMENT_MOVE_DOWN             op_attachment_move_down
	OP_ATTACHMENT_MOVE_UP               op_attachment_move_up
	OP_ATTACHMENT_NEW_MIME              op_attachment_new_mime
	OP_ATTACHMENT_PRINT                 op_attachment_print
	OP_ATTACHMENT_RENAME_ATTACHMENT     op_attachment_rename_attachment
	OP_ATTACHMENT_SAVE                  op_attachment_save
	OP_ATTACHMENT_TOGGLE_DISPOSITION    op_attachment_toggle_disposition
	OP_ATTACHMENT_TOGGLE_RECODE         op_attachment_toggle_recode
	OP_ATTACHMENT_TOGGLE_UNLINK         op_attachment_toggle_unlink
	OP_ATTACHMENT_UNGROUP               op_attachment_ungroup
	OP_ATTACHMENT_UPDATE_ENCODING       op_attachment_update_encoding
	OP_ATTACHMENT_VIEW                  op_display_headers
	OP_ATTACHMENT_VIEW_MAILCAP          op_display_headers
	OP_ATTACHMENT_VIEW_PAGER            op_display_headers
	OP_ATTACHMENT_VIEW_TEXT             op_display_headers
	OP_COMPOSE_EDIT_FILE                op_compose_edit_file
	OP_COMPOSE_EDIT_MESSAGE             op_compose_edit_message
	OP_COMPOSE_ISPELL                   op_compose_ispell
	OP_COMPOSE_POSTPONE_MESSAGE         op_compose_postpone_message
	OP_COMPOSE_RENAME_FILE              op_compose_rename_file
	OP_COMPOSE_SEND_MESSAGE             op_compose_send_message
	OP_COMPOSE_WRITE_MESSAGE            op_compose_write_message
	OP_DISPLAY_HEADERS                  op_display_headers
	OP_ENVELOPE_EDIT_HEADERS            op_envelope_edit_headers
	OP_EXIT                             op_exit
	OP_FORGET_PASSPHRASE                op_forget_passphrase
	OP_PIPE                             op_attachment_filter

envelope/functions.c:528:17: env_function_dispatcher - EnvelopeFunctions[]
	OP_COMPOSE_AUTOCRYPT_MENU           op_compose_autocrypt_menu
	OP_COMPOSE_PGP_MENU                 op_compose_pgp_menu
	OP_COMPOSE_SMIME_MENU               op_compose_smime_menu
	OP_ENVELOPE_EDIT_BCC                op_envelope_edit_bcc
	OP_ENVELOPE_EDIT_CC                 op_envelope_edit_cc
	OP_ENVELOPE_EDIT_FCC                op_envelope_edit_fcc
	OP_ENVELOPE_EDIT_FOLLOWUP_TO        op_envelope_edit_followup_to
	OP_ENVELOPE_EDIT_FROM               op_envelope_edit_from
	OP_ENVELOPE_EDIT_NEWSGROUPS         op_envelope_edit_newsgroups
	OP_ENVELOPE_EDIT_REPLY_TO           op_envelope_edit_reply_to
	OP_ENVELOPE_EDIT_SUBJECT            op_envelope_edit_subject
	OP_ENVELOPE_EDIT_TO                 op_envelope_edit_to
	OP_ENVELOPE_EDIT_X_COMMENT_TO       op_envelope_edit_x_comment_to

compose/preview.c:406:21: preview_function_dispatcher - PreviewFunctions[]
	OP_PREVIEW_PAGE_DOWN                preview_page_down
	OP_PREVIEW_PAGE_UP                  preview_page_up

menu/functions.c:316:18: menu_function_dispatcher - MenuFunctions[]
	OP_BOTTOM_PAGE                      menu_movement
	OP_CURRENT_BOTTOM                   menu_movement
	OP_CURRENT_MIDDLE                   menu_movement
	OP_CURRENT_TOP                      menu_movement
	OP_FIRST_ENTRY                      menu_movement
	OP_HALF_DOWN                        menu_movement
	OP_HALF_UP                          menu_movement
	OP_HELP                             op_help
	OP_JUMP                             op_jump
	OP_JUMP_1                           op_jump
	OP_JUMP_2                           op_jump
	OP_JUMP_3                           op_jump
	OP_JUMP_4                           op_jump
	OP_JUMP_5                           op_jump
	OP_JUMP_6                           op_jump
	OP_JUMP_7                           op_jump
	OP_JUMP_8                           op_jump
	OP_JUMP_9                           op_jump
	OP_LAST_ENTRY                       menu_movement
	OP_MIDDLE_PAGE                      menu_movement
	OP_NEXT_ENTRY                       menu_movement
	OP_NEXT_LINE                        menu_movement
	OP_NEXT_PAGE                        menu_movement
	OP_PREV_ENTRY                       menu_movement
	OP_PREV_LINE                        menu_movement
	OP_PREV_PAGE                        menu_movement
	OP_SEARCH                           menu_search
	OP_SEARCH_NEXT                      menu_search
	OP_SEARCH_OPPOSITE                  menu_search
	OP_SEARCH_REVERSE                   menu_search
	OP_TOP_PAGE                         menu_movement

gui/global.c:178:20: global_function_dispatcher - GlobalFunctions[]
	OP_CHECK_STATS                      op_check_stats
	OP_ENTER_COMMAND                    op_enter_command
	OP_REDRAW                           op_redraw
	OP_SHELL_ESCAPE                     op_shell_escape
	OP_SHOW_LOG_MESSAGES                op_show_log_messages
	OP_VERSION                          op_version
	OP_WHAT_KEY                         op_what_key

