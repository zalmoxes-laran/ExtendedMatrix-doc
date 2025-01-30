Properties (Qualia)
===================

.. _qualia:

Introduction
-----------

The Extended Matrix adopts and extends Pustejovsky's qualia theory to create a comprehensive system for documenting both objective and subjective properties in archaeological documentation. While the original qualia structure provides a solid foundation for describing object properties, the Extended Matrix extends this framework to handle the specific needs of archaeological documentation, including temporal perceptions and degrees of certainty.

The **Qualia Roles**, introduced by **James Pustejovsky** in *The Generative Lexicon* (1995), aim to model **the dynamic nature of meaning** in natural language. Traditional lexicons treat word meanings as fixed, but Qualia Roles explain **systematic polysemy** by defining four semantic dimensions: **Formal (what it is), Constitutive (what it’s made of), Telic (what it’s for), and Agentive (how it came to be)**. Rooted in **computational linguistics**, this framework enhances **natural language processing (NLP)** by allowing AI to infer context-dependent meanings. It emerged from the need to **overcome rigid lexical databases** in favor of **generative, flexible semantics**. Beyond linguistics, Qualia Roles resonate with **cognitive science, philosophy, and knowledge representation**, offering a **transdisciplinary** approach. By integrating **historical, functional, and structural aspects of meaning**, they **enable holistic knowledge modeling**, crucial for fields like **archaeology, AI, and digital humanities**, where **multifaceted interpretation** is essential.

The **Extended Matrix** expands Qualia Roles into a **qualitative knowledge graph for Cultural Heritage**, integrating **temporal, material, and interpretative dimensions** to document archaeological data **holistically** and trace the **evolution of meaning across historical contexts**. It introduces **ActorNodes** to manage **temporal perceptions**, allowing **multiple interpretations** to coexist within the documentation system. By **linking properties to paradata chains** and **documenting certainty levels**, it ensures **transparent, validated data**. The Extended Matrix is a **flexible, generative framework** that **adapts to diverse archaeological contexts**, offering a **comprehensive, dynamic model** for **multidimensional knowledge representation**.

Original Qualia Framework
-----------------------

Pustejovsky (1995) defined four fundamental qualia roles:

1. **Formal quale**: What kind of thing is it?
2. **Constitutive quale**: What is it made of?
3. **Telic quale**: What is it for?
4. **Agentive quale**: How did it come into being?

.. admonition:: Example
   :class: example

   In Pustejovsky's original framework, a column might be described as:
   * Formal: A vertical architectural support element
   * Constitutive: Made of marble
   * Telic: Supports the entablature
   * Agentive: Carved from a single block

Extended Matrix Qualia System
--------------------------

The Extended Matrix expands this framework to address the specific needs of archaeological documentation:

1. Fundamental Properties
~~~~~~~~~~~~~~~~~~~~~~~

.. _existence:

**Existence**
   The foundational property that must be established before any other qualia can be considered.
   
   * Physical existence (for US/USM)
   * Documented existence (for USD)
   * Hypothetical existence (for USV)
   * Reconstructed existence (for VSF)

2. Extended Qualia Roles
~~~~~~~~~~~~~~~~~~~~~~

2.1 Extended Formal Quale
^^^^^^^^^^^^^^^^^^^^^^^

Encompasses measurable and observable characteristics:

**Dimensions** (container property)
   * height
   * width
   * depth
   
   .. admonition:: Example
      :class: example

      A single "dimensions" property might contain "100,20,60 cm" instead of separate height, width, and depth properties.

**Position** (container property)
   * coordinates
   * orientation
   * elevation

2.2 Extended Constitutive Quale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Material** (container property)
   * primary_material
   * construction_technique
   * surface_treatment

2.3 Extended Telic Quale
^^^^^^^^^^^^^^^^^^^^^^

Includes both original and historical functions:
   * primary_function
   * secondary_uses
   * spatial_role
   * historical_adaptations

2.4 Extended Agentive Quale
^^^^^^^^^^^^^^^^^^^^^^^^^

Documents creation and modifications:
   * construction_date
   * builder
   * modification_history
   * conservation_status

3. Temporal Perception System
~~~~~~~~~~~~~~~~~~~~~~~~~~

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

.. admonition:: Technical Tip
   :class: technical-tip

   The ActorNode connects to properties through temporal relationships, allowing multiple interpretations to coexist within the documentation system.

Implementation Details
-------------------

.. admonition:: Data Format
   :class: data-format

   Property hierarchy example:

   ```json
   {
     "column_01": {
       "existence": {
         "type": "physical",
         "certainty": "confirmed"
       },
       "dimensions": {
         "value": "450,60,60",
         "unit": "cm",
         "contains": ["height", "width", "depth"],
         "method": "direct_measurement"
       },
       "perceptions": [
         {
           "actor": "ActorNode_01",
           "epoch": "100_CE",
           "properties": {
             "significance": "ritual",
             "status": "active_religious"
           }
         },
         {
           "actor": "ActorNode_02",
           "epoch": "2023_CE",
           "properties": {
             "significance": "archaeological",
             "status": "preserved"
           }
         }
       ]
     }
   }
   ```

Best Practices
------------

1. **Property Hierarchy Management**
   * Use container properties when possible
   * Document relationships between properties
   * Maintain consistent property structures

2. **Temporal Interpretation**
   * Always link subjective interpretations to ActorNodes
   * Document the temporal context of interpretations
   * Preserve multiple historical perspectives

3. **Evidence Documentation**
   * Link properties to paradata chains
   * Document certainty levels
   * Maintain clear validation paths

References
---------

* Pustejovsky, J. (1995). "The Generative Lexicon". MIT Press.