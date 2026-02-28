.. badge:: Full Course
   :color: blue

FAQ: Using Epochs as Relative Phases
====================================

.. raw:: html

   <!-- Replace VIDEO_ID with the actual YouTube video ID for 19_em_faq_temporal -->
   <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
   <iframe src="https://www.youtube.com/embed/VIDEO_ID_19_em_faq_temporal"
           style="position:absolute;top:0;left:0;width:100%;height:100%;"
           frameborder="0" allowfullscreen></iframe>
   </div>
   <p><em>▶ FAQ: Using Epochs as Relative Phases (~~3 min)</em></p>

| **Clip:** 19  |  **Duration:** ~3 min  |  **Recording segment:** 1:33:29 → ~1:36:30

----

Prerequisites
-------------

:doc:`07-canvas-metadata-epochs`

Overview
--------

Epochs can be used as broad relative phases without exact calendar dates — for example, 'Roman period' or 'Phase 1'. The temporal propagation algorithm means that if one node is dated 'after 193 AD', all nodes above it in the graph are automatically bounded to after 193 AD.

.. figure:: /_static/screenshots/clip_19/0002_roman_times_epoch.jpg
   :alt: An epoch labelled 'Roman times' — no calendar date required.
   :width: 90%

   An epoch labelled 'Roman times' — no calendar date required.

Key Concepts
------------

- Epochs do not require absolute dates — relative labels are fully supported.
- Temporal propagation: one dated node constrains all related nodes automatically.
- The Python library returns all temporally bounded nodes via a single query.
- Temporal reasoning is computed at runtime, not stored as fixed values.

Screenshots
-----------

.. figure:: /_static/screenshots/clip_19/0003_single_dated_node_193ad.jpg
   :alt: One node dated 'after 193 AD' acts as the temporal anchor.
   :width: 90%

   One node dated 'after 193 AD' acts as the temporal anchor.

.. figure:: /_static/screenshots/clip_19/0004_propagation_algorithm.jpg
   :alt: Propagation: all nodes above the anchor are automatically bounded.
   :width: 90%

   Propagation: all nodes above the anchor are automatically bounded.

Try It Yourself
---------------

Set one node in the playground EM to 'after 300 AD' and run the temporal query to see which other nodes are automatically constrained.

.. note::

   A video walkthrough for this tutorial will be available on the Extended Matrix YouTube channel.

.. seealso::

   :doc:`EM Canvas, Metadata and Epochs <07-canvas-metadata-epochs>`

