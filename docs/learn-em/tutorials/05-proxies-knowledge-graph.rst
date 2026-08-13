.. badge:: Full Course
   :color: blue

From 3D Models to Knowledge: Proxies and the Knowledge Graph
============================================================

.. raw:: html

   <!-- Replace VIDEO_ID with the actual YouTube video ID for 05_em_proxies_kg -->
   <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
   <iframe src="https://www.youtube.com/embed/VIDEO_ID_05_em_proxies_kg"
           style="position:absolute;top:0;left:0;width:100%;height:100%;"
           frameborder="0" allowfullscreen></iframe>
   </div>
   <p><em>▶ From 3D Models to Knowledge: Proxies and the Knowledge Graph (~~4 min)</em></p>

| **Clip:** 05  |  **Duration:** ~4 min  |  **Recording segment:** ~22:00 → ~26:00

----

Prerequisites
-------------

:doc:`02-data-lifecycle`, :doc:`../../../em-blender-tools-doc:tutorials/04-3dsc-site-scale`

Overview
--------

A 3D survey records geometry, not knowledge. The transition from photogrammetry to an EM happens by creating *proxies* — segmented volumes that represent stratigraphic units. EM uses a knowledge graph (not tables) allowing runtime queries, multi-temporal visualisation, and multiple interpretations.

And this is where "a proxy is knowledge" stops being a slogan and becomes a
piece of modelling. In EM 1.6 the proxy is a **property of the stratigraphic
unit** — the quale ``geometry`` — and not an object standing beside it. The
volume you segmented is the property's *payload* (a **semantic shape**: convex
hulls, spheres, or a ``.glb``); the property itself carries the assertion and,
crucially, the **chain of paradata** that justifies it.

That is the difference between a mesh and knowledge: a mesh is a shape, while a
property can be asked *how do you know?* — and answer.

.. figure:: /_static/screenshots/clip_05/0001_knowledge_vs_survey.jpg
   :alt: The key transition: a 3D survey records geometry, EM records knowledge.
   :width: 90%

   The key transition: a 3D survey records geometry, EM records knowledge.

Key Concepts
------------

- A 3D model is a *representation*; a proxy is *knowledge*.
- The proxy is a **property** of the unit (the quale ``geometry``), not a separate
  object: the shape is its payload, the paradata chain is its justification.
- Because it is a property, **one geometry can be synthesised from several
  sources** — two extractors and a combiner concluding in one shape.
- A region traced on a photograph or a drawing is itself evidence: **annotating is
  extracting**, and a 2D annotation can feed the geometry.
- EM uses a knowledge graph — not tables — for richer querying and temporal support.
- The same site can be represented at multiple epochs within one dataset.
- Stratigraphy applies beyond excavations: buildings, mosaics, vegetation all have it.

A worked example: the wall that no single source describes
-----------------------------------------------------------

A Roman wall survives in a basement. The recent photogrammetric survey covers it
accurately — but only the exposed face, because a modern partition hides the
rest. A 1931 photograph, taken before the partition was built, shows the whole
elevation but has no scale and no camera data.

Neither source gives you the wall. Together they do, and EM records exactly
that:

.. code-block:: text

   US101 ──has_property──▶ geometry ──has_semantic_shape──▶ the reconstructed volume
                              ▲
              has_data_provenance
                              │
                          combiner
                          ╱       ╲
                extractor           extractor
            "photogrammetric      "traced on the 1931 photograph"
             survey, 2024"            │
                                      │ extracted_from
                                      ▼
                              the annotated region

Read it aloud and it is an argument: *the geometry of US101 is this volume,
because a 2024 survey gave us the exposed face and a 1931 photograph — where we
traced the wall's outline — gave us the part now hidden, and the two were
reconciled.*

The traced outline is a first-class element (an **AnnotationRegion**): a region
of one image, recorded in coordinates relative to the picture rather than in
pixels, so it survives the photograph being re-scanned at another size. It is
*interpretation, not raw evidence* — deciding "this and not that" is already
interpreting — and it can be cited by more than one reading: two scholars may
trace the same brick and disagree about it, which is one region and two claims.

.. note::

   Modelled this way, "what do we actually know about this wall?" is a question
   the graph can answer at runtime, source by source. That is the whole reason
   the proxy stopped being a lone volume.

Screenshots
-----------

.. figure:: /_static/screenshots/clip_05/0002_proxy_volumes_on_model.jpg
   :alt: Coloured proxy volumes overlaid on the 3D photogrammetric model.
   :width: 90%

   Coloured proxy volumes overlaid on the 3D photogrammetric model.

.. figure:: /_static/screenshots/clip_05/0003_knowledge_graph_vs_table.jpg
   :alt: Knowledge graph vs. flat table: the EM approach allows runtime queries and temporal layers.
   :width: 90%

   Knowledge graph vs. flat table: the EM approach allows runtime queries and temporal layers.

.. figure:: /_static/screenshots/clip_05/0004_colosseum_epochs.jpg
   :alt: The Colosseum represented at multiple epochs within a single EM dataset.
   :width: 90%

   The Colosseum represented at multiple epochs within a single EM dataset.

Try It Yourself
---------------

In the playground dataset, identify three proxy volumes and examine which stratigraphic units they represent.

.. note::

   A video walkthrough for this tutorial will be available on the Extended Matrix YouTube channel.

.. seealso::

   :doc:`EM Nodes: Stratigraphic Units and Paradata <08-nodes-paradata-qualia>`

   The formal side of this chapter: :ref:`the geometry property <geometry>`
   (the property and its payload) and
   :ref:`the geometry quale <geometry_qualia>` (its entry in the vocabulary).

