Extractor Types
==============

Introduction
-----------

Extractors are specialized tools and methodologies used in the Extended Matrix framework to derive qualia (properties) from source documents. Each extractor type is designed for specific kinds of analysis and has defined accuracy levels, validation requirements, and reliability factors.

.. note::
   Accuracy levels in the framework are defined as:
   
   * Very High: 95% accuracy
   * High: 85% accuracy
   * Medium High: 75% accuracy
   * Medium: 65% accuracy
   * Low: 50% accuracy

Physical Measurement Extractors
----------------------------
:Getty AAT: `300053578 <http://vocab.getty.edu/aat/300053578>`_
:CIDOC CRM: Activity: :class:`E16_Measurement`, Result: :class:`E54_Dimension`

Methods for extracting dimensional data from various documents:

* **3D Model Analysis**
    * Source documents: 3D scans, photogrammetric models, CAD models
    * Target qualia: height, width, depth, diameter, volume
    * Accuracy level: High (85%)
    * Tools:
        * 3D software
        * Measurement tools
    * Reliability factors:
        * Model resolution
        * Registration quality
        * Point cloud density
    * Validation requirements:
        * Peer review required
        * Cross verification required
        * Minimum 5 samples

* **Technical Drawing Analysis**
    * Source documents: architectural drawings, survey drawings, construction plans
    * Target qualia: height, width, depth, diameter
    * Accuracy level: Medium High (75%)
    * Tools:
        * CAD software
        * Digital measurement tools
    * Reliability factors:
        * Drawing accuracy
        * Scale reliability
        * Detail level
    * Validation requirements:
        * Peer review required
        * Cross verification required
        * Minimum 3 samples

Material Analysis Extractors
-------------------------
:Getty AAT: `300053816 <http://vocab.getty.edu/aat/300053816>`_
:CIDOC CRM: Activity: :class:`E7_Activity`, Procedure: :class:`E29_Design_or_Procedure`

* **Photographic Analysis**
    * Source documents: photographs, microscope images, spectral images
    * Target qualia: material type, surface treatment, conservation state
    * Accuracy level: Medium (65%)
    * Tools:
        * Image analysis software
        * Comparative databases
    * Reliability factors:
        * Image quality
        * Lighting conditions
        * Camera calibration
    * Validation requirements:
        * Peer review required
        * Cross verification required
        * Minimum 3 samples

* **Laboratory Report Analysis**
    * Source documents: material analysis reports, scientific studies, test results
    * Target qualia: material composition, physical properties, chemical properties
    * Accuracy level: Very High (95%)
    * Tools:
        * Scientific databases
        * Analysis protocols
    * Reliability factors:
        * Lab credibility
        * Methodology soundness
        * Sample representativeness
    * Validation requirements:
        * Peer review required
        * Cross verification required
        * Minimum 1 sample

Temporal Analysis Extractors
-------------------------
:Getty AAT: `300054714 <http://vocab.getty.edu/aat/300054714>`_
:CIDOC CRM: Activity: :class:`E13_Attribute_Assignment`, Result: :class:`E52_Time-Span`

* **Archival Document Analysis**
    * Source documents: historical documents, archival records, historical maps
    * Target qualia: construction date, modification date, historical phase
    * Accuracy level: Medium High (75%)
    * Tools:
        * Archival databases
        * Document analysis software
    * Reliability factors:
        * Document authenticity
        * Source reliability
        * Contextual consistency
    * Validation requirements:
        * Peer review required
        * Cross verification required
        * Minimum 2 samples

* **Scientific Dating Analysis**
    * Source documents: laboratory reports, dating certificates, analysis results
    * Target qualia: absolute date, date range, chronological phase
    * Accuracy level: Very High (95%)
    * Tools:
        * Dating databases
        * Calibration software
    * Reliability factors:
        * Method reliability
        * Sample quality
        * Contextual association
    * Validation requirements:
        * Peer review required
        * Cross verification required
        * Minimum 1 sample

Functional Analysis Extractors
---------------------------
:Getty AAT: `300068003 <http://vocab.getty.edu/aat/300068003>`_
:CIDOC CRM: Activity: :class:`E13_Attribute_Assignment`, Result: :class:`E55_Type`

* **Architectural Analysis**
    * Source documents: architectural plans, technical reports, building surveys
    * Target qualia: spatial organization, circulation pattern, structural role
    * Accuracy level: High (85%)
    * Tools:
        * Architectural software
        * Spatial analysis tools
    * Reliability factors:
        * Documentation completeness
        * Architectural expertise
        * Contextual understanding
    * Validation requirements:
        * Peer review required
        * Cross verification required
        * Minimum 3 samples

* **Use Pattern Analysis**
    * Source documents: historical accounts, ethnographic studies, user documentation
    * Target qualia: primary function, secondary functions, use evolution
    * Accuracy level: Medium (65%)
    * Tools:
        * Comparative databases
        * Pattern analysis software
    * Reliability factors:
        * Source reliability
        * Temporal coverage
        * Cultural context
    * Validation requirements:
        * Peer review required
        * Cross verification required
        * Minimum 5 samples

Cultural Analysis Extractors
-------------------------
:Getty AAT: `300379612 <http://vocab.getty.edu/aat/300379612>`_
:CIDOC CRM: Activity: :class:`E13_Attribute_Assignment`, Result: :class:`E28_Conceptual_Object`

* **Iconographic Analysis**
    * Source documents: photographs, drawings, historical illustrations
    * Target qualia: symbolic meaning, artistic style, iconographic program
    * Accuracy level: Medium High (75%)
    * Tools:
        * Iconographic databases
        * Comparative catalogs
    * Reliability factors:
        * Expert knowledge
        * Comparative material
        * Cultural context
    * Validation requirements:
        * Peer review required
        * Cross verification required
        * Minimum 3 samples

* **Historical Context Analysis**
    * Source documents: historical texts, period documents, contemporary accounts
    * Target qualia: cultural significance, historical context, social value
    * Accuracy level: Medium (65%)
    * Tools:
        * Historical databases
        * Context analysis software
    * Reliability factors:
        * Source credibility
        * Contextual understanding
        * Historiographical consensus
    * Validation requirements:
        * Peer review required
        * Cross verification required
        * Minimum 5 samples

Conservation Analysis Extractors
-----------------------------
:Getty AAT: `300435429 <http://vocab.getty.edu/aat/300435429>`_
:CIDOC CRM: Activity: :class:`E14_Condition_Assessment`, Result: :class:`E3_Condition_State`
:CEN 16096: Condition Assessment Level 1, Visual survey

* **Condition Report Analysis**
    * Source documents: condition reports, conservation surveys, monitoring records
    * Target qualia: conservation state, degradation patterns, intervention needs
    * Accuracy level: High (85%)
    * Tools:
        * Condition assessment software
        * Documentation databases
    * Reliability factors:
        * Report completeness
        * Assessor expertise
        * Temporal coverage
    * Validation requirements:
        * Peer review required
        * Cross verification required
        * Minimum 1 sample

* **Intervention History Analysis**
    * Source documents: restoration reports, intervention documentation, maintenance records
    * Target qualia: previous interventions, treatment effectiveness, maintenance needs
    * Accuracy level: Medium High (75%)
    * Tools:
        * Conservation databases
        * Intervention tracking software
    * Reliability factors:
        * Documentation quality
        * Intervention documentation
        * Follow-up records
    * Validation requirements:
        * Peer review required
        * Cross verification required
        * Minimum 2 samples

.. note::
   All extractors require peer review and cross verification to ensure reliability and accuracy of the extracted information. The minimum number of samples varies based on the extractor type and its specific requirements.