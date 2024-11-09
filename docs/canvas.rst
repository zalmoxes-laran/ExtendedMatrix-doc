Canvas
======

The Extended Matrix is drawn within a canvas, which serves as the frame where all nodes and data are displayed, enabling their organization for a clear and effective representation of information.

.. figure:: img/canvas_example.png
   :width: 400px
   :align: left

   *The canvas where all the nodes are drawn.*

As in the Harris Matrix, the Y-axis represents time (newer elements at the top, older ones at the bottom). The canvas is typically divided into swimlanes (horizontal stripes) that define epochs (`EpochNode`) or time periods. These divisions are established during the study of the context (for instance, when analyzing a Roman villa) as a preliminary, macroscopic organization of the archaeological remains (including elements that are no longer present or were never built) into different historical phases. This division can be iteratively modified at any time by adding new swimlanes and moving the necessary nodes to their correct epoch.
The canvas can also be divided into sectors (vertical columns) to distinguish spatially separate areas of the site (such as the peristylium, room A, room B, fauces, etc.). At the top, there is a title that identifies the canvas. Formally, this title is a node and, like other nodes, can have a description (not mandatory) providing essential information.
The canvas enables one of the most powerful features of the Extended Matrix formal language: the data funnel.

Data Funnel Structure
---------------------

The Extended Matrix utilizes a hierarchical data structure known as the **Data Funnel**. This structure organizes data into three levels of granularity, ensuring consistency, avoiding duplication, and providing detailed information where necessary.

.. figure:: img/data_funnel.png
   :width: 600px
   :align: center
   
   *Data Funnel with: A) General Data, B) Local Data, and C) Specific Data are located.*

1. General Background Data
--------------------------

**Definition**: General Background Data encompasses information that applies uniformly to all nodes within the knowledge graph of the Extended Matrix. These data provide a global context, essential for maintaining coherence across different elements and preventing data duplication.

**Values**:

- **Extended Matrix ID**: An identifier assigned to a coherent stratigraphic portion of an archaeological site or monument. This ID helps avoid duplications and maintains consistency in node identification within the graph.

- **ORCID**: Unique identifiers of authors involved in the project, allowing each node to be linked to a specific author in a structured and identifiable manner.

- **Licence**: 

- **Embargo**: expressed in months,  

**Objective**: To ensure that every node in the graph is coherently linked to a set of common properties, maintaining the integrity of the system and providing adequate granularity.

2. Local Background Data
------------------------

**Definition**: Local Background Data are information that apply only to a subset of stratigraphic nodes. These data include properties shared among certain nodes that belong to the same context or chronological period, defined by a shared temporal property.

**Values**:

- **start and end**: A time interval (temporal delta) assigned to a group of stratigraphic nodes sharing common characteristics. The temporal delta is based on an interpretation of evidence, such as formal coherence or the use of the same construction technique (e.g., Roman Era, 0-100 AD).

**Objective**: To connect groups of nodes to a common temporal or functional context, simplifying the representation of multiple nodes sharing similar properties within a specific context.

3. Specific Node Data
---------------------

**Definition**: Specific Node Data represent the unique information that applies to individual stratigraphic units. These data take precedence over Local Background Data and can override shared properties when necessary.

**Values**:

- **Start Time** and **End Time**: The specific temporal properties of a stratigraphic unit indicating its chronological limits. These data override shared Temporal Deltas.

- **Qualia**: Physical Properties like Material, style, dimensions (height, width, length), and state (existing or destroyed) of the stratigraphic unit or subjective properties to express how thigs were percived in the past (meaning, scope, etc...).

**Objective**: To provide detailed descriptions of each node's unique characteristics, offering more granular and precise information compared to Local Background Data.

Data Propagation Protocol
-------------------------

**Definition**: The Data Propagation Protocol is the mechanism by which temporal data are propagated among nodes in the graph. It is based on the hierarchical levels of the Data Funnel and uses a fallback system when specific data are missing.

**Rules of the Protocol**:

1. If a node has both **Start Time** and **End Time**, these values are used as its temporal reference.

2. If the **End Time** is missing, the system ascends to the parent stratigraphic node to find an appropriate **End Time**.

3. If no **End Time** is found in any parent node, the **End Time** from the shared **Temporal Delta (Epoch Node)** is used to temporally contextualize the node.

**Example of Application**:

- A node with a Start Time of 20 AD and an End Time of 40 AD will be included in a chronological query between 30 and 35 AD.

- If a node lacks an End Time, the system uses the End Time from the parent node or the shared Temporal Delta to determine its temporal context.

**Objective**: To ensure that temporal data are correctly inherited or propagated among nodes, maintaining consistency in chronological visualizations.

Benefits of the Data Funnel Structure
-------------------------------------

- **Consistency**: By defining data at different levels, the Data Funnel ensures that nodes share common properties where appropriate, reducing inconsistencies.

- **Avoidance of Duplication**: General and Local Background Data prevent the need to repeat the same information across multiple nodes.

- **Granularity**: Specific Node Data allow for detailed descriptions when necessary, providing precise information for individual nodes.

- **Efficient Data Management**: The hierarchical structure facilitates easier data management and updates, as changes at higher levels automatically propagate to relevant nodes.

Conclusion
----------

The Data Funnel structure in the Extended Matrix provides a robust framework for organizing stratigraphic data. By categorizing information into General Background Data, Local Background Data, and Specific Node Data, the system balances the need for both shared context and detailed specificity, enhancing the overall integrity and usability of the stratigraphic knowledge graph.

