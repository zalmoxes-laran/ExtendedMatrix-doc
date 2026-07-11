Location
========

.. _location:

A *location* expresses the **set-theoretic membership** of a node in a
named spatial entity. It answers the question *"what (named) place is
this in?"*. It is one of the three orthogonal grouping axes of the
Extended Matrix:

- *when* the node belongs in time          → :doc:`stratigraphic_nodes` epoch / swimlane
- *with what intention* it was made        → :doc:`activity`
- **what (named) place it is in**          → this page

A node may carry membership on all three axes at once and they do not
interfere with each other.

.. note::

   The Location concept has been formalised at the s3dgraphy /
   datamodel level in v0.1.41 (originating discussion:
   `s3dgraphy issue #5
   <https://github.com/zalmoxes-laran/s3Dgraphy/issues/5>`_, raised
   from the pyArchInit integration). It is the first concept in this
   manual to follow the unified concept-first template (overview · em
   graph · s3d graph · em_data · CIDOC mapping · examples). Future
   pages — Property, Document, Author, License, Activity (refactor) —
   will adopt the same structure.


Overview
--------

Three **kinds** of location coexist on the same axis:

- **Toponym** — *external / administrative* identity. Pompei, Lazio,
  Italia, Latium et Campania. The names a place would carry on a
  political map or on a postal address. Stable across studies, owned
  by the wider world.
- **Study** — *operational / procedural* identity. Saggio 4, settore
  A2, quadrato 12, sondage NW. The names a place carries inside the
  excavation methodology of one specific project; another project
  on the same physical site would use different names.
- **Functional** — *interpretive / semantic* identity. Basilica, room
  A, courtyard, kiln. The names a place carries inside the
  reconstructive narrative — they describe what the place is *for*,
  not where it is on a map nor how the dig was organised.

The three are distinct, not redundant. The same physical wall can
simultaneously be in *toponym* ``Pompei``, in *study* ``Saggio4/A2``,
and in *functional* ``Casa del Fauno / Room 12``. None of those three
descriptions can be derived from the others.

Two structural properties follow from this design:

- **Membership is m:n.** A wall between two rooms belongs to *both*
  rooms — and it is the wall, not the wall's relation to one of the
  rooms, that is the data. Multiple memberships per node are
  first-class.
- **Locations are hierarchical.** A location can itself be inside
  another location: ``Pompei`` ⊃ ``Sector 4`` ⊃ ``Casa del Fauno`` ⊃
  ``Room 12``. The hierarchy is recursive (a location ``is_in_location``
  of another location) and is independent on each *kind* axis (the
  toponym tree and the functional tree are separate trees).

Propagation along the Location axis is **additive**: when a node has
multiple memberships, all of them apply, none of them overrides.
This is the opposite default from time (``EpochNode`` propagation is
substitutive: the finest-grained epoch wins). The asymmetry is
intentional and matches archaeological practice.

A location is **identitary, not geometric**. A coordinate, an EPSG
code, a shift vector — those belong to a :doc:`source_node`-side
``GeoPositionNode`` (the *georef* node), not to a ``Location``. The
two concepts are linked, but they are not the same thing: see *CIDOC
mapping* below.


Representation in em graph
--------------------------

In yEd notation, a ``LocationNodeGroup`` renders as a **dashed
round-rectangle group folder**, fill ``#F5F5F5``, label at top.
Border colour varies by kind: toponym ``#888888``, study ``#3A5A8C``,
functional ``#000000``.

For a node with **multiple memberships**, em graph picks exactly one
to render as a yEd group folder — the one carrying ``is_primary=true``
on its ``is_in_location`` edge. The remaining memberships render as
labels / badges on the node, not as overlapping group folders. This is
a yEd limitation (group folders cannot stack), not a property of the
formalism: in the underlying s3d graph all memberships are first-class
and equal. Choosing which membership is primary is therefore a
*rendering* decision, not an *epistemic* one — typically the
functional location is the most informative one for a reader of the
diagram, but the choice is per-node.

The hierarchy is rendered the same way the Location *itself* would be:
nested group folders, with the parent location wrapping the child
ones. So in em graph a ``Casa del Fauno`` group folder appears inside
a ``Sector 4`` group folder, which appears inside a ``Pompei`` group
folder.


Representation in s3d graph
---------------------------

Class: ``LocationNodeGroup`` (subclass of ``GroupNode``). See the
`s3dgraphy reference
<https://github.com/zalmoxes-laran/s3Dgraphy>`_ for the full Python
API.

- **Required field** ``kind`` ∈ ``{"toponym", "study", "functional"}``.
  Construction with any other value raises ``ValueError``.
- **Field** ``propagation`` defaulting to ``"additive"``. Declared so
  that future engines can opt into substitutive composition per
  instance, even though the canonical Location behaviour is additive.
- **Edge** ``is_in_location`` (canonical) / ``includes_location``
  (reverse). Source node types: ``StratigraphicNode``,
  ``ParadataNode``, ``ParadataNodeGroup``, ``DocumentNode``,
  ``ExtractorNode``, ``CombinerNode``, ``PropertyNode``, and
  ``LocationNodeGroup`` itself (for the recursive hierarchy). Target:
  always ``LocationNodeGroup``.
- **Edge attribute** ``is_primary: bool`` (default ``false``).
  At most one ``is_primary=true`` edge per source. Carries the
  rendering hint described above.
- Multiple ``is_in_location`` edges per source are first-class —
  this is how m:n membership is encoded.

Construction example:

.. code-block:: python

   from s3dgraphy.nodes import LocationNodeGroup
   from s3dgraphy.edges import Edge

   pompei = LocationNodeGroup("loc_pompei", "Pompei", kind="toponym")
   sect4  = LocationNodeGroup("loc_sect4",  "Sector 4", kind="study")
   fauno  = LocationNodeGroup("loc_fauno",  "Casa del Fauno", kind="functional")
   room12 = LocationNodeGroup("loc_room12", "Room 12", kind="functional")

   # Hierarchy (recursive Location → Location)
   Edge("eh1", sect4.node_id,  pompei.node_id, "is_in_location")
   Edge("eh2", fauno.node_id,  sect4.node_id,  "is_in_location")
   Edge("eh3", room12.node_id, fauno.node_id,  "is_in_location")

   # m:n membership of a wall between two rooms
   e_primary = Edge("ew1", "wall_77", room12.node_id, "is_in_location")
   e_primary.attributes["is_primary"] = True
   e_secondary = Edge("ew2", "wall_77", "loc_room13", "is_in_location")
   e_secondary.attributes["is_primary"] = False


Representation in em_data
-------------------------

In the ``em_data.xlsx`` workbook, the Location concept is a single
column on the ``Units`` sheet, by convention named
``location_paths``. The column is multi-valued and uses two of the
three workbook-wide conventions documented in :doc:`em_data`:
**multi-valued cells** (separator ``;``), **hierarchical paths**
(separator ``/``), and **kind prefixes** (``topo:``, ``study:``,
``func:``).

A typical cell:

.. code-block:: text

   func:Pompei/Sector_4/Casa_del_Fauno/Room_12; topo:Pompei; study:Saggio4/A2

The first value is treated as **primary** unless overridden — its
``is_in_location`` edge will carry ``is_primary=true`` in the s3d
graph and, in em graph, will become the yEd group folder.

Round-trip rules:

- A cell with one value produces one ``is_in_location`` edge.
- A cell with several values produces several edges (m:n
  membership).
- A hierarchical path ``A/B/C`` produces three nested
  ``LocationNodeGroup`` nodes (``A``, ``B``, ``C``) connected by
  two recursive ``is_in_location`` edges (``B → A``, ``C → B``),
  and the source node's ``is_in_location`` edge attaches to the
  leaf (``C``).
- Three top-level prefixes (``topo:``, ``study:``, ``func:``) each
  produce a separate hierarchy tree; the trees are not merged.

When the AI extractor (StratiMiner) populates ``location_paths``
from a PDF or set of field notes, it follows the same conventions —
see :doc:`knowledge_tree` and :doc:`em_data` for how the workbook is
the AI extraction's primary output.


Naming conventions
~~~~~~~~~~~~~~~~~~

The field ``kind`` (Python instance attribute and JSON datamodel field) is the
canonical name for **single-axis sub-discrimination** on s3dgraphy nodes from
v0.1.41 onward. It deliberately avoids ``type``, which is structurally reserved
for class identity (``node_type``, registered in ``Node.node_type_map``) and
saturated in CIDOC mapping (``rdf:type``, ``P2_has_type``).

For **multi-axis classification** (e.g. ``DocumentNode.role`` /
``content_nature`` / ``geometry``) each axis keeps its own semantically named
field. ``kind`` is reserved for single-axis cases like ``LocationNodeGroup``.


CIDOC-CRM mapping
-----------------

The Extended Matrix Location concept maps cleanly onto CIDOC-CRM
core, with one CIDOC-CRM-native composition for the *kind* axis and
one genuinely new RDF property for the *is_primary* rendering hint.

.. list-table::
   :header-rows: 1
   :widths: 35 35 30

   * - s3dgraphy / em concept
     - CIDOC mapping
     - Notes
   * - ``LocationNodeGroup`` (the node itself)
     - **E53 Place**
     - Vanilla CIDOC core. CRMarchaeo does not introduce a Place-level
       container distinct from E53, so plain E53 is preferred.
   * - ``kind ∈ {toponym, study, functional}``
     - ``E53 Place`` ── **P2_has_type** ──▷ ``E55 Type``
     - The three values are reserved E55 Type *instances*:
       ``s3d:KindToponym``, ``s3d:KindStudy``, ``s3d:KindFunctional``.
       CIDOC-native composition; no new property URI is introduced.
   * - ``is_in_location`` (Stratigraphic / Paradata → Location)
     - **P53_has_former_or_current_location**
     - Vanilla CIDOC core.
   * - ``is_in_location`` (Location → Location, recursion)
     - **P89_falls_within**
     - Vanilla CIDOC core. Same edge name in s3dgraphy, two CIDOC
       predicates depending on the endpoints; the JSON datamodel
       declares both via the ``context_mapping`` block of the edge.
   * - ``is_primary`` (edge attribute)
     - ``s3d:isPrimary`` *(proposed)*
     - No CIDOC-core or CRMarchaeo equivalent. This is a UX /
       rendering disambiguation flag (which membership is the yEd
       group folder), legitimately new.
   * - ``propagation`` (node field)
     - *(none)*
     - Schema-level metadata (a rule about how the engine composes
       memberships), not instance data. Not serialised to triples.

The relationship with the *georef* node is expressed at the CIDOC
level via **P161_has_spatial_projection** linking the ``E53 Place``
(a Location) to an ``E94 Space Primitive`` (a georef geometry — see
the dedicated geometry node page when it lands). Location is the
*identity*; georef is the *geometry*. They are different nodes,
linked by P161, and they remain separated end-to-end through the
em graph, the s3d graph, and the triplestore.

.. admonition:: Stability of the ``s3d:`` namespace
   :class: warning

   The identifiers in the ``s3d:`` namespace introduced for the
   Location concept (``s3d:KindToponym``, ``s3d:KindStudy``,
   ``s3d:KindFunctional``, ``s3d:isPrimary``) are *candidate
   primitives* for the forthcoming **CRMem extension** (formerly
   referred to as *CIDOC-S3D*; in the spirit of CRMarchaeo / CRMsci /
   CRMinf — an extension of the CIDOC-CRM dedicated to the concepts
   of the Extended Matrix that CIDOC-core does not cover; the
   ``em:`` namespace of ``em.ttl`` is its current formal draft).
   Their stability level is
   ``proposed``: consumers should expect potential URI rename when
   the extension is formalised. The s3dgraphy JSON datamodel
   carries ``extension_status: "proposed"`` on every such URI as a
   machine-readable marker.


Examples
--------

Single membership
~~~~~~~~~~~~~~~~~

A floor that belongs to one room. ``Units`` row for the floor:

.. code-block:: text

   ID:        US3471
   TYPE:      US
   ...
   location_paths:  func:Pompei/Sector_4/Casa_del_Fauno/Room_12

Resulting s3d graph fragment: four ``LocationNodeGroup`` nodes (one
per path level, all kind=functional), three recursive
``is_in_location`` edges connecting them, and one
``is_in_location`` edge from ``US3471`` to the leaf
``LocationNodeGroup`` (``Room_12``). The latter carries
``is_primary=true``.

m:n membership
~~~~~~~~~~~~~~

A wall between two rooms. The wall belongs to both rooms;
the diagram-author's choice is to render the *south* room as the
primary group folder.

.. code-block:: text

   ID:        USM77
   TYPE:      USM
   ...
   location_paths:  func:.../Room_12; func:.../Room_13

Resulting s3d graph: two ``is_in_location`` edges from ``USM77``,
the first with ``is_primary=true``, the second with
``is_primary=false`` (or the attribute simply absent — the default
is ``false``). In em graph, ``USM77`` lives inside the ``Room_12``
group folder; a small badge / label on the node records the
secondary membership in ``Room_13``.

Hierarchy across kinds
~~~~~~~~~~~~~~~~~~~~~~

The same wall as above, with all three kinds expressed:

.. code-block:: text

   location_paths:  func:Pompei/Sector_4/Casa_del_Fauno/Room_12; func:Pompei/Sector_4/Casa_del_Fauno/Room_13; topo:Pompei; study:Saggio4/A2

Resulting s3d graph: the two functional memberships from the
previous example, plus two more ``is_in_location`` edges to a
toponym leaf (``Pompei``) and a study leaf (``A2``, inside
``Saggio4``). The CIDOC triplestore that retrieves this fragment
sees a single E53 Place per leaf, classified by the appropriate
E55 Type instance, and the wall (an A-stratigraphic-unit) bound
to all four leaves via P53.


.. seealso::

   - :doc:`em_data` — workbook-wide conventions referenced above.
   - :doc:`activity` — the orthogonal grouping axis (intention).
   - :doc:`stratigraphic_nodes`, :doc:`auxiliary_stratigraphic_nodes`
     — the source side of the membership.
   - `s3dgraphy issue #5
     <https://github.com/zalmoxes-laran/s3Dgraphy/issues/5>`_ — the
     originating discussion (PyArchInit integration, by
     `@enzococca <https://github.com/enzococca>`_).
