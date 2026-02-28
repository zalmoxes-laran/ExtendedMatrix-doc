
Learn EM
========

Bare in mind that the path to learn and use EM depends on your scope and your background. 

1. EM formal language (for smart humanists)
-------------------------------------------

Provides an overview of the EM language, a formal graphical notation used to describe stratigraphy and archaeological contexts. This documentation recommends learning the EM language, which can be studied using simple materials such as pencil and paper. The relevant sections of this documentation explain the basics of EM, emphasizing that it is not a programming language but a specialized tool for representing archaeological studies and reconstructions.

.. tip::

   The reference repository, which contains example cards, node icons, templates and other useful material, is available at https://github.com/zalmoxes-laran/ExtendedMatrix/tree/EM_1.5_dev/

2. Annotate stratigraphy on 3D models (for jedi-humanists)
------------------------------------------------------------------------------------------------

If you want to connect your documentation to 3D models, it is a good idea to learn also some of the tools from the Extended Matrix Framework (EMF), starting from the EMtools for Blender. `You can find the documentation here <https://docs.extendedmatrix.org/projects/EM-tools/en/latest/index.html>`_.

.. note::

   Tipically users can work in team splitting the effort between two or more members (i.e. one drawing the EM, one modelling in Blender). 

3. Prepare high-quality 3D models for EM workflows (not for the faint of heart!)
--------------------------------------------------

To enhance your 3D survey quality, including model accuracy, survey process documentation, and metadata management, consider adopting the 3D Survey Collection suite (3DSC). This toolset integrates with Blender and Metashape (Reality Capture in progress), providing a comprehensive workflow for archaeological 3D documentation. `The complete documentation is available here <https://docs.extendedmatrix.org/projects/3DSC/en/latest/>`_.

.. note::

   High-quality 3D models, accessible even on modest computers through tools like 3DSC, are essential for effective stratigraphic documentation. These models enable direct 3D annotation and seamless connection to your database.

4. If you want to customize EM for your workflow (join the bright side of the force!)
-------------------------------------------------------------------------------------

Contributing to add features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to contribute to add new features to EM:

* **For EMtools in Blender**: you can start learning Python for Blender `here <https://www.youtube.com/watch?v=rKGNc6CQ2cg>`_ (in Italian, with English subtitles) and ask for support from the EM community on `Facebook <https://www.facebook.com/groups/extendedmatrix>`_ or `Telegram <https://t.me/UserGroupEM>`_.

* **To contribute to s3dgraphy**: consult the `Contributing Guidelines <https://github.com/zalmoxes-laran/s3dgraphy/blob/main/CONTRIBUTING.md>`_ on the GitHub repository.

Porting EM to other platforms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To port Extended Matrix to other platforms like **Revit**, **3D Studio Max**, **Unity**, or **Unreal Engine**, we recommend using the **s3dgraphy** Python library.

**What is s3dgraphy?**

s3dgraphy is the core Python library that implements the Extended Matrix formal language. It has been extracted from EM-tools to become a standalone library, enabling EM functionality to be brought to any platform that supports Python.

**Key features:**

* 🔗 **Graph-based architecture**: Native support for complex archaeological relationships
* 📊 **Stratigraphic modeling**: Specialized node types for archaeological units
* 🔄 **Format interoperability**: Import/export GraphML, JSON, and archaeological standard formats
* 🏛️ **Archaeological standards**: Built-in support for CIDOC-CRM mapping
* ⚡ **Extensible design**: Easy to extend with custom node types and relationship definitions

**Getting started:**

1. **Installation**

   .. code-block:: bash

      pip install s3dgraphy

2. **Basic usage example**

   .. code-block:: python

      from s3dgraphy import Graph
      from s3dgraphy.nodes import StratigraphicNode, DocumentNode
      
      # Create a new graph
      graph = Graph("my_site")
      
      # Add a stratigraphic unit
      us001 = StratigraphicNode("US001", node_type="US")
      us001.set_attribute("description", "Stone wall foundation")
      graph.add_node(us001)
      
      # Add documentation
      doc001 = DocumentNode("DOC001", "site_plan.pdf")
      graph.add_node(doc001)
      
      # Create relationship
      graph.add_edge(us001.node_id, doc001.node_id, "documented_by")
      
      # Export to GraphML
      graph.export_graphml("my_site.graphml")

3. **Integration with your platform**

   To integrate s3dgraphy into your application:
   
   * Use s3dgraphy APIs to create and manage EM graphs
   * Implement the visual interface specific to your platform
   * Use supported export/import formats (GraphML, JSON) for interoperability

**Available resources:**

* 📖 **Complete documentation**: `s3dgraphy Documentation <https://docs.extendedmatrix.org/projects/s3dgraphy/>`_ *(coming soon)*
* 💻 **GitHub Repository**: https://github.com/zalmoxes-laran/s3dgraphy
* 🐛 **Issue Tracker**: https://github.com/zalmoxes-laran/s3dgraphy/issues
* 📧 **Developer contact**: emanuel.demetrescu@cnr.it

**Extended Matrix Ecosystem:**

s3dgraphy is part of the broader Extended Matrix Framework ecosystem:

* **EM-tools for Blender** - 3D visualization and annotation
* **3D Survey Collection (3DSC)** - High-quality 3D model preparation
* **ATON 3 Framework** - Web-based archaeological visualization
* **Heriverse Platform** - Virtual heritage experiences

.. note::

   s3dgraphy is currently under active development. Version 1.0 is planned for Q4 2025 with complete features for multi-platform integration. For the current development status, consult the `roadmap <https://github.com/zalmoxes-laran/s3dgraphy/blob/main/ROADMAP.md>`_.

.. tip::

   For integration examples and complete workflows, consult the `Examples & Workflows <https://docs.extendedmatrix.org/projects/s3dgraphy/examples/>`_ section in the s3dgraphy documentation.
