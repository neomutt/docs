"""
Generate redirect pages for each config option.

Creates a stable URL at reference/config/NAME for every (cfg-*)= label,
redirecting to the actual themed page where the option is documented.
"""

import os
from pathlib import Path
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

REDIRECT_TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url={url}">
  <link rel="canonical" href="{url}">
  <script>window.location.replace("{url}")</script>
</head>
<body>
  <p>Redirecting to <a href="{url}">{name}</a>...</p>
</body>
</html>
"""


def generate_redirects(app: Sphinx, exception: Exception | None) -> None:
    if exception or "READTHEDOCS" not in os.environ:
        return

    std = app.env.get_domain("std")
    labels = std.labels  # label -> (docname, labelid, sectionname)

    outdir = Path(app.outdir)
    cfg_count = 0
    cmd_count = 0
    fun_count = 0

    for label, (docname, labelid, _sectionname) in labels.items():
        if label.startswith("cfg-"):
            # cfg-sidebar-visible -> sidebar_visible
            name = label[4:].replace("-", "_")
            redirect_dir = outdir / "config" / name

            # Build relative URL from reference/config/NAME/index.html to the actual page
            target_page = app.builder.get_target_uri(docname)
            # redirect is 2 levels deep: config/NAME/index.html -> ../..
            url = f"../../{target_page}#{labelid}"

            redirect_dir.mkdir(parents=True, exist_ok=True)
            (redirect_dir / "index.html").write_text(REDIRECT_TEMPLATE.format(url=url, name=name))

            cfg_count += 1

        elif label.startswith("cmd-"):
            # cmd-append-hook -> append-hook
            name = label[4:]
            redirect_dir = outdir / "command" / name

            # Build relative URL from reference/config/NAME/index.html to the actual page
            target_page = app.builder.get_target_uri(docname)
            # redirect is 2 levels deep: config/NAME/index.html -> ../..
            url = f"../../{target_page}#{labelid}"

            redirect_dir.mkdir(parents=True, exist_ok=True)
            (redirect_dir / "index.html").write_text(REDIRECT_TEMPLATE.format(url=url, name=name))

            cmd_count += 1

        elif label.startswith("fn-"):
            # cmd-append-hook -> append-hook
            name = label[3:]
            redirect_dir = outdir / "function" / name

            # redirect is 2 levels deep: config/NAME/index.html -> ../..
            url = f"../../reference/functions/index.html#{labelid}"

            redirect_dir.mkdir(parents=True, exist_ok=True)
            (redirect_dir / "index.html").write_text(REDIRECT_TEMPLATE.format(url=url, name=name))

            fun_count += 1

    logger.info(f"config_redirects: generated {cfg_count} config redirect pages")
    logger.info(f"config_redirects: generated {cmd_count} command redirect pages")
    logger.info(f"config_redirects: generated {fun_count} function redirect pages")


def setup(app: Sphinx) -> dict:
    app.connect("build-finished", generate_redirects)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
