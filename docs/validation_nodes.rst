Paradata Nodes
=============

.. _paradatanodes:

Introduction
-----------

Paradata nodes (also known as validation nodes) are a specialized set of nodes designed to express data provenance—documenting how we know what we know about stratigraphic units. These nodes form a "family" that works together to create a clear chain of evidence and interpretation.

.. admonition:: Example
   :class: example

   When an archaeologist documents a marble capital, they might need to support their assertions about its material, decoration, or dimensions with various sources and interpretations. Paradata nodes help track this chain of evidence systematically.

Node Types in Archaeological Context
---------------------------------

.. _propertynode:

Property Node
~~~~~~~~~~~~

A property node represents a specific characteristic or attribute of a stratigraphic unit. The name of a property corresponds to its type (e.g., "material", "height", "length").

.. note::
   For a complete taxonomy of property types and their relationships, please refer to the Properties and Qualia section of this documentation.

.. admonition:: Example
   :class: example

   For a column base, properties might include:
   * material = marble
   * height = 45cm
   * style = Doric

.. admonition:: Technical Tip
   :class: technical-tip

   s3Dgraphy automatically generates unique identifiers by combining the ID of the connected stratigraphic unit with the property name (e.g., "USM100.height", "SF10.material").

.. _documentnode:

Document Node
~~~~~~~~~~~~

A document node represents primary sources that provide evidence about stratigraphic units.

.. admonition:: Example
   :class: example

   Common document types include:
   * Excavation reports
   * Historical photographs
   * Ancient texts
   * Survey drawings

.. _extractornode:

Extractor Node
~~~~~~~~~~~~~

An extractor node captures how researchers interpret information from source documents.

.. admonition:: Example
   :class: example

   An archaeologist reading a 19th-century excavation report might note: "The description on page 10 clearly identifies this capital as being made of Pentelic marble, based on the crystalline structure described."

.. _combinernode:

Combiner Node
~~~~~~~~~~~~

A combiner node represents the synthesis of multiple interpretations to support a single conclusion.

.. admonition:: Example
   :class: example

   An archaeologist might combine:
   * A historical photograph showing column dimensions
   * An excavation report describing material
   * A comparative analysis of similar structures
   To establish comprehensive documentation of a column's properties.

Working Together: The Paradata Chain
---------------------------------

.. admonition:: Example
   :class: example

   Consider documenting a fragmentary lintel:

   1. **Physical Evidence**: Fragmentary lintel (SU003)
   2. **Source**: Historical photograph of Temple of Mars, Rome (D01)
   3. **Interpretation**: Analysis of decorative elements visible in photograph
   4. **Property**: Decoration style attribution

.. admonition:: Technical Tip
   :class: technical-tip

   The paradata chain follows the DIKW (Data-Information-Knowledge-Wisdom) hierarchy:
   * Data: Raw sources (Document Nodes)
   * Information: Interpreted sources (Extractor Nodes)
   * Knowledge: Combined interpretations (Combiner Nodes)
   * Wisdom: Applied understanding (Property Nodes)

Multiple Source Validation
------------------------

.. admonition:: Example
   :class: example

   Complex properties often require multiple sources:

   * Physical elements: Fragmentary lintel (SU003) atop two columns
   * Sources: Position measurements of both columns
   * Interpretation: Analysis of spatial relationships
   * Synthesis: Combined measurements determine total length
   * Property: Final length attribution

.. figure:: img/EM_Reference_CHART_C_graph.jpg
   :width: 400
   :align: center
   :alt: Paradata chain example
   :name: paradata_chain

   Example of paradata chain (Draft diagram - to be updated)

Implementation Details
-------------------

.. admonition:: Data Format
   :class: data-format

   Node naming conventions:
   * Document nodes: "D.01", "D.02", etc.
   * Extractor nodes: [Document ID].[sequence], e.g., "D.01.01"
   * Combiner nodes: "C.01", "C.02", etc.
   * Property nodes: [Unit ID].[property name], e.g., "USM100.height"

Best Practices
------------

1. **Documentation Chain Integrity**
   * Maintain clear links between all nodes in the chain
   * Document reasoning at each interpretation step
   * Preserve connection to original sources

2. **Multiple Source Handling**
   * Use combiner nodes when synthesizing multiple sources
   * Document conflicts or discrepancies between sources
   * Explain reasoning for preferring certain interpretations

3. **Property Documentation**
   * Link properties to supporting evidence
   * Document certainty levels
   * Note alternative interpretations when relevant

References
---------

The paradata chain concept is grounded in the DIKW (Data-Information-Knowledge-Wisdom) hierarchy:

* Ackoff, R. L. (1989). "From Data to Wisdom". Journal of Applied Systems Analysis, 16(1), pp. 3-9.

.. admonition:: Technical Note
   :class: technical-tip

   For details on implementing these concepts in s3Dgraphy and integration with other systems, please refer to the Technical Documentation section.