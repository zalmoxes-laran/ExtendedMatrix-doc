Properties of the EM
====================

.. _whatareproperties:

What is a property ?
--------------------

A property is an element that defines a quality of the object to be represented. 
Properties include


.. _existence:

Existence
---------

The existence property contains the wisdom of the existence of an element.

According to the kind of US-node it is connected to, it can be implicit or to be made explicit.
An implicit existence is not mandatory nor suggested, an explicit existence should be declared.

An implicit existance is in the case of US/USM that are real elements you can see and touch. The same thing happens with the USV/s nodes that represents elements whose existence property is certain. 

Examples of existence to be made explicit are USD, USV/n and VSF whose certainty of existence should be justified by mentioning the main proof we have.  

.. _geometry:

Geometry
--------

The geometry property defines the dimensions of the object (length, width, thickness, shape).  
Within the Extended Matrix, the geometry property can be defined, for example, by a floor plan or photogrammetric model of the area to be reconstructed.

**The proxy IS this property.** What has always been called the *proxy* of a
stratigraphic unit — its geometry-without-material, the volume you segment out
of a photogrammetric model — is not a thing standing beside the unit: it is one
of the unit's properties, a quale like colour or dating, that answers *what
shape does this unit have, and where*.

Two parts, and the division is the whole point:

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Part
     - What it holds
   * - the **property** (``geometry``)
     - the assertion — *this unit has this shape* — and, through the ordinary
       paradata chain, **how we know it**: which extractor read it, from which
       source, and which combiner reconciled several readings.
   * - the **semantic shape**
     - the numbers: convex hulls and spheres, or a ``.glb`` file. Attached to the
       property with ``has_semantic_shape``.

The shape carries no argument and the property carries no coordinates. That is
deliberate: the numbers can live in a file when they are large and inline when
they are small, without changing anything about what the property *says*.

Why it matters — a lone shape cannot say where it came from. As a property, the
geometry inherits the same chain every other quale has, and one consequence
follows immediately: **the same geometry can be synthesised from several
sources**. A recent but incomplete photogrammetric survey and a historical
photograph become two extractors, joined by a combiner, concluding in one
geometry — instead of two disconnected shapes with nothing to say which is
which.

The sources may include a **2D annotation**: a region traced on a photograph or
a drawing is evidence, and an extractor can be based on it. See
:doc:`extractor_nodes` and :ref:`paradatanodes`.

.. admonition:: Changed in EM 1.6
   :class: warning

   Until EM 1.6 the proxy was modelled as an object of its own, attached
   directly to the unit. From EM 1.6 it is a **property of type ``geometry``**
   whose payload is the semantic shape (``has_semantic_shape``).

   Nothing was taken away from the shape — same geometry, same file, same
   meaning. What changed is **who points at it**: the unit points at the
   property, and the property points at the shape.

   *Consequences for existing material.* Graphs authored before EM 1.6 keep
   their geometry and keep working; what they lack is the chain of paradata,
   because a standalone shape never had one. A one-shot migration of legacy
   graphs (standalone shape → geometry property + payload) is planned. Software
   that reads the proxy — EM Tools for Blender, Heriverse, any parser walking
   the graph — must follow the property instead of looking for a shape hanging
   off the unit.

.. _placement:

Placement
--------

Placement is the property that defines the exact location of geometry, either in local or global coordinates. The main sources from which to infer the positioning property of geometry are technical drawings, excavation plans, and photogrammetric models.


.. _material:

Material
--------
Material property defines the material(s) of which the object is made. This characteristic can be inferred from various sources, such as excavation reports, ancient sources etc.


.. _color:

Color
--------
The color property defines the original color(s) of the object. As with the :ref:`material` property, it can be defined from excavation reports and ancient sources.