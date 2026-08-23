Glossary
========

This page collects the **formal terms** used by the Extended Matrix
language. Each entry points back to the main chapter that defines the
concept in detail; this glossary is meant as a quick-lookup reference,
not as a substitute for the chapters themselves.

.. note::

   **Editors:** keep entries short (1–3 sentences). The canonical
   definition lives in the linked chapter — this page only restates the
   gist and points there.

.. glossary::
   :sorted:

   Extended Matrix (EM)
   EM
      The formal language for documenting stratigraphy and virtual
      reconstruction processes in cultural heritage. Defined as a typed
      visual notation drawable in yEd or producible programmatically
      via :term:`s3Dgraphy`. See :doc:`stratigraphic_approach`.

   Extended Matrix Framework (EMF)
      The set of open-source software tools that operationalise the EM
      language: the :term:`yEd palette`, :term:`EM Tools for Blender`,
      :term:`3DSC`, :term:`Heriverse` and the :term:`s3Dgraphy` library
      that holds them together. See the
      `framework overview <https://www.extendedmatrix.org/about>`__.

   Extended Matrix Ecosystem
      The combined whole of the formal language and its toolset:
      :term:`EM` (the language) together with the
      :term:`Extended Matrix Framework (EMF)` (the open-source toolset
      that operationalises it — :term:`yEd palette`,
      :term:`EM Tools for Blender`, :term:`s3Dgraphy`,
      :term:`Heriverse`, :term:`3DSC`). Used when you need to refer to
      the entire EM-aware stack as a single thing.

   EM Tools for Blender
   EM Tools
      The open-source Blender add-on that connects an :term:`EM graph`
      to 3D content inside Blender — browse stratigraphic units, link
      proxies, drive visualisation by epoch and property, export to
      :term:`Heriverse` and CSV. Part of the
      :term:`Extended Matrix Framework (EMF)`. See the
      `EM Tools manual <https://docs.extendedmatrix.org/projects/EM-tools/>`__.

   3DSC
      3D Survey Collection — the open-source Blender add-on (with a
      companion Metashape pipeline) for managing photogrammetric and
      3D survey data: level-of-detail handling, texture baking, and
      asset preparation ready to be linked to an :term:`EM graph`.
      Part of the :term:`Extended Matrix Framework (EMF)`. See the
      `3DSC documentation <https://docs.extendedmatrix.org/projects/3DSC/>`__.

   yEd palette
      The palette of EM-typed nodes and arcs that turns yEd (a free
      graph editor) into an :term:`EM graph` authoring tool. The
      starting point for anyone drawing an EM by hand. Part of the
      :term:`Extended Matrix Framework (EMF)`.

   Stratigraphic Unit (US)
      The basic unit of archaeological stratigraphy: a discrete
      physical entity (a layer, a wall, a cut) recorded during
      excavation. EM extends this with virtual variants — see
      :doc:`stratigraphic_nodes`.

   Virtual Stratigraphic Unit (USV)
      A stratigraphic unit whose physical evidence is partial or
      absent and whose existence is inferred. Comes in two flavours
      — :term:`USVs` (with an in-situ anchor) and :term:`USVn`
      (pure typology). See :doc:`stratigraphic_nodes`.

   USVs
      A Virtual Stratigraphic Unit anchored to an in-situ
      archaeological remain. The anchor connects the inference back to
      tangible evidence. See :doc:`stratigraphic_nodes`.

   USVn
      A Virtual Stratigraphic Unit defined purely by typology — no
      in-situ anchor, the unit is reconstructed from comparanda and
      type-based reasoning. See :doc:`stratigraphic_nodes`.

   USD
      A Documented Stratigraphic Unit — a unit attested by
      bibliographic, archival or iconographic documentation rather
      than by direct excavation. See :doc:`stratigraphic_nodes`.

   Special Find (SF)
      A discrete object found in a stratigraphic unit, recorded as a
      separate entity (e.g. an inscription, a coin). See
      :doc:`auxiliary_stratigraphic_nodes`.

   Virtual Special Find (VSF)
      A nodegroup containing :term:`SF <Special Find (SF)>` fragments
      that have been reconstructed virtually. The VSF is a *container*,
      not a single reconstructed object. See
      :doc:`auxiliary_stratigraphic_nodes`.

   Transformation Stratigraphic Unit (TSU)
      A node type introduced in EM 1.4 (and refined in 1.5) for
      documenting *states* and *transformations* — decay, restoration,
      thematic surveys — rather than the original construction events.

   Property (Qualia)
      A typed paradata attribute attached to a stratigraphic unit —
      a measurable or qualitative value (length, material, dating,
      construction technique). Connected upstream to the
      :term:`Extractor` and :term:`Combiner` nodes that justify the
      value. See :doc:`qualia` and :doc:`paradata_nodes`.

   Document
      A primary source — a survey drawing, a photograph, a manuscript,
      a publication — referenced by an :term:`Extractor` to derive a
      :term:`Property (Qualia)`. See :doc:`source_node`.

   Extractor
      A paradata node representing the *act of extraction* of an
      attribute from a :term:`Document`. Materialises the
      "from-source-to-property" reasoning step. See
      :doc:`extractor_nodes`.

   Combiner
      A paradata node that *combines* multiple extractor outputs into
      a single :term:`Property (Qualia)` value, typically when a
      single value cannot be derived from a single source. See
      :doc:`paradata_group`.

   Paradata
      The reasoning that connects sources to interpretive results:
      what was used, how it was used, and what was concluded.
      Mandatory in EM — every reconstructive node must be backed by a
      paradata chain. See :doc:`paradata_nodes`.

   Activity
      An Activity Node Group — a set of stratigraphic units linked by
      a common operation (e.g. "construction of the apse"). See
      :doc:`activity`.

   Epoch
      A named time horizon used to attribute and filter stratigraphic
      units (``has_first_epoch`` / ``has_last_epoch``). It is the
      temporal counterpart of a *swimlane* in the :term:`Canvas` —
      every node that belongs to that period is contained within its
      swimlane, which acts as the visual home of the epoch in the
      :term:`EM graph`. Epochs are not stratigraphic units themselves;
      they are the calendar against which units are placed. See
      :doc:`canvas`.

   Canvas
      The yEd surface where the :term:`EM graph` is authored. Carries
      the metadata used by the framework — site code, epoch palette,
      author, licence — typically inside an ``SL_PD`` nodegroup, and
      organises nodes by :term:`Epoch` through swimlanes. See
      :doc:`canvas`.

   EM graph
      The **visual notation** of an Extended Matrix — the typed nodes
      and arcs as drawn on paper, in yEd with the :term:`yEd palette`,
      or produced by AI-extraction workflows. The human-readable face
      of EM. Distinct from the in-memory :term:`S3D Graph` that
      :term:`s3Dgraphy` builds from it.

   Knowledge Graph
      The underlying property graph encoded by an :term:`EM graph`,
      made programmatically accessible via :term:`s3Dgraphy` as an
      :term:`S3D Graph`. See :doc:`knowledge_tree`.

   s3Dgraphy
      The open-source Python library that handles the mapping between
      tool-specific data formats (GraphML, JSON, XLSX) and the
      Stratigraphic :term:`Knowledge Graph`. It is the *package* — the
      runtime artifact it produces is the :term:`S3D Graph`. Used by
      every framework component (:term:`EM Tools for Blender`,
      :term:`Heriverse`, :term:`3DSC`) for any programmatic access to
      EM data. See the index page of this manual.

      *See also:* the long-term perspective for this work — its
      formalisation as a CIDOC-CRM family extension for stratigraphy
      and virtual reconstruction — carries the working name **CRMem**
      (formerly *CRM-s3D* / *CIDOC-S3D*). Its current formal draft is
      the ``em:`` namespace declared in ``em.ttl`` (s3Dgraphy,
      dereferenceable via w3id.org/em/); the ``s3d:`` namespace
      remains reserved for library-internal terms that are not part
      of the ontology.

   pyArchInit
      An open-source `QGIS <https://qgis.org>`_ plugin for archaeological data
      management, with particular strength in 2D GIS visualization of
      stratigraphic data. Maintained by an active community led by Luca Mandolesi.
      In the Extended Matrix ecosystem, pyArchInit projects are consumed through
      the `s3Dgraphy <https://github.com/zalmoxes-laran/s3Dgraphy>`_ library,
      either by reference or by baking their records into the EM graph.
      See the :doc:`cookbook/pyarchinit_integration` recipe for the integration
      workflow and the :doc:`ecosystem` registry entry.

   S3D Graph
      The **in-memory property graph** produced by :term:`s3Dgraphy`.
      It is the runtime data structure with all methods for reading,
      writing and querying stratigraphic relationships, and is
      serialisable to JSON. Distinct from the visual notation
      (:term:`EM graph`) which is the human-readable face — the S3D
      Graph is the machine-processable face of the same knowledge.

   Heriverse
      The web-based publication platform of the EM Framework — turns
      :term:`EM graphs <EM graph>` and 3D content into navigable,
      paradata-aware online experiences. The public product name; the
      underlying conceptual model is :term:`StratiVerse` (used in
      academic papers and internal manuals). See the
      `Heriverse documentation <https://docs.extendedmatrix.org/projects/heriverse/en/1.5/>`__.

   StratiVerse
      The conceptual model that underlies the :term:`Heriverse`
      product. Referenced in academic papers and internal manuals;
      the public tool name is **Heriverse**.

.. note::

   **Editors:** when you add a new term, place its short definition
   here and link to the chapter where the full discussion lives.
   Avoid redefining concepts in two places — the chapter is
   authoritative; the glossary entry is the lookup.
