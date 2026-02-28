Learning Path: Developer Track
==============================

**Audience:** Developers and ontologists extending the EM ecosystem.

**Total estimated time:** ~27 min

**Prerequisites:** Python programming experience. Familiarity with JSON and RDF helpful.

----

Steps
-----

1. **EM Data Architecture and the Python Library** (~7 min)

   Under the hood: EM stores data as a JSON property graph (not a relational database). The Python library reads and writes...

   :doc:`→ Open tutorial <learn-em/tutorials/11-data-architecture>`

2. **FAQ: CIDOC CRM Mapping and Interoperability** (~3 min)

   Each EM node type maps to a CIDOC CRM class defined in the node type JSON. When exporting to RDF, EM writes directly in ...

   :doc:`→ Open tutorial <learn-em/tutorials/20-faq-vocabulary-mapping>`

3. **Auxiliary Resources: pyArchInit and External Data Connections** (~4 min)

   Auxiliary resources connect live external databases to the EM. The pyArchInit connection pulls excavator records, images...

   :doc:`→ Open tutorial <../../../em-blender-tools-doc:tutorials/15-pyarchinit-external-data>`

4. **Bulk Import via the Excel Mapping Tool** (~4 min)

   Import thousands of SUs from an Excel spreadsheet using a JSON mapping file. The mapping file defines which Excel column...

   :doc:`→ Open tutorial <../../../em-blender-tools-doc:tutorials/16-mapping-tool-excel>`

5. **Creating Proxies and Exporting Your Dataset** (~4 min)

   The Proxy Box Creator places a proxy volume on a 3D object by recording two alignment points, measuring wall thickness a...

   :doc:`→ Open tutorial <../../../em-blender-tools-doc:tutorials/18-proxy-export-manager>`

.. toctree::
   :hidden:
   :maxdepth: 1

   ../tutorials/11-data-architecture
   ../tutorials/20-faq-vocabulary-mapping
