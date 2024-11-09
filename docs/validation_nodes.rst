Paradata Nodes
=============

.. _paradatanodes:

General background on paradata nodes
----------------------------------

Paradata nodes (also known as validation nodes) are a specialized set of nodes designed to express data provenance—documenting how we know what we know about stratigraphic units. These nodes form a "family" that works together to create a clear chain of evidence and interpretation, following the DIKW (Data-Information-Knowledge-Wisdom) hierarchy.

Each node within the paradata family must have a unique identifier to enable precise referencing within the Extended Matrix. These identifiers follow specific naming conventions detailed under each node type.

Node Types
---------


1. Property Node
----------------

.. _propertynode:

.. image:: img/2D/property.png
   :width: 128px
   :align: left

A property node represents a specific characteristic or attribute of a stratigraphic unit. Examples include material composition, dimensions, color, or any other measurable or observable property.

**Naming Convention:**
  The name of a property node corresponds to the type of property or qualia it represents (e.g., "material", "height", "length", "color"). s3Dgraphy automatically generates unique identifiers by combining the ID of the connected stratigraphic unit with the property name.

**Examples:**
  * "USM100.height" for the height property of stratigraphic unit USM100
  * "SF10.length" for the length property of special find SF10
  * "USV50.material" for the material property of virtual stratigraphic unit USV50

This naming approach ensures that:
1. Properties are consistently categorized by their type
2. Each property instance is uniquely identified in relation to its stratigraphic unit
3. The relationship between properties and units is immediately clear from the identifier

**Usage Example:**
  Property "material = marble" associated with a capital


2. Document Node
---------------

.. _documentnode:

.. image:: img/2D/document.png
   :width: 128px
   :align: left

Also known as a source node, a document node represents the primary source of information. This could be an excavation report, historical document, photograph, or any other form of documentation that provides evidence about a stratigraphic unit.

**Naming Convention:**
  * Prefix: "D."
  * Example: "D.01" for the first document

**Usage Example:**
  An excavation report from the 19th century describing a marble capital

1. Extractor Node
----------------

.. _extractornode:

.. image:: img/nodes/extractor.png
   :width: 128px
   :align: left

An extractor node represents the interpretation of information from a document node by a researcher. It captures the specific way in which information from a source is understood and applied to understanding a stratigraphic unit.

**Naming Convention:**
  * Composed of the related document name plus a sequence number
  * Example: "D.01.01" for the first extraction from Document 1

**Usage Example:**
  "At page 10 of document D.01, a description clearly refers to that capital"

4. Combiner Node
---------------

.. _combinernode:

.. image:: img/nodes/combiner.png
   :width: 128px
   :align: left

A combiner node represents the synthesis of multiple interpretations from different sources. It is used when a property or characteristic is determined through the consideration of multiple pieces of evidence.

**Naming Convention:**
  * Prefix: "C."
  * Example: "C.01" for the first combiner node

**Usage Example:**
  "Based on the interpretation of document A and the interpretation of document B, we can conclude the material is marble"


Working Together: Practical Examples
---------------------------------

1. Single Source Property Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: img/EM_Reference_CHART_C_a.jpg
   :width: 400
   :align: center

Consider a fragmentary lintel (SU003) with a reconstructed USV/s 100. A "decoration" property is established through:
* Document Node (D.01): A photograph of the Temple of Mars in Rome
* Extractor Node (D.01.01): Interpretation focusing on relevant decorative elements
* Property Node (P.01): Final decoration attribution

This example demonstrates how a single source can be used to validate a property of a virtual reconstruction.

2. Multiple Source Property Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: img/EM_Reference_CHART_C_b.jpg
   :width: 400
   :align: center

In a more complex case, consider:
* Physical elements: fragmentary lintel (SU003) atop two columns (SU001, SU002)
* Virtual reconstruction: USV/s 100
* Properties to validate: length and decoration

The length property is particularly interesting as it's derived from two sources:
* Document Nodes (D.01, D.02): Position measurements of both columns
* Extractor Nodes: Interpretations of measurements
* Combiner Node: Synthesis of measurements to determine total length
* Property Node: Final length attribution

Certainty Levels in Virtual Reconstructions
----------------------------------------

The Extended Matrix recognizes three levels of certainty in virtual reconstructions (USV):

1. **Structural (USV/s)**
   * Highest certainty level
   * Based on physical evidence and clear stratigraphic relationships
   * Properties typically supported by direct archaeological evidence

2. **Non-structural (USV/n)**
   * Medium certainty level
   * Based on comparative analysis and architectural rules
   * Properties often supported by multiple indirect sources

3. **Special Find Reintegration (VSF)**
   * Specific certainty level for repositioned elements
   * Based on archaeological finds and architectural analysis
   * Properties validated through both direct and comparative evidence

Best Practices
-------------

1. **Unique Identification**
   * Ensure each node has a unique identifier following the naming conventions
   * Use consistent prefixes (P., D., C.) for easy identification

2. **Clear Documentation**
   * Document the rationale for each extraction and combination
   * Maintain clear references to specific sections or pages in source documents

3. **Chain Integrity**
   * Maintain clear connections between related nodes
   * Document any assumptions or uncertainties in interpretations

4. **Version Control**
   * Track changes to interpretations over time
   * Document when and why combinations of evidence are updated

Implementation in Extended Matrix
------------------------------

.. figure:: img/EM_Reference_CHART_C_graph.jpg
   :width: 400
   :align: center

The example above shows a complete paradata chain, demonstrating how different node types work together to validate properties of virtual reconstructions. This implementation follows the DIKW hierarchy:
* Data: Raw sources (Document Nodes)
* Information: Interpreted sources (Extractor Nodes)
* Knowledge: Combined interpretations (Combiner Nodes)
* Wisdom: Applied understanding (Property Nodes)