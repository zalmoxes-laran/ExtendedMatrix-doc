EM workspace preparation
========================

.. _em_workspace_preparation:

Before authoring an Extended Matrix project, three preparatory artifacts need
to live on your file system, alongside any tooling you'll use. They belong to
the EM language itself, not to a specific tool — set them up once at the start
of a new project, and iterate on them as your evidence base grows.

This page is the canonical "before you start" checklist. The full repository
layout for production projects is documented in :doc:`project_organization`;
this page focuses on the *minimal* preparation that every EM project shares,
so the picker, EM Tools, yEd and Heriverse all find what they expect.

Standard folder structure
-------------------------

Extended Matrix expects a specific folder layout for any project workspace.
A reference structure is provided as a downloadable zip — unzip it at the
root of a new project to obtain the canonical tree.

.. admonition:: Download the workspace template
   :class: note

   `EM_FolderTree_v1.5.zip <https://github.com/zalmoxes-laran/ExtendedMatrix/raw/refs/heads/EM_1.5_dev/07_FolderTree/EM_FolderTree_v1.5.zip>`_
   — the canonical folder tree maintained in the Extended Matrix repository.

The minimal shape every EM project shares looks like this:

.. code-block:: text

   my_project/
   ├── my_project.graphml          # the EM graph (yEd / em_data.xlsx output)
   ├── source_list.xlsx            # the source register
   ├── em_data.xlsx                # optional tabular authoring companion
   ├── DosCo/                      # the document collection
   │   ├── D.01_first_document.pdf
   │   ├── D.02_aerial_photo_1972.jpg
   │   └── ...
   └── (additional project folders — see project_organization.rst)

The full v1.5 production layout (``00_Quick_Views/``, ``01_Archival_Sources/``,
``05_Reality_Based_Data/`` and so on) is the recommended structure for
multi-year fieldwork. For a first project, a small replica, or a teaching
exercise, the four pieces above are enough — and every EM-aware tool will
work with them.

The DosCo folder
----------------

**DosCo** (Dossier Comparativo / Document Collection) is a folder where you
place every file that you want to elevate to the rank of *document* within
the EM graph: PDFs, images, historical photographs, 3D models, drawings,
written sources. Anything that will serve as evidence in your reconstruction.

You do **not** put every file you have into DosCo — only the ones you intend
to cite in the graph as documents. The graph references documents from this
folder by their identifier (see below). At any later moment you can elevate
an additional file to document status from within EM Tools in Blender; this
preparatory step simply seeds the initial collection.

Naming convention
~~~~~~~~~~~~~~~~~

Every file in DosCo carries a sequential identifier with the prefix ``D.``:

.. code-block:: text

   DosCo/
   ├── D.01_first_document_label.pdf
   ├── D.02_aerial_photo_1972.jpg
   ├── D.03_excavation_drawing.dwg
   └── ...

The label after the underscore is freeform — pick whatever is most informative
to you. The graph references the document by its ``D.NN`` identifier, so the
descriptive label is for human readability only.

.. note::

   The ``D.NN`` identifier is the *single* link that propagates from the
   :doc:`Source List <source_node>` to the file on disk and to the Document
   node in the graph. Keep the prefix stable once assigned — the rest of the
   filename can be renamed freely.

The ``source_list.xlsx`` register
---------------------------------

Alongside the DosCo folder, keep a **source_list.xlsx** spreadsheet (Microsoft
Excel or LibreOffice Calc, saved as ``.xlsx``) that catalogs each document in
DosCo with structured metadata: identifier, description, citation/URL, type,
which properties the source can validate, and any other field your project
needs.

This register is the canonical source of truth for what's in DosCo. When you
later import the sources into the graph via EM Tools (EMdb), the register is
the file you point the import to.

.. admonition:: Download the source_list.xlsx template
   :class: note

   The current template lives in the Extended Matrix repository under
   `03_Sources_list <https://github.com/zalmoxes-laran/ExtendedMatrix/tree/EM_1.5_dev/03_Sources_list>`_.
   Place the file at the root of your project, next to the ``.graphml``,
   and rename it ``source_list.xlsx``.

The column schema (Name / Description / Url / Property that can validate /
original id. / Type / Preview / Notes) is documented in detail in
:ref:`source-list-schema`. For a new project, the only columns you cannot
skip are **Name** (``D.NN``), **Description** and **Type** — the rest can be
filled in iteratively as the dossier grows.

.. seealso::

   * :ref:`source-list-schema` — full column reference, including the
     *Property that can validate* column that drives the validation chain.
   * :doc:`source_node` — how the entries in the register become Document
     nodes in the graph.
   * :doc:`project_organization` — the full production folder structure,
     for multi-year fieldwork projects.

Why these three artifacts, set up now
-------------------------------------

Adopting the folder tree, the DosCo dossier and the ``source_list.xlsx``
register at the start of a project saves you from restructuring later. By
the time you open Blender to start modelling, your evidence base is already
organised and citable, and every tool downstream — yEd for drawing the
matrix, EM Tools for connecting it to proxies, Heriverse for publishing the
result — finds the files where it expects them.

The same three artifacts are also what makes an EM project shareable: zip
the folder, hand it to a collaborator, and they have everything they need
to open the graph and trace every document back to its source.
