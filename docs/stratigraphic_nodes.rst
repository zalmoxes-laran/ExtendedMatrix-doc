Stratigraphic Nodes
===================

.. _stratigraphicunits:

General background on stratigraphic units
-----------------------------------------

A stratigraphic unit in some academic scholarships is also known as locus or context. It indicates the result of an action that occurred at a specific moment in time. The result (the construction of a wall, the destruction of a roof, is the silt deposited on top of structures following a flood, the chemical change of surfaces due to a fire) in turn have a life span that ends with the moment it is defunctionalized (destroyed, abandoned, buried). It has a spatio-temporal nature: temporal persistence of a geometry in a given point in space. When the position change, the US will change its nature.

.. note::
  More details about the stratigraphic approach can be found  `here <stratigraphic_approach.html>`_

Stratigraphic units can be classified into main categories:
-----------------------------------------------------------

1. Physical Stratigraphic Units
-------------------------------

These are tangible units that either still exist or have left clear stratigraphic evidence. They can be directly observed, measured, and analyzed in the field. Physical stratigraphic units include existing walls, floors, deposits, or archaeological remains that have been documented through proper stratigraphic methods.

.. _usnode:

1.1. Stratigraphic Unit - US 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/2D/US.png
  :width: 128px
  :align: left

A Stratigraphic Unit indicates the result of an action that occurred at a specific moment in time. The SU defines objects found still *in situ* (and noted using the techniques of stratigraphic reading). These are tangible units that either still exist or have left clear stratigraphic evidence. They can be directly observed, measured, and analyzed in the field. Physical stratigraphic units include existing walls, floors, deposits, or archaeological remains that have been documented through proper stratigraphic methods.

.. _serusnode:

1.2. Serial Stratigraphic Unit - serSU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/2D/serSU.png
  :width: 128px
  :align: left

A Serial Stratigraphic Unit is employed when it is more practical and efficient to use a single unit to represent multiple serial elements of the same type. This approach is particularly useful for documenting architectural features such as a sequence of capitals, a series of column bases, a set of roof beams, or similar repetitive elements.

This type of serial documentation is specifically used when the elements in the series are geometrically discontinuous - meaning they do not physically touch each other. Examples include multiple wall segments that are spatially separated, freestanding column bases, or other architectural elements that share similar characteristics but are not physically connected.
The flexibility of this system allows for individual elements to be removed from the series and documented separately at any time, should they present unique characteristics or require detailed individual documentation. This might occur when an element shows distinctive decorative features, exhibits unusual wear patterns, or presents specific conservation issues that warrant individual attention.

.. _usd:

1. Documentary Stratigraphic Units (USD)
----------------------------------------

These units are known only through historical documentation. Their *existence* is verified through various historical sources considered reliable such as photographs, paintings and artistic representations, written descriptions, maps and plans, and oral histories. While not physically present, they can be reliably placed in the stratigraphic sequence based on documentary evidence. This category also includes repositioned elements (anastylosis) when their original position is confirmed by historical documentation.

.. image:: img/2D/USD.png
  :width: 128px
  :align: left

It connects to these properties:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* existence
* geometry
* placement
* material
* color
* etc..

1. Virtual Stratigraphic Units (USV)
------------------------------------

These represent elements that no longer exist and must be reconstructed. Their existence is inferred through presence of physical gaps on archaeological evidence, analysis of surrounding structures, architectural necessity, and comparative studies. Virtual units are essential for understanding the complete stratigraphic sequence, even though they cannot be directly observed. Their reconstruction requires careful analysis and interpretation of available evidence. 

They are divided into:

.. _usvnodes:

3.1 USV/s node:
~~~~~~~~~~~~~~~

.. image:: img/2D/USVs.png
  :width: 128px
  :align: left

Structural Virtual Stratigraphic Unit, a reconstruction hypothesis based on an in situ fragmented SU. It acts as a restoration of a -SU, making its presence "physically proven."

.. figure:: img/B01.png
  :width: 600
  :align: center 
  
  Example: On top of a podium SU01 there is a SU02 (in situ), fragmented due to a -SU03 (destruction of the upper part of the column). A USV/s 100 hypothetical reconstruction is provisioned in order to restore the action of destruction -SU03.


3.2 USV/n node:
~~~~~~~~~~~~~~~

.. image:: img/2D/USVn.png
  :width: 128px
  :align: left

Non-structural Virtual Stratigraphic Unit, a reconstruction hypothesis based on "sources" such as comparisons or general rules. It is not connected to a -SU and, as a result, is not "physically proven."

.. figure:: img/B02.png
  :width: 600
  :align: center 

  Example: There are only the remains of a podium SU01. A USV/n 100 hypothetical reconstruction is provisioned (without physical destruction signs that prove the presence of a column).

.. _usvseries:

3.3 USV series node:
~~~~~~~~~~~~~~~~~~~~

.. image:: img/2D/serUSV.png
  :width: 128px
  :align: left

A series of USVn objects, like a colonnade or a sequence of acroteria, considered as a whole. This seriation node acts as a proxy for the entire group.

.. figure:: img/B03.png
  :width: 600
  :align: center 

  Example: There are only the remains of a podium SU01. A USV/n 100 hypothetical reconstruction series of columns is provisioned (without physical destruction signs that prove the presence of a column). The series node allows to instance several USV/n at once.

.. figure:: img/B04.png
  :width: 400
  :align: center 

  Example: On top of a podium SU01 there is a column SU02 (in situ) fragmented due to a -SU03 (destruction of the upper part of the column). A USV/s 100 hypothetical reconstruction is provisioned in order to restore the destruction’s action -SU03. A series USV/n 101 is provided in order to complete the peristasis of the temple.


4. Special Finds and Virtual Special Finds (SF and VSF):
--------------------------------------------------------

These categories relate to anastylosis, where original architectural elements have been found *not in situ* and repositioned. When an element exists but its original position cannot be determined with absolute certainty (i.e. uncertain attribution to a given context or specific position), it is recorded as a Special Find (SF). When this element is repositioned in a hypothetical location based on archaeological interpretation rather than documentary evidence, its new position is recorded as a Virtual Special Find (VSF). This dual recording system allows archaeologists to track both the physical element and its interpretative repositioning separately.

.. _sfnodes:

4.1 Special Find node:
~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/2D/SF.png
  :width: 128px
  :align: left

Refers to a non-in situ element (fragmented or intact) that needs to be repositioned. It is a real object with several known properties (color, material, etc.) except for the original position.

.. figure:: img/B05.png
  :width: 400
  :align: center 

  Example: There are only the remains of a podium SU01 with a collapsed column SF01. A USV/n 100 hypothetical reconstruction is provisioned using the SF as a source. This kind of USV/n has a special status.

.. figure:: img/B06.png
  :width: 400
  :align: center 

  Example: There are only the remains of a podium SU01 with a collapsed column SF01 (special find 01). A USV/n 100 series hypothetical reconstruction of the colonnade is provisioned using the SF as a source.

4.2 Virtual Special Find node:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/2D/VSF.png
  :width: 128px
  :align: left

A Virtual Special Find (VSF) represents the restoration, integration, or completion of an original architectural element that has been repositioned through anastylosis (recorded as Special Find - SF). While the SF documents the anastylosis - the repositioning of an original found piece - the VSF records any additional restoration work, completion, or integration necessary to enhance the understanding or stability of that element.
Like other virtual stratigraphic units (VSU/s), a VSF inherits specific physical properties from its corresponding SF, such as material characteristics, certain dimensions, decorative features, and construction techniques. This inheritance of properties ensures that any restoration or completion work remains coherent with the original element's characteristics.
For example:

SF records a partially preserved original column capital that has been repositioned through anastylosis
VSF documents the restoration work performed to complete missing parts of that same capital, maintaining consistency with the original's dimensions, material properties, and stylistic features

This relationship between SF and VSF allows archaeologists to maintain a clear distinction between original repositioned elements (anastylosis - SF) and their subsequent restoration or completion work (VSF), while ensuring appropriate documentation of both the original fabric and conservation interventions.

Cumulative example of different USV nodes used together
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: img/B07.png
  :width: 600
  :align: center 
  
  USV/s and USV/n are used together. Different -SU allow to propose different USV/s.



