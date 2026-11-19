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

   This documentation covers **EM 1.5** (current stable version).

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

   * - `Start EM ↗ <https://www.extendedmatrix.org/start>`__
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

The **EM Ecosystem** is documented across several manuals, each kept beside
the code it describes. **EM** (this manual) is the formal language; **EMF** —
the EM Framework — is the family of tools that speak it. Every manual below
is published under ``docs.extendedmatrix.org``.

.. list-table::
   :widths: 26 16 58
   :header-rows: 1
   :class: em-manuals

   * - Manual
     - Open
     - What it answers
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
     - `Open ↗ <https://docs.extendedmatrix.org/projects/s3dgraphy/en/v1.5/>`__
     - Python library — the computational implementation of EM as a
       property knowledge graph (GraphML/JSON).
   * - **Heriverse**
     - `Open ↗ <https://docs.extendedmatrix.org/projects/heriverse/en/1.5/>`__
     - Heritage Science Metaverse — web-based publication and
       collaborative VR for EM-aware scenes.
   * - **EMStudio** *(from EM 1.6)*
     - `Open ↗ <https://docs.extendedmatrix.org/projects/emstudio-doc/en/1.6/>`__
       · `IT ↗ <https://docs.extendedmatrix.org/projects/emstudio-doc/it/1.6/>`__
     - The standalone editor, recommended for authoring from EM 1.6 onwards.
       It reads the graphs authored on this line and opens them in place.

The StratiGraph tools
=====================

`StratiGraph <https://stratigraph-eccch.eu>`__ is the Horizon Europe project
that builds the shared node around the Extended Matrix. Its manuals have an
address of their own, ``docs.stratigraph-eccch.eu``, and they cite this one
rather than repeating it.

.. list-table::
   :widths: 26 16 58
   :header-rows: 1
   :class: em-manuals

   * - Manual
     - Open
     - What it answers
   * - **The node, and its catalogue**
     - `Open ↗ <https://docs.stratigraph-eccch.eu/projects/node/en/latest/>`__
     - The place a team shares: rooms, studies, documents, who may see what,
       and the catalogue that publishes what a room decides to publish.
   * - **StratiField**
     - `Open ↗ <https://docs.stratigraph-eccch.eu/projects/field/en/latest/>`__
     - The field assistant: recording on site with no network, and the
       synchronisation with the node when there is one.
   * - **Recording templates**
     - `Open ↗ <https://docs.stratigraph-eccch.eu/projects/templates/en/v0.1.0/>`__
     - The sheets and the controlled vocabularies a team starts from.
   * - **StratiGraph Academy**
     - `Open ↗ <https://academy.stratigraph-eccch.eu>`__
     - Not a manual: where you learn the craft — the competence nodes and
       the five working phases of an investigation.

If you are unsure where to start: stay here if you have *evidence to
organise and a notation to learn*; open **EM-Tools** if you have *3D
content to annotate in Blender*; reach for **3DSC** if you have *raw
survey data to clean and align*; open **Heriverse** when your
reconstruction is *ready to be shared with the world*.

.. note::

   This documentation describes the EM 1.5 stable language. A 1.6 version
   is currently under development; minor adjustments to the notation may
   occur in future releases.

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
