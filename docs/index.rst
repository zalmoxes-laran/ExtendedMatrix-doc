Welcome to Extended Matrix documentation!
=========================================

**Extended Matrix** is a formal language with which to keep track of virtual reconstruction processes. It is intended to be used by archaeologists and heritage specialists to document in a robust way their scientific activities. The EM allows to record the sources used and the processes of analysis and synthesis that have led from scientific evidence to virtual reconstruction. It organises 3D archaeological record so that the 3D modelling steps are smoother, transparent and scientifically complete. It has been developed by E. Demetrescu at CNR-ISPC (Rome, former CNR-ITABC). EM is at its 1.4 version (a 1.5 version is currently under development).

In a wider perspective and due to its abstract approach, the Extended Matrix can be used as a human readable metaphor to ingest and present liquid semantic data. In other words, the nodes that compone the paradata section can be used to track and annotate in a simple but effective way several data provenance path exceeding the traditional reconstruction process it was firstly applied to.

.. admonition:: First time here?
   :class: tip

   If this is your very first contact with the Extended Matrix project,
   the recommended landing page is `extendedmatrix.org <https://www.extendedmatrix.org>`__
   — it explains *what* EM is, *who* it is for, and *which* of the
   manuals you should open next. This site you are reading now is the
   **language reference**: the place where the formal notation is
   defined and discussed.

EM, EM Tools, 3DSC, EMviq: who is who
-------------------------------------

A new user often meets several names at once. The distinction matters
because each one solves a different problem:

.. list-table::
   :header-rows: 1
   :widths: 22 38 40

   * - Name
     - What it is
     - Where to learn it
   * - **Extended Matrix (EM)**
     - The *formal language* used to document stratigraphy and
       reconstruction processes. Drawn in yEd or produced from
       ``em_data.xlsx``.
     - You are here.
   * - **EM Tools**
     - The *Blender add-on* that connects an EM graph to 3D content.
     - `EM Tools manual <https://docs.extendedmatrix.org/projects/EM-tools/>`__
   * - **3DSC**
     - A complementary Blender environment for high-quality 3D survey
       processing that can feed EM Tools.
     - `3D-survey-collection docs <https://docs.extendedmatrix.org/projects/3D-survey-collection>`__
   * - **EMviq**
     - The *web visualisation* component of the 1.4 framework — the
       browser-side viewer for EM-aware 3D scenes.
     - `EMviq pages on EM <https://www.extendedmatrix.org/em-framework/emviq>`__

If you are unsure which one you need: stay here if you have *evidence
to organise and a notation to learn*; switch to the EM Tools manual if
you have *3D content to annotate in Blender*; reach for 3DSC if you
have *raw survey data to clean and align*; open EMviq when your
reconstruction is ready to be shared on the web.

.. tip::

   New to EM? Start with :doc:`usage` for installation and the broad
   workflow, then walk through :doc:`nodes_intro`, :doc:`stratigraphic_nodes`
   and :doc:`properties` — these three pages cover ~80% of the
   day-to-day vocabulary in 1.4.

Check out the :doc:`usage` section for further information, including how to :ref:`installation` the project.
For the description of the nodes, see :doc:`nodes_intro`
For the properties, see :ref:`properties`

.. note::

   This documentation is related to the EM 1.4 release line. For the
   in-development 1.5 line — including TSU, Landscape mode and the
   standalone s3dgraphy library — switch to the
   `1.5 development docs <https://docs.extendedmatrix.org/en/1.5.0dev/>`__.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   nodes_intro
   stratigraphic_nodes
   stratigraphic_approach
   validation_nodes
   properties

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
