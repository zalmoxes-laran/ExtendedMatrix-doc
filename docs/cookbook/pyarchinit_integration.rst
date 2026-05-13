PyArchInit ↔ Extended Matrix integration
=========================================

`PyArchInit <https://www.pyarchinit.org/>`_ is a QGIS-based archaeological
data management system widely used in the Italian archaeology community.
Since AI06 (release 5.5.0-alpha, 2026), PyArchInit ships an automatic
mapping layer to Extended Matrix via the s3dgraphy library: stratigraphic
records authored in PyArchInit can be exported as EM-compatible GraphML
files, and reimported with full round-trip identity preservation.

This page explains the architecture of the bridge from an EM author's
perspective. For PyArchInit's own documentation, please refer to the
project's official site:

- Main site: `pyarchinit.org <https://www.pyarchinit.org/>`__
- API documentation: `pyarchinit-api.readthedocs.io <https://pyarchinit-api.readthedocs.io/>`__
- Source repository: `github.com/pyarchinit/pyarchinit <https://github.com/pyarchinit/pyarchinit>`__

What the bridge does
--------------------

PyArchInit's stratigraphic table is mapped to Extended Matrix nodes
through a projector layer that lives inside PyArchInit. The mapping
preserves:

- **Stratigraphic units**: each row of ``us_table`` becomes an EM
  stratigraphic node (US, USV, etc.) with the appropriate node type
  derived from PyArchInit's typology field.
- **Activities**: PyArchInit's ``attivita`` column maps to EM
  ``ActivityNodeGroup`` (historical-intent semantics).
- **Spatial dimensions**: as of AI07 (planned release on top of
  s3dgraphy 0.1.41), spatial columns (``struttura``, ``area``,
  ``settore``, ``ambient``, ``saggio``, ``quad_par``) map to EM
  ``LocationNodeGroup`` with appropriate ``kind`` discriminators
  (``functional`` / ``study``).
- **Toponym chain**: from ``site_table.{nazione, regione, provincia,
  comune}``, an automatic recursive ``LocationNodeGroup(kind="toponym")``
  chain is generated.
- **Paradata**: site-level Author / License / Embargo paradata from
  PyArchInit's metadata fields (shipped since 5.4.0-alpha).

Round-trip integrity
--------------------

The bridge guarantees that an export → reimport cycle preserves the
``us_table`` byte-for-byte (validated by an integration test suite
contributed to s3dgraphy in pyarchinit/pyarchinit#5). This means: if
you author in PyArchInit, export to GraphML, open in yEd, save without
edits, and reimport into PyArchInit — your data is unchanged.

This is the cornerstone that allows PyArchInit and Extended Matrix
workflows to coexist: changes made in yEd (e.g., manual matrix
refinement) can be inspected and merged back into PyArchInit's
database when appropriate.

When to use this integration
----------------------------

- You already work with PyArchInit for excavation data management and
  want to add EM-style stratigraphic reasoning and reconstruction on
  top, without re-typing your data.
- You want to extract a previously-recorded PyArchInit dataset into
  EM for analysis or publication.
- You are publishing a multi-site or multi-period project and need
  to combine multiple PyArchInit databases into a unified EM workspace.

The bridge does not replace either system: it gives them a shared
language. PyArchInit remains the canonical authoring tool for field
recording; Extended Matrix remains the canonical environment for
reconstructive reasoning and publication.

Setting up the integration
--------------------------

The bridge code lives inside PyArchInit. Once you install PyArchInit
5.5.0-alpha or later, the EM export and reimport flows are available
from PyArchInit's own menu. There is no separate installation step
on the Extended Matrix side beyond having a recent EM Tools / s3dgraphy
release.

For technical details on the projector layer (target audience: developers
writing custom mappers for other databases), see the s3dgraphy
documentation on building consumer integrations.

See also
--------

- :doc:`../ecosystem` — version-agnostic registry of third-party tools
  that consume s3dgraphy (includes the canonical PyArchInit ecosystem
  entry with maintainer and licence metadata).
