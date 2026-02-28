.. badge:: Full Course
   :color: blue

Combining Sources: The Grey Zone
================================

.. raw:: html

   <!-- Replace VIDEO_ID with the actual YouTube video ID for 09_em_grey_zone -->
   <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
   <iframe src="https://www.youtube.com/embed/VIDEO_ID_09_em_grey_zone"
           style="position:absolute;top:0;left:0;width:100%;height:100%;"
           frameborder="0" allowfullscreen></iframe>
   </div>
   <p><em>▶ Combining Sources: The Grey Zone (~~4 min)</em></p>

| **Clip:** 09  |  **Duration:** ~4 min  |  **Recording segment:** 42:48 → ~47:00

----

Prerequisites
-------------

:doc:`08-nodes-paradata-qualia`

Overview
--------

Real excavations rarely have complete documentation. EM handles the 'grey zone' of incomplete or evolving records by combining multiple sources (photogrammetry, drawings, historical photos) through extractor and combiner nodes, creating proxies that aggregate information from all available evidence.

.. figure:: /_static/screenshots/clip_09/0001_raw_vs_annotated_model.jpg
   :alt: Side-by-side: raw 3D model vs. annotated model with proxy volumes.
   :width: 90%

   Side-by-side: raw 3D model vs. annotated model with proxy volumes.

Key Concepts
------------

- Most archaeological records are incomplete — EM is designed for this reality.
- Extractor nodes pull information from a specific document or source.
- Combiner nodes aggregate multiple extractors into a single proxy.
- The grey zone: what is known, partly known, and unknown is explicit in the graph.

Screenshots
-----------

.. figure:: /_static/screenshots/clip_09/0003_incomplete_photogrammetry.jpg
   :alt: An ongoing excavation: photogrammetry captures only part of the evidence.
   :width: 90%

   An ongoing excavation: photogrammetry captures only part of the evidence.

.. figure:: /_static/screenshots/clip_09/0005_combiner_node_graph.jpg
   :alt: EM graph: a combiner node aggregating two source extractors into one proxy.
   :width: 90%

   EM graph: a combiner node aggregating two source extractors into one proxy.

.. figure:: /_static/screenshots/clip_09/0006_damaged_heritage_combining.jpg
   :alt: Combining historical and current documentation for damaged heritage.
   :width: 90%

   Combining historical and current documentation for damaged heritage.

Try It Yourself
---------------

In yEd, create a combiner node that merges a photogrammetry extractor and a drawing extractor for the same SU.

.. note::

   The video for this tutorial is available on the StratiGraph private YouTube channel.
   Clip filename: ``09_em_grey_zone.mp4``

.. seealso::

   :doc:`Pseudo-Stratigraphy and Remote Sensing <10-pseudo-stratigraphy>`

