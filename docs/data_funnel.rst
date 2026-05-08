.. _data_funnel:

Data Funnel Structure
=====================

The Extended Matrix uses a **hierarchical data structure** — the
*Data Funnel* — to spread context across the graph without duplicating
it on every node. Three scopes hold values at increasing levels of
specificity: the :term:`Canvas` (global default), the :term:`Epoch`
swimlane (period-wide), and the individual stratigraphic node
(per-unit). When the resolver looks up a property, it walks these
scopes from the **most specific to the most general** and returns the
**first non-null value** it finds.

.. code-block:: text

   ┌─────────────────────────────────────────────────────────┐
   │   Resolution order — first non-null value wins          │
   └─────────────────────────────────────────────────────────┘

      ┌───────────────────────────────┐    ◄── HIGHEST priority
      │  Specific Node                │
      │  (US, USV, USD, SF, ...)      │
      │  start · end · qualia         │
      └───────────────┬───────────────┘
                      │  if not on the node ↓
                      ▼
      ┌───────────────────────────────┐
      │  Epoch Node   (swimlane)      │
      │  start · end                  │
      └───────────────┬───────────────┘
                      │  if not on the epoch ↓
                      ▼
      ┌───────────────────────────────┐    ◄── LOWEST priority (default)
      │  Canvas   (graph header)      │
      │  EM ID · ORCID · License ·    │
      │  Embargo                      │
      └───────────────────────────────┘

In plain prose: a value declared on a single node **wins over** the
value carried by its epoch swimlane; the epoch's value in turn **wins
over** the canvas-level default. In the opposite direction this is
*inheritance* — a node with no explicit value picks up its epoch's
value, and an epoch with no explicit value picks up the canvas
default.

The next three sections describe what each scope typically holds,
listed from the broadest (canvas) to the narrowest (specific node).

1. General Background Data
--------------------------

*Canvas-level scope — lowest priority, the default fallback that
applies to every node when no narrower scope declares the value.*

General Background Data encompasses information that applies uniformly to all nodes within the knowledge graph of the Extended Matrix. These data provide a global context, essential for maintaining coherence across different elements and preventing data duplication.

**Values**:

- **Extended Matrix ID**: An identifier assigned to a coherent stratigraphic portion of an archaeological site or monument. This ID helps avoid duplications and maintains consistency in node identification within the graph.
- **ORCID**: Unique identifiers of authors involved in the project, allowing each node to be linked to a specific author in a structured and identifiable manner.
- **Licence**: It uses the Creative Commons license schema (i.e., CC-BY-NC).
- **Embargo**: Expressed in months, it defines the disclosure moment in time when the dataset can be released to the public (using the license above).


To ensure that every node in the graph is coherently linked to a set of common properties, maintaining the integrity of the system and providing adequate granularity.

The Extended Matrix ID serves as a prefix to make each stratigraphic unit identifier unique across multiple excavation projects. This approach solves a common archaeological data management challenge: the same identifier (like "USM100") may be used across different excavation sites.

By adding a unique excavation ID prefix, we create globally unique identifiers. For example::

    GTS16.USM100

Where:

- **GTS16** is the Extended Matrix ID for the Great Temple of Sarmizegetusa, 2016 campaign
- **USM100** is the local stratigraphic unit identifier

.. note::
   **Moving from Individual Context to Landscape Analysis**

   Traditional archaeological documentation manages each excavation as a separate entity, making inter-site analysis challenging. The Extended Matrix ID system allows archaeologists to:

   1. **Manage multiple sites in a single Blender session**: Combine data from multiple excavations or monuments while maintaining distinct identification.

   2. **Prevent ID collisions**: Even when two different sites have identically numbered units (e.g., USM100), the prefixed IDs (GTS16.USM100 vs. PTR19.USM100) remain distinct.

   3. **Enable landscape-level analysis**: By integrating multiple sites with unique identifiers, researchers can shift from analyzing individual contexts to understanding entire archaeological landscapes.

   4. **Facilitate collaboration**: Team members working on different sites can share a single data environment while maintaining organizational clarity.

This approach creates a hierarchical namespace for archaeological data, similar to domain naming systems used in other fields, ensuring that local identifiers remain meaningful within their context while becoming globally unique when combined with the Extended Matrix ID.

2. Local Background Data
------------------------

*Epoch-level scope — wins over the canvas default; applies uniformly
to every node placed in the same swimlane unless overridden at the
node level.*

**Definition**: Local Background Data are information that apply only to a subset of stratigraphic nodes. These data include properties shared among certain nodes that belong to the same context or chronological period, defined by a shared temporal property.

**Values**:
- **start** and **end**: Define the temporal boundaries of each Epoch - graphically represented with a swimlane - (``EpochNode``), representing a time interval (e.g., Augustan Era: -27 to 14). These dates are determined through macroscopic interpretation of archaeological evidence such as architectural styles, construction techniques, and formal coherence.

**Objective**: To connect groups of nodes to a common temporal or functional context, simplifying the representation of multiple nodes sharing similar properties within a specific context.

3. Specific Node Data
---------------------

*Node-level scope — highest priority, wins over both the epoch
swimlane and the canvas default.*

**Definition**: Specific Node Data represent the unique information that applies to individual stratigraphic units. These data take precedence over Local Background Data and can override shared properties when necessary.

**Values**:

- **Start Time** and **End Time**: The specific temporal properties of a stratigraphic unit indicating its chronological limits. These data override shared Temporal Deltas.

- **Qualia**: Physical Properties like Material, style, dimensions (height, width, length), and state (existing or destroyed) of the stratigraphic unit or subjective properties to express how thigs were percived in the past (meaning, scope, etc...).

**Objective**: To provide detailed descriptions of each node's unique characteristics, offering more granular and precise information compared to Local Background Data.

Data Propagation Protocol
-------------------------

The mechanism by which a query for the value of a property on a node
walks the Data Funnel. The rule is the same as the resolution order
above and applies uniformly to temporal bounds, authorship, licence,
embargo and any other propagatable property:

1. If the **specific node** carries the value, use it.
2. Otherwise, fall back to the value declared on the **epoch
   swimlane** the node belongs to.
3. Otherwise, fall back to the **canvas**-level default.
4. If none of the three scopes carries the value, the property is
   undefined at that point in the graph.

**Worked example — temporal resolution on a USM node:**

- The node declares ``start = 20 AD, end = 40 AD`` → both bounds
  resolve to the node's own values; the node is included in a
  chronological query for the ``30–35 AD`` window.
- The node declares ``start = 20 AD`` and no ``end`` → ``start``
  resolves to the node, ``end`` falls back to the epoch swimlane's
  ``end``.
- The node declares no times at all → both ``start`` and ``end``
  resolve to the epoch swimlane's bounds.

**Objective**: ensure that values are correctly inherited or
overridden along the node → epoch → canvas chain, keeping the graph
consistent without forcing every node to redeclare context that is
already shared at a broader scope.

Benefits of the Data Funnel Structure
-------------------------------------

- **Consistency**: By defining data at different levels, the Data Funnel ensures that nodes share common properties where appropriate, reducing inconsistencies.

- **Avoidance of Duplication**: General and Local Background Data prevent the need to repeat the same information across multiple nodes.

- **Granularity**: Specific Node Data allow for detailed descriptions when necessary, providing precise information for individual nodes.

- **Efficient Data Management**: The hierarchical structure facilitates easier data management and updates, as changes at higher levels automatically propagate to relevant nodes.

Important Considerations
------------------------

.. note::
   **Setup of a new GrapML file**

   1. **Set the ID in the upper part of the canvas.** A common error when setting up a new GrapML file is to forget to set the Extended Matrix ID in the General Background Data. This omission can lead to confusion and potential ID collisions when integrating data from multiple excavation projects.

   2. **Set start and end for each epoch.** You need to set the start and end dates for each Epoch in the Local Background Data. This step is crucial for establishing the temporal framework within which the stratigraphic nodes will be contextualized.
   

Conclusion
----------

The Data Funnel structure in the Extended Matrix provides a robust framework for organizing stratigraphic data. By categorizing information into General Background Data, Local Background Data, and Specific Node Data, the system balances the need for both shared context and detailed specificity, enhancing the overall integrity and usability of the stratigraphic knowledge graph.

