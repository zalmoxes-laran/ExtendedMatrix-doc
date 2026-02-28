.. badge:: Full Course
   :color: blue

EM Language: Canvas, Metadata and Epochs
========================================

.. raw:: html

   <!-- Replace VIDEO_ID with the actual YouTube video ID for 07_em_canvas_epochs -->
   <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
   <iframe src="https://www.youtube.com/embed/VIDEO_ID_07_em_canvas_epochs"
           style="position:absolute;top:0;left:0;width:100%;height:100%;"
           frameborder="0" allowfullscreen></iframe>
   </div>
   <p><em>▶ EM Language: Canvas, Metadata and Epochs (~~4 min)</em></p>

| **Clip:** 07  |  **Duration:** ~4 min  |  **Recording segment:** ~33:30 → ~38:00

----

Prerequisites
-------------

:doc:`06-archaeological-workflow`

Overview
--------

The EM canvas is the root container for all data. It carries metadata fields (human ID, author, ORCID, licence, embargo) that propagate to all leaf nodes. Epochs are swim-lane containers representing chronological or interpretive phases — they do not require absolute dates.

.. figure:: /_static/screenshots/clip_07/0001_fictional_em_canvas.jpg
   :alt: A fictional EM canvas showing all metadata fields.
   :width: 90%

   A fictional EM canvas showing all metadata fields.

Key Concepts
------------

- The canvas is the root node of every Extended Matrix.
- Metadata set on the canvas propagates automatically to all child nodes.
- Epochs are interpretive containers — they can be relative phases, not just calendar dates.
- Periodization is an act of interpretation and must be traceable via paradata.

Screenshots
-----------

.. figure:: /_static/screenshots/clip_07/0003_orcid_licence_embargo.jpg
   :alt: Metadata fields: ORCID, licence type, and embargo date.
   :width: 90%

   Metadata fields: ORCID, licence type, and embargo date.

.. figure:: /_static/screenshots/clip_07/0004_swim_lanes_epochs_yed.jpg
   :alt: Epochs displayed as swim lanes in the yEd graph editor.
   :width: 90%

   Epochs displayed as swim lanes in the yEd graph editor.

.. figure:: /_static/screenshots/clip_07/0005_metadata_propagation.jpg
   :alt: Metadata propagation from canvas to all leaf nodes.
   :width: 90%

   Metadata propagation from canvas to all leaf nodes.

Try It Yourself
---------------

In yEd, create a new canvas with your site code as the human ID and add two epochs: one for construction, one for destruction.

.. note::

   A video walkthrough for this tutorial will be available on the Extended Matrix YouTube channel.

.. seealso::

   :doc:`Creating Your First Extended Matrix <em-blender-tools-doc:tutorials/13-first-matrix-creation>`

