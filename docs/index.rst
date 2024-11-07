Extended Matrix documentation
=============================

**Extended Matrix** is a formal language with which to keep track of virtual reconstruction processes. It is intended to be used by archaeologists and heritage specialists to document in a robust way their scientific activities. The EM allows to record the sources used and the processes of analysis and synthesis that have led from scientific evidence to virtual reconstruction. It organises 3D archaeological record so that the 3D modelling steps are smoother, transparent and scientifically complete. Its development is leaded by E. Demetrescu at CNR-ISPC (Rome, former CNR-ITABC). EM is at its 1.4 version (a 1.5 version is currently under development).

Extended Matrix structure
-------------------------

.. _em_structure:

The diagram shows the essential structure of Extended Matrix through its core components.

.. image:: img/EM_schema.png
   :alt: Core components of Extended Matrix: Language, Framework and Knowledge Graph.
   :width: 200px
   :align: left
   *Core components of Extended Matrix: Language, Framework and Knowledge Graph.*

At the center, Extended Matrix connects three fundamental elements: the Extended Matrix Language, which provides the formal notation system; the Extended Matrix Framework, which includes all necessary software tools; and the Multidimensional Knowledge Graph, which serves as the underlying graph database structure. These components work together to provide a comprehensive system for archaeological data management and interpretation.

How can I start learning and using it ?
---------------------------------------

Bare in mind that learning and using EM depends on your scope and your background. 

1. You can just use EM to document your studies and your reconstruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

it is reccommended to learn at least the EM language that is explained in this manual.

2. If you want to connect your documentation to 3D models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

it is a good idea to learn also some of the tools from the Extended Matrix Framework (EMF), starting from the EMtools for Blender. You can find the documentation `here <https://docs.extendedmatrix.org/projects/EM-tools/en/latest/index.html>`_.

.. note::

   Tipically users can work in team splitting the effort between two or more members (i.e. one drawing the EM, one modelling in Blender). 

3. If you want to improve your 3D survey
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

namely the quality of 3D models, annotation of the survey process, etc.. consider to adopt the 3D Survey Collection suite (3DSC) for Blender and Metashape. You can find the documentation `here <https://docs.extendedmatrix.org/projects/3DSC/en/latest/>`_.

.. note::

   The access to high visual quality models (using even modest computers) like the ones that you can create with 3DSC are very important to be able to annotate stratigraphic documentation directly on 3D and connect it to your database.

Scope
-----

In a wider perspective and due to its abstract approach, the Extended Matrix can be used as a human readable metaphor to ingest and present liquid semantic data. In other words, the nodes that compone the paradata section can be used to track and annotate in a simple but effective way several data provenance path exceeding the traditional reconstruction process it was firstly applied to.

.. note::

   This documentation is related to a EM 1.5 development version: please pay attention that modifications may occur before releasing the final version.

.. toctree::
   :maxdepth: 2
   :caption: Set-up

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
