# Commands Summary

## Alias

### `alias`

**Command:** `CMD_ALIAS`

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

### `unalias`

**Command:** `CMD_UNALIAS`

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

## Hook

All hook commands are defined in `hooks/commands.c` and use various parsing functions.

### `account-hook`

**Command:** `CMD_ACCOUNT_HOOK`

**Parse Function:** `parse_hook_regex()` in `hooks/parse. c`

**Data Storage:**
- **Global List:** `Hooks` array (indexed by hook type)
- **Structure:** `struct Hook` containing:
  - `int type` - `MUTT_ACCOUNT_HOOK`
  - `struct Regex *regex` - Compiled regex pattern
  - `char *command` - Command to execute

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `charset-hook`

**Command:** `CMD_CHARSET_HOOK`

**Parse Function:** `parse_hook_charset()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_CHARSET_HOOK`
- **Structure:** `struct Hook` with:
  - `char *regex->pattern` - Charset alias
  - `char *command` - Local charset name

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `crypt-hook`

**Command:** `CMD_CRYPT_HOOK`

**Parse Function:** `parse_hook_crypt()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_CRYPT_HOOK`
- **Structure:** `struct Hook` with:
  - `struct Regex *regex` - Recipient pattern
  - `char *command` - Key ID to use

**Owner:** Global hooks subsystem (ncrypt module)

**Data Field:** `CMD_NO_DATA` (0)

### `fcc-hook`

**Command:** `CMD_FCC_HOOK`

**Parse Function:** `parse_hook_mailbox()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_FCC_HOOK`
- **Structure:** `struct Hook` with:
  - `struct Pattern *pattern` - Message pattern
  - `char *command` - Mailbox path for saving

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `fcc-save-hook`

**Command:** `CMD_FCC_SAVE_HOOK`

**Parse Function:** `parse_hook_mailbox()` in `hooks/parse.c`

**Data Storage:**
- **Dual storage:** Creates both `MUTT_FCC_HOOK` and `MUTT_SAVE_HOOK` entries
- Same structure as `fcc-hook`

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `folder-hook`

**Command:** `CMD_FOLDER_HOOK`

**Parse Function:** `parse_hook_folder()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_FOLDER_HOOK`
- **Structure:** `struct Hook` with:
  - `struct Regex *regex` - Folder path pattern (or exact match if `-noregex`)
  - `char *command` - Commands to execute

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `iconv-hook`

**Command:** `CMD_ICONV_HOOK`

**Parse Function:** `parse_hook_charset()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_ICONV_HOOK`
- Similar to `charset-hook`, defines charset aliases

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `index-format-hook`

**Command:** `CMD_INDEX_FORMAT_HOOK`

**Parse Function:** `parse_hook_index()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_INDEX_FORMAT_HOOK`
- **Structure:** `struct Hook` with:
  - `char *regex->pattern` - Hook name
  - `struct Pattern *pattern` - Email pattern (optional negation with `!`)
  - `char *command` - Format string

**Owner:** Global hooks subsystem (index module)

**Data Field:** `CMD_NO_DATA` (0)

### `mbox-hook`

**Command:** `CMD_MBOX_HOOK`

**Parse Function:** `parse_hook_mbox()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_MBOX_HOOK`
- **Structure:** `struct Hook` with:
  - `struct Regex *regex` - Mailbox pattern
  - `char *command` - Destination mbox path

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `message-hook`

**Command:** `CMD_MESSAGE_HOOK`

**Parse Function:** `parse_hook_pattern()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_MESSAGE_HOOK`
- **Structure:** `struct Hook` with:
  - `struct Pattern *pattern` - Message pattern
  - `char *command` - Commands to execute

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `reply-hook`

**Command:** `CMD_REPLY_HOOK`

**Parse Function:** `parse_hook_pattern()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_REPLY_HOOK`
- Same structure as `message-hook`

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `save-hook`

**Command:** `CMD_SAVE_HOOK`

**Parse Function:** `parse_hook_mailbox()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_SAVE_HOOK`
- Same structure as `fcc-hook`

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `send-hook`

**Command:** `CMD_SEND_HOOK`

**Parse Function:** `parse_hook_pattern()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_SEND_HOOK`
- Same structure as `message-hook`

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `send2-hook`

**Command:** `CMD_SEND2_HOOK`

**Parse Function:** `parse_hook_pattern()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_SEND2_HOOK`
- Executed whenever composed message is edited

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `shutdown-hook`

**Command:** `CMD_SHUTDOWN_HOOK`

**Parse Function:** `parse_hook_global()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_SHUTDOWN_HOOK`
- **Structure:** `struct Hook` with:
  - `char *command` - Commands to run on shutdown
  - No pattern/regex (global hook)

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `startup-hook`

**Command:** `CMD_STARTUP_HOOK`

**Parse Function:** `parse_hook_global()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_STARTUP_HOOK`
- Same structure as `shutdown-hook`

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `timeout-hook`

**Command:** `CMD_TIMEOUT_HOOK`

**Parse Function:** `parse_hook_global()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_TIMEOUT_HOOK`
- Same structure as global hooks

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `unhook`

**Command:** `CMD_UNHOOK`

**Parse Function:** `parse_unhook()` in `hooks/parse.c`

**Data Storage:**
- **Removes from:** `Hooks` array
- **Pattern `*`:** Clears all hooks
- **Specific type:** Removes hooks of specified type

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

## Key Binding

All key binding commands are defined in `key/init.c` and registered via `KeyCommands`.

### `bind`

**Command:** `CMD_BIND`

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

### `unbind`

**Command:** `CMD_UNBIND`

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

### `macro`

**Command:** `CMD_MACRO`

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

### `unmacro`

**Command:** `CMD_UNMACRO`

**Parse Function:** `parse_unbind()` in `key/commands.c` (shared with `unbind`)

**Data Storage:**
- **Removes from:** `Keymaps[]` array
- Same removal logic as `unbind` but for macros

**Owner:** Global keybinding subsystem

**Data Field:** `CMD_NO_DATA` (0)

**Notifications:** Sends `NT_MACRO_DELETE` or `NT_MACRO_DELETE_ALL`

### `exec`

**Command:** `CMD_EXEC`

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

### `push`

**Command:** `CMD_PUSH`

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

## Configuration

### `set`

**Command:** `CMD_SET`

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

### `unset`

**Command:** `CMD_UNSET`

**Parse Function:** `parse_set()` in `config/set.c` (shared with `set`)

**Data Storage:**
- **Modifies:** `NeoMutt->sub->cs` (ConfigSet)
- **Action:** Resets variable to empty/NULL state
  - Bools: Set to false
  - Strings: Set to NULL/empty
  - Numbers: Set to 0

**Owner:** Global configuration subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `reset`

**Command:** `CMD_RESET`

**Parse Function:** `parse_set()` in `config/set.c` (shared with `set`)

**Data Storage:**
- **Modifies:** `NeoMutt->sub->cs` (ConfigSet)
- **Action:** Restores variable to its `initial` value from `struct ConfigDef`

**Owner:** Global configuration subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `toggle`

**Command:** `CMD_TOGGLE`

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

### `setenv`

**Command:** `CMD_SETENV`

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

### `unsetenv`

**Command:** `CMD_UNSETENV`

**Parse Function:** `parse_setenv()` in `commands/setenv.c` (shared parser)

**Data Storage:**
- **Removes from:** `NeoMutt->env` and system environment
- Calls `unsetenv(3)` to remove from process

**Owner:** Global NeoMutt environment

**Data Field:** `CMD_NO_DATA` (0)

### `source`

**Command:** `CMD_SOURCE`

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

### `finish`

**Command:** `CMD_FINISH`

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

### `ifdef`

**Command:** `CMD_IFDEF`

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

### `ifndef`

**Command:** `CMD_IFNDEF`

**Parse Function:** `parse_ifdef()` in `commands/ifdef.c` (shared parser)

**Data Storage:**
- Same as `ifdef`

**Owner:** Parser evaluation (transient)

**Behavior:**
- Inverse of `ifdef`
- If symbol NOT defined: Execute command
- If defined: Skip command

**Data Field:** `CMD_NO_DATA` (0)

## List Management

### `alternates`

**Command:** `CMD_ALTERNATES`

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

### `unalternates`

**Command:** `CMD_UNALTERNATES`

**Parse Function:** `parse_unalternates()` in `commands/alternates.c`

**Data Storage:**
- **Removes from:** `struct RegexList Alternates`
- **Pattern `*`:** Clears entire list

**Owner:** Global alternates subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `lists`

**Command:** `CMD_LISTS`

**Parse Function:** `parse_lists()` in `commands/group.c`

**Data Storage:**
- **Global List:** `struct RegexList MailLists`
- **Structure:** `struct RegexNode` with compiled regex

**Owner:** Global mailing list subsystem

**Additional Storage:**
- **Groups:** Can categorize lists via `-group` flag

**Purpose:** Recognize mailing list addresses

**Data Field:** `CMD_NO_DATA` (0)

### `unlists`

**Command:** `CMD_UNLISTS`

**Parse Function:** `parse_unlists()` in `commands/group.c`

**Data Storage:**
- **Removes from:** `struct RegexList MailLists`
- **Pattern `*`:** Clears entire list

**Owner:** Global mailing list subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `subscribe`

**Command:** `CMD_SUBSCRIBE`

**Parse Function:** `parse_subscribe()` in `commands/group.c`

**Data Storage:**
- **Global List:** `struct RegexList SubscribedLists`
- **Structure:** `struct RegexNode` with compiled regex

**Owner:** Global subscription subsystem

**Purpose:** Mark mailing lists user is subscribed to

**Data Field:** `CMD_NO_DATA` (0)

### `unsubscribe`

**Command:** `CMD_UNSUBSCRIBE`

**Parse Function:** `parse_unsubscribe()` in `commands/group.c`

**Data Storage:**
- **Removes from:** `struct RegexList SubscribedLists`
- **Pattern `*`:** Clears entire list

**Owner:** Global subscription subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `subscribe-to`

**Command:** `CMD_SUBSCRIBE_TO`

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

### `unsubscribe-from`

**Command:** `CMD_UNSUBSCRIBE_FROM`

**Parse Function:** `parse_unsubscribe_from()` in `nntp/commands.c`

**Data Storage:**
- **Modifies:** Same NNTP newsgroup data
- Sets `subscribed = false`

**Owner:** NNTP account data structure

**Data Field:** `CMD_NO_DATA` (0)

### `ignore`

**Command:** `CMD_IGNORE`

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

### `unignore`

**Command:** `CMD_UNIGNORE`

**Parse Function:** `parse_unignore()` in `commands/ignore.c`

**Data Storage:**
- **Removes from:** `struct ListHead Ignore`
- **Pattern `*`:** Clears entire ignore list (show all headers)

**Owner:** Global header display subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `hdr_order`

**Command:** `CMD_HDR_ORDER`

**Parse Function:** `parse_stailq()` in `commands/parse.c`

**Data Storage:**
- **Global List:** `struct ListHead HeaderOrderList`
- **Structure:** `struct ListNode` with header field names

**Owner:** Global header display subsystem

**Purpose:** Define order headers are displayed

**Data Field:** `IP &HeaderOrderList` (pointer to the list)

### `unhdr_order`

**Command:** `CMD_UNHDR_ORDER`

**Parse Function:** `parse_unstailq()` in `commands/parse.c`

**Data Storage:**
- **Removes from:** `HeaderOrderList`
- **Pattern `*`:** Clears entire list

**Owner:** Global header display subsystem

**Data Field:** `IP &HeaderOrderList` (pointer to the list)

## MIME and Attachment

### `alternative_order`

**Command:** `CMD_ALTERNATIVE_ORDER`

**Parse Function:** `parse_stailq()` in `commands/parse.c`

**Data Storage:**
- **Global List:** `struct ListHead AlternativeOrderList`
- **Structure:** `struct ListNode` containing:
  - `char *data` - MIME type (e.g., "text/plain")

**Owner:** Global MIME handler subsystem

**Purpose:** Set preference order for multipart/alternative

**Data Field:** `IP &AlternativeOrderList`

### `unalternative_order`

**Command:** `CMD_UNALTERNATIVE_ORDER`

**Parse Function:** `parse_unstailq()` in `commands/parse.c`

**Data Storage:**
- **Removes from:** `AlternativeOrderList`
- **Pattern `*`:** Clears entire list

**Owner:** Global MIME handler subsystem

**Data Field:** `IP &AlternativeOrderList`

### `auto_view`

**Command:** `CMD_AUTO_VIEW`

**Parse Function:** `parse_stailq()` in `commands/parse.c`

**Data Storage:**
- **Global List:** `struct ListHead AutoViewList`
- **Structure:** `struct ListNode` with MIME types

**Owner:** Global MIME handler subsystem

**Purpose:** MIME types to display automatically inline

**Data Field:** `IP &AutoViewList`

### `unauto_view`

**Command:** `CMD_UNAUTO_VIEW`

**Parse Function:** `parse_unstailq()` in `commands/parse.c`

**Data Storage:**
- **Removes from:** `AutoViewList`
- **Pattern `*`:** Clears entire list

**Owner:** Global MIME handler subsystem

**Data Field:** `IP &AutoViewList`

### `mime_lookup`

**Command:** `CMD_MIME_LOOKUP`

**Parse Function:** `parse_stailq()` in `commands/parse.c`

**Data Storage:**
- **Global List:** `struct ListHead MimeLookupList`
- **Structure:** `struct ListNode` with MIME types

**Owner:** Global MIME handler subsystem

**Purpose:** MIME types to look up via mailcap

**Data Field:** `IP &MimeLookupList`

### `unmime_lookup`

**Command:** `CMD_UNMIME_LOOKUP`

**Parse Function:** `parse_unstailq()` in `commands/parse.c`

**Data Storage:**
- **Removes from:** `MimeLookupList`
- **Pattern `*`:** Clears entire list

**Owner:** Global MIME handler subsystem

**Data Field:** `IP &MimeLookupList`

### `attachments`

**Command:** `CMD_ATTACHMENTS`

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

### `unattachments`

**Command:** `CMD_UNATTACHMENTS`

**Parse Function:** `parse_unattachments()` in `attach/commands.c`

**Data Storage:**
- **Removes from:** `AttachAllow`, `AttachExclude`, `InlineAllow`, `InlineExclude`
- **Pattern `*`:** Clears all attachment rules

**Owner:** Global attachment subsystem

**Data Field:** `CMD_NO_DATA` (0)

## Color and Display

### `color`

**Command:** `CMD_COLOR`

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

### `uncolor`

**Command:** `CMD_UNCOLOR`

**Parse Function:** `parse_uncolor()` in `color/commands.c`

**Data Storage:**
- **Removes from:** `ColorList[]` array
- **Pattern `*`:** Removes all patterns for specified object
- **Specific pattern:** Removes matching color rule

**Owner:** Global color subsystem

**Data Field:** `CMD_NO_DATA` (0)

**Notifications:** Sends `NT_COLOR` with color ID

### `mono`

**Command:** `CMD_MONO`

**Parse Function:** `parse_mono()` in `color/commands.c`

**Data Storage:**
- **Same as `color`** but only sets attributes (bold, underline, etc.)
- Uses same `ColorList[]` structure
- Foreground/background colors ignored on monochrome terminals

**Owner:** Global color subsystem

**Status:** Deprecated (use `color` instead)

**Data Field:** `CMD_NO_DATA` (0)

### `unmono`

**Command:** `CMD_UNMONO`

**Parse Function:** `parse_unmono()` in `color/commands.c`

**Data Storage:**
- **Removes from:** `ColorList[]` array
- Same removal logic as `uncolor`

**Owner:** Global color subsystem

**Status:** Deprecated (use `uncolor` instead)

**Data Field:** `CMD_NO_DATA` (0)

## Scoring and Spam

### `score`

**Command:** `CMD_SCORE`

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

### `unscore`

**Command:** `CMD_UNSCORE`

**Parse Function:** `parse_unscore()` in `commands/score.c`

**Data Storage:**
- **Removes from:** `struct ScoreList Scores`
- **Pattern `*`:** Clears all scoring rules

**Owner:** Global scoring subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `spam`

**Command:** `CMD_SPAM`

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

### `nospam`

**Command:** `CMD_NOSPAM`

**Parse Function:** `parse_nospam()` in `commands/spam.c`

**Data Storage:**
- **Removes from:** `struct ReplaceList SpamList`
- **Pattern `*`:** Clears all spam rules

**Owner:** Global spam detection subsystem

**Data Field:** `CMD_NO_DATA` (0)

## Group and Address Management

### `group`

**Command:** `CMD_GROUP`

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

### `ungroup`

**Command:** `CMD_UNGROUP`

**Parse Function:** `parse_group()` in `commands/group.c` (shared parser)

**Data Storage:**
- **Removes from:** `NeoMutt->groups`
- **Pattern `*`:** Removes all addresses/patterns from group
- **Specific:** Removes matching addresses or patterns

**Owner:** Global group subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `my_hdr`

**Command:** `CMD_MY_HDR`

**Parse Function:** `parse_my_hdr()` in `commands/my_hdr.c`

**Data Storage:**
- **Global List:** `struct ListHead UserHeader`
- **Structure:** `struct ListNode` containing:
  - `char *data` - Complete header line ("Name: value")

**Owner:** Global custom header subsystem

**Purpose:** Add custom headers to outgoing messages

**Data Field:** `CMD_NO_DATA` (0)

### `unmy_hdr`

**Command:** `CMD_UNMY_HDR`

**Parse Function:** `parse_unmy_hdr()` in `commands/my_hdr.c`

**Data Storage:**
- **Removes from:** `struct ListHead UserHeader`
- **Pattern `*`:** Removes all custom headers
- **Field name:** Removes headers starting with specified field

**Owner:** Global custom header subsystem

**Data Field:** `CMD_NO_DATA` (0)

## Mailbox Management

### `mailboxes`

**Command:** `CMD_MAILBOXES`

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

### `named-mailboxes`

**Command:** `CMD_NAMED_MAILBOXES`

**Parse Function:** `parse_mailboxes()` in `commands/mailboxes.c` (shared)

**Data Storage:**
- **Same as `mailboxes`** but requires explicit labels
- Syntax: `named-mailboxes <label> <path> [<label> <path> ...]`

**Owner:** Global mailbox subsystem

**Difference from `mailboxes`:**
- Must provide label for each mailbox
- Cannot use flags like `-label`, `-notify`, `-poll`

**Data Field:** `CMD_NO_DATA` (0)

### `unmailboxes`

**Command:** `CMD_UNMAILBOXES`

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

## Tag Transform

### `tag-formats`

**Command:** `CMD_TAG_FORMATS`

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

### `tag-transforms`

**Command:** `CMD_TAG_TRANSFORMS`

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

### `subjectrx`

**Command:** `CMD_SUBJECTRX`

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

### `unsubjectrx`

**Command:** `CMD_UNSUBJECTRX`

**Parse Function:** `parse_unsubjectrx_list()` in `commands/subjectrx.c`

**Data Storage:**
- **Removes from:** `SubjectRegexList`
- **Pattern `*`:** Clears all subject rewriting rules
- **Specific regex:** Removes matching rule

**Owner:** Global subject rewriting subsystem

**Data Field:** `CMD_NO_DATA` (0)

## Mailto and Sidebar

### `mailto_allow`

**Command:** `CMD_MAILTO_ALLOW`

**Parse Function:** `parse_stailq()` in `commands/parse.c`

**Data Storage:**
- **Global List:** `struct ListHead MailToAllow`
- **Structure:** `struct ListNode` with allowed header field names

**Owner:** Global mailto handler subsystem

**Purpose:** Whitelist header fields allowed in `mailto: ` URLs

**Security:** Prevents arbitrary headers being set via mailto links

**Data Field:** `IP &MailToAllow`

### `unmailto_allow`

**Command:** `CMD_UNMAILTO_ALLOW`

**Parse Function:** `parse_unstailq()` in `commands/parse.c`

**Data Storage:**
- **Removes from:** `MailToAllow`
- **Pattern `*`:** Clears entire whitelist (blocks all extra headers)

**Owner:** Global mailto handler subsystem

**Data Field:** `IP &MailToAllow`

### `sidebar_pin`

**Command:** `CMD_SIDEBAR_PIN`

**Parse Function:** `parse_sidebar_pin()` in `sidebar/commands.c`

**Data Storage:**
- **Global List:** `struct ListHead SidebarPinned`
- **Structure:** `struct ListNode` containing:
  - `char *data` - Mailbox path to pin

**Owner:** Sidebar subsystem

**Purpose:** Pin mailboxes to top of sidebar (always visible)

**Data Field:** `CMD_NO_DATA` (0)

**Note:** Sidebar support must be compiled in

### `sidebar_unpin`

**Command:** `CMD_SIDEBAR_UNPIN`

**Parse Function:** `parse_sidebar_unpin()` in `sidebar/commands.c`

**Data Storage:**
- **Removes from:** `SidebarPinned`
- **Pattern `*`:** Unpins all mailboxes

**Owner:** Sidebar subsystem

**Data Field:** `CMD_NO_DATA` (0)

## Utility and Information

### `cd`

**Command:** `CMD_CD`

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

### `echo`

**Command:** `CMD_ECHO`

**Parse Function:** `parse_echo()` in `commands/parse.c`

**Data Storage:**
- **No persistent storage**
- **Action:** Displays message to status line via `mutt_message()`

**Owner:** Message window (transient)

**Behavior:**
- Expands variables and expandos in message
- Message displayed until next screen update

**Data Field:** `CMD_NO_DATA` (0)

### `version`

**Command:** `CMD_VERSION`

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

### `hooks`

**Command:** `CMD_HOOKS`

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

### `lua`

**Command:** `CMD_LUA`

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

### `lua-source`

**Command:** `CMD_LUA_SOURCE`

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

### `append-hook`

**Command:** `CMD_APPEND_HOOK`

**Parse Function:** `parse_hook_folder()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_APPEND_HOOK`
- **Structure:** `struct Hook` with:
  - `struct Regex *regex` - Folder pattern
  - `char *command` - Commands to execute when appending to folder

**Owner:** Global hooks subsystem

**Data Field:** `CMD_NO_DATA` (0)

### `close-hook`

**Command:** `CMD_CLOSE_HOOK`

**Parse Function:** `parse_hook_folder()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_CLOSE_HOOK`
- **Structure:** Same as `append-hook`

**Owner:** Global hooks subsystem

**Purpose:** Execute commands when closing a folder

**Data Field:** `CMD_NO_DATA` (0)

### `open-hook`

**Command:** `CMD_OPEN_HOOK`

**Parse Function:** `parse_hook_folder()` in `hooks/parse.c`

**Data Storage:**
- **Global List:** `Hooks` array with type `MUTT_OPEN_HOOK`
- **Structure:** Same as `append-hook`

**Owner:** Global hooks subsystem

**Purpose:** Execute commands when opening a folder

**Data Field:** `CMD_NO_DATA` (0)

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

