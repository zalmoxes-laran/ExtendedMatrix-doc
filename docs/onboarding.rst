Onboarding
==========

.. _emonboarding:

.. note::

   This section is new in EM 1.6 and **will grow**: worked examples, a
   mapping walkthrough and the first community profiles will be added as
   they arrive. It rests on two specifications, which are the reference
   when this page and they disagree:
   `em.json — the Extended Matrix document format
   <https://w3id.org/extendedmatrix/spec/em-json/>`__ (version 1.1) and
   `EM Profiles
   <https://github.com/ExtendedMatrix/vocabularies/blob/main/profiles/SPEC.md>`__
   (version 0.1, Editor's Draft; the name is provisional).

Extended Matrix is one formal language, but the communities that use it are
many: each records its own qualities, reads its sources in its own ways and
produces documents that only it produces. This page is for a community — a
discipline, a research group, the developers of a recording tool — that wants
to bring its data into EM without bending them and without splitting the
language. It says what such a community can bring, how it declares it, how it
writes its data, and how what it brings is kept and versioned.

What a community can bring
--------------------------

The package a community brings is called a **profile**. It may contain:

* **Qualia vocabularies** — the controlled values of the qualities it records
  (:doc:`qualia`), as small SKOS vocabularies.
* **Kinds of extractor** — the ways it reads its sources (:doc:`extractor_nodes`),
  with the formats each one reads and the qualia it yields.
* **Kinds of document** — the documents peculiar to it (:doc:`source_node`),
  with their formats.
* **Node and edge types of its own**, when the core does not name something it
  needs. Each new node type is a **species of a core type** — a kind of
  stratigraphic unit, of document, of extractor, of property — and each new
  edge declares its **family** (stratigraphic, relative chronology, epochs,
  paradata, other) and whether it takes part in the **propagation** of
  information. Normally it does not: a new edge that changed what the core
  derives about time would change the language, not extend it.
* **Glyphs and visual rules** for its types, in the same format as the core's:
  how they are drawn in the Graph view and, where it makes sense, in the
  Matrix, and in which lane.
* **Plugins** — tools that view or interpret its media, declared as pointers
  to where they are published, in the form of the EM connector architecture.

Two rules keep the language one. Every new type is the species of a core
type, so the core algorithms keep working on data that uses it. And there is
always a **fallback**: a tool that does not have the profile draws a new node
with the glyph of the core type it specialises, and keeps it, with all its
data, when it writes the file back.

How to write a profile
----------------------

A profile is a folder in the public repository
`ExtendedMatrix/vocabularies <https://github.com/ExtendedMatrix/vocabularies>`__,
``profiles/<name>/``, with a manifest, ``profile.json``. The manifest gives
the profile an identity (an IRI), a short **prefix**, a version, a lifecycle
state (proposed, stable, deprecated), curators and a licence, and then lists
what the profile brings. The types a profile introduces are written with its
prefix, so that they never collide with a core type:

.. code-block:: json

   {
     "name": "example-toolmarks",
     "prefix": "tm",
     "version": "0.1.0",
     "node_types": [{
       "type": "tm:mark_field",
       "label": {"en": "Field of tool marks"},
       "specializes": "UL",
       "mapping": {"iri": "http://www.cidoc-crm.org/cidoc-crm/E25_Human-Made_Feature"}
     }],
     "edge_types": [{
       "type": "tm:same_tool_as",
       "label": {"en": "Same tool as"},
       "family": "other",
       "propagates": false,
       "allowed_connections": [{"source": "tm:mark_field", "target": "tm:mark_field"}],
       "mapping": {"iri": "http://www.cidoc-crm.org/cidoc-crm/P130_shows_features_of"}
     }]
   }

The excerpt comes from the example profile of the repository, which
illustrates the specification with a generic case (the marks hand tools leave
on dressed stone, read as a species of the working unit, ``UL``). The
manifest is checked against a JSON schema and by the tests of the repository:
that every type specialises a core type that exists, that every type a rule
names is declared, that the vocabularies are there.

How to map your data and write em.json
--------------------------------------

The ontology (CRMem and the CIDOC CRM family) says what things *mean*; an
em.json file carries the **types of the EM language**. Bringing data into EM
is therefore a **mapping**: from the community's records to EM nodes, edges
and qualia — using the core types where they fit and the profile's types
where they do not.

The file is then written in one of two ways:

* **through s3Dgraphy**, the reference library, which every official tool
  uses to read and write the format (see the
  `s3dgraphy manual <https://docs.extendedmatrix.org/projects/s3dgraphy/en/v1.6/>`__);
* **with any other library** that passes the public **conformance suite** of
  the em.json specification: reading every file of the suite with the expected
  result, and writing back without losing what the specification describes.

A file that uses a profile **declares it in its header**, with the version it
was written with, and every node of a profile type names the core type it
specialises, so that a tool without the profile can fall back:

.. code-block:: json

   {"header": {
      "format": "em.json",
      "version": "1.1",
      "profiles": [{"iri": "https://example.org/em-profiles/example-toolmarks", "version": "0.1.0"}]
   }}

.. code-block:: json

   {"id": "mf1", "node_type": "tm:mark_field", "name": "MF1",
    "data": {"em_specializes": "UL"}}

A missing profile is never a reason to refuse a file.

How to contribute to the vocabularies
-------------------------------------

The repository `ExtendedMatrix/vocabularies
<https://github.com/ExtendedMatrix/vocabularies>`__ holds the SKOS modules
Extended Matrix originates, the cards of the external vocabularies it aligns
with, the alignments, and the profiles. Every module resolves under
``https://w3id.org/extendedmatrix/vocab/<module>/``. Contributions arrive as
pull requests and are reviewed by the curators of what they touch:

#. **Open an issue** to propose a module or a profile: say what you need to
   record and why no existing vocabulary covers it. If the term already lives
   in the Getty AAT, PeriodO or a national thesaurus, the module aligns with
   it instead of restating it.
#. **Send a pull request.** A module carries a version, a lifecycle state,
   curators and a licence (CC BY 4.0 unless there is a reason); every concept
   carries a label, a definition in your own words and its source. An
   alignment with another vocabulary stays *proposed* until somebody with
   standing in that vocabulary has verified it.
#. **After the merge** the module is published on the Extended Matrix site,
   with a header naming the commit it was published from.

How what you bring is versioned
-------------------------------

Three numbers, independent, never mixed:

* **the format** — ``header.version`` of em.json (1.1), which changes only
  with the form of the document;
* **the core** — the EM language and its datamodels
  (``header.datamodel_versions``), which change with the language;
* **each profile** — its own version, in semantic versioning, declared in
  the header of every file that uses it.

Updating a community's vocabulary or profile does not change the number of
the core or of the format; a tool that knows an older version of a profile
reads a file written with a newer one, falling back on what it does not know.
Each vocabulary module, too, has its own version and lifecycle.
