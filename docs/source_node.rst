Document Nodes: Managing Archaeological Sources
============================================

.. _documentnodes_extended:

Introduction
-----------

Document nodes (also known as source nodes) are fundamental elements in the Extended Matrix framework, representing primary and secondary sources that support our archaeological interpretations. As described in the paradata nodes section, they form part of the validation chain for archaeological properties. This chapter provides an operational deep-dive into how to effectively manage and organize these sources in practice.
Each document is assigned a unique identifier (e.g., "D.01", "D.02") that serves as a reference throughout the documentation process.

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