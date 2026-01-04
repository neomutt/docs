# Menu Developer Documentation

## Overview

The Menu is a core component of NeoMutt that provides a selectable list interface for displaying items. It acts as a **virtual window** over the caller's data - the Menu itself doesn't store any data, but rather provides a viewport and interaction layer for external data sources.

## Architecture

### Key Concepts

1. **Virtual Window**: The Menu is a viewport that displays a subset of items (a "page") from a larger dataset
2. **Data Separation**: The Menu doesn't own the data it displays; data is stored in `Menu:: mdata`
3. **Callback-Driven**: The Menu uses function pointers (MenuAPI) to interact with caller data
4. **Viewport Management**: The Menu manages `top` (first visible item) and `current` (selected item) indices

### Menu Structure

```c
struct Menu {
  int current;              // Currently selected item
  int max;                  // Total number of entries
  int top;                  // First visible entry (top of viewport)
  int page_len;             // Number of visible entries per screen
  
  // Function pointers (MenuAPI)
  int (*make_entry)(struct Menu *menu, int line, int max_cols, struct Buffer *buf);
  int (*search)(struct Menu *menu, regex_t *rx, int line);
  int (*tag)(struct Menu *menu, int sel, int act);
  const struct AttrColor *(*color)(struct Menu *menu, int line);
  
  void *mdata;              // Caller's private data
  void (*mdata_free)(struct Menu *menu, void **ptr);
  
  struct MuttWindow *win;   // Associated window
  struct ConfigSubset *sub; // Config items
  enum MenuType type;       // Menu type (MENU_INDEX, MENU_ALIAS, etc.)
};
```

## Creating a Menu and MuttWindow

### Step 1: Create the Menu Window

```c
#include "menu/lib.h"

// Create a new Menu Window
struct MuttWindow *menu_win = menu_window_new(MENU_GENERIC, NeoMutt->sub);
struct Menu *menu = menu_win->wdata;
```

### Step 2: Set Up Menu Data

```c
// Allocate your data structure
struct MyMenuData *mdata = MUTT_MEM_CALLOC(1, struct MyMenuData);

// Attach it to the menu
menu->mdata = mdata;
menu->mdata_free = my_menu_data_free;  // Optional cleanup function

// Set the number of items
menu->max = my_item_count;
```

### Step 3: Implement MenuAPI Functions

Set the callback functions to connect your data to the Menu:

```c
menu->make_entry = my_make_entry;
menu->search = my_search;      // Optional
menu->tag = my_tag;            // Optional, for tagging support
menu->color = my_color;        // Optional, for custom colors
```

## MenuAPI Functions

### 1. `make_entry()` - Generate Text for a Line

**Purpose**: Format a single menu line for display. 

**Signature**:
```c
int make_entry(struct Menu *menu, int line, int max_cols, struct Buffer *buf);
```

**Parameters**:
- `menu`: The Menu containing items
- `line`: Menu line number (0-based index into your data)
- `max_cols`: Maximum column width available, or -1 for unlimited
- `buf`: Output buffer to write formatted text

**Return Value**:  Number of display columns used (screen width, not bytes)

**Example Implementation**:
```c
static int my_make_entry(struct Menu *menu, int line, int max_cols, struct Buffer *buf)
{
  struct MyMenuData *mdata = menu->mdata;
  struct MyItem *item = ARRAY_GET(&mdata->items, line);
  
  if (! item)
    return 0;
  
  // Account for arrow cursor width if enabled
  const bool c_arrow_cursor = cs_subset_bool(menu->sub, "arrow_cursor");
  if (c_arrow_cursor)
  {
    const char *const c_arrow_string = cs_subset_string(menu->sub, "arrow_string");
    if (max_cols > 0)
      max_cols -= (mutt_strwidth(c_arrow_string) + 1);
  }
  
  // Format the entry using expando or manual formatting
  const struct Expando *c_my_format = cs_subset_expando(menu->sub, "my_format");
  return expando_filter(c_my_format, MyRenderCallbacks, item,
                        MUTT_FORMAT_ARROWCURSOR, max_cols, NeoMutt->env, buf);
}
```

### 2. `search()` - Custom Search Implementation

**Purpose**:  Determine if a line matches a search pattern.

**Signature**:
```c
int search(struct Menu *menu, regex_t *rx, int line);
```

**Parameters**:
- `menu`: The Menu containing items
- `rx`: Compiled regex pattern to match
- `line`: Line number to test

**Return Value**: Return value from `regexec()` (0 = match, non-zero = no match)

**Example Implementation**:
```c
static int my_search(struct Menu *menu, regex_t *rx, int line)
{
  struct MyMenuData *mdata = menu->mdata;
  struct MyItem *item = ARRAY_GET(&mdata->items, line);
  
  if (!item)
    return REG_NOMATCH;
  
  // Search in item's searchable fields
  if (regexec(rx, item->name, 0, NULL, 0) == 0)
    return 0;
  
  if (regexec(rx, item->description, 0, NULL, 0) == 0)
    return 0;
  
  return REG_NOMATCH;
}
```

**Note**: If you don't provide a custom `search()`, the Menu will use a generic search that calls `make_entry()` and searches the formatted text.

### 3. `tag()` - Multiple Selection Support

**Purpose**: Tag or untag items for batch operations.

**Signature**: 
```c
int tag(struct Menu *menu, int sel, int act);
```

**Parameters**:
- `menu`: The Menu containing items
- `sel`: Index of item to tag
- `act`: Action to perform: 
  - `0` = untag
  - `1` = tag
  - `-1` = toggle

**Return Value**: Net change in number of tagged items (+1, 0, or -1)

**Example Implementation**:
```c
static int my_tag(struct Menu *menu, int sel, int act)
{
  struct MyMenuData *mdata = menu->mdata;
  struct MyItem *item = ARRAY_GET(&mdata->items, sel);
  
  if (!item)
    return 0;
  
  bool old_tagged = item->is_tagged;
  
  // Apply the action
  if (act >= 0)
    item->is_tagged = (act == 1);
  else
    item->is_tagged = !item->is_tagged;
  
  // Return the change
  return (int)item->is_tagged - (int)old_tagged;
}
```

### 4. `color()` - Set Default Color for a Line

**Purpose**:  Determine the color/attributes for a menu line.

**Signature**: 
```c
const struct AttrColor *color(struct Menu *menu, int line);
```

**Parameters**:
- `menu`: The Menu containing items
- `line`: Line number to colorize

**Return Value**: Pointer to AttrColor structure, or NULL for default

**Example Implementation**: 
```c
static const struct AttrColor *my_color(struct Menu *menu, int line)
{
  struct MyMenuData *mdata = menu->mdata;
  struct MyItem *item = ARRAY_GET(&mdata->items, line);
  
  if (!item)
    return simple_color_get(MT_COLOR_NORMAL);
  
  // Color based on item state
  if (item->is_deleted)
    return simple_color_get(MT_COLOR_DELETED);
  
  if (item->is_new)
    return simple_color_get(MT_COLOR_NEW);
  
  // Default color
  return simple_color_get(MT_COLOR_NORMAL);
}
```

## Virtual Window Concept

The Menu acts as a **virtual window** over your data: 

```
Your Data Array (100 items):
┌─────────────────────────────┐
│ Item 0                      │
│ Item 1                      │
│ ...                         │
│ Item 42  ← menu->top        │ ┌───────────────────┐
│ Item 43                     │ │ Item 42           │ ← Displayed
│ Item 44                     │ │ Item 43           │
│ Item 45  ← menu->current    │ │ Item 45 (selected)│
│ Item 46                     │ │ Item 46           │
│ Item 47                     │ │ Item 47           │
│ ...                         │ └───────────────────┘
│ Item 99                     │   5 visible items
└─────────────────────────────┘   (menu->page_len)
```

- **`menu->max`**: Total number of items in your data (100)
- **`menu->top`**: Index of first visible item (42)
- **`menu->page_len`**: Number of items visible on screen (5)
- **`menu->current`**: Currently selected item (45)

The Menu doesn't copy or store your data.  When it needs to display a line, it calls your `make_entry()` function with the line number. 

## Viewport Functions

### Movement Functions that Change Selection

These functions change `menu->current` and may adjust `menu->top`:

- `menu_top_page()` - Move selection to top of current page
- `menu_middle_page()` - Move selection to middle of current page
- `menu_bottom_page()` - Move selection to bottom of current page
- `menu_prev_entry()` - Move selection up one item
- `menu_next_entry()` - Move selection down one item
- `menu_first_entry()` - Move selection to first item (index 0)
- `menu_last_entry()` - Move selection to last item (index max-1)

### Movement Functions that Change View

These functions change `menu->top` and may adjust `menu->current`:

- `menu_current_top()` - Scroll view to put current selection at top
- `menu_current_middle()` - Scroll view to put current selection at middle
- `menu_current_bottom()` - Scroll view to put current selection at bottom
- `menu_half_up()` - Scroll view up by half a page
- `menu_half_down()` - Scroll view down by half a page
- `menu_prev_line()` - Scroll view up by one line
- `menu_next_line()` - Scroll view down by one line
- `menu_prev_page()` - Scroll view up by one page
- `menu_next_page()` - Scroll view down by one page

### Setting Selection Programmatically

```c
// Set the selected item
menu_set_index(menu, new_index);

// Or use the underlying function with explicit notification
menu_set_and_notify(menu, new_top, new_current);
```

## Menu Configuration Options

The Menu behavior is controlled by several config variables:

### `$menu_context` (Number, default: 0)

Controls the number of lines of "context" kept visible when scrolling: 

```
menu_context = 2: 

┌───────────────┐      User presses       ┌───────────────┐
│ Item 5        │         DOWN            │ Item 6        │
│ Item 6        │      (page down)        │ Item 7        │
│ Item 7 ←sel   │         ───→            │ Item 8        │
│ Item 8        │                         │ Item 9 ←sel   │
│ Item 9        │                         │ Item 10       │
└───────────────┘                         └───────────────┘
    
    Items 6-7 remain visible (2 lines of context)
```

- **Value**: Number of lines (max:  page_len / 2)
- **Effect**: When scrolling, this many lines remain visible from the previous view
- **Similar to**: `$pager_context`

### `$menu_scroll` (Boolean, default: false)

Controls whether menus scroll line-by-line or page-by-page:

- **false** (default): Jumping to a line off-screen clears and redraws a new page
- **true**: Menu scrolls smoothly one line at a time

```
menu_scroll = false:          menu_scroll = true:
Page boundaries matter        Smooth scrolling

┌───────────┐                 ┌───────────┐
│ Item 0    │  Press          │ Item 1    │
│ Item 1    │  DOWN at        │ Item 2    │
│ Item 2    │  bottom         │ Item 3    │
│ Item 3    │  ───→           │ Item 4    │
│ Item 4←sel│                 │ Item 5←sel│
└───────────┘                 └───────────┘
     ↓                             ↓
┌───────────┐                 ┌───────────┐
│ Item 5←sel│                 │ Item 2    │
│ Item 6    │                 │ Item 3    │
│ Item 7    │                 │ Item 4    │
│ Item 8    │                 │ Item 5    │
│ Item 9    │                 │ Item 6←sel│
└───────────┘                 └───────────┘
 (new page)                   (scrolled 1 line)
```

### `$menu_move_off` (Boolean, default: true)

Controls whether the last item can scroll off the bottom: 

- **true** (default): Last entry can move off bottom of screen
- **false**: Last entry stays anchored to bottom (when possible)

```
menu_move_off = true:         menu_move_off = false: 

┌────────────┐                 ┌────────────┐
│ Item 6     │                 │ Item 6     │
│ Item 7     │                 │ Item 7     │
│ Item 8     │                 │ Item 8     │
│ Item 9     │                 │ Item 9←sel │
│ Item 10←sel│ (last item)     │ Item 10    │ (last item)
└────────────┘                 └────────────┘
Can scroll to:                 Cannot scroll past:
┌────────────┐                 ┌────────────┐
│ Item 10←sel│                 │ Item 9     │
│            │                 │ Item 10←sel│
│            │                 │            │
│            │                 │            │
│            │                 │            │
└────────────┘                 └────────────┘
```

### `$arrow_cursor` (Boolean, default: false)

Controls cursor display style:

- **false**:  Highlight entire line
- **true**: Show arrow indicator (see `$arrow_string`)

### `$arrow_string` (String, default: "->")

Custom string for arrow cursor mode. 

## Redraw Flags

The Menu uses flags to optimize redraws:

- `MENU_REDRAW_NO_FLAGS` - No redraw needed
- `MENU_REDRAW_INDEX` - Redraw all visible entries
- `MENU_REDRAW_MOTION` - Redraw after cursor movement (old and new positions)
- `MENU_REDRAW_CURRENT` - Redraw only the current entry
- `MENU_REDRAW_FULL` - Complete redraw of menu

Queue a redraw: 
```c
menu_queue_redraw(menu, MENU_REDRAW_INDEX);
```

## Complete Example

Here's a complete example of creating a simple menu:

```c
// Data structure
struct MyMenuData {
  struct StringArray items;
};

// make_entry callback
static int my_make_entry(struct Menu *menu, int line, int max_cols, struct Buffer *buf)
{
  struct MyMenuData *mdata = menu->mdata;
  const char *item = ARRAY_GET(&mdata->items, line);
  
  if (!item)
    return 0;
  
  buf_strcpy(buf, item);
  return mutt_strwidth(item);
}

// Cleanup callback
static void my_mdata_free(struct Menu *menu, void **ptr)
{
  struct MyMenuData *mdata = *ptr;
  ARRAY_FREE(&mdata->items);
  FREE(ptr);
}

// Create and use the menu
void create_my_menu(void)
{
  // Create menu window
  struct MuttWindow *menu_win = menu_window_new(MENU_GENERIC, NeoMutt->sub);
  struct Menu *menu = menu_win->wdata;
  
  // Set up data
  struct MyMenuData *mdata = MUTT_MEM_CALLOC(1, struct MyMenuData);
  ARRAY_INIT(&mdata->items);
  ARRAY_ADD(&mdata->items, "Item 1");
  ARRAY_ADD(&mdata->items, "Item 2");
  ARRAY_ADD(&mdata->items, "Item 3");
  
  // Attach to menu
  menu->mdata = mdata;
  menu->mdata_free = my_mdata_free;
  menu->max = ARRAY_SIZE(&mdata->items);
  menu->make_entry = my_make_entry;
  
  // Menu is ready to use
  // ... event loop, etc.
}
```

## Best Practices

1. **Always validate line numbers** in MenuAPI callbacks - check bounds before accessing data
2. **Account for arrow_cursor** in `make_entry()` when calculating max_cols
3. **Keep data in sync** - update `menu->max` when your data changes
4. **Use menu_queue_redraw()** - don't manually set redraw flags
5. **Implement search()** for better performance on large datasets (optional)
6. **Implement color()** for visual feedback based on item state (optional)
7. **Free resources** - implement `mdata_free()` if you allocate data

## See Also

- Source files: `menu/*. c` and `menu/lib. h`
- Example implementations: `index/`, `alias/`, `attach/`, `postpone/` directories
- Window system: `gui/mutt_window.h`
- Configuration: `menu/config.c`
