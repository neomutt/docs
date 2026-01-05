# Commands Summary

## Part 1: Alias Commands (2 commands)

### 1. CMD_ALIAS - `alias`

**Parse Function:** `parse_alias()` in `alias/commands.c`

**Data Storage:**
- **Global List:** `struct AliasList Aliases` (defined in `alias/alias.h`)
- **Structure:** `struct Alias` containing: 
  - `char *name` - Alias key
  - `struct AddressList addr` - Email addresses
  - `char *comment` - Comment text
  - `struct TagList tags` - Tags parsed from comments
  
**Owner:** Global alias subsystem

**Additional Storage:**
- **Reverse lookup:** Hash table via `alias_reverse_add()`
- **Groups:** `NeoMutt->groups` (HashTable) if `-group` flag used

**Data Field:** `CMD_NO_DATA` (0)

### 2. CMD_UNALIAS - `unalias`

**Parse Function:** `parse_unalias()` in `alias/commands.c`

**Data Storage:**
- **Removes from:** `struct AliasList Aliases`
- **Pattern `*`:** Clears entire `Aliases` list via `aliaslist_clear()`
- **Specific key:** Searches `Aliases`, removes matching entry

**Owner:** Global alias subsystem

**Cleanup:**
- Calls `alias_reverse_delete()` before removal
- Calls `alias_free()` to deallocate memory

**Data Field:** `CMD_NO_DATA` (0)

## Part 2: Hook Commands (18 commands)

All hook commands are defined in `hooks/commands.c` and use various parsing functions.

### 3. CMD_ACCOUNT_HOOK - `account-hook`

**Parse Function:** `parse_hook_regex()` in `hooks/parse. c`

**Data Storage:**
- **Global List:** `Hooks` array (indexed by hook type)
- **Structure:** `struct Hook` containing:
  - `int type` - `MUTT_ACCOUNT_HOOK`
  - `struct Regex *regex` - Compiled regex pattern
  - `char *command` - Command to execute
  
**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 4. CMD_CHARSET_HOOK - `charset-hook`

**Parse Function:** `parse_hook_charset()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_CHARSET_HOOK`
- **Structure:** `struct Hook` with:
  - `char *regex->pattern` - Charset alias
  - `char *command` - Local charset name

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 5. CMD_CRYPT_HOOK - `crypt-hook`

**Parse Function:** `parse_hook_crypt()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_CRYPT_HOOK`
- **Structure:** `struct Hook` with:
  - `struct Regex *regex` - Recipient pattern
  - `char *command` - Key ID to use

**Owner:** Global hooks subsystem (ncrypt module)

**Data Field:** `CMD_NO_DATA` (0)

### 6. CMD_FCC_HOOK - `fcc-hook`

**Parse Function:** `parse_hook_mailbox()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_FCC_HOOK`
- **Structure:** `struct Hook` with:
  - `struct Pattern *pattern` - Message pattern
  - `char *command` - Mailbox path for saving

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 7. CMD_FCC_SAVE_HOOK - `fcc-save-hook`

**Parse Function:** `parse_hook_mailbox()` in `hooks/parse.c`

**Data Storage:**
- **Dual storage:** Creates both `MUTT_FCC_HOOK` and `MUTT_SAVE_HOOK` entries
- Same structure as `fcc-hook`

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 8. CMD_FOLDER_HOOK - `folder-hook`

**Parse Function:** `parse_hook_folder()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_FOLDER_HOOK`
- **Structure:** `struct Hook` with:
  - `struct Regex *regex` - Folder path pattern (or exact match if `-noregex`)
  - `char *command` - Commands to execute

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 9. CMD_ICONV_HOOK - `iconv-hook`

**Parse Function:** `parse_hook_charset()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_ICONV_HOOK`
- Similar to `charset-hook`, defines charset aliases

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 10. CMD_INDEX_FORMAT_HOOK - `index-format-hook`

**Parse Function:** `parse_hook_index()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_INDEX_FORMAT_HOOK`
- **Structure:** `struct Hook` with:
  - `char *regex->pattern` - Hook name
  - `struct Pattern *pattern` - Email pattern (optional negation with `!`)
  - `char *command` - Format string

**Owner:** Global hooks subsystem (index module)

**Data Field:** `CMD_NO_DATA` (0)

### 11. CMD_MBOX_HOOK - `mbox-hook`

**Parse Function:** `parse_hook_mbox()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_MBOX_HOOK`
- **Structure:** `struct Hook` with:
  - `struct Regex *regex` - Mailbox pattern
  - `char *command` - Destination mbox path

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 12. CMD_MESSAGE_HOOK - `message-hook`

**Parse Function:** `parse_hook_pattern()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_MESSAGE_HOOK`
- **Structure:** `struct Hook` with:
  - `struct Pattern *pattern` - Message pattern
  - `char *command` - Commands to execute

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 13. CMD_REPLY_HOOK - `reply-hook`

**Parse Function:** `parse_hook_pattern()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_REPLY_HOOK`
- Same structure as `message-hook`

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 14. CMD_SAVE_HOOK - `save-hook`

**Parse Function:** `parse_hook_mailbox()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_SAVE_HOOK`
- Same structure as `fcc-hook`

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 15. CMD_SEND_HOOK - `send-hook`

**Parse Function:** `parse_hook_pattern()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_SEND_HOOK`
- Same structure as `message-hook`

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 16. CMD_SEND2_HOOK - `send2-hook`

**Parse Function:** `parse_hook_pattern()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_SEND2_HOOK`
- Executed whenever composed message is edited

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 17. CMD_SHUTDOWN_HOOK - `shutdown-hook`

**Parse Function:** `parse_hook_global()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_SHUTDOWN_HOOK`
- **Structure:** `struct Hook` with:
  - `char *command` - Commands to run on shutdown
  - No pattern/regex (global hook)

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 18. CMD_STARTUP_HOOK - `startup-hook`

**Parse Function:** `parse_hook_global()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_STARTUP_HOOK`
- Same structure as `shutdown-hook`

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 19. CMD_TIMEOUT_HOOK - `timeout-hook`

**Parse Function:** `parse_hook_global()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_TIMEOUT_HOOK`
- Same structure as global hooks

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 20. CMD_UNHOOK - `unhook`

**Parse Function:** `parse_unhook()` in `hooks/parse.c`

**Data Storage:**
- **Removes from:** `Hooks` array
- **Pattern `*`:** Clears all hooks
- **Specific type:** Removes hooks of specified type

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

## Part 2: Key Binding Commands (6 commands)

All key binding commands are defined in `key/init.c` and registered via `KeyCommands`.

### 21. CMD_BIND - `bind`

**Parse Function:** `parse_bind()` in `key/commands.c`

**Data Storage:**
- **Global Array:** `struct KeymapList Keymaps[MENU_MAX]` (one list per menu type)
- **Structure:** `struct Keymap` containing:
  - `char *keys` - Key sequence
  - `int len` - Length of key sequence
  - `int op` - Operation code (e.g., `OP_DELETE`)
  - `char *macro` - NULL for bindings
  - `char *desc` - NULL for bindings
  - `short eq` - Sequence number

**Owner:** Global keybinding subsystem

**Additional Storage:**
- Each menu type (MENU_INDEX, MENU_PAGER, etc.) has its own list
- Stored in `Keymaps[]` array indexed by `enum MenuType`

**Data Field:** `CMD_NO_DATA` (0)

**Notifications:** Sends `NT_BINDING_ADD` or `NT_BINDING_DELETE` via `NeoMutt->notify`

### 22. CMD_UNBIND - `unbind`

**Parse Function:** `parse_unbind()` in `key/commands.c`

**Data Storage:**
- **Removes from:** `Keymaps[]` array
- **Pattern `*`:** Removes all bindings for specified menu(s), restores defaults
- **Specific key:** Removes binding for that key sequence

**Owner:** Global keybinding subsystem

**Behavior:**
- Sets operation to `OP_NULL` to unbind
- Can operate on multiple menus at once

**Data Field:** `CMD_NO_DATA` (0)

**Notifications:** Sends `NT_BINDING_DELETE` or `NT_BINDING_DELETE_ALL`

### 23. CMD_MACRO - `macro`

**Parse Function:** `parse_macro()` in `key/commands.c`

**Data Storage:**
- **Global Array:** Same `Keymaps[]` structure as `bind`
- **Structure:** `struct Keymap` containing:
  - `char *keys` - Key sequence that triggers macro
  - `int op` - Set to `OP_MACRO`
  - `char *macro` - Macro text (key sequence to execute)
  - `char *desc` - Optional description

**Owner:** Global keybinding subsystem

**Execution Storage:**
- **Macro buffer:** `struct KeyEventArray MacroEvents` in `key/get.c`
- When macro triggered, its text is pushed onto `MacroEvents` stack

**Data Field:** `CMD_NO_DATA` (0)

**Notifications:** Sends `NT_MACRO_ADD` via `NeoMutt->notify`

### 24. CMD_UNMACRO - `unmacro`

**Parse Function:** `parse_unbind()` in `key/commands.c` (shared with `unbind`)

**Data Storage:**
- **Removes from:** `Keymaps[]` array
- Same removal logic as `unbind` but for macros

**Owner:** Global keybinding subsystem

**Data Field:** `CMD_NO_DATA` (0)

**Notifications:** Sends `NT_MACRO_DELETE` or `NT_MACRO_DELETE_ALL`

### 25. CMD_EXEC - `exec`

**Parse Function:** `parse_exec()` in `key/commands.c`

**Data Storage:**
- **No persistent storage** - command executes immediately
- **Temporary storage:** 
  - Operations parsed into local `ops[]` array
  - Pushed onto `MacroEvents` buffer via `mutt_push_macro_event()`

**Owner:** Execution stack (transient)

**Behavior:**
- Looks up function names in menu's operation table
- Converts to operation codes
- Pushes onto macro event queue in reverse order

**Data Field:** `CMD_NO_DATA` (0)

### 26. CMD_PUSH - `push`

**Parse Function:** `parse_push()` in `key/commands.c`

**Data Storage:**
- **No persistent storage** - simulates typing immediately
- **Temporary storage:**
  - String tokenized via `generic_tokenize_push_string()`
  - Characters pushed onto `UngetKeyEvents` buffer

**Owner:** Input event queue (transient)

**Behavior:**
- Simulates user typing the string
- String is processed character-by-character
- Each character added to `UngetKeyEvents` buffer

**Data Field:** `CMD_NO_DATA` (0)

## Part 3: Configuration Commands (10 commands)

### 27. CMD_SET - `set`

**Parse Function:** `parse_set()` in `config/set.c`

**Data Storage:**
- **Global Config:** `NeoMutt->sub->cs` (ConfigSet)
- **Structure:** `struct HashElem` for each variable containing:
  - `char *key` - Variable name
  - `struct ConfigDef *data` - Variable definition
  - `intptr_t initial` - Initial value
  - `intptr_t data` - Current value

**Owner:** Global configuration subsystem

**Storage by Type:**
- **Bool/Quad:** Stored as `intptr_t` directly
- **Number:** Stored as `intptr_t` (long)
- **String:** Allocated string, pointer stored
- **Path:** Expanded path string
- **Address:** `struct Address` pointer
- **Enum:** Stored as integer index
- **Mbtable:** Multi-byte character table
- **Regex:** Compiled `regex_t` pointer
- **Slist:** String list structure

**Data Field:** `CMD_NO_DATA` (0)

**Notifications:** Sends `NT_CONFIG` with variable name

### 28. CMD_UNSET - `unset`

**Parse Function:** `parse_set()` in `config/set.c` (shared with `set`)

**Data Storage:**
- **Modifies:** `NeoMutt->sub->cs` (ConfigSet)
- **Action:** Resets variable to empty/NULL state
  - Bools: Set to false
  - Strings: Set to NULL/empty
  - Numbers: Set to 0

**Owner:** Global configuration subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 29. CMD_RESET - `reset`

**Parse Function:** `parse_set()` in `config/set.c` (shared with `set`)

**Data Storage:**
- **Modifies:** `NeoMutt->sub->cs` (ConfigSet)
- **Action:** Restores variable to its `initial` value from `struct ConfigDef`

**Owner:** Global configuration subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 30. CMD_TOGGLE - `toggle`

**Parse Function:** `parse_set()` in `config/set.c` (shared with `set`)

**Data Storage:**
- **Modifies:** `NeoMutt->sub->cs` (ConfigSet)
- **Action:** For bool/quad variables: 
  - `MUTT_YES` → `MUTT_NO`
  - `MUTT_NO` → `MUTT_YES`
  - `MUTT_ASKYES` → `MUTT_ASKNO`
  - `MUTT_ASKNO` → `MUTT_ASKYES`

**Owner:** Global configuration subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 31. CMD_SETENV - `setenv`

**Parse Function:** `parse_setenv()` in `commands/setenv.c`

**Data Storage:**
- **Process Environment:** `NeoMutt->env` (char** array, private copy of environ)
- **System Environment:** Also sets in actual process via `setenv(3)`

**Owner:** Global NeoMutt environment

**Structure:**
- Array of `"NAME=value"` strings
- NULL-terminated like `environ`

**Query Mode:** `setenv VAR? ` queries value without setting

**Data Field:** `CMD_NO_DATA` (0)

### 32. CMD_UNSETENV - `unsetenv`

**Parse Function:** `parse_setenv()` in `commands/setenv.c` (shared parser)

**Data Storage:**
- **Removes from:** `NeoMutt->env` and system environment
- Calls `unsetenv(3)` to remove from process

**Owner:** Global NeoMutt environment

**Data Field:** `CMD_NO_DATA` (0)

### 33. CMD_SOURCE - `source`

**Parse Function:** `parse_source()` in `commands/source.c`

**Data Storage:**
- **No persistent storage** - reads and executes file immediately
- **Temporary:** File descriptor and buffer during parsing

**Owner:** Parser (transient)

**Behavior:**
- Opens file specified
- Reads line-by-line
- Each line passed to `parse_rc_line()`
- Nested sourcing supported

**Data Field:** `CMD_NO_DATA` (0)

### 34. CMD_FINISH - `finish`

**Parse Function:** `parse_finish()` in `commands/ifdef.c`

**Data Storage:**
- **No persistent storage**
- **Action:** Sets return code to `MUTT_CMD_FINISH`

**Owner:** Parser state (transient)

**Behavior:**
- Stops processing current config file
- Returns control to caller
- Often used with `ifdef`/`ifndef`

**Data Field:** `CMD_NO_DATA` (0)

### 35. CMD_IFDEF - `ifdef`

**Parse Function:** `parse_ifdef()` in `commands/ifdef.c`

**Data Storage:**
- **No persistent storage**
- **Checks:** Symbol tables for compile-time features

**Owner:** Parser evaluation (transient)

**Symbol Sources Checked:**
- Config variables in `NeoMutt->sub->cs`
- Functions in menu operation tables
- Compile-time features (`ENABLE_NLS`, `USE_IMAP`, etc.)

**Behavior:**
- If symbol defined:  Execute command
- If not defined: Skip command

**Data Field:** `CMD_NO_DATA` (0)

### 36. CMD_IFNDEF - `ifndef`

**Parse Function:** `parse_ifdef()` in `commands/ifdef.c` (shared parser)

**Data Storage:**
- Same as `ifdef`

**Owner:** Parser evaluation (transient)

**Behavior:**
- Inverse of `ifdef`
- If symbol NOT defined: Execute command
- If defined: Skip command

**Data Field:** `CMD_NO_DATA` (0)

## Part 4: List Management Commands (12 commands)

### 37. CMD_ALTERNATES - `alternates`

**Parse Function:** `parse_alternates()` in `commands/alternates.c`

**Data Storage:**
- **Global List:** `struct RegexList Alternates`
- **Structure:** `struct RegexNode` containing:
  - `struct Regex *regex` - Compiled pattern
  - `STAILQ_ENTRY` - List linkage

**Owner:** Global alternates subsystem

**Additional Storage:**
- **Groups:** Can add to `NeoMutt->groups` via `-group` flag

**Purpose:** Define user's alternate email addresses

**Data Field:** `CMD_NO_DATA` (0)

### 38. CMD_UNALTERNATES - `unalternates`

**Parse Function:** `parse_unalternates()` in `commands/alternates.c`

**Data Storage:**
- **Removes from:** `struct RegexList Alternates`
- **Pattern `*`:** Clears entire list

**Owner:** Global alternates subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 39. CMD_LISTS - `lists`

**Parse Function:** `parse_lists()` in `commands/group.c`

**Data Storage:**
- **Global List:** `struct RegexList MailLists`
- **Structure:** `struct RegexNode` with compiled regex

**Owner:** Global mailing list subsystem

**Additional Storage:**
- **Groups:** Can categorize lists via `-group` flag

**Purpose:** Recognize mailing list addresses

**Data Field:** `CMD_NO_DATA` (0)

### 40. CMD_UNLISTS - `unlists`

**Parse Function:** `parse_unlists()` in `commands/group.c`

**Data Storage:**
- **Removes from:** `struct RegexList MailLists`
- **Pattern `*`:** Clears entire list

**Owner:** Global mailing list subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 41. CMD_SUBSCRIBE - `subscribe`

**Parse Function:** `parse_subscribe()` in `commands/group.c`

**Data Storage:**
- **Global List:** `struct RegexList SubscribedLists`
- **Structure:** `struct RegexNode` with compiled regex

**Owner:** Global subscription subsystem

**Purpose:** Mark mailing lists user is subscribed to

**Data Field:** `CMD_NO_DATA` (0)

### 42. CMD_UNSUBSCRIBE - `unsubscribe`

**Parse Function:** `parse_unsubscribe()` in `commands/group.c`

**Data Storage:**
- **Removes from:** `struct RegexList SubscribedLists`
- **Pattern `*`:** Clears entire list

**Owner:** Global subscription subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 43. CMD_SUBSCRIBE_TO - `subscribe-to`

**Parse Function:** `parse_subscribe_to()` in `nntp/commands.c` (NNTP-specific)

**Data Storage:**
- **NNTP Server Data:** `struct NntpAccountData *adata`
- **Structure:** `struct NntpMboxData` for newsgroup containing:
  - `bool subscribed` - Subscription flag
  - Stored in server's newsgroup list

**Owner:** NNTP account data structure

**Purpose:** Subscribe to NNTP newsgroups

**Data Field:** `CMD_NO_DATA` (0)

**Note:** NNTP module must be compiled in

### 44. CMD_UNSUBSCRIBE_FROM - `unsubscribe-from`

**Parse Function:** `parse_unsubscribe_from()` in `nntp/commands.c`

**Data Storage:**
- **Modifies:** Same NNTP newsgroup data
- Sets `subscribed = false`

**Owner:** NNTP account data structure

**Data Field:** `CMD_NO_DATA` (0)

### 45. CMD_IGNORE - `ignore`

**Parse Function:** `parse_ignore()` in `commands/ignore.c`

**Data Storage:**
- **Global List:** `struct ListHead Ignore`
- **Structure:** `struct ListNode` containing:
  - `char *data` - Header field name to ignore
  - `STAILQ_ENTRY` - List linkage

**Owner:** Global header display subsystem

**Purpose:** Hide headers when displaying messages

**Special Case:** `ignore *` ignores all headers

**Data Field:** `CMD_NO_DATA` (0)

### 46. CMD_UNIGNORE - `unignore`

**Parse Function:** `parse_unignore()` in `commands/ignore.c`

**Data Storage:**
- **Removes from:** `struct ListHead Ignore`
- **Pattern `*`:** Clears entire ignore list (show all headers)

**Owner:** Global header display subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 47. CMD_HDR_ORDER - `hdr_order`

**Parse Function:** `parse_stailq()` in `commands/parse.c`

**Data Storage:**
- **Global List:** `struct ListHead HeaderOrderList`
- **Structure:** `struct ListNode` with header field names

**Owner:** Global header display subsystem

**Purpose:** Define order headers are displayed

**Data Field:** `IP &HeaderOrderList` (pointer to the list)

### 48. CMD_UNHDR_ORDER - `unhdr_order`

**Parse Function:** `parse_unstailq()` in `commands/parse.c`

**Data Storage:**
- **Removes from:** `HeaderOrderList`
- **Pattern `*`:** Clears entire list

**Owner:** Global header display subsystem

**Data Field:** `IP &HeaderOrderList` (pointer to the list)

## Part 5: MIME and Attachment Commands (8 commands)

### 49. CMD_ALTERNATIVE_ORDER - `alternative_order`

**Parse Function:** `parse_stailq()` in `commands/parse.c`

**Data Storage:**
- **Global List:** `struct ListHead AlternativeOrderList`
- **Structure:** `struct ListNode` containing:
  - `char *data` - MIME type (e.g., "text/plain")

**Owner:** Global MIME handler subsystem

**Purpose:** Set preference order for multipart/alternative

**Data Field:** `IP &AlternativeOrderList`

### 50. CMD_UNALTERNATIVE_ORDER - `unalternative_order`

**Parse Function:** `parse_unstailq()` in `commands/parse.c`

**Data Storage:**
- **Removes from:** `AlternativeOrderList`
- **Pattern `*`:** Clears entire list

**Owner:** Global MIME handler subsystem

**Data Field:** `IP &AlternativeOrderList`

### 51. CMD_AUTO_VIEW - `auto_view`

**Parse Function:** `parse_stailq()` in `commands/parse.c`

**Data Storage:**
- **Global List:** `struct ListHead AutoViewList`
- **Structure:** `struct ListNode` with MIME types

**Owner:** Global MIME handler subsystem

**Purpose:** MIME types to display automatically inline

**Data Field:** `IP &AutoViewList`

### 52. CMD_UNAUTO_VIEW - `unauto_view`

**Parse Function:** `parse_unstailq()` in `commands/parse.c`

**Data Storage:**
- **Removes from:** `AutoViewList`
- **Pattern `*`:** Clears entire list

**Owner:** Global MIME handler subsystem

**Data Field:** `IP &AutoViewList`

### 53. CMD_MIME_LOOKUP - `mime_lookup`

**Parse Function:** `parse_stailq()` in `commands/parse.c`

**Data Storage:**
- **Global List:** `struct ListHead MimeLookupList`
- **Structure:** `struct ListNode` with MIME types

**Owner:** Global MIME handler subsystem

**Purpose:** MIME types to look up via mailcap

**Data Field:** `IP &MimeLookupList`

### 54. CMD_UNMIME_LOOKUP - `unmime_lookup`

**Parse Function:** `parse_unstailq()` in `commands/parse.c`

**Data Storage:**
- **Removes from:** `MimeLookupList`
- **Pattern `*`:** Clears entire list

**Owner:** Global MIME handler subsystem

**Data Field:** `IP &MimeLookupList`

### 55. CMD_ATTACHMENTS - `attachments`

**Parse Function:** `parse_attachments()` in `attach/commands.c`

**Data Storage:**
- **Global Lists:**
  - `struct AttachMatch *AttachAllow` - Allowed attachments
  - `struct AttachMatch *AttachExclude` - Excluded attachments
  - `struct AttachMatch *InlineAllow` - Allowed inline
  - `struct AttachMatch *InlineExclude` - Excluded inline
- **Structure:** `struct AttachMatch` containing:
  - `char *major` - MIME major type
  - `char *minor` - MIME minor type (can be regex)
  - `int major_int` - Parsed major type code
  - `struct Regex *minor_regex` - Compiled minor type pattern

**Owner:** Global attachment subsystem

**Purpose:** Control attachment counting and display

**Data Field:** `CMD_NO_DATA` (0)

### 56. CMD_UNATTACHMENTS - `unattachments`

**Parse Function:** `parse_unattachments()` in `attach/commands.c`

**Data Storage:**
- **Removes from:** `AttachAllow`, `AttachExclude`, `InlineAllow`, `InlineExclude`
- **Pattern `*`:** Clears all attachment rules

**Owner:** Global attachment subsystem

**Data Field:** `CMD_NO_DATA` (0)

## Part 6: Color and Display Commands (4 commands)

### 57. CMD_COLOR - `color`

**Parse Function:** `parse_color()` in `color/parse_color.c`

**Data Storage:**
- **Global Array:** `struct ColorLineList ColorList[MT_COLOR_MAX]`
- **Structure:** `struct ColorLine` containing:
  - `enum ColorId cid` - Color object ID (e.g., `MT_COLOR_HEADER`)
  - `struct AttrColor color` - Foreground/background/attributes
  - `struct Regex *regex` - Pattern for conditional coloring (optional)
  - `int match` - Match number for regex groups

**Owner:** Global color subsystem

**Storage per Color Object:**
- Simple colors: Single entry in `ColorList[cid]`
- Pattern colors: Multiple entries (e.g., `color header red blue "^From:"`)

**Merged Colors:**
- Colors can be merged/overlaid
- Final color computed by merging all matching rules

**Data Field:** `CMD_NO_DATA` (0)

**Notifications:** Sends `NT_COLOR` with color ID

### 58. CMD_UNCOLOR - `uncolor`

**Parse Function:** `parse_uncolor()` in `color/commands.c`

**Data Storage:**
- **Removes from:** `ColorList[]` array
- **Pattern `*`:** Removes all patterns for specified object
- **Specific pattern:** Removes matching color rule

**Owner:** Global color subsystem

**Data Field:** `CMD_NO_DATA` (0)

**Notifications:** Sends `NT_COLOR` with color ID

### 59. CMD_MONO - `mono`

**Parse Function:** `parse_mono()` in `color/commands.c`

**Data Storage:**
- **Same as `color`** but only sets attributes (bold, underline, etc.)
- Uses same `ColorList[]` structure
- Foreground/background colors ignored on monochrome terminals

**Owner:** Global color subsystem

**Status:** Deprecated (use `color` instead)

**Data Field:** `CMD_NO_DATA` (0)

### 60. CMD_UNMONO - `unmono`

**Parse Function:** `parse_unmono()` in `color/commands.c`

**Data Storage:**
- **Removes from:** `ColorList[]` array
- Same removal logic as `uncolor`

**Owner:** Global color subsystem

**Status:** Deprecated (use `uncolor` instead)

**Data Field:** `CMD_NO_DATA` (0)

## Part 7: Scoring and Spam Commands (4 commands)

### 61. CMD_SCORE - `score`

**Parse Function:** `parse_score()` in `commands/score.c`

**Data Storage:**
- **Global List:** `struct ScoreList Scores`
- **Structure:** `struct Score` containing:
  - `struct Pattern *pattern` - Message pattern to match
  - `int score` - Score value to add
  - `bool exact` - Exact match flag

**Owner:** Global scoring subsystem

**Behavior:**
- Patterns evaluated against messages
- Matching patterns' scores accumulated
- Final score stored in `email->score`

**Data Field:** `CMD_NO_DATA` (0)

### 62. CMD_UNSCORE - `unscore`

**Parse Function:** `parse_unscore()` in `commands/score.c`

**Data Storage:**
- **Removes from:** `struct ScoreList Scores`
- **Pattern `*`:** Clears all scoring rules

**Owner:** Global scoring subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 63. CMD_SPAM - `spam`

**Parse Function:** `parse_spam()` in `commands/spam.c`

**Data Storage:**
- **Global List:** `struct ReplaceList SpamList`
- **Structure:** `struct Replace` containing:
  - `struct Regex *regex` - Pattern to match in headers
  - `char *templ` - Replacement template (format string)

**Owner:** Global spam detection subsystem

**Purpose:**
- Parse spam headers (X-Spam-Score, etc.)
- Extract spam score/status
- Format for display via `%H` expando

**Data Field:** `CMD_NO_DATA` (0)

### 64. CMD_NOSPAM - `nospam`

**Parse Function:** `parse_nospam()` in `commands/spam.c`

**Data Storage:**
- **Removes from:** `struct ReplaceList SpamList`
- **Pattern `*`:** Clears all spam rules

**Owner:** Global spam detection subsystem

**Data Field:** `CMD_NO_DATA` (0)

## Part 8: Group and Address Management (4 commands)

### 65. CMD_GROUP - `group`

**Parse Function:** `parse_group()` in `commands/group.c`

**Data Storage:**
- **Global Hash Table:** `NeoMutt->groups` (HashTable)
- **Structure:** `struct Group` containing:
  - `char *name` - Group name
  - `struct RegexList rx_list` - Regex patterns to match addresses
  - `struct AddressList addr_list` - Explicit addresses in group

**Owner:** Global group subsystem (also accessible by aliases)

**Behavior:**
- `-rx` flag: Add regex pattern to group
- `-addr` flag: Add explicit addresses to group

**Data Field:** `CMD_NO_DATA` (0)

### 66. CMD_UNGROUP - `ungroup`

**Parse Function:** `parse_group()` in `commands/group.c` (shared parser)

**Data Storage:**
- **Removes from:** `NeoMutt->groups`
- **Pattern `*`:** Removes all addresses/patterns from group
- **Specific:** Removes matching addresses or patterns

**Owner:** Global group subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 67. CMD_MY_HDR - `my_hdr`

**Parse Function:** `parse_my_hdr()` in `commands/my_hdr.c`

**Data Storage:**
- **Global List:** `struct ListHead UserHeader`
- **Structure:** `struct ListNode` containing:
  - `char *data` - Complete header line ("Name: value")

**Owner:** Global custom header subsystem

**Purpose:** Add custom headers to outgoing messages

**Data Field:** `CMD_NO_DATA` (0)

### 68. CMD_UNMY_HDR - `unmy_hdr`

**Parse Function:** `parse_unmy_hdr()` in `commands/my_hdr.c`

**Data Storage:**
- **Removes from:** `struct ListHead UserHeader`
- **Pattern `*`:** Removes all custom headers
- **Field name:** Removes headers starting with specified field

**Owner:** Global custom header subsystem

**Data Field:** `CMD_NO_DATA` (0)

## Part 9: Mailbox Management Commands (3 commands)

### 69. CMD_MAILBOXES - `mailboxes`

**Parse Function:** `parse_mailboxes()` in `commands/mailboxes.c`

**Data Storage:**
- **Global List:** `struct MailboxList AllMailboxes`
- **Structure:** `struct Mailbox` containing:
  - `char *name` - Mailbox name
  - `char *realpath` - Actual path to mailbox
  - `enum MailboxType type` - Type (MBOX, MAILDIR, IMAP, etc.)
  - `char *label` - Optional label for display
  - `bool notify` - New mail notification flag
  - `bool poll` - Polling enabled flag
  - `struct Account *account` - Parent account

**Owner:** Global mailbox subsystem

**Additional Storage:**
- Mailboxes also stored in `NeoMutt->accounts` array
- Each account has `struct AccountMailboxes` list

**Flags:**
- `-label <name>` or `-nolabel` - Set display label
- `-notify` or `-nonotify` - Control notifications
- `-poll` or `-nopoll` - Control polling

**Data Field:** `CMD_NO_DATA` (0)

**Notifications:** Sends `NT_MAILBOX_ADD`

### 70. CMD_NAMED_MAILBOXES - `named-mailboxes`

**Parse Function:** `parse_mailboxes()` in `commands/mailboxes.c` (shared)

**Data Storage:**
- **Same as `mailboxes`** but requires explicit labels
- Syntax: `named-mailboxes <label> <path> [<label> <path> ...]`

**Owner:** Global mailbox subsystem

**Difference from `mailboxes`:**
- Must provide label for each mailbox
- Cannot use flags like `-label`, `-notify`, `-poll`

**Data Field:** `CMD_NO_DATA` (0)

### 71. CMD_UNMAILBOXES - `unmailboxes`

**Parse Function:** `parse_unmailboxes()` in `commands/mailboxes.c`

**Data Storage:**
- **Removes from:** `AllMailboxes` list
- **Pattern `*`:** Removes all mailboxes from watch list
- **Specific path:** Removes matching mailbox

**Owner:** Global mailbox subsystem

**Behavior:**
- Does not delete mailbox data, only removes from monitoring
- Mailbox can be re-added later

**Data Field:** `CMD_NO_DATA` (0)

**Notifications:** Sends `NT_MAILBOX_DELETE`

## Part 10: Tag Transform Commands (4 commands)

### 72. CMD_TAG_FORMATS - `tag-formats`

**Parse Function:** `parse_tag_formats()` in `commands/tags.c`

**Data Storage:**
- **Global Hash Table:** `struct HashTable *TagFormats`
- **Structure:** Hash entry containing:
  - `char *key` - Tag name
  - `char *value` - Format string (expando)

**Owner:** Global tag subsystem (Notmuch feature)

**Purpose:** Define how tags are formatted/expanded in index

**Example:** `tag-formats "inbox" "GI"`

**Data Field:** `CMD_NO_DATA` (0)

**Note:** Notmuch support must be compiled in

### 73. CMD_TAG_TRANSFORMS - `tag-transforms`

**Parse Function:** `parse_tag_transforms()` in `commands/tags.c`

**Data Storage:**
- **Global Hash Table:** `struct HashTable *TagTransforms`
- **Structure:** Hash entry containing:
  - `char *key` - Tag name
  - `char *value` - Transformed display string (often icon/symbol)

**Owner:** Global tag subsystem

**Purpose:** Transform tag names to icons/symbols for display

**Example:** `tag-transforms "inbox" "📥" "sent" "📤"`

**Data Field:** `CMD_NO_DATA` (0)

### 74. CMD_SUBJECTRX - `subjectrx`

**Parse Function:** `parse_subjectrx_list()` in `commands/subjectrx.c`

**Data Storage:**
- **Global List:** `struct ReplaceList SubjectRegexList`
- **Structure:** `struct Replace` containing:
  - `struct Regex *regex` - Pattern to match in subject
  - `char *templ` - Replacement template

**Owner:** Global subject rewriting subsystem

**Purpose:** Apply regex-based transformations to displayed subjects

**Example:** `subjectrx "\\[.*\\] (.*)" "%1"` - Remove mailing list tags

**Data Field:** `CMD_NO_DATA` (0)

### 75. CMD_UNSUBJECTRX - `unsubjectrx`

**Parse Function:** `parse_unsubjectrx_list()` in `commands/subjectrx.c`

**Data Storage:**
- **Removes from:** `SubjectRegexList`
- **Pattern `*`:** Clears all subject rewriting rules
- **Specific regex:** Removes matching rule

**Owner:** Global subject rewriting subsystem

**Data Field:** `CMD_NO_DATA` (0)

## Part 11: Mailto and Sidebar Commands (4 commands)

### 76. CMD_MAILTO_ALLOW - `mailto_allow`

**Parse Function:** `parse_stailq()` in `commands/parse.c`

**Data Storage:**
- **Global List:** `struct ListHead MailToAllow`
- **Structure:** `struct ListNode` with allowed header field names

**Owner:** Global mailto handler subsystem

**Purpose:** Whitelist header fields allowed in `mailto: ` URLs

**Security:** Prevents arbitrary headers being set via mailto links

**Data Field:** `IP &MailToAllow`

### 77. CMD_UNMAILTO_ALLOW - `unmailto_allow`

**Parse Function:** `parse_unstailq()` in `commands/parse.c`

**Data Storage:**
- **Removes from:** `MailToAllow`
- **Pattern `*`:** Clears entire whitelist (blocks all extra headers)

**Owner:** Global mailto handler subsystem

**Data Field:** `IP &MailToAllow`

### 78. CMD_SIDEBAR_PIN - `sidebar_pin`

**Parse Function:** `parse_sidebar_pin()` in `sidebar/commands.c`

**Data Storage:**
- **Global List:** `struct ListHead SidebarPinned`
- **Structure:** `struct ListNode` containing:
  - `char *data` - Mailbox path to pin

**Owner:** Sidebar subsystem

**Purpose:** Pin mailboxes to top of sidebar (always visible)

**Data Field:** `CMD_NO_DATA` (0)

**Note:** Sidebar support must be compiled in

### 79. CMD_SIDEBAR_UNPIN - `sidebar_unpin`

**Parse Function:** `parse_sidebar_unpin()` in `sidebar/commands.c`

**Data Storage:**
- **Removes from:** `SidebarPinned`
- **Pattern `*`:** Unpins all mailboxes

**Owner:** Sidebar subsystem

**Data Field:** `CMD_NO_DATA` (0)

## Part 12: Utility and Information Commands (7 commands)

### 80. CMD_CD - `cd`

**Parse Function:** `parse_cd()` in `commands/parse. c`

**Data Storage:**
- **No persistent storage**
- **Action:** Changes process working directory via `chdir(2)`

**Owner:** Process state (system call)

**Behavior:**
- No argument: Change to `$HOME`
- With path: Change to specified directory
- Updates `pwd` for relative path resolution

**Data Field:** `CMD_NO_DATA` (0)

### 81. CMD_ECHO - `echo`

**Parse Function:** `parse_echo()` in `commands/parse.c`

**Data Storage:**
- **No persistent storage**
- **Action:** Displays message to status line via `mutt_message()`

**Owner:** Message window (transient)

**Behavior:**
- Expands variables and expandos in message
- Message displayed until next screen update

**Data Field:** `CMD_NO_DATA` (0)

### 82. CMD_VERSION - `version`

**Parse Function:** `parse_version()` in `commands/parse.c`

**Data Storage:**
- **No persistent storage**
- **Action:** Displays version information

**Owner:** Display output (transient)

**Output Includes:**
- NeoMutt version string
- Build date
- Compile-time features
- System information

**Data Field:** `CMD_NO_DATA` (0)

### 83. CMD_HOOKS - `hooks`

**Parse Function:** `parse_hooks()` in `hooks/commands.c`

**Data Storage:**
- **No persistent storage**
- **Action:** Displays all defined hooks

**Owner:** Display output (transient)

**Behavior:**
- Dumps all entries from `Hooks` array
- Groups by hook type
- Shows pattern and command for each

**Data Field:** `CMD_NO_DATA` (0)

### 84. CMD_LUA - `lua`

**Parse Function:** `parse_lua()` in `lua/commands.c`

**Data Storage:**
- **No persistent storage for command itself**
- **Action:** Executes Lua code immediately
- **Lua State:** `lua_State *LuaState` (global Lua interpreter)

**Owner:** Lua interpreter state

**Behavior:**
- Parses Lua expression from command line
- Executes in global Lua context
- Can modify Lua variables/functions

**Data Field:** `CMD_NO_DATA` (0)

**Note:** Lua support must be compiled in (`USE_LUA`)

### 85. CMD_LUA_SOURCE - `lua-source`

**Parse Function:** `parse_lua_source()` in `lua/commands.c`

**Data Storage:**
- **No persistent storage for command**
- **Action:** Loads and executes Lua file
- **Lua State:** Uses global `LuaState`

**Owner:** Lua interpreter state

**Behavior:**
- Opens specified Lua file
- Executes via `luaL_dofile()`
- Can define functions, set variables, etc.

**Data Field:** `CMD_NO_DATA` (0)

**Note:** Lua support must be compiled in

### 86. CMD_APPEND_HOOK - `append-hook`

**Parse Function:** `parse_hook_folder()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_APPEND_HOOK`
- **Structure:** `struct Hook` with:
  - `struct Regex *regex` - Folder pattern
  - `char *command` - Commands to execute when appending to folder

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### 87. CMD_CLOSE_HOOK - `close-hook`

**Parse Function:** `parse_hook_folder()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_CLOSE_HOOK`
- **Structure:** Same as `append-hook`

**Owner:** Global hooks subsystem

**Purpose:** Execute commands when closing a folder

**Data Field:** `CMD_NO_DATA` (0)

### 88. CMD_OPEN_HOOK - `open-hook`

**Parse Function:** `parse_hook_folder()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_OPEN_HOOK`
- **Structure:** Same as `append-hook`

**Owner:** Global hooks subsystem

**Purpose:** Execute commands when opening a folder

**Data Field:** `CMD_NO_DATA` (0)

## Part 13: Final Command

### 89. CMD_EXEC - `exec` (already covered in Part 2)

This was already detailed in the Key Binding Commands section (#25).

# **Summary Statistics**

## Data Ownership Summary:

| Owner | Count | Commands |
|-------|-------|----------|
| **Global Lists/Arrays** | 45 | Aliases, Hooks, Lists, Scores, Colors, etc. |
| **NeoMutt->sub->cs (Config)** | 10 | set, unset, reset, toggle, etc. |
| **Keymaps[] Array** | 6 | bind, unbind, macro, unmacro, exec, push |
| **NeoMutt->groups** | 2 | group, ungroup |
| **NeoMutt->accounts** | 3 | mailboxes, named-mailboxes, unmailboxes |
| **Transient/No Storage** | 10 | echo, cd, version, source, etc. |
| **Module-Specific** | 13 | NNTP, Lua, Sidebar, Notmuch features |

## Storage Pattern Summary:

1. **Global Lists** (most common): 
   - Singly-linked:  `STAILQ_HEAD`
   - Doubly-linked: `TAILQ_HEAD`
   - Hash tables: `struct HashTable`

2. **Configuration Values**:
   - Stored in `NeoMutt->sub->cs` (ConfigSet)
   - Type-specific storage (bool, string, number, etc.)

3. **Per-Menu Data**:
   - Keybindings:  Separate list per menu type
   - Functions: Menu-specific operation tables

4. **Account/Mailbox Data**:
   - Hierarchical:  Account → Mailboxes
   - Stored in `NeoMutt->accounts`

5. **Transient Commands**:
   - Execute immediately, no persistent storage
   - Examples: echo, cd, version, exec, push

## Data Field Values:

- **`CMD_NO_DATA` (0)**: 85 commands
- **Pointer to list**: 4 commands (alternative_order, hdr_order, mailto_allow, etc.)

