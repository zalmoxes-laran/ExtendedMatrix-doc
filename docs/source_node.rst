Document Nodes: Managing Archaeological Sources
============================================

.. _documentnodes_extended:

Introduction
-----------

Document nodes (also known as source nodes) are fundamental elements in the Extended Matrix framework, representing primary and secondary sources that support our archaeological interpretations. As described in the paradata nodes section, they form part of the validation chain for archaeological properties. This chapter provides an operational deep-dive into how to effectively manage and organize these sources in practice.
Each document is assigned a unique identifier (e.g., "D.01", "D.02") that serves as a reference throughout the documentation process.

.. note::
   :class: admonition-purple

   The structured version of the Document (Source) Nodes is available in JSON format at  
   `EM Blender Tools - Document Types JSON <https://github.com/zalmoxes-laran/EM-blender-tools/blob/EMtools_3dgraphy/s3Dgraphy/JSON_config/em_document_types.json>`_.

`new` 3D representation of Document Nodes
-----------------------------------------

Document nodes can be represented in 3D space as a collection of digital assets, each corresponding to a specific source. These assets can be visualized in a virtual environment, providing a spatial representation of the documentation sources. The 3D representation is normally created withih the context of a 3D model of the archaeological site or object. In the EM framework, the 3D representation of document nodes is used to visualize the spatial distribution of sources and their relationships to the archaeological properties they validate. They are created using the Blender software and can be exported along with the overall scene in the GLTF format to be reused in EMviq or in Heriverse web-app.

Document Types and Classification
-------------------------------

The Extended Matrix framework organizes documentation into standardized categories, each mapped to established cultural heritage vocabularies.

Spatial Documentation
~~~~~~~~~~~~~~~~~~~
:Getty AAT: `300389935 <http://vocab.getty.edu/aat/300389935>`_
:CIDOC CRM: :class:`E36_Visual_Item` with property :property:`P67_refers_to`
:Dublin Core: ``dcterms:spatial``

Documents containing spatial information and measurements:

* **3D Models**
    * Formats: GLTF, OBJ, PLY, FBX, 3DS, E57
    * Key extractions: dimensions, spatial relationships, geometric features
    * Required metadata:
        * creation_date
        * creator
        * software_used
        * coordinate_system
        * spatial_resolution
    * Optional metadata:
        * accuracy_assessment
        * processing_workflow
        * registration_method
        * point_cloud_density
    * Supported extractors:
        * 3D model analysis
        * Geometric analysis
        * Spatial pattern analysis

* **Technical Drawings**
    * Formats: DWG, DXF, PDF, SVG
    * Key extractions: dimensions, construction details, spatial layout
    * Required metadata:
        * creation_date
        * author
        * scale
        * drawing_type
        * reference_system
    * Optional metadata:
        * revision_history
        * drawing_conventions
        * associated_specifications

Scientific Documentation
~~~~~~~~~~~~~~~~~~~~~~
:Getty AAT: `300379612 <http://vocab.getty.edu/aat/300379612>`_
:CIDOC CRM: :class:`E31_Document` with property :property:`P140_assigned_attribute_to`

* **Material Analysis Reports**
    * Formats: PDF, DOCX, XLSX
    * Key extractions: 
        * material_composition
        * physical_properties
        * chemical_properties
        * degradation_patterns
    * Required metadata:
        * analysis_date
        * laboratory
        * analysis_method
        * sampling_strategy
        * analyst
    * Optional metadata:
        * equipment_used
        * calibration_data
        * error_margins

* **Dating Analysis Reports**
    * Formats: PDF, DOCX, XLSX
    * Key extractions:
        * absolute_date
        * date_range
        * dating_method_reliability
        * chronological_context
    * Required metadata:
        * analysis_date
        * laboratory
        * dating_method
        * sample_description
        * calibration_curve

Historical Documentation
~~~~~~~~~~~~~~~~~~~~~~
:Getty AAT: `300343082 <http://vocab.getty.edu/aat/300343082>`_
:CIDOC CRM: :class:`E31_Document` with property :property:`P70_documents`
:Dublin Core: ``dcterms:source``

* **Archival Documents**
    * Formats: PDF, TXT, DOCX, TIFF
    * Key extractions:
        * historical_context
        * construction_history
        * ownership_history
        * modification_events
    * Required metadata:
        * archive_reference
        * document_date
        * document_type
        * archival_location
    * Optional metadata:
        * transcription_details
        * preservation_state
        * access_restrictions

* **Historical Photographs**
    * Formats: TIFF, JPG, PDF
    * Key extractions:
        * historical_appearance
        * temporal_changes
        * architectural_features
        * urban_context
    * Required metadata:
        * photo_date
        * photographer
        * archive_reference
        * subject_location
    * Optional metadata:
        * camera_details
        * print_type
        * negative_reference

Conservation Documentation
~~~~~~~~~~~~~~~~~~~~~~~~
:Getty AAT: `300379612 <http://vocab.getty.edu/aat/300379612>`_
:CIDOC CRM: :class:`E31_Document` with property :property:`P140_assigned_attribute_to`
:Dublin Core: ``dcterms:provenance``

* **Condition Reports**
    * Formats: PDF, DOCX, XLSX
    * Key extractions:
        * conservation_state
        * degradation_patterns
        * risk_factors
        * intervention_priorities
    * Required metadata:
        * assessment_date
        * assessor
        * assessment_method
        * condition_classification
    * Optional metadata:
        * environmental_data
        * previous_treatments
        * monitoring_history

* **Intervention Reports**
    * Formats: PDF, DOCX, XLSX
    * Key extractions:
        * treatment_methods
        * materials_used
        * intervention_results
        * follow_up_recommendations
    * Required metadata:
        * intervention_date
        * conservator
        * intervention_type
        * materials_used
        * documentation_method
    * Optional metadata:
        * preliminary_tests
        * environmental_conditions
        * post_treatment_monitoring

.. note::
   All Getty AAT links point to the Art & Architecture Thesaurus, providing standardized terminology for cultural heritage documentation. CIDOC CRM mappings follow the latest version (7.1.1) of the standard.


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

.. _source-list-schema:

Source List schema
~~~~~~~~~~~~~~~~~~

.. versionadded:: 1.3
   Introduced as the *formalized source list for data collection*.

.. versionchanged:: 1.6
   Two-sheet structure (Analytical / Comparative Sources) canonicalised.
   The *Type* column is promoted to a closed controlled vocabulary
   aligned with the DocumentNode three-axis classification (DP-07).
   The Source List can now be merged directly into the ``Documents``
   sheet of ``em_data.xlsx`` (DP-02) without manual duplication. See
   DP-58 in the development projects index at
   https://docs.extendedmatrix.org/projects/development-projects/.

The Source List is a single-purpose XLSX file (``source_list.xlsx``)
sitting at the project root next to the ``.graphml``. It registers
every bibliographic and archival source referenced by Document nodes
in the graph and assigns each one a stable project-local identifier
(``D.NN``) that propagates to the DosCo folder and to the graph itself.

**Sheet structure (Analytical vs Comparative)**

A 1.6 Source List workbook contains two sheets, anchored on
DocumentNode Axis 1 (*role*):

* ``Analytical Sources`` — primary sources for *this* reconstruction
  (excavation reports of the site, surveys, dossiers).
* ``Comparative Sources`` — external references and analogies
  (parallels from other sites, treatises, comparative iconography).

Both sheets share the same 8-column schema. Single-sheet workbooks
named ``sources`` (the legacy 1.3 layout) are still accepted by all
importers for backward compatibility.

**Column reference**

.. list-table::
   :header-rows: 1
   :widths: 14 22 16 24 10 14

   * - Column
     - Purpose
     - Format
     - Example
     - Required
     - Maps to (DP-07)
   * - **Name**
     - Project-local unique ID
     - ``D.NN`` (zero-padded, sequential)
     - ``D.01``
     - yes
     - DocumentNode ``id``
   * - **Description**
     - Natural-language description of the source
     - Free text, ~1 sentence
     - "Photogrammetric model of the Great Temple, 2015"
     - yes
     - DocumentNode ``description``
   * - **Url**
     - Citation / DOI / web URL
     - Bibliographic citation or URL
     - "Daicoviciu H. et al., *Sargetia* XIV, 1979"
     - recommended
     - DocumentNode ``url``
   * - **Property that can validate**
     - Qualia / properties this source can support
     - Comma-separated names (see :doc:`qualia`)
     - ``geometry, material, elevation``
     - recommended
     - Drives ExtractorNode targeting
   * - **original id.**
     - Archive or library reference
     - Free text
     - "ASR, Fondo Disegni, b.12, c.34r"
     - optional
     - DocumentNode ``archive_reference``
   * - **Type**
     - Source typology (closed vocabulary [#typevocab16]_)
     - One of: ``3d``, ``pdf``, ``image``, ``map``, ``text``, ``audio``, ``dataset``
     - ``pdf``
     - yes
     - Axis 2 ``content_nature`` + Axis 3 ``geometry``
   * - **Preview**
     - Optional thumbnail
     - Embedded image cell
     - —
     - optional
     - UI hint (Document Manager)
   * - **Notes**
     - Free-form annotations
     - Free text
     - "OCR quality low for pp. 142–148"
     - optional
     - DocumentNode ``notes``

.. [#typevocab16] The 1.6 *Type* vocabulary is the canonical projection
   of DP-07 Axes 2 and 3 onto a flat label set:
   ``3d`` → 3d_object + reality_based;
   ``pdf`` / ``text`` → 2d_object (no geometry);
   ``image`` / ``map`` → 2d_object + observable;
   ``audio`` / ``dataset`` → no geometry.
   Importers translate each Type back into the full three-axis tuple at
   ingest time.

**Worked example (excerpt)**

.. list-table::
   :header-rows: 1
   :widths: 8 28 26 24 6 8

   * - Name
     - Description
     - Url
     - Property that can validate
     - Type
     - Notes
   * - D.01
     - Photogrammetric model of the Great Temple
     - Demetrescu E., 2015 (unpublished)
     - geometry, material, elevation, surface_treatment
     - 3d
     -
   * - D.02
     - Excavation report 1975–1977
     - Daicoviciu H. et al., *Sargetia* XIV, 1979, pp. 139–154
     - stratigraphy, architecture, dimensions, construction_technique
     - pdf
     - OCR low pp. 142–148

**Integration with em_data.xlsx (DP-02)**

When a ``Documents`` sheet is missing in a project's ``em_data.xlsx``
(DP-02 StratiMiner pipeline), the importer can pull it directly from
``source_list.xlsx``: the 8 columns above map one-to-one onto the
em_data Documents schema with the *Type* column unfolding into the
two DP-07 axes. This eliminates the previous duplication where authors
had to maintain the same source registry in two files.

.. seealso::

   * :doc:`extractor_nodes` — how the *Property that can validate*
     column drives the validation chain.
   * :doc:`qualia` — the property vocabulary used in column 4.
   * :doc:`project_organization` — DosCo folder layout and ``D.NN`` ID
     propagation from the Source List to the file system.

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