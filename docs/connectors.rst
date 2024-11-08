Extended Matrix Connectors
=========================

.. _emconnectors:

General background on Extended Matrix connections
-------------------------------------------------

In the Extended Matrix formal language, connectors (or edges) represent relationships between different nodes in the stratigraphic documentation. These connections help establish temporal sequences, show relationships between elements, and document data provenance. Each connector type has specific rules about which kinds of nodes it can connect, ensuring that the resulting graph maintains logical consistency.

Connector Types
---------------

1. Chronological Relationships
------------------------------

These connectors establish temporal relationships between stratigraphic units.

.. _isbefore:

1.1. Is Before (is_before)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/connectors/is_before.png
   :width: 128px
   :align: left

Indicates a temporal sequence where one stratigraphic unit occurs before another. This is one of the fundamental relationships in stratigraphic documentation, establishing the chronological order of events and formations.

**Allowed Connections:**
  * Source: Stratigraphic Unit
  * Target: Stratigraphic Unit

.. _hassametime:

1.2. Has Same Time (has_same_time)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/connectors/has_same_time.png
   :width: 128px
   :align: left

Indicates that two elements are contemporaneous, meaning they existed or were created at the same time. This relationship helps establish horizontal relationships in the stratigraphic sequence.

**Allowed Connections:**
  * Source: Stratigraphic Unit
  * Target: Stratigraphic Unit

.. _changedfrom:

1.3. Changed From (changed_from)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/connectors/changed_from.png
   :width: 128px
   :align: left

Represents the transformation of an object over time, indicating that one stratigraphic unit evolved or changed into another form.

**Allowed Connections:**
  * Source: Stratigraphic Unit
  * Target: Stratigraphic Unit

2. Provenance Relationships
--------------------------

.. _provenance:

2.1. Provenance (provenance)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/connectors/provenance.png
   :width: 128px
   :align: left

Represents all data and property provenance relationships in the Extended Matrix. This connector type is used to document how properties are associated with stratigraphic units, how data is extracted from sources, and how information is combined or synthesized.

**Allowed Connections:**
  * Between Stratigraphic Units and Property Nodes
  * Between Property Nodes and Extractor/Combiner Nodes
  * Between Extractor Nodes and Document Nodes
  * Between Combiner Nodes and Extractor Nodes

3. Special Relationships
-----------------------

These connectors handle specific cases and general relationships.

.. _contrastswith:

3.1. Contrasts With (contrasts_with)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/connectors/contrasts_with.png
   :width: 128px
   :align: left

Represents contrasting or mutually exclusive time branches in the documentation.

**Allowed Connections:**
  * Source: Time Branch Node Group
  * Target: Time Branch Node Group

.. _genericconnection:

3.2. Generic Connection (generic_connection)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/connectors/generic_connection.png
   :width: 128px
   :align: left

Represents a non-specific connection between nodes when other specific relationship types don't apply.

**Allowed Connections:**
  * Source: Stratigraphic Unit, Property Node
  * Target: Stratigraphic Unit, Property Node

Technical Implementation Notes
------------------------------

Provenance Implementation in s3dgraphy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While the Extended Matrix formal language defines a single "provenance" connector type, the s3dgraphy library internally differentiates this connection based on the types of nodes being connected:

* When connecting a Stratigraphic Unit to a Property Node, it's treated as a "has_property" relationship
* When connecting a Property Node to an Extractor/Combiner Node, it's handled as a "has_data_provenance" relationship
* When connecting an Extractor Node to a Document Node, it's processed as an "extracted_from" relationship
* When connecting a Combiner Node to an Extractor Node, it's managed as a "combines" relationship

This internal differentiation allows s3dgraphy to maintain appropriate validation rules and processing logic while presenting a simplified connection model to users.

Swimlanes and Groups in the Multi-Knowledge Graph (MKG)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the visualization of the Extended Matrix, swimlanes and groups are represented as visual containers. However, s3dgraphy internally interprets these as nodes with specific connections to the elements they contain:

1. **Epoch Swimlanes**
   * Nodes within an epoch swimlane are connected to that epoch through two possible relationships:
     - ``has_first_epoch``: Indicates the swimlane where a stratigraphic unit first appears
     - ``survive_in_epoch``: Used for subsequent swimlanes where the unit continues to exist
   * The survival of a unit in subsequent epochs depends on its relationship with chronologically later continuity nodes

2. **Activity Groups**
   * Elements within an activity group are connected to the group through the ``has_activity`` relationship
   * This allows for the organization and categorization of related stratigraphic units based on common activities or events

3. **Time Branch Groups**
   * Nodes within a time branch group are connected to that group through the ``has_timebranch`` relationship
   * This structure enables the representation of alternative interpretations or hypotheses about the stratigraphic sequence

These internal representations allow s3dgraphy to maintain the logical structure of the Extended Matrix while providing an intuitive visual representation through swimlanes and groups in the user interface.