"""Unit tests for the NeoMutt Pygments lexer."""

import pytest
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

from neomutt_lexer import NeoMuttLexer


@pytest.fixture
def lexer():
    return NeoMuttLexer()


def _tokens(lexer, text):
    """Return list of (token_type, value) from lexing text."""
    return list(lexer.get_tokens(text))


def _token_types(lexer, text):
    """Return just token types, filtering out trailing newline."""
    return [
        (t, v) for t, v in _tokens(lexer, text)
        if t not in (Whitespace,) or v != "\n"
    ]


# ---------------------------------------------------------------
# Comments
# ---------------------------------------------------------------

class TestComments:
    def test_full_line_comment(self, lexer):
        tokens = _tokens(lexer, "# this is a comment\n")
        assert tokens[0] == (Comment.Single, "# this is a comment")

    def test_trailing_comment(self, lexer):
        tokens = _tokens(lexer, "set folder = ~/Mail # comment\n")
        types = [t for t, v in tokens]
        assert Comment.Single in types


# ---------------------------------------------------------------
# Strings
# ---------------------------------------------------------------

class TestStrings:
    def test_double_quoted(self, lexer):
        tokens = _tokens(lexer, 'set folder = "~/Mail"\n')
        values = [v for t, v in tokens if t == String.Double]
        assert "~/Mail" in values

    def test_single_quoted(self, lexer):
        tokens = _tokens(lexer, "set from = 'alice@example.com'\n")
        values = [v for t, v in tokens if t == String.Single]
        assert "alice@example.com" in values

    def test_backtick(self, lexer):
        tokens = _tokens(lexer, "set my_pass = `gpg --decrypt pass.gpg`\n")
        values = [v for t, v in tokens if t == String.Backtick]
        assert any("gpg" in v for v in values)

    def test_escape_in_double_quote(self, lexer):
        tokens = _tokens(lexer, r'set strstr = "hello\nworld"' + "\n")
        types = [t for t, v in tokens]
        assert String.Escape in types


# ---------------------------------------------------------------
# Numbers
# ---------------------------------------------------------------

class TestNumbers:
    def test_positive_number(self, lexer):
        tokens = _tokens(lexer, "set mail_check = 120\n")
        assert any(t == Number and v == "120" for t, v in tokens)

    def test_negative_number(self, lexer):
        tokens = _tokens(lexer, "score ~A -10\n")
        assert any(t == Number and v == "-10" for t, v in tokens)


# ---------------------------------------------------------------
# Operators
# ---------------------------------------------------------------

class TestOperators:
    def test_equals(self, lexer):
        tokens = _tokens(lexer, "set folder = ~/Mail\n")
        assert any(t == Operator and "=" in v for t, v in tokens)

    def test_plus_equals(self, lexer):
        tokens = _tokens(lexer, "set sidebar_width += 5\n")
        assert any(t == Operator and v == "+=" for t, v in tokens)

    def test_query_prefix(self, lexer):
        tokens = _tokens(lexer, "set ?strstr\n")
        assert any(t == Operator and v == "?" for t, v in tokens)

    def test_ampersand_prefix(self, lexer):
        tokens = _tokens(lexer, "set &strstr\n")
        assert any(t == Operator and v == "&" for t, v in tokens)


# ---------------------------------------------------------------
# Commands
# ---------------------------------------------------------------

class TestCommands:
    @pytest.mark.parametrize("cmd", [
        "set", "unset", "toggle", "reset",
        "bind", "unbind", "macro", "unmacro",
        "color", "uncolor", "mono", "unmono",
        "alias", "unalias",
        "source", "push", "exec", "echo", "cd",
        "ifdef", "ifndef", "finish",
        "mailboxes", "unmailboxes",
        "lists", "unlists",
        "subscribe", "unsubscribe",
        "alternates", "unalternates",
        "ignore", "unignore",
    ])
    def test_command_keyword(self, lexer, cmd):
        tokens = _tokens(lexer, f"{cmd} arg\n")
        assert tokens[0][0] == Keyword
        assert tokens[0][1] == cmd

    @pytest.mark.parametrize("cmd", [
        "folder-hook", "send-hook", "message-hook",
        "startup-hook", "shutdown-hook", "timeout-hook",
        "account-hook", "charset-hook",
    ])
    def test_hook_command(self, lexer, cmd):
        tokens = _tokens(lexer, f'{cmd} "pattern" "command"\n')
        assert tokens[0][0] == Keyword
        assert tokens[0][1] == cmd


# ---------------------------------------------------------------
# Functions (in angle brackets)
# ---------------------------------------------------------------

class TestFunctions:
    def test_function_in_bind(self, lexer):
        tokens = _tokens(lexer, "bind index j next-entry\n")
        # next-entry is just text in bind context, but <next-entry> is a function
        tokens2 = _tokens(lexer, "macro index A \"<save-message>=Archive<enter>\"\n")
        types = [t for t, v in tokens2]
        # Inside the string, function names aren't separately highlighted
        # But in push/exec context they are
        tokens3 = _tokens(lexer, "push <check-stats>\n")
        assert any(t == Name.Function for t, v in tokens3)

    def test_function_standalone(self, lexer):
        tokens = _tokens(lexer, "push <next-page>\n")
        assert any(t == Name.Function and v == "<next-page>" for t, v in tokens)


# ---------------------------------------------------------------
# Config options in set command
# ---------------------------------------------------------------

class TestConfigOptions:
    def test_option_name(self, lexer):
        tokens = _tokens(lexer, "set folder = ~/Mail\n")
        assert any(t == Name.Variable and v == "folder" for t, v in tokens)

    def test_multiple_options(self, lexer):
        tokens = _tokens(lexer, "set sort = date sidebar_visible = yes\n")
        vars_found = [v for t, v in tokens if t == Name.Variable]
        assert "sort" in vars_found
        assert "sidebar_visible" in vars_found


# ---------------------------------------------------------------
# Colors
# ---------------------------------------------------------------

class TestColors:
    def test_simple_color(self, lexer):
        tokens = _tokens(lexer, "color normal white default\n")
        builtins = [v for t, v in tokens if t == Name.Builtin]
        assert "white" in builtins
        assert "default" in builtins

    def test_bright_color(self, lexer):
        tokens = _tokens(lexer, "color error brightred default\n")
        builtins = [v for t, v in tokens if t == Name.Builtin]
        assert "brightred" in builtins

    def test_palette_color(self, lexer):
        tokens = _tokens(lexer, "color normal color252 color234\n")
        builtins = [v for t, v in tokens if t == Name.Builtin]
        assert "color252" in builtins
        assert "color234" in builtins

    def test_rgb_color(self, lexer):
        tokens = _tokens(lexer, "color normal #f0e1d2 #1a1a2e\n")
        lits = [v for t, v in tokens if t == Literal]
        assert "#f0e1d2" in lits
        assert "#1a1a2e" in lits


# ---------------------------------------------------------------
# Color objects
# ---------------------------------------------------------------

class TestColorObjects:
    @pytest.mark.parametrize("obj", [
        "normal", "error", "indicator", "status",
        "sidebar_new", "sidebar_highlight",
        "compose_header", "compose_security_encrypt",
    ])
    def test_simple_object(self, lexer, obj):
        tokens = _tokens(lexer, f"color {obj} white default\n")
        assert any(t == Name.Entity and v == obj for t, v in tokens)

    @pytest.mark.parametrize("obj", ["body", "header", "index", "index_author"])
    def test_regex_object(self, lexer, obj):
        tokens = _tokens(lexer, f'color {obj} red default "pattern"\n')
        assert any(t == Name.Entity and v == obj for t, v in tokens)

    def test_quoted_levels(self, lexer):
        for level in ("quoted", "quoted1", "quoted5", "quoted9"):
            tokens = _tokens(lexer, f"color {level} green default\n")
            assert any(t == Name.Entity and v == level for t, v in tokens)


# ---------------------------------------------------------------
# Menus
# ---------------------------------------------------------------

class TestMenus:
    @pytest.mark.parametrize("menu", [
        "index", "pager", "compose", "browser",
        "alias", "attach", "editor", "generic",
    ])
    def test_menu_in_bind(self, lexer, menu):
        tokens = _tokens(lexer, f"bind {menu} j next-entry\n")
        assert any(t == Name.Tag and v == menu for t, v in tokens)

    def test_comma_separated_menus(self, lexer):
        tokens = _tokens(lexer, "bind index,pager j next-entry\n")
        tags = [v for t, v in tokens if t == Name.Tag]
        assert "index" in tags
        assert "pager" in tags
        assert any(t == Punctuation and v == "," for t, v in tokens)


# ---------------------------------------------------------------
# Alias comment tags
# ---------------------------------------------------------------

class TestAliasTags:
    def test_alias_with_tags(self, lexer):
        tokens = _tokens(lexer, 'alias boss "The Boss" <boss@ex.com> # contact tags:vip,work\n')
        labels = [v for t, v in tokens if t == Name.Label]
        assert any("tags:" in v for v in labels)
        assert any("vip,work" in v for v in labels)

    def test_alias_without_tags(self, lexer):
        tokens = _tokens(lexer, "alias admin Admin <admin@ex.com> # just a comment\n")
        # Should still have the comment
        assert any(t == Comment.Single for t, v in tokens)


# ---------------------------------------------------------------
# Quad options and sort values
# ---------------------------------------------------------------

class TestEnums:
    @pytest.mark.parametrize("val", ["yes", "no", "ask-yes", "ask-no"])
    def test_quad_values(self, lexer, val):
        tokens = _tokens(lexer, f"set delete = {val}\n")
        assert any(t == Name.Constant and v == val for t, v in tokens)

    @pytest.mark.parametrize("val", [
        "date", "threads", "reverse-date", "last-date-received",
        "mailbox-order", "score", "alpha",
    ])
    def test_sort_values(self, lexer, val):
        tokens = _tokens(lexer, f"set sort = {val}\n")
        assert any(t == Name.Constant and v == val for t, v in tokens)


# ---------------------------------------------------------------
# Hooks
# ---------------------------------------------------------------

class TestHooks:
    def test_folder_hook(self, lexer):
        tokens = _tokens(lexer, 'folder-hook "=work" "set sort=threads"\n')
        assert tokens[0] == (Keyword, "folder-hook")

    def test_startup_hook(self, lexer):
        tokens = _tokens(lexer, "startup-hook \"echo 'hello'\"\n")
        assert tokens[0] == (Keyword, "startup-hook")


# ---------------------------------------------------------------
# Line continuation
# ---------------------------------------------------------------

class TestLineContinuation:
    def test_backslash_newline(self, lexer):
        text = "set strstr \\\n  = value\n"
        tokens = _tokens(lexer, text)
        # Should not error; the continuation should be handled
        assert any(t == Keyword for t, v in tokens)


# ---------------------------------------------------------------
# Variable expansion
# ---------------------------------------------------------------

class TestVariableExpansion:
    def test_dollar_variable(self, lexer):
        tokens = _tokens(lexer, "set strstr = $HOME/Mail\n")
        assert any(
            t == Name.Variable.Global and v == "$HOME" for t, v in tokens
        )


# ---------------------------------------------------------------
# Full example file
# ---------------------------------------------------------------

class TestExampleFile:
    def test_example_parses_without_error(self, lexer):
        """The example file should lex without producing Error tokens."""
        import os
        example = os.path.join(os.path.dirname(__file__), "example.neomuttrc")
        with open(example) as f:
            text = f.read()
        tokens = list(lexer.get_tokens(text))
        error_tokens = [(t, v) for t, v in tokens if t == Error]
        assert error_tokens == [], f"Error tokens found: {error_tokens[:10]}"
