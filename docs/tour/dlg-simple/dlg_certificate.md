# Certificate Verification

dlg_certificate() MENU_DIALOG - Certificate Verification

conn/dlg_verifycert.c:225:6: dlg_certificate()
	km_dokey(MENU_DIALOG)
	km_dokey(MENU_GENERIC)

MENU_DIALOG - OpDialog
	"quit"                        OP_QUIT
	"exit"                        OP_EXIT

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

conn/dlg_verifycert.c:250:6: dlg_certificate()
	// Translated
	OP_NEXT_ENTRY     OP_NEXT_LINE
	OP_PREV_ENTRY     OP_PREV_LINE
	OP_CURRENT_TOP    OP_TOP_PAGE
	OP_CURRENT_BOTTOM OP_BOTTOM_PAGE
	OP_CURRENT_MIDDLE OP_MIDDLE_PAGE
	// Quit
	ABORT
	OP_QUIT
	// Menu options
	OP_MAX + 1
	OP_MAX + 2
	OP_MAX + 3
	OP_MAX + 4
	// Ignored
	OP_JUMP
	OP_JUMP_1
	OP_JUMP_2
	OP_JUMP_3
	OP_JUMP_4
	OP_JUMP_5
	OP_JUMP_6
	OP_JUMP_7
	OP_JUMP_8
	OP_JUMP_9
	// Ignored
	OP_SEARCH
	OP_SEARCH_NEXT
	OP_SEARCH_OPPOSITE
	OP_SEARCH_REVERSE

