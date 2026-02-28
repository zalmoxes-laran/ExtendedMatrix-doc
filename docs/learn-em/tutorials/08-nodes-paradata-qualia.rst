.. badge:: Full Course
   :color: blue

EM Nodes: Stratigraphic Units, Activities and Paradata
======================================================

.. raw:: html

   <!-- Replace VIDEO_ID with the actual YouTube video ID for 08_em_nodes_paradata -->
   <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
   <iframe src="https://www.youtube.com/embed/VIDEO_ID_08_em_nodes_paradata"
           style="position:absolute;top:0;left:0;width:100%;height:100%;"
           frameborder="0" allowfullscreen></iframe>
   </div>
   <p><em>▶ EM Nodes: Stratigraphic Units, Activities and Paradata (~~4 min)</em></p>

| **Clip:** 08  |  **Duration:** ~4 min  |  **Recording segment:** ~38:00 → 42:48

----

Prerequisites
-------------

:doc:`07-canvas-metadata-epochs`

Overview
--------

Stratigraphic node types (construction, destruction, use, etc.) represent individual actions. Activity nodes group multiple SUs into campaigns. Paradata nodes carry qualitative information (qualia) such as material, dimensions, and provenance, linked to centralised vocabulary lists.

.. figure:: /_static/screenshots/clip_08/0001_su_node_types_slide.jpg
   :alt: Overview of EM stratigraphic node types.
   :width: 90%

   Overview of EM stratigraphic node types.

Key Concepts
------------

- EM defines typed SU nodes: construction, destruction, use, transformation, etc.
- Activity nodes cluster multiple SUs into broader operations or campaigns.
- Paradata nodes carry qualia — material, dimensions, provenance, uncertainty level.
- Node types are defined in a central JSON file, making the vocabulary extensible.

Screenshots
-----------

.. figure:: /_static/screenshots/clip_08/0003_paradata_node_qualia.jpg
   :alt: A paradata node with qualia subgraph open.
   :width: 90%

   A paradata node with qualia subgraph open.

.. figure:: /_static/screenshots/clip_08/0004_qualia_example_material.jpg
   :alt: Qualia example: material = travertine, height = 4.2 m.
   :width: 90%

   Qualia example: material = travertine, height = 4.2 m.

.. figure:: /_static/screenshots/clip_08/0005_json_node_types.jpg
   :alt: The centralised JSON file defining all node types and connectors.
   :width: 90%

   The centralised JSON file defining all node types and connectors.

Try It Yourself
---------------

In the playground EM, find a paradata node and list all qualia attached to it.

.. note::

   A video walkthrough for this tutorial will be available on the Extended Matrix YouTube channel.

.. seealso::

   :doc:`Paradata Manager and Graph Visualization <em-blender-tools-doc:tutorials/17-paradata-graph-viz>`

