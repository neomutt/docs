# Expando System Developer Documentation

## Overview

The Expando system in NeoMutt is a powerful framework for parsing and rendering format strings with dynamic data.  Expandos are placeholders (like `%s`, `%n`, `%{name}`) that get replaced with actual data at runtime.  The system is located in the `expando/` directory.

## How Expandos are Defined

### Core Data Structures

Expandos are defined using the `ExpandoDefinition` structure:

```c
struct ExpandoDefinition
{
  const char           *short_name;      ///< Short Expando name, e.g. "n"
  const char           *long_name;       ///< Long Expando name, e.g. "name"
  short                 did;             ///< Domain ID
  short                 uid;             ///< Unique ID in domain
  
  struct ExpandoNode *(*parse)(const char *str, struct ExpandoFormat *fmt, 
                               int did, int uid, ExpandoParserFlags flags, 
                               const char **parsed_until, 
                               struct ExpandoParseError *err);
};
```

**Key fields:**
- `short_name`: Single-character name used like `%n`
- `long_name`: Multi-character name used like `%{name}`
- `did`: Domain ID (groups related expandos together, e.g., `ED_EMAIL`, `ED_ENVELOPE`)
- `uid`: Unique identifier within the domain (e.g., `ED_EMA_SIZE`, `ED_ENV_FROM`)
- `parse`: Optional custom parser function for complex expandos

### Example Definition

```c
static const struct ExpandoDefinition TestFormatDef[] = {
  // short_name, long_name, domain_id, unique_id, parse_function
  { "a",  "apple",  1, 2, NULL },
  { "b",  "banana", 1, 3, NULL },
  { "c",  "cherry", 1, 4, parse_custom },
  { NULL, NULL, 0, -1, NULL }  // Terminator
};
```

### Expando Nodes

Once parsed, expandos become nodes in a tree structure:

```c
struct ExpandoNode
{
  enum ExpandoNodeType      type;        ///< Type:  ENT_EXPANDO, ENT_TEXT, ENT_CONDITION, etc.
  int                       did;         ///< Domain ID
  int                       uid;         ///< Unique ID
  struct ExpandoFormat     *format;      ///< Formatting info (padding, justification)
  const char               *text;        ///< Node-specific text
  struct ExpandoNodeArray   children;    ///< Children nodes
  void  *ndata;                          ///< Private node data
  int (*render)(/*...*/);                ///< Render function
};
```

**Node Types:**
- `ENT_EXPANDO`: Standard expando placeholder
- `ENT_TEXT`: Plain text
- `ENT_CONDITION`: Conditional expando (`%<X?true&false>`)
- `ENT_CONDBOOL`: Boolean condition
- `ENT_CONDDATE`: Date-based condition
- `ENT_PADDING`: Padding characters
- `ENT_CONTAINER`: Container for other nodes

---

## How Parsing Works

### Overview

Parsing converts a format string like `"%a %b %<c? yes&no>"` into a tree of `ExpandoNode` objects.

### Main Parsing Function

```c
struct Expando *expando_parse(const char *str, 
                              const struct ExpandoDefinition *defs,
                              struct Buffer *err)
```

**Process:**

1. **Create Expando Object**: Initialize with the format string
   ```c
   struct Expando *exp = expando_new(str);
   ```

2. **Parse Nodes**: Parse the string into a tree of nodes
   ```c
   node_parse_many(exp->node, str, NTE_NO_FLAGS, defs, &parsed_until, &error);
   ```

3. **Optimize Tree**:  Simplify the tree structure
   ```c
   node_padding_repad(&exp->node);
   node_container_collapse_all(&exp->node);
   ```

### Node Parsing

The `node_expando_parse()` function handles individual expando parsing:

```c
struct ExpandoNode *node_expando_parse(const char *str, 
                                       const struct ExpandoDefinition *defs,
                                       ExpandoParserFlags flags, 
                                       const char **parsed_until,
                                       struct ExpandoParseError *err)
```

**Steps:**

1. **Skip '%' character**: All expandos start with `%`

2. **Parse format specifiers**: Optional printf-style formatting like `%-20. 10`
   ```c
   struct ExpandoFormat *fmt = parse_format(str, parsed_until, err);
   ```
   - Format includes: min_cols, max_cols, justification, leader character, lowercase flag

3. **Parse expando name**: Match short name or long name
   ```c
   struct ExpandoNode *node = parse_short_name(str, defs, flags, fmt, parsed_until, err);
   ```

4. **Create node**: If found, create an `ExpandoNode`
   ```c
   return node_expando_new(fmt, def->did, def->uid);
   ```

### Short Name vs Long Name

**Short name** (`%a`):
- Single character after `%`
- Parsed by `parse_short_name()`

**Long name** (`%{apple}`):
- Wrapped in curly braces
- Parsed by `parse_long_name()`

### Custom Parsers

Some expandos need custom parsing (e.g., date formats with `%[...]`):

```c
struct ExpandoNode *parse_custom(const char *str, struct ExpandoFormat *fmt,
                                 int did, int uid, ExpandoParserFlags flags,
                                 const char **parsed_until,
                                 struct ExpandoParseError *err)
{
  // Custom parsing logic
  *parsed_until = str + parsed_length;
  return node_expando_new(fmt, did, uid);
}
```

### Enclosures

Expandos can be enclosed with terminators (e.g., `%[apple]`):

```c
struct ExpandoNode *node_expando_parse_enclosure(const char *str, int did, int uid, 
                                                 char terminator,
                                                 struct ExpandoFormat *fmt,
                                                 const char **parsed_until,
                                                 struct ExpandoParseError *err)
```

---

## How Callbacks Work

### Overview

Callbacks provide the actual data to fill in expandos. There are two types:  **string callbacks** and **number callbacks**.

### Callback Structure

```c
struct ExpandoRenderCallback
{
  int did;                  ///< Domain ID
  int uid;                  ///< Unique ID
  get_string_t get_string;  ///< Callback to get string data
  get_number_t get_number;  ///< Callback to get numeric data
};
```

### String Callbacks

**Signature:**
```c
typedef void (*get_string_t)(const struct ExpandoNode *node, 
                             void *data, 
                             MuttFormatFlags flags, 
                             struct Buffer *buf);
```

**Example:**
```c
static void alias_name(const struct ExpandoNode *node, void *data,
                       MuttFormatFlags flags, struct Buffer *buf)
{
  const struct AliasView *av = data;
  const char *s = av->alias->name;
  buf_strcpy(buf, s);
}
```

### Number Callbacks

**Signature:**
```c
typedef long (*get_number_t)(const struct ExpandoNode *node, 
                             void *data, 
                             MuttFormatFlags flags);
```

**Example:**
```c
static long alias_number(const struct ExpandoNode *node, void *data, 
                         MuttFormatFlags flags)
{
  const struct AliasView *av = data;
  return av->num + 1;
}
```

### Registering Callbacks

Callbacks are registered in an array, matched by `did` and `uid`:

```c
const struct ExpandoRenderCallback AliasRenderCallbacks[] = {
  // Domain ID,   Unique ID,       String Callback,  Number Callback
  { ED_ALIAS,     ED_ALI_NAME,     alias_name,       NULL },
  { ED_ALIAS,     ED_ALI_NUMBER,   NULL,             alias_number },
  { ED_ALIAS,     ED_ALI_TAGGED,   alias_tagged,     alias_tagged_num },
  { -1, -1, NULL, NULL },  // Terminator
};
```

### Callback Lookup During Rendering

When rendering, the system looks up callbacks by DID/UID:

```c
// Try to find string callback first
const struct ExpandoRenderCallback *erc_match = find_get_string(erc, node->did, node->uid);
if (erc_match)
{
  erc_match->get_string(node, data, flags, buf_expando);
}
else
{
  // Fall back to number callback
  erc_match = find_get_number(erc, node->did, node->uid);
  const long num = erc_match->get_number(node, data, flags);
  buf_printf(buf_expando, "%ld", num);
}
```

### String vs Number Preference

The system **prefers string callbacks** over number callbacks.  This allows dates to be stored as timestamps (numbers) but displayed as formatted strings.

### Rendering Process

```c
int expando_render(const struct Expando *exp, 
                   const struct ExpandoRenderCallback *erc,
                   void *data, 
                   MuttFormatFlags flags, 
                   int max_cols, 
                   struct Buffer *buf)
```

1.  Traverse the expando tree
2. For each node, find the matching callback by DID/UID
3. Call the callback with the user data
4. Apply formatting (padding, justification, lowercase)
5. Append to output buffer

---

## How Conditional Expandos Work

### Overview

Conditional expandos display different content based on a condition. They come in three flavors:

1. **Boolean conditions**: `%<X?true_text&false_text>`
2. **Date conditions**: `%<[3m? recent&old>` (within 3 months?)
3. **Old-style conditionals**: `%?X?true_text&false_text? `

### Structure

A conditional expando has three parts:

```c
enum ENCondition
{
  ENC_CONDITION,      ///< The condition to test
  ENC_TRUE,           ///< Content if true
  ENC_FALSE,          ///< Content if false
};
```

### Parsing Conditional Expandos

```c
struct ExpandoNode *node_condition_parse(const char *str, 
                                         NodeTextTermFlags term_chars,
                                         const struct ExpandoDefinition *defs,
                                         const char **parsed_until,
                                         struct ExpandoParseError *err)
```

**Format:** `%<X?true_text&false_text>`

**Steps:**

1. **Parse format** (optional): `%-20<X?... >`
   ```c
   fmt = parse_format(str, parsed_until, err);
   ```

2. **Detect old vs new style**:
   - Old: `%?X?...? `
   - New: `%<X?...>`

3. **Parse condition node**:  The expando that determines true/false
   ```c
   node_cond = parse_short_name(str, defs, EP_CONDITIONAL, NULL, parsed_until, err);
   ```

4. **Convert to boolean node** if needed: 
   ```c
   if (node_cond->type == ENT_EXPANDO)
   {
     node_cond->type = ENT_CONDBOOL;
     node_cond->render = node_condbool_render;
   }
   ```

5. **Parse true clause**: Text between `?` and `&`
   ```c
   node_true = node_container_new();
   node_parse_many(node_true, str, term_true, defs, parsed_until, err);
   ```

6. **Parse false clause** (optional): Text after `&`
   ```c
   if (str[0] == '&')
   {
     node_false = node_container_new();
     node_parse_many(node_false, str, term_false, defs, parsed_until, err);
   }
   ```

7. **Check terminator**: `>` for new style, `?` for old style

8. **Create condition node**:
   ```c
   return node_condition_new(node_cond, node_true, node_false, fmt);
   ```

### Rendering Conditional Expandos

```c
static int node_condition_render(const struct ExpandoNode *node,
                                 const struct ExpandoRenderCallback *erc,
                                 struct Buffer *buf, int max_cols, 
                                 void *data, MuttFormatFlags flags)
```

**Process:**

1. **Evaluate condition**:  Render the condition node and use return value as boolean
   ```c
   const struct ExpandoNode *node_cond = node_get_child(node, ENC_CONDITION);
   int rc_cond = node_cond->render(node_cond, erc, buf_cond, max_cols, data, flags);
   ```

2. **Choose branch**:  Render true or false node based on condition
   ```c
   if (rc_cond == true)
   {
     const struct ExpandoNode *node_true = node_get_child(node, ENC_TRUE);
     rc = node_render(node_true, erc, buf_cond, max_cols, data, flags);
   }
   else
   {
     const struct ExpandoNode *node_false = node_get_child(node, ENC_FALSE);
     rc = node_render(node_false, erc, buf_cond, max_cols, data, flags);
   }
   ```

3. **Apply formatting**: Apply any format specifications to the result

### Boolean Conditions

**Rendering:**
```c
int node_condbool_render(const struct ExpandoNode *node,
                         const struct ExpandoRenderCallback *erc, 
                         struct Buffer *buf,
                         int max_cols, void *data, MuttFormatFlags flags)
```

1. Try number callback first: 
   ```c
   const struct ExpandoRenderCallback *erc_match = find_get_number(erc, node->did, node->uid);
   if (erc_match)
   {
     const long num = erc_match->get_number(node, data, flags);
     return (num != 0); // Convert to boolean
   }
   ```

2. Try string callback:
   ```c
   erc_match = find_get_string(erc, node->did, node->uid);
   if (erc_match)
   {
     erc_match->get_string(node, data, flags, buf_str);
     return (buf_len(buf_str) > 0); // Non-empty = true
   }
   ```

### Date Conditions

**Format:** `%<[Nm? true&false>` where: 
- `N` = number of time periods
- `m` = period type:  `y` (year), `m` (month), `w` (week), `d` (day), `H` (hour), `M` (minute)

**Examples:**
- `%<[3m?recent&old>` - True if within 3 months
- `%<[1d?today&older>` - True if within 1 day

**Private data:**
```c
struct NodeCondDatePrivate
{
  int    count;         ///< Number of units (e.g., 3)
  char   period;        ///< Period type (e.g., 'm')
};
```

**Rendering:**
1. Calculate cutoff time based on count and period
2. Get date from data via callback
3. Compare date to cutoff
4. Return true/false

---

## Complete Example

### Define Expandos

```c
static const struct ExpandoDefinition EmailFormatDef[] = {
  { "s",  "subject",  ED_EMAIL, ED_EMA_SUBJECT, NULL },
  { "f",  "from",     ED_EMAIL, ED_EMA_FROM,    NULL },
  { "n",  "number",   ED_EMAIL, ED_EMA_NUMBER,  NULL },
  { NULL, NULL, 0, -1, NULL }
};
```

### Implement Callbacks

```c
static void email_subject(const struct ExpandoNode *node, void *data,
                          MuttFormatFlags flags, struct Buffer *buf)
{
  const struct Email *email = data;
  buf_strcpy(buf, email->env->subject);
}

static long email_number(const struct ExpandoNode *node, void *data, 
                         MuttFormatFlags flags)
{
  const struct Email *email = data;
  return email->index + 1;
}

const struct ExpandoRenderCallback EmailRenderCallbacks[] = {
  { ED_EMAIL, ED_EMA_SUBJECT, email_subject, NULL },
  { ED_EMAIL, ED_EMA_NUMBER,  NULL,          email_number },
  { -1, -1, NULL, NULL },
};
```

### Parse and Render

```c
// Parse format string
const char *format = "%n %-30. 30s %<f?From:  %f>";
struct Buffer *err = buf_pool_get();
struct Expando *exp = expando_parse(format, EmailFormatDef, err);

// Render with data
struct Email *email = /* ... */;
struct Buffer *output = buf_pool_get();
expando_render(exp, EmailRenderCallbacks, email, 
               MUTT_FORMAT_NO_FLAGS, 80, output);

// Output:  "1 Email subject here           From: sender@example.com"
```

---

## Key Files Reference

- `expando/definition.h` - Expando definitions
- `expando/expando.c` - Main parsing and rendering
- `expando/node_expando.c` - Expando node implementation
- `expando/node_condition.c` - Conditional expando implementation
- `expando/node_condbool.c` - Boolean condition implementation
- `expando/node_conddate.c` - Date condition implementation
- `expando/render. h` - Rendering callbacks
- `expando/helpers.c` - Helper functions for callback lookup

---

## Testing

See test files in `test/expando/`:
- `test/expando/node_expando. c` - Expando parsing tests
- `test/expando/node_condition_parse.c` - Conditional parsing tests
- `test/expando/simple_expando.c` - Basic expando tests
- `test/expando/simple_expando_render.c` - Rendering tests

---

## Summary

The Expando system is a sophisticated template engine that: 
1. **Defines** expandos via `ExpandoDefinition` arrays with DID/UID pairs
2. **Parses** format strings into tree structures of `ExpandoNode` objects
3. **Renders** nodes by looking up callbacks (string or number) by DID/UID
4. **Handles conditionals** with boolean, date, and custom condition types

This architecture provides flexibility for complex formatting while maintaining clean separation between definition, parsing, and rendering. 

