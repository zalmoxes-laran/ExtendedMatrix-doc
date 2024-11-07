Extended Matrix documentation
=============================

**Extended Matrix** is a formal language with which to keep track of virtual reconstruction processes. It is intended to be used by archaeologists and heritage specialists to document in a robust way their scientific activities. The EM allows to record the sources used and the processes of analysis and synthesis that have led from scientific evidence to virtual reconstruction. It organises 3D archaeological record so that the 3D modelling steps are smoother, transparent and scientifically complete. Its development is leaded by E. Demetrescu at CNR-ISPC (Rome, former CNR-ITABC). EM is at its 1.4 version (a 1.5 version is currently under development).

Extended Matrix structure
-------------------------

The diagram shows the essential structure of Extended Matrix through its core components.

.. image:: img/EM_schema_general.png
  :width: 300px
  :align: left


.. image:: img/2D/US.png
  :width: 128px
  :align: left

*Core components of Extended Matrix: Language, Framework and Knowledge Graph.*

At the center, the s3Dgraphy Extended Matrix connects three fundamental elements: the Extended Matrix Language, which provides the formal notation system; the Extended Matrix Framework, which includes all necessary software tools; and the Multidimensional Knowledge Graph, which serves as the underlying graph database structure. These components work together to provide a comprehensive system for archaeological data management and interpretation.

.. note::

   This documentation is related to a EM 1.5 development version: please pay attention that modifications may occur before releasing the final version.

.. toctree::
   :maxdepth: 2
   :caption: How to start

   learn_EM
   usage

.. toctree::
   :maxdepth: 2
   :caption: Formal Language

   canvas
   nodes_intro
   stratigraphic_nodes
   activity
   validation_nodes
   properties
   paradata_group
   alternate_hypotheses
   utils

.. toctree::
   :maxdepth: 2
   :caption: Theoretical Aspects:

   stratigraphic_approach
