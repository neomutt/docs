NeoMutt Guide
=============

The official documentation for `NeoMutt <https://neomutt.org>`_, a
terminal-based email client.  Built with `Sphinx <https://www.sphinx-doc.org/>`_
and hosted on `Read the Docs <https://readthedocs.org/>`_.

.. image:: https://readthedocs.org/projects/neomutt/badge/?version=latest
   :target: https://neomutt.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Structure
---------

The guide follows the `Diátaxis <https://diataxis.fr/>`_ documentation
framework and is organised into four sections:

:Tutorials:     Step-by-step lessons for newcomers (10 pages)
:How-to guides: Task-oriented recipes for specific goals (62 pages)
:Reference:     Technical descriptions of configuration, commands, and
                functions (55 pages)
:Explanation:   Background discussion of concepts and design (14 pages)

Source material was converted from the DocBook XML manual
(``manual.xml``) that ships with the NeoMutt source code.

Building locally
----------------

Prerequisites: Python 3.10+ and ``pip``.

.. code-block:: bash

   # Install dependencies
   pip install -r docs/requirements.txt

   # Build HTML
   make html

   # Open in a browser
   open build/html/index.html    # macOS
   xdg-open build/html/index.html  # Linux

The generated site is written to ``build/html/``.

Contributing
------------

Contributions are welcome.  Pages marked **[TEMPLATE]** contain outlines
that need to be fleshed out, and pages with **📷 Screenshot Needed**
markers are waiting for terminal screenshots.

Please keep the Diátaxis style conventions noted at the top of each page.

Links
-----

- **NeoMutt website:** https://neomutt.org
- **NeoMutt source:** https://github.com/neomutt/neomutt
- **This documentation:** https://github.com/neomutt/neomutt (``guide`` branch)

License
-------

This documentation is licensed under the **GNU General Public License v2**,
the same license as NeoMutt itself.
