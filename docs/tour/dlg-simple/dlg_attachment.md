# Attachment View

dlg_attachment() MENU_ATTACHMENT - Attachment View

attach/dlg_attach.c:248:6: dlg_attachment()
	menu_tagging_dispatcher()
	km_dokey(MENU_ATTACHMENT)
	km_dokey(MENU_GENERIC)
	attach_function_dispatcher()
	menu_function_dispatcher()
	global_function_dispatcher()

MENU_ATTACHMENT - OpAttachment
	"bounce-message"              OP_BOUNCE_MESSAGE
	"check-traditional-pgp"       OP_CHECK_TRADITIONAL
	"collapse-parts"              OP_ATTACHMENT_COLLAPSE
	"compose-to-sender"           OP_COMPOSE_TO_SENDER
	"delete-entry"                OP_ATTACHMENT_DELETE
	"display-toggle-weed"         OP_DISPLAY_HEADERS
	"edit-type"                   OP_ATTACHMENT_EDIT_TYPE
	"exit"                        OP_EXIT
	"extract-keys"                OP_EXTRACT_KEYS
	"followup-message"            OP_FOLLOWUP
	"forget-passphrase"           OP_FORGET_PASSPHRASE
	"forward-message"             OP_FORWARD_MESSAGE
	"forward-to-group"            OP_FORWARD_TO_GROUP
	"group-chat-reply"            OP_GROUP_CHAT_REPLY
	"group-reply"                 OP_GROUP_REPLY
	"list-reply"                  OP_LIST_REPLY
	"list-subscribe"              OP_LIST_SUBSCRIBE
	"list-unsubscribe"            OP_LIST_UNSUBSCRIBE
	"pipe-entry"                  OP_PIPE
	"pipe-message"                OP_PIPE
	"print-entry"                 OP_ATTACHMENT_PRINT
	"reply"                       OP_REPLY
	"resend-message"              OP_RESEND
	"save-entry"                  OP_ATTACHMENT_SAVE
	"undelete-entry"              OP_ATTACHMENT_UNDELETE
	"view-attach"                 OP_ATTACHMENT_VIEW
	"view-mailcap"                OP_ATTACHMENT_VIEW_MAILCAP
	"view-pager"                  OP_ATTACHMENT_VIEW_PAGER
	"view-text"                   OP_ATTACHMENT_VIEW_TEXT

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

attach/functions.c:709:20: attach_function_dispatcher - AttachFunctions[]
	OP_ATTACHMENT_COLLAPSE              op_attachment_collapse
	OP_ATTACHMENT_DELETE                op_attachment_delete
	OP_ATTACHMENT_EDIT_TYPE             op_attachment_edit_type
	OP_ATTACHMENT_PRINT                 op_attachment_print
	OP_ATTACHMENT_SAVE                  op_attachment_save
	OP_ATTACHMENT_UNDELETE              op_attachment_undelete
	OP_ATTACHMENT_VIEW                  op_attachment_view
	OP_ATTACHMENT_VIEW_MAILCAP          op_attachment_view_mailcap
	OP_ATTACHMENT_VIEW_PAGER            op_attachment_view_pager
	OP_ATTACHMENT_VIEW_TEXT             op_attachment_view_text
	OP_BOUNCE_MESSAGE                   op_bounce_message
	OP_CHECK_TRADITIONAL                op_check_traditional
	OP_COMPOSE_TO_SENDER                op_compose_to_sender
	OP_DISPLAY_HEADERS                  op_attachment_view
	OP_EXIT                             op_exit
	OP_EXTRACT_KEYS                     op_extract_keys
	OP_FOLLOWUP                         op_followup
	OP_FORGET_PASSPHRASE                op_forget_passphrase
	OP_FORWARD_MESSAGE                  op_forward_message
	OP_FORWARD_TO_GROUP                 op_forward_to_group
	OP_GROUP_CHAT_REPLY                 op_reply
	OP_GROUP_REPLY                      op_reply
	OP_LIST_REPLY                       op_reply
	OP_LIST_SUBSCRIBE                   op_list_subscribe
	OP_LIST_UNSUBSCRIBE                 op_list_unsubscribe
	OP_PIPE                             op_attachment_pipe
	OP_REPLY                            op_reply
	OP_RESEND                           op_resend

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

