"""Pygments lexer for NeoMutt configuration files.

Handles NeoMutt's rich configuration language including commands, color
definitions, key bindings, config variables, functions, and more.
"""

from pygments.lexer import RegexLexer, bygroups, include, using, words
from pygments.token import (
    Comment,
    Error,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Text,
    Whitespace,
)

__all__ = ["NeoMuttLexer"]

# ---------------------------------------------------------------------------
# Keyword lists extracted from NeoMutt source code
# ---------------------------------------------------------------------------

# Commands that take set-style arguments (option = value)
SET_COMMANDS = (
    "set", "unset", "toggle", "reset",
)

# Commands that take bind-style arguments (menu key function)
BIND_COMMANDS = (
    "bind", "unbind", "macro", "unmacro",
)

# Commands that take color arguments (object fg bg [regex])
COLOR_COMMANDS = (
    "color", "uncolor", "mono", "unmono",
)

# Commands that define aliases
ALIAS_COMMANDS = (
    "alias", "unalias",
)

# Hook commands (pattern/regex + command)
HOOK_COMMANDS = (
    "account-hook", "charset-hook", "crypt-hook", "fcc-hook",
    "fcc-save-hook", "folder-hook", "iconv-hook", "index-format-hook",
    "mbox-hook", "message-hook", "reply-hook", "save-hook", "send-hook",
    "send2-hook", "shutdown-hook", "startup-hook", "timeout-hook",
    "new-mail-hook", "unhook", "pgp-hook",
    "open-hook", "close-hook", "append-hook",
)

# All other commands
OTHER_COMMANDS = (
    "alternates", "unalternates",
    "alternative-order", "unalternative-order",
    "attachments", "unattachments",
    "auto-view", "unauto-view",
    "cd", "echo", "exec", "finish",
    "group", "ungroup",
    "header-order", "unheader-order",
    "ifdef", "ifndef",
    "ignore", "unignore",
    "lists", "unlists",
    "lua", "lua-source",
    "mailboxes", "unmailboxes",
    "named-mailboxes",
    "mailto-allow", "unmailto-allow",
    "mime-lookup", "unmime-lookup",
    "my-header", "unmy-header",
    "nospam",
    "push",
    "score", "unscore",
    "setenv", "unsetenv",
    "sidebar-pin", "sidebar-unpin",
    "source",
    "spam",
    "subject-regex", "unsubject-regex",
    "subjectrx", "unsubjectrx",
    "subscribe", "unsubscribe",
    "subscribe-to", "unsubscribe-from",
    "tag-formats", "tag-transforms",
    "version",
    "virtual-mailboxes", "unvirtual-mailboxes",
)

# All commands combined (for quick reference in root state)
ALL_COMMANDS = (
    SET_COMMANDS + BIND_COMMANDS + COLOR_COMMANDS + ALIAS_COMMANDS +
    HOOK_COMMANDS + OTHER_COMMANDS
)

# Menus used in bind/macro commands
MENUS = (
    "generic", "alias", "attach", "browser", "editor",
    "index", "compose", "pager", "pgp", "smime",
    "postpone", "query", "mix", "autocrypt",
)

# Simple color names
COLORS = (
    "black", "red", "green", "yellow", "blue",
    "magenta", "cyan", "white", "default",
    "brightblack", "brightred", "brightgreen", "brightyellow",
    "brightblue", "brightmagenta", "brightcyan", "brightwhite",
)

# Color objects/targets (simple, one fg + bg)
COLOR_OBJECTS_SIMPLE = (
    "attachment", "bold", "error", "hdrdefault", "indicator",
    "markers", "message", "normal", "options", "progress",
    "prompt", "search", "signature", "tilde", "tree",
    "underline", "warning", "italic", "stripe",
    # sidebar
    "sidebar_background", "sidebar_divider", "sidebar_flagged",
    "sidebar_highlight", "sidebar_indicator", "sidebar_new",
    "sidebar_ordinary", "sidebar_spool_file", "sidebar_unread",
    # compose
    "compose_header", "compose_security_encrypt", "compose_security_sign",
    "compose_security_both", "compose_security_none",
)

# Color objects that take an optional regex/pattern argument
COLOR_OBJECTS_REGEX = (
    "attach_headers", "body", "header", "index",
    "index_author", "index_collapsed", "index_date",
    "index_flags", "index_label", "index_number",
    "index_size", "index_subject", "index_tag", "index_tags",
    "status",
)

# Quoted levels (quoted, quoted0 .. quoted9)
COLOR_OBJECTS_QUOTED = tuple(
    f"quoted{i}" for i in range(10)
) + ("quoted",)

ALL_COLOR_OBJECTS = (
    COLOR_OBJECTS_SIMPLE + COLOR_OBJECTS_REGEX + COLOR_OBJECTS_QUOTED
)

# Quad option values
QUAD_VALUES = ("yes", "no", "ask-yes", "ask-no")

# Sort values for $sort, $sort_aux
SORT_VALUES = (
    "date", "date-received", "date-sent",
    "from", "to", "subject", "size",
    "threads", "unsorted", "mailbox-order",
    "score", "label", "spam",
    # last- prefix variants
    "last-date", "last-date-received", "last-date-sent",
    # reverse- prefix variants
    "reverse-date", "reverse-date-received", "reverse-date-sent",
    "reverse-from", "reverse-to", "reverse-subject", "reverse-size",
    "reverse-threads", "reverse-unsorted", "reverse-mailbox-order",
    "reverse-score", "reverse-label", "reverse-spam",
    "reverse-last-date", "reverse-last-date-received",
    "reverse-last-date-sent",
    # browser sort
    "alpha", "count",
    "reverse-alpha", "reverse-count",
)

# Mono attributes
MONO_ATTRS = (
    "none", "bold", "underline", "reverse", "standout",
    "italic",
)


class NeoMuttLexer(RegexLexer):
    """Pygments lexer for NeoMutt configuration files."""

    name = "NeoMutt"
    aliases = ["neomutt", "neomuttrc", "muttrc"]
    filenames = [
        "*.neomuttrc", "*.muttrc",
        "neomuttrc", "muttrc",
        ".neomuttrc", ".muttrc",
    ]
    mimetypes = []
    url = "https://neomutt.org"
    version_added = ""

    tokens = {
        # ---------------------------------------------------------------
        # Shared / reusable fragments
        # ---------------------------------------------------------------
        "whitespace": [
            (r"[ \t]+", Whitespace),
        ],
        "escapes": [
            (r"\\[\\\"\'ntre ]", String.Escape),
            (r"\\x[0-9a-fA-F]{2}", String.Escape),
            (r"\\[0-7]{1,3}", String.Escape),
            (r"\\c.", String.Escape),
            (r"\\.", String.Escape),
        ],
        "string-double": [
            (r'"', String.Double, "#pop"),
            (r"\\\n", String.Double),  # line continuation
            include("escapes"),
            (r'[^"\\]+', String.Double),
        ],
        "string-single": [
            (r"'", String.Single, "#pop"),
            (r"[^']+", String.Single),
        ],
        "string-backtick": [
            (r"`", String.Backtick, "#pop"),
            (r"[^`]+", String.Backtick),
        ],
        "color-value": [
            # RGB hex color
            (r"#[0-9a-fA-F]{6}\b", Literal),
            # Palette color (color0 .. color255)
            (r"color\d{1,3}\b", Name.Builtin),
            # Simple color names (including bright variants)
            (words(COLORS, suffix=r"\b"), Name.Builtin),
        ],
        "generic-value": [
            include("whitespace"),
            (r"#.*$", Comment.Single),
            (r"\\\n", Text),  # line continuation
            (r'"', String.Double, "string-double"),
            (r"'", String.Single, "string-single"),
            (r"`", String.Backtick, "string-backtick"),
            # function names in angle brackets
            (r"<[a-zA-Z][-a-zA-Z0-9]+>", Name.Function),
            # RGB hex color (must be before generic word)
            (r"#[0-9a-fA-F]{6}\b", Literal),
            # Numbers
            (r"-?\d+\b", Number),
            # Operators
            (r"[=!<>]=?|[+\-*/]=?|\?|&|;", Operator),
            # $variable expansion
            (r"\$[a-zA-Z_][a-zA-Z0-9_]*", Name.Variable.Global),
            # General unquoted word (catch-all)
            (r"[^\s#\"'`\\]+", Text),
        ],

        # ---------------------------------------------------------------
        # Root state
        # ---------------------------------------------------------------
        "root": [
            include("whitespace"),
            # Comment (full line or trailing)
            (r"#.*$", Comment.Single),
            # Line continuation
            (r"\\\n", Text),
            # Empty lines
            (r"\n", Whitespace),

            # --- Dispatch commands by category (longer matches first) ---

            # Hook commands (must come before other commands due to hyphens)
            (words(HOOK_COMMANDS, suffix=r"\b"), Keyword, "hook-command"),

            # Set-style commands
            (words(SET_COMMANDS, suffix=r"\b"), Keyword, "set-command"),

            # Bind-style commands
            (words(BIND_COMMANDS, suffix=r"\b"), Keyword, "bind-command"),

            # Color commands
            (words(COLOR_COMMANDS, suffix=r"\b"), Keyword, "color-command"),

            # Alias commands
            (words(ALIAS_COMMANDS, suffix=r"\b"), Keyword, "alias-command"),

            # All other known commands
            (words(OTHER_COMMANDS, suffix=r"\b"), Keyword, "generic-args"),

            # Fallback: unknown command-like word at start of line
            (r"[a-zA-Z][-a-zA-Z0-9_]*", Name, "generic-args"),
        ],

        # ---------------------------------------------------------------
        # set / unset / toggle / reset
        # ---------------------------------------------------------------
        "set-command": [
            include("whitespace"),
            (r"#.*$", Comment.Single, "#pop"),
            (r"\\\n", Text),
            (r"\n", Whitespace, "#pop"),
            # Operators: =, +=, -=, also ? and & prefixes
            (r"[?&]", Operator),
            (r"\+?=", Operator),
            (r"-=", Operator),
            # Values: quad options / sort values (must precede generic name)
            (words(QUAD_VALUES, suffix=r"\b"), Name.Constant),
            (words(SORT_VALUES, suffix=r"\b"), Name.Constant),
            # Config option name
            (r"[a-zA-Z_][a-zA-Z0-9_]*", Name.Variable),
            # Strings
            (r'"', String.Double, "string-double"),
            (r"'", String.Single, "string-single"),
            (r"`", String.Backtick, "string-backtick"),
            # Numbers
            (r"-?\d+\b", Number),
            # $variable
            (r"\$[a-zA-Z_][a-zA-Z0-9_]*", Name.Variable.Global),
            # Boolean-style: no prefix for the option
            (r"!", Operator),
            # Unquoted value fallback
            (r"[^\s#\"'`\\=!?&]+", String),
        ],

        # ---------------------------------------------------------------
        # bind / unbind / macro / unmacro
        # ---------------------------------------------------------------
        "bind-command": [
            include("whitespace"),
            (r"#.*$", Comment.Single, "#pop"),
            (r"\\\n", Text),
            (r"\n", Whitespace, "#pop"),
            # Menu names (can be comma-separated)
            (words(MENUS, suffix=r"\b"), Name.Tag),
            (r",", Punctuation),
            # Key sequence (often quoted)
            (r'"', String.Double, "string-double"),
            (r"'", String.Single, "string-single"),
            # Function name in angle brackets
            (r"<[a-zA-Z][-a-zA-Z0-9]+>", Name.Function),
            # Bare key (single char or special like \t, \Cx for ctrl keys)
            (r"\\[a-zA-Z]", String.Escape),
            (r"[^\s#\"'<,\\]+", String),
        ],

        # ---------------------------------------------------------------
        # color / uncolor / mono / unmono
        # ---------------------------------------------------------------
        "color-command": [
            include("whitespace"),
            (r"\\\n", Text),
            (r"\n", Whitespace, "#pop"),
            # Color objects
            (words(ALL_COLOR_OBJECTS, suffix=r"\b"), Name.Entity),
            # Color values (fg, bg) — must precede comment rule for #RRGGBB
            include("color-value"),
            # Comment (after RGB hex check)
            (r"#.*$", Comment.Single, "#pop"),
            # Mono attributes
            (words(MONO_ATTRS, suffix=r"\b"), Name.Builtin),
            # Regex pattern (for body, header, index, etc.)
            (r'"', String.Double, "string-double"),
            (r"'", String.Single, "string-single"),
            # Pattern like ~A or ~f
            (r"~[a-zA-Z]", Name.Attribute),
            # Unquoted text (pattern or other)
            (r"[^\s#\"'\\]+", String),
        ],

        # ---------------------------------------------------------------
        # alias / unalias
        # ---------------------------------------------------------------
        "alias-command": [
            include("whitespace"),
            (r"\\\n", Text),
            (r"\n", Whitespace, "#pop"),
            # Comment with optional tags annotation
            (r"(#)(.*?)(tags:)([\w,]+)(.*$)",
             bygroups(Comment.Single, Comment.Single, Name.Label,
                      Name.Label, Comment.Single), "#pop"),
            (r"#.*$", Comment.Single, "#pop"),
            # Email address in angle brackets
            (r"<[^>]+@[^>]+>", String),
            # Quoted strings
            (r'"', String.Double, "string-double"),
            (r"'", String.Single, "string-single"),
            # Alias name (first word), then address parts
            (r"[^\s#\"'<\\]+", Text),
        ],

        # ---------------------------------------------------------------
        # *-hook commands
        # ---------------------------------------------------------------
        "hook-command": [
            include("whitespace"),
            (r"#.*$", Comment.Single, "#pop"),
            (r"\\\n", Text),
            (r"\n", Whitespace, "#pop"),
            # Pattern in quotes
            (r'"', String.Double, "string-double"),
            (r"'", String.Single, "string-single"),
            (r"`", String.Backtick, "string-backtick"),
            # Pattern operators (~f, ~t, etc.)
            (r"~[a-zA-Z]", Name.Attribute),
            # Inline command keywords after pattern
            (words(ALL_COMMANDS, suffix=r"\b"), Keyword),
            # $variable
            (r"\$[a-zA-Z_][a-zA-Z0-9_]*", Name.Variable.Global),
            # Operators
            (r"[=!|&]", Operator),
            # Numbers
            (r"-?\d+\b", Number),
            # General text
            (r"[^\s#\"'`\\]+", Text),
        ],

        # ---------------------------------------------------------------
        # Generic argument list (for other commands)
        # ---------------------------------------------------------------
        "generic-args": [
            include("generic-value"),
            (r"\n", Whitespace, "#pop"),
        ],
    }
