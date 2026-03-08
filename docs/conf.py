# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'NeoMutt'
copyright = '2026, Richard Russon'
author = 'flatcap'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'myst_parser',
    'sphinx_design',
]

myst_enable_extensions = [
    'colon_fence',
]

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.png"

html_theme_options = {
    "max_navbar_depth": 2,
    "pygments_light_style": "gruvbox-light",
    "pygments_dark_style": "gruvbox-dark",
    "use_download_button": False,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_context = {
    "display_github": True,
    "github_user": "neomutt",
    "github_repo": "neomutt",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

