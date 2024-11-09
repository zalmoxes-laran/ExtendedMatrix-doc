Archaeological Properties and Qualia
=================================

.. _properties_and_qualia:

Introduction
-----------

The Extended Matrix uses a structured system of properties based on philosophical qualia (Pustejovsky, 1995) and adapted for archaeological documentation. This system recognizes both fundamental properties and hierarchical relationships between properties, allowing for flexible and precise documentation of archaeological findings.

1. Fundamental Properties
-----------------------

.. _existence:

1.1 Existence
~~~~~~~~~~~~

The existence property is fundamental in archaeological documentation, reflecting different levels of certainty about an element's historical presence.

**Certainty Levels:**
  * Confirmed (implicit for physical US/USM nodes)
  * Documented (for USD nodes, requires source citation)
  * Hypothetical (for USV/n nodes, requires justification)
  * Reconstructed (for VSF nodes, based on evidence)

2. Core Qualia Properties
-----------------------

Based on Pustejovsky's qualia structure and adapted for archaeological needs:

.. _formal:

2.1 Formal Quale (What it is)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Properties describing the physical nature and measurements of the element.

**Dimensions:**
  A container property that can be expressed either:
  
  * As a unified property:
    - Value format: "height,width,depth" (e.g., "100,20,60")
    - Units must be specified (e.g., "cm")
    
  * Or broken down into component properties:
    - Height
    - Width
    - Depth
    
  .. note::
     When dimensions are specified as a unified property, individual dimension properties should not be used.

**Position:**
  A container property that can include:
  
  * Coordinates (x,y,z)
  * Orientation
  * Elevation
  
**Shape:**
  * Basic geometry
  * Architectural type
  * Form classification

.. _constitutive:

2.2 Constitutive Quale (What it's made of)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Properties describing the material composition.

**Material:**
  A container property that can include:
  
  * Primary material
  * Construction technique
  * Surface treatment
  
**Physical Properties:**
  * Color
  * Texture
  * Density
  * State of conservation

.. _telic:

2.3 Telic Quale (What it's for)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Properties describing function and use.

**Function:**
  A container property that can include:
  
  * Primary function
  * Secondary uses
  * Spatial role
  
**Usage:**
  * Period of use
  * Type of use
  * Usage patterns

.. _agentive:

2.4 Agentive Quale (How it came to be)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Properties describing creation and modification.

**Creation:**
  A container property that can include:
  
  * Construction date
  * Builder/workshop
  * Construction technique
  
**Modifications:**
  * Restoration history
  * Adaptation phases
  * Destruction events

3. Interpretative Layer
---------------------

The interpretative layer connects properties to specific actors and epochs, allowing for the documentation of changing interpretations over time.

**Structure:**
  .. code-block:: json
  
  {
    "property": "function",
    "interpretations": [
      {
        "actor": "Archaeologist A",
        "epoch": "1900-1920",
        "value": "temple",
        "confidence": "high",
        "basis": "architectural features"
      },
      {
        "actor": "Archaeologist A",
        "epoch": "1920-1930",
        "value": "administrative building",
        "confidence": "medium",
        "basis": "new inscriptions found"
      }
    ]
  }

4. Best Practices for Property Usage
---------------------------------

1. **Hierarchical Properties:**
   * Use container properties when possible to reduce redundancy
   * Document which sub-properties are covered by a container property
   * Maintain consistency in property hierarchy across the documentation

2. **Property Values:**
   * Use standardized formats for values
   * Include units where applicable
   * Document value conventions in metadata

3. **Interpretative Documentation:**
   * Always link interpretations to specific actors and epochs
   * Document changes in interpretation over time
   * Maintain clear chains of evidence through paradata nodes

5. Implementation in Extended Matrix
--------------------------------

Example of property hierarchies in practice:

.. code-block:: json

{
    "node_id": "USM100",
    "properties": {
        "existence": {
            "value": "confirmed",
            "certainty": "physical"
        },
        "dimensions": {
            "value": "100,20,60",
            "unit": "cm",
            "contains": ["height", "width", "depth"]
        },
        "material": {
            "value": "marble",
            "contains": {
                "type": "Pentelic",
                "technique": "carved",
                "surface": "polished"
            }
        }
    },
    "interpretations": [
        // as shown in section 3
    ]
}

References
---------

* Pustejovsky, J. (1995). "The Generative Lexicon". MIT Press.
* [Additional references for archaeological property documentation conventions]