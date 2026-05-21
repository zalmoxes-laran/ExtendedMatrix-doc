Extended Matrix — Documentation
===============================

Sphinx sources for the Extended Matrix (EM) manual. The rendered
documentation is published at
`docs.extendedmatrix.org <https://docs.extendedmatrix.org/>`_ and
hosted on Read the Docs.

This branch tracks **EM 1.6 — in development**; the rendered output is
served at https://docs.extendedmatrix.org/en/1.6/. For the latest
stable release of the manual see the
`EM 1.5 documentation <https://docs.extendedmatrix.org/en/1.5/>`_.

About Extended Matrix
---------------------

The Extended Matrix (EM) is a scientific method and formal language for
the Cultural Heritage domain. It is based on knowledge graph networks
and grounded on FAIR and Open Science principles. EM formalises complex
interpretative philological phenomena — such as virtual reconstructive
hypotheses — in a transparent and robust manner, enabling
verifiability of results, reusability of data and collaborative
interpretation.

For the methodology repository, palettes, templates and the
ecosystem-wide README see the
`main EM repository <https://github.com/zalmoxes-laran/ExtendedMatrix>`_.
For the broader project home, see
`extendedmatrix.org <https://extendedmatrix.org>`_. The 1.6 line is
under active development; expect topics to be added, renamed or
restructured as the release matures.

Branch model
------------

One branch per release line. Each branch builds an independent version
of the manual on Read the Docs.

============  ================================================  ===========================================
Branch        Release line                                      Published at
============  ================================================  ===========================================
``main``      Landing / aggregator                              ``docs.extendedmatrix.org``
``1.5.0``     Current LTS — EM 1.5 (latest stable)              ``docs.extendedmatrix.org/en/1.5/``
``1.4.0``     Legacy LTS — EM 1.4                               ``docs.extendedmatrix.org/en/1.4.0/``
``1.6``       **Development — EM 1.6 (this branch)**            ``docs.extendedmatrix.org/en/1.6/``
============  ================================================  ===========================================

Repository layout
-----------------

::

    docs/                 # Sphinx sources
        conf.py           # Sphinx configuration (entry point for RTD)
        index.rst         # Manual entry point
        *.rst             # Per-topic pages (nodes, connectors, paradata, ...)
        cookbook/         # Worked examples
        learn-em/         # Tutorial track
        mini_tutorials/   # Short how-tos
        img/              # Figures
        requirements.txt  # Sphinx build dependencies
    .readthedocs.yaml     # Read the Docs build configuration
    README.rst            # This file

Building the manual locally
---------------------------

The manual is a standard Sphinx project. From the repository root:

.. code-block:: bash

    python -m venv .venv
    source .venv/bin/activate           # on Windows: .venv\Scripts\activate
    pip install -r docs/requirements.txt
    cd docs
    make html                           # output in docs/_build/html

Open ``docs/_build/html/index.html`` in a browser to preview.

For a clean rebuild, run ``make clean html``. The same build is
reproduced by Read the Docs using ``.readthedocs.yaml`` — Python 3.12
on Ubuntu 22.04, with ``docs/requirements.txt`` as the dependency set.

Contributing
------------

Documentation contributions are welcome — fixes, clarifications, new
examples, translations.

1. Open or pick up an issue describing the change.
2. Fork the repository and create a feature branch off the appropriate
   release branch: ``1.6`` for upcoming-release content (this branch),
   or ``1.5.0`` for fixes against the current stable manual.
3. Edit the relevant ``.rst`` file under ``docs/``. Keep changes
   focused: one topic per pull request makes review easier.
4. Build locally (``make html``) and check that your pages render
   without Sphinx warnings.
5. Open a pull request against the same release branch you forked
   from. Cross-port to other release branches is handled on a
   case-by-case basis after review.

Questions and discussion happen on the
`Telegram open-group <https://t.me/UserGroupEM>`_ and on the
`main EM repository <https://github.com/zalmoxes-laran/ExtendedMatrix>`_.

Citation
--------

If you cite the EM methodology in academic work, use the canonical
Zenodo DOI:

.. code-block:: bibtex

    @misc{demetrescu_extendedmatrix_nodate,
      title     = {{ExtendedMatrix}},
      author    = {Demetrescu, Emanuel},
      publisher = {Zenodo},
      doi       = {10.5281/zenodo.5957132},
      url       = {https://doi.org/10.5281/zenodo.5957132},
    }

License
-------

See the `main EM repository
<https://github.com/zalmoxes-laran/ExtendedMatrix>`_ for the project
license. Documentation contributions are accepted under the same
terms.
