# NeoMutt Expando User Guide

## Table of Contents

1. [What are Expandos?](#what-are-expandos)
2. [How to Use Expandos](#how-to-use-expandos)
3. [Formatting Expandos](#formatting-expandos)
4. [Conditional Expandos](#conditional-expandos)
5. [Quick Reference](#quick-reference)

---

## What are Expandos? 

Expandos are **format strings** used throughout NeoMutt to customize how information is displayed. They work like placeholders that get replaced with actual data when NeoMutt displays content.

### Why Use Expandos? 

Expandos allow you to:
- **Customize displays**:  Change how emails, folders, and other items appear
- **Show relevant information**: Display exactly what you want to see
- **Save screen space**: Format content efficiently
- **Create dynamic content**: Show different information based on conditions

### Where are Expandos Used?

Expandos are used in many NeoMutt configuration settings: 

- `$index_format` - Email list display
- `$status_format` - Status bar content
- `$folder_format` - Folder list display
- `$compose_format` - Compose screen display
- `$attach_format` - Attachment list display
- `$alias_format` - Alias list display
- And many more...

### Basic Syntax

Expandos start with a percent sign (`%`) followed by a character: 

```
%s    - Subject of email
%f    - Sender (From: )
%d    - Date
%n    - Message number
```

Plain text can be mixed with expandos:

```
"Message %n: %s"
```

This might display as:  **Message 42: Hello World**

---

## How to Use Expandos

### Simple Example

Let's customize how emails appear in your inbox.  The default might look like:

```
1  Jan 15  John Smith    (5. 2K)  Meeting tomorrow
2  Jan 15  Jane Doe      (1.3K)  Project update
```

This is controlled by `$index_format`. Here's a simple format string:

```muttrc
set index_format="%4C %Z %{%b %d} %-20.20L (%4c) %s"
```

**What each expando means:**
- `%4C` - Message number (4 characters wide)
- `%Z` - Status flags (new, replied, etc.)
- `%{%b %d}` - Date (abbreviated month and day)
- `%-20.20L` - From/To field (left-aligned, exactly 20 characters)
- `(%4c)` - Message size in parentheses (4 characters wide)
- `%s` - Subject

### Short Names vs Long Names

Most expandos have two forms: 

**Short name** (single character):
```
%s    - Subject
%f    - From
%n    - Number
```

**Long name** (descriptive, in curly braces):
```
%{subject}     - Same as %s
%{from}        - Same as %f
%{number}      - Same as %n
```

Long names are more readable in complex formats: 

```muttrc
# Using short names
set status_format="%f:  %m messages (%n new)"

# Using long names (equivalent)
set status_format="%{folder}: %{message_count} messages (%{new_count} new)"
```

### Special Characters

Some expandos use special delimiters:

**Square brackets** for date formats:
```
%[%Y-%m-%d]       - Date in YYYY-MM-DD format
%[%H:%M]          - Time in 24-hour format
%[%I:%M %p]       - Time in 12-hour format with AM/PM
```

**Curly braces** for long names:
```
%{subject}        - Long form of %s
%{from}           - Long form of %f
```

---

## Formatting Expandos

Expandos support powerful formatting options similar to C's `printf()`.

### Basic Format Syntax

```
%[flags][width][.max_width]<expando>
```

**Components:**
- **flags**: Optional formatting flags (-, _, =, 0)
- **width**:  Minimum field width
- **max_width**: Maximum field width (truncation)
- **expando**: The expando character

### Width Control

**Minimum width** (pad with spaces if shorter):

```muttrc
set index_format="%5n %s"
```

Examples:
```
    1 Short subject
   42 Another subject
  123 Yet another
```

Numbers are right-aligned by default.

**Maximum width** (truncate if longer):

```muttrc
set index_format="%n %. 30s"
```

If subject is longer than 30 characters, it will be truncated: 
```
1 This is a very long subject th... 
```

**Combined** (min and max):

```muttrc
set index_format="%5n %20. 30s"
```

- At least 20 characters wide
- At most 30 characters wide
- Padded with spaces if shorter than 20
- Truncated if longer than 30

### Alignment Flags

**Left align** with `-`:

```muttrc
set index_format="%-20f %s"
```

From field is left-aligned in 20 character space:
```
John Smith           Meeting tomorrow
Jane Doe             Project update
```

**Right align** (default for numbers):

```muttrc
set index_format="%20f %s"
```

From field is right-aligned: 
```
        John Smith Meeting tomorrow
          Jane Doe Project update
```

**Center align** with `=`:

```muttrc
set index_format="%=20s"
```

Subject is centered in 20 character space:
```
    Hello World
  Meeting Tomorrow
```

### Padding Characters

**Space padding** (default):

```muttrc
set index_format="%4n %s"
```
```
   1 First message
  42 Forty-second message
```

**Zero padding** with `0`:

```muttrc
set index_format="%04n %s"
```
```
0001 First message
0042 Forty-second message
```

**Underscore padding** with `_`:

```muttrc
set index_format="%_4n %s"
```
```
___1 First message
__42 Forty-second message
```

### Case Conversion

**Lowercase** with `_` before expando:

```muttrc
set index_format="%_s"
```

Converts subject to lowercase:
```
HELLO WORLD → hello world
Meeting Tomorrow → meeting tomorrow
```

### Dynamic Padding

**Fill to end of line** with `>`:

```muttrc
set status_format="-%r-NeoMutt: %f %>- [Msgs:%m]"
```

The `%>-` fills remaining space with dashes:
```
-rw-NeoMutt: inbox/-----------------------------------[Msgs:42]
```

**Soft fill** with `|`:

```muttrc
set status_format="NeoMutt: %f %|.  [Msgs:%m]"
```

The `%|.` fills remaining space with dots:
```
NeoMutt: inbox/................................ .[Msgs:42]
```

**Hard fill** with `*`:

```muttrc
set status_format="NeoMutt %*X [Msgs:%m]"
```

The `%*X` fills remaining space with 'X':
```
NeoMutt XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX[Msgs:42]
```

### Complete Formatting Examples

**Example 1: Clean email list**

```muttrc
set index_format="%4C %Z %{%b %d} %-20.20L (%4c) %s"
```

Output:
```
   1 N Jan 15 John Smith           (5.2K) Meeting tomorrow at 3pm
  42   Jan 14 Jane Doe             (1.3K) RE: Project update needed
 123 r Jan 13 Bob Johnson          ( 867) Quick question about docs
```

**Example 2: Compact format**

```muttrc
set index_format="%3C│%Z│%[%m/%d]│%-15.15L│%. 40s"
```

Output:
```
  1│N│01/15│John Smith     │Meeting tomorrow at 3pm
 42│ │01/14│Jane Doe       │RE: Project update needed
123│r│01/13│Bob Johnson    │Quick question about docs
```

**Example 3: Detailed format**

```muttrc
set index_format="%4C [%Z] %D %-20.20F (%4c) %s"
```

Output:
```
   1 [N] Jan 15 14:32 John Smith           (5.2K) Meeting tomorrow at 3pm
  42 [ ] Jan 14 09:15 Jane Doe             (1.3K) RE: Project update needed
 123 [r] Jan 13 16:47 Bob Johnson          ( 867) Quick question about docs
```

**Example 4: Status bar with padding**

```muttrc
set status_format="-%r-NeoMutt:  %f [Msgs:%? M?%M/?%m%? n? New:%n?%? o? Old:%o?%? d? Del:%d?%?F? Flag:%F?%?t? Tag:%t?] %>-%? p?( %p postponed )?---"
```

Output:
```
-rw-NeoMutt: inbox [Msgs:42 New:5 Flag:2] -------------(3 postponed)---
```

---

## Conditional Expandos

Conditional expandos display different content based on conditions.  They allow dynamic formatting that responds to data. 

### Basic Conditional Syntax

**New style** (recommended):

```
%<condition? true_text&false_text>
```

**Old style** (still supported):

```
%?condition?true_text&false_text? 
```

**Components:**
- **condition**: An expando that evaluates to true/false
- **true_text**:  Shown if condition is true
- **false_text**: Shown if condition is false (optional)

### Simple Examples

**Example 1: Show "New" only if there are new messages**

```muttrc
set status_format="Msgs:%m%<n?  New:%n>"
```

If there are new messages: 
```
Msgs:42 New:5
```

If no new messages:
```
Msgs:42
```

**Example 2: Flag indicator**

```muttrc
set index_format="%4C %Z %s%<F?  [FLAGGED]>"
```

Output:
```
   1 N Meeting tomorrow [FLAGGED]
  42   Project update
```

**Example 3: With both true and false branches**

```muttrc
set index_format="%4C %<%t? [TAGGED]&       > %s"
```

If message is tagged:
```
   1 [TAGGED] Important message
```

If not tagged:
```
  42          Regular message
```

### Nested Expandos in Conditionals

You can use expandos inside conditional branches:

```muttrc
set status_format="Msgs:%m%<n? New:%n>%<F?  Flagged:%F>"
```

Output varies based on data:
```
Msgs:42 New: 5 Flagged:2         (has both new and flagged)
Msgs:42 New:5                   (has only new)
Msgs:42 Flagged:2               (has only flagged)
Msgs:42                         (has neither)
```

### Multiple Conditions

Chain conditions for complex logic:

```muttrc
set status_format="NeoMutt: %f [%m msgs%<n? (%n new)>%<F? (%F flagged)>%<t? (%t tagged)>]"
```

Output:
```
NeoMutt: inbox [42 msgs (5 new) (2 flagged) (3 tagged)]
NeoMutt: sent [15 msgs]
```

### Boolean Expandos

Many expandos are boolean (true/false):

- `%t` - Message is tagged
- `%F` - Message is flagged  
- `%L` - Message is from a mailing list
- `%X` - Message has attachments

**Example:  Show attachment indicator**

```muttrc
set index_format="%4C %Z %<%X? 📎&  > %-20.20f %s"
```

Output:
```
   1 N 📎 John Smith           Report with attachments
  42   📎 Jane Doe             Meeting notes
 123      Bob Johnson          Quick question
```

### Date-Based Conditionals

Show different content based on message age:

**Syntax**:  `%<[Nm? true&false>`

Where:
- `N` = number
- `m` = time period: 
  - `y` = years
  - `m` = months  
  - `w` = weeks
  - `d` = days
  - `H` = hours
  - `M` = minutes

**Example 1: Highlight recent messages**

```muttrc
set index_format="%4C %<%[1d? TODAY! &%[%b %d]> %-20.20f %s"
```

Output:
```
   1 TODAY! John Smith           Meeting tomorrow
  42 Jan 14 Jane Doe             Project update
 123 Jan 13 Bob Johnson          Question
```

**Example 2: Different colors for message age**

```muttrc
set index_format="%4C %<%[1d?%[%H:%M]&%<%[1w?%[%a %H:%M]&%[%b %d]>> %s"
```

Output:
```
   1 14:32 Meeting tomorrow           (today - show time)
  42 Mon 09:15 Project update          (this week - show day and time)
 123 Jan 08 Question                   (older - show date)
```

**Example 3: Three-tier date display**

```muttrc
set index_format="%4C %<%[1d?%[%H:%M]&%<%[7d?%[%a]&%[%m/%d]>> %s"
```

- Less than 1 day old: Show time (14:32)
- Less than 7 days old: Show day (Mon, Tue, etc.)
- Older:  Show date (01/15)

### Conditional Formatting

You can apply formatting to the entire conditional:

```muttrc
set status_format="Msgs:%m%<n? %-20.20 New messages:  %n>"
```

The formatting (`%-20.20`) applies to the entire true branch. 

### Complex Conditional Examples

**Example 1: Smart message counter**

```muttrc
set status_format="%f:  %m message%<m? %<M?&s>>%<n?  (%n new)>"
```

Logic:
- Shows "message" if m=1
- Shows "messages" if m>1  
- Adds " (N new)" if new messages exist

Output:
```
inbox: 1 message (1 new)
inbox: 42 messages (5 new)
inbox: 15 messages
```

**Example 2: Detailed status with multiple conditions**

```muttrc
set status_format="-%r-NeoMutt:  %f [Total:%m%<n? New:%n>%<d? Del:%d>%<F? Flag:%F>%<t? Tag:%t>] %>--%<P?(Postponed:  %P) >--"
```

Output adapts to current state:
```
-rw-NeoMutt: inbox [Total:42 New:5 Flag:2 Tag:3] -----------------(Postponed: 2) --
-rw-NeoMutt: sent [Total:15] ----------------------------------------------------
```

**Example 3: Dynamic width adjustment**

```muttrc
set index_format="%<M?%4C&%3C> %Z %-20.20f %s%<X?  [%X attachments]>"
```

- Uses 4-character width if more than 999 messages
- Uses 3-character width otherwise
- Shows attachment count if present

**Example 4: Thread indicator**

```muttrc
set index_format="%4C %Z %<%g? [Thread]&       > %-20.20f %s"
```

Shows `[Thread]` for messages with replies. 

### Best Practices for Conditionals

1. **Keep it readable**: Use long names for complex conditions
   ```muttrc
   # Clear
   set status_format="%{folder}: %{msg_count} messages%<new_count?  (%{new_count} new)>"
   
   # Less clear
   set status_format="%f: %m messages%<n? (%n new)>"
   ```

2. **Test with different data**: Check how it looks with zero values, high values, etc.

3. **Provide defaults**: Always consider the false case
   ```muttrc
   # Good:  Shows status either way
   set index_format="%<%F?[★ ]&   > %s"
   
   # Bad:  Alignment breaks when flag changes
   set index_format="%<%F?[★ ]>%s"
   ```

4. **Use whitespace wisely**: Include spaces in conditional branches
   ```muttrc
   # Good: Space before "New:"
   set status_format="Total:%m%<n? New:%n>"
   
   # Bad:  Missing space
   set status_format="Total:%m%<n? New:%n>"
   ```

---

## Quick Reference

### Common Index Format Expandos

| Expando | Description | Example |
|---------|-------------|---------|
| `%C` | Message number | 1, 42, 123 |
| `%Z` | Status flags | N (new), D (deleted), r (replied) |
| `%s` | Subject | Meeting tomorrow |
| `%f` | From (sender) | john@example.com |
| `%L` | From/To (smart) | John Smith or To Jane Doe |
| `%d` | Date (locale) | Jan 15 |
| `%D` | Date/time (locale) | Jan 15 14:32 |
| `%[fmt]` | Date (custom) | `%[%Y-%m-%d]` → 2025-01-15 |
| `%c` | Message size | 5.2K, 867 |
| `%t` | To:  field | jane@example.com |
| `%F` | Author name | John Smith |
| `%X` | Attachment count | 2 |
| `%g` | Newsgroup name | comp.mail.neomutt |

### Common Status Format Expandos

| Expando | Description | Example |
|---------|-------------|---------|
| `%f` | Folder name | inbox, sent |
| `%m` | Total messages | 42 |
| `%n` | New messages | 5 |
| `%d` | Deleted messages | 2 |
| `%F` | Flagged messages | 3 |
| `%t` | Tagged messages | 4 |
| `%l` | Mailbox size | 1.2M |
| `%P` | Postponed count | 2 |
| `%r` | Read-only flag | - or r |
| `%M` | Hidden messages | 8 |
| `%V` | NeoMutt version | NeoMutt 2024-01-01 |

### Formatting Quick Reference

| Format | Effect | Example |
|--------|--------|---------|
| `%20s` | Min width 20, right-aligned | `       Short text` |
| `%-20s` | Min width 20, left-aligned | `Short text       ` |
| `%=20s` | Min width 20, centered | `   Short text    ` |
| `%.20s` | Max width 20, truncate | `This is a very lon... ` |
| `%20.30s` | Min 20, max 30 | Pad to 20, truncate at 30 |
| `%04n` | Width 4, zero-padded | `0042` |
| `%_s` | Lowercase | `hello world` |
| `%>-` | Fill to end with `-` | `Text----` |

### Conditional Quick Reference

| Pattern | Description | Example |
|---------|-------------|---------|
| `%<X? yes>` | Show "yes" if X is true | `%<F?★>` |
| `%<X?yes&no>` | Show "yes" or "no" | `%<t?Tagged&Normal>` |
| `%<[1d?new&old>` | Date-based (< 1 day) | Show "new" if recent |
| `%<[3m?recent&old>` | Date-based (< 3 months) | Show "recent" if within 3 months |
| `%<[1w?%[%a]&%[%b %d]>` | Nested conditional | Show day if < 1 week, else date |

### Date Format Codes

Common date format codes for `%[...]`:

| Code | Description | Example |
|------|-------------|---------|
| `%Y` | Year (4 digits) | 2025 |
| `%y` | Year (2 digits) | 25 |
| `%m` | Month (01-12) | 01 |
| `%b` | Month abbreviated | Jan |
| `%B` | Month full | January |
| `%d` | Day of month | 15 |
| `%a` | Weekday abbreviated | Mon |
| `%A` | Weekday full | Monday |
| `%H` | Hour (24-hour) | 14 |
| `%I` | Hour (12-hour) | 02 |
| `%M` | Minute | 32 |
| `%S` | Second | 45 |
| `%p` | AM/PM | PM |

---

## Complete Configuration Examples

### Minimal Setup

```muttrc
# Simple, clean format
set index_format="%4C %Z %d %-20.20L %s"
set status_format="-%r-NeoMutt:  %f [Msgs:%m%<n? New:%n>] %>--%P--"
```

### Compact Setup

```muttrc
# Information-dense format
set index_format="%3C│%Z│%[%m/%d %H:%M]│%-15.15F│%4c│%s%<X? 📎>"
set status_format="%f:%m%<n? (%n new)>%<F? (%F flag)>%<t?(%t tag)> %> %P"
```

### Detailed Setup

```muttrc
# Maximum information
set index_format="%4C [%Z] %<%[1d?%[%H:%M]&%<%[7d?%[%a %H:%M]&%[%b %d]>> %-20.20F (%4c) %s%<X? [%X att]>%<g?  [thread]>"
set status_format="-%r-NeoMutt: %f [Total:%m%<n? New:%n>%<o? Old:%o>%<d? Del:%d>%<F? Flag:%F>%<t? Tag:%t>] %>-%<P? ( Postponed:%P )?--"
```

### Visual Setup (with Unicode)

```muttrc
# Modern appearance with symbols
set index_format="%4C %Z %<%F?★& > %<%[1d?%[%H:%M]&%[%b %d]> %-20.20L %<%X? 📎& > %s"
set status_format="📧 %f • %m messages%<n? • %n new>%<F? • %F flagged> %> NeoMutt"
```

---

## Tips and Tricks

1. **Test your formats**: Use `:set index_format="..."` in NeoMutt to test without editing config

2. **Start simple**: Begin with basic expandos, add formatting gradually

3. **Check width**: Use `$COLUMNS` consideration for status bar formats

4. **Use colors**: Combine with `color index` for better visual separation

5. **Document complex formats**: Add comments to explain your conditional logic
   ```muttrc
   # Show time if today, day if this week, date if older
   set index_format="%4C %<%[1d?%[%H:%M]&%<%[7d?%[%a]&%[%b %d]>> %s"
   ```

6. **Platform differences**: Date formats may vary by locale settings

7. **Performance**: Very complex formats may slow down display on large mailboxes

---

This guide covers the essential concepts of NeoMutt expandos. For specific expandos available in each format string, refer to the NeoMutt manual or use `:help <setting>` within NeoMutt (e.g., `:help index_format`).
