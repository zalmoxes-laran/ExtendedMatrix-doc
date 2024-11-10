Document Nodes: Managing Archaeological Sources
============================================

.. _documentnodes_extended:

Introduction
-----------

Document nodes (also known as source nodes) are fundamental elements in the Extended Matrix framework, representing primary and secondary sources that support our archaeological interpretations. As described in the paradata nodes section, they form part of the validation chain for archaeological properties. This chapter provides an operational deep-dive into how to effectively manage and organize these sources in practice.
Each document is assigned a unique identifier (e.g., "D.01", "D.02") that serves as a reference throughout the documentation process.

Source List Tool
--------------

.. figure:: img/source_list.png
   :width: 800
   :align: center
   
   The Source List tool provides a structured approach to collecting and organizing documentary sources. Each row represents a document with its metadata and potential validation properties.

The Source List is designed to track:
* Document identification (unique ID)
* Description of the source
* Original bibliographic reference or URL
* Properties that can be validated using this source
* Document type (3D model, photo, drawing, text, etc.)
* Preview (when available)

Team Organization: The Source Hunter
---------------------------------

The collection and organization of sources can be efficiently managed by assigning a dedicated team member (the "source hunter") to:
* Search and collect relevant documentation from libraries and archives
* Organize digital resources
* Maintain the source list
* Track validation properties for each source

Document Organization: The DosCo System
------------------------------------

Sources are organized in a Dossier Comparativ (DosCo) folder structure where:

1. Each document maintains its unique identifier as a prefix
2. Original filenames are preserved after the prefix
3. Digital files follow the naming convention:
   ``D.XX_original_filename.extension``

Example::

    DosCo/
    ├── D.01_photogrammetric_survey_temple.pdf
    ├── D.02_dodwell_engraving_1834.jpg
    ├── D.03_castrum_reconstruction.pdf
    └── ...

Properties Validation Column
-------------------------

A key feature of the Source List is the "Property that can validate" column, which:
* Identifies specific properties that can be validated using each source
* Helps in building the validation chain through paradata nodes
* Guides the creation of extractor nodes
* Supports evidence-based property documentation

Examples of validation properties:
* Geometrical measurements
* Material identification
* Construction techniques
* Architectural details
* Site morphology
* Spatial relationships

Best Practices
------------

1. **Source Collection:**
   * Systematically search both physical and digital archives
   * Document the origin and reliability of each source
   * Maintain high-quality digital copies

2. **Documentation:**
   * Use consistent naming conventions
   * Keep the Source List updated
   * Link sources to specific properties they can validate

3. **Team Coordination:**
   * Assign clear responsibilities for source collection
   * Regular updates to the Source List
   * Clear communication about validation needs

4. **Digital Organization:**
   * Maintain organized DosCo folders
   * Use consistent file naming
   * Ensure proper backup of digital sources

This systematic approach to source management ensures that:
* All interpretations are properly documented
* Sources are easily retrievable
* The validation chain remains clear and verifiable
* Team members can efficiently collaborate on documentation