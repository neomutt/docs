# Alias Query

dlg_query() MENU_QUERY - Alias Query

alias/dlg_query.c:365:6: dlg_query()
	menu_tagging_dispatcher()
	km_dokey(MENU_QUERY)
	km_dokey(MENU_GENERIC)
	alias_function_dispatcher()
	menu_function_dispatcher()
	global_function_dispatcher()

MENU_QUERY - OpQuery
	"create-alias"                OP_CREATE_ALIAS
	"exit"                        OP_EXIT
	"limit"                       OP_MAIN_LIMIT
	"mail"                        OP_MAIL
	"query"                       OP_QUERY
	"query-append"                OP_QUERY_APPEND
	"sort"                        OP_SORT
	"sort-reverse"                OP_SORT_REVERSE
	"tag-pattern"                 OP_MAIN_TAG_PATTERN
	"untag-pattern"               OP_MAIN_UNTAG_PATTERN

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

alias/functions.c:465:19: alias_function_dispatcher - AliasFunctions[]
	OP_CREATE_ALIAS                     op_create_alias
	OP_DELETE                           op_delete
	OP_EXIT                             op_exit
	OP_GENERIC_SELECT_ENTRY             op_generic_select_entry
	OP_MAIL                             op_generic_select_entry
	OP_MAIN_LIMIT                       op_main_limit
	OP_MAIN_TAG_PATTERN                 op_main_tag_pattern
	OP_MAIN_UNTAG_PATTERN               op_main_untag_pattern
	OP_QUERY                            op_query
	OP_QUERY_APPEND                     op_query
	OP_SEARCH                           op_search
	OP_SEARCH_NEXT                      op_search
	OP_SEARCH_OPPOSITE                  op_search
	OP_SEARCH_REVERSE                   op_search
	OP_SORT                             op_sort
	OP_SORT_REVERSE                     op_sort
	OP_UNDELETE                         op_delete

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

