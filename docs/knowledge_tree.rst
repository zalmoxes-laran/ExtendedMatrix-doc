The Knowledge Tree
===================

.. contents::
   :local:
   :depth: 2

A living metaphor
------------------

The Extended Matrix is best understood through the metaphor of a living tree.
The metaphor is *anthropocentric*: it organises the system around how a human
researcher reads, writes, and grows an Extended Matrix over time. It is built
up here in three additive stages — each figure is the previous one with a new
layer added. Same silhouette, same palette, more detail.

Throughout the chapter, *sap* stands for the data that flows through the tree:
it rises from the roots when you load a file, courses through the trunk while
EMtools and s3Dgraphy operate on it, reaches the leaves when external
containers are linked, and descends back to the roots when you save. The tree
is alive because the data flows in both directions.


Stage 1 — Trunk, branches, leaves
----------------------------------

.. figure:: img/knowledge_tree_stage1.png
   :width: 760
   :align: center

   Stage 1 — the basic anatomy of the Extended Matrix as a knowledge tree.

The **trunk** is the Extended Matrix itself: the formalism, the stratigraphic
structure, the chronology. Its fibres are the things that hold the matrix
together — the stratigraphic relationships of *overlies*, *cuts*, *fills*,
*abuts*, *bonds*, *equals*, and the temporal scaffolding of periods, phases,
and subphases. The trunk is what makes a matrix recognisable as an Extended
Matrix, and it is the part that is written most carefully and changed most
infrequently.

The **branches** are the node types that articulate from the trunk: ``US``,
``USVs``, ``USVn``, ``SF``, ``USD``, ``VSF``, and the others described in
:doc:`nodes_intro`. They are the structural arms of the formalism — the places
where data finds a meaningful home. A property has to attach somewhere; the
branches are the somewheres.

The **leaves** are the *external content* the matrix leans on. A leaf is any
container of information attached to a branch by reference — its content
lives outside the trunk, in its own ecosystem, and is *borrowed* by the tree
each time the project is opened. Leaves come in two visually similar but
technically distinct families:

- **Tabular leaves** — Excel/database/CSV containers that hold per-unit
  attributes. ``EMdb`` catalogs of stratigraphic units attach to the ``US``
  branch; ``pyArchInit`` rows attach to ``US`` or ``USVs``; the *source list*
  and the ``DosCo`` documentary folder attach to ``USD``. Their content is
  scalar, temporal, relational — the same kind of fibre the trunk's wood is
  made of.

- **Object-storage leaves** — non-tabular containers that hold content of a
  different nature: a Blender ``.blend`` scene with proxies and
  representational models, a 3DSC point-cloud catalogue, a folder of
  high-resolution photogrammetric meshes, an image library, a multimedia
  bundle. They attach to the branch that matches their semantics (a 3D
  proxy of a ``US`` to the ``US`` branch, a textured surface to ``USVs``
  or ``VSF``).

A single auxiliary system like ``EMdb`` commonly produces several leaves on
different branches at once — one per category of material — each attached
where it makes sense.

**Leaves are linked, not absorbed.** They live in their own containers and
are read into the in-memory ``s3D graph`` (the *living wood* of the trunk)
each time the project is opened. While the s3D graph is alive, the leaf's
content is accessible through the matrix as if it had always been there.
But at save time, *by default*, the leaf's content does **not** travel with
the trunk into its serialised forms (``em_data.xlsx``, ``GraphML``, ``JSON``,
and the forthcoming ``RDF/CIDOC`` triplestore): the auxiliary container
remains the source of truth, the trunk only borrows. Leaves can fall and
grow back without changing the trunk.

This default — *link, not absorb* — is itself a feature, not a limitation.
It lets a project run two ecosystems in parallel: the EM serialised stack
(``em_data.xlsx``, ``GraphML``, ``JSON``, ``RDF``) on one side, the external
stack (``pyArchInit``, ``EMdb``, ``DosCo``, ``Blender``, ``3DSC``, image
libraries) on the other — without forcing a fusion that neither side wants.
Authors keep editorial control on each stack and decide, leaf by leaf,
whether and when to commit to integration.

That deliberate decision to integrate is the *graft* (Stage 2).


Stage 2 — Grafts
-----------------

.. figure:: img/knowledge_tree_stage2.png
   :width: 760
   :align: center

   Stage 2 — Stage 1 plus the grafts: leaves the author has deliberately
   let take root.

A **graft** is a leaf the author has decided to *let take root* — to fuse
permanently with the trunk's wood. Where a leaf is a borrowing, a graft is
an integration: its content stops being a runtime reference and becomes part
of the matrix the next time the trunk is saved. The technical operation that
realises a graft is the **bake**: it reads the leaf's content and writes it
into the trunk's serialised forms (``em_data.xlsx``, ``GraphML``, ``JSON``,
``RDF/CIDOC``). After bake, the leaf is no longer a leaf — it is fibre.

Not every leaf is graftable. The constraint comes from what the trunk's
wood can hold:

- **Tabular leaves are graftable.** Their content is scalar, temporal,
  relational — exactly the kind of fibre the trunk is made of. Once baked,
  a tabular leaf's values are written into the serialised forms and travel
  with the matrix wherever it goes. The author can keep the original
  spreadsheet/database alive on the side; the matrix now also carries its
  own copy.

- **Object-storage leaves are not graftable, by construction.** A Blender
  mesh, a point cloud, a high-resolution image, a textured surface — none
  of these can fuse into a node-and-edge structure. They remain leaves
  forever: attached, accessible from the in-memory s3D graph, but never
  absorbed. The trunk holds a reference; the content stays in its own
  ecosystem. This is not a choice — it is the shape of the wood.

The grafting metaphor is not casual. A graft is something the gardener
*chooses*, joins, and tends. It carries content the trunk could not produce
on its own, and it earns its place in the tree by being deliberately let
take root.

.. note::

   The bake is reversible only in the weak sense that you can always
   restart from the auxiliary container if you have kept it around. Once
   the trunk has been saved with baked content, that content *is* fibre:
   there is no "un-bake" operation that surgically removes it from the
   serialised forms without manual editing.


Stage 3 — Roots
----------------

.. figure:: img/knowledge_tree_stage3.png
   :width: 760
   :align: center

   Stage 3 — Stage 2 plus the roots: the file formats from which the
   Extended Matrix draws its sap and into which it deposits it back.

The trunk is not a single file. The Extended Matrix is one entity expressed
in several **roots** — the file formats that the tree both draws from and
deposits back into:

- ``em_data.xlsx`` — the unified workbook with five sheets (``Units``,
  ``Epochs``, ``Claims``, ``Authors``, ``Documents``), produced by humans
  manually or by AI through the StratiMiner prompt. It is the root through
  which the matrix can be planted from scratch from documentary sources, or
  grown by patient hand from existing tabular data. The workbook's shape,
  authoring conventions (multi-valued cells, hierarchical paths, kind
  prefixes), and per-concept column contracts are documented on the
  dedicated :doc:`em_data` page — that is the canonical reference both
  for human authors and for the StratiMiner AI extractor.

- ``GraphML`` — the human-readable root, opened in yEd Graph Editor with the
  Extended Matrix palette. This is where humans see the matrix as a network
  they can read, edit, and reason about visually.

- ``JSON`` for Heriverse — the export root that feeds the public Heriverse
  environment, where the matrix becomes a navigable spatial-temporal
  experience.

- ``RDF / CIDOC`` triplestore — *forthcoming.* The semantic-web root that
  will let the matrix participate in the broader cultural-heritage knowledge
  graph, exposing its content through CIDOC-CRM mappings as triples,
  query-able through SPARQL.

The roots are bidirectional where round-trip makes sense. Sap rises when you
load (``em_data.xlsx`` → in-memory ``s3D Graph``; ``GraphML`` → ``s3D
Graph``), and it descends when you save (``s3D Graph`` → ``em_data.xlsx``;
``s3D Graph`` → ``GraphML``; ``s3D Graph`` → ``JSON``; ``s3D Graph`` →
``RDF``). The in-memory ``s3D Graph`` is the living wood of the trunk: the
moment-by-moment state of the tree, machine-actionable, the pivot through
which all roots communicate.

**What travels through the roots:** the trunk's own fibre — the EM formalism,
its branches, the stratigraphic structure — *plus* any **baked grafts** that
have been integrated into it. These elements move freely between
``em_data.xlsx``, ``GraphML``, ``JSON`` and ``RDF`` — wherever you save,
they follow.

**What does not travel:** plain leaves that have not been let take root. At
each new session they reload from their own auxiliary containers, just as
before. **Object-storage leaves never travel** through the roots — they are
non-graftable by construction and stay anchored to the trunk by reference,
with their content untouched in its own ecosystem (a Blender ``.blend``,
a 3DSC catalogue, an image library).

This is what frees the modern Extended Matrix from any single canonical
file. You can enter through whichever root suits your work — AI-driven
extraction through ``em_data.xlsx``, manual stratigraphy through
``GraphML``/yEd, archaeological fieldwork through ``pyArchInit``, semantic-
web alignment through the triplestore — and the tree will still be the
same tree.


Two orthogonal dimensions
--------------------------

The figure now describes two things at once, and it is worth keeping them
distinct in your mind:

1. **Anthropocentric integration** (above ground): how a human researcher
   composes a complete Extended Matrix project — the trunk of the formalism,
   the branches of node types, the leaves of all external content (tabular
   and object-storage), and the grafts of those leaves the author has
   deliberately integrated. This is *what is in the matrix*.

2. **Representation and exchange** (below ground): how the matrix is
   serialised and shared — the roots of ``em_data.xlsx``, ``GraphML``,
   ``JSON``, and the forthcoming ``RDF/CIDOC`` triplestore. This is *how
   the matrix moves between formats and between people*.

These dimensions are independent. You can change which roots you use without
changing what is in the tree; you can let new leaves take root without
changing how the tree is serialised. Keeping them visually distinct (above
the ground line vs. below it) is a way of keeping them distinct in practice.


Working with leaves: linking and grafting in practice
------------------------------------------------------

In day-to-day work the leaves of a project are managed through ``EMtools``
and ``s3Dgraphy``. Each auxiliary type uses a specific *mapping* that
defines how its columns or fields translate to graph node properties. The
``s3Dgraphy MappingRegistry`` ships three default mappings — ``pyarchinit``,
``emdb``, ``generic`` — and supports custom project-specific mapping
directories.

The principle for the **default link mode** is *non-destructive enrichment*:
auxiliary data adds attributes to existing nodes; it does not alter the
trunk's structure, and it does not change the trunk's serialised forms at
save time. The auxiliary container keeps editorial autonomy; the matrix
just borrows the values while running. This is the right mode for data that
is still evolving — laboratory results that come in over months,
interpretations that get refined, image inventories that grow.

When a particular auxiliary becomes stable enough that you want it to be
permanently part of the matrix, you **bake** it: this promotes the linked
properties from runtime borrowings into trunk fibre, writing them into
``em_data.xlsx`` / ``GraphML`` / ``JSON`` / ``RDF``. From that point on the
values travel with the matrix wherever it goes, even if the original
auxiliary container is no longer at hand.

The bake is available only for tabular leaves — the kind of content the
trunk's wood can hold. Object-storage leaves stay linked forever, by
construction; they are accessed at runtime through the s3D graph but their
content never enters the trunk. That is a good thing: it keeps the trunk
small and the storage of large 3D / image content where it belongs.


Entering the tree: a practical summary
---------------------------------------

A reader who has followed the metaphor this far will want to know how to
actually start a project. The Extended Matrix can be entered through any of
its roots; the choice depends on the nature of the source material and on
the team:

- **Through** ``yEd`` **with the EM palette** — manual, traditional, ideal
  for small-to-medium projects where the stratigrapher builds the graph
  directly. See the
  `yEd workflow guide <https://docs.extendedmatrix.org/projects/EM-tools/en/1.5/creating_em.html#from-graphml-yed>`_.

- **Through** ``em_data.xlsx`` **via StratiMiner or by hand** — the unified
  workbook approach. AI extraction through the StratiMiner prompt populates
  the workbook from PDFs and field notes; alternatively a human team can
  fill it manually from existing tabular data. The s3Dgraphy
  ``UnifiedXLSXImporter`` parses the workbook into an in-memory ``s3D
  Graph`` and from there into ``GraphML``. The workbook itself — sheets,
  columns, authoring conventions, per-concept contracts — is documented on
  :doc:`em_data`, which is the contract that both human authors and
  StratiMiner are held to. See also the
  `Excel import guide <https://docs.extendedmatrix.org/projects/EM-tools/en/1.5/creating_em.html#from-excel-standard-stratigraphy>`_
  for the operational details on the EM Tools side.

- **Through** ``pyArchInit`` — the archaeological information system can
  export GraphML files in Extended Matrix format directly, bringing
  fieldwork records into the tree as a starting point. See the
  `pyArchInit documentation <https://pyarchinit.readthedocs.io/it/latest/novit%C3%A0.html#herris-matrix-per-extended-matrix-tool>`_.

Each entry point produces (or contributes to) the same trunk. From there
you link your leaves (tabular and object-storage) and let take root — by
baking — those that you want to integrate permanently.

.. seealso::

   - :doc:`em_data` — the canonical reference for the ``em_data.xlsx``
     workbook (sheets, conventions, per-concept column contracts)
   - :doc:`qualia` — the property taxonomy that lives along the branches
   - :doc:`paradata_nodes` — how data provenance is recorded along the trunk
   - :doc:`data_funnel` — the three-level data hierarchy
   - `Creating EM from Different Sources (EMtools docs) <https://docs.extendedmatrix.org/projects/EM-tools/en/1.5/creating_em.html>`_
