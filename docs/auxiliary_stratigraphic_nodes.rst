Auxiliary Stratigraphic nodes
=============================

Auxiliary Stratigraphic Nodes help us better understand how layers of earth and remains form and change over time. These units don't exist alone – they're always connected to main stratigraphic units and provide extra information about how the layers developed.

.. _continuity_node:

Continuity Node
---------------

One aspect that remained inadequately addressed in the Matrix for many years was the method of expressing the lifespan of a stratigraphic unit—specifically, the duration between its creation and its destruction. Although various hypotheses and proposals have been put forward, the literature lacked a solution that was coherent with the Matrix's graph-based structure.

.. image:: img/2D/continuity.png
   :width: 128px
   :align: left

In the Extended Matrix (EM), this temporal continuity is expressed through a continuity node (represented by a black diamond), which marks the end of a stratigraphic unit's life cycle. For example, when a wall collapses and is removed from the site, when wooden beams disappeared due to a fire or even during an excavation when a structure is destroyed (after it is fully documented). The beginning of the unit's life is marked by the stratigraphic unit itself.


This approach provides several advantages:

1. **Graph Consistency**: The continuity node maintains the graph-based nature of the Matrix while adding temporal depth
2. **Clear Temporal Boundaries**: It explicitly marks both the beginning (the stratigraphic unit) and end (the continuity node) of a unit's existence
3. **Relationship Integration**: The node can participate in the stratigraphic sequence, allowing clear representation of how one unit's end relates to other units' beginnings or endings
4. **Documentation Precision**: It enables precise documentation of when a unit ceased to function in its original capacity

The introduction of the continuity node resolves a long-standing limitation in stratigraphic documentation, providing a formal way to represent not just the creation of stratigraphic units but their complete lifecycle within the archaeological record.

Real vs virtual units: asymmetric semantics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The effect of a continuity node **depends on the type of unit it is attached to**. The EM treats real and virtual units asymmetrically, because they carry a different epistemic status.

**Attached to a real stratigraphic unit** (US, USM, USR, SU, SE …):
   The continuity node **declares the end of life** of the unit. Without a continuity node, a real unit is assumed to **persist** from its epoch of creation **until the end of the recorded periods** — physical evidence is taken as surviving unless proven otherwise. Adding a continuity node terminates that persistence at the epoch the continuity node belongs to.

   *Example*: a wall (SU05) is built in Epoch 2. With no continuity node it is considered still standing in Epochs 3, 4 and 5 as well. If a continuity node is attached to SU05 and placed in Epoch 4, the wall is treated as no longer present from Epoch 5 onward.

**Attached to a virtual stratigraphic unit** (USV/s, USV/n, SF, VSF and their series/group variants):
   The continuity node **extends the life** of the virtual unit. By default, a virtual unit exists only in the epoch where it is declared — because it represents a reconstruction hypothesis anchored to a single temporal slice. Attaching one or more continuity nodes artificially extends that hypothesis into additional epochs.

   *Example*: a hypothetical column (USV/n 100) is declared in Epoch 2. Without any continuity node it is visible only in Epoch 2. Attaching continuity nodes in Epochs 3 and 4 extends the reconstruction so that the column is also considered present in those epochs.

The continuity node is therefore the single mechanism that inverts the default temporal semantics depending on the realness of the unit:

- **real unit** → default = alive until the end; continuity node **ends** it.
- **virtual unit** → default = alive only in one epoch; continuity node **extends** it.

This asymmetry reflects the epistemic status of the two categories: physical evidence is assumed to survive until proven otherwise, while reconstructions are taken as local hypotheses unless explicitly propagated.

