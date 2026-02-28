.. badge:: Full Course
   :color: blue
.. badge:: Developer Track
   :color: orange

EM Data Architecture and the Python Library
===========================================

.. raw:: html

   <!-- Replace VIDEO_ID with the actual YouTube video ID for 11_em_data_architecture -->
   <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
   <iframe src="https://www.youtube.com/embed/VIDEO_ID_11_em_data_architecture"
           style="position:absolute;top:0;left:0;width:100%;height:100%;"
           frameborder="0" allowfullscreen></iframe>
   </div>
   <p><em>▶ EM Data Architecture and the Python Library (~~7 min)</em></p>

| **Clip:** 11  |  **Duration:** ~7 min  |  **Recording segment:** ~50:00 → 57:29

----

Prerequisites
-------------

:doc:`09-grey-zone-combining`

Overview
--------

Under the hood: EM stores data as a JSON property graph (not a relational database). The Python library reads and writes this graph, exposes a REST API, and connects Blender with the Heriverse web platform. Node types and qualia vocabularies are defined in JSON files bundled with the code — offline-first.

.. figure:: /_static/screenshots/clip_11/0001_architecture_diagram.jpg
   :alt: EM architecture: Blender → Python library → JSON graph → Heriverse.
   :width: 90%

   EM architecture: Blender → Python library → JSON graph → Heriverse.

Key Concepts
------------

- EM data = JSON property graph, not a relational database.
- The Python library mediates between Blender, yEd, and the Heriverse web platform.
- Node types and qualia are defined in JSON — changing one file propagates to all tools.
- Vocabularies (Getty, CIDOC) are bundled for offline use — no internet required.
- A REST API exposes the graph for external tools and automation.

Screenshots
-----------

.. figure:: /_static/screenshots/clip_11/0002_json_node_declaration.jpg
   :alt: The node declaration JSON file defining all node types and connectors.
   :width: 90%

   The node declaration JSON file defining all node types and connectors.

.. figure:: /_static/screenshots/clip_11/0003_qualia_json_getty_links.jpg
   :alt: Qualia definitions with linked Getty vocabulary URIs.
   :width: 90%

   Qualia definitions with linked Getty vocabulary URIs.

.. figure:: /_static/screenshots/clip_11/0005_rest_api_docs.jpg
   :alt: The EM Python library REST API documentation.
   :width: 90%

   The EM Python library REST API documentation.

Try It Yourself
---------------

Open the EM node types JSON in a text editor and add a new qualia property to the 'construction' node type.

.. note::

   The video for this tutorial is available on the StratiGraph private YouTube channel.
   Clip filename: ``11_em_data_architecture.mp4``

.. seealso::

   :doc:`Installing EM Tools: yEd and Blender <em-blender-tools-doc:tutorials/12-install-yed-blender>`

