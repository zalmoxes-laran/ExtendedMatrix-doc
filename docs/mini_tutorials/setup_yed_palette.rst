Set up the yEd palette
======================

Before you can draw an Extended Matrix in yEd, you need to install the
EM palette so the canonical node shapes are available in the canvas.
This setup is a one-off operation per yEd installation.

Prerequisites
-------------

- `yEd Graph Editor <https://www.yworks.com/products/yed>`_ installed on
  your machine (free for personal and academic use).
- The Extended Matrix palette template (``.graphml`` file), distributed
  as a zip archive — see :doc:`/em_workspace_preparation` for download
  links to the canonical EM workspace materials.

Steps
-----

1. **Download the palette zip** from the canonical EM workspace
   distribution. Unzip it on your file system. **Do not open the
   ``.graphml`` file directly** — it is a template to be imported into yEd,
   not a graph to be edited.

2. **Open yEd Graph Editor.** A blank canvas appears.

3. From the menu bar, choose **Edit → Manage Palette…**.

4. In the Manage Palette dialog, click **Import…** (lower-left area
   depending on yEd version).

5. **Select the EM palette ``.graphml`` template** you unzipped in step 1.
   Click Open.

6. The palette appears in the **right-hand column** of active templates
   in the Manage Palette dialog, labelled **Extended Matrix palette**.
   Make sure it is enabled (checked).

7. Close the Manage Palette dialog. Back on the canvas, the palette
   panel on the right side of yEd now shows **Extended Matrix palette**
   as the last entry. All EM node types (US, USV, USD, SF, RSF, …) are
   available from here — drag them onto the canvas to start authoring
   your matrix.

.. figure:: /_static/mini_tutorials/yed_manage_palette_open.png
   :alt: Manage Palette dialog in yEd, with Extended Matrix palette imported
   :align: center
   :width: 90%

   The yEd Manage Palette dialog after importing the Extended Matrix
   template. The palette appears in the right-hand column of active
   palettes.

Next steps
----------

With the palette in place, head to :doc:`/draw_the_matrix` to start
authoring your stratigraphic graph.

.. seealso::

   - :doc:`/em_workspace_preparation` — the broader scene setup
     (folder structure, DosCO, source register)
   - :doc:`/draw_the_matrix` — using the palette in practice
