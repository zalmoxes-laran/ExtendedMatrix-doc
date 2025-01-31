Properties (Qualia)
===================

.. _qualia:

Introduction
------------

The term "qualia" originated in philosophy of mind to describe subjective sensory experiences. In computational linguistics, Pustejovsky (1995) redefined it as a structural framework to describe objects by combining objective properties with functional and generative aspects. This work was foundational for natural language processing and AI, as it provided a systematic way for machines to understand and generate context-dependent meanings of words and concepts. The Extended Matrix further develops this structured approach for Cultural Heritage documentation needs, maintaining its compatibility with computational processing while specializing it for the domain's requirements.

While Pustejovsky's original framework (Formal, Constitutive, Telic, and Agentive roles) provides valuable theoretical foundations, the Extended Matrix adopts a more specialized structure optimized for Cultural Heritage documentation.

Extended Matrix Qualia Categories
--------------------------------

.. note::
   :class: admonition-purple

   The structure is accessible in a structured format via JSON at  
   `EM Blender Tools - Qualia Types JSON <https://github.com/zalmoxes-laran/EM-blender-tools/blob/EMtools_3dgraphy/s3Dgraphy/JSON_config/em_qualia_types.json>`_.


1. Physical and Material Qualia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Qualia describing tangible and measurable characteristics.

Dimensional Qualia
^^^^^^^^^^^^^^^^^^

Properties describing measurable spatial characteristics:

* **Height**
    * Getty AAT: `300055644 <http://vocab.getty.edu/aat/300055644>`_
    * CIDOC CRM: :class:`E54_Dimension`
    * Dublin Core: ``dcterms:extent``
    * Units: cm, m, ft
    * Expected extractors: direct measurement, 3D model measurement, drawing measurement

* **Width**
    * Getty AAT: `300055647 <http://vocab.getty.edu/aat/300055647>`_
    * CIDOC CRM: :class:`E54_Dimension`
    * Dublin Core: ``dcterms:extent``
    * Units: cm, m, ft
    * Expected extractors: direct measurement, 3D model measurement, drawing measurement

**Length**
   * Getty AAT: `300055644 <http://vocab.getty.edu/aat/300055644>`_
   * CIDOC CRM: :class:`E54_Dimension`
   * Dublin Core: ``dcterms:extent``
   * Units: cm, m, ft
   * Expected extractors: direct measurement, 3D model measurement, drawing measurement

**Thickness**
   * Getty AAT: `300055650 <http://vocab.getty.edu/aat/300055650>`_
   * CIDOC CRM: :class:`E54_Dimension`
   * Dublin Core: ``dcterms:extent``
   * Units: mm, cm, m
   * Expected extractors: direct measurement, material analysis, cross-section measurement

* **Diameter**
    * Getty AAT: `300055624 <http://vocab.getty.edu/aat/300055624>`_
    * CIDOC CRM: :class:`E54_Dimension`
    * Dublin Core: ``dcterms:extent``
    * Units: cm, m, ft
    * Expected extractors: direct measurement, 3D model measurement, drawing measurement

* **Depth**
    * Getty AAT: `300072633 <http://vocab.getty.edu/aat/300072633>`_
    * CIDOC CRM: :class:`E54_Dimension`
    * Dublin Core: ``dcterms:extent``
    * Units: cm, m, ft
    * Expected extractors: direct measurement, 3D model measurement, drawing measurement

* **Weight**
    * Getty AAT: `300056240 <http://vocab.getty.edu/aat/300056240>`_
    * CIDOC CRM: :class:`E54_Dimension`
    * Units: kg, g, lb
    * Expected extractors: direct measurement

Material Qualia
^^^^^^^^^^^^^^^

Physical material characteristics:

* **Material Type**
    * Getty AAT: `300010358 <http://vocab.getty.edu/aat/300010358>`_
    * CIDOC CRM: :class:`E57_Material`
    * Dublin Core: ``dcterms:medium``
    * Vocabulary source: Getty AAT
    * Expected extractors: visual inspection, laboratory analysis

* **Surface Treatment**
    * Getty AAT: `300053001 <http://vocab.getty.edu/aat/300053001>`_
    * CIDOC CRM: :class:`E11_Modification`
    * Dublin Core: ``dcterms:description``
    * Expected extractors: visual inspection, surface analysis

* **Granulometry**
    * Getty AAT: `300417183 <http://vocab.getty.edu/aat/300417183>`_
    * CIDOC CRM: :class:`E54_Dimension`
    * Values: fine, medium, coarse
    * Expected extractors: visual inspection, microscopic analysis

State Qualia
^^^^^^^^^^^^

Current physical condition:

* **Conservation State**
    * Getty AAT: `300379396 <http://vocab.getty.edu/aat/300379396>`_
    * CIDOC CRM: :class:`E3_Condition_State`
    * ICOM CIDOC: ``Object Condition Information``
    * Values: excellent, good, fair, poor, very_poor
    * Expected extractors: visual inspection, condition assessment

* **Integrity**
    * Getty AAT: `300055863 <http://vocab.getty.edu/aat/300055863>`_
    * CIDOC CRM: :class:`E3_Condition_State`
    * Dublin Core: ``dcterms:description``
    * Data type: percentage (0-100)
    * Expected extractors: visual inspection, 3D model analysis

Technical Qualia
^^^^^^^^^^^^^^^^

Construction and execution techniques:

* **Construction Technique**
    * Getty AAT: `300053001 <http://vocab.getty.edu/aat/300053001>`_
    * CIDOC CRM: :class:`E29_Design_or_Procedure`
    * Dublin Core: ``dcterms:description``
    * Vocabulary source: Getty AAT
    * Expected extractors: visual inspection, technical analysis

2. Spatiotemporal Qualia
~~~~~~~~~~~~~~~~~~~~~~~~

Spatial and temporal characteristics.

Spatial Qualia
^^^^^^^^^^^^^^

* **Absolute Position**
    * Getty AAT: `300387565 <http://vocab.getty.edu/aat/300387565>`_
    * CIDOC CRM: :class:`E53_Place`
    * Coordinate system: cartesian_3d (x, y, z)
    * Reference system: WGS84
    * Expected extractors: GPS survey, total station survey, 3D model measurement

* **Orientation**
    * Getty AAT: `300131574 <http://vocab.getty.edu/aat/300131574>`_
    * CIDOC CRM: :class:`E54_Dimension`
    * Components: azimuth, tilt, roll
    * Units: degrees
    * Expected extractors: compass measurement, 3D model analysis

* **Elevation**
    * Getty AAT: `300055644 <http://vocab.getty.edu/aat/300055644>`_
    * CIDOC CRM: :class:`E54_Dimension`
    * Units: m, ft
    * Expected extractors: GPS survey, total station survey, leveling

* **Arrangement**
    * Getty AAT: `300067654 <http://vocab.getty.edu/aat/300067654>`_
    * CIDOC CRM: :class:`E55_Type`
    * Values: linear, radial, grid, clustered, scattered, concentric
    * Expected extractors: visual inspection, spatial analysis

Temporal Qualia
^^^^^^^^^^^^^

* **Absolute Start Date**
    * Getty AAT: `300404284 <http://vocab.getty.edu/aat/300404284>`_
    * CIDOC CRM: :class:`E52_Time-Span`
    * Format: YYYY-MM-DD

* **Absolute End Date**
    * Getty AAT: `300404284 <http://vocab.getty.edu/aat/300404284>`_
    * CIDOC CRM: :class:`E52_Time-Span`
    * Format: YYYY-MM-DD

* **Dating Method**
    * Getty AAT: `300054714 <http://vocab.getty.edu/aat/300054714>`_
    * CIDOC CRM: :class:`E55_Type`
    * Values: stratigraphy, typology, c14, dendrochronology, historical_sources, stylistic_analysis
    * Expected extractors: dating analysis, laboratory analysis

1. Functional Qualia
~~~~~~~~~~~~~~~~~~~

Use and performance characteristics.

Telic Qualia
^^^^^^^^^^^
Original and intended functions:

* **Primary Function**
    * Getty AAT: `300068003 <http://vocab.getty.edu/aat/300068003>`_
    * CIDOC CRM: :class:`E55_Type`
    * Vocabulary source: Getty AAT
    * Expected extractors: functional analysis, historical research, comparative analysis

* **Secondary Functions**
    * Getty AAT: `300068003 <http://vocab.getty.edu/aat/300068003>`_
    * CIDOC CRM: :class:`E55_Type`
    * Vocabulary source: Getty AAT
    * Expected extractors: functional analysis, historical research

Structural Qualia
^^^^^^^^^^^^^^^
Structural and mechanical roles:

* **Structural Role**
    * Getty AAT: `300264518 <http://vocab.getty.edu/aat/300264518>`_
    * CIDOC CRM: :class:`E55_Type`
    * Values: load_bearing, non_load_bearing, reinforcing, connecting, supporting, decorative
    * Expected extractors: structural analysis, architectural analysis

* **Stress Type**
    * Getty AAT: `300264519 <http://vocab.getty.edu/aat/300264519>`_
    * CIDOC CRM: :class:`E55_Type`
    * Values: compression, tension, bending, shear, torsion
    * Expected extractors: structural analysis

Performative Qualia
^^^^^^^^^^^^^^^^^
Performance and capability characteristics:

* **Load Capacity**
    * Getty AAT: `300265725 <http://vocab.getty.edu/aat/300265725>`_
    * CIDOC CRM: :class:`E54_Dimension`
    * Units: kN, kgf
    * Expected extractors: structural analysis, load testing

4. Cultural and Interpretive Qualia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cultural significance and meaning.

Stylistic Qualia
^^^^^^^^^^^^^^^
Artistic and stylistic characteristics:

* **Artistic Style**
    * Getty AAT: `300015646 <http://vocab.getty.edu/aat/300015646>`_
    * CIDOC CRM: :class:`E55_Type`
    * Vocabulary source: Getty AAT
    * Expected extractors: style analysis, comparative analysis

* **Stylistic Influences**
    * Getty AAT: `300015646 <http://vocab.getty.edu/aat/300015646>`_
    * CIDOC CRM: :class:`E55_Type`
    * Vocabulary source: Getty AAT
    * Expected extractors: historical analysis, stylistic analysis

5. Contextual Qualia
~~~~~~~~~~~~~~~~~~~

Management and administrative information (Experimental category).

Administrative Qualia
^^^^^^^^^^^^^^^^^^^

* **Inventory Number**
    * Getty AAT: `300312355 <http://vocab.getty.edu/aat/300312355>`_
    * CIDOC CRM: :property:`P48_has_preferred_identifier`
    * Expected extractors: archival research, museum documentation

* **Legal Status**
    * Getty AAT: `300435427 <http://vocab.getty.edu/aat/300435427>`_
    * CIDOC CRM: :property:`P104_is_subject_to`
    * Vocabulary source: Getty AAT
    * Expected extractors: legal documentation, administrative research

* **Intervention History**
    * Getty AAT: `300379504 <http://vocab.getty.edu/aat/300379504>`_
    * CIDOC CRM: :class:`E11_Modification`

* **Conservation Status**
    * Getty AAT: `300435429 <http://vocab.getty.edu/aat/300435429>`_
    * CIDOC CRM: :property:`P44_has_condition`
    * Vocabulary source: Getty AAT
    * Expected extractors: conservation assessment, condition survey

* **Access Conditions**
    * Getty AAT: `300435430 <http://vocab.getty.edu/aat/300435430>`_
    * CIDOC CRM: :property:`P104_is_subject_to`
    * Vocabulary source: Getty AAT
    * Expected extractors: access assessment, management review

Implementation in s3Dgraphy
--------------------------

The Extended Matrix qualia framework is implemented in the s3Dgraphy library through a structured JSON schema that provides standardized definitions, controlled vocabularies, and mappings to established standards. The complete schema can be found in the s3Dgraphy library documentation [link to be provided].

Temporal Perception System
-------------------------

.. _actornode:

The Extended Matrix introduces the ActorNode concept to manage temporal perceptions:

.. image:: img/nodes/actor_node.png
   :width: 128px
   :align: left

An ActorNode represents an individual or group whose interpretation of properties is being recorded. This allows documentation of how properties were perceived at different times by different observers.

.. admonition:: Example
   :class: example

   A temple column's significance might be interpreted differently:

   **Ancient Priest (1st century CE)**
    * Telic: Sacred support of temple structure
    * Symbolic: Connection between earth and heavens

   **Medieval Chronicler (12th century)**
    * Telic: Reminder of pagan past
    * Symbolic: Example of ancient craftsmanship

   **Modern Archaeologist (21st century)**
    * Telic: Evidence of construction techniques
    * Symbolic: Indicator of economic resources

References
----------

* Pustejovsky, J. (1995). "The Generative Lexicon". MIT Press.
* `Getty Art & Architecture Thesaurus <http://vocab.getty.edu/aat/>`_
* `CIDOC CRM Documentation <http://www.cidoc-crm.org/>`_