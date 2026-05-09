em_data
=======

.. _em-data:

The ``em_data.xlsx`` workbook is the **tabular root** of the Extended
Matrix — the place where the leaves of the knowledge tree live as
spreadsheet rows. Together with the GraphML file (the visual root) and
the JSON export (the publication root), it forms one of the three
file-shaped surfaces from which an ``s3D Graph`` can be reconstructed in
memory and from which all downstream artifacts (em-graph in yEd,
Heriverse JSON, the CIDOC triplestore) are derived.

This page is the canonical reference for the workbook itself: its
sheets, its conventions, and the contracts each concept page (Property,
Document, Author, License, Activity, Location, …) satisfies when it
projects itself onto a column.

.. note::

   This is a *living* reference. The base shape (5 sheets, the
   ``Units`` / ``Epochs`` / ``Claims`` / ``Authors`` / ``Documents``
   skeleton already described in :doc:`knowledge_tree`) is stable. The
   per-concept column contracts are the edge that grows: each new
   concept page in this manual closes one such contract. Readers
   following an older revision of the workbook should look at the
   *concept* pages first — they are now the source of truth for which
   columns belong to which concept.


Why a tabular companion to the graph?
--------------------------------------

The graph is good at structure: nodes, typed arcs, propagation rules.
A spreadsheet is good at the leaves: descriptions, dates, dimensions,
literature references — the long-form data that no graph editor can
edit pleasantly. ``em_data.xlsx`` is the *single* place where those
leaves live, so that:

- Humans can author them with familiar tools (Excel, LibreOffice,
  Google Sheets, ``pandas``).
- AI extractors (StratiMiner is the canonical one — see
  :doc:`knowledge_tree`) can produce them as their natural output.
- The s3Dgraphy ``UnifiedXLSXImporter`` can ingest them into an
  in-memory ``s3D Graph`` from which a GraphML, a JSON, or a CIDOC
  triplestore can all be regenerated deterministically.

The contract is bidirectional: the workbook is *both* an input format
(plant the matrix from a spreadsheet) and an output format (export the
in-memory graph back into a workbook for hand-editing). Round-trip is
preserved as long as you stick to the conventions on this page.


Workbook shape
--------------

The base ``em_data.xlsx`` has five sheets:

.. list-table::
   :header-rows: 1
   :widths: 18 82

   * - Sheet
     - Purpose
   * - ``Units``
     - One row per stratigraphic unit (real or virtual): ID, type
       (US / USVs / USVn / SF / VSF / USD …), description,
       interpretation, building technique, materials, dimensions, and
       the per-concept columns described below (epochs, locations,
       activities, …).
   * - ``Epochs``
     - The temporal scaffolding: epoch ID, name, ``start`` / ``end``,
       description. Referenced from ``Units`` and from per-property
       temporal stamps.
   * - ``Claims``
     - The paradata layer: each row is one interpretive claim about a
       Unit (e.g. an attribution of dimension, a chronological
       inference, a building-technique determination), with the
       ``Authors`` and ``Documents`` that justify it.
   * - ``Authors``
     - Registry of human and AI authors. Referenced by ID from
       ``Claims`` and from header metadata.
   * - ``Documents``
     - Registry of source documents (photographs, reports, drawings,
       analyses), with role / content_nature / geometry classifiers
       and a relative path into ``DosCo/``. Referenced by ID from
       ``Claims`` and from interpretive columns.

For the broader project layout (``my_project.graphml`` /
``em_data.xlsx`` / ``source_list.xlsx`` / ``DosCo/``) see
:doc:`nodes_intro` and :doc:`project_organization`.


Authoring conventions
---------------------

Three small conventions make the workbook robust under round-trip and
under collaboration. Every concept page in this manual assumes them.

Multi-valued cells
~~~~~~~~~~~~~~~~~~

When a column accepts more than one value, values are separated by
**semicolon** (``;``) with a single space after each separator:

.. code-block:: text

   topo:Pompei; study:Saggio4/A2; func:Casa_del_Fauno/Room12

Trailing semicolons are tolerated. Quoting is not required — the
separator is reserved.

Hierarchical paths
~~~~~~~~~~~~~~~~~~

When a value is hierarchical, the levels are joined by **forward
slash** (``/``), root first, with no surrounding spaces:

.. code-block:: text

   Pompei/Sector_4/Casa_del_Fauno/Room_12

Slashes inside a single level are not supported — use underscores or
camel case to disambiguate.

Kind prefixes
~~~~~~~~~~~~~

When a column carries values that belong to multiple *epistemic
planes*, each value is prefixed with a short kind tag and a colon.
The Location concept uses this convention with three tags
(``topo:``, ``study:``, ``func:``); the same pattern is reused by
other concepts that need plane-discrimination on the same axis. See
the relevant concept page for the tag vocabulary.

Primary value
~~~~~~~~~~~~~

When a column accepts multiple values *and* the formalism allows one
of them to be primary (the typical case for membership relations
rendered as yEd group folders in em-graph), **the first value is
treated as primary** by default. Concept pages that override this
default say so explicitly.


Concept-by-concept projection
------------------------------

Each concept formalised in this manual describes its own column
contract on its dedicated page. The pages currently closed are:

.. list-table::
   :header-rows: 1
   :widths: 22 22 56

   * - Concept
     - Sheet · column(s)
     - Manual page
   * - Location
     - ``Units`` · ``location_paths``
     - :doc:`location`
   * - Activity
     - ``Units`` · ``activity_path``
     - :doc:`activity`
   * - *(more to come)*
     -
     - This list grows as concept pages migrate to the new template.

If you are looking for a column that does not appear above yet, the
authoritative source is the column header in the workbook produced by
``s3dgraphy``'s exporter; the concept-page contracts will catch up
during the EM 1.5 / 1.6 documentation refactor.


Round-trip with AI extraction
------------------------------

The :doc:`knowledge_tree` page describes how an ``em_data.xlsx`` can
be produced by AI from PDFs and field notes via the StratiMiner
prompt. The conventions on this page are the contract that the AI
output is held to: a workbook produced by StratiMiner that respects
multi-valued cells, hierarchical paths, and kind prefixes is
ingestible by s3Dgraphy's ``UnifiedXLSXImporter`` without manual
post-processing. Concept pages that introduce a new column also
publish, on their pages, the prompt fragment that StratiMiner uses
to populate it.


.. seealso::

   - :doc:`knowledge_tree` — the wider metaphor: graph as trunk,
     workbook as one of the three roots, AI / yEd / pyArchInit as
     entry points.
   - :doc:`nodes_intro` — the project-folder shape that hosts
     ``em_data.xlsx`` alongside the GraphML and the ``DosCo/``
     directory.
   - :doc:`location` — first concept page that closes a column
     contract on this template.
