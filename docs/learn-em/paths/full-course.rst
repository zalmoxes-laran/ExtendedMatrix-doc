Learning Path: Full Course
==========================

**Audience:** All practitioners who want comprehensive EM knowledge.

**Total estimated time:** ~70 min

**Prerequisites:** Blender 3.x and yEd installed. Familiarity with basic 3D concepts helpful but not required.

----

Steps
-----

1. **Introduction: What Is Extended Matrix?** (~4 min)

   Extended Matrix (EM) is a formal language and Blender add-on for archaeological and paleontological documentation. This ...

   :doc:`→ Open tutorial <learn-em/tutorials/01-introduction>`

2. **The EM Data Lifecycle: Create, Manage, Enrich, Export** (~3 min)

   The four-phase EM workflow: creating data, managing data, enriching data, and exporting data. EM can start from various ...

   :doc:`→ Open tutorial <learn-em/tutorials/02-data-lifecycle>`

3. **3D Survey Collection: Level of Detail in Blender** (~6 min)

   The 3D Survey Collection (3DSC) add-on solves the problem of working with very large photogrammetric models in Blender. ...

   :doc:`→ Open tutorial <../../../em-blender-tools-doc:tutorials/03-3dsc-lod-concept>`

4. **Site-Scale LOD and Data Preparation** (~4 min)

   Working at site scale with hundreds of objects. Bulk LOD switching lets you maintain all objects at a low-poly level and...

   :doc:`→ Open tutorial <../../../em-blender-tools-doc:tutorials/04-3dsc-site-scale>`

5. **From 3D Models to Knowledge: Proxies and the Knowledge Graph** (~4 min)

   A 3D survey records geometry, not knowledge. The transition from photogrammetry to an EM happens by creating *proxies* —...

   :doc:`→ Open tutorial <learn-em/tutorials/05-proxies-knowledge-graph>`

6. **The Archaeological Documentation Workflow** (~7 min)

   The full pipeline from excavation to digital reconstruction: field documentation, post-excavation processing, and virtua...

   :doc:`→ Open tutorial <learn-em/tutorials/06-archaeological-workflow>`

7. **EM Language: Canvas, Metadata and Epochs** (~4 min)

   The EM canvas is the root container for all data. It carries metadata fields (human ID, author, ORCID, licence, embargo)...

   :doc:`→ Open tutorial <learn-em/tutorials/07-canvas-metadata-epochs>`

8. **EM Nodes: Stratigraphic Units, Activities and Paradata** (~4 min)

   Stratigraphic node types (construction, destruction, use, etc.) represent individual actions. Activity nodes group multi...

   :doc:`→ Open tutorial <learn-em/tutorials/08-nodes-paradata-qualia>`

9. **Combining Sources: The Grey Zone** (~4 min)

   Real excavations rarely have complete documentation. EM handles the 'grey zone' of incomplete or evolving records by com...

   :doc:`→ Open tutorial <learn-em/tutorials/09-grey-zone-combining>`

10. **Pseudo-Stratigraphy and Remote Sensing** (~3 min)

   Geophysical and remote sensing data can be integrated into EM as pseudo-stratigraphic units — hypothetical nodes that re...

   :doc:`→ Open tutorial <learn-em/tutorials/10-pseudo-stratigraphy>`

11. **EM Data Architecture and the Python Library** (~7 min)

   Under the hood: EM stores data as a JSON property graph (not a relational database). The Python library reads and writes...

   :doc:`→ Open tutorial <learn-em/tutorials/11-data-architecture>`

12. **Installing EM Tools: yEd and the Blender Add-on** (~5 min)

   Step-by-step installation: download the EM add-on from GitHub releases, install it in Blender via Edit → Preferences → A...

   :doc:`→ Open tutorial <../../../em-blender-tools-doc:tutorials/12-install-yed-blender>`

13. **Creating Your First Extended Matrix** (~4 min)

   Create a minimal Extended Matrix from scratch: drag the canvas from the yEd palette, fill in metadata (human ID, author,...

   :doc:`→ Open tutorial <../../../em-blender-tools-doc:tutorials/13-first-matrix-creation>`

14. **Multi-Temporal 3D Visualization Demo** (~9 min)

   Live demo with the Great Temple dataset: switching between epochs, assigning different 3D models to different time perio...

   :doc:`→ Open tutorial <../../../em-blender-tools-doc:tutorials/14-multitemporal-visualization>`

15. **Auxiliary Resources: pyArchInit and External Data Connections** (~4 min)

   Auxiliary resources connect live external databases to the EM. The pyArchInit connection pulls excavator records, images...

   :doc:`→ Open tutorial <../../../em-blender-tools-doc:tutorials/15-pyarchinit-external-data>`

16. **Bulk Import via the Excel Mapping Tool** (~4 min)

   Import thousands of SUs from an Excel spreadsheet using a JSON mapping file. The mapping file defines which Excel column...

   :doc:`→ Open tutorial <../../../em-blender-tools-doc:tutorials/16-mapping-tool-excel>`

17. **Paradata Manager and Graph Visualization** (~4 min)

   The Paradata Manager shows all qualia for a selected SU. Alt+F selects a 3D object and highlights it in the Stratigraphi...

   :doc:`→ Open tutorial <../../../em-blender-tools-doc:tutorials/17-paradata-graph-viz>`

18. **Creating Proxies and Exporting Your Dataset** (~4 min)

   The Proxy Box Creator places a proxy volume on a 3D object by recording two alignment points, measuring wall thickness a...

   :doc:`→ Open tutorial <../../../em-blender-tools-doc:tutorials/18-proxy-export-manager>`

19. **FAQ: Using Epochs as Relative Phases** (~3 min)

   Epochs can be used as broad relative phases without exact calendar dates — for example, 'Roman period' or 'Phase 1'. The...

   :doc:`→ Open tutorial <learn-em/tutorials/19-faq-temporal-phases>`

20. **FAQ: CIDOC CRM Mapping and Interoperability** (~3 min)

   Each EM node type maps to a CIDOC CRM class defined in the node type JSON. When exporting to RDF, EM writes directly in ...

   :doc:`→ Open tutorial <learn-em/tutorials/20-faq-vocabulary-mapping>`

.. toctree::
   :hidden:
   :maxdepth: 1

   ../tutorials/01-introduction
   ../tutorials/02-data-lifecycle
   ../tutorials/05-proxies-knowledge-graph
   ../tutorials/06-archaeological-workflow
   ../tutorials/07-canvas-metadata-epochs
   ../tutorials/08-nodes-paradata-qualia
   ../tutorials/09-grey-zone-combining
   ../tutorials/10-pseudo-stratigraphy
   ../tutorials/11-data-architecture
   ../tutorials/19-faq-temporal-phases
   ../tutorials/20-faq-vocabulary-mapping
