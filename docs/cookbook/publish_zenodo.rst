.. _publish-zenodo:

Publishing your EM dataset to Zenodo
====================================

`Zenodo <https://zenodo.org/>`_ is a general-purpose research data
repository operated by CERN, supporting versioned datasets with
persistent DOIs (Digital Object Identifiers). It's the canonical
publication path for Extended Matrix-based reconstructive datasets
that need to be cited, archived, and made openly accessible.

This recipe sketches the workflow and the caveats. The page will be
extended with a worked example (the Great Temple of Sarmizegetusa
project, currently in preparation) as soon as that publication goes
live.

ORCID — get one first
---------------------

Before publishing anything on Zenodo, get an `ORCID iD
<https://orcid.org/>`_ if you don't have one. ORCID is a persistent
researcher identifier that links your publications, datasets, and
software contributions across platforms. Zenodo integrates with ORCID
natively. Beyond Zenodo, the ORCID iD is recommended throughout the
Extended Matrix ecosystem as the canonical author identifier — it
makes paradata authorship traceable when projects are forked, merged,
or shared across teams.

What a DOI gives you
--------------------

When you publish a deposit on Zenodo, the platform mints a DOI that
points uniquely and permanently to that specific version of your
dataset. The DOI:

- Survives institutional or project domain changes.
- Lets others cite the exact dataset you published, not a moving
  target.
- Is indexed by scholarly search engines and citation databases.
- Allows reuse under the license you assign (CC-BY, CC0, etc.).

In practice, a DOI'd dataset is a real publication. Treat it like
one when you prepare it: clear authorship, clear license, clear
description, complete files.

Rights — verify before publishing
---------------------------------

Before publishing anything in your DosCo or any other EM artefact,
you must be certain you have the right to publish each individual
item. This is the most error-prone part of the workflow.

Particular attention to:

- **Extractor nodes and their attached media** are usually intellectual
  property of the authors of the extracting work — they are derivative
  works (an annotation, a quotation, a measurement) layered on top
  of an original source. The authors of the extractor (you, your
  team, third-party collaborators) hold rights on the *extraction*;
  the underlying source may belong to someone else. Verify case by
  case.
- **Original sources** (historical photographs, archival documents,
  archaeological survey deliverables, prior publications) may carry
  separate copyrights. Some are in the public domain; others require
  permission to redistribute.
- **3D survey models** may belong to the surveying team or to the
  contracting institution — not automatically to you.
- **Reconstructive proxies and representation models** you authored
  in EM Tools are your own work and are publishable under your
  chosen license, unless they incorporate textures or geometries
  with third-party rights.

When in doubt about a single document or media file in your DosCo:
**do not include it in the Zenodo deposit**. Instead, publish a
pointer (URL, archive reference, or bibliographic citation) to the
document where it lives online, and let the graph reference that
pointer rather than carrying the file.

Folder structure inside the deposit
-----------------------------------

Use the canonical Extended Matrix folder structure inside your
Zenodo deposit. The same tree that organises your local workspace
(``DosCo/``, ``matrix/``, ``model/``, ``source_list.xlsx``, etc. —
see :doc:`/em_workspace_preparation`) carries to the deposit. This
makes the dataset legible to anyone familiar with EM, and lets
downstream tools (custom mappers, future bulk-import scripts)
parse the deposit without bespoke unpacking logic.

Versioning
----------

Zenodo supports versioned deposits: when your dataset evolves (new
data, corrections, fresh interpretations), you publish a new version
with its own DOI under the same conceptual identifier. The
*conceptual DOI* points to the latest version; each version DOI
points to that specific snapshot.

Plan your versioning strategy at the start:

- **v1.0.0** at first publication, even if the work continues.
- Bump the version for substantive changes that affect the
  reconstruction or the evidence base.
- Use the Zenodo description field to summarise what changed
  between versions.

Immutability — once published, the files cannot be deleted
----------------------------------------------------------

Zenodo applies a SHA digital signature to every published file. Once
a version is live, **the files are immutable**: they cannot be
deleted, edited, or replaced. You can publish a new version of the
deposit, but the previous version's files remain available at their
original DOI.

This is a feature, not a limitation — it's the foundation of
citability. But it also means:

- Sensitive or rights-questionable files must not be in the deposit
  in the first place (see Rights, above).
- Personal data, anything that could violate GDPR if revealed, must
  be filtered out before upload.
- Pre-publication review (by you, your co-authors, your institution)
  must happen before the "publish" button is pressed.

Treat the deposit pre-upload as you would treat a journal manuscript
proof: assume everything you put in is going to be permanent.

Worked example
--------------

The first published Extended Matrix dataset under this workflow will
be the *Great Temple of Sarmizegetusa* project — currently in
preparation. This section will be expanded with the concrete deposit
metadata, file inventory, and lessons learned as soon as that
publication goes live.

Future direction
----------------

A direct exporter from EM Tools to a Zenodo-ready deposit bundle
is on the development tracker (see the `development projects
<https://dev.extendedmatrix.org/dev-projects/>`_ for status). Until
that ships, the upload to Zenodo is a manual operation: prepare the
folder, zip if needed, upload via the Zenodo web interface, fill
in the metadata, attach the ORCID, set the license, mint the DOI.
