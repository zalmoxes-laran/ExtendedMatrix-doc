.. badge:: Full Course
   :color: blue
.. badge:: Developer Track
   :color: orange

FAQ: CIDOC CRM Mapping and Interoperability
===========================================

.. raw:: html

   <!-- Replace VIDEO_ID with the actual YouTube video ID for 20_em_faq_vocabularies -->
   <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
   <iframe src="https://www.youtube.com/embed/VIDEO_ID_20_em_faq_vocabularies"
           style="position:absolute;top:0;left:0;width:100%;height:100%;"
           frameborder="0" allowfullscreen></iframe>
   </div>
   <p><em>▶ FAQ: CIDOC CRM Mapping and Interoperability (~~3 min)</em></p>

| **Clip:** 20  |  **Duration:** ~3 min  |  **Recording segment:** ~1:36:30 → 1:39:29

----

Prerequisites
-------------

:doc:`11-data-architecture`

Overview
--------

Each EM node type maps to a CIDOC CRM class defined in the node type JSON. When exporting to RDF, EM writes directly in CIDOC CRM while preserving the EM formal language as a provenance layer. 'Special finds' in EM cover architectonic blocks, coins in strata, and palaeontological specimens.

.. figure:: /_static/screenshots/clip_20/0001_json_cidoc_mapping.jpg
   :alt: Node type JSON showing the CIDOC CRM class for each EM node type.
   :width: 90%

   Node type JSON showing the CIDOC CRM class for each EM node type.

Key Concepts
------------

- Every node type JSON entry includes its CIDOC CRM class mapping.
- RDF export writes in CIDOC while keeping EM as the provenance record.
- 'Special find' is a stratigraphic concept covering blocks, coins, and bone finds.
- Future: full Linked Open Data publication via the RDF export pipeline.

Screenshots
-----------

.. figure:: /_static/screenshots/clip_20/0002_special_find_explanation.jpg
   :alt: Special finds in EM: architectonic blocks, coins in strata, fossil specimens.
   :width: 90%

   Special finds in EM: architectonic blocks, coins in strata, fossil specimens.

.. figure:: /_static/screenshots/clip_20/0003_rdf_integration_plan.jpg
   :alt: RDF integration roadmap: EM as provenance layer, CIDOC as output.
   :width: 90%

   RDF integration roadmap: EM as provenance layer, CIDOC as output.

Try It Yourself
---------------

Find the CIDOC CRM mapping for the 'construction' node type in the node types JSON file.

.. note::

   A video walkthrough for this tutorial will be available on the Extended Matrix YouTube channel.

.. seealso::

   :doc:`EM Data Architecture and Python Library <11-data-architecture>`

