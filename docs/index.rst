=========================================
Extended Matrix Ecosystem — Documentation
=========================================

.. note::

   You are reading the **manual of the Extended Matrix (EM)** — the formal
   language at the heart of the **EM Ecosystem**. The Ecosystem is the
   umbrella that groups two layers: **EM** (this manual — the formal
   language) and the **EM Framework (EMF)** — the family of tools that
   speak EM. For an overview of the project, the tools that build on EM
   and the latest news, the reference site is
   `extendedmatrix.org <https://www.extendedmatrix.org>`__.

   This documentation covers **EM 1.6** — currently under active
   development. For the current stable language reference, see the
   `EM 1.5 manual <https://docs.extendedmatrix.org/en/1.5/>`__.

**Extended Matrix** is a formal language used to document stratigraphy and
virtual reconstruction processes. It is intended for archaeologists and
heritage specialists who need to keep track, in a robust and verifiable way,
of the sources, analyses and interpretive steps that lead from scientific
evidence to a reconstruction. Development is led by E. Demetrescu at
CNR-ISPC (Rome, former CNR-ITABC).

Quick start
===========

.. list-table::
   :widths: 30 70
   :header-rows: 0
   :class: longtable

   * - `Start ↗ <https://www.extendedmatrix.org/start>`__
     - First contact with Extended Matrix — what it is, who it is for and
       why it matters.
   * - `Choose your Path ↗ <https://www.extendedmatrix.org/find-your-path>`__
     - Guided picker on the project website to find the right entry point
       for your role and project.
   * - :doc:`learn_EM`
     - The guided tour through this manual — calibrated for humanists,
       archaeologists, 3D modellers and developers.

Documentation across the EM Ecosystem
=====================================

The **EM Ecosystem** is documented across several manuals, each focused on
a specific layer. **EM** (this manual) is the formal language; **EMF** —
the EM Framework — is the family of tools that speak it. The table below
shows where to go for what.

.. list-table::
   :widths: 25 15 60
   :header-rows: 1
   :class: longtable

   * - Manual
     - Open
     - Focus
   * - **Extended Matrix** *(this manual)*
     - *you are here*
     - The formal language: stratigraphic nodes, paradata, sources,
       connectors, epochs, qualia.
   * - **EM-Tools**
     - `Open ↗ <https://docs.extendedmatrix.org/projects/EM-tools/en/1.5/>`__
     - Blender add-on that connects an EM graph to 3D content for
       reconstruction work.
   * - **3DSC**
     - `Open ↗ <https://docs.extendedmatrix.org/projects/3DSC/en/latest/>`__
     - Blender environment for high-quality 3D survey processing that
       feeds EM-Tools.
   * - **s3dgraphy**
     - `Open ↗ <https://docs.extendedmatrix.org/projects/s3dgraphy/en/latest/>`__
     - Python library — the computational implementation of EM as a
       property knowledge graph (GraphML/JSON).
   * - **Heriverse**
     - `Open ↗ <https://docs.extendedmatrix.org/projects/heriverse/en/1.5/>`__
     - Heritage Science Metaverse — web-based publication and
       collaborative VR for EM-aware scenes.

If you are unsure where to start: stay here if you have *evidence to
organise and a notation to learn*; open **EM-Tools** if you have *3D
content to annotate in Blender*; reach for **3DSC** if you have *raw
survey data to clean and align*; open **Heriverse** when your
reconstruction is *ready to be shared with the world*.

.. note::

   This documentation describes the **EM 1.6 development version**: the
   notation may still receive minor adjustments before the final release.
   For the current stable language reference, see the EM 1.5 manual.

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: How to start

   learn_EM
   em_workspace_preparation
   usage
   draw_the_matrix
   project_organization

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Formal Language

   canvas
   nodes_intro
   stratigraphic_nodes
   auxiliary_stratigraphic_nodes
   activity
   location
   paradata_nodes
   qualia
   source_node
   extractor_nodes
   paradata_group
   connectors
   alternate_hypotheses
   data_funnel
   utils

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Data layer

   em_data

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Theoretical Aspects

   stratigraphic_approach
   knowledge_tree

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Mini tutorials

   mini_tutorials/index

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Cookbook

   cookbook/index

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Ecosystem

   ecosystem

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Reference

   glossary
   references
