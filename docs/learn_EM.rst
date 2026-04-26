
Learn EM
========

The path to learn and use EM depends on your scope and your background. Pick the entry that fits where you are now — none of them is "harder" than another, they just emphasise different parts of the same workflow. Each section below ends with a **Take action** block: a short, concrete thing you can do today to get your hands on the method.

1. EM formal language (for smart humanists)
-------------------------------------------

This is where every EM journey starts. The EM language is a typed graphical notation — nodes for stratigraphic units, sources, paradata; arcs for stratigraphic and provenance relations — that you can read and write *by hand*, with a pencil on paper, before any software is involved. The relevant sections of this site walk through each node type and connector. Crucially, EM is **not** a programming language: it is a notation for describing archaeological evidence and the reasoning that turns it into a reconstruction.

.. tip::

   The reference repository, with example cards, node icons, templates and assets, is at https://github.com/zalmoxes-laran/ExtendedMatrix/tree/EM_1.5_dev/

.. admonition:: Take action — *learn by doing with yEd*
   :class: tip

   yEd is the free graph editor most EM authors use to draw GraphML files with the EM palette. A 30-minute hands-on:

   1. Install yEd from `yworks.com <https://www.yworks.com/products/yed>`__.
   2. Import the EM palette (instructions in the `EM Tools manual — Importing the EM palette <https://docs.extendedmatrix.org/projects/EM-tools/en/latest/installation.html#importing-the-em-palette-in-yed>`__).
   3. Drag the EM canvas onto the workspace and fill in the metadata (site code, author, ORCID, licence).
   4. Add two stratigraphic units and connect them with the appropriate stratigraphic relation.
   5. Save as ``.graphml`` — that file is already a valid Extended Matrix.

   Then come back to :doc:`stratigraphic_nodes` to read what you just drew.

2. Annotate stratigraphy on 3D models (for jedi-humanists)
----------------------------------------------------------

If you want to connect EM documentation to 3D models, learn one tool from the **EM Framework (EMF)** beyond yEd: the **EM Tools** add-on for Blender. With it, an EM graph drawn in yEd becomes a navigable, queryable 3D scene where every stratigraphic unit lights up next to its proxy. The full manual is at the `EM Tools docs <https://docs.extendedmatrix.org/projects/EM-tools/en/latest/index.html>`__.

When you are ready to *publish* a reconstruction with its full paradata chain, the EMF web platform that closes the loop is **Heriverse** — the Heritage Science Metaverse — which opens any EM-aware scene in a browser, with epoch switching, source pop-ups, and collaborative VR. See the `Heriverse documentation <https://docs.extendedmatrix.org/projects/heriverse/en/latest/>`__. (The underlying conceptual model, *StratiVerse*, is the topic of separate scientific papers; it is what makes Heriverse possible, but you do not need to learn it to use the platform.)

.. note::

   Many users work in teams, splitting the effort across two or more members (for example, one drawing the EM in yEd, one annotating in Blender). EM is built for collaboration: every node carries author, licence and embargo metadata so contributions stay traceable.

.. admonition:: Take action — *open a real graph in Blender*
   :class: tip

   1. Install EM Tools (`installation guide <https://docs.extendedmatrix.org/projects/EM-tools/en/latest/installation.html>`__).
   2. Download an example dataset from the `Extended Matrix download page <https://www.extendedmatrix.org/download>`__ — pick one with a ``.graphml`` and a ``DosCo`` folder.
   3. In Blender, open the EM Setup panel, point it at the ``.graphml`` and the ``DosCo`` folder, and press *Reload*.
   4. Browse the units in the Stratigraphy Manager, switch the Visual Manager to *Epochs* mode, and watch the scene change as you click on different time slices.

   For a guided walk-through, follow :doc:`tutorials/13-first-matrix-creation <em-tools:tutorials/13-first-matrix-creation>` in the EM Tools manual.

3. Prepare high-quality 3D models for EM workflows
--------------------------------------------------

Good EM annotations need good 3D models underneath. The **3D Survey Collection (3DSC)** is the EMF toolset that helps you build them: workflow management for photogrammetry (Metashape, Reality Capture in progress), level-of-detail handling, metadata propagation, and direct integration with EM Tools. It runs entirely on modest hardware and is designed for archaeologists, not for visual-effects studios — so don't be put off by the words "3D survey". The complete documentation is `here <https://docs.extendedmatrix.org/projects/3DSC/en/latest/>`__.

.. note::

   High-quality 3D models — accessible even on a laptop through 3DSC — are what make stratigraphic annotation *direct on the model* possible, instead of going through 2D drawings. They are also what makes Heriverse exports beautiful.

.. admonition:: Take action — *try 3DSC on one wall*
   :class: tip

   You don't need a whole site. Pick a single feature you have already photogrammetered (one wall, one trench section, one find), bring it into 3DSC and let the LOD pipeline produce a clean low-poly proxy. That single object, used as a proxy in EM Tools, is enough to feel the difference.

4. Customize EM for your workflow
---------------------------------

Contributing to add features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to contribute features to EM:

* **For EM Tools in Blender** — start with the Python-for-Blender introduction `here <https://www.youtube.com/watch?v=rKGNc6CQ2cg>`__ (Italian, English subtitles) and ask the community on `Telegram <https://t.me/UserGroupEM>`__ or `Facebook <https://www.facebook.com/groups/extendedmatrix>`__.
* **For s3dgraphy** — see the `Contributing Guidelines <https://github.com/zalmoxes-laran/s3dgraphy/blob/main/CONTRIBUTING.md>`__ on GitHub.

Porting EM to other platforms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To bring EM to platforms beyond Blender — Revit, 3ds Max, Unity, Unreal — the recommended path is the **s3dgraphy** Python library. s3dgraphy is the computational implementation of EM as a property knowledge graph (GraphML / JSON), extracted from EM Tools so it can live anywhere Python runs. You write the visual layer for your platform; s3dgraphy enforces the EM data model under the hood. Full reference and examples in the `s3dgraphy documentation <https://docs.extendedmatrix.org/projects/s3dgraphy/>`__ *(under construction)* and in the `s3dgraphy repository <https://github.com/zalmoxes-laran/s3dgraphy>`__.

.. admonition:: Take action — *write a 20-line Python script*
   :class: tip

   ``pip install s3dgraphy``, load an existing ``.graphml``, list every US with its first epoch, dump it as CSV. If that script runs, you have everything you need to bind s3dgraphy to any host platform.

The EM Framework (EMF)
----------------------

When the documentation talks about *the framework*, it means the family of tools that all speak the same EM data model through s3dgraphy. As of EM 1.5:

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Component
     - Role
   * - **EM** (this manual)
     - The formal language. The notation you read and write.
   * - **s3dgraphy**
     - Python library. The shared data model that every other component speaks.
   * - **EM Tools** (Blender)
     - 3D visualisation, annotation, paradata authoring, export. `Manual <https://docs.extendedmatrix.org/projects/EM-tools/en/latest/>`__.
   * - **3D Survey Collection (3DSC)**
     - Photogrammetry pipeline and 3D model preparation upstream of EM Tools. `Manual <https://docs.extendedmatrix.org/projects/3DSC/en/latest/>`__.
   * - **Heriverse**
     - Web-based publication and collaborative VR for EM-aware scenes. `Manual <https://docs.extendedmatrix.org/projects/heriverse/en/latest/>`__.
   * - **ATON 3**
     - Web visualisation framework underpinning Heriverse. `GitHub <https://github.com/phoenixbf/aton>`__.
   * - **pyArchInit connector**
     - Imports Harris matrices and field records from pyArchInit into EM. See the `EM Tools tutorial <https://docs.extendedmatrix.org/projects/EM-tools/en/latest/tutorials/15-pyarchinit-external-data.html>`__.

.. note::

   s3dgraphy is in active development; version 1.0 with full multi-platform support is on the roadmap. For status see the `s3dgraphy roadmap <https://github.com/zalmoxes-laran/s3dgraphy/blob/main/ROADMAP.md>`__.
