# Ask the user for a string

mw_get_field() MENU_EDITOR - Ask the user for a string

editor/window.c:273:5: mw_get_field()
	km_dokey_event(MENU_EDITOR)
	enter_function_dispatcher()

MENU_EDITOR - OpEditor
	"backspace"       OP_EDITOR_BACKSPACE
	"backward-char"   OP_EDITOR_BACKWARD_CHAR
	"backward-word"   OP_EDITOR_BACKWARD_WORD
	"bol"             OP_EDITOR_BOL
	"capitalize-word" OP_EDITOR_CAPITALIZE_WORD
	"complete"        OP_EDITOR_COMPLETE
	"complete-query"  OP_EDITOR_COMPLETE_QUERY
	"delete-char"     OP_EDITOR_DELETE_CHAR
	"downcase-word"   OP_EDITOR_DOWNCASE_WORD
	"eol"             OP_EDITOR_EOL
	"forward-char"    OP_EDITOR_FORWARD_CHAR
	"forward-word"    OP_EDITOR_FORWARD_WORD
	"help"            OP_HELP
	"history-down"    OP_EDITOR_HISTORY_DOWN
	"history-search"  OP_EDITOR_HISTORY_SEARCH
	"history-up"      OP_EDITOR_HISTORY_UP
	"kill-eol"        OP_EDITOR_KILL_EOL
	"kill-eow"        OP_EDITOR_KILL_EOW
	"kill-line"       OP_EDITOR_KILL_LINE
	"kill-whole-line" OP_EDITOR_KILL_WHOLE_LINE
	"kill-word"       OP_EDITOR_KILL_WORD
	"mailbox-cycle"   OP_EDITOR_MAILBOX_CYCLE
	"quote-char"      OP_EDITOR_QUOTE_CHAR
	"redraw-screen"   OP_REDRAW
	"transpose-chars" OP_EDITOR_TRANSPOSE_CHARS
	"upcase-word"     OP_EDITOR_UPCASE_WORD

editor/functions.c:482:5: enter_function_dispatcher() - EnterFunctions[]
	OP_EDITOR_BACKSPACE       op_editor_backspace
	OP_EDITOR_BACKWARD_CHAR   op_editor_backward_char
	OP_EDITOR_BACKWARD_WORD   op_editor_backward_word
	OP_EDITOR_BOL             op_editor_bol
	OP_EDITOR_CAPITALIZE_WORD op_editor_capitalize_word
	OP_EDITOR_COMPLETE        op_editor_complete
	OP_EDITOR_COMPLETE_QUERY  op_editor_complete
	OP_EDITOR_DELETE_CHAR     op_editor_delete_char
	OP_EDITOR_DOWNCASE_WORD   op_editor_capitalize_word
	OP_EDITOR_EOL             op_editor_eol
	OP_EDITOR_FORWARD_CHAR    op_editor_forward_char
	OP_EDITOR_FORWARD_WORD    op_editor_forward_word
	OP_EDITOR_HISTORY_DOWN    op_editor_history_down
	OP_EDITOR_HISTORY_SEARCH  op_editor_history_search
	OP_EDITOR_HISTORY_UP      op_editor_history_up
	OP_EDITOR_KILL_EOL        op_editor_kill_eol
	OP_EDITOR_KILL_EOW        op_editor_kill_eow
	OP_EDITOR_KILL_LINE       op_editor_kill_line
	OP_EDITOR_KILL_WHOLE_LINE op_editor_kill_whole_line
	OP_EDITOR_KILL_WORD       op_editor_kill_word
	OP_EDITOR_MAILBOX_CYCLE   op_editor_complete
	OP_EDITOR_QUOTE_CHAR      op_editor_quote_char
	OP_EDITOR_TRANSPOSE_CHARS op_editor_transpose_chars
	OP_EDITOR_UPCASE_WORD     op_editor_capitalize_word
	OP_HELP                   op_help
	OP_REDRAW                 op_redraw
	

