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

.. figure:: /_static/screenshots/clip_05/0001_knowledge_vs_survey.jpg
   :alt: The key transition: a 3D survey records geometry, EM records knowledge.
   :width: 90%

   The key transition: a 3D survey records geometry, EM records knowledge.

Key Concepts
------------

- A 3D model is a *representation*; a proxy is *knowledge*.
- EM uses a knowledge graph — not tables — for richer querying and temporal support.
- The same site can be represented at multiple epochs within one dataset.
- Stratigraphy applies beyond excavations: buildings, mosaics, vegetation all have it.

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

