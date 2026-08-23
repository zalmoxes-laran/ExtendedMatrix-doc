.. Proposed rewrite of docs/learn_EM.rst on the ExtendedMatrix-doc
   repo (renders to https://docs.extendedmatrix.org/en/1.5/learn_EM.html).

   Goal (audit 2026-07-01): align the manual's "Learn EM" landing to
   the site's /start triad (Archaeologist / Modeller / Developer) so a
   reader lands on the same three entry points across
   extendedmatrix.org and docs.extendedmatrix.org. Within the modeller
   path, split explicitly Survey specialist vs Basic modeller —
   they are two distinct personas in the 8-figures list on
   https://extendedmatrix.org/personas/ and were previously conflated
   under a single "3D modelling" umbrella.

   Structural changes from the current version:
     • Four numbered sections → three primary paths matching /start
       (Archaeologist / Modeller / Developer), plus a small "for team
       leads" pointer at the end (mirroring /start's meta-path 4).
     • The current #2 (annotate stratigraphy) and #3 (prepare 3D
       models) become the two explicit sub-paths of the Modeller
       track. Each carries its persona name (Survey specialist /
       Basic modeller) so the split is legible.
     • Each path adds a short "→ Also on the site" cross-ref to the
       corresponding /start entry point so readers can pivot between
       manual and site.
     • The trailing components table stays intact but is now framed
       as "The EM Ecosystem — EM + EMF" instead of "The EM Framework
       (EMF)" — since the umbrella term for the whole is "EM
       Ecosystem" and EMF specifically means the tool layer.
     • "Contributing" and "Porting to other platforms" are folded
       into the Developer path (they are what a developer DOES).

   Propagate to 1.6 branch after 1.5 lands (per repo rule that new
   content targets 1.6 only, but structural restructures of shared
   pages apply to both).

Learn EM
========

The path to learn Extended Matrix depends on your role in the project. Pick the entry that fits where you are now — none is "harder" than another, they emphasise different parts of the same workflow. Each section below ends with a **Take action** block: a short, concrete thing you can do today.

The same three paths are laid out visually on the site — see `Start on extendedmatrix.org <https://www.extendedmatrix.org/start/>`__ for the graphical version and cross-refs to the tools that support each.

1. For archaeologists — the formal language
-------------------------------------------

*Persona: Stratigrapher · Source Hunter · EM Drawer.*

This is where every EM journey starts. The EM language is a typed graphical notation — nodes for stratigraphic units, sources, paradata; arcs for stratigraphic and provenance relations — that you can read and write *by hand*, with a pencil on paper, before any software is involved. The relevant sections of this manual walk through each node type and connector. Crucially, EM is **not** a programming language: it is a notation for describing archaeological evidence and the reasoning that turns it into a reconstruction.

.. tip::

   The reference repository, with example cards, node icons, templates and assets, is at https://github.com/zalmoxes-laran/ExtendedMatrix/tree/EM_1.5_dev/

.. admonition:: Take action — *learn by doing with yEd*
   :class: tip

   yEd is the free graph editor most EM authors use to draw GraphML files with the EM palette. A 30-minute hands-on:

   1. Install yEd from `yworks.com <https://www.yworks.com/products/yed>`__.
   2. Import the EM palette (instructions in the `EM Tools manual — Importing the EM palette <https://docs.extendedmatrix.org/projects/EM-tools/en/1.5/installation.html#importing-the-em-palette-in-yed>`__).
   3. Drag the EM canvas onto the workspace and fill in the metadata (site code, author, ORCID, licence).
   4. Add two stratigraphic units and connect them with the appropriate stratigraphic relation.
   5. Save as ``.graphml`` — that file is already a valid Extended Matrix.

   Then come back to :doc:`stratigraphic_nodes` to read what you just drew.

→ Also on the site: `Start · Sources, stratigraphy, reconstruction <https://www.extendedmatrix.org/start/#1>`__ · `Tools for archaeologists <https://www.extendedmatrix.org/tools/#archaeologist>`__.

2. For 3D modellers — capture then annotate
-------------------------------------------

The modelling track has two distinct halves. They are two different professional figures in the EM personas list and are often held by two different team members. Read both — you may only own one, but knowing the other is what lets the handoff between them work.

2a. Prepare 3D models for EM workflows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Persona: Survey specialist.*

Good EM annotations need good 3D models underneath. The **3D Survey Collection (3DSC)** is the EMF toolset that helps you build them: workflow management for photogrammetry (Metashape, Reality Capture in progress), level-of-detail handling, metadata propagation, and direct integration with EM Tools. It runs on modest hardware and is designed for archaeologists, not for visual-effects studios — so don't be put off by the words "3D survey". This track also covers geophysical prospection and topographic survey (georadar, magnetometry, GNSS, total station, terrestrial LiDAR) — any capture that produces reality-based data the graph will annotate. The complete documentation is `here <https://docs.extendedmatrix.org/projects/3DSC/en/latest/>`__.

.. note::

   High-quality 3D models — accessible even on a laptop through 3DSC — are what make stratigraphic annotation *direct on the model* possible, instead of going through 2D drawings. They are also what makes Heriverse exports beautiful.

.. admonition:: Take action — *try 3DSC on one wall*
   :class: tip

   You don't need a whole site. Pick a single feature you have already photogrammetered (one wall, one trench section, one find), bring it into 3DSC and let the LOD pipeline produce a clean low-poly proxy. That single object, used as a proxy in EM Tools, is enough to feel the difference.

2b. Annotate stratigraphy on 3D models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Persona: Basic modeller (the Golden Twelve figure).*

Once you have a mesh from 2a — or one you've been handed by the survey specialist — you can connect EM documentation to it via the **EM Tools** add-on for Blender. With it, an EM graph drawn in yEd becomes a navigable, queryable 3D scene where every stratigraphic unit lights up next to its proxy. The full manual is at the `EM Tools docs <https://docs.extendedmatrix.org/projects/EM-tools/en/1.5/index.html>`__. The foundational Blender-modelling shortcuts you need — proxy modelling, control-point modelling, LOD work, semantic shapes — are covered by *The Golden Twelve*, a two-page reference card (`doi:10.5281/zenodo.21068528 <https://zenodo.org/records/21068528>`__).

When you are ready to *publish* a reconstruction with its full paradata chain, the EMF web platform that closes the loop is **Heriverse** — the Heritage Science Metaverse — which opens any EM-aware scene in a browser, with epoch switching, source pop-ups, and collaborative VR. See the `Heriverse documentation <https://docs.extendedmatrix.org/projects/heriverse/en/1.5/>`__. (The underlying conceptual model, *StratiVerse*, is the topic of separate scientific papers; it is what makes Heriverse possible, but you do not need to learn it to use the platform.)

.. note::

   Many users work in teams, splitting the effort across two or more members (for example, one drawing the EM in yEd, one annotating in Blender). EM is built for collaboration: every node carries author, licence and embargo metadata so contributions stay traceable.

.. admonition:: Take action — *open a real graph in Blender*
   :class: tip

   1. Install EM Tools (`installation guide <https://docs.extendedmatrix.org/projects/EM-tools/en/1.5/installation.html>`__).
   2. Download an example dataset from the `Extended Matrix download page <https://www.extendedmatrix.org/download>`__ — pick one with a ``.graphml`` and a ``DosCo`` folder.
   3. In Blender, open the EM Setup panel, point it at the ``.graphml`` and the ``DosCo`` folder, and press *Reload*.
   4. Browse the units in the Stratigraphy Manager, switch the Visual Manager to *Epochs* mode, and watch the scene change as you click on different time slices.

   For a guided walk-through, follow :doc:`tutorials/13-first-matrix-creation <em-tools:tutorials/13-first-matrix-creation>` in the EM Tools manual.

→ Also on the site: `Start · 3D models annotated with EM data <https://www.extendedmatrix.org/start/#2>`__ · `Tools for 3D modellers <https://www.extendedmatrix.org/tools/#modeller>`__.

3. For developers — extend, integrate, port
-------------------------------------------

*Persona: Information Technology specialist.*

EM is implemented as a Python knowledge-graph library (**s3dgraphy**) that you can plug into any platform — Revit, 3ds Max, Unity, Unreal, custom pipelines. s3dgraphy is the computational implementation of EM as a property knowledge graph (GraphML / JSON), extracted from EM Tools so it can live anywhere Python runs. You write the visual layer for your platform; s3dgraphy enforces the EM data model under the hood. Full reference in the `s3dgraphy documentation <https://docs.extendedmatrix.org/projects/s3dgraphy/>`__ *(under construction)* and in the `s3dgraphy repository <https://github.com/zalmoxes-laran/s3dgraphy>`__.

Contributing features back:

* **For EM Tools in Blender** — start with the Python-for-Blender introduction `here <https://www.youtube.com/watch?v=rKGNc6CQ2cg>`__ (Italian, English subtitles) and ask the community on `Telegram <https://t.me/UserGroupEM>`__ or `Facebook <https://www.facebook.com/groups/extendedmatrix>`__.
* **For s3dgraphy** — see the `Contributing Guidelines <https://github.com/zalmoxes-laran/s3dgraphy/blob/main/CONTRIBUTING.md>`__ on GitHub.

.. admonition:: Take action — *write a 20-line Python script*
   :class: tip

   ``pip install s3dgraphy``, load an existing ``.graphml``, list every US with its first epoch, dump it as CSV. If that script runs, you have everything you need to bind s3dgraphy to any host platform.

→ Also on the site: `Start · Extend, integrate, contribute <https://www.extendedmatrix.org/start/#3>`__ · `Tools for developers <https://www.extendedmatrix.org/tools/#developer>`__.

For team leads — building a team, scoping a project
---------------------------------------------------

Extended Matrix projects compose **eight canonical professional figures** — stratigrapher, source hunter, survey specialist, IT specialist, EM drawer, basic modeller, advanced modeller, storyteller. Most projects cover them with two or three real humans wearing several hats. Naming the figures explicitly is what lets a project scale beyond a single researcher. Competences are not silos: real work blurs the boundaries. What the eight personas offer is one *possible division of labour* to assign when a project grows.

→ See the full typology at `extendedmatrix.org/personas/ <https://www.extendedmatrix.org/personas/>`__.

The EM Ecosystem — EM + EMF
---------------------------

The **EM Ecosystem** is the umbrella that groups **EM** (this manual — the formal language) with the **EM Framework (EMF)** — the family of tools that speak EM through s3dgraphy. The two layers are distinct but complementary: EM is the notation; EMF is the toolset that reads, writes, visualises and publishes what the notation describes. As of EM 1.5:

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
     - 3D visualisation, annotation, paradata authoring, export. `Manual <https://docs.extendedmatrix.org/projects/EM-tools/en/1.5/>`__.
   * - **3D Survey Collection (3DSC)**
     - Photogrammetry pipeline and 3D model preparation upstream of EM Tools. `Manual <https://docs.extendedmatrix.org/projects/3DSC/en/latest/>`__.
   * - **Heriverse**
     - Web-based publication and collaborative VR for EM-aware scenes. `Manual <https://docs.extendedmatrix.org/projects/heriverse/en/1.5/>`__.
   * - **ATON 3**
     - Web visualisation framework underpinning Heriverse. `GitHub <https://github.com/phoenixbf/aton>`__.
   * - **pyArchInit connector**
     - Imports Harris matrices and field records from pyArchInit into EM. See the `EM Tools tutorial <https://docs.extendedmatrix.org/projects/EM-tools/en/1.5/tutorials/15-pyarchinit-external-data.html>`__.

.. note::

   s3dgraphy is in active development; version 1.0 with full multi-platform support is on the roadmap. For status see the `s3dgraphy roadmap <https://github.com/zalmoxes-laran/s3dgraphy/blob/main/ROADMAP.md>`__.
