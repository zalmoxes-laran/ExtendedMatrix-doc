Ecosystem
=========

This page lists third-party tools that consume **s3dgraphy** (the Python
implementation of Extended Matrix) inside their own user-facing
workflow. It complements the *Extended Matrix Framework* tools that are
maintained inside the EM project itself — yEd palette, EM Tools for
Blender, 3D Survey Collection, Heriverse, and the s3dgraphy library
itself — by surfacing the *external* software that has chosen to ground
its archaeological data on the EM data model.

The list is intended for two audiences:

- **Researchers and practitioners** evaluating which of their existing
  tools already speaks EM, so that they can reuse a single graph across
  the recording, analysis, modelling, and publication phases of a
  project.
- **Developers and maintainers of consumer tools** who want a concrete
  reference of how others have approached the integration — vendoring
  strategy, projector logic, roundtrip story, version pinning — before
  adopting s3dgraphy in their own codebase.

This page is **version-agnostic**: it tracks the integration ecosystem
as a whole and is not pinned to a specific release of the EM formal
language.

Inclusion criteria
------------------

Listed integrations are not curated or endorsed beyond a few light
filters that make the list useful rather than aspirational:

- **Public, active repository.** The integration code is published
  under an OSI-approved licence and the upstream is maintained
  (commits, releases, or issue activity in the last twelve months).
- **Non-trivial s3dgraphy usage.** A meaningful integration — for
  example a *projector* that materialises an EM graph from native
  data, a roundtrip story (read/edit/write back), or a sustained
  consumer of the API beyond a one-off import script.
- **Declared maintenance.** A named maintainer or maintaining
  organisation, and a documented integration entry point (a docs page,
  a tutorial, or a README section) that explains *what* the
  integration does and *how* it is wired to s3dgraphy.

This is a soft filter, not gatekeeping: the goal is to keep the page
useful for newcomers, not to police who is allowed to integrate.

Listed integrations
-------------------

PyArchInit
~~~~~~~~~~

QGIS plugin for archaeological recording — a single environment for
stratigraphic, alphanumeric, multimedia and topographical data, used by
research groups and archaeological field operators since 2005.

:Maintained by: `Luca Mandolesi <https://github.com/pyarchinit>`__ &
   `Enzo Cocca <https://github.com/enzococca>`__ (s3dgraphy integration
   authored by Enzo Cocca).
:s3dgraphy support: 0.1.41, vendored under
   ``ext_libs/s3dgraphy``.
:Integration docs: `pyarchinit-api.readthedocs.io
   <https://pyarchinit-api.readthedocs.io/en/latest/>`__
:Repository: https://github.com/pyarchinit/pyarchinit
:Licence: GPL-2.0

PyArchInit consumes s3dgraphy to bridge the QGIS-side stratigraphic
recording with the Extended Matrix data model: stratigraphic units,
relationships, and selected paradata authored in PyArchInit can be
projected onto a s3dgraphy graph and exchanged with the rest of the
Extended Matrix Framework. The integration was first announced as
issue `#5
<https://github.com/zalmoxes-laran/s3dgraphy/issues/5>`__ on the
s3dgraphy repository.

How to be listed
----------------

Maintainers of consumer tools that want to be added to this page are
invited to open an issue on the
`s3dgraphy issue tracker
<https://github.com/zalmoxes-laran/s3dgraphy/issues>`__ with a short
*integration story* covering:

- the tool's name, repository URL and licence;
- a one-line description of what the tool does;
- the version of s3dgraphy currently consumed and the vendoring or
  dependency strategy (pip dependency, vendored copy, fork);
- a pointer to the integration documentation (README section, manual
  page, or tutorial);
- the maintainer name and contact (preferably a GitHub handle).

The s3dgraphy maintainers will review the request, confirm that the
soft inclusion criteria are met, and add the entry on this page in a
subsequent documentation release.
